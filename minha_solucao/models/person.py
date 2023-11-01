from sqlalchemy import Column, Integer, String, Date, ARRAY
from ..database import Base

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    apelido = Column(String, unique=True)
    nome = Column(String)
    nascimento = Column(Date)
    stack = Column(ARRAY(Integer),nullable=True)
