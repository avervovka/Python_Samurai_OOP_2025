class Socks:
    _counter = 0

    def __init__(self):
        Socks._counter += 1
        self.sock = 'левый' if Socks._counter % 2 != 0 else 'правый'

for i in range(10):
    (x := Socks()), print(x.__dict__)
