from schemas.person import PersonSchema
from configs.database import (get_db_connection)
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.person import PersonModel
import uuid
from typing import List
from psycopg2 import errors

class PersonService:
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db
    
    def create(self, person: PersonSchema) -> uuid.UUID:
        # persons_already_registered = self.db.query(PersonModel).filter(PersonModel.apelido == person.apelido).limit(1).all()
        # if len(persons_already_registered) > 0:
        #     raise HTTPException(status_code=422,detail="Uma pessoa com esse apelido já existe")
        person_id = uuid.uuid4()
        stack = ','.join(person.stack) if person.stack else ''
        person_model = PersonModel(
            id=person_id, 
            apelido=person.apelido,
            nome=person.nome,
            nascimento=person.nascimento,
            stack=person.stack,
            concatenado = ','.join([person.nome,person.apelido,stack])
        )
        try:
            self.db.add(person_model)
            self.db.commit()
            #self.db.refresh(person_model)
        except IntegrityError as err:
            assert isinstance(err.orig, errors.UniqueViolation)
            raise HTTPException(status_code=422,detail="Uma pessoa com esse apelido já existe")
        return person_id
    
    def get_by_id(self, uuid: uuid.UUID) -> PersonModel:
        return self.db.query(PersonModel).filter(PersonModel.id == uuid).first()
    
    def get(self, query: str) -> List[PersonModel]:
        print(query)
        return self.db.query(PersonModel).filter(PersonModel.concatenado.like(f"%{query}%")).limit(50).all()
    
    def count(self) -> int:
        return self.db.query(PersonModel.id).count()