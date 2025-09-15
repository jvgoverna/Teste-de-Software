import unittest
from src.Calculadora import Calculadora


class Test_Integracao(unittest.TestCase):
    
    def test_operacoes_sequenciais ( self ) :
        calc = Calculadora ()
        # Sequencia : 2 + 3 = 5 , depois 5 * 4 = 20 , depois 20 / 2 = 10
        calc.somar (2 , 3)
        resultado1 = calc.obter_ultimo_resultado ()

        calc.multiplicar ( resultado1 , 4)

        resultado2 = calc.obter_ultimo_resultado ()

        calc.dividir ( resultado2 , 2)
        resultado_final = calc.obter_ultimo_resultado ()

        self.assertEqual ( resultado_final , 10)
        self.assertEqual ( len ( calc.historico ) , 3)

    def test_operacoes_sequenciais_incorreto(self): # Teste extra Operações Sequenciais
        calc = Calculadora()

        calc.somar(2,3)
        resultado1 = calc.obter_ultimo_resultado()

        with self.assertRaises ( ValueError ) :
            calc.dividir (resultado1 , 0)


    def test_integracao_historico_resultado ( self ) :
        calc = Calculadora ()
        calc.potencia (2 , 3) # 2^3 = 8
        calc.somar ( calc.obter_ultimo_resultado () , 2) # 8 + 2 = 10
        
        self.assertEqual ( calc.obter_ultimo_resultado () , 10)
        self.assertEqual ( len ( calc.historico ) , 2)
        self.assertIn ("2 ^ 3 = 8", calc.historico )
        self.assertIn ("8 + 2 = 10", calc.historico )

    def test_integracao_historico_resultado2 (self): # Teste extra Interface entre Métodos
        calc = Calculadora ()
        calc.potencia (5 , 3) # 2^3 = 8
        calc.somar ( calc.obter_ultimo_resultado () , 2) # 8 + 2 = 10
        calc.multiplicar(calc.obter_ultimo_resultado(), 2)
        
        self.assertEqual ( calc.obter_ultimo_resultado () , 10)
        self.assertEqual ( len ( calc.historico ) , 2)
        self.assertIn ("2 ^ 3 = 8", calc.historico )
        self.assertIn ("8 + 2 = 10", calc.historico )

    if __name__ == '__main__':
        unittest.main()