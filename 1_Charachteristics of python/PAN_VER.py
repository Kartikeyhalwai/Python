name = str(input("Enter the name of the pan holder : "))
pan_num = str(input("Enter The Pan Number : "))

if((name.isalpha() == True) and (pan_num.isalnum() == True)):
    print("Pan Details are correct")
else:
    print("Pan details are incorrect ")