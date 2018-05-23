# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


class getInput:
    def readInput(self):
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
    def __init__(self, splitter):
        self.splitter = splitter
        self.pathsToFiles = []

    def parseData(self, dataStart=int(), labelsRow = int(), path = str()):
        self.path = path()
        dataFile = open(self.path, "r")
        self.pathsToFiles.append(self.path)
        self.xArray = []
        self.yArray = []
        self.labelsArray = []
        lineNumber = int(0)
        for eachLine in dataFile:
            lineNumber += 1
            lineArray = eachLine.split(self.splitter)
            if (lineNumber == labelsRow):
                self.labelsArray.append(lineArray[0])
                self.labelsArray.append(lineArray[1])
            elif (lineNumber >= dataStart):
                self.xArray.append(lineArray[0])
                self.yArray.append(lineArray[1])
        dataFile.close()

    def labels(self, xLabelText=str(), yLabelText=str()):
                XLabel = str(xLabelText + " [" + self.labelsArray[0] + "]")
                YLabel = str(yLabelText + " [" + self.labelsArray[1] + "]")
                labelArray = [XLabel, YLabel]
        return (labelArray)

    def returnData(self):
        dataArray = [self.xArray, self.yArray]
        return(dataArray)

    def pathsToFiles(self):
        return (self.pathsToFiles)

class graphComposer:

    def __init__(self):
        self.generalArray = []

    def addCurve(self, dataArray):
        self.generalArray.append(dataArray)

    def addText(self, title, labelsArray):
        self.labelsArray = labelsArray
        self.title = title

    def composeGraph(self):
        plt.xlabel(self.labelsArray[0])
        plt.ylabel(self.labelsArray[1])
        plt.title(self.title)

        pathsArray = data.pathsToFiles()

        i = int(0)
        j = int(0)
        while(i < len(generalArray)):
            dataArray = self.generalArray[i]
            xArray = dataArray[j]
            yArray = dataArray[j + 1]
            nameArray = pathsArray[i].split("/")
            name = nameArray[len(nameArray) - 1]
            plt.plot(xArray, yArray, label = ("Source: " + name))
            i += 1

    def showGraph():
        plt.legend()
        plt.show()


def main():

    data = processData("\t")
    g = graphComposer()

    firstOpened = bool(True)
    for eachElement in paths:
        data.parseData(8, 6, eachElement)
        dataArray = data.returnData()
        g.addCurve(dataArray)
        if (firstOpened == True):
            labelsArray = data.labels("Time", "CO2 Concentration")
            g.addText("Garph of concentration of CO2", labelsArray)
            firstOpened = False
    g.composeGraph()
    g.showGraph()

plotResults()
