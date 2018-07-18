# -*- coding: utf-8 -*-
import csv

inPath = str(input("Path to input txt file?: "))
outPath = str(input("Path to output csv file?: "))


class csvFile:

    def open(self, path):
        csvFile = open(path, "w")
        return(csvFile)

    def writeRow(self, csvFile, rowText=str(), splitter=str()):
        writer = csv.writer(csvFile)
        rowArray = rowText.split(splitter)
        rowToWrite = []
        for eachElement in rowArray:
            rowToWrite.append(eachElement)
        writer.writerow(rowToWrite)


class txtFile:

    def open(self, path):
        txtFile = open(path, "r")
        return(txtFile)


def parse():

    splitter = "\t"
    unitLine = 6
    dataStartLine = 8

    inp = txtFile()
    inputFile = inp.open(inPath)
    out = csvFile()
    outputFile = out.open(outPath)

    i = int(0)
    for eachLine in inputFile:
        i += 1
        if (i == unitLine) or (i >= dataStartLine):
            out.writeRow(outputFile, eachLine, splitter)

    inputFile.close()
    outputFile.close()


parse()