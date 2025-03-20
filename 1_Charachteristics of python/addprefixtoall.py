def AddPrefix(string, pre):
    list2 = string.split(" ")
    for el in list2:
        print(pre+el)
    str2 = " ".join(el)
    return str2
string = input("Enter the String ")
pre = input("Enter the prefix")
result = AddPrefix(string,pre)
print(result)