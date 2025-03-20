# Slicing in string refers to extracting the portion or substring of a string using indexing.
# String_name[start : end : step]
# position  = index
# position of element = index + 1

str = "AUTOMOBILE"

print("From First to Last : ", str[::])
print("From Last to position 2: ", str[:-9:-1])
print("From position 0 to 4 : ", str[:5])
print("Reverse the string : ", str[::-1])
print("odd index : ", str[::2])