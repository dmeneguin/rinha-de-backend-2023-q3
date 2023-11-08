from schemas.person import PersonSchema
from configs.database import (get_db_connection)
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.person import PersonModel
from uuid import UUID
from typing import List

class PersonService:
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db
    
    def create(self, person: PersonSchema) -> PersonModel:
        persons_already_registered = self.db.query(PersonModel).filter(PersonModel.apelido == person.apelido).limit(1).all()
        if len(persons_already_registered) > 0:
            raise HTTPException(status_code=422,detail="Uma pessoa com esse apelido já existe")
        person_model = PersonModel(
            apelido=person.apelido,
            nome=person.nome,
            nascimento=person.nascimento,
            stack=person.stack,
            concatenado = person.nome + ',' + person.apelido + ',' + ','.join(person.stack)
        )
        self.db.add(person_model)
        self.db.commit()
        self.db.refresh(person_model)
        return person_model
    
    def get_by_id(self, uuid: UUID) -> PersonModel:
        return self.db.query(PersonModel).filter(PersonModel.id == uuid).first()
    
    def get(self, query: str) -> List[PersonModel]:
        print(query)
        return self.db.query(PersonModel).filter(PersonModel.concatenado.like(f"%{query}%")).limit(50).all()
    
    def count(self) -> int:
        return self.db.query(PersonModel.id).count()