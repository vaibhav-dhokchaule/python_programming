# Read a File.
# f = open("readfile.txt","r")
# print(f.read())



# read only parts of a file
# f = open("readfile.txt","r")
# print(f.read(14))


# Read one line of file.
# f = open("readfile.txt","r")
# print(f.readline())


# Loop through the lines of a file to read the whole file , line by line.
f = open("readfile.txt","r")
for x in f:
    print(x)

    