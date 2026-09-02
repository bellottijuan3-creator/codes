# Lista de exercicicos

# Exercicio 1

lado = float(input("Digite o valor do lado: "))
area = lado * lado

print(f"A area do quadrado de lado {lado} é: {area}")

###########################
# Exercicio 2


salario = float(input("Digite seu salário: "))
reajuste = salario * 0.15

print(f"Seu salario com o novo reajuste é {salario + reajuste}")

###########################
# Exercicio 3

altura = float(input("Digite a altura do triangulo: "))
base = float(input("Digite a base do triangulo: "))
area = (base * altura) / 2

print(f"A area do triangulo é {area}")

###########################
# Exercicio 4 


c = float(input("Digite quantos Graus Celcius você quer converter "))
f = (9*c+160)/5
print(f"{c} Graus Celcius convertido em F, fica: {f}")

###########################
# Exercicio 5


a = int(input("Digite o coeficiente A: "))
b = int(input("Digite o coeficiente B: "))
c = int(input("Digite o coeficiente C: "))
delta = (b * b) - (4 * a * c)
print(f"O delta é {delta}")
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

print(f"O valor de X1 = {x1}\n"
      f"O valor de X1 = {x2}")

###########################
# Exercicio 6


v1 = input("Digite o valor 1 a ser trocado: ")
v2 = input("Digite o valor 2 a ser trocado: ")

print(f"O primeiro valor antes era {v1}\n"
      f"O segundo valor antes era {v2}")
d = v1
v1 = v2
v2 = d
print(f"O primeiro valor depois da troca agora é {v1}\n"
      f"O segundo valor depois da troca agora é {v2}"),

###########################
# Exercicio 7


altura = float(input("Digite o valor da altura: "))
largura = float(input("Digite o valor da largura: "))
comprimento = float(input("Digite o valor do comprimento: "))
area = altura * largura * comprimento






