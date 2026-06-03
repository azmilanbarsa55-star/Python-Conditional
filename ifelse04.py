
masofa = input("masofani kiriting: ")
if 0 < masofa > 1:
    print("Piyoda yuring")
elif 1 < masofa > 5:
    print("Velosiped yoki elektr skuter")
elif 5 < masofa > 50:
    print("Avtobus yoki mashina")
elif masofa < 50:
    print("Poyezd yoki samolyot")
else:
    print("Masofa manfiy bo'la olmaydi!")