from logger import logger
class Board:
    def __init__(self, board_size, snakes_count, ladders_count, snakes=None, ladders=None, players=None):
        self.board_size = board_size
        self.snakes_count = snakes_count
        self.ladders_count = ladders_count
        self.snakes = []
        self.ladders = []
        self.players = players
        if snakes:
            self.load_snakes(snakes)
        if ladders:
            self.load_ladders(ladders)

    def load_snakes(self, snakes):
        self.snakes = [Snake(head, tail) for head, tail in snakes]

    def load_ladders(self, ladders):
        self.ladders = [Ladder(bottom, top) for top, bottom in ladders]

    def show_board(self):
        position = 1
        board_representation = []

        for _ in range(self.board_size):
            row_representation = []
            for _ in range(self.board_size):
                cell_representation = f"{position:02d}"
                if position in [snake.head for snake in self.snakes]:
                    cell_representation = "SH"
                elif position in [snake.tail for snake in self.snakes]:
                    cell_representation = "ST"
                elif position in [ladder.top for ladder in self.ladders]:
                    cell_representation = "LT"
                elif position in [ladder.bottom for ladder in self.ladders]:
                    cell_representation = "LB"
                for player in self.players:
                    if player.position == position:
                        cell_representation = cell_representation + ' & ' + player.name[0]
                row_representation.append(cell_representation)
                position += 1
            board_representation.append(" ".join(row_representation))

        for row in reversed(board_representation):
            logger.info(row)


class Ladder:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail