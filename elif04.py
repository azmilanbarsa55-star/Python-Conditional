yosh = int(input("yoshingizni kiriting: "))
narx = 100

if yosh < 7:
 print(int(narx - (narx * 50 / 100)))

if 7 <= yosh <= 17:
 print(int(narx - (narx * 30 / 100)))

if yosh > 60:
 print(int(narx - (narx * 20 / 100)))
