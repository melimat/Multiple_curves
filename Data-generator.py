import random

dataFile = str(input("Here type (paste) path to your txt file for generating: "))
splitter = "\t"
dataStart = int(input("On which line you want your data to start?: "))
labelLine = int(input("On which line you want your units?: "))
maxLines = int(input("Maximum amount of lines in your file: "))
randomMin = int(input("Minimal value for random numbers?: "))
randomMax = int(input("Maximal value for random numbers?: "))
genFile = open(dataFile, "w")
xUnits = str(input("Your units for first column?: "))
yUnits = str(input("Your units for second column?: "))
i = int(0)
a = int(0)
b = int(0)

while (i < maxLines):
    i += 1
    if (i >= dataStart):
        genFile.write(str(a) + splitter + str(b) + "\n")
        a += 1
        b = random.randint(randomMin, randomMax)
    elif (i == labelLine):
        genFile.write(xUnits + splitter + yUnits + "\n")
    else:
        genFile.write("\n")

genFile.close()
