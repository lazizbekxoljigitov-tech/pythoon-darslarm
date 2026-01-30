try:

  age = int(input("yoshingiz:"))
  if age < 10:
    print("Sizga bepul")
  elif 10 < age < 18:
    print("Sizga 18 ming so'm")
  elif 18 < age < 60:
    print("sizga 70 ming so'm")
  else:
    print("Error!!")
except ValueError:
  print("Yoshingizni to'g'ri kiriting !!")
