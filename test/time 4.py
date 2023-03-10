#Это тринеровка
#версия 4
#Автор: johnny-kiv
import datetime
import time
from tkinter import*
root = Tk()
now = datetime.datetime.now()
c=Canvas(root,bg="yellow",width=800,height=600,cursor="pencil")
c.create_oval(250,500,550,550,fill="Black")
c.create_oval(350,500,450,530,fill="gray")
c.create_rectangle(350,500,450,530,fill="gray")
c.pack()
root.mainloop()

