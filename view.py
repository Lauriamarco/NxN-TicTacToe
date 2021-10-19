def print_matrix(matrix, length):
    for i in range(30):
        print()
    space = "   "
    for i in range(length + 1):
        if i == 0:
            print("        ", end="")
        else:
            print(" ( ", chr(i + 64), " ) ", end="")
    print()
    for row in range(length):
        for col in range(length):
            if matrix[row][col] == 0:
                value = " "
            else:
                value = matrix[row][col]
            if col == 0:
                if row + 1 >= 10:
                    space = "  "
                    if row + 1 >= 100:
                        space = " "
                print("( ", row + 1, " )", space, value, "  |", end="")
            elif col == length - 1:
                print("   ", value, "   ", end="")
            else:
                print("   ", value, "  |", end="")
        print()
        if row != length - 1:
            print("       ", " ------  " * length, end="")
        print()


def length_matrix():
    while True:
        print("Inserisci la grandezza desiderata")
        length = input("il numero deve essere maggiore o uguale a 5  ...  ")
        if length.isdigit():
            if int(length) >= 5:
                return length


def num_players():
    while True:
        print("Inserisci il numero di giocatori")
        num = input("il numero deve essere maggiore o uguale a 2  ...  ")
        if num.isdigit():
            if int(num) >= 2:
                return num


def move(player):
    col = None
    row = None
    while True:
        print(f"----- Muove il giocatore :{player + 1} -----")
        print("Inserisci le coordinate della prossima mossa es (A,1)")
        y = input("y :")
        if not y.isdigit() and len(y) == 1:
            if y.isupper():
                col = ord(y) - 64
            elif y.islower():
                col = ord(y) - 96
            x = input("x :")
            if x.isdigit():
                row = int(x)
        return row, col


def start_game():
    print("-----NEW MATCH-----")


def print_point(points):
    for i in range(len(points)):
        print(f" Player: {i + 1}  -  Points :{points[i]}")


def print_err(x, y):
    if y is None or x is None:
        print("Si prega di inserire delle coordinate corrette")
    else:
        print(f"La mossa a coordinate ({chr(y + 64)},{x}) non e' valida. Riprovare")


def winner(w):
    print(f"----- IL VINCITORE E' PLAYER: {w} -----")


def rematch():
    while True:
        print("Vuoi giocare ancora?")
        r = input(" Si/No  ")
        if r == "N" or r == "n" or r == "no" or r == "NO" or r == "No":
            return False
        elif r == "S" or r == "s" or r == "SI" or r == "Si" or r == "si":
            return True
