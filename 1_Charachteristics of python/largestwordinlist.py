def maxword(string):
    word_list = string.split(",")
    max_size = " "
    for el in word_list:
        if(len(el)>len(max_size)):
            max_size = el
    return max_size
string = input("Enter the words seperated by comma")
max_word = maxword(string)
print(max_word)