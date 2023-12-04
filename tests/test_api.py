from historias.historia_repository import HistoriaRepository
from usuarios.usuario_repository import UsuarioRepository
from historias.historia_model import Historia
from usuarios.usuario_model import Usuario
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from database import Base
from main import app
import pytest
import os

client = TestClient(app)

load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}/{dbname}'

@pytest.fixture(scope="function")
def db():
    # Configura uma engine de teste
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    # Cria todas as tabelas no banco de dados em memória
    Base.metadata.create_all(engine)

    # Cria uma sessão configurada para testes
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Cria uma instância de sessão
    db_session = TestingSessionLocal()

    yield db_session  # Isso permite que o teste use a sessão

    db_session.close()  # Limpa a sessão depois que o teste termina

# def test_verifica_email(db):
#     email_novo = 'covasmaisoumenos@gmail.com'
#     email_cadastrado = 'covas_bomdemais@gmail.com'
#     assert UsuarioRepository.verifica_email(db, email_novo) is True
#     assert UsuarioRepository.verifica_email(db, email_cadastrado) is False

# def test_criar_usuario(db):
#     nome = 'Yuri'
#     email = 'yuri_bomdemais@gmail.com'
#     senha = '98765'

#     novo_usuario = Usuario(nome = nome, email = email, senha = senha)
#     usuario_criado = UsuarioRepository.criar_usuario(db, novo_usuario)

#     assert usuario_criado is not None
#     assert usuario_criado.nome == nome
#     assert usuario_criado.email == email

# def test_obter_usuario(db):
#     email_usuario = 'yuri_bomdemais@gmail.com'
#     usuario = UsuarioRepository.obter_usuario(db, email_usuario)
#     assert usuario.email == email_usuario

# def test_obter_usuarios(db):
#     usuarios = UsuarioRepository.obter_usuarios(db)
#     assert isinstance(usuarios, list)   
#     assert len(usuarios) > 0
#     for usuario in usuarios:
#         assert isinstance(usuario, Usuario)

# def test_atualiza_usuario(db):
#     email_usuario = 'yuri_bomdemais@gmail.com'
#     atualizando = {
#         'nome': 'Yuri Zé Roela'
#     }
#     usuario_atualizado = UsuarioRepository.atualiza_usuario(db, email_usuario, atualizando)

#     assert usuario_atualizado.nome == 'Yuri Zé Roela'

# def test_deletar_usuario(db):
#     email = 'yuri_bomdemais@gmail.com'
#     usuario = UsuarioRepository.deletar_usuario(db, email)
#     assert usuario == True

# def test_criar_historia(db):
#     titulo = 'Historia Animal 2'
#     categoria = 'Ficção'
#     conteudo = 'Sabe o que aconteceu de novo...'

#     nova_historia = Historia(titulo = titulo, categoria = categoria, conteudo = conteudo)
#     criando_nova_historia = HistoriaRepository.criar_historia(db, nova_historia)

#     assert criando_nova_historia.titulo == titulo
#     assert criando_nova_historia.categoria == categoria
#     assert criando_nova_historia.conteudo == conteudo

# def test_obter_historia(db):
#     titulo = 'Historia Animal'
#     historia = HistoriaRepository.obter_historia(db, titulo)

#     assert historia.titulo == titulo
#     assert isinstance(historia.titulo, str)
#     assert isinstance(historia.conteudo, str)

# def test_obter_historias(db):
#     historias = HistoriaRepository.obter_historias(db)

#     assert isinstance(historias, list)
#     for historia in historias:
#         isinstance(historia, Historia)

# def test_atualiza_historia(db):
#     titulo = 'Historia Animal'
#     atualizando = {
#         "conteudo": "Cara, cansei disso já"
#     }
#     historia_atualizada = HistoriaRepository.atualizar_historia(db, titulo, atualizando)

#     assert historia_atualizada.conteudo == 'Cara, cansei disso já'
#     assert isinstance(historia_atualizada, Historia)

# def test_deletar_historia(db):
#     titulo = 'Historia Animal 2'
#     historia_deletada = HistoriaRepository.deletar_historia(db, titulo)

#     assert historia_deletada == True

def test_criando_usuario_api():
    info_usuario_novo = {
        "nome":"Gabriel",
        "email":"gabriel_bomdemais@gmail.com",
        "senha":"12345"
    }

    retorno = client.post("/usuario", json=info_usuario_novo)
    assert retorno.status_code == 200
    assert retorno.json()['email'] == "gabriel_bomdemais@gmail.com"
