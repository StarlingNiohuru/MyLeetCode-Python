class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagonal1 = 0
        self.diagonal2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1
        self.rows[row] += score
        self.cols[col] += score
        if row == col:
            self.diagonal1 += score
        if row + col == self.n - 1:
            self.diagonal2 += score
        if self.rows[row] == self.n or self.cols[col] == self.n or \
                self.diagonal1 == self.n or self.diagonal2 == self.n:
            return 1
        if self.rows[row] == -self.n or self.cols[col] == -self.n or \
                self.diagonal1 == -self.n or self.diagonal2 == -self.n:
            return 2
        return 0
