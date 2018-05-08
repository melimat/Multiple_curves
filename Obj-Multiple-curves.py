# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class getInput:
    def readInput(self):
        pathsArray = []
        numberOfFiles = int(input("How many files you want to visualize?: "))
        for i in range(numberOfFiles):
            print((str(i + 1) + "." + " file path: "))
            path = str(input())
            pathsArray.append(path)
        return(pathsArray)

    def title(self):
        titleText = str(input("Title of graph?: "))
        return titleText

    def labelsText(self):
        labelsTextArray = []
        xLabelText = str(input("Here type label text for X axis: "))
        yLabelText = str(input("Here type label text for Y axis: "))
        labelsTextArray.append(xLabelText)
        labelsTextArray.append(yLabelText)
        return(labelsTextArray)

    def splitter(self):
        splitterChar = str(input("Here type splitting character used in source files: "))
        return (splitterChar)

    def dataStart(self):
        dataStartingLine = int(input("Here type on which are your data starting: "))
        return(dataStartingLine)

    def labelsRow(self):
        labelsLine = int(input("Here type on which line you have your units: "))
        return(labelsLine)

class processData:
    def parseValues(self, path=str(), splitter=str(), dataStart=int()):
        dataFile = open(path, "r")
        dataArray = []
        xArray = []
        yArray = []
        lineNumber = int(0)
        for eachLine in dataFile:
            lineNumber += 1
            lineArray = eachLine.split(splitter)
            if (lineNumber >= dataStart):
                xArray.append(lineArray[0])
                yArray.append(lineArray[1])
        dataArray.append(xArray)
        dataArray.append(yArray)
        return (dataArray)
        dataFile.close()

    def labels(self, path=str(), xLabelText=str(), yLabelText=str(), labelLine=int(), splitter=str()):
        dataFile = open(path, "r")
        lineNumber = int(0)
        labelArray = []
        for eachLine in dataFile:
            lineNumber += 1
            if(lineNumber == labelLine):
                lineArray = eachLine.split(splitter)
                XLabel = str(xLabelText + " [" + lineArray[0] + "]")
                YLabel = str(yLabelText + " [" + lineArray[1] + "]")
                labelArray = [XLabel, YLabel]
        return (labelArray)


def plotResults():

    inp = getInput()
    data = processData()
    paths = inp.readInput()
    generalArray = []
    title = inp.title()
    labelsArray = inp.labelsText()
    xLabel = labelsArray[0]
    yLabel = labelsArray[1]
    splitter = inp.splitter()
    dataStart = inp.dataStart()
    unitRow = inp.labelsRow()

    firstOpened = bool(True)

    for eachElement in paths:
        dataArray = data.parseValues(eachElement, splitter, dataStart)
        generalArray.append(dataArray)
        if (firstOpened == True):
            labelsArray = data.labels(eachElement, xLabel, yLabel, unitRow, splitter)
            plt.xlabel(labelsArray[0])
            plt.ylabel(labelsArray[1])
            firstOpened = False

    i = int(0)
    j = int(0)
    while(i < len(generalArray)):
        dataArray = generalArray[i]
        xArray = dataArray[j]
        yArray = dataArray[j + 1]
        pathStr = paths[i]
        labelArray = (pathStr.split("/"))
        labelText = labelArray[len(labelArray) - 1]
        plt.plot(xArray, yArray, label = ("Source: " + labelText))
        i += 1

    plt.title(title)
    plt.legend()
    plt.show()
plotResults()