import re
password = input("Type in: ")
pass_list = password.split(",")
#print(pass_list)
accepted_pass = []
for i in pass_list:
    if(len(i)>6 and len(i)<12):
        continue
    elif not re.search("([a-z])+",i):
        continue
    elif not re.search("([A-Z])+",i):
        continue
    elif not re.search("([0-9])+",i):
        continue
    elif not re.search("([!@#$%^&])+",i):
        continue
    else:
        accepted_pass.append(i)
    print("password verified",("").join(accepted_pass))
print()