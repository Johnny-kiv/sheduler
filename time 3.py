#Это напоминальщик 
#версия 3
#Автор: johnny-kiv
import time
a2 = int(input("Введите минуты работы: "))
b2 = int(input("Введите минуты отдыха: "))
if a2 == 0:
    a4 = 60*20
if b2 == 0:
    b4 = 20*60
else:
    a4 = a2*60
    b4 = b2*60
r = 1
t = 0
t1 = 0
print("Работаем")
while r:
    for r in range(a4):
        t = t+1
        time.sleep(1)
        print(t)
    print("\a  \n \t Отдыхаем")
    t = 0
    for r in range(b4):
        t1=t1+1
        time.sleep(1)
        print(t1)
    print("\a Работаем")
    t1 = 0
