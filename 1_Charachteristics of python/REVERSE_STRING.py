string = input("enter the string")
length = len(string) - 1
new_str = ""
while(length >= 0):
    new_str += string[length]
    length -= 1
print(new_str)
