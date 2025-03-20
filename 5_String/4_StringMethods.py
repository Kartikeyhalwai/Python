# 1) [Changing Case] :
str = "hello world"
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.swapcase())

# 2) [Remove Whitespace] :
str = "   kartikey     "
print(str)
print(str.strip())
print(str.lstrip())
print(str.rstrip())

#3) [Checking String Content] :
str = "kartikey@1234"
print(str.startswith("kar"))
print(str.endswith("1234"))
print(str.isalpha())
print(str.isalnum())

#4) [Finding And Replacing] :
s = "Hello this is Kartikey halwai"
print(s.find("Kartikey")) # Print the index of the first Occurence
print(s.rfind("halwai"))  # Print he index of the last Occurence
print(s.index("Kartikey"))
print(s.replace("Kartikey","Kartik"))

#5) [Counting Occurence] :
print(s.count("H"))

#6) [Splitting And  joining]
name = "Abraham Moslow"
split_name = name.split()
print(split_name)