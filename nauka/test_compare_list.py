prod = [['39','123'],['41','48']]

#kand = {1: ['39', '41'], 2: ['39', '38'], 3: ['39', '48'], 4: ['39', '32'], 5: ['41', '38'], 6: ['41', '48'], 7: ['41', '32'], 8: ['38', '48'], 9: ['38', '32'], 10: ['48', '32']}

kandList = [('48-41', '48-41', '41-48')]

# zlicza ilosc wystapien danego ciagu w danych wejsciowych
def count_occurrence_list(candidateList, productList):
    countTransactionDictionary = {}
    for znak in candidateList:
        for transaction in productList:
            print(transaction)
            print(znak)
            if set(znak).issubset(transaction):
                key = "-".join(map(str, znak))
                if key in countTransactionDictionary:
                    countTransactionDictionary[key] += 1
                else:
                    countTransactionDictionary[key] = 1
    return countTransactionDictionary






print(count_occurrence_list(kandList,prod))