# Khai báo thư viện
import matplotlib.pyplot as plt
import numpy as np
import math

# Nhập hệ số của PT ax^2 + bx + c.
print("Nhap he so a: ")
a = int(input())
while True:
    if a==0:
        a = int(input("Hệ số a phải khác 0. Nhập lại a: "))
    else:
        break

print("Nhap he so b: ")
b = int(input())
while True:
    if b==0:
        a = int(input("Hệ số b phải khác 0. Nhập lại b: "))
    else:
        break

print("Nhap he so c: ")
c = int(input())

def PTB2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b/(2*a)
        return "Phuong trinh co nghiem kep x1 = x2 = " + str(x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return "Phuong trinh co 2 nghiem phan biet: x1 = " + str(x1) + ", x2 = " + str(x2)

print(PTB2(a, b, c))

x = np.linspace(-10, 10, 100)
y = a*x**2 + b*x + c
plt.rcParams.update({'font.size': 14})
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Đồ thị hàm số y = {0}x^2 + {1}x + {2}".format(a, b, c))
plt.show()