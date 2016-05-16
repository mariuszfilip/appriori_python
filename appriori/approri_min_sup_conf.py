
import itertools
import appriori
import sys
from PyQt4 import QtGui


def run_appriori(min_sup_input , min_confidence_input, x_elements , item):
    f = open('retail.dat.txt', 'r')
    dane = f.read()
    f.close()

    productList = []
    wyszyskieWartosci = []
    lista = dane.split('\n')

    min_sup = min_sup_input
    count_elements = x_elements

    resultAll = {}

    candidateListe = {}
    countTransactionFirst = {}

    # pierwsza petla zliczajaca ilosc wystapien
    for wiersz in lista:
        wierszList = wiersz.split(' ')
        wierszList = list(filter(appriori.clear_list, wierszList))
        # print (wierszList)
        i = 0
        productList.append(wierszList)
        for znak in wierszList:
            test = [(str(znak))]
            candidateListe[(str(znak))] = [str(znak)]
            if znak in countTransactionFirst:
                countTransactionFirst[znak] += 1
            else:
                countTransactionFirst[znak] = 1

    # candidateListe = set(candidateListe)
    countAllItems = len(lista)


    # countTransaction = count_occurrence(candidateListe, productList)
    result, countTransactionSummary ,test , resultAll = appriori.find_candidate_list_with_min_support(countTransactionFirst, min_sup, countAllItems, countTransactionFirst,min_confidence_input)


    print('Kandydaci - lista 1 elementowa - podsumowanie')
    for value in resultAll.values():
        print(value)


    repeadDone = 1
    result2 = result
    oldcountTransaction = countTransactionFirst
    while (repeadDone < count_elements):
        repeadDone += 1
        candidateListePairs2 = list(itertools.product(result2, repeat=repeadDone))
        countTransaction2 = appriori.count_occurrence_list(candidateListePairs2, productList)
        result, countTransactionSummary, result2,resultAll = appriori.find_candidate_list_with_min_support(countTransaction2, min_sup, countAllItems,oldcountTransaction,min_confidence_input)
        oldcountTransaction = countTransactionSummary
        print('Kandydaci - lista %d elementowa - podsumowanie',repeadDone)
        for value in resultAll.values():
            if str(item) in str(value['key']):
                print(value)
            else:
                if value['key'] in result2:
                    result2.remove(value['key'])

    #print(resultAll)
    print('koniec')


class Example(QtGui.QWidget):
    min_sup = 0
    min_confidence = 0
    count_element = 0
    item = 0

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        min_sup_label = QtGui.QLabel('Min sup')
        min_conf_label = QtGui.QLabel('Min conf')
        count_elements_label = QtGui.QLabel('Ilosc elementow')
        item_label = QtGui.QLabel('Szukaj dla ')

        self.min_sup = QtGui.QLineEdit()
        self.min_confidence = QtGui.QLineEdit()
        self.count_element = QtGui.QLineEdit()
        self.item = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(12)

        grid.addWidget(min_sup_label, 1, 0)
        grid.addWidget(self.min_sup, 1, 1)

        grid.addWidget(min_conf_label, 2, 0)
        grid.addWidget(self.min_confidence, 2, 1)

        grid.addWidget(count_elements_label, 3, 0)
        grid.addWidget(self.count_element, 3, 1)

        grid.addWidget(item_label, 4, 0)
        grid.addWidget(self.item, 4, 1)

        button = QtGui.QPushButton('Przelicz')
        button.clicked.connect(lambda : self.handleButton())

        grid.addWidget(button,5 ,0)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def handleButton(self):
        run_appriori(float(self.min_sup.text()), float(self.min_confidence.text()), float(self.count_element.text()), self.item.text())
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
