import math
import os
os.system('cls')
'''
course = "python learning"
print(len(course))
# indexing
print(course[0])
print(course[6])
'''

# slicing
''''
print(course[0:7])
print(course[0:8])
print(course[0:-4])
print(course[0:7:2])
print(course[:7:-2])
print(course[::-1])  # reverse

for i in range(1, 21, 3):
    print(i,  end="_")
    '''

# \"
# \'
# \\
# \n
# \t
# برای جدا کردن متن یا اضافه کردن خط جدید یا اضافه کردن "" در یک رشته متن

# message = "hello\nsina"
# print(message)
'''
#این قسمت برای متصل کردن دوتا متغییر تعریف شده بود ضعف و فراموشی بنده سر این بود که یادم رفته بود اون مقداری که مقداری که تغریف کرده بودم رو درون ""  قرار بدم
car = "207"
gar = "white"
full = f"{car} {gar}" Or full = car + "" + gar
print(full)
print(gar[0:3])
'''

'''
# متد های استرینگها string methods 
course = "  python Programming "
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("t"))
print(course.strip())  # کلیر کردن فضاهای خالی
print(course.replace("py", "co"))  # جایگزینی کاراکتر با کاراکتر 
print("Pro" in course)
print("pro" in course)
print("sina" not in course)  # ایا وجود ندارد؟
'''
'''
# standard arithmetic operetors :
print(10/3)
print(10//3)
print(10 % 3)  # باقی مانده تقسیم
print(10**3)

# Augmented assignment Operators :
x = 7
# x = x + 3
# x += 3
# x /= 2
x %= 2
print(x)
'''

"""
print(round(3.4))
print(abs(-3.8))  # قدر مطلق
print(pow(3, 3))
print(divmod(17, 4))
# math functions
print(math.ceil(2.3))  # به سمت بالا
print(math.floor(4.8))  # به سمت پایین رند میشود
print(math.factorial(4))
print(math.sin(math.pi / 2))
print(math.fabs(4.2))
print(math.isinf(2))
"""

'''
x = input("x: ")
y = float(x) + 1
z = (float(x) + float(y))/2
print(f"x: {x} , y :{y} , z= {z}")
print(type(x))
print(type(z))
print(bool())
A = math.floor(z)
# A = math.ceil(z)
print(A)
'''

file_name = "my_photo.png"
# file_name = "my_python_file.png"
name = file_name.split(".")[0]
name = name.replace("_", " ")
name = name.title()
print(name)
