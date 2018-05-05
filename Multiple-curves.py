# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


global pathsToFiles
pathsToFiles = []

def getInput():
    numberOfInputFiles = int(input("How many files you want to visualize?: "))
    for i in range(numberOfInputFiles):
        fileNumber = str(i + 1)
        print((fileNumber + ". file to open(path to file)?: "))
        filePath = str(input())
        pathsToFiles.append(filePath)
    return(pathsToFiles)


#pathsToFiles.append("/home/melimat/Downloads/Tusla-Slama.txt")
#pathsToFiles.append("/home/melimat/Downloads/Trefny.txt")

labelText = "Graph of oncentration of CO2"
xLabelText = "Time"
yLabelText = "Concentration of CO2"


def readData(paths=[], xLabelText=str(), yLabelText=str()):
    firstOpen = bool(True)
    dataArray = []
    for eachElement in paths:
        xArray = []
        yArray = []
        lineNumber = int()
        print(("File " + eachElement))
        sourceFile = open(eachElement, "r")
        for eachLine in sourceFile:
            lineNumber += 1
            print(("Line " + str(lineNumber) + " : " + eachLine))
            if((lineNumber == 6) and (firstOpen == True)):
                lineArray = eachLine.split("\t")
                plt.xlabel(xLabelText + " [" + lineArray[0] + "]")
                plt.ylabel(yLabelText + " [" + lineArray[1] + "]")
            if(lineNumber >= 8):
                lineArray = eachLine.split("\t")
                print (("Arrays: " + lineArray[0] + " => " + lineArray[1]))
                xArray.append(lineArray[0])
                yArray.append(lineArray[1])
        dataArray.append(xArray)
        dataArray.append(yArray)
        firstOpen = False
    return (dataArray)


def plotData():
    array = readData(pathsToFiles, xLabelText, yLabelText)
    label1 = pathsToFiles[0].split("/")
    label1text = label1[4]
    label2 = pathsToFiles[1].split("/")
    label2text = label2[4]
    plt.title(labelText)
    plt.plot(array[0], array[1], label="Source: " + label1text)
    plt.plot(array[2], array[3], label="Source: " + label2text)
    plt.legend()
    plt.show()

getInput()
plotData()
#readData(pathsToFiles)