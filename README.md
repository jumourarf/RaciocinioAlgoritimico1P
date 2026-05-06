# 🐍 Raciocínio Algorítmico em Python

Repositório com exercícios e tarefas desenvolvidos durante o **1º período de Engenharia de Software** na disciplina de Raciocínio Algorítmico.

**Aluna:** Julia Moura  
**Curso:** Engenharia de Software  
**Período:** 1º Semestre  
**Linguagem:** Python 🐍

---

## 📚 Conteúdos Estudados

### ✅ Condicionais (`if / elif / else`)
Estruturas de decisão para controlar o fluxo do programa com base em condições.

```python
nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

### 🔁 Laços de Repetição (`for` / `while`)
Estruturas usadas para repetir blocos de código enquanto uma condição for verdadeira.

```python
# Tabuada com for
numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Contagem regressiva com while
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
```

---

### 📋 Listas e Vetores
Estrutura de dados para armazenar coleções de elementos.

```python
notas = [8.5, 7.0, 9.2, 6.8]

media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")

notas.append(10.0)   # adiciona elemento
notas.sort()          # ordena a lista
print(notas)
```

---

### 🗂️ Dicionários
Estrutura de dados que armazena pares de **chave: valor**.

```python
aluno = {
    "nome": "Julia Moura",
    "curso": "Engenharia de Software",
    "periodo": 1,
    "notas": [8.5, 9.0, 7.5]
}

print(aluno["nome"])
print(f"Média: {sum(aluno['notas']) / len(aluno['notas']):.2f}")
```

---


