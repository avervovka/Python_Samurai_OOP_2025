from string import ascii_lowercase as letters

class Button:

    def __init__(self, letter: str):
        self.letter = letter

lst = [Button(i) for i in letters]
print(lst)

