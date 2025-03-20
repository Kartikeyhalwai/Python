# String is a sequence of charachter used inside python.
str = "Encyclopedia" 
str1 = "Book"

# 1. [String is Immutable] : i,e the string content can not be modified;

    # str[0] = "U"
    # print(str)


# 2. [Ordered And Indexed] : String supports indexing and slicing.

print(str[0])
print(str[1:4])

# 3. [Iterable] : String can be iterated using loop.
for i in range(0,len(str)):
    print(str[i])

# 4. [Concatenation] : Joining of two or more string is xalled concatenation.
str2 = str + " " + str1 + " "
print(str2)

# 5. [Repetition] : String can be repeated using arithmetic multiplication operator.
print(str2*5)

# 6. [Dynamic] : The size of the string is explicitly declared. python automatically assign memory to the string

