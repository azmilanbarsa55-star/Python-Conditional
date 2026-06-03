a = float(input("birinchi sonni kiriting: "))
b = float(input("ikkinchi sonni kiriting: "))
amal = input("amalni kiriting: ")

if amal == "+":
    print(a + b)

elif amal == "-":
    print(a - b)

elif amal == "*":
    print(a * b)

elif amal == "/":
    if b == 0:
        print("nolga bo'lib bo'lmaydi")
    else:
        print(a / b)

else:
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")