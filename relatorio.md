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

## Execução dos Testes

Comando executado:
```bash
python -m unittest discover tests -v

test_integracao_historico_resultado (Test_Integracao.Test_Integracao.test_integracao_historico_resultado) ... ok
test_integracao_historico_resultado2 (Test_Integracao.Test_Integracao.test_integracao_historico_resultado2) ... FAIL
test_operacoes_sequenciais (Test_Integracao.Test_Integracao.test_operacoes_sequenciais) ... ok
test_operacoes_sequenciais_incorreto (Test_Integracao.Test_Integracao.test_operacoes_sequenciais_incorreto) ... ok
test_consistencia_historico (Test_Unidade.Test_Unidade.test_consistencia_historico) ... ok
test_divisao (Test_Unidade.Test_Unidade.test_divisao) ... ok
test_divisao_por_zero (Test_Unidade.Test_Unidade.test_divisao_por_zero) ... ok
test_divisao_zero_por_zero (Test_Unidade.Test_Unidade.test_divisao_zero_por_zero) ... ERROR
test_entrada_saida_div (Test_Unidade.Test_Unidade.test_entrada_saida_div) ... ok
test_entrada_saida_mult (Test_Unidade.Test_Unidade.test_entrada_saida_mult) ... ok
test_entrada_saida_pow (Test_Unidade.Test_Unidade.test_entrada_saida_pow) ... ok
test_entrada_saida_soma (Test_Unidade.Test_Unidade.test_entrada_saida_soma) ... ok
test_entrada_saida_sub (Test_Unidade.Test_Unidade.test_entrada_saida_sub) ... FAIL
test_fluxos_divisao (Test_Unidade.Test_Unidade.test_fluxos_divisao) ... ok
test_historico_com_negativos_e_zero (Test_Unidade.Test_Unidade.test_historico_com_negativos_e_zero) ... FAIL
test_inicializacao (Test_Unidade.Test_Unidade.test_inicializacao) ... ok
test_inicializacao_objeto (Test_Unidade.Test_Unidade.test_inicializacao_objeto) ... ok
test_limite_inferior (Test_Unidade.Test_Unidade.test_limite_inferior) ... ok
test_limite_superior (Test_Unidade.Test_Unidade.test_limite_superior) ... ok
test_limpar_historico_vazio (Test_Unidade.Test_Unidade.test_limpar_historico_vazio) ... ok
test_mensagem_dupla_divisao_zero (Test_Unidade.Test_Unidade.test_mensagem_dupla_divisao_zero) ... FAIL
test_mensagens_erro (Test_Unidade.Test_Unidade.test_mensagens_erro) ... ok
test_modificacao_historico (Test_Unidade.Test_Unidade.test_modificacao_historico) ... ok
test_operacoes_indeterminadas (Test_Unidade.Test_Unidade.test_operacoes_indeterminadas) ... FAIL
test_tipagem_dupla_incorreta (Test_Unidade.Test_Unidade.test_tipagem_dupla_incorreta) ... ok
test_tipagem_invalida (Test_Unidade.Test_Unidade.test_tipagem_invalida) ... ok
test_underflow (Test_Unidade.Test_Unidade.test_underflow) ... ok

======================================================================
ERROR: test_divisao_zero_por_zero (Test_Unidade.Test_Unidade.test_divisao_zero_por_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 164, in test_divisao_zero_por_zero
    resultado = calc.dividir(0,0)
                ^^^^^^^^^^^^^^^^^
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\src\Calculadora.py", line 36, in dividir
    raise ValueError (" Divisao por zero nao permitida ")
ValueError:  Divisao por zero nao permitida

======================================================================
FAIL: test_integracao_historico_resultado2 (Test_Integracao.Test_Integracao.test_integracao_historico_resultado2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Integracao.py", line 49, in test_integracao_historico_resultado2
    self.assertEqual ( calc.obter_ultimo_resultado () , 10)
AssertionError: 254 != 10

======================================================================
FAIL: test_entrada_saida_sub (Test_Unidade.Test_Unidade.test_entrada_saida_sub)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 16, in test_entrada_saida_sub
    self.assertEqual ( resultado , 3)
AssertionError: -3 != 3

======================================================================
FAIL: test_historico_com_negativos_e_zero (Test_Unidade.Test_Unidade.test_historico_com_negativos_e_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 107, in test_historico_com_negativos_e_zero
    self.assertIn("0 / 2 = 0", calc.historico)
AssertionError: '0 / 2 = 0' not found in ['-2 + 3 = 1', '0 - 5 = -5', '-3 * -4 = 12', '0 / 2 = 0.0']

======================================================================
FAIL: test_mensagem_dupla_divisao_zero (Test_Unidade.Test_Unidade.test_mensagem_dupla_divisao_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 202, in test_mensagem_dupla_divisao_zero
    calc.dividir(0,0)
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\src\Calculadora.py", line 36, in dividir
    raise ValueError (" Divisao por zero nao permitida ")
ValueError:  Divisao por zero nao permitida

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 204, in test_mensagem_dupla_divisao_zero
    self.assertEqual (str ( e ) , " Divisao dupla por zero não permitida")
AssertionError: ' Divisao por zero nao permitida ' != ' Divisao dupla por zero não permitida'
-  Divisao por zero nao permitida
?                    ^           -
+  Divisao dupla por zero não permitida
?          ++++++          ^


======================================================================
FAIL: test_operacoes_indeterminadas (Test_Unidade.Test_Unidade.test_operacoes_indeterminadas)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 155, in test_operacoes_indeterminadas
    self.assertEqual( resultado , float('inf') )
AssertionError: nan != inf

----------------------------------------------------------------------

```

