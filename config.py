import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask 基础
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    # 数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "shared_luggage.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 调试
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
