from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR, TEXT, CHAR, BOOLEAN, Numeric
from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy_utils import ChoiceType

class Project(Base):
    STATUSES = [
        (u'uncheked', u'Не проверено'),
        (u'cheked', u'Проверено'),
        (u'filtered', u'Пройден экспертный фильтр'),
        (u'lead_selected', u'Назначен лидер'),
        (u'in_progress', u'Выполняется'),
        (u'archive', u'Архив')
    ]

    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR)
    goal = Column(VARCHAR)
    description = Column(VARCHAR)
    expected_results = Column(VARCHAR)
    #status = Column(ChoiceType(STATUSES))#ChoiceType
    result_represent_form = Column(VARCHAR)
    is_payable = Column(BOOLEAN, default=False)
    payment_amount = Column(Numeric, nullable=True)
    comment = Column(VARCHAR, nullable=True)
    partners = Column(VARCHAR, nullable=True)
    vacancies = Column(Integer, ForeignKey("vacancy.id"), index=True)
    #team = Column(Integer, ForeignKey("userinproject.id"), index=True)
    
    team = relationship("UserInProject", back_populates="project")

class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    skills_required = Column(Integer, ForeignKey("competence.id"), index=True)
    skills_as_plus = Column(Integer, ForeignKey("competence.id"), index=True)

class Competence(Base):
    __tablename__ = "competence"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

class UserInProject(Base):
    ROLES = [
        (u'partner', u'Партнер'),
        (u'student', u'Студент'),
        (u'moderator', u'Работник IT-Центра'),
        (u'project_lead', u'Лидер проекта')
    ]
    __tablename__ = "userinproject"
    #id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    #role = Column(ChoiceType(ROLES))
    project = relationship("Project", back_populates="team")
    user = relationship("User", back_populates="projects")



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    #projects = Column(Integer, ForeignKey("project.id"), index=True)
    competences = Column(Integer, ForeignKey("competence.id"), index=True, nullable=True)
    projects = relationship("UserInProject", back_populates="user")