Comando executado:
```bash
run -m unittest discover tests

.F.....E....F.F.....F..F...
======================================================================
ERROR: test_divisao_zero_por_zero (Test_Unidade.Test_Unidade.test_divisao_zero_por_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 164, in test_divisao_zero_por_zero
    resultado = calc.dividir(0,0)
                ^^^^^^^^^^^^^^^^^
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\src\Calculadora.py", line 36, in dividir
    raise ValueError (" Divisao por zero nao permitida ")
ValueError:  Divisao por zero nao permitida

======================================================================
FAIL: test_integracao_historico_resultado2 (Test_Integracao.Test_Integracao.test_integracao_historico_resultado2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Integracao.py", line 49, in test_integracao_historico_resultado2
    self.assertEqual ( calc.obter_ultimo_resultado () , 10)
AssertionError: 254 != 10

======================================================================
FAIL: test_entrada_saida_sub (Test_Unidade.Test_Unidade.test_entrada_saida_sub)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 16, in test_entrada_saida_sub
    self.assertEqual ( resultado , 3)
AssertionError: -3 != 3

======================================================================
FAIL: test_historico_com_negativos_e_zero (Test_Unidade.Test_Unidade.test_historico_com_negativos_e_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 107, in test_historico_com_negativos_e_zero
    self.assertIn("0 / 2 = 0", calc.historico)
AssertionError: '0 / 2 = 0' not found in ['-2 + 3 = 1', '0 - 5 = -5', '-3 * -4 = 12', '0 / 2 = 0.0']

======================================================================
FAIL: test_mensagem_dupla_divisao_zero (Test_Unidade.Test_Unidade.test_mensagem_dupla_divisao_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 202, in test_mensagem_dupla_divisao_zero
    calc.dividir(0,0)
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\src\Calculadora.py", line 36, in dividir
    raise ValueError (" Divisao por zero nao permitida ")
ValueError:  Divisao por zero nao permitida

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 204, in test_mensagem_dupla_divisao_zero
    self.assertEqual (str ( e ) , " Divisao dupla por zero não permitida")
AssertionError: ' Divisao por zero nao permitida ' != ' Divisao dupla por zero não permitida'
-  Divisao por zero nao permitida
?                    ^           -
+  Divisao dupla por zero não permitida
?          ++++++          ^


======================================================================
FAIL: test_operacoes_indeterminadas (Test_Unidade.Test_Unidade.test_operacoes_indeterminadas)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\enzzo\Downloads\AT5\projeto_calculadora\tests\Test_Unidade.py", line 155, in test_operacoes_indeterminadas
    self.assertEqual( resultado , float('inf') )
AssertionError: nan != inf

----------------------------------------------------------------------
Ran 27 tests in 0.010s

FAILED (failures=5, errors=1)

```

Comando executado:
```bash
python -m unittest tests.test_unidade.TestCalculadora.test_soma -v
test_unidade (unittest.loader._FailedTest.test_unidade) ... ERROR

======================================================================
ERROR: test_unidade (unittest.loader._FailedTest.test_unidade)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_unidade
Traceback (most recent call last):
  File "C:\Users\enzzo\anaconda3\Lib\unittest\loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
             ^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'tests.test_unidade'


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```






