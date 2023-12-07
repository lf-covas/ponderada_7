from sqlalchemy.orm import Session
from .usuario_model import Usuario

class UsuarioRepository():
    @staticmethod
    def verifica_email(db: Session, email: str):
        if db.query(Usuario).filter(Usuario.email == email).first() is not None:
            return True
        else:
            return False

    @staticmethod
    def criar_usuario(db: Session, usuario: Usuario):
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    
    @staticmethod
    def obter_usuario(db: Session, email: str):
        return db.query(Usuario).filter(Usuario.email == email).first()
    
    @staticmethod
    def obter_usuarios(db: Session):
        return db.query(Usuario).all()
    
    @staticmethod
    def atualiza_usuario(db: Session, email: str, usuario_atualizado: dict):
        db_usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if db_usuario:
            for key, value in usuario_atualizado.items():
                setattr(db_usuario, key, value)
            db.commit()
            db.refresh(db_usuario)
            return db_usuario
        return None
    
    @staticmethod
    def deletar_usuario(db: Session, email: str):
        db_usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if db_usuario is not None:
            db.delete(db_usuario)
            db.commit()
            return True


