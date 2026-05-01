""" x = 10
for i in range (20,10,-2):
    x=x+2
    print("Hi")
for i in "Hi":
    print(x, end=" ") """



"""for i in range (9):
    print("*",end=" ")
print()
for j in range (i):
        print("*               *")
for i in range (9):
    print("*",end=" ")"""


"""a=int(input("Enter any Number"))
if a%2==0:
    for i in range(1,11):
        print("{} x {} = {}".format(i,a,i*a))
else:
    for i in range(1,a+1):
        print("{} x {} = {}".format(i,a,i*a))"""

#NO OF WORDS COUNT
"""a = input("Enter Any sentence: ")
c = 0
for i in range(len(a)):
    if (a[i]==" " and a[i+1]!= " "):
        c=c+1
print("Words:",c+1)"""

"""import random
p1 = input("Enter player1: ")
p2 = input("Enter player2: ")
s1=10
s2=10
d1=random.randint(1,10)
d2=random.randint(1,10)
print("______________PLAYER1 TURN____________")
while(True):
    g1=int(input("Enter your guess: "))
    s1=s1-1
    if g1==d1:
        break
print("______________PLAYER2 TURN____________")
while(True):
    g2=int(input("Enter your guess: "))
    s2=s2-1
    if g2==d2:
        break
print("_______________SUMMARY_________________")
print("{}:{}".format(p1,s1))
print("{}:{}".format(p2,s2))
print("________________________________________")
if s1 > s2:
    print("Winner is ",p1)
elif s2>s1:
    print("Winner is ",p2)
else:
    print("DRAW")"""
