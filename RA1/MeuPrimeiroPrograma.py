print ("Meu primeiro programa!")
# 1. Definir a variavel peso
p = 75.5

#Exemplo usando .format()
print("Você pesa {} quilos".format(p))

#Exemplo usando f-string
print(f"Voce pesa {p} quilos")

# Usuario digitando o peso:
p = input("Digite seu peso: ")
print(f"Voce pesa {p} quilos")

# --- EXEMPLO 1: Inteiro
X = int(input("Informe o valor de X: "))
print(f"O dobro de X e: {X * 2}")

# --- EXEMPLO 2: Float
Y = float(input("Informe o valor de Y: "))
print(f"O valor de Y com 20% de bonus e: {Y * 1.2}")

# --- EXEMPLO 3: Multiplas entradas
#Nota: No Python lemos uma por uma
A = bool(input("Informe o valor de A (Apere enter para falso ou digite algo para verdadeiro): "))
XPTO = input("Informe o valor de XPTO (Texto): ")
Nota = float(input("Informe o valor de Nota: "))

print("-" * 20)
print(f"Resultado: A={A}, XPTO={XPTO}, Nota={Nota}")