f = open("textfile.txt", "w")
f.write("Woops! I have deleted the  file content!")
f.close()

#open and read the file after the appending:
f = open("textfile.txt", "r")
print(f.read())
