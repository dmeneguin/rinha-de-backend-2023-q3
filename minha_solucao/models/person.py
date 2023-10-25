from pydantic import BaseModel,field_validator
from datetime import date,datetime
from typing import Union

class Person(BaseModel):
    apelido: str
    nome: str
    nascimento: date
    stack: Union[list[str], None]

    @field_validator('nascimento', mode='before')
    @classmethod
    def check_date_format(cls, d: str) -> date:
        return datetime.strptime(d, "%Y-%m-%d").date()