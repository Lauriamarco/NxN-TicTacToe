from itertools import groupby


class Match:
    game_state = True
    matrix = []
    size = 0
    num_player = []
    point = []

    def __init__(self, n, pl):
        self.size = n
        for i in range(pl):
            self.num_player.append(i + 1)  # add number of player

        for i in range(pl):
            self.point.append(0)  # add number of player

        for i in range(int(self.size)):
            row = []
            for j in range(int(self.size)):  # total column is N
                row.append(0)  # adding 0 value for each column for this row
            self.matrix.append(row)

    def get_matrix(self):
        return self.matrix

    def get_length(self):
        return self.size

    def get_num_players(self):
        return self.num_player

    def add_symbol(self, player, x, y):
        if x is not None and y is not None and x - 1 < self.size and y - 1 < self.size and  self.matrix[x - 1][y - 1] == 0:
            self.matrix[x - 1][y - 1] = self.num_player[player]
            return True
        else:
            return False

    def check_diag_top_bot_dx(self):  # questa controlla la diagonale
        for j in range(0, self.size - 2):
            i = 0
            self.__check_point__([(i + c, j + c) for c in range(self.size - j)])
        return self.point

    def check_diag_top_bot_sx(self):
        for i in range(1, self.size - 2):
            j = 0
            self.__check_point__([(i + c, j + c) for c in range(self.size - i)])
        return self.point

    def check_diag_bot_top_sx(self):  # questa controlla la diagonale
        for i in range(self.size - 1, 1, -1):
            j = 0
            self.__check_point__([(i - c, j + c) for c in range(i + 1)])
        return self.point

    def check_diag_bot_top_dx(self):
        for i in range(self.size - 1, 2, -1):
            j = 1
            self.__check_point__([(i - c, j + c) for c in range(i)])
        return self.point

    def check_row(self):
        for i in range(self.size):
            self.__check_point__([(i, j) for j in range(self.size)])
        return self.point

    def check_col(self):
        for j in range(self.size):
            self.__check_point__([(i, j) for i in range(self.size)])
        return self.point

    def __check_point__(self, sequence):
        arr = [self.matrix[i][j] for i, j in sequence]
        for last_player, subseq in groupby(arr):
            seq = list(subseq)
            if int(last_player) != 0:
                self.__add_point__(last_player, len(seq))
        return self.point

    def __add_point__(self, pl, length):
        if length >= 5:
            self.point[pl - 1] = 50
        elif length == 4:
            self.point[pl - 1] = 20
        elif length == 3:
            self.point[pl - 1] = 2
        return self.point

    def check_win(self):
        for i in range(len(self.point)):
            if self.point[i] >= 50:
                self.game_state = False
                return i

    def get_point(self):
        return self.point

    def get_game_state(self):
        return self.game_state

    def clear_all(self):
        self.matrix.clear()
        self.point.clear()
        self.num_player.clear()
        self.size = 0
        self.game_state = True

