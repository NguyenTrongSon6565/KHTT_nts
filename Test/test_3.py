#1. Kết quả và hiển thị kết quả.
#1.1
5 
x = 5
x + 1
#1.2: viết câu lệnh chương trình và chạy nó, kết quả đầu ra là gì.
y = x + 1
#1.3: In 
print("y = ", y)

#2.Arithmetic expressions and their types
#2.1

width = 17
height = 12.0
delimiter  = '.'

#2.2

x1 = width/2
x2 = width//2

x3 = width/2.0
x4 = height/3

x5 = 1 + 2*5
x6 = (1+2)*5

x7 = delimiter*width
x8 = delimiter*int(height)

print("delimiter = {8}, x1 = {0}, x2 = {1}, x3 = {2}, x4 = {3}, x5 = {4}, x6 = {5}, x7 = {6}, x8 = {7}" .format(x1, x2, x3, x4, x5, x6, x7, x8, delimiter))

print("type(delimiter): {0}, type(x1): {1}, type(x2): {2}, type(x3): {3}, type(x4): {4}, type(x5): {5}, type(x6): {6}, type(x7): {7}, type(x8): {8}"
       .format(type(delimiter), type(x1), type(x2), type(x3), type(x4), type(x5), type(x6), type(x7), type(x8)))

#3. Planck’s constant reduced.
#3.1.
from math import pi
def planck1():
    h = 6.62607004e-34
    h_bar = h/(2*pi)
    print("h_bar1 = ", h_bar)

def planck2():
    h = 6.62607004e-34
    h_bar = h/2*pi
    print("h_bar2 = ", h_bar)

planck1()
planck2()

'''3.2. First, before we try to calculate using Python, let us roughly calculate it by hand — or,

You should be able to calculate it by at least one figure in your head! We will use this.

As a “sanity check” on our Python result.'''

#3.3. Now look at the following lines of code:
import math

# define constants

h = 6.62606876e-34 # Planck’s constant

hbar = h / 2 * math.pi # Planck’s constant reduced

# generate output

print ("hbar = ", hbar)

#3.4. What will be obtained for the value of the bar with this code? Is it what we “want”? Explain.
'''Kết quả không như chúng ta muốn vì hbar = h / 2 * math.pi không phải là h/(2*pi)'''