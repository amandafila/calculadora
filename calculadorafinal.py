print ("Escolha uma das opções abaixo: \n 1 - soma \n 2 - subtração \n 3 - multiplicação \n 4 - divisão \n 5 - sair")
opcao = int(input("Digite o número da operação escolhida: "))
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if opcao == 5:
    print ("Operação encerrada.")
elif opcao == 1:
    soma = num1 + num2
    print (f"O resultado é: {soma}")
elif opcao == 2:
    sub = num1 - num2
    print (f"O resultado é: {sub}")
elif opcao == 3:
    mul = num1*num2
    print (f"O resultado é: {mul}")
else:
    div = num1 /num2
    print (f"O resultado é: {div}")