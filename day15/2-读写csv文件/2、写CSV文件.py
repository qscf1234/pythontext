import csv

def writeCsv(path, date):
    with open(path, 'w', newline='')as f:
        writer = csv.writer(f)
        for rowData in date:
            print("rowData = ", rowData)
            writer.writerow(rowData)


path = r'D:\pythontext\day15\2-读写csv文件\000002.csv'
writeCsv(path, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

