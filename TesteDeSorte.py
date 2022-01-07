import random
num= int(random.randrange(0,5))
numero= int(input("O computador escolherá um numero de 0 até 5, tente adivinhar qual número é:"))
if num==numero:
    print(f"\nO número escolhido pelo computador foi: {num}")
    print(f"O número que você escolheu foi: {numero}")
    print("\nUau, você realmente é bem sortudo, parabéns, você acertou :D")
else:
    print(f"\nO número escolhido pelo computador foi: {num}")
    print(f"O número que você escolheu foi: {numero}")
    print("\nInfelizmente a resposta está errada D:")
