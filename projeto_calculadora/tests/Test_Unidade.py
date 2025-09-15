import unittest
from src.Calculadora import Calculadora



class Test_Unidade (unittest.TestCase) :
    def test_entrada_saida_soma ( self ) :
        calc = Calculadora ()
        resultado = calc.somar(5 , 3)
        self.assertEqual( resultado , 8)
        self.assertEqual( calc.obter_ultimo_resultado () , 8)

    def test_entrada_saida_sub ( self ) :
        calc = Calculadora ()
        resultado = calc.subtrair(5,8)
        self.assertEqual ( resultado , 3)
        self.assertEqual ( calc.obter_ultimo_resultado () , 3)

    def test_entrada_saida_mult ( self ) :
        calc = Calculadora ()
        resultado = calc.multiplicar (5 , 3)
        self.assertEqual( resultado , 15)
        self.assertEqual( calc.obter_ultimo_resultado () , 15)

    def test_entrada_saida_div ( self ) :
        calc = Calculadora ()
        resultado = calc.dividir (6 , 3)
        self.assertEqual( resultado , 2)
        self.assertEqual( calc.obter_ultimo_resultado () , 2)    


    def test_entrada_saida_pow ( self ) : #Teste extra entrada e saída
        calc = Calculadora ()
        resultado = calc.potencia (2 , 2)
        self.assertEqual ( resultado , 4)
        self.assertEqual ( calc.obter_ultimo_resultado () , 4)


    def test_tipagem_invalida ( self ) :
        calc = Calculadora ()

        nNone = None
        nNumero = 2
        nString = "2"

        with self.assertRaises ( TypeError ) :
            calc.somar (nString, nNumero)
            calc.subtrair(nString, nNumero)
            calc.dividir(nString, nNumero)
            calc.multiplicar(nString, nNumero)
            calc.potencia(nString, nNumero)

        with self.assertRaises ( TypeError ) :
            calc.somar (nNone, nNumero)
            calc.subtrair(nNone, nNumero)
            calc.dividir(nNone, nNumero)
            calc.multiplicar(nNone, nNumero)
            calc.potencia(nNone, nNumero)

        with self.assertRaises ( TypeError ) :
            calc.somar (nNone, nString)
            calc.subtrair(nNone, nString)
            calc.dividir(nNone, nString)
            calc.multiplicar(nNone, nString)
            calc.potencia(nNone, nString)

    def test_tipagem_dupla_incorreta(self): # Teste extra tipagem 
        calc = Calculadora()

        nLista = [1,2]
        nString = "2"

        with self.assertRaises ( TypeError ) :
            calc.somar (nString, nLista)
            calc.subtrair(nString, nLista)
            calc.dividir(nString, nLista)
            calc.multiplicar(nString, nLista)
            calc.potencia(nString, nLista)
        
        with self.assertRaises ( TypeError ) :
            calc.somar (nLista, nString)
            calc.subtrair(nLista, nString)
            calc.dividir(nLista, nString)
            calc.multiplicar(nLista, nString)
            calc.potencia(nLista, nString)

    def test_consistencia_historico ( self ) :
        calc = Calculadora ()
        calc.somar (2 , 3)
        calc.multiplicar (4 , 5)
        self.assertEqual ( len ( calc . historico ) , 2)
        self.assertIn ("2 + 3 = 5", calc . historico )
        self.assertIn ("4 * 5 = 20", calc . historico )
    
    def test_historico_com_negativos_e_zero(self): # Teste extra consistência
        calc = Calculadora()

        calc.somar(-2, 3)
        calc.subtrair(0, 5)
        calc.multiplicar(-3, -4)
        calc.dividir(0, 2)

        self.assertEqual(len(calc.historico), 4)
        self.assertIn("-2 + 3 = 1", calc.historico)
        self.assertIn("0 - 5 = -5", calc.historico)
        self.assertIn("-3 * -4 = 12", calc.historico)
        self.assertIn("0 / 2 = 0", calc.historico)


    def test_inicializacao ( self ) :
        calc = Calculadora ()
        self.assertEqual(calc.resultado , 0)
        self.assertEqual (len(calc.historico) , 0)
    
    def test_inicializacao_objeto ( self ): # Teste extra inicialização
        calc = Calculadora()
        self.assertIsInstance(calc, Calculadora)

    def test_modificacao_historico ( self ) :
        calc = Calculadora ()
        calc.somar (1 , 1)
        self.assertEqual (len ( calc.historico ) , 1)
        calc.limpar_historico ()
        self.assertEqual (len ( calc.historico ) , 0)

    def test_limpar_historico_vazio(self): # Teste extra modificação de dados
        calc = Calculadora()
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_limite_inferior ( self ) :
        calc = Calculadora ()
        # Teste com zero
        resultado = calc.somar (0 , 5)
        self.assertEqual ( resultado , 5)
        # Teste com numeros negativos muito pequenos
        resultado = calc.multiplicar ( -1e-10 , 2)
        self.assertEqual( resultado , -2e-10)

    def test_underflow(self): #Teste extra limite inferior
        calc = Calculadora ()
        resultado = calc.multiplicar(1e-300, 1e-300)
        self.assertEqual(resultado, 0.0)

    def test_limite_superior ( self ) :
        calc = Calculadora ()
        # Teste com numeros grandes
        resultado = calc.somar (float('inf') , float('inf'))
        self.assertEqual( resultado , float('inf') )    

    def test_operacoes_indeterminadas (self): #teste extra limite_superior
        calc = Calculadora ()
        # Teste com numeros grandes
        resultado = calc.somar (float('inf') , - float('inf'))
        self.assertEqual( resultado , float('inf') ) 

    def test_divisao_por_zero ( self ) :
        calc = Calculadora ()
        with self.assertRaises ( ValueError ) :
            calc.dividir (10 , 0)

    def test_divisao_zero_por_zero ( self ) : #Teste extra Valores Fora do Intervalo
        calc = Calculadora ()
        resultado = calc.dividir(0,0)
        self.assertIsNaN(resultado)

    def test_fluxos_divisao ( self ) :
        calc = Calculadora ()
        # Caminho normal
        resultado = calc.dividir (10 , 2)
        self.assertEqual ( resultado , 5)
        # Caminho de erro
        with self.assertRaises ( ValueError ) :
            calc.dividir (10 , 0)
    
    def test_divisao ( self ): #Teste extra fluxos de controle
        calc = Calculadora()
        # Divisão com números negativos
        resultado = calc.dividir(-10, 2)
        self.assertEqual(resultado, -5)
        
        # Divisão de um número pequeno por um grande
        resultado = calc.dividir(1, 1000)
        self.assertEqual(resultado, 0.001)

        # Divisão de zero por um número
        resultado = calc.dividir(0, 5)
        self.assertEqual(resultado, 0)


    def test_mensagens_erro ( self ) :
        calc = Calculadora ()
        try :
            calc.dividir (5 , 0)
        except ValueError as e :
            self.assertEqual (str ( e ) , " Divisao por zero nao permitida ")

    def test_mensagem_dupla_divisao_zero(self): # Teste extra Mensagens de erro
        calc = Calculadora()

        try:
            calc.dividir(0,0)
        except ValueError as e :
            self.assertEqual (str ( e ) , " Divisao dupla por zero não permitida")

    if __name__ == '__main__':
        unittest.main()