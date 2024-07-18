import json
from core_components.board import Board
from core_components.dice import Dice
from core_components.player import Player
from logger import logger


class Game:
    def __init__(self, config_file):
        self.is_game_running = True
        with open(config_file, 'r') as file:
            self.config = json.load(file)
        self.load_configurations()
        self.load_compnents()
    
    def load_configurations(self):
        self.board_size = self.config["board_size"]
        self.number_of_players = self.config["number_of_players"]
        self.total_snakes = self.config["total_snakes"]
        self.snakes = self.config["snakes"]
        self.total_laddders = self.config["total_laddders"]
        self.ladders = self.config["ladders"]
        self.number_of_dice = self.config["number_of_dice"]
        self.movement_strategy = self.config["movement_strategy"]
        self.player_names = self.config["player_names"]
        self.starting_locations = self.config["starting_locations"]

    def load_compnents(self):
        self.load_players()
        self.load_board()
        self.load_dice()

    def load_board(self):
        self.board = Board(self.board_size, self.total_snakes, self.total_laddders, self.snakes, self.ladders, self.players)
        logger.info("The board structure is configured")
        self.board.show_board()
    
    def load_dice(self):
        self.dice = Dice(self.number_of_dice, self.movement_strategy)
    
    def load_players(self):
        self.players = []
        for name, location in zip(self.player_names, self.starting_locations):
            self.players.append(Player(name, location))

    def play(self):
        logger.info("---------START GAME---------")
        while True:
            for player in self.players:
                score = self.dice.roll(player)
                new_position = player.move(score, self.board)
                self.board.show_board()
                if new_position == self.board.board_size ** 2:
                    logger.info(f"{player.name} won the game!")
                    logger.info("---------END GAME---------")
                    return
            
            
            
        



