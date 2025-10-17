# def soma():
#     n1 = float(input("Digite o primeiro número: "))
#     n2 = float(input("Digite o segundo número: "))
#     result = n1 + n2
#     return result
# print(soma()) 

# def subtracao():
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resulta = num1 - num2
#     return resulta
# print(subtracao()) 

# def multiplicacao():
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resulta = num1 * num2
#     return resulta
# print(multiplicacao()) 

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        return("Nenhum numero pode ser dividido por 0")
    else:
        resulta = num1 / num2
    return resulta
print(divisao()) 