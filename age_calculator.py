import os
os.system("cls")

date = input("birth date: ")
current_year = input("current year : ")
print(date)
print(current_year)
print("----------")
print("birth year = ", date[6:10])
print("birth month =", date[3:5])
print("birth day =", date[3:5])
print("Age =", int(current_year) - int(date[6:10]))
