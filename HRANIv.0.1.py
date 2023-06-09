
age = 16

if (age < 1):
    Pnormal = 132
    Pable = 30
elif (age < 4):
    Pnormal = 124
    Pable = 30
elif (age < 6):
    Pnormal = 106
    Pable = 20
elif (age < 8):
    Pnormal = 98
    Pable = 20
elif (age < 10):
    Pnormal = 88
    Pable = 20
elif (age < 12):
    Pnormal = 80
    Pable = 20
elif (age < 15):
    Pnormal = 75
    Pable = 20
elif (age < 50):
    Pnormal = 70
    Pable = 10
elif (age < 60):
    Pnormal = 74
    Pable = 10
else:
    Pnormal = 79
    Pable = 10

P1 = int(input("Пульс первого измерения: "))
P2 = int(input("Пульс второго измерения: "))
Pcurrent = (P1 + P2)/2

Pdifference = abs(Pcurrent - Pnormal)

Ppercent = Pdifference * 10 / Pable
print("Ваш коэффициент отклонения пульса (если больше 10 - плохо, меньше - все в норме): " + str(Ppercent))

Pcurrenty = int(input("Введите ваш вчерашний пульс (в дальнейшем ввод будет автоматически): "))
Pdelta = abs(Pcurrenty - Pcurrent)
Pjump = Pdelta * 6 / Pable

Prating = max(Pjump, Ppercent)
print("Ваш рейтинг пульса (максимум из коэффициента скачков пульса и коэффициента отклонения пульса: " + str(Prating))

if (age < 5):
    BLnormal = 60
    BLable = 15
    BUnormal = 90
    BUable = 15
elif (age < 6):
    BLnormal = 65
    BLable = 15
    BUnormal = 95
    BUable = 15
elif (age < 13):
    BLnormal = 70
    BLable = 10
    BUnormal = 105
    BUable = 15
elif (age < 19):
    BLnormal = 77
    BLable = 4
    BUnormal = 117
    BUable = 12
elif (age < 24):
    BLnormal = 79
    BLable = 4
    BUnormal = 120
    BUable = 12
elif (age < 29):
    BLnormal = 80
    BLable = 4
    BUnormal = 121
    BUable = 12
elif (age < 34):
    BLnormal = 81
    BLable = 4
    BUnormal = 122
    BUable = 12
elif (age < 39):
    BLnormal = 82
    BLable = 4
    BUnormal = 123
    BUable = 12
elif (age < 44):
    BLnormal = 83
    BLable = 4
    BUnormal = 125
    BUable = 12
elif (age < 49):
    BLnormal = 84
    BLable = 4
    BUnormal = 127
    BUable = 12
elif (age < 54):
    BLnormal = 85
    BLable = 4
    BUnormal = 129
    BUable = 13
elif (age < 59):
    BLnormal = 86
    BLable = 4
    BUnormal = 131
    BUable = 13
else:
    BLnormal = 87
    BLable = 4
    BUnormal = 134
    BUable = 13

BL1 = int(input("Нижнее давление первого измерения: "))
BL2 = int(input("Нижнее давление второго измерения: "))
BLcurrent = (BL1 + BL2)/2

BLdifference = abs(BLcurrent - BLnormal)
BLpercent = BLdifference * 10 / BLable

BU1 = int(input("Верхнее давление первого измерения: "))
BU2 = int(input("Верхнее давление второго измерения: "))
BUcurrent = (BU1 + BU2)/2

BUdifference = abs(BUcurrent - BUnormal)
BUpercent = BUdifference * 10 / BUable

Brating = max(BUpercent, BLpercent)
print("Ваш рейтинг давления (максимум из коэффициента отклонения нижнего давления и верхнего давления: " + str(Brating))



Hrating = max(Prating, Brating)
print("Ваш рейтинг здоровья: " + str(Hrating))

allHealthRatings = [3, 6, 8]

allHealthRatings.append(Hrating)
l = min(7, len(allHealthRatings))
curHealthRatings = allHealthRatings[len(allHealthRatings)-l:]

Hsigma = sum(curHealthRatings)
Hfinal = max(curHealthRatings)

print("Ваша сумма рейтингов здоровья: " + str(Hsigma) + ", ваш рейтинг здоровья, на который стоит обратить наибольшее внимание: " + str(Hfinal))

if (Hsigma > 60 or Hfinal > 10):
    print("Вам необходимо срочно обратиться к врачу!")
elif (Hsigma > 50 or Hfinal > 8):
    print("Вам стоит получше следить за своим здоровьем: вероятно, Вам скоро придется сходить к врачу")
else:
    print("С Вашим здоровьем все в порядке. Продолжайте за ним следить с помощью нашей платформы!")