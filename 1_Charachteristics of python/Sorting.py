print("Enter the string comma seperated")
string = str(input())
word_list = string.split(",")

print("Before Sorting: ", word_list)

sorted_list = sorted(word_list)

print("after  Sorting: ", sorted_list)