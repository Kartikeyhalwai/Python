#Right Angled triangle;
n = 5
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()

print()
#Square
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()

print()

#Hollow Square
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
        
    print()


#Rhombus
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(0,n):
        print("*",end="")
    print()

#right angled triangle
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print()