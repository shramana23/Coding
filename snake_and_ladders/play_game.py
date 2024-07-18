
import argparse
from core_components.game import Game
from logger import logger

def parse_args():
    parser = argparse.ArgumentParser(description='Start the game with the specified board structure.')
    parser.add_argument('--file-name', type=str, default='2_players_sum_dice_strategy.json', help='Path to the board structure JSON file')
    return parser.parse_args()

if __name__ == '__main__':
    logger.info("Welcome to Snake and Ladder Game")
    logger.info("Let's start the game :- )")
    logger.info("---------------------------------")
    args = parse_args()
    game = Game("./board_structure/" + args.file_name)
    game.play()