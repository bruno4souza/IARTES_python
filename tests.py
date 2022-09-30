import funcionario as fn

class TestFuncionario(object):
    def testMaiorIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.maiorIdade() == True

    def testValidarIdade(self):
        func = fn.Funcionario()
        assert func.set_idade(25) == True
        assert func.set_idade("25") == False
    def testValidarNome(self):
        func = fn.Funcionario()
        assert func.set_nome("Joao Paulo") == True
        #assert func.set_nome('4na K0zan') == False
        assert func.set_nome(3443) == False
        assert func.set_nome(' ') == False