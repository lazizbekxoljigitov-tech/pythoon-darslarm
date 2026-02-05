summa = 100000

print("ATM ga xush kelibsiz!")
print("==================================")
print("1. Pul yechish")
print("2. Pul kiritish")
print("3. Hisobni tekshirish")
print("4. Chiqish")
print("Iltimos, tanlovni kiriting (1, 2, 3 yoki 4): ")
print("==================================")

while True:
  tanlash = int(input("tanlov: "))
  if tanlash == 1:
    yechish = int(input("Yechmoqchi bo'lgan summani kiriting: "))
    if yechish > summa:
      print("Kechirasiz, hisobingizda yetarli mablag' yo'q.")
    else:
      summa -= yechish
      print(f"{yechish} so'm yechildi. Qolgan summa: {summa} so'm.")
  
  elif tanlash == 2:
    kiritish = int(input("Kiritmoqchi bo'lgan summani kiriting: "))
    summa += kiritish
    print(f"{kiritish} so'm kiritildi. Jami summa: {summa} so'm.")
  
  elif tanlash == 3:
    print(f"Hisobingizda {summa} so'm mavjud.")
  
  elif tanlash == 4:
    print("ATM dan chiqish. Xayr!")
    break
  
  else:
    print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")