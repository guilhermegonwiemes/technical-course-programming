saldo = 1000
tentativas = 0
saques = 0


def login():
       global tentativas
       username = input("\nInsira o Nome do Usuário: ").lower()
       password = input("\nInsira a Senha do Usuário: ")
      
       if username == "carlos" and password == "7242":
           print("\nAcesso Autorizado\n")
           menu()
           return
       else:
           if tentativas < 3:
               print("\nO usuário ou a senha estão incorretos\n")
               tentativas = tentativas + 1
               print("Tentativa número", tentativas)
               login()
           else:
               print("\nLimite de Tentativas Atingido!")


def menu():
   print("\n   === Menu ===\n\nO que você gostaria de fazer?\n [1] Consultar Saldo\n [2] Depositar\n [3] Sacar\n [4] Sair\n")
   opcao = int(input("\nDigite sua opção: \n"))
  
   if opcao == 1:
       checar_saldo()
   elif opcao == 2:
       depositar()
   elif opcao == 3:
       sacar()
   elif opcao == 4:
       print("\nObrigado por usar nosso sistema!\n")
       return
   else:
       print("\nOpção inválida!\n")
       menu()


def checar_saldo():
   print("\nO seu saldo é R$", saldo,"\n")
   menu()


def depositar():
   global saldo  # ← Corrigido: era "saldo1"
  
   deposito = float(input("Você gostaria de depositar dinheiro?\n\n [0] Não quero Depositar\n [1] Quero depositar: "))
  
   if deposito == 0:
       menu()
   elif deposito == 1:
       valordeposito = float(input("\nQuanto dinheiro você gostaria de depositar? R$ "))
      
       # Atualiza o saldo SEMPRE que há depósito
       saldo = saldo + valordeposito
      
       if valordeposito > 1.99:
           print("\nPerfeito! R$", valordeposito, "foram depositados em sua conta!\n")
       else:
           print("\nPerfeito! R$", valordeposito, "foi depositado em sua conta!\n")
          
       print("\nSeu novo saldo é R$", saldo, "\n")
       menu()


def sacar():
   global saques
   saque = float(input("\nVocê gostaria de sacar dinheiro?\n\n [0] Não\n [1] Sim\n"))
   if saque == 0:
        menu()
   else:
       if saques < 5:
           saques = saques + 1
           contanotas()
       else:
           print("\nVocê atingiu seu limite de saques diários (5), volte amanhã para sacar mais\n")
           menu()


def contanotas():
   global saldo
  
   # Declaração das variáveis da Cédulas
   valor_original = 0
   nota100 = 0
   nota50 = 0
   nota20 = 0
   nota10 = 0
   nota5 = 0
   nota2 = 0
   nota1 = 0


   valor_original = int(input("\nQuanto dinheiro você quer sacar? R$ "))


   if valor_original > saldo:
       print("\nVocê não pode sacar mais do que tem!")
       print("Seu saldo atual é R$", saldo, "\n")
       sacar()
   else:
       valor_restante = valor_original
      
       nota100 = valor_restante // 100
       valor_restante = valor_restante % 100


       nota50 = valor_restante // 50
       valor_restante = valor_restante % 50


       nota20 = valor_restante // 20
       valor_restante = valor_restante % 20


       nota10 = valor_restante // 10
       valor_restante = valor_restante % 10


       nota5 = valor_restante // 5
       valor_restante = valor_restante % 5


       nota2 = valor_restante // 2 
       valor_restante = valor_restante % 2


       nota1 = valor_restante // 1
      
       print("\nVocê irá receber essas notas a seguir:\n")
       print(nota100, "nota(s) de R$100")
       print(nota50, "nota(s) de R$50")
       print(nota20, "nota(s) de R$20")
       print(nota10, "nota(s) de R$10")
       print(nota5, "nota(s) de R$5")
       print(nota2, "nota(s) de R$2")
       print(nota1, "nota(s) de R$1")




       saldo = saldo - valor_original
      
       print(f"\nSaque de R$ {valor_original} realizado com sucesso!")
       print(f"Seu novo saldo é R$ {saldo}\n")


       menu()


login()

