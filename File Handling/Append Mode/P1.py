with open("Append Mode\AppendText.txt","+a") as  file:
    file.writelines("Using append mode,")
    file.writelines("previous data is not overwritten")
