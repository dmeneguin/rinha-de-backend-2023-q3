from pydantic import BaseModel,field_validator, StringConstraints
from typing_extensions import Annotated
from datetime import date,datetime
from typing import Union

class Person(BaseModel):
    apelido: Annotated[str,StringConstraints(max_length=32)]
    nome: Annotated[str, StringConstraints(max_length=100)]
    nascimento: date
    stack: Union[list[Annotated[str, StringConstraints(max_length=32)]], None]

    @field_validator('nascimento', mode='before')
    @classmethod
    def check_date_format(cls, d: str) -> date:
        return datetime.strptime(d, "%Y-%m-%d").date()