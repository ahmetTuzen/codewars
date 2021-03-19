def rps(p1, p2):
    winner = -1
    if "oc" in p1 and "ci" in p2 or "pa" in p1 and "oc" in p2 or "ci" in p1 and "pa" in p2:
        winner = 1
    else:
        winner = 2

    return "Draw!" if p1 == p2 else f"Player {winner} won!"
