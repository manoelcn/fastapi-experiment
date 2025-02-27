# FastAPI Cars API

Uma API simples para gerenciar informações de carros, construída com FastAPI.

## Descrição

Este projeto é uma API RESTful desenvolvida com FastAPI que permite consultar informações sobre carros. Foi criado com o objetivo de aprender e explorar os recursos do framework FastAPI.

## Funcionalidades

- Listagem de todos os carros disponíveis
- Consulta de informações detalhadas de um carro específico por ID

## Rotas Disponíveis

- `GET /`: Mensagem de boas-vindas
- `GET /cars`: Retorna a lista completa de carros
- `GET /cars/{car_id}`: Retorna informações de um carro específico pelo ID

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- Python

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/fastapi-cars-api.git
   cd fastapi-cars-api
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

Para iniciar o servidor:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação da API

A documentação interativa da API estará disponível em:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
