
vazn = float(input("Vazn (kg): "))
boy = float(input("Bo'y (m): "))

if vazn <= 0 or boy <= 0:
    print("Vazn va bo'y musbat bo'lishi kerak.")
elif boy < 0.5 or boy > 3.0:
    print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak.")
elif vazn < 1 or vazn > 500:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak.")
else:
    bmi = vazn / (boy ** 2)

    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Tasnif: Kam vazn")
    elif bmi < 25:
        print("Tasnif: Normal vazn")
    elif bmi < 30:
        print("Tasnif: Ortiqcha vazn")
    else:
        print("Tasnif: Semizlik")