def isPP(n):
    l = 100 if n < 10000 else 10000
    m = 10 if n < 10000 else 10
    for i in range(2, l):
        for u in range(2, m):
            if i ** u == n:
                return [i, u]
    return None
