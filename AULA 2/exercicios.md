# Exercícios com FOR

## Regras gerais
- Use `for` obrigatoriamente em todos os exercícios.
- Valide entradas quando fizer sentido (ex.: não aceitar números negativos onde não faz sentido).
- Mostre resultados com mensagens claras.

---

## 1) Tabuada completa
Peça ao usuário um número inteiro `n` e mostre a tabuada de `n` de 1 até 10, no formato:
n x i = resultado

---

## 2) Soma de 1 até N
Peça um número inteiro `n` e calcule a soma de todos os números de 1 até `n` usando `for`.
Exemplo: n = 5 -> 1+2+3+4+5 = 15

---

## 3) Contagem de pares e ímpares
Peça um número inteiro `n` e conte quantos números entre 1 e `n` são pares e quantos são ímpares.
Exiba as duas quantidades.

---

## 4) Soma apenas dos pares
Peça um número inteiro `n` e some somente os números pares de 1 até `n`.
Exiba a soma final.

---

## 5) Maior e menor de uma lista de números
Peça ao usuário quantos números ele quer digitar (`qtd`).
Depois, leia `qtd` números e ao final mostre:
- o maior número
- o menor número

---

## 6) Média com validação
Peça quantas notas o usuário quer informar (`qtd`).
Leia as notas (0 a 10). Se digitar fora do intervalo, peça novamente.
Calcule e mostre a média final.

---

## 7) Contar vogais em uma frase
Peça ao usuário uma frase e conte quantas vogais existem nela (a, e, i, o, u).
Ignore maiúsculas/minúsculas.
Exiba o total de vogais.

---

## 8) Inverter uma string manualmente
Peça ao usuário um texto e gere uma versão invertida usando `for`.
Não use fatiamento `[::-1]`.

---

## 9) Fatorial de N
Peça um número inteiro `n` (n >= 0) e calcule `n!` usando `for`.
Exemplos:
0! = 1
5! = 120

---

## 10) Verificar número primo
Peça um número inteiro `n` e verifique se ele é primo.
Mostre "Primo" ou "Não primo".
Dica: conte quantos divisores `n` tem.

---

## 11) Somar dígitos de um número
Peça um número inteiro positivo e some seus dígitos usando `for` percorrendo a string do número.
Exemplo: 358 -> 3 + 5 + 8 = 16

---

## 12) Contar ocorrências de um caractere
Peça ao usuário um texto e depois um caractere.
Conte quantas vezes esse caractere aparece no texto (ignorando maiúsculas/minúsculas).

---

## 13) Gerar lista de múltiplos
Peça um número inteiro `base` e um limite `limite`.
Mostre todos os múltiplos de `base` entre 1 e `limite`.

---

## 14) Relatório de números (resumo)
Peça ao usuário quantos números ele quer digitar (`qtd`).
Leia os números e ao final mostre:
- soma total
- média
- maior
- menor
- quantidade de positivos, negativos e zeros

---

## Desafio 1) Padrão de asteriscos (crescendo)
Peça um número inteiro `n` e mostre um triângulo de asteriscos com `n` linhas:
*
**
***
...
(n linhas)

---

## Desafio 2) Separar e somar por posição
Peça um número inteiro `n` e calcule:
- soma dos números em posições pares (2ª, 4ª, 6ª...) de 1 até n
- soma dos números em posições ímpares (1ª, 3ª, 5ª...) de 1 até n
Exiba as duas somas.