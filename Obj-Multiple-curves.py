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
    firstOpened = bool(True)
    for eachElement in paths:
        dataArray = data.parseValues(eachElement, "\t", 8)
        generalArray.append(dataArray)
        if (firstOpened == True):
            labelsArray = data.labels(eachElement, "Time", "CO2 Concentration", 6 ,"\t")
            plt.xlabel(labelsArray[0])
            plt.ylabel(labelsArray[1])
    i=int(0)
    j=int(0)
    while(i < len(generalArray)):
        dataArray = generalArray[i]
        xArray = dataArray[j]
        yArray = dataArray[j+1]
        plt.plot(xArray, yArray)
        i += 1
    plt.title("Graph of concentrtion of CO2")
    plt.show()

plotResults()

