# Relatório de Testes – Calculadora

## 1. Objetivo
O objetivo desta atividade foi aplicar, na prática, conceitos de **Testes de Unidade**, **Testes de Integração** e **Medição de Cobertura de Código**.  
O sistema em questão é uma **calculadora simples** com operações aritméticas (soma, subtração, multiplicação, divisão, potência), além do controle de histórico e obtenção do último resultado.

A execução dos testes foi feita utilizando o **framework `unittest` do Python** e a ferramenta **`coverage.py`** para mensurar a cobertura.

---

## 2. Resumo da Execução
Foi utilizada a ferramenta `coverage.py` para medir a cobertura dos testes implementados.

**Relatório obtido:**
- `src\Calculadora.py` → **91%** (46 instruções, 4 não cobertas)  
- `tests\test_integracao.py` → **89%** (38 instruções, 4 não cobertas)  
- `tests\test_unidade.py` → **85%** (156 instruções, 23 não cobertas)  
- **Cobertura total:** **87%** (240 instruções, 31 não cobertas)  

Isso indica que a maior parte do código da calculadora foi testada, mas ainda existem cenários não testados, principalmente nos casos de exceção e testes extras.

---

## 3. Análise dos Testes de Unidade
Os **testes de unidade** foram responsáveis por validar **cada método isoladamente** da classe `Calculadora`.

- **Cobertura:** 85%  
  - Verificação correta de operações básicas (soma, subtração, multiplicação, divisão, potência).  
  - Testes de tipagem para rejeitar argumentos inválidos.  
  - Consistência no histórico de operações.  
  - Cenários de inicialização e limpeza de dados.  
  - Testes com limites numéricos (valores pequenos, grandes e infinitos).  

- **Problemas**
  - Alguns testes extras falharam por divergência entre o esperado e o código (ex.: `0/0`, mensagens de erro com espaços a mais).  
  - Nem todos os caminhos de exceção foram cobertos, deixando 23 instruções sem execução.  

- **Conclusão:**
  - Testes de unidade são essenciais para garantir a **confiabilidade individual de cada método**.  
  - Eles ajudam a capturar **erros de tipagem, comportamentos inesperados e casos de limite extremo**.  
  - Porém, exigem muita atenção aos detalhes: se o teste espera algo diferente da implementação (como mensagens de erro), ele falha, mostrando a importância da **alinhamento entre requisitos e código**.  

---

## 4. Análise dos Testes de Integração
Os **testes de integração** validaram como os métodos da calculadora funcionam em conjunto.

- **Cobertura:** 89%  
  - Verificação de operações encadeadas (ex.: soma → multiplicação → divisão).  
  - Testes de interface entre métodos, garantindo que o `obter_ultimo_resultado` e o `historico` se atualizam corretamente.  
  - Incluíram também cenários de erro (divisão por zero dentro de uma sequência).  

- **Problemas:**
  - Alguns testes extras não foram totalmente cobertos, resultando em 4 instruções não executadas.  

- **Conclusão:**
  - Testes de integração são fundamentais para garantir que os métodos **se comunicam corretamente**.  
  - Eles revelam problemas que não aparecem em testes unitários, como falhas na manutenção do estado interno da calculadora (ex.: último resultado e histórico).  

---

## 5. Executando testes normais x cobertura
- **Execução normal (`python -m unittest discover tests -v`)**  
  ➝ Apenas executa os testes e informa quais passaram ou falharam.  

- **Execução com cobertura (`coverage run -m unittest discover tests`)**  
  ➝ Executa os testes **e monitora quais linhas do código foram realmente utilizadas**.  
  ➝ Depois é possível gerar relatórios:  
  - `coverage report` → mostra no terminal (percentuais de cobertura).  
  - `coverage html` → gera um relatório visual em HTML (linhas cobertas ficam verdes, não cobertas ficam vermelhas).  

Mesmo que todos os testes passem, o coverage ajuda a identificar **partes do código que nunca foram testadas**.

---

## 6. Conclusão Geral
- A cobertura total de **87%** demonstra que os testes foram abrangentes e aplicados em cenários diversos.   
- **Testes de Unidade** reforçaram a importância da validação detalhada, tratamento de erros e casos de limite extremo.  
- **Testes de Integração** mostraram a relevância de avaliar a **coerência do sistema como um todo**, garantindo que os métodos funcionam de forma conjunta e confiável.  
