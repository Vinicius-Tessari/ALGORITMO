# Como Funciona uma Matriz em Programação

## 1. O que é uma matriz?

Uma **matriz** é uma estrutura usada para armazenar dados em formato de **linhas e colunas**.

Ela funciona como uma tabela.

Exemplo visual:

```text
1  2  3
4  5  6
7  8  9
```

Essa matriz possui:

- 3 linhas;
- 3 colunas.

Por isso, podemos dizer que ela é uma matriz **3x3**.

---

## 2. Matriz em Python

Em Python, uma matriz pode ser representada usando **listas dentro de listas**.

Exemplo:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Cada lista interna representa uma linha da matriz.

```python
[1, 2, 3]  # primeira linha
[4, 5, 6]  # segunda linha
[7, 8, 9]  # terceira linha
```

---

## 3. Entendendo linhas e colunas

A matriz abaixo:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Pode ser vista assim:

```text
        coluna 0   coluna 1   coluna 2
linha 0     1          2          3
linha 1     4          5          6
linha 2     7          8          9
```

Em Python, a contagem começa em **0**.

Ou seja:

```text
Primeira linha  -> linha 0
Segunda linha   -> linha 1
Terceira linha  -> linha 2
```

O mesmo acontece com as colunas:

```text
Primeira coluna -> coluna 0
Segunda coluna  -> coluna 1
Terceira coluna -> coluna 2
```

Python começa contando do zero. Estranho no começo, normal depois. Tipo café sem açúcar.

---

## 4. Como acessar um valor da matriz

Para acessar um valor da matriz, usamos:

```python
matriz[linha][coluna]
```

Exemplo:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][0])
```

Saída:

```text
1
```

Explicação:

```python
matriz[0][0]
```

Significa:

```text
linha 0, coluna 0
```

Ou seja, o primeiro valor da matriz.

---

## 5. Exemplos de acesso

Usando esta matriz:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Temos:

```python
print(matriz[0][0])  # 1
print(matriz[0][1])  # 2
print(matriz[0][2])  # 3

print(matriz[1][0])  # 4
print(matriz[1][1])  # 5
print(matriz[1][2])  # 6

print(matriz[2][0])  # 7
print(matriz[2][1])  # 8
print(matriz[2][2])  # 9
```

---

## 6. Como alterar um valor da matriz

Também podemos modificar um valor da matriz.

Exemplo:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[1][1] = "X"

print(matriz)
```

Resultado:

```python
[
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]
```

O valor `5` foi substituído por `"X"`.

Isso aconteceu porque:

```python
matriz[1][1]
```

representa a posição do meio da matriz.

---

## 7. Como percorrer uma matriz

Para percorrer uma matriz, usamos um `for` dentro de outro `for`.

Exemplo:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor)
```

Saída:

```text
1
2
3
4
5
6
7
8
9
```

O primeiro `for` percorre as linhas.

O segundo `for` percorre os valores dentro de cada linha.

---

## 8. Mostrando a matriz em formato de tabela

Podemos mostrar a matriz de forma mais organizada:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()
```

Saída:

```text
1 2 3
4 5 6
7 8 9
```

Explicação:

```python
print(valor, end=" ")
```

Mostra os valores na mesma linha, separados por espaço.

Já este comando:

```python
print()
```

quebra a linha depois que todos os valores daquela linha foram exibidos.

---

## 9. Exemplo prático: Jogo da Velha

Um tabuleiro de jogo da velha pode ser representado por uma matriz.

```python
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
```

Visualmente:

```text
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

Se o jogador escolher o centro do tabuleiro, podemos fazer:

```python
tabuleiro[1][1] = "X"
```

Resultado:

```text
1 | 2 | 3
4 | X | 6
7 | 8 | 9
```

---

## 10. Exibindo um tabuleiro de jogo da velha

```python
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

for linha in tabuleiro:
    print(" | ".join(linha))
```

Saída:

```text
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

O comando:

```python
" | ".join(linha)
```

junta os valores da linha colocando `|` entre eles.

---

## 11. Convertendo posição do jogador para linha e coluna

Em um jogo da velha, o jogador normalmente escolhe uma posição de 1 a 9.

Exemplo:

```text
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

Mas a matriz usa linha e coluna.

Por isso, usamos este cálculo:

```python
linha = (posicao - 1) // 3
coluna = (posicao - 1) % 3
```

Exemplo com a posição 5:

```python
posicao = 5

linha = (posicao - 1) // 3
coluna = (posicao - 1) % 3

print(linha)
print(coluna)
```

Saída:

```text
1
1
```

Ou seja, a posição 5 corresponde a:

```python
tabuleiro[1][1]
```

Que é o centro do tabuleiro.

---

## 12. Tabela de conversão

| Posição digitada | Linha | Coluna |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 0 | 1 |
| 3 | 0 | 2 |
| 4 | 1 | 0 |
| 5 | 1 | 1 |
| 6 | 1 | 2 |
| 7 | 2 | 0 |
| 8 | 2 | 1 |
| 9 | 2 | 2 |

---

## 13. Exemplo completo simples

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")

for linha in matriz:
    print(linha)

matriz[1][1] = 0

print("Matriz alterada:")

for linha in matriz:
    print(linha)
```

Saída:

```text
Matriz original:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Matriz alterada:
[1, 2, 3]
[4, 0, 6]
[7, 8, 9]
```

---

## 14. Resumo

Uma matriz é uma estrutura com **linhas e colunas**.

Em Python, usamos listas dentro de listas:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Para acessar um valor:

```python
matriz[linha][coluna]
```

Para alterar um valor:

```python
matriz[linha][coluna] = novo_valor
```

Para percorrer:

```python
for linha in matriz:
    for valor in linha:
        print(valor)
```


