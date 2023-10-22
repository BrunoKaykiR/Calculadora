#### CALCULADORA #####

from Calculadora import soma, sub, multi, divi
from time import sleep


while True:
    print('\n\n\t\t\t\t\tSeja Bem-Vindo a Calculadora')

    operation = input('Digite o símbolo da operação:\n[+] Soma\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n[>_] Sair\n').upper().strip()

    match operation:
        case '+':
            number1 = float(input('Insira o primeiro número: '))
            number2 = float(input('Insira o segundo número: '))
            print(f'O resultado de {number2} + {number2} = {soma(number1, number2):.2f}\n')

        case '-':
            number1 = float(input('Insira o primeiro número: '))
            number2 = float(input('Insira o segundo número: '))
            print(f'O resultado de {number2} - {number2} = {sub(number1, number2):.2f}\n')

        case '*':
            number1 = float(input('Insira o primeiro número: '))
            number2 = float(input('Insira o segundo número: '))
            print(f'O resultado de {number2} - {number2} = {multi(number1, number2):.2f}\n')

        case '/':
            number1 = float(input('Insira o primeiro número: '))
            number2 = float(input('Insira o segundo número: '))
            print(f'O resultado de {number2} - {number2} = {divi(number1, number2):.2f}\n')

        case '>_':
            print('Finalizando o Sistema...\n')
            sleep(2)
            print('SISTEMA FINALIZADO!')
            break

        case _:
            print('ERROR! Opção Inválida!')

    stop = input('Deseja realizar outra operação? (Y/N) ').upper().strip()

    match stop:
        case 'Y':
            print('Reiniciando o sistema, aguarde...')
            sleep(2)

        case 'N':
            print('Finalizando o Sistema...\n')
            sleep(2)
            print('SISTEMA FINALIZADO!')
            break
