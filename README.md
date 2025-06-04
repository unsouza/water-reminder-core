# Water Reminder

Aplicativo para registrar o consumo diário de água.

## Como rodar a aplicação

1. **Suba os containers com Docker**  
   No terminal, execute:

   ```bash
   docker compose up -d
   ```

2. **Acesse o container da aplicação**

   ```bash
   docker compose exec app bash
   ```

3. **Inicie o servidor FastAPI**

   ```bash
   fastapi dev run.py --host 0.0.0.0
   ```

## Tecnologias utilizadas

- **Python** – Linguagem de programação principal da aplicação.
- **FastAPI** – Framework moderno e performático para construção de APIs em Python.
- **Docker** – Ferramenta de containerização usada para facilitar a execução do projeto.
- **Masonite ORM** – ORM (Object-Relational Mapper) simples e intuitivo para interagir com o banco de dados usando Python.