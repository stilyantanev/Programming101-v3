from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    balance = Column(Float, default=0)


class TanCode(Base):
    __tablename__ = "tancodes"
    id = Column(Integer, primary_key=True)
    tan_code = Column(String)
    is_used = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))
    clients = relationship(Client, backref="tan_codes")
