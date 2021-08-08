from configparser import ConfigParser
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

environment = environ["APP_ENV"]
config = ConfigParser()
config.read(f"config-{environment}.ini")
username = config.get("database", "username")
password = config.get("database", "password")
database_name = config.get("database", "database-name")
database_hostname = config.get("database", "hostname")
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{database_hostname}/{database_name}"
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
