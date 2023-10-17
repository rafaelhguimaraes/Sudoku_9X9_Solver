# Especificação da Versão do Sudoku com Subgrades

O Sudoku é um jogo baseado na colocação lógica de números inteiros em uma grade M x M. O objetivo do jogo é a colocação de números de 1 a M em cada célula da grade M x M, de forma que em todas as colunas e linhas da grade não ocorra a repetição de nenhum número.

Na versão mais complexa do Sudoku, a grade deve ser do tipo M² x M² (N = M², para N e M inteiros), de forma que a grade principal pode ser dividida em subgrades menores de tamanho M x M. Assim, o objetivo do jogo é a colocação de números de 1 a N em cada célula da grade M² x M², de forma que em todas as colunas e linhas da grade não ocorra a repetição de nenhum número e também com a restrição adicional de não haver repetição dos números de 1 a N nas subgrades M x M. O quebra-cabeça possui algumas pistas iniciais, que são números inseridos em algumas células e cabe ao desafiante descobrir que valores colocar no restante das células vazias de forma a atender as restrições do puzzle. 

Por exemplo, uma possível configuração inicial do puzzle 9x9, com subgrades 3x3 (N=9 e M=3) é vista na Figura a, contemplando as dicas iniciais, enquanto a Figura b apresenta uma solução final para essa instância, onde é possível verificar que não existem repetições nas 9 linhas, nas 9 colunas e também nas 9 subgrades 3x3.
