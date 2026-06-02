def calculadora():
    while True:
        print('=========================')
        print("Calculadora Simples")
        print('=========================')
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        print('-------------------------')
        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a Calculadora Simples!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação soma é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação subtração é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação multiplicação é: ", resultado)

        elif operacao == '4':
            if numero_2 != 0:
                resultado = numero_1 / numero_2
                print("O resultado da operação divisão é: ", resultado)
            else:
                print("Erro: Divisão por zero não é permitida.")

calculadora()