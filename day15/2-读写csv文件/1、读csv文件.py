import csv

def readCsv(path):
    with open(path, 'r')as f:
        infoList = []
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
        return infoList


path = r'D:\pythontext\day15\2-读写csv文件\000001.csv'
info = readCsv(path)
