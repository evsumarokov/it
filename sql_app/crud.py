from sqlalchemy.orm import Session
from sqlalchemy import update
from . import models, schemas



###
def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    current_project=db.query(models.Project).filter(models.Project.id == project_id)  
    db.add(current_project)
    db.commit()
    db.refresh(current_project)
    return current_project

def list_projects(db: Session):
    return db.query(models.Project).all()
###
def get_vacancy(db: Session, vacancy_id: int):
    return db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()

def create_vacancy(db: Session, vacancy: schemas.VacancyCreate):
    db_vacancy = models.Vacancy(**vacancy.dict())
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy

def list_vacancies(db: Session):
    return db.query(models.Vacancy).all()
###
def get_сompetence(db: Session, сompetence_id: int):
    return db.query(models.Сompetence).filter(models.Сompetence.id == сompetence_id).first()

def create_сompetence(db: Session, сompetence: schemas.СompetenceCreate):
    db_сompetence = models.Competence(**сompetence.dict())
    db.add(db_сompetence)
    db.commit()
    db.refresh(db_сompetence)
    return db_сompetence

def list_competencies(db: Session):
    return db.query(models.Competence).all()
###
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db: Session):
    return db.query(models.User).all()
###
def get_userinproject(db: Session, project_id: int):
    list_users = []
    p = db.query(models.UserInProject).filter(models.UserInProject.project_id == project_id).all()
    for i in p:
        list_users.append(get_user(db, i.user_id))
    return list_users

def add_userinproject(db: Session, userinproject: schemas.UserInProject):
    db_userinproject = models.UserInProject(**userinproject.dict())
    db.add(db_userinproject)
    db.commit()
    db.refresh(db_userinproject)
    return db_userinproject