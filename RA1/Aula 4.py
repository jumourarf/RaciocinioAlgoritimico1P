#Exercicio 1: simples
print ("No Brasil o voto é permitido a partir dos 16 anos!")
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print ("Você ja pode votar!")
else:
    print ("Você ainda não tem idade para votar!")

#Exercicio 2: composto
numero = int(input("Digite um numero inteiro: "))
if numero > 0:
    print("O número é positivo!")
elif numero < 0:
    print("O número é negativo!")
else:
    print("O número é zero!")

#Exercicio 3: simples
compra = float(input("Digite o valor do compra: "))
desconto = float(compra * 0.10)
total = compra - desconto
if compra > 100:
    print (total)
else:
    print (compra)
    print ("Nas compras acima de R$100,00 você ganha 10% de desconto")

#Exercicio 4: composto
nota = float(input("Digite sua nota: "))
if nota >= 9:
    print ("Parabéns!! Você foi aprovado!!")
elif 7 < nota < 8.9:
    print ("Aprovado!")
elif 4 < nota < 6.9:
    print ("Você está em recuperação!")
else:
    print ("Reprovado!")

#Exercicio 5: simples
numero = int(input("Digite um numero inteiro: "))
if numero % 2 == 0:
    print("Esse número é par!")
else:
    print("Esse número é impar!")

#Exercicio 6: simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print (numero1)
else:
    print (numero2)

#Exercício 7: simples
usuario_correto = "julia"
digite = input("Digite o nome do usuário: ")
if digite == usuario_correto:
    print("Acesso liberado!")
else:
    print("Usuário desconhecido!")

#Exercício 8: simples
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = (peso / altura ** 2)
if IMC > 25:
    print ("Acima do peso ideal!")
else:
    print("Peso dentro da normalidade!")

#Exercicio 9: condicional
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))
if lado1 == lado2 == lado3:
    print("Triangulo equilatero!")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Triangulo Isosceles")
else:
    print("Triangulo Escaleno")

#Exercicio 10: simples
numero = int(input("Digite um numero inteiro: "))
if numero % 5 == 0:
    print("O número é multiplo de 5!")
else:
    print("O número não é multiplo de 5!")

#Exercicio 11: condicional
idade = int(input("Digite sua idade: "))
if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 10:
    print("Infantil B")
elif 11 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
else:
    print("Adultos")

#Execicio 12: condicional
distancia = float(input("Digite a distância que deseja percorrer em km:"))
menor = distancia * 0.50
maior = distancia * 0.45
if distancia <= 200:
    print(menor)
elif distancia > 200:
    print(maior)
else:
    print("Invalido")

#Exercicio 13: simples
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print ("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")

#Exercicio 14: simples
salario = float(input("Digite o seu salario: "))
bonificacao1 = salario * 0.10
total1 = salario + bonificacao1
bonificacao2 = salario * 0.15
total2 = salario + bonificacao2
if salario > 1621:
    print(total1)
else:
    print(total2)


#Exercicio 15: simples
veloc = float(input("Digite o velocidade do carro: "))
if veloc > 80:
    multa = (veloc - 80) * 7
    print("Você foi multado, o valor é: ", multa)
else:
    print("Você esta dentro da valocidade permitida")

#Exercicio 16: composto
temperatura = float(input("Digite uma temperatura em celcius: "))
escolha = str(input("Converter para fahrenheit ou kelvin: "))
fahrenheit = float
kelvin = float
if escolha == "fahrenheit":
    print(temperatura * 4.5 + 32)
elif escolha == "kelvin":
    print(temperatura + 273.15)
else:
    print("A temperatura é: ")

#Eexrcicio 17; simples
area = float(input("Digite a área em metros a ser pintada: "))
if area > 54:
    print("Precisa de mais de uma lata.")
else:
    print("O total da sua compra é de R$80,00.")

#Exercício 18: simples
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Digite quantos anos deseja pagar: "))
total = salario * 0.30
prestacao = (valor / anos) / 12
if prestacao > total:
    print("Não é possível fazer o empréstimo")
else:
    print("É possivel fazer o emprestimo")
