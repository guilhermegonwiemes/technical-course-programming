from random import randint

num = randint(1, 100)

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))

    if palpite < num:
        print("O número é maior.")
    elif palpite > num:
        print("O número é menor.")
    else:
        print("Parabéns! Você acertou o número.")
        break