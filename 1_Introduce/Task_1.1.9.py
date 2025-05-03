# вводные данные(в lst хранится список объектов)
lst = [1, 'timespy', 'spy', 'loshok']

class FindSpy:
    spy = 'spy'


lst = [hasattr(FindSpy, 'spy') for i in lst]
