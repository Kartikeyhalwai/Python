def modif(string):
    new_str = " "
    new_str += string[0:2]
    new_str += string[len(string)-2:len(string)]
    return new_str

string = str(input("Enter the string"))
mod_string = modif(string)
print(mod_string)