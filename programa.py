import math
import emoji
from operacoes import *
while True:
    operacao = int(input("Escolha a operação: 1- Adição; 2- Subtração; 3- Multiplicação; 4- Divisão; 0- Para encerrar o codigo: "))
    if operacao == 1:
        print(soma())
    elif operacao == 2:
        print(subtracao())
    elif operacao == 3:
        print(multiplicacao())
    elif operacao == 4:
        print(divisao())
    elif operacao == 0:
        break
print(emoji.emojize('Obrigado por usar nosso pograma! :thumbs_up:'))