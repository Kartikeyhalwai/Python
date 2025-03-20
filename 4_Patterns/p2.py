#left downwards triangle
n = 5
for i in range (0,n+1):
    for j in range (n-i,0,-1):
        print("*",end="")
    print()

print()
#right downwards triangle
n = 5
for i in range (0,n):
    for j in range (0,i):
        print(" ",end ="")
    for k in range(n-i,0,-1):
        print("*",end="")
    print()

print()

#Pyramid
for i in range (0,n):
    for j in range (n-i,0,-1):
        print(" ",end="")
    for k in range (2*i-1,0,-1):
        print("*",end="")
    print()
print()
#Inverted pyramid
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(2*(n-i)-1,0,-1):
        print("*",end="")
    print()