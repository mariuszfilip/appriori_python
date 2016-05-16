from klasy import Zwierze
from klasy import Pies
b = 0
a = 1
try:
    zwierze = Zwierze()
    pies = Pies()

    if b == 1:
        raise (EOFError)
    if a == 1:
        raise (ArithmeticError, 'test_compare_list.py')
    if b == 0:
        raise (RuntimeError , 'co jest')
except Exception as e:
    print ('Uwaga',e)