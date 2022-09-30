from abc import ABC, abstractmethod

class Funcionario(object):
    def __init__(self, idade:int, nome:str, matricula:str):
        self.idade = idade
        self.nome = nome
        self.matricula = matricula

    def set_idade(self, idade:int):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_nome(self, nome:str):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_matricula(self, matricula:str):
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula

    @abstractmethod
    def pegar_funcionario(self):
        return print("Funcionario Contratado")

    def maiorIdade(self):
        if self.idade >= 18:
            return True
        else:
            return False


class FuncionarioRH(Funcionario):
    def __init__(self, nome:str, matricula:str, idade:int, meta_contratacao:int, qtd_contratacao:int):
        super().__init__(nome, matricula, idade)
        self.meta_contratacao = meta_contratacao
        self.qtd_contratacao = qtd_contratacao

    def set_meta_contratacao(self, meta_contratacao):
        self.meta_contratacao = meta_contratacao

    def get_meta_contratacao(self):
        return self.meta_contratacao

    def set_qtd_contratacao(self, qtd_contratacao):
        self.qtd_contratacao = qtd_contratacao

    def get_qtd_contratacao(self):
        return self.qtd_contratacao

    @abstractmethod
    def recrutar_funcionario(self):
        pass

    @abstractmethod
    def palestrar(self):
        pass

class FuncionarioTI(Funcionario):
    def __init__(self, nome:str, matricula:str, idade:int, senha_rede:str, id_computador:int):
        super().__init__(nome, matricula, idade)
        self.senha_rede = senha_rede
        self.id_computador = id_computador

    def set_senha_rede(self, senha_rede):
        self.senha_rede = senha_rede

    def get_senha_rede(self):
        return self.senha_rede

    def set_senha_rede(self, id_computador):
        self.id_computador = id_computador

    def get_senha_rede(self):
        return self.id_computador

    @abstractmethod
    def logar_rede(self):
       pass

class Psicologa(FuncionarioRH):
    def __init__(self, nome:str, matricula:str, idade:int, meta_contratacao:int, qtd_contratacao:int, crp:str, sala_atendimento:str):
        super().__init__(nome, matricula, idade, meta_contratacao, qtd_contratacao)
        self.crp = crp
        self.sala_atendimento = sala_atendimento

    def set_crp(self, crp):
        self.crp = crp

    def get_crp(self):
        return self.crp

    def set_sala_atendimento(self, sala_atendimento):
        self.sala_atendimento = sala_atendimento

    def get_sala_atendimento(self):
        return self.sala_atendimento

class Recrutadora(FuncionarioRH):
    def __init__(self, nome:str, matricula:str, idade:int, meta_contratacao:int, qtd_contratacao:int, tipo_recrutamento:str, vagas_disponiveis:list):
        super().__init__(nome, matricula, idade, meta_contratacao, qtd_contratacao)
        self.tipo_recrutamento = tipo_recrutamento
        self.vagas_disponiveis = vagas_disponiveis

    def set_tipo_recrutamento(self, tipo_recrutamento):
        self.tipo_recrutamento = tipo_recrutamento

    def get_tipo_recrutamento(self):
        return self.tipo_recrutamento

    def set_vagas_disponiveis(self, vagas_disponiveis):
        self.vagas_disponiveis = vagas_disponiveis

    def get_vagas_disponiveis(self):
        return self.vagas_disponiveiso

class Desenvolvedor(FuncionarioTI):
    def __init__(self, nome:str, matricula:str, idade:int, senha_rede:str, id_computador:str, linguagem:list, senioridade:str):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self.linguagem = linguagem
        self.senioridade = senioridade

    def set_linguagem(self, linguagem):
        self.linguagem = linguagem

    def get_linguagem(self):
        return self.linguagem

    def set_senioridade(self, senioridade):
        self.senioridade = senioridade

    def get_senioridade(self):
        return self.senioridade

class Suporte(FuncionarioTI):
    def __init__(self, nome:str, matricula:str, idade:int, senha_rede:str, id_computador:str, setor:str, especialidade:str):
        super().__init__(nome, matricula, idade, senha_rede, id_computador)
        self.setor = setor
        self.especialidade = especialidade

    def set_setor(self, setor):
        self.setor = setor

    def get_setor(self):
        return self.setor

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

    def get_especialidade(self):
        return self.especialidade

f = Funcionario(23,'nome', '1826180265')

frh = FuncionarioRH(25,'nome', '121314', 100,13)

fti = FuncionarioTI(30, 'Bruno', '3454', 'senha_teste', 3453535)

ftidev = Desenvolvedor(30, 'Bruno', '3454', 'senha_teste', 3453535, ['Python','Java'], 'QA PL')

print(frh.idade)

print(fti.idade)

print(ftidev.linguagem)
