def warn_the_sheep(queue):
    i = queue.index("wolf")

    if i+1 == len(queue):
        message = "Pls go away and stop eating my sheep"
    else:
        message = f"Oi! Sheep number {len(queue) - i - 1}! You are about to be eaten by a wolf!"

    return message
