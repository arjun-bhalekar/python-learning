from abc import ABC, abstractmethod

# ---abstract class jut like interface putting abstract methods only
class GamingConsole(ABC):
    @abstractmethod
    def up(self): pass
    @abstractmethod
    def down(self): pass
    @abstractmethod
    def left(self): pass
    @abstractmethod
    def right(self): pass


# --- implementer class 1 ----
class MarioGame(GamingConsole):
    def up(self):
        print("jump")
    def down(self):
        print("goes into a table")
    def left(self):
        print("go backword")
    def right(self):
        print("go forward")

class ChessGame(GamingConsole):
    def up(self):
        print("move up")
    def down(self):
        print("move down")
    def left(self):
        print("move left")
    def right(self):
        print("move right")

# marioGame = MarioGame()
# marioGame.up()
# marioGame.down()
# marioGame.left()
# marioGame.right()
#
# chessGame = ChessGame()
# chessGame.up()
# chessGame.down()
# chessGame.left()
# chessGame.right()

games = [MarioGame(), ChessGame()]

for game in games:
    game.up()
    game.down()
    game.left()
    game.right()

