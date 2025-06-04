# Water Reminder

Aplicativo para registrar o consumo diário de água.

## Como rodar a aplicação

1. **No terminal, execute:**  
   ```
   docker compose up -d
   ```

## Documentação da API

A API está disponível em `http://127.0.0.1:8000` e oferece os seguintes endpoints:

### Usuários

#### Criar Usuário
```http
POST /users
```

**Body:**
```json
{
    "name": "string",
    "weight": float
}
```

**Resposta:**
```json
{
    "id": integer,
    "name": "string",
    "weight": float,
    "created_at": "datetime",
    "updated_at": "datetime"
}
```

#### Buscar Usuário
```http
GET /users/me
```

**Headers:**
- `X-User-Id`: ID do usuário (integer)

**Resposta:**
```json
{
    "id": integer,
    "name": "string",
    "weight": float,
    "created_at": "datetime",
    "updated_at": "datetime"
}
```

### Histórico de Consumo

#### Registrar Consumo
```http
POST /histories
```

**Headers:**
- `X-User-Id`: ID do usuário (integer)

**Body:**
```json
{
    "ml": integer
}
```

**Resposta:**
```json
{
    "id": integer,
    "ml": integer,
    "user_id": integer,
    "created_at": "datetime",
    "updated_at": "datetime"
}
```

#### Consultar Consumo Diário
```http
GET /histories/consumed
```

**Headers:**
- `X-User-Id`: ID do usuário (integer)

**Resposta:**
```json
{
    "total_consumed": integer
}
```

#### Consultar Histórico de Consumo
```http
GET /histories/history
```

**Headers:**
- `X-User-Id`: ID do usuário (integer)

**Resposta:**
```json
[
    {
        "date": "YYYY-MM-DD",
        "total_ml": integer
    }
]
```

## Tecnologias utilizadas

- **Python** – Linguagem de programação principal da aplicação.
- **FastAPI** – Framework moderno e performático para construção de APIs em Python.
- **Docker** – Ferramenta de containerização usada para facilitar a execução do projeto.
- **Masonite ORM** – ORM (Object-Relational Mapper) simples e intuitivo para interagir com o banco de dados usando Python.