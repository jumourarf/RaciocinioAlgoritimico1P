idade = int(input("Digite sua idade: "))
if 0 <= idade <= 17:
    print("Menor de idade!")
elif 18 <= idade <= 59:
    print("Adulto!")
else:
    print("Idoso!")