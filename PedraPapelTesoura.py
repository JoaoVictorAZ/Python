from random import randrange
pedra="1"
papel="2"
tesoura="3"
pontoc=0
pontoh=0

print("\n\033[1;31mSeja bem vindo ao Jokenpo (Pedra, Papel ou Tesoura)\033[m")
rodadas=int(input("Escolha quantas rodadas você quer que o jogo tenha: "))
for x in range(rodadas):
    print(f"\033[1;31mBem Vindo a Rodada {x+1}\033[m\n")
    escolha = int(input("""Escolha a opção que você deseja jogar:
        [1] = Pedra 
        [2] = Papel
        [3] = Tesoura
        : """))

    if escolha>0 and escolha<4:
        computador = randrange(1, 4)
        print(f"""\033[1;32mVocê escolheu\033[m {escolha}
\033[1;34mO computador escolheu\033[m {computador}
""")

        if computador == escolha:
            print("Uau, Você não perdeu... Mas também não ganhou, isso foi um empate.\n")
            pontoc +=1
            pontoh +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        ##
        elif computador == 1 and escolha == 2:
            print("Parabéns, escreveu sua vitória com esse papel hein?\n")
            pontoh +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        elif computador == 1 and escolha == 3:
            print("Ixe maria, Você foi QUEBRADO pela máquina\n")
            pontoc +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        ##
        elif computador == 2 and escolha == 1:
            print("Você foi embrulhado pelo papel digital\n")
            pontoc +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        elif computador == 2 and escolha == 3:
            print("Tsc Tsc Tsc, sua tesoura passou pelo papel sem dificuldades\n")
            pontoh +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        ##
        elif computador == 3 and escolha == 1:
            print("Sua pedra ESBUGALHOU a tesoura inimiga\n")
            pontoh +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
        elif computador == 3 and escolha == 2:
            print("A tesoura digital te rasgou papelzinho ;-;\n")
            pontoc +=1
            print(f"Seus pontos:{pontoh}\nPontos da máquina: {pontoc}\n---------------------------------")
    else:
        print("Você não escolheu um número válido")
    if x+1==rodadas:
        if pontoc > pontoh:
            print(f"""\033[1;31mResultado:\033[m 
Seus pontos:{pontoh}
Pontos da máquina: {pontoc}
A Skynet te venceu dessa vez, mas quem sabe na próxima...""")
        elif pontoc == pontoh:
            print(f"""\033[1;31mResultado:\033[m
Seus pontos:{pontoh}
Pontos da máquina: {pontoc}
Wow calma lá amigão, você empatou com a máquina? você sabe que isso é raro né?""")
        elif pontoc < pontoh:
            print(f"""\033[1;31mResultado:\033[m
Seus pontos:{pontoh}
Pontos da máquina: {pontoc}
TEEEEEMOS UM NOVO CAMPEÃO DE JOKENPO, PARABENS VOCÊ VENCEU A MÁQUINA""")
