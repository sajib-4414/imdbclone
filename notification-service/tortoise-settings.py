TORTOISE_ORM = {
    "connections": {
        "default": "asyncpg://root:root@notification-db:5432/notification_db",
    },
    "apps": {
        "models": {"models": ["app.db", "aerich.models"], "default_connection": "default"},
    },
}