from dotenv import dotenv_values
from masoniteorm.connections import ConnectionResolver

config = dotenv_values(".env")

DATABASES = {
    "default": "postgres",
    "postgres": {
        "port": 5432,
        "user": "default",
        "host": config.get("DB_HOST", "localhost"),
        "driver": "postgres",
        "password": "secret",
        "log_queries": False,
        "database": "default",
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)
