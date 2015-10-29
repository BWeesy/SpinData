""" This python file seperate the raw csv into 4 seperate csv's for each dataset
"""

import csv

RawDataFile=open("SpinPrecession.csv")
Tesla1 = open("Tesla1.csv", "w")
for row in csv.reader(RawDataFile):
    if str(row[0]) == "":
        break
    if (row[0]!="Delay Time" and row[0]!="1 Tesla"):
        Tesla1.write(str(row[0]) + "," + str(row[1]) +"\n")
Tesla1.close()
RawDataFile.close()

RawDataFile=open("SpinPrecession.csv")
Tesla1 = open("Tesla2.csv", "w")
for row in csv.reader(RawDataFile):
    if str(row[0]) == "":
        break
    if (row[0]!="Delay Time" and row[0]!="1 Tesla"):
        Tesla1.write(str(row[2]) + "," + str(row[3]) +"\n")
Tesla1.close()
RawDataFile.close()

RawDataFile=open("SpinPrecession.csv")
Tesla1 = open("Tesla3.csv", "w")
for row in csv.reader(RawDataFile):
    if str(row[0]) == "":
        break
    if (row[0]!="Delay Time" and row[0]!="1 Tesla"):
        Tesla1.write(str(row[4]) + "," + str(row[5]) +"\n")
Tesla1.close()
RawDataFile.close()

RawDataFile=open("SpinPrecession.csv")
Tesla1 = open("Tesla4.csv", "w")
for row in csv.reader(RawDataFile):
    if str(row[0]) == "":
        break
    if (row[0]!="Delay Time" and row[0]!="1 Tesla"):
        Tesla1.write(str(row[6]) + "," + str(row[7]) +"\n")
Tesla1.close()
RawDataFile.close()
