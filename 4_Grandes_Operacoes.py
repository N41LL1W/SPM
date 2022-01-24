def Arredonde001():
    from random import randint
    cont = 1
    repete = 'S'
    pontos = 0

    print('╔'+'═'*65+'╗')
    print('║\033[;7m'+' '*12+'DESAFIO DE MATEMÁTICA - AREDONDE O NÚMERO'+' '*12+'\033[m║')
    print('╠'+'═'*65+'╣')
    while repete != 'N':
        escolha = randint(10, 1000)
        casa = randint(1, 2)
        espaco = 0
        espaco2 = 0
        espaco3 = 0
        if escolha > 11 and escolha < 100:
            p1 = 10
            p2 = 10
            p3 = 5
            casa = 'dezena'
            if cont <=9:
                espaco = 3
            elif cont >=10 and cont <= 999 or cont < 0:
                espaco = 2

            if pontos <= 9:
                espaco2 = 25
                espaco3 = 29
            elif pontos >= 10 and pontos <= 999:
                espaco2 = 24
                espaco3 = 28

        elif escolha > 101 and escolha < 1000:
            if casa == 1:
                p1 = 10
                p2 = 10
                p3 = 5
                casa = 'dezena'
                if cont <= 9:
                    espaco = 2
                else:
                    espaco = 1

                if pontos <= 9:
                    espaco2 = 25
                    espaco3 = 29
                elif pontos >= 10 and pontos <= 999:
                    espaco2 = 24
                    espaco3 = 28
            else:
                p1 = 100
                p2 = 100
                p3 = 50
                casa = 'centena'
                if cont <= 9:
                    espaco = 1
                else:
                    espaco = 0

                if pontos <= 9:
                    espaco2 = 25
                    espaco3 = 29
                elif pontos >= 10 and pontos <= 999:
                    espaco2 = 24
                    espaco3 = 28

        print(f'║ \033[34;1m Questão {cont}.\033[m Arredonde o número {escolha} para a {casa} mais próxima.'+' '*espaco + '║')
        quest = escolha
        resp = float(input('║  Resposta: '+' '*53 + '║\n' + '║' + ' '*5))

        verif = quest % p1

        if verif >= p3:
            verif = (p2 - verif) + quest
        else:
            verif = quest - verif

        while resp != verif:
            if resp != verif:
                print('║'+' '*3 + '\033[1;41mINCORRETO! Tente novamente.\033[m'+' '*35 + '║')
                pontos = pontos - 1
                print('║' + ' ' * 3 + '\033[31mVocê NÃO pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * espaco2 + '║')
                resp = float(input('║  Resposta: '+' '*53 + '║\n' + '║' + ' '*5))

        print('║'+' '*3 + '\033[1;42mCERTO! PARABÉNS!!!\033[m'+' '*44 + '║')
        pontos = pontos + 3
        print('║'+' '*3 + '\033[32mVocê pontuou, agora tem {} pontos.\033[m'.format(pontos)+' '* espaco3 + '║')
        cont += 1
        repete = str(input('║'+' '*3 + 'Proxima Questão? [ S ] ou [ N ]'+' '*31 + '║\n' + '║' + ' '*5)).upper()[0:1]

def Soma001():

    from random import randint
    cont = 1
    repete = 'S'
    pontos = 0

    print('╔'+'═'*65+'╗')
    print('║\033[;7m'+' '*13+'DESAFIO DE MATEMÁTICA - SOME OS NÚMEROS'+' '*13+'\033[m║')
    print('╠'+'═'*65+'╣')

    print('║\033[1;33m'+' '*13+'Escolha o que somar: '+' '*31+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 1 ] Unidades'+' '*38+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 2 ] Dezenas'+' '*39+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 3 ] Centenas'+' '*38+'\033[m║')

    escolha = int(input('║'+' '*13+'\033[1;43mSua escolha:'+'\033[m '*40 + '║\n' + '║' + ' '*13))
    print('╠'+'═'*65+'╣')

    if escolha == 1:
        p1 = 1
        p2 = 10
    elif escolha == 2:
        p1 = 10
        p2 = 100
    elif escolha == 3:
        p1 = 100
        p2 = 1000
    num1 = randint(p1, p2)
    num2 = randint(p1, p2)
    print('║\033[1;34m'+' '*13+'Questão {}.\033[m Calcule a soma de {} + {}'.format(cont, num1, num2)+' '*18+'║')
    soma = num1 + num2
    resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

    while resp != soma:
        if resp != soma:
            print('INCORRETO! Tente novamente.')
            resp = float(input('Resposta: '))

    print('CERTO! PARÁBENS!!!')

def Subtracao001():

    from random import randint
    p1 = 1
    p2 = 10

    print('''Escolha o que subtrair: 
    [ 1 ] Unidades
    [ 2 ] Dezenas
    [ 3 ] Centenas''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1 or escolha == 2 or escolha == 3:
        if escolha == 1:
            p1 = 1
            p2 = 10
        elif escolha == 2:
            p1 = 10
            p2 = 100
        elif escolha == 3:
            p1 = 100
            p2 = 1000
    else:
        print('Opção inválida!')
        print('''Escolha o que subtrair: 
        [ 1 ] Unidades
        [ 2 ] Dezenas
        [ 3 ] Centenas''')
        escolha = int(input('Sua escolha: '))
    num1 = randint(p1, p2)
    num2 = randint(p1, p2)
    print('Questão. Calcule a subtração de {} - {}'.format(num1, num2))
    soma = num1 - num2
    resp = float(input('Resposta: '))

    while resp != soma:
        if resp != soma:
            print('INCORRETO! Tente novamente.')
            resp = float(input('Resposta: '))

    print('CERTO! PARÁBENS!!!')

def Multiplicacao001():

    from random import randint

    print('''Escolha o que multiplicar: 
    [ 1 ] Unidades
    [ 2 ] Dezenas
    [ 3 ] Centenas''')
    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        p1 = 1
        p2 = 10
    elif escolha == 2:
        p1 = 10
        p2 = 100
    elif escolha == 3:
        p1 = 100
        p2 = 1000
    num1 = randint(p1, p2)
    num2 = randint(p1, p2)
    print('Questão. Calcule a soma de {} x {}'.format(num1, num2))
    produto = num1 * num2
    resp = float(input('Resposta: '))

    while resp != produto:
        if resp != produto:
            print('INCORRETO! Tente novamente.')
            resp = float(input('Resposta: '))

    print('CERTO! PARÁBENS!!!')

def Divisao001():

    from random import randint

    print('''Escolha o que dividir: 
    [ 1 ] Unidades
    [ 2 ] Dezenas
    [ 3 ] Centenas''')
    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        p1 = 1
        p2 = 10
    elif escolha == 2:
        p1 = 10
        p2 = 100
    elif escolha == 3:
        p1 = 100
        p2 = 1000
    num1 = randint(p1, p2)
    num2 = randint(p1, p2)
    print('Questão. Calcule a soma de {} ÷ {}'.format(num1, num2))
    quociente = num1 / num2
    resp = float(input('Resposta: '))

    while resp != quociente:
        if resp != quociente:
            print('INCORRETO! Tente novamente.')
            resp = float(input('Resposta: '))

    print('CERTO! PARÁBENS!!!')

Soma001()