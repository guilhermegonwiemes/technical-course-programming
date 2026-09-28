numero = float(input('Digite um número:'))

for i in range(11):
    resultado = numero * i
    print(f'{numero} x {i} = \033[32m{resultado}\033[0m')