import re

class Validador:
    def validar_email(self, email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        email_return = True
        if (re.search(regex, email)):
            email_return = True
        else:
            email_return = False
        return email_return

    def validar_cpf(self, cpf):
        #Valida a mascara do CPF
        regex = re.compile('([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})')
        cpf_return = True
        if (re.search(regex, cpf)):
            cpf_return = True
        else:
            cpf_return = False
        count_cpf = [int(count_digito) for count_digito in cpf if count_digito.isdigit()] #Separa os digitos do CPF
        if len(count_cpf) != 11 or len(set(count_cpf)) == 1:
            return False
        sum_of_products = sum(a * b for a, b in zip(count_cpf[0:9], range(10, 1, -1))) #Verifica o primeiro validador
        expected_digit = (sum_of_products * 10 % 11) % 10
        if count_cpf[9] != expected_digit:
            cpf_return = False
        sum_of_products = sum(a * b for a, b in zip(count_cpf[0:10], range(11, 1, -1))) #Verifica o segundo validador
        expected_digit = (sum_of_products * 10 % 11) % 10
        if count_cpf[10] != expected_digit:
            cpf_return = False

        return cpf_return