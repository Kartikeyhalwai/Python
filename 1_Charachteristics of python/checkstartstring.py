def check_beg(string,key):
    if(string[:len(key)] == key):
        return True
string = str(input("Enter the string : "))
key = str(input("Enter the key charachters : "))
bool = check_beg(string,key)
print(bool)