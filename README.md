# Jogoteca

[Versão 2.0](https://hub.docker.com/repository/docker/dansolo7/jogoteca/tags?page=1)

### Setup

#### Dependencias

Instale o [docker](https://docs.docker.com/engine/install/) e o
[docker-composer](https://docs.docker.com/compose/install/)

Crie um docker network do tipo overlay chamada `backend` antes de subir o projeto.

Obs: Vai precisar iniciar o `docker swarm`

***Exporte as seguintes variaveis de ambiente no seu sistema:***
```
MYSQL_HOST='mysql' # Nome do serviço do banco na rede overlay do docker
MYSQL_USER='nome do usuario do banco'
MYSQL_PASSWORD='senha do usuario do banco'
MYSQL_DB='jogoteca' # Database por padrao tem o nome de jogoteca
```

***docker-compose -f docker-compose.yml up***

# Sobre
Aplicação de uma biblioteca de jogos em [Flask](https://flask.palletsprojects.com/en/1.1.x/). O front-end bem simples
com HTML, CSS e JavaScript.

***Features:***

Registro e adição de jogos com `nome`,`categoria` e `plataforma` e uma imagem como capa do jogo;

Cadastro de usuários. Utilização da biblioteca [passlib](https://passlib.readthedocs.io/en/stable/)
para criptografia `sha-256` das senhas dos usuarios no banco de dados.

## Camada Docker

Aplicação dockerizada com a imagem [python:3.8-slim](https://hub.docker.com/_/python)

O banco de dados utilizando a imagem pura do [MySQL](https://hub.docker.com/_/mysql)


### Projeto:

```
.
├── app
│   ├── config.py
│   ├── dao.py
│   ├── helpers.py
│   ├── jogoteca.py
│   ├── migrations
│   │   ├── prepara_banco_manual.py
│   │   └── prepara_banco.py
│   ├── models.py
│   ├── static
│   │   ├── app.css
│   │   ├── app.js
│   │   ├── bootstrap.css
│   │   └── jquery.js
│   ├── templates
│   │   ├── cadastro.html
│   │   ├── criar.html
│   │   ├── editar.html
│   │   ├── lista.html
│   │   ├── login.html
│   │   └── template.html
│   ├── uploads
│   │   ├── capa1-1589304859.864615.jpg
│   │   └── capa_padrao.jpg
│   └── views.py
├── docker-compose.yml
├── docker-entrypoint.sh
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
└── valida-conexao-db.py
```
