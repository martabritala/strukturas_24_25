class Node:
    def __init__(self, saturs, pirms=None, pec=None):
        self.info = saturs
        self.next = pec
        self.prev = pirms

    def read(self):
        print(self.info)


class List:
    def __init__(self):
        self.sakums = None

    def add(self, jaunais):
        if self.sakums == None:
            self.sakums = Node(jaunais)
        else:
            pedejais = self.sakums
            while pedejais.next:
                pedejais = pedejais.next
            pedejais.next = Node(jaunais, pirms = pedejais)

    def read(self):
        if self.sakums == None:
            print("Saraksts ir tukšs!")
        esosais = self.sakums
        while esosais:
            esosais.read()
            esosais = esosais.next


saraksts = List()
saraksts.read()
saraksts.add("Suns")
saraksts.add("Kāja")
saraksts.add("Māja")
saraksts.add(2)

saraksts.read()
print("=====")
saraksts.sakums.next.next.next.prev.prev.prev.next.read()
    