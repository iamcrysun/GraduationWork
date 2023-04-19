import os
from dataclasses import dataclass

import yaml
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from server.configs.config import CONFIGS_PATH, ENVS_PATH


@dataclass(slots=True, frozen=True)
class DBConfig:
    host: str
    port: str
    name: str


@dataclass(slots=True, frozen=True)
class DBLogin:
    user: str
    password: str


def read_database_config_from(file: str) -> DBConfig:
    with open(file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            config = DBConfig(**config)

            return config
        except yaml.YAMLError as exc:
            print(exc)


db_config = read_database_config_from(os.path.join(CONFIGS_PATH, "db.yaml"))
login_db_config = DBLogin(**dotenv_values(os.path.join(ENVS_PATH, ".db")))

connection_string = f'postgresql://{login_db_config.user}:{login_db_config.password}' \
                    f'@{db_config.host}:{db_config.port}/{db_config.name}'

engine = create_engine(connection_string)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
