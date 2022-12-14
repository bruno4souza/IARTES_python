# Projeto final para a disciplina de Python

## 1. Introdução

Nosso programa vai contextualizar o registro de funcionarios de uma Startup  através de uma programação orientada a objetos, na qual vamos abstrair diversas funções e cargos, que são comuns em setores presentes no mercado de trabalho.  

## 2. A hierarquia

Pensando em um cenário real de uma empresa, a seguinte hierarquia será implementada. 

Teremos funcionário e esses funcinários são divididos entre funcionários de RH e funcionários de TI, os funcionários de RH podem ser psicólogos e recrutadores, já os funcionários de TI podem ser desenvolvedores e suporte.

## 3. Herança

Como é possível perceber, o esquema de funcionários da nossa empresa pode ser implementado utilizando o conceito de herança da orientação a objeto. Assim, a nossa classe pai será "Funcionário" as classes "Funcionário de RH" e "Funcionário de TI" serão classes filhas e por sua vez as classes Psicologa, Recrutadora, Desenvolvedor e Suporte serão classes netas como pode ser observado na imagem abaixo.

![3.1](Imagens/hierarquiaFunc.png)

## 4. Polimorfismo

Para implementar o polimorfismo utilizaremos o método "Pagamento_funcionario" que será um método da classe Funcinário mas que será implementado diferente por cada um dos funcionários do sistema. Abaixo segue as imagem que mostram a implementação para cada um dos tipos de funcionários.

4.1 Pisicólogo

Para o pagamento do cardo de psicólogo a conta do pagamento é feita com base na palestra oferecida, caso o atributo seja True o salário é dobrado

![4.1](Imagens/pagfuncpsi.png)

4.2 Recrutadora

Para o pagamento de recrutadora, o salário se basea na meta de contratação obtida, caso a meta seja atingida o salário é muntiplicado por 4 caso não seja é multiplicado por 1.5.

![4.2](Imagens/pagfuncrecrut.png)

4.3 Suporte

Para o profissional de suporte a regra se basea no setor, caso ele seja do setor de segurança o salário é dobrado se não ele recebe mais uma multiplicação de 1.5

![4.3](Imagens/pagfuncsuporte.png)

4.4 Desenvolvedor

Para os desenvolvedores o salário é baseado na senioridade, júnior recebe o salário base, pleno o dobro do salário base e o sénior recebe o triplo do salário base

![4.4](Imagens/pagfuncdev.png)

## 5. Encapsulamento

Para todos os atributos que são referentes a classe principal (Funcionário), utilizamos o conceito de encapsulamento de orientação a objeto. Por isso, esses atributos são todos privados e só podem ser acessados usando os métodos set/get. Na imagem abaixo segue um exemplo da implementação do conceito de encapsulamento.

![5.1](Imagens/encapsulamento1.png)

## 6. Relatório de cobertura de código

Nossa primeira execução de cobertura de teste que alcançou 67%. Nessa primeira execução, testamos o método de validar se o funcionário é meior de idade ou não e focamos nos set/get dos atributos que são da classe principal (Funcionário), também fizemos testes para os atributos da classe filha (FuncionárioRH.)

![6.1](Imagens/porcentagem1.png)

A segunda execução conseguimos 87% porcento de cobertura. Testamos os atributos que faltaram dos profissionais de TI e da psicologa que é uma sub-classe de FuncionárioRH.

![6.2](Imagens/oitentaporcento.png)

Na terceira vez que rodamos atingimos os 100% de cobertura das tarefas implementadas. Foram verificados as linhas de código faltantes.

![6.3](Imagens/cemporcento.png)
