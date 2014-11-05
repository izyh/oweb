
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "cdcee9db-0af6-487a-85b6-5aeeffa2ca8eb80f5d1f-5637-49fe-97fc-7abb050083f55178c939-b8fa-4983-a2bf-8636c737ab44"
NEVERCACHE_KEY = "15c7b70b-9d57-4861-b6c6-8c27b16c650ac345b268-8737-49b0-97ac-524a539761f2d5fe261d-cbd7-4a7e-94df-5e0e3a79e461"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
