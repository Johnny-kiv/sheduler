#Это напоминальщик 
#версия 3
#Автор: johnny-kiv
import time
a2 = int(input("Введите минуты работы: "))
b2 = int(input("Введите минуты отдыха: "))
с2 = int(input("Введите часы нахождения в школе: "))
if a2 == 0:
    a4 = 60*20
if b2 == 0:
    b4 = 20*60
if с2 == 0:
    с4 = с2*(60*60)
else:
    a4 = a2*60
    b4 = b2*60
    с4 = с2*(60*60)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a \n \t Идём в школу")
time.sleep(с4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t Делаем уроки ")
time.sleep(b4)
print("Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t Английский язык")
time.sleep(b4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t Cольфеджио ")
time.sleep(b4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t Спорт ")
time.sleep(b4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a \n \t Чтение")
time.sleep(b4)
print("\a Работаем на компьютере ")
time.sleep(a4)
print("\a  \n \t Фортепиано ")
time.sleep(b4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t Гитара ")
time.sleep(b4)
print("\a Работаем на компьютере")
time.sleep(a4)
print("\a  \n \t А теперь спать ")