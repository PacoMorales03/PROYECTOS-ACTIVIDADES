sudoku = [
    [3, 0, 0, 4, 6, 1, 0, 0, 0],  # Fila N (Suma = 14)
    [0, 0, 0, 0, 0, 0, 0, 0, 1],  # Fila A (Suma = 1)
    [1, 6, 0, 0, 8, 2, 0, 0, 4],  # Fila T (Suma = 20)
    [0, 0, 0, 0, 0, 0, 0, 0, 1],  # Fila A (Suma = 1)
    [0, 0, 2, 1, 0, 4, 0, 5, 0],  # Fila L (Suma = 12)
    [0, 0, 0, 2, 3, 0, 0, 4, 0],  # Fila I (Suma = 9)
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # Fila A (Suma = 1)
    [0, 0, 4, 0, 9, 0, 0, 0, 0],  # Fila G (Suma = 7)
    [0, 0, 1, 0, 0, 2, 0, 0, 0]   # Fila C (Suma = 3)
]
def correcto(tablero, fil, col, num):
    if num in tablero[fil]:
        return False
    for i in range(9):
        if tablero[i][col] == num:
            return False
    fil_ini = (fil // 3) * 3
    col_ini = (col // 3) * 3
    for i in range(fil_ini, fil_ini + 3):
        for j in range(col_ini, col_ini + 3):
            if tablero[i][j] == num:
                return False
    
    return True
def resolver(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                for num in range(1, 10):
                    if correcto(tablero, fila, col, num):
                        tablero[fila][col] = num 
                        if resolver(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True 
def imprimir(tablero):
    for fil in tablero:
        print(fil)

if resolver(sudoku):
    imprimir(sudoku)
else:
    print("El Sudoku no tiene solución.")