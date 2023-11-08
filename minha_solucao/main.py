from typing import Union
from fastapi import FastAPI, Depends, Response, status
from schemas.person import PersonSchema
from services.person import PersonService
from uuid import UUID

app = FastAPI()

@app.post("/pessoas", status_code=status.HTTP_201_CREATED)
def register_person(person: PersonSchema, response: Response, person_service: PersonService = Depends()):
    created_person = person_service.create(person)
    response.headers["Location"] = f"/pessoas/{created_person.id}"
    return created_person

@app.get("/pessoas/{person_id}")
def get_person(person_id: UUID, person_service: PersonService = Depends()):
    return person_service.get_by_id(person_id)

@app.get("/pessoas")
def get_person(t: Union[str, None] = None, person_service: PersonService = Depends()):
    return person_service.get(t)

@app.get("/contagem-pessoas")
def count_person(person_service: PersonService = Depends()):
    return person_service.count()