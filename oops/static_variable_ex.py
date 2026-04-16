
class Player:

    # static variable common at class level
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_player_count():
        return Player.count

# def get_player_count():
#     return Player.count


player1 = Player('Arjun')
print(Player.get_player_count()) # 1

player2 = Player('Mukund')
print(Player.get_player_count()) # 2

player3 = Player('Danish')
print(Player.get_player_count()) # 3