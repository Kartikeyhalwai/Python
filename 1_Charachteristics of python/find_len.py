def findlen(string):
    count = 0
    for el in string:
        count += 1
    return count
string = str(input("Enter the string"))
length = findlen(string)
print("The length of the string is ", length)