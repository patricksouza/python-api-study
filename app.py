
from itertools import count
from typing import Optional

from flask import Flask, request, jsonify
from flask_pydantic_spec import (
    FlaskPydanticSpec, Response, Request
)

from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='API RESTFUL PYTHON')
spec.register(server)

database = TinyDB(storage=MemoryStorage)

counter = count()

"""Definindo o MODELO esperado"""


class DBValue(BaseModel):
    id: Optional[int]
    name: Optional[str]
    age: Optional[int]


class DBSingleValueModel(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(counter))
    name: str
    age: int


class DBMultiValuesModel(BaseModel):
    values: list[DBSingleValueModel]
    valueCount: int


"""Definindo as rotas(endpoints, recursos...)"""


@server.get('/values')
@spec.validate(
    query=DBValue,
    resp=Response(HTTP_200=DBMultiValuesModel)
)
def QueryAllDBValues():
    query = request.context.query.dict(exclude_none=True)
    allQueryValues = database.search(Query().fragment(query))
    return jsonify(
        DBMultiValuesModel(
            values=allQueryValues,
            valueCount=len(allQueryValues)
        ).dict()
    )

@server.post('/values')
@spec.validate(
    body=Request(DBValue),
    resp=Response(HTTP_201=DBValue)
)
def InsertDBValue():
    request_body = request.context.body.dict()
    database.insert(request_body)
    return request_body

server.run()
