from pydantic import BaseModel

class HistoriaBase(BaseModel):
    titulo: str
    categoria: str
    conteudo: str

    class Config:
        from_attributes = True



