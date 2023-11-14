from fastapi import FastAPI, Depends, Response, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from schemas.person import PersonSchema
from services.person import PersonService
from uuid import UUID
# from configs.database import Base, engine
# import os

# if os.environ['API_ID'] == 'api1':
#     Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    input_obj = exc.errors()[0]['input']
    if not input_obj:
        return PlainTextResponse(str(input_obj), status_code=422)
    else:
        return PlainTextResponse(str(input_obj), status_code=400)

@app.post("/pessoas", status_code=status.HTTP_201_CREATED)
def register_person(person: PersonSchema, response: Response, person_service: PersonService = Depends()):
    person_id = person_service.create(person)
    response.headers["Location"] = f"/pessoas/{person_id}"
    return

@app.get("/pessoas")
def get_person(t: str | None= None, person_service: PersonService = Depends()):
    if not t:
        raise HTTPException(status_code=400,detail="t é um parâmetro obrigatório")
    return person_service.get(t)

@app.get("/pessoas/{person_id}")
def get_person(person_id: UUID, person_service: PersonService = Depends()):
    return person_service.get_by_id(person_id)

@app.get("/contagem-pessoas")
def count_person(person_service: PersonService = Depends()):
    return person_service.count()