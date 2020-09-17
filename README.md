# Projeto base para projetos que utilizam Docker com imagens Postgres e Flask

### Desenvolvedores
* [Rodrigo Marcelino](https://github.com/RodrigoMarcelin)
* [Matheus Santos](https://github.com/matheuscosantos)
* [Yasmin Araujo](https://github.com/yasminaraujoarantes)

## Introdução

Nesse repositório foi desenvolvido uma build base em containers Docker para projetos que utilizam o framework Flask e o sistema gerenciador de banco de dados Postgres.

## Guia de instalação:
### Clonando o repositório:

Para clonar o repositório adicione o seguinte comando no terminal:
```
git clone https://github.com/RodrigoMarcelin/exemplo_docker_flask.git
```

### Executando o container:
Entre na pasta do projeto pelo terminal e insira o comando: 
```
docker-compose up -d
```
Para verificar se os containers estão em execução:

```
docker ps
```
Para acessar a aplicação no navegador:

```
http://localhost:5000
```
## Estrutura do projeto:

O projeto é dividido em três partes, templates para os arquivos HTML, aplicação Flask e banco de dados Postgres, a camada template e o app python são executados em um container chamado "web" e o banco de dados é executado no container chamado "bd"

A imagem a seguir representa a estrutura do projeto:

![](https://github.com/RodrigoMarcelin/exemplo_docker_flask/blob/master/imagens/estrutura_do_projeto.jpeg)

### Docker File:
Dockerfile contem a base para a aplicação em flask, onde são definidos:

* Imagem utilizada: flask-crud-base,
* Criação e pastas: /app e /home/app,
* Porta para exposição da aplicação: 5000
* Forma de instruções: Python 3

Exemplo:

```
FROM fanoftal2/flask-crud-base:1

ADD ./app /home/app/
WORKDIR /home/app/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
```
### Docker-compose:
O docker-compose permite criar grupos de conteiners, que funcionam na mesma rede e possui relações entre si, no caso desse projeto são criados dois serviços, "web" e "db".

As instruções definidas no docker-compose são:
1. WEB
* A base da aplicação é: .
* Portas de rede espelhadas do container e do SO: 5000:5000
* Diretórios espelhados do container e do SO: ./app/:/home/app


2. DB
* A imagens utilizada é: postgres:10
* As variáveis de ambiente estão em: .env
* Porta exposta é: 5432

Exemplo:

```
version: "3"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app/:/home/app/
    depends_on:
      - db
  db:
    image: postgres:10
    env_file: .env
    ports:
      - "5432:5432"
    volumes:
      - /docker/volumes/postgres:/var/lib/postgresql/data
```

[Link para o repositório](https://github.com/RodrigoMarcelin/exemplo_docker_flask)