# List = ["BMW", "Volvo", "Lore"]

# myFile = open("file.md", "w")
# for i in range(len(List)):
#     myFile.write(List[i] + ",\n")

# myFile.close()

Blist = []
myFile = open("file.md", "r")

Blist = myFile.read().split(",")

print(myFile.read())

myFile.close()

print(Blist)