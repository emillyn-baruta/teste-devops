from unittest.mock import patch
from src.main import Estudante, root, funcaoteste, create_estudante, update_estudante, delete_estudante


def test_root():
    result = root()
    assert result == {"message": "Hello World"}

def test_funcao_teste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result

def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert update_estudante(10)

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert delete_estudante(5)
