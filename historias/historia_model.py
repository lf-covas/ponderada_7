from sqlalchemy import Integer, String, Column, Text
from database import Base

class Historia(Base):
    __tablename__ = 'historia'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    categoria = Column(String(100), index=True)
    conteudo = Column(Text)