from enum import Enum
import random
from logger import logger


class Dice:
    def __init__(self, dice_count, movement_strategy):
        self.dice_count = dice_count
        self.movement_strategy = MovementStrategy(movement_strategy)

    def roll(self, player):
        roll_of_all_dices = [random.randint(1, 6) for _ in range(self.dice_count)] 
        logger.info(f" {player.name} rolled the dice --- {roll_of_all_dices}")
        if self.movement_strategy == MovementStrategy.SUM:
            score = sum(roll_of_all_dices)
            logger.info(f"{player.name} scored {score} according to 'SUM' strategy")
            return score
        elif self.movement_strategy == MovementStrategy.MAX:
            score = max(roll_of_all_dices)
            logger.info(f"{player.name} scored {score} according to 'MAX' strategy")
            return score
        elif self.movement_strategy == MovementStrategy.MIN:
            score = min(roll_of_all_dices)
            logger.info(f"{player.name} scored {score} according to 'MIN' strategy")
            return score
        else:
            raise NotImplementedError

class MovementStrategy(Enum):
    """
        sum: sum of numbers on dies
        max: max of numbers on dies
        min: min of numbers on dies
    """
    SUM = "SUM"
    MAX = "MAX"
    MIN = "MIN"
