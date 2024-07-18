from logger import logger

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, score, board):
        new_position = self.position + score
        if new_position > board.board_size ** 2:
            logger.info(f"No move by {self.name}")
            return self.position
        logger.info(f"{self.name} moved from {self.position} to {new_position}")
        self.position = new_position
        for snake in board.snakes:
            if self.position == snake.head:
                self.position = snake.tail
                logger.info(f"Oops! {self.name} has bitten by snake at {snake.head}! Moving from {snake.head} to {snake.tail}")
                break

        for ladder in board.ladders:
            if self.position == ladder.bottom:
                logger.info(f"Yeay! {self.name} has climbed the ladder at {ladder.bottom}! Moving from {ladder.bottom} to {ladder.top}")
                self.position = ladder.top
                break
        return self.position
      