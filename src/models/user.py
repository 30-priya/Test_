from sqlalchemy import Column, String, Integer, ForeignKey,Text,Enum,ARRAY,Boolean , LargeBinary , PickleType
from src.common.database import Database
from flask_sqlalchemy import SQLAlchemy

class RoleEnum(Enum):
    ROLE1 = 'Role1'
    ROLE2 = 'Role2'
    ROLE3 = 'Role3'
# db = SQLAlchemy()

class User(Database.Base_model):
    __tablename__ = "users"
    
    username = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    password = Column(String(500), nullable=True)
    role = Column(Enum('Role1', 'Role2', 'Role3', name='role_type'))
