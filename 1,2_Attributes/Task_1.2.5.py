class TumbaUmba:
    pass


def func(n):
    instances = []

    for i in range(n):
        instance = TumbaUmba()
        instance.warrior = (i % 3 != 2)
        instances.append(instance)

    return instances


print(*map(lambda x: x.warrior, func(9)))

# lst = []
# for i in range(1, int(input('Enter a number: ')) + 1):
#     if i % 3 == 0:
#         lst.append(False)
#     else:
#         lst.append(True)
# print(lst)
