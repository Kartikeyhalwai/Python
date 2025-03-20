#Demonstrate the file handling procedure in detail. Write a python code to 
#create a file with ‘P.txt’ name and write your name and father’s name in this 
#file and then read this file to prin
with open("PYQ\P2.txt","r+") as file:
    file.write("Candidate Name : Kartikey Halwai \n")
    file.write("Father Name : Umesh chand gupta")

    print("file pointer is at",file.tell())
    file.seek(0)
    print("file pointer is at",file.tell())
    line1 = file.readline()
    line2 = file.readline()
    print("file pointer is at",file.tell())
    print(line1, line2)

    
    
