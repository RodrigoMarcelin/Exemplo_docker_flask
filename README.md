# Implementação de docker com flask e postgres
## Guia de instalação:
### Clonando rep:

para clonar o repositório adicione o seguinte coando no terminal:
```
git clone https://github.com/RodrigoMarcelin/exemplo_docker_flask.git
```
### Executando o container:
entre na pasta do projeto pelo terminal, e insira o comando 
```
docker-compose up -d
```
testar o aplicativo em:

```
localhost:5000
```
## Funcionamento:
### Estrutura do projeto:
O projeto é dividido em três partes, templates HTML, app Python, banco de dados Postgres, 
a camada template e o app python são executados em um container e o banco de dados é executado em outro.

A imagem a seguir representa a estrutura do progeto:

![](https://github.com/RodrigoMarcelin/exemplo_docker_flask/blob/master/imagens/estrutura_do_projeto.jpeg)

### Docker File:
Docker file é o servidor flask, onde é utilizado a imagem flask-crud-base, onde é criada a pasta que ficarão os arquivos do projeto "./app /home/app/",
definido a porta de execução "5000", e entrypoint para definir o tipo de execução do processo

```
FROM fanoftal2/flask-crud-base:1

ADD ./app /home/app/
WORKDIR /home/app/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
```
### Docker-compose:
O docker-compose permite criar conteiners, para funcionar na mesma rede e possui relações entre si, no caso desse projeto são criads dois serviços web e db,
onde o web só executa após a criação do db e são defidas as portas e diretórios com volumes.

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
    expose:
      - 5432
```

