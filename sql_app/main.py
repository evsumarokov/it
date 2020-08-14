from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/projects/", response_model=schemas.Project)
def create_project(
    project: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    return crud.create_project(db=db, project=project)

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(
    project: schemas.Project,
    db: Session = Depends(get_db)
):
    project_id :int = project.id
    return crud.update_project(db=db, project_id=project_id, project=project)

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.get("/projects/", response_model=List[schemas.Project])
def list_projects(db: Session = Depends(get_db)):
    db_projects = crud.list_projects(db)
    
    return db_projects

@app.post("/vacancies/", response_model=schemas.Vacancy)
def create_vacancy(
    vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)
):
    return crud.create_vacancy(db=db, vacancy=vacancy)

@app.get("/vacancies/{vacancy_id}", response_model=schemas.Vacancy)
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    db_vacancy = crud.get_vacancy(db, vacancy_id=vacancy_id)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy

@app.get("/vacancies/", response_model=List[schemas.Vacancy])
def list_vacancies(db: Session = Depends(get_db)):
    db_vacancies = crud.list_vacancies(db)
    
    return db_vacancies

@app.post("/competencies/", response_model=schemas.Сompetence)
def create_сompetence(
    сompetence: schemas.СompetenceCreate, db: Session = Depends(get_db)
):
    return crud.create_сompetence(db=db, сompetence=сompetence)

@app.get("/competencies/{сompetence_id}", response_model=schemas.Сompetence)
def read_сompetence(сompetence_id: int, db: Session = Depends(get_db)):
    db_сompetence = crud.get_сompetence(db, сompetence_id=сompetence_id)
    if db_сompetence is None:
        raise HTTPException(status_code=404, detail="Competence not found")
    return db_сompetence

@app.get("/competencies/", response_model=List[schemas.Сompetence])
def list_competencies(db: Session = Depends(get_db)):
    db_competencies = crud.list_competencies(db)
    
    return db_competencies

@app.post("/users/", response_model=schemas.User)
def create_сompetence(
    user: schemas.UserCreate, db: Session = Depends(get_db)
):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def list_users(db: Session = Depends(get_db)):
    db_users = crud.list_users(db)
    
    return db_users

@app.get("/project/{project_id}/users", response_model=List[schemas.User])
def list_users(project_id: int, db: Session = Depends(get_db)):
    db_userinproject = crud.get_userinproject(db, project_id=project_id)
    if db_userinproject is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_userinproject

@app.post("/userinproject/", response_model=schemas.UserInProject)
def add_userinproject(
    userinproject: schemas.UserInProject,
    db: Session = Depends(get_db)
):
    try:
        return crud.add_userinproject(db=db, userinproject=userinproject)
    except:
        raise HTTPException(status_code=404, detail="Users or project does not exist")
'''
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
'''