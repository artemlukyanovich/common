import os


class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "lesson17hw"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "lesson17hw_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    PG_USER = "lesson17hw"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "lesson17hw_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


def get_config(env):
    return configs.get(env)


configs = {
    "TEST": TestConfig,
    "DEFAULT": Config
}


# def run_config():
#     env = os.environ.get("ENV")
#     if env == "TEST":
#         return TestConfig
#     else:
#         return Config

