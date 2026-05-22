import os

def get_current_version() -> str:
    current_version: str = str(os.getenv('APP_VERSION'))
    return current_version