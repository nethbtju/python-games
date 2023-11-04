
class NautsAndCrossesGame:
    gameBoard = [['A', 'B', 'C'],
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I']]

    winObserver = {'ABC': [0, 0], 'DEF': [0, 0], 'GHF': [0, 0], 'ADG': [0, 0], 'BEH': [0, 0], 'CFI': [0, 0],
                   'AEI': [0, 0], 'CEG': [0, 0]}
    player1 = (0, 'O')
    player2 = (1, 'X')
    queue = [player1, player2]

    def __init__(self):
        pass

    def playGame(self):
        self.printBoard()
        placedTokens = 0
        queue = self.queue
        while len(queue) > 1 and placedTokens < 9:
            self.canPlayTurn()
            placedTokens += 1

        winner = "Winner is " + self.queue.pop()[1]
        print(winner)

    """ Function to place the token on the board
    """
    def placeToken(self, player, position):
        board = self.gameBoard
        matrix_size = len(board)
        val, token = player
        for i in range(matrix_size):
            for j in range(matrix_size):
                if board[i][j] == position:
                    board[i][j] = token
                    if self.didPlayerWin(position, val):
                        return False
        return True


    def didPlayerWin(self, position, player_val):
        observer = self.winObserver
        for key in observer.keys():
            if position in key:
                observer_tuple = observer[key]
                observer_tuple[player_val] += 1
                print(observer_tuple[player_val])
                if observer_tuple[player_val] == 3:
                    return True
                observer[key] = observer_tuple
        return False

    def canPlayTurn(self):
        current_player = self.queue.pop(0)
        play_str = "Player " + current_player[1] + " Place Your Token On:\n"
        position = input(play_str)
        while self.placeToken(current_player, position):
            self.printBoard()
            self.queue.append(current_player)
            return

        self.queue = [current_player]
        return

    def printBoard(self):
        board = self.gameBoard
        string = "- - - - - - - \n"
        matrix_size = len(board)
        for i in range(matrix_size):
            not_end_of_row = 2
            for j in range(matrix_size):
                if not_end_of_row:
                    string += "| " + board[i][j] + " "
                    not_end_of_row -= 1
                else:
                    string += "| " + board[i][j] + " |\n"
            string += "- - - - - - -\n"

        print(string)


if __name__ == "__main__":
    newGame = NautsAndCrossesGame()
    newGame.playGame()