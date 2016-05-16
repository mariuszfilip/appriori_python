import collections
from functools import reduce

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b


print (c)
print (a)


if 5 in a:
    print ('ok')

a1= ['1', '3', '4' , '2']
b2 = ('1', '2')




#test2 = list(set(a) & set(b))
#print(test)




def intersect_ordered(a, b):
    matches = []
    ia, ib = 0, 0
    la, lb = len(a), len(b)
    while ia < la and ib < lb:
        va, vb = a[ia], b[ib]
        if va < vb:
            ia += 1
        elif vb < va:
            ib += 1
        else:
            matches.append(va)
            ia += 1
            ib += 1
    return matches



print(intersect_ordered(a1,b2))


exit()
#print(list(test2))
#print(list(b))



def sequences_contain_same_items(a, b):
    for item in a:
        try:
            i = b.index(item)
        except ValueError:
            return False
        if b[i] != a[i]:
            return False
    return True


print(sequences_contain_same_items(list(test2),list(b)))
