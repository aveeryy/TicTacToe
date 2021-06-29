import random
import sys

class TicTacToe:

    PLAYERS = {False: 'X', True: 'O'}
    POSSIBLE_WINS = (
        # Horizontal
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        # Vertical
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        # Diagonal
        (1, 5, 9),
        (3, 5, 7)
    )

    def build_visual_board(self):
        self.visual_board = ''
        self.rows = -1
        for i in range(7):
            if not (i % 2):
                self.visual_board += '=' * 15 + '\n'
            else:
                self.rows += 1
                for j in range(3):
                    self.visual_board += f'= {j + 1 * i + self.rows} ='
                self.visual_board += '\n'
        return self.visual_board

    def modify_game_board(self, move=int, player=bool):
        'Modifies both the internal board and the visual one'
        self.board[int(move)] = self.PLAYERS[player]
        self.visual_board = self.visual_board.replace(str(move), self.PLAYERS[player])

    def cpu_player(self):
        'Selects a random place in the board'
        cpu_choice = None
        while True:
            cpu_choice = random.choice(list(self.board.keys()))
            if self.board[cpu_choice] is None:
                break
        print(f'[-] The CPU put their piece in {cpu_choice}\n')
        # Place the piece
        self.modify_game_board(move=cpu_choice, player=True)

    def check_for_win(self, player=bool):
        i = self.PLAYERS[player]
        for pos in self.POSSIBLE_WINS:
            if self.board[pos[0]] == i and self.board[pos[1]] == i and self.board[pos[2]] == i:
                return True
        return False

    def start(self, use_cpu_player=True):
        # Reset variables
        self.board = {i: None for i in range(1, 10)}
        self.visual_board = self.build_visual_board()
        self.turn = False  # False for player 0 (X), True for player 1 (O) or CPU
        self.turns = 0
        while True:
            # Check for a tie
            if self.turns >= 9:
                print('[-] That\'s a tie!')
                return
            self.current_player_naming = "Player" if not use_cpu_player or use_cpu_player and not self.turn else "CPU"
            print(self.visual_board)
            print(f'[-] It\'s {self.current_player_naming} (Piece {self.PLAYERS[self.turn]}) turn!')
            if self.turn and not use_cpu_player or not self.turn:
                while True:
                    self.move = input('Your move: ')
                    # Check if it's not in range 1-9
                    if int(self.move) not in range(1, 10):
                        print('[!] Invalid input')
                        continue
                    # Check if the move is invalid
                    if self.board[int(self.move)] is not None:
                        print('[!] You can\'t make that move!')
                        continue
                    # Place the piece
                    self.modify_game_board(move=self.move, player=self.turn)
                    break
            else:
                self.cpu_player()
            # Check if current player has won
            if self.check_for_win(player=self.turn):
                print(f'[-] {self.current_player_naming} (Piece {self.PLAYERS[self.turn]}) won!')
                return
            self.turns += 1
            # Switch players
            self.turn = True != self.turn
        

if __name__ == '__main__':
    # Start the game
    TicTacToe().start(use_cpu_player='-cpu' in sys.argv)