class Node:
    def __init__(self, saturs, vecaks=None, mazais=None, lielais=None, limenis = 0):
        self.info = saturs
        self.parent = vecaks
        self.smaller = mazais
        self.bigger = lielais
        self.level = limenis
        return
    
    def read(self):
        print(f"dati: {self.info}, līmenis: {self.level}")
        return
    
class Koks:
    def __init__(self):
        self.sakne = None
        return
    
    def add(self, jaunais):
        if self.sakne == None:
            self.sakne = Node(jaunais)
            return
        limenis = 1
        vecaks = self.sakne
        if jaunais>vecaks.info:
            vieta = vecaks.bigger
        else:
            vieta = vecaks.smaller
        while vieta:
            limenis +=1
            vecaks = vieta
            if jaunais>vecaks.info:
                vieta = vecaks.bigger
            else:
                vieta = vecaks.smaller
        if jaunais>vecaks.info:
            vecaks.bigger = Node(jaunais, vecaks=vecaks, limenis=limenis)
        else:
            vecaks.smaller = Node(jaunais, vecaks=vecaks, limenis=limenis)
        return
    
    def read(self):
        if self.sakne == None:
            print("Kokā nav neviena elementa!")
            return
        elements = self.sakne
        # elements.read()
        # self.read(elements.smaller)
        # self.read(elements.bigger)
        self.read_ja_ir(elements)

    def read_ja_ir(self, elements):
        if elements == None:
            return
        elements.read()
        self.read_ja_ir(elements.smaller)
        self.read_ja_ir(elements.bigger)
        return

    def sort(self):
        if self.sakne == None:
            print("Nav elementu kokā")
            return
        sakums = self.sakne
        self.read_mazakais(sakums)

    def read_mazakais(self, mazakais):
        if mazakais.smaller:
            self.read_mazakais(mazakais.smaller)
        mazakais.read()
        if mazakais.bigger:
            self.read_mazakais(mazakais.bigger)
    
    def search(self, meklejamais):
        limenis, vecaks, skaits = self.parbauda_vienu(meklejamais, self.sakne, 0)
        if limenis == -1:
            print(f"Neeksitē elements, tika veiktas {skaits} pārbaudes")
            return
        if limenis == 0:
            print(f"Elements ir koka sakne, tika veiktas {skaits} pārbaudes")
            return
        print(f"Elementa līmenis ir {limenis}, tā vecāks ir {vecaks}, tika veiktas {skaits} pārbaudes")
        return

    def parbauda_vienu(self, meklejamais, elements:Node, skaits):
        skaits += 1
        if meklejamais == elements.info:
            vecaks = None
            if elements.parent:
                vecaks = elements.parent.info
            return elements.level, vecaks, skaits
        if elements.smaller and elements.info > meklejamais:
            return self.parbauda_vienu(meklejamais, elements.smaller, skaits)
        if elements.bigger and elements.info < meklejamais:
            return self.parbauda_vienu(meklejamais, elements.bigger, skaits)
        return -1, None, skaits










koks = Koks()
koks.add(8)
koks.add(4)
koks.add(90)
koks.add(1)
koks.add(7)
koks.add(3)
koks.add(2)
koks.add(18)
koks.sort()
koks.search(105)
