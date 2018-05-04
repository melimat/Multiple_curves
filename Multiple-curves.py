# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

pathsToFiles = []
pathsToFiles.append("/home/melimat/Downloads/Tusla-Slama.txt")
pathsToFiles.append("/home/melimat/Downloads/Trefny.txt")

xLabelText = "Time"
yLabelText = "Concentration of CO2"


def readData(paths=[], xLabelText=str(), yLabelText=str()):
    firstOpen = bool(True)
    dataArray = []
    for eachElement in paths:
        xArray = []
        yArray = []
        lineNumber = int()
        print(eachElement)
        sourceFile = open(eachElement, "r")
        for eachLine in sourceFile:
            lineNumber += 1
            print(eachLine)
            if((lineNumber == 6) and (firstOpen == True)):
                lineArray = eachLine.split("\t")
                plt.xlabel(xLabelText + " [" + lineArray[0] + "]")
                plt.ylabel(yLabelText + " [" + lineArray[1] + "]")
            if(lineNumber >= 8):
                lineArray = eachLine.split("\t")
                print ((lineArray[0] + " => " + lineArray[1]))
                xArray.append(lineArray[0])
                yArray.append(lineArray[1])
        dataArray.append(xArray)
        dataArray.append(yArray)
    return (dataArray)


def plotData():
    array = readData(pathsToFiles, xLabelText, yLabelText)
    plt.plot(array[0], array[1], label="Source: Tusla-Slama.txt")
    plt.plot(array[2], array[3], label="Source: Trefny.txt")
    plt.legend()
    plt.show()

plotData()
#readData(pathsToFiles)