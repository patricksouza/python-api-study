# COMANDOS USADOS

1. poetry init -n
2. poetry add flask ou pip install flask
3. poetry add httpie ou pip install httpie
4. poetry add flask-pydantic-spec ou pip install flask-pydantic-spec (swagger/OpenAPI)
5. poetry add tinydb ou pip install tinydb


## COMANDOS PARA RODAR

poetry shell
flask run
flask run --no-debugger --no-reload



## COMANDOS PARA CHECAR OS ENDPOINTS

http get http://127.0.0.1:5000/values
http post http://127.0.0.1:5000/values age=2 name=Carlos


## Links importantes

### Gerenciando envs
https://python-poetry.org/docs/managing-environments/


### Mudar interpretador
https://stackoverflow.com/questions/71229685/packages-installed-with-poetry-fail-to-import