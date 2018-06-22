# restapi-facebook
## Rest API Facebook Test

Pequeno script para teste da api do facebook utilizando python3 com flask e SQLAlchemy.

### Instalação:
```shell
    pip install -r requirements.txt
```
### Utilização:

  Após instalar as dependências, insira seu token do facebook api em
  **app/config.py**:

  ```python
    #Facebook token
    facebook_token = "TOKEN"
  ```

  Inicie o servidor:

  ```shell
   python server.py
  ```

O serviço estará disponível na porta 5000 (http://localhost:5000)

### Utlizando a API:

#### Inclusão de um usuário:

```shell
curl -X POST ­-F facebookId=670286562 http://localhost:5000/person/
```
Resposta: HTTP 201

#### Listagem do usuários:

```shell
curl http://localhost:5000/person/?limit=10
```
Resposta: HTTP 200

#### Remover usuário:

```shell
curl -X DELETE http://localhost:xxxx/person/670286562/
```

Resposta: HTTP 204
