# inovaware-devops-simulacao# Simulação DevOps - InovaWare

Este repositório simula uma ação DevOps com foco em integração contínua usando GitHub Actions, baseado no cenário da startup fictícia InovaWare.

## 🔧 O que está sendo testado?

Uma função em Python que calcula o tempo estimado de chegada de um transporte público, com base na distância e velocidade.

## 🚀 Pipeline CI

A pipeline roda automaticamente a cada `push` ou `pull request` na branch `main`, executando os testes com Pytest.

## 📂 Estrutura do projeto

- `src/estimador.py`: código principal
- `tests/test_estimador.py`: testes automatizados
- `.github/workflows/ci.yml`: pipeline
- `requirements.txt`: dependências

## ✅ Como testar localmente

```bash
pip install -r requirements.txt
pytest
