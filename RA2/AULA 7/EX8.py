alunos = {"Julia": 10,
       "Valentina": 10,
       "Veronica": 7,
       "Henrique": 8}
nome = input("Nome do aluno: ")
nota = alunos.get(nome, "Aluno não encontrado!")
print(nota)