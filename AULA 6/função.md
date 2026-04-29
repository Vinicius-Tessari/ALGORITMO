# O que é uma função?

Uma **função** é um bloco de código que faz uma tarefa específica.

Pense nela como uma **máquina**:

você coloca algo (entrada)
ela processa
devolve um resultado (saída)

---

# Estrutura básica

```python
def nome_da_funcao(parametros):
    # código
    return resultado
```

---

# Exemplo 1 — Função simples

```python
def dizer_ola():
    print("Olá!")
```

### Como usar:

```python
dizer_ola()
```

### O que acontece:

* você chama a função
* ela executa o código dentro dela
* imprime: `Olá!`

---

# Exemplo 2 — Com entrada (parâmetro)

```python
def dizer_ola(nome):
    print(f"Olá, {nome}!")
```

### Uso:

```python
dizer_ola("João")
```

### Resultado:

```
Olá, João!
```

Aqui o `nome` é um **parâmetro** (valor que entra na função)

---

# Exemplo 3 — Com retorno (`return`)

```python
def somar(a, b):
    return a + b
```

### Uso:

```python
resultado = somar(5, 3)
print(resultado)
```

### Resultado:

```
8
```

`return` devolve o valor para quem chamou a função

---

# Exemplo 4 — Função útil

```python
def converter_minutos_para_segundos(minutos):
    return minutos * 60
```

### Uso:

```python
segundos = converter_minutos_para_segundos(5)
print(segundos)
```

### Resultado:

```
300
```

---

# Resumão

Uma função:

* evita repetir código
* organiza melhor o programa
* facilita leitura
* permite reutilização

---

# Analogia simples

Função = **receita de bolo**

* ingredientes → parâmetros
* preparo → código
* bolo pronto → retorno

---

**Fim**
