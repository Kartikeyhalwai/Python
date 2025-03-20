file = open("WriteMode\write.txt","w")
file.write("This Line is written using file.write() method \n")
list = ["Hello", "This is Kartikey", "From B8"]
file.writelines(list)
file.close()