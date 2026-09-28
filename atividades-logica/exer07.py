numeros = []
for i in range(3):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
print(f"O maior número digitado é: {max(numeros)}")