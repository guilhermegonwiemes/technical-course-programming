numeros = []
contador = 1
while contador < 11:
    numeros.append(contador)
    print(contador)
    contador += 1
print(f'A soma dos números de 1 até 10 é: {sum(numeros)}')