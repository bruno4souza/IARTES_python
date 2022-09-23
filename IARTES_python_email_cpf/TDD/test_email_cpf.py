import validador as val

class TestEmail(object):
    #Testar um email valido
    def test_email_valido(self):
        v = val.Validador()
        email = 'bruno.souza@ufam.com.br'
        assert v.validar_email(email) == True

    #Testar um email invalido
    def test_email_invalido(self):
        v = val.Validador()
        email = 'bruno.souza:ufam.com.br'
        assert v.validar_email(email) == False

    #Testar um CPF valido
    def test_cpf_valido(self):
        v = val.Validador()
        cpf = '23969685052'
        assert v.validar_cpf(cpf) == True

    # Testar um CPF valido informando os pontos e trasso
    def test_cpf_valido_caracteres(self):
        v = val.Validador()
        cpf = '239.696.850-52'
        assert v.validar_cpf(cpf) == True

    # Testar um CPF invalido
    def test_cpf_invalido(self):
        v = val.Validador()
        cpf = '15235967588'
        assert v.validar_cpf(cpf) == False

    # Testar um CPF invalido que não tem os 11 digitos
    def test_cpf_invalido_menor(self):
        v = val.Validador()
        cpf = '152359675'
        assert v.validar_cpf(cpf) == False

    # Testar um CPF invalido que informe caracteres a mais
    def test_cpf_invalido_caracteres(self):
        v = val.Validador()
        cpf = '152.359.675--88'
        assert v.validar_cpf(cpf) == False