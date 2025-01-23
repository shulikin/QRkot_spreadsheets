import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

from pydantic import (
    BaseSettings,
    EmailStr
)


class Constant:
    """Класс для хранения различных констант."""

    DEFAULT_INVESTED = 0
    NAME_MAX_LEN = 100
    NAME_MIN_LEN = 1
    BASE_DIR = Path(__file__).parent
    LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
    DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
    VALUE_INPUT_OPTION_USER_ENTERED = 'USER_ENTERED'
    SHEET_ID = 0
    DRIVE_API_NAME = 'drive'
    DRIVE_API_VERSION = 'v3'
    SHEETS_API_TYPE = 'GRID'
    SHEET_TITLE_TEMPLATE = 'Отчёт на {date}'
    SHEET_LOCALE = 'ru_RU'
    SHEET_NAME = 'Лист1'
    SHEETS_API_NAME = 'sheets'
    SHEETS_API_VERSION = 'v4'
    SHEET_GRID_PROPERTIES = {'rowCount': 100, 'columnCount': 11}
    SPREADSHEET_RANGE = 'A1:D100'
    PERMISSION_ROLE = 'writer'
    PERMISSION_TYPE = 'user'
    MAJOR_DIMENSION_ROWS = 'ROWS'
    TOKEN_EXPIRATION_DATE = 3600
    MIN_PASSWORD_LENGTH = 3
    DOCS_GOOGL_URL = 'https://docs.google.com/spreadsheets/d/'
    RETURNED_NULL = 0

    # Шаблон таблицы
    TABLE_TEMPLATE = [
        ['Отчет', '{date}'],
        ['Топ проектов'],
        ['Название проекта', 'Время сбора', 'Описание'],
    ]


class Settings(BaseSettings):
    """Класс конфигурации."""

    app_title: str = 'Благотворительный фонд QRKot'
    app_description: str = 'Фонд собирает пожертвования на целевые проекты'
    database_url: str = 'sqlite+aiosqlite:///./qrkot.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None
    admin_email: Optional[str] = None
    format = Constant.DATETIME_FORMAT

    class Config:
        """Класс конфигурации '.env'."""

        env_file = '.env'


settings = Settings()


def configure_logging():
    """Функция настройки логирования."""
    log_dir = Constant.BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'qrkot.log'
    rotating_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 ** 6,
        backupCount=5
    )
    logging.basicConfig(
        datefmt=Constant.DATETIME_FORMAT,
        format=Constant.LOG_FORMAT,
        level=logging.INFO,
        handlers=(
            rotating_handler,
            logging.StreamHandler()
        )
    )
