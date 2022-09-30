from abc import ABC, abstractmethod
from asyncio.windows_events import NULL

class Funcionario(object):
    
    
    def __init__(self, idade:int = 0, nome:str = None, matricula:str = None):
        self._idade = idade
        self._nome = nome
        self._matricula = matricula
    

    def set_idade(self, idade:int):
        
        if not isinstance(idade, int):
            return False
        else: 
            self._idade = idade
            return True
        

    def get_idade(self):
        return self._idade

    def set_nome(self, nome:str):
        if not isinstance(nome, str) or nome==' ':
                return False
        else: 
            self._nome = nome
            return True

    def get_nome(self):
        return self._nome

    # A Matricula tem obrigatoriamente 6 caracteres 
    def set_matricula(self, matricula:str):
        if not isinstance(matricula, str) or matricula==' ':
            return False
        elif matricula.__len__() != 6:
            return False
        else: 
            self._matricula = matricula
            return True
        

    def get_matricula(self):
        return self._matricula

    @abstractmethod
    def pegar_funcionario(self):
        return "Funcionario Contratado"

    def maiorIdade(self):
        if self._idade >= 18:
            return True
        else:
            return False


class FuncionarioRH(Funcionario):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, meta_contratacao:int = 0, qtd_contratacao:int = 0 ):
        super().__init__(nome, matricula, idade)
        self._meta_contratacao = meta_contratacao
        self._qtd_contratacao = qtd_contratacao

    def set_meta_contratacao(self, meta_contratacao:int):
        if not isinstance(meta_contratacao, int):
            return False
        else: 
            self._meta_contratacao = meta_contratacao
            return True
        

    def get_meta_contratacao(self):
        return self._meta_contratacao

    def set_qtd_contratacao(self, qtd_contratacao:int):
        if not isinstance(qtd_contratacao, int):
            return False
        else: 
            self._qtd_contratacao = qtd_contratacao
            return True
        

    def get_qtd_contratacao(self):
        return self._qtd_contratacao

    @abstractmethod
    def recrutar_funcionario(self):
        self.set_qtd_contratacao(self.get_qtd_contratacao()+1)
        return "Novo Funcionario Recrutado"

    @abstractmethod
    def palestrar(self):
        return "Recrutador esta palestrando"

class FuncionarioTI(Funcionario):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, senha_rede:str = None, id_computador:int = 0):
        super().__init__(nome, matricula, idade)
        self._senha_rede = senha_rede
        self._id_computador = id_computador

    def set_senha_rede(self, senha_rede):
        self._senha_rede = senha_rede

    def get_senha_rede(self):
        return self._senha_rede

    def set_senha_rede(self, id_computador):
        self._id_computador = id_computador

    def get_senha_rede(self):
        return self._id_computador

    @abstractmethod
    def logar_rede(self):
       pass

class Psicologa(FuncionarioRH):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, meta_contratacao:int  = 0, qtd_contratacao:int  = 0 , crp:str = None, sala_atendimento:str = None):
        super().__init__(nome, matricula, idade, meta_contratacao, qtd_contratacao)
        self._crp = crp
        self._sala_atendimento = sala_atendimento

    def set_crp(self, crp):
        self._crp = crp

    def get_crp(self):
        return self._crp

    def set_sala_atendimento(self, sala_atendimento):
        self._sala_atendimento = sala_atendimento

    def get_sala_atendimento(self):
        return self._sala_atendimento

class Recrutadora(FuncionarioRH):
    def __init__(self, nome:str = None, matricula:str = None, idade:int = 0, meta_contratacao:int = 0 , qtd_contratacao:int= 0 , tipo_recrutamento:str = None, vagas_disponiveis:list = None):
        super().__init__(nome, matricula, idade, meta_contratacao, qtd_contratacao)
        self._tipo_recrutamento = tipo_recrutamento
        self._vagas_disponiveis = vagas_disponiveis

    def set_tipo_recrutamento(self, tipo_recrutamento):
        self._tipo_recrutamento = tipo_recrutamento

    def get_tipo_recrutamento(self):
        return self._tipo_recrutamento

    def set_vagas_disponiveis(self, vagas_disponiveis):
        self._vagas_disponiveis = vagas_disponiveis

    def get_vagas_disponiveis(self):
        return self._vagas_disponiveiso

class Desenvolvedor(FuncionarioTI):
    def __init__(self, nome:str = None, matricula:str  = None, idade:int = 0, senha_rede:str  = None, id_computador:str  = None, linguagem:list  = None, senioridade:str  = None):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self._linguagem = linguagem
        self._senioridade = senioridade

    def set_linguagem(self, linguagem):
        self._linguagem = linguagem

    def get_linguagem(self):
        return self._linguagem

    def set_senioridade(self, senioridade):
        self._senioridade = senioridade

    def get_senioridade(self):
        return self._senioridade

class Suporte(FuncionarioTI):
    def __init__(self, nome:str  = None , matricula:str  = None, idade:int = 0, senha_rede:str  = None, id_computador:str  = None, setor:str  = None, especialidade:str  = None):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self._setor = setor
        self._especialidade = especialidade

    def set_setor(self, setor):
        self._setor = setor

    def get_setor(self):
        return self._setor

    def set_especialidade(self, especialidade):
        self._especialidade = especialidade

    def get_especialidade(self):
        return self._especialidade

f = Funcionario()
f.set_idade(23)
#f.set_nome('Fulano')
#f.set_matricula ('n1230an')
#f = Funcionario(23)
#f.set_idade(23)
print(f.get_idade())

#frh = FuncionarioRH(25,'nome', '121314', 100,13)

#fti = FuncionarioTI(30, 'Bruno', '3454', 'senha_teste', 3453535)

#ftidev = Desenvolvedor(30, 'Bruno', '3454', 'senha_teste', 3453535, ['Python','Java'], 'QA PL')

#print(frh.idade)

#print(fti.idade)

#print(ftidev.linguagem)
