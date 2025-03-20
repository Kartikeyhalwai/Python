def removenth(string,key):
    str2 = ""
    for i in range(0,len(string)):
        if(key == i):
            pass
        else:
            str2+=string[i]
    return str2
string = str(input("Enter the string : "))
key = int(input("Enter the position to be deleted : "))
modif = removenth(string, key)
print(modif)