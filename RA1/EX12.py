num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o ultimo número: "))
for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i)