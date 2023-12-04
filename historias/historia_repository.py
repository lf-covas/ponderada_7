from sqlalchemy.orm import Session
from .historia_model import Historia 

class HistoriaRepository():

    @staticmethod
    def criar_historia(db: Session, historia: Historia):
        db.add(historia)
        db.commit()
        db.refresh(historia)
        return historia
    
    @staticmethod
    def obter_historia(db: Session, historia_titulo: str):
        return db.query(Historia).filter(Historia.titulo == historia_titulo).first()
    
    @staticmethod
    def obter_historias(db: Session):
        return db.query(Historia).all()
    
    @staticmethod
    def atualizar_historia(db: Session, historia_titulo: str, historia_atualizada: dict):
        db_historia = db.query(Historia).filter(Historia.titulo == historia_titulo).first()
        if db_historia:
            for key, value in historia_atualizada.items():
                setattr(db_historia, key, value)
            db.commit()
            db.refresh(db_historia)
            return db_historia
        return None
    
    @staticmethod
    def deletar_historia(db: Session, historia_titulo: str):
        db_historia = db.query(Historia).filter(Historia.titulo == historia_titulo).first()
        if db_historia is not None:
            db.delete(db_historia)
            db.commit()
            return True
