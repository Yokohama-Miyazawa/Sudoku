import sys
import subprocess


def read_cnf(filename='board.txt'):
    init_board = []

    with open(filename, 'r') as f:
        for i in f.readlines():
            init_board.append(i.split())

    return init_board


def output_decode(output, size):
    results = []
    for i in output:
        cnf_var = int(i)
        if cnf_var <= 0:
            continue
        result = cnf_var % size if cnf_var % size else size
        results.append(result)
    return results


def main():
    args = sys.argv
    input_file = args[1]

    # 各マスに変数を割り当てる
    squares = []
    cnf_var = 0
    size = 9
    block_size = int(size**0.5)

    for i in range(size):
        row = []
        for j in range(size):
            square = []
            for k in range(size):
                square.append((cnf_var+1)+k)
            cnf_var += size
            row.append(square)
        squares.append(row)

    # CNFに出力する各行
    cnf_line = []

    # 各マスにはある値が入る
    for i in range(size):
        for j in range(size):
            cnf_line.append(' '.join(map(str, squares[i][j])) + ' 0')

    # 各行に一つの数字は一個だけ
    for i in range(size):
        for j in range(size):
            for j2 in range(j+1, size):
                for k in range(size):
                    cnf_line.append("-" + str(squares[i][j][k]) + " -" +
                                    str(squares[i][j2][k]) + " 0")

    # 各列に一つの数字は一個だけ
    for j in range(size):
        for i in range(size):
            for i2 in range(i+1, size):
                for k in range(size):
                    cnf_line.append("-" + str(squares[i][j][k]) + " -" +
                                    str(squares[i2][j][k]) + " 0")

    # 各ブロックで数字は重複しない
    for g in range(block_size):
        for h in range(block_size):
            leftup_x, leftup_y = block_size * g, block_size * h
            for i in range(leftup_x, leftup_x+block_size):
                for j in range(leftup_y, leftup_y+block_size):
                    for i2 in range(leftup_x, leftup_x+block_size):
                        for j2 in range(leftup_y, leftup_y+block_size):
                            if i > i2 or (i == i2 and j >= j2):
                                continue
                            for k in range(size):
                                cnf_line.append("-" + str(squares[i][j][k]) +
                                                " -" + str(squares[i2][j2][k])
                                                + " 0")

    # 初期盤面の情報
    init_board = read_cnf(input_file)
    for i in range(size):
        for j in range(size):
            init_val = int(init_board[i][j])
            if init_val > 0:
                k = (init_val % size if init_val % size else size) - 1
                cnf_line.append(str(squares[i][j][k]) + " 0")

    cnf_line = ["p cnf " + str(cnf_var) + " " + str(len(cnf_line))] + cnf_line

    with open('sudoku.cnf', 'w') as f:
        f.write('\n'.join(cnf_line) + '\n')

    #subprocess.run(["minisat", "sudoku.cnf", "output.txt"])
    subprocess.run(["./minisat", "sudoku.cnf", "output.txt"])
    #subprocess.run(["rm", "sudoku.cnf"])

    with open('output.txt', 'r') as f:
        result = f.readlines()[1].split()

    #subprocess.run(["rm", "output.txt"])

    decoded_result = output_decode(result, size)
    board = []
    for i in range(size):
        board_row = []
        for j in range(size):
            board_row.append(decoded_result.pop(0))
        board.append(board_row)

    with open('result.txt', 'w') as f:
        for i in board:
            f.write(' '.join(map(str, i)) + '\n')


if __name__ == '__main__':
    main()
