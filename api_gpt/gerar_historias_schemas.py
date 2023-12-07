from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class TrechoAtualizado(BaseModel):
    conteudo: str