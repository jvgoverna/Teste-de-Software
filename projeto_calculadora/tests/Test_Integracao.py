from Calculadora import Calculadora


class Test_Integracao:
    
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
        self.assertEqual ( len ( calc . historico ) , 3)


    def test_integracao_historico_resultado ( self ) :
        calc = Calculadora ()
        calc.potencia (2 , 3) # 2^3 = 8
        calc.somar ( calc.obter_ultimo_resultado () , 2) # 8 + 2 = 10
        
        self.assertEqual ( calc.obter_ultimo_resultado () , 10)
        self.assertEqual ( len ( calc.historico ) , 2)
        self.assertIn ("2 ^ 3 = 8", calc.historico )
        self.assertIn ("8 + 2 = 10", calc.historico )
