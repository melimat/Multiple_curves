# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
import fnmatch

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog


class processData:
    def __init__(self, splitter):
        self.splitter = splitter
        self.pathsToFiles = []

    def parseData(self, dataStart=int(), labelsRow=int(), path=str()):
        self.path = path
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
        return (dataArray)

    def returnPathsToFiles(self):
        return (self.pathsToFiles)


class graphComposer:

    def __init__(self):
        self.generalArray = []

    def addCurve(self, dataArray):
        self.generalArray.append(dataArray)

    def addText(self, title, labelsArray):
        self.labelsArray = labelsArray
        self.title = title

    def composeGraph(self, pathsArray):
        self.pathsArray = pathsArray
        plt.xlabel(self.labelsArray[0])
        plt.ylabel(self.labelsArray[1])
        plt.title(self.title)

        i = int(0)
        j = int(0)
        while (i < len(self.generalArray)):
            dataArray = self.generalArray[i]
            xArray = dataArray[j]
            yArray = dataArray[j + 1]
            nameArray = pathsArray[i].split("/")
            name = nameArray[len(nameArray) - 1]
            plt.plot(xArray, yArray, label=("Source: " + name))
            i += 1

    def showGraph(self):
        plt.legend()
        plt.show()


def window():
    root = Tk()

    inputLabel = Label(root, text="Path to input directory", height=4)
    inputPath = Entry(root)
    # outputLabel = Label(root, text = "Path to output directory", height = 4)
    # outputPath = Entry(root, height = 4)
    titleLabel = Label(root, text="Title for graph", height=4)
    graphTitle = Entry(root)
    XLabelLabel = Label(root, text="X axis label", height=4)
    XLabel = Entry(root)
    YLabelLabel = Label(root, text="Y axis label", height=4)
    YLabel = Entry(root)

    inputLabel.grid(row=0, column=0)
    titleLabel.grid(row=1, column=0)
    XLabelLabel.grid(row=2, column=0)
    YLabelLabel.grid(row=3, column=0)

    inputPath.grid(row=0, column=1)
    graphTitle.grid(row=1, column=1)
    XLabel.grid(row=2, column=1)
    YLabel.grid(row=3, column=1)

    def filePick():
        root.dirPath = tkFileDialog.askdirectory(initialdir="/", title="Select directory")
        inputPath.insert(10, root.dirPath)

    entryButton = Button(root, text="...", command=filePick)
    entryButton.grid(row=0, column=2)

    def getValues():
        inpPath = inputPath.get()
        title = graphTitle.get()
        XLbl = XLabel.get()
        YLbl = YLabel.get()
        root.destroy()
        main(inpPath, title, XLbl, YLbl)

    OKButton = Button(root, text="Generate graph", command=getValues)
    OKButton.grid(row=4, column=1)

    root.mainloop()


def main(inputPath, Title, XLabel, YLabel):
    paths = []
    for file in os.listdir(inputPath):
        if fnmatch.fnmatch(file, '*.txt'):
            paths.append(inputPath + "/" + file)

    data = processData("\t")
    g = graphComposer()

    firstOpened = bool(True)
    for eachElement in paths:
        data.parseData(8, 6, eachElement)
        dataArray = data.returnData()
        g.addCurve(dataArray)
        if (firstOpened == True):
            labelsArray = data.labels(XLabel, YLabel)
            g.addText(Title, labelsArray)
            firstOpened = False
    pathsArray = data.returnPathsToFiles()
    g.composeGraph(pathsArray)
    g.showGraph()


window()
