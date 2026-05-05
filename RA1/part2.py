for i in range(2):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    ma = (n1 + n2 + n3 + n4)/4

    print(f"Média anual = {ma:.2f}")

    if ma >=7:
        print("Aprovado")
    else:
        print("Reprovado")