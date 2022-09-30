import funcionario as fn

class TestFuncionario(object):
    def testMaiorIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.maiorIdade() == True
        func.set_idade(16)
        assert func.maiorIdade() == False


    def testValidarIdade(self):
        func = fn.Funcionario()
        assert func.set_idade(25) == True
        assert func.set_idade("25") == False
    
    def testPegarIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_idade() == 25

    def testValidarNome(self):
        func = fn.Funcionario()
        assert func.set_nome("Joao Paulo") == True
        #assert func.set_nome('4na K0zan') == False
        assert func.set_nome(3443) == False
        assert func.set_nome(' ') == False
    
    def testPegarNome (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_nome() == 'nome'

    def testValidarMatricula(self):
        func = fn.Funcionario()
        assert func.set_matricula('N1420B') == True
        assert func.set_matricula('N1420B1') == False
        assert func.set_matricula(344334) == False
        assert func.set_matricula(' ') == False
    
    def testPegarMatricula (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_matricula() == '121314'

    def testPegarFuncionario (self):
        func = fn.Funcionario()
        assert func.pegar_funcionario() == 'Funcionario Contratado'
    
    def testMetaContratacao(self):
        func = fn.FuncionarioRH()
        assert func.set_meta_contratacao(100) == True
        assert func.set_meta_contratacao("25") == False
    
    def testPegaMetaContratacao(self):
        func = fn.FuncionarioRH()
        func.set_meta_contratacao(100)
        assert func.get_meta_contratacao() == 100

    def testQtdContratacao(self):
        func = fn.FuncionarioRH()
        assert func.set_qtd_contratacao(100) == True
        assert func.set_qtd_contratacao("25") == False
    
    def testPegaQtdContratacao(self):
        func = fn.FuncionarioRH()
        func.set_qtd_contratacao(45)
        assert func.get_qtd_contratacao() == 45
    
    def testRecrutarFuncionario (self):
        func = fn.FuncionarioRH()
        func.set_qtd_contratacao(45)
        assert func.recrutar_funcionario() == 'Novo Funcionario Recrutado'
        assert func.get_qtd_contratacao() == 46
    

    def testpalestrar (self):
        func = fn.FuncionarioRH()
        func.palestrar()
        assert  func.palestrar() == "Recrutador esta palestrando"