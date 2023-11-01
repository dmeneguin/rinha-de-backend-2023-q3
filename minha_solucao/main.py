from typing import Union
from fastapi import FastAPI
from schemas.person import Person

app = FastAPI()

@app.post("/pessoas")
def register_person(person: Person):
    return {"method":f"register person {person}"}

@app.get("/pessoas/{person_id}")
def get_person(person_id: int):
    return {"method":f"get person by id {person_id}"}

@app.get("/pessoas")
def get_person(t: Union[str, None] = None):
    return {"method":f"query persons by {t}"}

@app.get("/contagem-pessoas")
def count_person():
    return {"method":"count person"}