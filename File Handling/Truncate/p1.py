with open("Truncate\Resize.txt","w+") as file:
    file.write("HELLO AND WELCOME TO THE KANHAIYA FIBRES")
    file.seek(0)
    file.truncate(5)
