string_s = "sitting"
string_t = "kitten"


def levenshtein(string_s, string_t):
    del_cost = 1
    ins_cost = 1
    first_row = []
    first_col = []
    row = len(string_s) + 1
    col = len(string_t) + 1
    for i in range(len(string_s) + 1):
        first_row.append(i)
    for i in range(len(string_t) + 1):
        first_col.append(i)
    matrix = [[0] * col for _ in range(row)]
    # Them phan tu cho hang 1 va cot 1
    for r in range(col):
        matrix[0][r] = first_col[r]
    for c in range(row):
        matrix[c][0] = first_row[c]
    for r in range(1, row):
        for c in range(1, col):
            if string_s[r-1] == string_t[c-1]:
                sub_cost = 0
            else:
                sub_cost = 1
            matrix[r][c] = min(matrix[r - 1][c] + del_cost, matrix[r]
                               [c - 1] + ins_cost, matrix[r-1][c-1] + sub_cost)

    for r in range(row):
        for c in range(col):
            print(matrix[r][c], end=' ')
        print()

    return matrix[(row - 1)][(col - 1)]


print(levenshtein(string_s, string_t))
