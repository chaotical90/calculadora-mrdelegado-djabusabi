# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para divisão
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."
# Função para multiplicação
def multiplicacao(x, y):
    return x * y
# Função principal
def calculadora():
    lista_historico = []
    while (True):

        print('Quer o calcular o que?')
        op = input("Digite a operacao: ")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        resultado_soma = soma(num1, num2)
        resultado_subtracao = subtracao(num1, num2)
        resultado_divisao = divisao(num1, num2)
        resultado_multiplicacao = multiplicacao(num1, num2)
        if op == '+':
            print("Resultado da soma: " + str(resultado_soma))
            lista_historico.append(resultado_soma)
        if op == '-':
            print("Resultado da subtração: " + str(resultado_subtracao))
            lista_historico.append(resultado_subtracao)
        if op == '/':
            print("Resultado da divisão: " + str(resultado_divisao))
            lista_historico.append(resultado_divisao)
        if op == '*':
            print("Resultado da multiplicação: " + str(resultado_multiplicacao))
            lista_historico.append(resultado_multiplicacao)
        if op == "hist":
            print("lista do historico: ")

# Executa a calculadora
calculadora()
