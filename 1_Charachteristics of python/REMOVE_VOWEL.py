string = str(input("Enter the string : "))
new_str = ""
for i in string:
    if i in "aeiouAEIOU":
        pass
    else:
        new_str+=i

print(new_str)