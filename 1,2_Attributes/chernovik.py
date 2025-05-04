class TumbaUmba:
    pass


def func(n):
    instances = []

    for i in range(1, n + 1):
        if i % 3 == 0:
            x = TumbaUmba()
            x.warrior = False
            instances.append(x)
        else:
            x = TumbaUmba()
            x.warrior = True
            instances.append(x)

    return instances

print(*map(lambda x: x.warrior, func(9)))
