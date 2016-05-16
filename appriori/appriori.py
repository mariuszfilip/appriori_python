import collections

# przygotowuje liste skladaja sie z x elementow
def prepare_list_x_elements(resultOperation,x_element):
    candidateListePairs = {}
    i = 0
    for x in range(x_element):
        if x == 0:
            continue
        print(x)
        for operation in resultOperation:
            for sub_operation in resultOperation:
                if sub_operation not in candidateListePairs and sub_operation != operation:
                    sublistOne = [sub_operation, operation]
                    sublistTwo = [operation, sub_operation]
                    if sublistOne in candidateListePairs.values() or sublistTwo in candidateListePairs.values():
                        print("znaleziono")
                    else:
                        i += 1
                        candidateListePairs[i] = [operation, sub_operation]

    return candidateListePairs

# przygotowuje liste skladaja sie z 2 elementow
def prepare_list_two_elements(resultOperation):
    candidateListePairs = {}
    i = 0
    for operation in resultOperation:
        for sub_operation in resultOperation:
            if sub_operation not in candidateListePairs and sub_operation != operation:
                sublistOne = [sub_operation, operation]
                sublistTwo = [operation, sub_operation]
                if sublistOne in candidateListePairs.values() or sublistTwo in candidateListePairs.values():
                    print("znaleziono")
                else:
                    i += 1
                    candidateListePairs[i] = [operation, sub_operation]
    return candidateListePairs


# czysci liste
def clear_list(x):
    return x != ''


# czysci liste
def explode_values(x):
    a = x[0]
    return set(a.split("-"))


# oblicza confidence
def calculate_confidence(count, items_transaction , last_value):
    if last_value == 0:
        return 0
    return float(count) / float(last_value)

# oblicza support
def calculate_support(count, items_transaction):
    return float(count) / float(items_transaction)


def sequences_contain_same_items(a, b):
    if collections.Counter(a) != collections.Counter(b):
        return False
    for item in a:
        try:
            i = b.index(item)
        except ValueError:
            return False
        if b[i] != a[i]:
            return False
    return True


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

# zlicza ilosc wystapien danego ciagu w danych wejsciowych
def count_occurrence_list(candidateList, productList):
    countTransactionDictionary = {}
    for znak in candidateList:
        #print(znak)
        for transaction in productList:
            if set(znak).issubset(transaction):
                part_common = intersect_ordered(transaction,znak)
                if sequences_contain_same_items(list(part_common),list(znak)):
                    key = "-".join(map(str, znak))
                    if key in countTransactionDictionary:
                        countTransactionDictionary[key] += 1
                    else:
                        countTransactionDictionary[key] = 1
            else:
                key = "-".join(map(str, znak))
                if key not in countTransactionDictionary:
                    countTransactionDictionary[key] = 0
    return countTransactionDictionary

# zlicza ilosc wystapien danego ciagu w danych wejsciowych
def count_occurrence(candidateList, productList):
    countTransactionDictionary = {}
    for znak in candidateList.values():
        for transaction in productList:
            if set(znak).issubset(transaction):
                key = "-".join(map(str, znak))
                if key in countTransactionDictionary:
                    countTransactionDictionary[key] += 1
                else:
                    countTransactionDictionary[key] = 1
    return countTransactionDictionary


# znajduje kandydatow z min support
def find_candidate_list_with_min_support(count_transaction_dictionary, min_support, countAllItems, last_count_transaction_dictionary,min_confidence):
    candidateResultList = []
    candidateResultListOnes = []
    dictResult = {}
    for key, value in count_transaction_dictionary.items():
        sup = calculate_support(value, countAllItems)
        if '-' in key:
            listTemp = key.split('-')
            listTemp.pop()
            new_key = '-'.join(listTemp)
            if new_key in last_count_transaction_dictionary :
                confidence = calculate_confidence(value, countAllItems, last_count_transaction_dictionary.get(new_key))
            else:
                continue
        else:
            confidence = calculate_confidence(value,countAllItems,value)
        if sup >= min_support:
            candidateResultList.append(str(key))
            dictResult[key] = {'conf': confidence, 'sup': sup, 'key': str(key)}
            if '-' in key:
                listTemp = key.split('-')
                for s in listTemp:
                    candidateResultListOnes.append(s)
            else:
                candidateResultListOnes.append(str(key))

    return candidateResultList, count_transaction_dictionary,candidateResultListOnes,dictResult