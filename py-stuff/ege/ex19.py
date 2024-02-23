from functools import lru_cache

def moves(h):
    a = h
    return a+1,a*4

@lru_cache(None)
def game(h):
    if h > 80:
        return 'win'
    if any(game(m)=='win' for m in moves(h)):
        return 'p1'
    if all(game(m)=='p1' for m in moves(h)):
        return 'v1'
    if any(game(m)=='v1' for m in moves(h)):
        return 'p2'
    if all(game(m)=='p1' or game(m)=='p2' for m in moves(h)):
        return 'v2'
for i in range(1,70):
    print(i, ' ', game(i))
