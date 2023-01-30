import logging
from os import environ, path


def set_up():
    """Sets up configuration for the app"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception as error:
        logging.error(error)

    config = {
        "DEBUG": bool(environ.get("DEBUG", 1)),
        "ENVIRONMENT": environ.get("ENVIRONMENT", ""),
        "MYSQL_DATABASE_URL": environ.get("MYSQL_DATABASE_URL", "sqlite:///./sql_app.db"),
        "NOSQL_DATABASE_URL": environ.get("NOSQL_DATABASE_URL"),
        "SECRET_KEY": environ.get("SECRET_KEY", "LinuxProfile"),
        "SENTRY_DSN": environ.get("SENTRY_DSN"),
        "BASE_DIR": path.abspath(path.dirname(__file__))
    }
    return config
