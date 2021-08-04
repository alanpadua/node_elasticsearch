# Ambiente

Verificar vessões 

**Node:**
```
    node -v
    v14.17.3
```

**NPM:**
```
    npm -v
    6.14.13
```

**Yarn:**
```
    npm install -g yarn
```

# Criação Projeto

## Criação
```
    yarn init -y
```

## Instala Libs
```
    yarn add typescript ts-node-dev -D
    yarn add express -D
    yarn @types/express -D
    yarn add @types/express -D
    yarn add @types/elasticsearch -D
    yarn add elasticsearch -D

    yarn add pg
    yarn add @types/pg -D
```

## Criar o arquivo typescript tsconfig.json
```
    yarn tsc --init
```

## Criar volumes Docker
```docker
    docker volume create ELASTIC_SEARCH_DATA
    docker volume create PGDATA_POSGRES
```

# Iniciar projeto

Subir na porta : **3333**
```
    yarn dev
```

**Iniciar a infraestrutura:**
```
    yarn infra-up
```

ou na pasta docker 
```
    docker-compose  up -d
```

**Parar a infraestrutura:**
```
    yarn infra-down
```
ou na pasta docker 
```
    docker-compose down
```

**Trecho package.json:**
```yaml
"scripts": {
    "dev": "ts-node-dev src/server.ts",
    "infra-up": "docker-compose -f docker/docker-compose.yml up -d",
    "infra-down": "docker-compose -f docker/docker-compose.yml down"
},
```

## URL Locais

 - [Localhost:5601 - Kibana](http://localhost:5601/)
 - [Localhost:9200 - Elasticsearch](http://localhost:9200/)
 - [Localhost:3333 - Project](http://localhost:3333/)

## Links referencia

 - [Yarn Install](https://yarnpkg.com/cli/install)
 - [Elastic Search API](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/api-reference.html)
 - [Elastic Search API Javascript](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/examples.html)

 ## 🗂 Material de apoio

- [Elasticsearch e Kibana](https://www.elastic.co/pt/elastic-stack)
- [Elasticsearch para NodeJS](https://www.npmjs.com/package/elasticsearch)
- [API do Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/16.x/api-reference.html)
- [Dataset de Imagens](http://www.imageprocessingplace.com/root_files_V3/image_databases.htm)
- [Imagens Repositório](https://www.kaggle.com/prondeau/the-car-connection-picture-dataset)
