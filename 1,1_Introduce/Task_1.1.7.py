class Number:
    x = None


lst = list(map(int, input().split()))
setattr(Number, 'x', max(lst))

