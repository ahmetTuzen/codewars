def how_much_i_love_you(nb_pedals):
    phrases = {0: "not at all", 1: "I love you", 2: "a little",
               3: "a lot", 4: "passionately", 5: "madly"}
    return phrases[nb_pedals % 6]
