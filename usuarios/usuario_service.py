from .usuario_repository import UsuarioRepository
from .usuarios_scehmas import UsuarioBase
from .usuario_model import Usuario
from sqlalchemy.orm import Session
from fastapi import HTTPException

class UsuarioService():
    def __init__(self):
        self.repository = UsuarioRepository()

    def criar_usuario(self, db: Session, usuario_schema: UsuarioBase):
        if self.repository.verifica_email(db, usuario_schema.email):
            raise HTTPException(status_code=400, detail="Email já está em uso")
        usuario_model = Usuario(nome = usuario_schema.nome, email = usuario_schema.email, senha = usuario_schema.senha)
        return self.repository.criar_usuario(db, usuario_model)
    
    def obter_usuario(self, db: Session, email: str):
        usuario = self.repository.obter_usuario(db, email)
        if usuario is None:
            raise HTTPException(status_code=404, detail= f"Nem um Usuário cadastrado com o email {email}.")
        return usuario
    
    def obter_usuarios(self, db: Session):
        return UsuarioRepository.obter_usuarios(db)
    
    def atualizar_usuario(self, db: Session, email:str, usuario_atualizado: dict):
        return self.repository.atualiza_usuario(db, email, usuario_atualizado)
    
    def deletar_usuario(self, db: Session, email: str):
        usuario = self.repository.deletar_usuario(db, email)
        if usuario is True:
            return f'Usuário com o email {email} deletado com sucesso!'
        else:
            return f'Usuário com o email {email} não encontrado.'


