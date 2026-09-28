valor = float(input("Digite o valor de uma compra: "))

if(valor > 100):
    valor_final = valor * 0.9
    print(f"O valor final com desconto é: {valor_final}")
else:
    print(f"O valor final é: {valor}")