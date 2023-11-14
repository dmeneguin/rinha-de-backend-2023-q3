from sqlalchemy import Column, String, Date, ARRAY
from configs.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class PersonModel(Base):
    __tablename__ = "persons"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    apelido = Column(String, unique=True, index=True)
    nome = Column(String)
    nascimento = Column(Date)
    stack = Column(ARRAY(String),nullable=True)
    concatenado = Column(String, index=True)
