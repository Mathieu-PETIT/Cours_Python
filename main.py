import csv
from UI import *
csvfichier = open(r'C:\Users\PTWV699\Documents\Python\Open Data Festival\panorama-des-festivals.csv',encoding='utf-8',newline="")
reader = csv.reader(csvfichier, delimiter=";")

interface = UI(Tk())
interface.mainloop()
interface.destroy()


