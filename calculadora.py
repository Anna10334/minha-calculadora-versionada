# Atividade 13 - Versionamento em Etapas com Git e VS Code
# Etapa 1: O Início do Projeto (1º Commit)

def soma_de_dois_numeros (numero1, numero2):
    soma_de_dois_numeros = numero1 + numero2
    return soma_de_dois_numeros
# Realizando a soma entre os dois numeros


# Etapa 2: Adicionando Funcionalidade (2º Commit)

def subtracao_de_dois_numeros (numero1, numero2):
    subtracao_de_dois_numeros = numero1 - numero2
    return subtracao_de_dois_numeros
# Realizando a subtração entre os dois numeros


# Etapa 3: Melhorando a Interação (3º Commit)

def multiplicacao_de_dois_numeros (numero1, numero2):
    multiplicacao_de_dois_numeros = numero1 * numero2
    return multiplicacao_de_dois_numeros
# Realizando a multiplicação entre os dois numeros

while True: # Loop do Menu de opcões
    print("""
    Selecione uma operação:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    5. Sair
    """)
    preferencia = input("Insira o número da operação desejada:")
    if preferencia == "5":
        print("Saindo do programa")
        break # Programa para assim que for selecionado a opção "5", que é sair.
    elif preferencia in ["1", "2", "3", "4"]:
        num1 = float (input("Digite o primeiro número: ")) # Entrada do primeiro número,
        num2 = float (input("Digite o segundo número: ")) # Entrada do Segundo número.
        if preferencia =="1":
            resultado = soma_de_dois_numeros (num1, num2)
            print(f"O Resultado da soma: {num1} + {num2} = {resultado}")
        elif preferencia== "2":
            resultado = subtracao_de_dois_numeros (num1, num2)
            print(f"O Resultado da subtração: {num1} - {num2} = {resultado}")
        elif preferencia == "3":
            resultado = multiplicacao_de_dois_numeros (num1, num2)
            print(f"O Resultado da multiplicação: {num1} * {num2} = {resultado}") 
        elif preferencia== "4":
            resultado = dividisao_de_dois_numeros (num1, num2)
            print(f"O Resultado da divisão: {num1} / {num2} = {resultado}")
    else:
        print("Opção inválida. Tente novamente")

# Acima ocorre o 'Menu de opções', que permite ao usuário escolher entre soma, subtração, multiplicação e divisão tendo assim um loop do menu de opções caso o mesmo queira inserir novamente outros dados.


# Etapa 4: Finalizando o Programa (4º Commit)

def dividisao_de_dois_numeros (numero1, numero2):
    try:
        if numero2 == 0:
            return "Erro! Não é possível dividir por zero"
    except ZeroDivisionError:
        print("Opção inválida. Por favor, tente novamente.")
    else:
        dividisao_de_dois_numeros = numero1 / numero2
        print(f" A divisao dos dois números é : {dividisao_de_dois_numeros}")

# Realizando a divisão entre os dois numeros e o tratamento de erro garantindo que o programa não quebre se o usuário tentar dividir por zero.



