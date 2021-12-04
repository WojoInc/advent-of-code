from sys import argv, exit

class Sum:
    def __init__(self, callback, limit):
        self.count = 0
        self.limit = limit
        self.callback = callback
    def inc(self):
        self.count += 1
        if self.count == self.limit:
            self.callback()

class Cell:
    def __init__(self, marked, x, y):
        self.marked = marked
        self.x = x
        self.y = y
    
class Board:
    def __init__(self, num, rows: list):
        self.boardnum = num
        self.len = len(rows)
        self._build_map(rows)
        self._build_sums()
    def _build_sums(self):
        self.sums = []
        for i in range(self.len * 2):
            self.sums.append(Sum(self.bingo, self.len))
    def _build_map(self, rows):
        self.rowmap = {}
        for i in range(self.len):
            for j in range(self.len):
                row = " ".join(rows[i].split()).split(" ")
                self.rowmap[row[j]] = Cell(False, j, i)
    def mark(self, num):
        self.last = num
        if num in self.rowmap:
            self.rowmap[num].marked = True
            self.sums[self.rowmap[num].x].inc()
            self.sums[self.len + self.rowmap[num].y].inc()
    def sum_unmarked(self):
        sum = 0
        for k,v in self.rowmap.items():
            sum += (int(k) if not v.marked else 0)
        return sum
    def bingo(self) -> bool:
        print(f"Bingo! Board #{self.boardnum}")
        print(f"Last num called: {self.last}")
        print(f"Sum of unmarked: {self.sum_unmarked()}")
        print(f"Score: {self.sum_unmarked() * int(self.last)}")
        exit()

with open(argv[1], 'r') as infile:
    inputs = infile.readlines()
    balls = inputs[0].split(",")
    boards = []
    # Parse the different boards
    boardnum = 0
    for i in range(2, len(inputs), 6):
        boards.append(Board(boardnum, inputs[i:i+5]).mark)
        boardnum += 1
    for ball in balls:
        print(f"Calling:{ball}")
        for board in boards:
            board(ball)