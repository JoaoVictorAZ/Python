salario=float(input("Informe o valor base do salário:"))
reajuste=float(input("Coloque aqui a porcentagem do reajuste:"))
valorr=salario*(reajuste/100)
valorfinal=salario+valorr
print(f"\nValor do reajuste: {valorr}\nSalário após reajuste: {valorfinal}")
