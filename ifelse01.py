ball = int(input("Ballni kiriting (0-100): "))

if ball < 0:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
if ball > 100:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
elif 90 <= ball <= 100:
    print("A (A'lo)")
elif 80 <= ball <= 89:
    print("B (Yaxshi)")
elif 70 <= ball <= 79:
    print("C (Qoniqarli)")
elif 60 <= ball <= 69:
    print("D (Qoniqarsiz)")
else:
    print("F (Rad)")