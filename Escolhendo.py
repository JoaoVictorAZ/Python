import random
n1= str(input("Digite o nome da primeira pessoa:"))
n2= str(input("digite o nome da segunda pessoa:"))
n3= str(input("digite o nome da terceira pessoa:"))
n4= str(input("digite o nome da ultima pessoa:"))
lista=(n1,n2,n3,n4)
print(f"\nO escolhido é {random.choice(lista)}")
