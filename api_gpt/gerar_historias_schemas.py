from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class TrechoRequest(BaseModel):
    trecho: dict