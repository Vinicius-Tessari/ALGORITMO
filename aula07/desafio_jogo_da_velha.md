# Desafio de Programação — Jogo da Velha Básico

## Objetivo

Criar um **Jogo da Velha básico** utilizando programação, aplicando conceitos de:

- variáveis;
- listas;
- estruturas condicionais;
- laços de repetição;
- funções;
- validação de entrada;
- lógica de vitória e empate.

O jogo deve funcionar no terminal.

---

## Descrição do desafio

O aluno deverá desenvolver um programa que permita que **dois jogadores** joguem Jogo da Velha.

O jogador 1 utilizará o símbolo **X**.  
O jogador 2 utilizará o símbolo **O**.

O jogo termina quando:

1. um dos jogadores vencer;
2. todas as posições forem preenchidas e houver empate.

---

## Modelo do tabuleiro

O tabuleiro deve possuir 9 posições, organizadas em 3 linhas e 3 colunas.

Exemplo:

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

Durante o jogo, os números devem ser substituídos por **X** ou **O**.

Exemplo:

```text
 X | 2 | O
-----------
 4 | X | 6
-----------
 O | 8 | 9
```

---

## Regras obrigatórias

O programa deve:

1. Exibir o tabuleiro na tela.
2. Permitir que dois jogadores joguem alternadamente.
3. Solicitar ao jogador a posição onde deseja jogar.
4. Validar se a posição digitada existe.
5. Validar se a posição escolhida ainda está livre.
6. Atualizar o tabuleiro após cada jogada.
7. Verificar se algum jogador venceu.
8. Verificar se houve empate.
9. Exibir uma mensagem final informando o vencedor ou empate.

---

## Condições de vitória

O programa deve verificar vitória nas seguintes possibilidades:

### Linhas

```text
1, 2, 3
4, 5, 6
7, 8, 9
```

### Colunas

```text
1, 4, 7
2, 5, 8
3, 6, 9
```

### Diagonais

```text
1, 5, 9
3, 5, 7
```

---

## Exemplo de funcionamento esperado

```text
Bem-vindo ao Jogo da Velha!

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Jogador X, escolha uma posição: 5

 1 | 2 | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9

Jogador O, escolha uma posição: 1

 O | 2 | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9
```

Ao final:

```text
Jogador X venceu!
```

Ou:

```text
O jogo terminou empatado!
```

---

## Funções sugeridas

O aluno pode organizar o código usando funções como:

```python
def mostrar_tabuleiro(tabuleiro):
    pass

def validar_jogada(tabuleiro, posicao):
    pass

def fazer_jogada(tabuleiro, posicao, jogador):
    pass

def verificar_vitoria(tabuleiro, jogador):
    pass

def verificar_empate(tabuleiro):
    pass
```

Essas funções são sugestões. O aluno pode criar outras funções, desde que o jogo funcione corretamente.

---

## Regras de validação

O programa não deve permitir:

- escolher uma posição menor que 1;
- escolher uma posição maior que 9;
- escolher uma posição já ocupada;
- quebrar o programa caso o usuário digite algo inválido.

Exemplo:

```text
Jogador X, escolha uma posição: 12
Posição inválida. Escolha um número de 1 a 9.
```

```text
Jogador O, escolha uma posição: 5
Essa posição já está ocupada. Escolha outra.
```

---

## Desafio extra

Para ganhar ponto extra, o aluno poderá implementar uma ou mais melhorias:

- permitir jogar novamente sem reiniciar o programa;
- contar placar dos jogadores;
- permitir o jogador escolher o próprio nome;
- limpar a tela a cada rodada;
- criar uma opção contra o computador;
- melhorar o visual do tabuleiro.

---

## Entrega

O aluno deverá entregar:

1. O arquivo `.py` com o código do jogo.
2. O programa funcionando sem erros.
3. O código organizado e comentado quando necessário.

---

## Observação importante

O objetivo do desafio não é apenas fazer o jogo funcionar.

O mais importante é demonstrar a lógica utilizada para:

- controlar turnos;
- validar entradas;
- atualizar o tabuleiro;
- verificar vitória;
- identificar empate.

Programar jogo da velha parece simples, mas se a lógica estiver bagunçada, vira jogo da velha possuído. Organização salva vidas — e notas também.
