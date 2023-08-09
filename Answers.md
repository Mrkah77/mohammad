#0
```python
print("Hello Mohammad Kahnavi")
```
#1
```python
print("Enter your name?")
name = input()
print("Hello" , name)
```
#2
```python
x = int(input())
y = int(input())
print(x+y)
```
#3
```python
x = int(input("Whrite the first number"))
y = int(input("Whrite the second number"))
z = str(x+y)
print("The sum of them is equal to: " + z)
```
#4
```python
x = input("Whats your first name?")
y = input("Whats your last name?")
z = print(x,y)
```
#5
```python
#Mathematical operations
print("Mohammad Kahnavi")
x = int(input())
y = int(input())
print("sum:",x + y)
print("Subtraction:", x - y)
print("split rand down:",x // y)
print("Times:", x * y)
print("The power off:", x ** y)
print("Divided:", x / y)
print("Remainder:", x % y)
```
#6
```python
#String functions
#Center()
text = "Love"
x = text.center(24, "♡")
print(x)
#find()
text = "Hello, My name is Mohammad kahnavi"
x = text.find("m")
print(x)
y = text.find("z")
print(y)
#Make trans()
text = "Hellp Mphammad!"
mytable = str.maketrans("p", "o")
print(text.translate(mytable))
#upper()
text = "Welcome To Alcatraz Prison"
x = text.upper()
print(x)
#lower()
text ="Welcome To Alcatraz Prison"
y = text.lower()
print(y)
#title()
text = "welcome to alcatraz prison"
x = text.title()
#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
```
#7
```python
x = int(input("your average is in...level:"))
if 20 >= x >= 18:
    print("Excellent")
elif 18 > x >= 15:
    print("Very good")
elif 15 > x >= 11:
    print("Good")
elif 11 > x >= 9:
    print("Normal")
elif 0 <= x < 9:
    print("Need more effort")
elif x > 20 or x < 0:
    print("The entered number is invalid")
```
#8
```python
numbers = []
a = int(input())
if a > 0:
    numbers.append(a)
b = int(input())
if b > 0:
    numbers.append(b)
c = int(input())
if c > 0:
    numbers.append(c)
d = int(input())
if d > 0:
    numbers.append(d)
e = int(input())
if e > 0:
    numbers.append(e)
print(numbers)
```
#9
```python
for i in range (5):
    x = input("Enter your name:")
    print(x)
```
#10
```python
for x in range(1, 101):
    if x % 7 == 0:
        print(x)
```
#11
```python
print("a:")
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

print("b:")
i = 5
while i >= 1:
    print(i * "*")
    i = i - 1

print("c:")
i = 1
while i <= 5:
    print((5 - i) * " " + i * "*")
    i = i + 1

print("d:")
i = 5
while i >= 1:
    print((5 - i) * " " + i * "*")
    i = i - 1
```
#12
```python
import math
def prime():
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
x = int(input())
print(prime())
استفاده از تابع تعریف شده در یک فایل دیگه:
from text import prime
prime()
```
#13
```python
#Queen
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 == x2 or y1 == y2 or x1 - y2 == x2 - y1 or y1 - x2 == y2 - x1 or y2 - x1 == y1 - x2 or x2 - y1 == x1 - y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#Rook
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 == x2 or y1 == y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#chess bishop
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if x1 - y2 == x2 - y1 or y1 - x2 == y2 - x1 or y2 - x1 == y1 - x2 or x2 - y1 == x1 - y2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
#knight
s1 = input()
s2 = input()
x1, y1 = s1.split()
x2, y2 = s2.split()
x1, x2 = int(x1), int(x2)
y1, y2 = int(y1), int(y2)
count = 0
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    count = count + 1
if count == 1:
    print("You can hit the nut")
else:
    print("You can't hit the nut")
```
#14
```python
x = input()
x = x.split()
y = input()
y = y.split()
z = input()
z = z.split()
c =0
Days_of_weeks = ["Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in Days_of_weeks:
    if day not in x and day not in y and day not in z:
        c += 1
print(c)
```
#15
```python
n = int(input())
m = int(input())
sigma = 0
for i in range(-10, m + 1):
    for j in range(1, n + 1):
        sigma += int((i + j)**3/(j**2))
print(sigma)
```
#16
```python
N = int(input("Enter a number: "))
if 1 <= N <= 30:
    print(N * "#")
else:
    print("not defined")
```
#17
```python
import math
x = int(input())
y = math.log2(x)
print(math.floor(y))
```
