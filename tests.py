from codecs import ascii_encode
import funcionario as fn

class TestFuncionario(object):
    #Teste do metodo que verifica se o funcionário é maior de idade.
    def testMaiorIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.maiorIdade() == True
        func.set_idade(16)
        assert func.maiorIdade() == False

    #Teste de validação da idade inserida.
    def testValidarIdade(self):
        func = fn.Funcionario()
        assert func.set_idade(25) == True
        assert func.set_idade("25") == False
    
    #Teste de uma coleta do atributo idade
    def testPegarIdade (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_idade() == 25

    #Teste de validação de um nome inserido.
    def testValidarNome(self):
        func = fn.Funcionario()
        assert func.set_nome("Joao Paulo") == True
        #assert func.set_nome('4na K0zan') == False
        assert func.set_nome(3443) == False
        assert func.set_nome(' ') == False
    
    #Teste de uma coleta do atributo nome.
    def testPegarNome (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_nome() == 'nome'

    #Teste de validação de uma matrícula inserida.
    def testValidarMatricula(self):
        func = fn.Funcionario()
        assert func.set_matricula('N1420B') == True
        assert func.set_matricula('N1420B1') == False
        assert func.set_matricula(344334) == False
        assert func.set_matricula(' ') == False
    
    #Teste de uma coleta do atributo matrícula.
    def testPegarMatricula (self):
        func = fn.FuncionarioRH(25, 'nome', '121314', 100, 13)
        assert func.get_matricula() == '121314'

    #Teste de validação do método de contratação de funcionario.
    def testPegarFuncionario (self):
        func = fn.Funcionario()
        assert func.pegar_funcionario() == 'Funcionario Contratado'
    
    #Teste que verifica a meta de contratação do funcionário de RH.
    def testMetaContratacao(self):
        func = fn.FuncionarioRH()
        assert func.set_meta_contratacao(100) == True
        assert func.set_meta_contratacao("25") == False
    
    #Teste de uma inserção e coleta do atributo meta de contratação.
    def testPegaMetaContratacao(self):
        func = fn.FuncionarioRH()
        func.set_meta_contratacao(100)
        assert func.get_meta_contratacao() == 100

    #Teste que valida uma inserção incorreta do atributo qtsd contratação.
    def testQtdContratacao(self):
        func = fn.FuncionarioRH()
        assert func.set_qtd_contratacao(100) == True
        assert func.set_qtd_contratacao("25") == False
    
    #Teste de uma inserção e coleta do atributo qtd contratação.
    def testPegaQtdContratacao(self):
        func = fn.FuncionarioRH()
        func.set_qtd_contratacao(45)
        assert func.get_qtd_contratacao() == 45
    
    #Teste que verifica a contratação de uma novo funcionário usando o metodo recrutar funcionário.
    def testRecrutarFuncionario (self):
        func = fn.FuncionarioRH()
        func.set_qtd_contratacao(45)
        assert func.recrutar_funcionario() == 'Novo Funcionario Recrutado'
        assert func.get_qtd_contratacao() == 46
    
    #Teste que verifica o método que permite ao funcionário de RH palestrar.
    def testpalestrar (self):
        func = fn.FuncionarioRH()
        func.palestrar()
        assert  func.palestrar() == "Recrutador esta palestrando"

    #Teste que verifica a utilização da senha de rede do funcionário de TI.
    def testSenhaRede(self):
        func = fn.FuncionarioTI()
        assert func.set_senha_rede("P@ssw0rd123") == True
        assert func.set_senha_rede("P@ssw") == False
        assert func.set_senha_rede(1231342) == False

    #Teste que verifica uma inserção e consumo do atributo de senha de rede.
    def testPegarSenhaRede(self):
        func = fn.FuncionarioTI()
        func.set_senha_rede("P@ssw0rd123")
        assert func.get_senha_rede() == "P@ssw0rd123"

    def testIdComputador(self):
        func = fn.FuncionarioTI()
        assert func.set_id_computador("PC00007") == True
        assert func.set_id_computador("PC0007") == False
        assert func.set_id_computador("PCdojunior") == False
        assert func.set_id_computador(1231342) == False

   
    def testPegarIdComputador(self):
        func = fn.FuncionarioTI()
        func.set_id_computador("PC00007")
        assert func.get_id_computador() == "PC00007"

    def testLogarRede(self):
        func = fn.FuncionarioTI()
        func.logar_rede()
        assert  func.logar_rede() == "Autenticado na Rede"
    
    def testCrp(self):
        func = fn.Psicologa()
        assert func.set_crp("10646") == True
        assert func.set_crp("106468") == False
        assert func.set_crp("1064") == False
        assert func.set_crp(10646) == False
        assert func.set_crp(1231342) == False

    def testPegarCrp(self):
        func = fn.Psicologa()
        func.set_crp("10646")
        assert func.get_crp()=="10646"

    def testSalaAtendimento(self):
        func = fn.Psicologa()
        assert func.set_sala_atendimento("Sala 2") == True
        assert func.set_sala_atendimento(2) == False
    def testPegarSalaAtendimento(self):
        func = fn.Psicologa()
        func.set_sala_atendimento("Sala 2")   
        assert func.get_sala_atendimento() == "Sala 2" 
