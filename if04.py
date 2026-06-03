balans = 5000
summa = int(input("Yechmoqchi bo'lgan summani kiriting: "))

if summa < 0:
    print("Manfiy summa kiritib bo'lmaydi.")
elif summa <= balans:
    print(f"Pul yechildi. Qolgan balans: {balans - summa} so'm")
else:
    print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")