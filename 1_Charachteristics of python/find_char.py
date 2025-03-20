def searchchar(string, key):
    pos = len(string)-1
    while(pos>=0):
        if(string[pos] == key):
            print(f"key is found at {pos}")
            break
    pos+=1

string = str(input("Enter the string : "))
key = str(input("enter the charachter to search : "))
searchchar(string, key)