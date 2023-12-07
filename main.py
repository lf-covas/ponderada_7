from fastapi import FastAPI, Depends, Body
from historias.historia_service import HistoriaService
from historias.historia_schemas import HistoriaBase
from usuarios.usuario_service import UsuarioService
from usuarios.usuarios_scehmas import UsuarioBase
from api_gpt.gerar_historias_schemas import PromptRequest, TrechoAtualizado
from api_gpt.gerar_historias import gerar_historias, complementar_historia
from sqlalchemy.orm import Session
from fastapi import HTTPException

from database import get_db

app = FastAPI()

@app.get("/historias")
async def historias(db: Session = Depends(get_db)):
    service = HistoriaService()
    return service.obter_todas_historias(db)

@app.get("/historia/{titulo}")
async def obter_historia(titulo: str, db: Session = Depends(get_db)):
    service = HistoriaService()
    historia = service.obter_historia_por_titulo(db, titulo)
    return historia

@app.post("/historia")
async def cria_historia(historia: HistoriaBase, db: Session = Depends(get_db)):
    service = HistoriaService()
    return service.criar_historia(db, historia)

@app.patch("/historia/{historia_titulo}")
async def atualiza_historia(historia_titulo: str, historia: dict = Body(...), db:Session = Depends(get_db)):
    service = HistoriaService()
    historia_atualizada = service.atualiza_historia(db, historia_titulo, historia)
    if historia_atualizada is None:
        raise HTTPException(status_code=404, detail= f"História {historia_titulo} não encontrada")
    return historia_atualizada

@app.patch("/historia/{historia_titulo}/adicionar_trecho")
async def atualiza_historia_com_gepetas(historia_titulo: str, novo_trecho: TrechoAtualizado, db: Session = Depends(get_db)):
    service = HistoriaService()
    trecho = novo_trecho.conteudo
    historia = service.obter_historia_por_titulo(db, historia_titulo)
    conteudo_atualizado = complementar_historia(historia.conteudo, trecho)
    historia_atualizada = service.atualiza_historia_com_gptas(db, historia_titulo, conteudo_atualizado)
    if historia_atualizada is None:
        raise HTTPException(status_code=404, detail= f"História {historia_titulo} não encontrada")
    return historia_atualizada

@app.delete("/historia/{titulo}")
async def deletar_historia(titulo: str, db: Session = Depends(get_db)):
    service = HistoriaService()
    return service.deletar_historia_por_titulo(db, titulo)

@app.get("/usuarios")
async def obter_usuarios(db: Session = Depends(get_db)):
    service = UsuarioService()
    return service.obter_usuarios(db)

@app.get("/usuario/{email}")
async def obter_usuario(email = str, db: Session = Depends(get_db)):
    service = UsuarioService()
    return service.obter_usuario(db, email)

@app.post("/usuario")
async def cria_usuario(usuario: UsuarioBase, db: Session = Depends(get_db)):
    service = UsuarioService()
    return service.criar_usuario(db, usuario)

@app.patch("/usuario/{email}")
async def atualiza_usuario(email: str, usuario: dict = Body(...), db: Session = Depends(get_db)):
    service = UsuarioService()
    usuario_atualizado = service.atualizar_usuario(db, email, usuario)
    if usuario_atualizado is None:
        raise HTTPException(status_code=404, detail=f"Nenhum usuário cadastrado com esse email: {email}")
    return usuario_atualizado

@app.delete("/usuario/{email}")
async def deletar_usuario(email: str, db: Session = Depends(get_db)):
    service = UsuarioService()
    return service.deletar_usuario(db, email)

@app.get("/")
async def root():
    return {"message": "Vei, que trabalho deu pra fazer isso ae..."}








@app.post("/gerar_historia")
async def gerar_historia_endpoint(PromptRequest: PromptRequest):
    try:
        resposta_historia = gerar_historias(PromptRequest.prompt)
        return {"historia": resposta_historia}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))