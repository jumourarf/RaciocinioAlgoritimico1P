usuarios = {"Alice": 28, "Bruno": 34, "Carla": 22}

def menu():
    print("\n=== GERENCIAMENTO DE USUARIOS ===")
    print("1 - Ver todos os usuarios")
    print("2 - Buscar usuario")
    print("3 - Adicionar usuario")
    print("4 - Atualizar idade")
    print("5 - Remover usuario (pop)")
    print("6 - Remover ultimo (popitem)")
    print("7 - Copiar dicionario")
    print("8 - Criar com fromkeys")
    print("9 - Atualizar com update")
    print("10 - Limpar tudo (clear)")
    print("11 - Criar com dict e tuplas")
    print("0 - Sair")

rodando = True

while rodando:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        print("\n-- Nomes --")
        for nome in usuarios.keys():
            print(nome)

        print("\n-- Idades --")
        for idade in usuarios.values():
            print(idade)

        print("\n-- Nome e Idade --")
        for nome, idade in usuarios.items():
            print(nome, ":", idade, "anos")

    elif opcao == "2":
        nome = input("Nome: ")
        resultado = usuarios.get(nome)
        if resultado == None:
            print("Usuario nao encontrado.")
        else:
            print(nome, "tem", resultado, "anos.")

    elif opcao == "3":
        nome = input("Nome: ")
        if nome in usuarios:
            print("Usuario ja existe.")
        else:
            idade = int(input("Idade: "))
            usuarios[nome] = idade
            print(nome, "adicionado!")

    elif opcao == "4":
        nome = input("Nome: ")
        if nome in usuarios:
            idade = int(input("Nova idade: "))
            usuarios[nome] = idade
            print("Idade atualizada!")
        else:
            print("Usuario nao encontrado.")

    elif opcao == "5":
        nome = input("Nome a remover: ")
        if nome in usuarios:
            usuarios.pop(nome)
            print(nome, "removido!")
        else:
            print("Usuario nao encontrado.")

    elif opcao == "6":
        if len(usuarios) == 0:
            print("Dicionario vazio.")
        else:
            nome, idade = usuarios.popitem()
            print("Removido:", nome, "-", idade, "anos")

    elif opcao == "7":
        copia = usuarios.copy()
        nome = input("Qual nome alterar na copia? ")
        if nome in copia:
            idade = int(input("Nova idade: "))
            copia[nome] = idade
            print("Original:", usuarios)
            print("Copia:   ", copia)
        else:
            print("Nome nao encontrado na copia.")

    elif opcao == "8":
        entrada = input("Nomes separados por virgula: ")
        nomes = entrada.split(",")
        lista_nomes = []
        for n in nomes:
            lista_nomes.append(n.strip())
        idade = int(input("Idade padrao: "))
        novo = dict.fromkeys(lista_nomes, idade)
        print("Criado:", novo)
        mesclar = input("Mesclar ao principal? (s/n): ")
        if mesclar == "s":
            usuarios.update(novo)
            print("Atualizado!")

    elif opcao == "9":
        print("Formato: Nome=Idade, Nome=Idade")
        entrada = input("> ")
        novo = {}
        pares = entrada.split(",")
        for par in pares:
            partes = par.split("=")
            nome = partes[0].strip()
            idade = int(partes[1].strip())
            novo[nome] = idade
        usuarios.update(novo)
        print("Dicionario atualizado:", novo)

    elif opcao == "10":
        confirma = input("Apagar tudo? (sim/nao): ")
        if confirma == "sim":
            usuarios.clear()
            print("Todos os usuarios removidos.")
        else:
            print("Cancelado.")

    elif opcao == "11":
        print("Formato: Nome,Idade separados por ponto e virgula")
        print("Exemplo: Ana,25;Pedro,30")
        entrada = input("> ")
        lista_tuplas = []
        partes = entrada.split(";")
        for parte in partes:
            dados = parte.split(",")
            nome = dados[0].strip()
            idade = int(dados[1].strip())
            lista_tuplas.append((nome, idade))
        novo = dict(lista_tuplas)
        print("Criado:", novo)
        mesclar = input("Mesclar ao principal? (s/n): ")
        if mesclar == "s":
            usuarios.update(novo)
            print("Atualizado!")

    elif opcao == "0":
        print("Ate logo!")
        rodando = False

    else:
        print("Opcao invalida.")