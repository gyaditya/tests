#Quiz Prep Adi
import random


#1
monj = ["January", "June", "July"]

#2
joy700 = []
for n in range(700):
    joy700.append("Joy")

#3
seven = []
for n in range(500):
    joy700.append(7)

#4
num = []
for n in range(5000):
    randnum = random.randrange(0, 100)
    num.append(randnum)

#5
num300 = []
for n in range(300):
    randnum2 = random.randrange(0, 40)
    num300.append(randnum2)

#6
multiple4 = []
for n in range(20, 801):
    if n%4 == 0:
        multiple4.append(n)

#7
even = []
for n in range(100, 9, -1):
    if n%2 == 0:
        even.append(n)

#8
colors_str = "red,orange,yellow,green,blue,indigo,violet"
newcolors = colors_str.split(",")

#9
cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
newcities = cities_str.split(";")

#10
userloop = True
names = []
while userloop:
    userinput = input("Please add a name\n")
    if userinput == "done":
        userloop = False
    else:
        names.append(userinput)
