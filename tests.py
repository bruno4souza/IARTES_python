import funcionario as fn

class TestFuncionario(object):
    def testMaiorIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.maiorIdade() == True

    def TestValidarIdade(self):
        func = fn.Funcionario()
        func.set_idade('25') == True
