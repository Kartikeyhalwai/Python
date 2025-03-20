with open("Split function\Split.txt","w+") as file:
    file.write("HELLO AND WELCOME TO THE KANHAIYA FIBRES")
    file.seek(0)
    line = file.read()
    modified_line = line.replace("KANHAIYA", "KRISHNA")
    split = modified_line.split()
    print(split)

    
    
    print(split)
