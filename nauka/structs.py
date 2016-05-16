
imionaList = ['mariusz', 'pawel', 3]

print (imionaList)

print (imionaList[0])

imionaList.append('piotr')
print (imionaList)

imionaList.insert(2, "dupa")


print (imionaList)


imionaTuple = ('mariusz','pawel','asd')
print (imionaTuple)


for i in imionaTuple:
    if i.find('asd') != -1:
        print ('znalazlem!!!')


klienciMap = {'Mariusz': 'Filipkowksi', 'Piotr': 'Filip'}

if klienciMap.has_key('Piotr2'):
    print (klienciMap.get('Piotr'))

klienciMap.popitem()

print (klienciMap)

#print klienci.get('Mariusz');
#print klienci.get('Filip');



