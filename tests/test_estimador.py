import pytest
from src.estimador import estimar_tempo

def test_estimativa_simples():
    assert estimar_tempo(10, 40) == 15.0

def test_velocidade_zero():
    with pytest.raises(ValueError):
        estimar_tempo(5, 0)

def test_distancia_negativa():
    with pytest.raises(ValueError):
        estimar_tempo(-10, 30)
