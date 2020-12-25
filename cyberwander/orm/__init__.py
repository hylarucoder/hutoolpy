import datetime

from sqlalchemy import DateTime, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from cyberwander.decorators import classproperty


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
