from os import environ, path


def set_up():
    """Sets up configuration for the app"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

    config = {
        "DEBUG": bool(environ.get("DEBUG", 1)),
        "ENVIRONMENT": environ.get("ENVIRONMENT", ""),
        "DATABASE_URL": environ.get("DATABASE_URL", "sqlite:///./sql_app.db"),
        "SECRET_KEY": environ.get("SECRET_KEY", "LinuxProfile"),
        "BASE_DIR": path.abspath(path.dirname(__file__))
    }
    return config
