from sqlalchemy import String, Column
from database import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    nome = Column(String(100), index=True)
    email = Column(String(100), primary_key=True, index=True)
    senha = Column(String(50))
    