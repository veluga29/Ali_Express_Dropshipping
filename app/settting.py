import os

API_KEY = os.getenv('AED_ZAPIEX_API_KEY', '')
DB_HOST = os.getenv('AED_DB_HOST', 'localhost')
DB_PORT = os.getenv('AED_DB_PORT', '')
DB_USER_NAME = os.getenv('AED_DB_USER_NAME', '')
DB_USER_PASSWORD = os.getenv('AED_DB_PASSWORD', '')
DB_NAME = os.getenv('AED_DB_NAME', '')

DATABASE_URL = f"postgres://{DB_USER_NAME}:" \
    f"{DB_USER_PASSWORD}" \
    f"@{DB_HOST}" \
    f":{DB_PORT}" \
    f"/{DB_NAME}"