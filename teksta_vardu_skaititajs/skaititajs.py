teksts = ""
with open("teksta_vardu_skaititajs/teksts.txt", "r", encoding="utf-8") as f:
    teksts = f.read()

vardi = teksts.split()
for i in range(len(vardi)):
    vardi[i] = vardi[i].strip(".,!-?*\'\")(")
    vardi[i] = vardi[i].lower()

visi_vardi = {}

for vards in vardi:
    if vards in visi_vardi:
        visi_vardi[vards] +=1
    else:
        visi_vardi[vards] = 1


biezakais_vards = ""
varda_skaits = 0

for viens in visi_vardi:
    if visi_vardi[viens] > varda_skaits:
        biezakais_vards = viens
        varda_skaits = visi_vardi[viens]

print (biezakais_vards, varda_skaits)
