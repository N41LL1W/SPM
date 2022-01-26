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

    while repete != 'N':

        p1 = 0
        q1 = 0
        ps1 = 0
        ps2 = 0

        if pontos <= 9:
            ps1 = 29
            ps2 = 25
        elif pontos >= 10 and pontos <= 99:
            ps1 = 28
            ps2 = 24
        elif pontos >= 100 and pontos <= 999:
            ps1 = 27
            ps2 = 23

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
        if escolha == 1:
            if num1 <= 9 and num2 <= 9:
                q1 = 18
            elif num1 >= 10 and num2 >= 10:
                q1 = 16
            else:
                q1 = 17
        elif escolha == 2:
            if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99):
                q1 = 16
            else:
                q1 = 15
        elif escolha == 3:
            if (num1 >= 100 and num1 <= 999) and (num2 >= 100 and num2 <= 999):
                q1 = 14
            else:
                q1 = 13

        print('║\033[1;34m'+' '*13+'Questão {}.\033[m Calcule a soma de {} + {}'.format(cont, num1, num2)+' '*q1+'║')
        soma = num1 + num2
        resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        while resp != soma:

            if resp != soma:
                print('║'+' '*13+'\033[1;41mINCORRETO! Tente novamente.'+'\033[m '*25  + '║' + ' '*3)
                pontos -= 1
                print('║' + ' ' * 3 + '\033[31mVocê NÃO pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps2 + '║')
                resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        print('║'+' '*13+'\033[1;42mCERTO! PARÁBENS!!!'+'\033[m '*34 + '║\n' + '║' + ' '*3)
        pontos += 3
        print('║' + ' ' * 3 + '\033[32mVocê pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps1 + '║')
        cont += 1
        repete = str(input('║' + ' ' * 3 + 'Proxima Questão? [ S ] ou [ N ]' + ' ' * 31 + '║\n' + '║' + ' ' * 5)).upper()[
                 0:1]
    print('╚' + '═' * 65 + '╝')

def Subtração001():

    from random import randint
    cont = 1
    repete = 'S'
    pontos = 0

    print('╔'+'═'*65+'╗')
    print('║\033[;7m'+' '*13+'DESAFIO DE MATEMÁTICA - SUBTRAIA OS NÚMEROS'+' '*13+'\033[m║')
    print('╠'+'═'*65+'╣')

    print('║\033[1;33m'+' '*13+'Escolha o que subtrair: '+' '*31+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 1 ] Unidades'+' '*38+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 2 ] Dezenas'+' '*39+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 3 ] Centenas'+' '*38+'\033[m║')


    escolha = int(input('║'+' '*13+'\033[1;43mSua escolha:'+'\033[m '*40 + '║\n' + '║' + ' '*13))
    print('╠'+'═'*65+'╣')

    while repete != 'N':

        p1 = 0
        q1 = 0
        ps1 = 0
        ps2 = 0

        if pontos <= 9:
            ps1 = 29
            ps2 = 25
        elif pontos >= 10 and pontos <= 99:
            ps1 = 28
            ps2 = 24
        elif pontos >= 100 and pontos <= 999:
            ps1 = 27
            ps2 = 23

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
        if escolha == 1:
            if num1 <= 9 and num2 <= 9:
                q1 = 18
            elif num1 >= 10 and num2 >= 10:
                q1 = 16
            else:
                q1 = 17
        elif escolha == 2:
            if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99):
                q1 = 16
            else:
                q1 = 15
        elif escolha == 3:
            if (num1 >= 100 and num1 <= 999) and (num2 >= 100 and num2 <= 999):
                q1 = 14
            else:
                q1 = 13

        print('║\033[1;34m'+' '*13+'Questão {}.\033[m Calcule a subtração de {} - {}'.format(cont, num1, num2)+' '*q1+'║')
        soma = num1 - num2
        resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        while resp != soma:

            if resp != soma:
                print('║'+' '*13+'\033[1;41mINCORRETO! Tente novamente.'+'\033[m '*25  + '║' + ' '*3)
                pontos -= 1
                print('║' + ' ' * 3 + '\033[31mVocê NÃO pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps2 + '║')
                resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        print('║'+' '*13+'\033[1;42mCERTO! PARÁBENS!!!'+'\033[m '*34 + '║\n' + '║' + ' '*3)
        pontos += 3
        print('║' + ' ' * 3 + '\033[32mVocê pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps1 + '║')
        cont += 1
        repete = str(input('║' + ' ' * 3 + 'Proxima Questão? [ S ] ou [ N ]' + ' ' * 31 + '║\n' + '║' + ' ' * 5)).upper()[
                 0:1]
    print('╚' + '═' * 65 + '╝')

def Multiplicação001():

    from random import randint
    cont = 1
    repete = 'S'
    pontos = 0

    print('╔'+'═'*65+'╗')
    print('║\033[;7m'+' '*13+'DESAFIO DE MATEMÁTICA - MULTIPLIQUE OS NÚMEROS'+' '*13+'\033[m║')
    print('╠'+'═'*65+'╣')

    print('║\033[1;33m'+' '*13+'Escolha o que multiplicar: '+' '*31+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 1 ] Unidades'+' '*38+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 2 ] Dezenas'+' '*39+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 3 ] Centenas'+' '*38+'\033[m║')


    escolha = int(input('║'+' '*13+'\033[1;43mSua escolha:'+'\033[m '*40 + '║\n' + '║' + ' '*13))
    print('╠'+'═'*65+'╣')

    while repete != 'N':

        p1 = 0
        q1 = 0
        ps1 = 0
        ps2 = 0

        if pontos <= 9:
            ps1 = 29
            ps2 = 25
        elif pontos >= 10 and pontos <= 99:
            ps1 = 28
            ps2 = 24
        elif pontos >= 100 and pontos <= 999:
            ps1 = 27
            ps2 = 23

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
        if escolha == 1:
            if num1 <= 9 and num2 <= 9:
                q1 = 18
            elif num1 >= 10 and num2 >= 10:
                q1 = 16
            else:
                q1 = 17
        elif escolha == 2:
            if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99):
                q1 = 16
            else:
                q1 = 15
        elif escolha == 3:
            if (num1 >= 100 and num1 <= 999) and (num2 >= 100 and num2 <= 999):
                q1 = 14
            else:
                q1 = 13

        print('║\033[1;34m'+' '*13+'Questão {}.\033[m Calcule a multiplicação de {} + {}'.format(cont, num1, num2)+' '*q1+'║')
        soma = num1 * num2
        resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        while resp != soma:

            if resp != soma:
                print('║'+' '*13+'\033[1;41mINCORRETO! Tente novamente.'+'\033[m '*25  + '║' + ' '*3)
                pontos -= 1
                print('║' + ' ' * 3 + '\033[31mVocê NÃO pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps2 + '║')
                resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        print('║'+' '*13+'\033[1;42mCERTO! PARÁBENS!!!'+'\033[m '*34 + '║\n' + '║' + ' '*3)
        pontos += 3
        print('║' + ' ' * 3 + '\033[32mVocê pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps1 + '║')
        cont += 1
        repete = str(input('║' + ' ' * 3 + 'Proxima Questão? [ S ] ou [ N ]' + ' ' * 31 + '║\n' + '║' + ' ' * 5)).upper()[
                 0:1]
    print('╚' + '═' * 65 + '╝')

def Divisao001():

    from random import randint
    cont = 1
    repete = 'S'
    pontos = 0

    print('╔'+'═'*65+'╗')
    print('║\033[;7m'+' '*13+'DESAFIO DE MATEMÁTICA - DIVIDA OS NÚMEROS'+' '*13+'\033[m║')
    print('╠'+'═'*65+'╣')

    print('║\033[1;33m'+' '*13+'Escolha o que dividir: '+' '*31+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 1 ] Unidades'+' '*38+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 2 ] Dezenas'+' '*39+'\033[m║')
    print('║\033[1;33m'+' '*13+'[ 3 ] Centenas'+' '*38+'\033[m║')


    escolha = int(input('║'+' '*13+'\033[1;43mSua escolha:'+'\033[m '*40 + '║\n' + '║' + ' '*13))
    print('╠'+'═'*65+'╣')

    while repete != 'N':

        p1 = 0
        q1 = 0
        ps1 = 0
        ps2 = 0

        if pontos <= 9:
            ps1 = 29
            ps2 = 25
        elif pontos >= 10 and pontos <= 99:
            ps1 = 28
            ps2 = 24
        elif pontos >= 100 and pontos <= 999:
            ps1 = 27
            ps2 = 23

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
        if escolha == 1:
            if num1 <= 9 and num2 <= 9:
                q1 = 18
            elif num1 >= 10 and num2 >= 10:
                q1 = 16
            else:
                q1 = 17
        elif escolha == 2:
            if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99):
                q1 = 16
            else:
                q1 = 15
        elif escolha == 3:
            if (num1 >= 100 and num1 <= 999) and (num2 >= 100 and num2 <= 999):
                q1 = 14
            else:
                q1 = 13

        print('║\033[1;34m'+' '*13+'Questão {}.\033[m Calcule a divisão de {} + {}'.format(cont, num1, num2)+' '*q1+'║')
        soma = num1 + num2
        resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        while resp != soma:

            if resp != soma:
                print('║'+' '*13+'\033[1;41mINCORRETO! Tente novamente.'+'\033[m '*25  + '║' + ' '*3)
                pontos -= 1
                print('║' + ' ' * 3 + '\033[31mVocê NÃO pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps2 + '║')
                resp = float(input('║'+' '*13+'\033[34mResposta:'+'\033[m '*43 + '║\n' + '║' + ' '*13))

        print('║'+' '*13+'\033[1;42mCERTO! PARÁBENS!!!'+'\033[m '*34 + '║\n' + '║' + ' '*3)
        pontos += 3
        print('║' + ' ' * 3 + '\033[32mVocê pontuou, agora tem {} pontos.\033[m'.format(pontos) + ' ' * ps1 + '║')
        cont += 1
        repete = str(input('║' + ' ' * 3 + 'Proxima Questão? [ S ] ou [ N ]' + ' ' * 31 + '║\n' + '║' + ' ' * 5)).upper()[
                 0:1]
    print('╚' + '═' * 65 + '╝')


Divisao001()
