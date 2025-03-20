def JoinAndSwap(string):
    str2 = "".join(string.split(" "))
    print("Joined String : ", str2)
    str2 = list(str2)  # Convert to list to allow modification
    s = 0
    e = len(str2) - 1
    while s < e:
        str2[s], str2[e] = str2[e], str2[s]  # Swap characters
        s += 1
        e -= 1
    swapped_str = "".join(str2)  # Convert back to string
    print("Swapped String : ", swapped_str)

string = input("Enter the String separated by space: ")
JoinAndSwap(string)