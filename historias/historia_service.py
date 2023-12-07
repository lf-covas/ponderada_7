from .historia_repository import HistoriaRepository
from .historia_schemas import HistoriaBase
from .historia_model import Historia
from sqlalchemy.orm import Session
from fastapi import HTTPException

class HistoriaService():
    def __init__(self):
        self.repository = HistoriaRepository()

    def criar_historia(self, db: Session, historia_schema: HistoriaBase):
        historia_model = Historia(titulo = historia_schema.titulo, categoria = historia_schema.categoria, conteudo = historia_schema.conteudo)
        return self.repository.criar_historia(db, historia_model)

    def obter_todas_historias(self, db: Session):
        return self.repository.obter_historias(db)
    
    def obter_historia_por_titulo(self, db: Session, historia_titulo: str):
        historia = self.repository.obter_historia(db, historia_titulo) 
        if historia:
            return historia
        else:
            return HTTPException(status_code=404, detail="História não encontrada")
       
    def atualiza_historia(self, db: Session, historia_titulo: str, historia_atualizada: dict):
        return self.repository.atualizar_historia(db, historia_titulo, historia_atualizada)
    
    def atualiza_historia_com_gptas(self, db: Session, historia_titulo: str, historia_atualizada: str):
        return self.repository.atualizar_historia_com_gptas(db, historia_titulo, historia_atualizada)
    
    def deletar_historia_por_titulo(self, db: Session, historia_titulo: str):
        resposta = self.repository.deletar_historia(db, historia_titulo)
        if resposta is True:
            return f'História {historia_titulo} deletada com sucesso!'
        else:
            return f'Historia {historia_titulo} não encontrada'