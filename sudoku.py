def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            cell_value = board[i][j]
            print(cell_value if cell_value != 0 else ".", end=" ")
        print()

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def is_subgrid_completed(board, subgrid_row, subgrid_col):
    subgrid = [board[i][j] for i in range(subgrid_row * 3, subgrid_row * 3 + 3) for j in range(subgrid_col * 3, subgrid_col * 3 + 3)]
    return sorted(subgrid) == list(range(1, 10))

def is_board_completed(board):
    for subgrid_row in range(3):
        for subgrid_col in range(3):
            if not is_subgrid_completed(board, subgrid_row, subgrid_col):
                return False
    return True

def play_sudoku():
    initial_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Bem-vindo ao Sudoku!")
    print("Para preencher uma célula vazia, insira a linha, a coluna e o valor (por exemplo, '3 2 7').")

    while not is_board_completed(initial_board):
        print_board(initial_board)
        user_input = input("Digite sua jogada (linha coluna valor) ou 'q' para sair: ")
        if user_input.lower() == 'q':
            break

        try:
            row, col, value = map(int, user_input.split())
            if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= value <= 9:
                if initial_board[row - 1][col - 1] == 0:
                    if is_valid_move(initial_board, row - 1, col - 1, value):
                        initial_board[row - 1][col - 1] = value
                        print("Jogada válida!")
                    else:
                        print(f"Essa jogada não é válida. O valor {value} já está presente na mesma linha, coluna ou subgrade.")
                else:
                    print(f"A célula ({row}, {col}) já está preenchida com o valor {initial_board[row - 1][col - 1]}.")
            else:
                print("Valores inválidos. As linhas, colunas e valores devem estar entre 1 e 9.")
        except ValueError:
            print("Entrada inválida. Use o formato 'linha coluna valor' (por exemplo, '3 2 7').")

    if is_board_completed(initial_board):
        print("Parabéns! Você resolveu o Sudoku.")
    print("Saindo do Sudoku.")

if __name__ == "__main__":
    play_sudoku()
