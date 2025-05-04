class Test:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


x = Test(blue='трактор', red='моська', ginger='бицепс')
print(x.__dict__)
