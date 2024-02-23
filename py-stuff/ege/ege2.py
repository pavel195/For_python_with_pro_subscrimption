"""
"""
from functools import lru_cache
def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 107:
        return "win"
    if any(game(m) == 'win' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'v1'
    if any(game(m) == 'v1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(h)):
        return 'v2'

h = (13, 20)
for i in range(20, 50):
    print(i, ' ', game((13, i)))
