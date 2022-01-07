estilo=int(input("""Esse é um teste de cores, a seguir você poderá escolher como mudar seu nome.
Estilo: 
1 = Normal
2 = Negrito
3 = Sublinhado
4 = Preencher
:"""))
if estilo==1:
    estilo=0

elif estilo==2:
    estilo=1

elif estilo==3:
    estilo=4

elif estilo==4:
    estilo=7
####################################

texto=int(input("""\nAgora vamos pro principal, qual cor você achar que combina mais com seu nome?
Preto = 1
Vermelho = 2
Verde = 3
Amarelo = 4
Azul = 5
Roxo = 6
Ciano = 7
Cinza = 8
Branco = 9
:"""))

if texto==1:
    texto=30

elif texto==2:
    texto=31

elif texto==3:
    texto=32

elif texto==4:
    texto=33

elif texto==5:
    texto=34

elif texto==6:
    texto=35

elif texto==7:
    texto=36

elif texto==8:
    texto=37

elif texto==9:
    texto=0

###########################################

nome = str(input("\nDigite aqui seu nome:"))
cor=f'\033[{estilo};{texto}m'
corf=  '\033[m'
print(f"\nOlá {cor}{nome}{corf}, é muito bom te conhecer :D")
