from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: str
    