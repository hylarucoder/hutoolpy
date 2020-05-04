import datetime

from sqlalchemy import create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from prevenger.kit.meta_kit import classproperty


def get_current_time():
    return datetime.datetime.now()


class BaseModel(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, default=get_current_time, onupdate=get_current_time)

    @classproperty
    def query(cls):
        return cls._session.query(cls)


Model: BaseModel = declarative_base(cls=BaseModel)
