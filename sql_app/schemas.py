from typing import List, Optional

from pydantic import BaseModel

'''
class ProjectCreate(BaseModel):
    id: int
    title: str
'''
class ProjectCreate(BaseModel):
    #id: int
    title: str
    goal: str
    description: str
    expected_results: str
    #status: str  # не понятно как назначать
    result_represent_form: str
    is_payable: bool
    payment_amount: Optional[float]
    comment: Optional[str]
    partners: Optional[str]
    vacancies: Optional[int]


class Project(BaseModel):
    id: int
    title: str
    goal: str
    description: str
    expected_results: str
    #status: str  # не понятно как назначать
    result_represent_form: str
    is_payable: bool
    payment_amount: Optional[float]
    comment: Optional[str]
    partners: Optional[str]
    vacancies: Optional[int]
    
    class Config:
        orm_mode = True



class Vacancy(BaseModel):
    id: int
    title: str
    skills_required: Optional[int]
    skills_as_plus: Optional[int]
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class VacancyCreate(BaseModel):
    #id: int
    title: str    
    
class Сompetence(BaseModel):
    id: int
    title: str
    
    class Config:
        orm_mode = True

class СompetenceCreate(BaseModel):
    title: str

class User(BaseModel):
    id: int
    full_name: str
    email: Optional[str]
    phone: Optional[str]
    Сompetences: Optional[int]

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    full_name: str

class UserInProject(BaseModel):  # не понятно как создавать
    project_id: int
    user_id: int
    #role: str  # не понятно как назначать

    class Config:
        orm_mode = True




'''
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
'''