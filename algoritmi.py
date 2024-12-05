saraksts = [5,78,2,38,6,91,3]

for j in range( len(saraksts)-1 ):
    for i in range( len(saraksts)-1-j ):
        if saraksts[i] > saraksts[i+1]:
            temp = saraksts[i]
            saraksts[i] = saraksts[i+1]
            saraksts[i+1] = temp

print(saraksts)



def meklet(list, num):
    for i in range( len(list) ):
        if num == list[i]:
            print(num, "Eksistē:", i)
            return i
    print (num, "Neeksistē")
    return -1

meklet(saraksts, 2)
meklet(saraksts, 23)