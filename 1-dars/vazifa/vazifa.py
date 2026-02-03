# do'kon 10  ming so'mlik atir 30 ming so'mlik atir va 45 ming so'mlik atir shularni sotad
# nechta nech pullik atir sotkanin anqlash
# va ularning 50% zi daromad 
# daromattan 12 foiz solg'ni chqarb tashlaymiz 
# va soliqdan keyin qancha daromad qold 
# agar umumi kassa puli 1000000 mln dan oshq bo'lsa 
# daromat soliqini 34 foizda ko'taramz 
# va undan qolgan qolgan oxrg daromatni hisoblaymiz
  


birinch = int(input("10 ming so'mlik : "))
ikki = int(input("30 ming so'mlik : "))
uch = int(input("45 ming so'mlik : "))

birinch_uchun = 10000
ikkinch_uchn = 30000
uchinch = 45000

jami = birinch + birinch_uchun + ikki + ikkinch_uchn + uch + uchinch

daromad = jami*5

if jami > 1000000:
  soliq = daromad * 0.34
else:
  soliq = daromad * 0.12

sof = daromad -soliq

print("asosi kassa:" + str(jami))
print("kassani yarmi:" + str(daromad))
print(" sof daromad" + str(sof))


