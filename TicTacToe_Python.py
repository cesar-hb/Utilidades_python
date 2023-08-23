# Mi primer intento de un juego de gato, cuando aun no sabia como hacer funciones.

fig = ""
count_x = 0
count_o = 0
count_blank = 0
count_turns = 2
count_xturns = 0
flag_fig = 0
flag_x = False
flag_o = False
flag_ongoing = False
sign = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
matrix = [[sign[0], sign[1], sign[2]],
          [sign[3], sign[4], sign[5]],
          [sign[6], sign[7], sign[8]]]
print(f"""---------
| {sign[0]} {sign[1]} {sign[2]} |
| {sign[3]} {sign[4]} {sign[5]} |
| {sign[6]} {sign[7]} {sign[8]} |
---------""")
while True:
    try:
        move = input("Enter the coordinates: ").split()
    except ValueError:
        print("You should enter numbers!")
        continue
    if move[0].isalpha() or move[1].isalpha():
        print("You should enter numbers!")
        continue
    elif 0 >= int(move[0]) or int(move[0]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif 0 >= int(move[1]) or int(move[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    move = int(move[0]) - 1 + (9 - (3 * int(move[1])))
    if sign[move] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    if (count_turns % 2) == 0:
        sign[move] = "X"
    elif count_turns % 2 == 1:
        sign[move] = "O"
    count_turns += 1
    print(f"""---------
    | {sign[0]} {sign[1]} {sign[2]} |
    | {sign[3]} {sign[4]} {sign[5]} |
    | {sign[6]} {sign[7]} {sign[8]} |
    ---------""")
    matrix[0][0] = sign[0]
    matrix[0][1] = sign[1]
    matrix[0][2] = sign[2]
    matrix[1][0] = sign[3]
    matrix[1][1] = sign[4]
    matrix[1][2] = sign[5]
    matrix[2][0] = sign[6]
    matrix[2][1] = sign[7]
    matrix[2][2] = sign[8]
    # Esto es un remanente de lo mal que hize la logica de matrices,
    ya que no pude asociar con una funcion las dos lecturas de matrices que necesitaba.
    for i in range(3):
        for j in range(3):
            fig = matrix[i][j]
            if fig == "X":
                count_x += 1
            if fig == "O":
                count_o += 1
            if fig == "_":
                count_blank += 1
            if j < 1:
                if matrix[i][j - 1] == fig == matrix[i][j + 1] and fig != "_":
                    if fig == "X":
                        flag_x = True
                    elif fig == "O":
                        flag_o = True
            if i < 1:
                if matrix[i - 1][j] == fig == matrix[i + 1][j] and fig != "_":
                    if fig == "X":
                        flag_x = True
                    elif fig == "O":
                        flag_o = True
    if matrix[1][1] == "X":
        if matrix[0][0] == "X" and matrix[2][2] == "X":
            flag_x = True
        if matrix[0][2] == "X" and matrix[2][0] == "X":
            flag_x = True
    if matrix[1][1] == "O":
        if matrix[0][0] == "O" and matrix[2][2] == "O":
            flag_o = True
        if matrix[0][2] == "O" and matrix[2][0] == "O":
            flag_o = True
    if count_blank > 0 and not flag_x and not flag_o:
        flag_ongoing = True
    count_xturns += 1
    if flag_x:
        print("X wins")
        break
    elif flag_o:
        print("O wins")
        break
    elif not flag_x and not flag_o and count_xturns == 9:
        print("Draw")
        break
