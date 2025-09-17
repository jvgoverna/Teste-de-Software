# Projeto de Testes de Software – Calculadora

Este repositório contém uma **calculadora simples** desenvolvida em Python, utilizada como base para a prática de **Testes de Unidade** e **Testes de Integração** na disciplina de **CC8550 - SIMULAÇÃO E TESTE DE SOFTWARE*.

O objetivo é aplicar os conceitos teóricos em um sistema pequeno, mas que permita validar diferentes tipos de teste utilizando a ferramenta `coverage.py`.

---


## 📂 Estrutura do Projeto

- projeto_calculadora/
  - src/
    - Calculadora.py  # Código da calculadora
  - tests/
    - __init__.py     # Arquivo vazio
    - test_unidade.py # Testes de unidade
    - test_integracao.py # Testes de integração
  - requirements.txt  # Dependências
  - README.md         # Documentação
  - relatorio.md      # Relatório dos testes
 

## Comandos para Execução

### Instalar dependências
    pip install -r requirements.txt

### Executar todos os testes
    python -m unittest discover tests -v

### Executar com cobertura
    coverage run -m unittest discover tests
    coverage report
    coverage html

### Executar teste específico
    python -m unittest tests.test_unidade.TestCalculadora.test_soma -v

