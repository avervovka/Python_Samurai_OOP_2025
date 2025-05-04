class Alphabet:
    a = 'abcdefgh'
    b = 'abcdefgh'
    c = 'abcdefgh'

x = Alphabet()
x.a = 'jksdhfjkhsdf'
x.b = 'kawjhfuerifiwsf'
x.c = 'eakuufrkehfkjse'
x.d = 'lsdkfiosdfoosd'

for key in Alphabet.__dict__.keys():
    if key in x.__dict__.keys():
        delattr(x, key)
