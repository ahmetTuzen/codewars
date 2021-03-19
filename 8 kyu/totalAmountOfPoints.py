def points(games):
    return sum(3 if game.split(':')[0] > game.split(':')[1] else 1 if game.split(':')[0] == game.split(':')[1] else 0 for game in games)
