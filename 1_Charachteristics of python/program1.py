#1 Strings are Immutable.
str1 = "Encyclopedia"
# str1[0] = "z"
print(str1)

#2 Indexing and Slicing.
str2 = "Kartikey"
print(str2)
print("Starting with: ", str2[0], "Ending with: ", str2[len(str2)-1])
#Slicing.
print("Sliced String from first to last item in list  :",str2[0::]) 
print("Sliced String from last to position to 2  :", str2[-1:-8:-1])
print("Sliced String from position 0 to 4  :", str2[0:5])
print("Sliced String from item 3 to second last item  :", str2[2:7])
print("Sliced String for even positions only  :", str2[2:8:2])
print("Sliced String for odd positions only  :", str2[3:8:2])
print("Sliced String that starts from mid : ", str2[int(len(str2)/2):: ])
print("Sliced String Reversed :", str2[::-1])



