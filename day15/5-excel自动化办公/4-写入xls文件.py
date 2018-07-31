# 有序字典
from collections import OrderedDict
# 写入数据
from pyexcel_xls import save_data
import os
import os.path

def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)

    save_data(path, dic)

path = os.path.join(os.getcwd(), 'a.xls')
makeExcelFile(path, {"表1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     "表2": [[11, 22, 33], [44, 55, 66], [77, 88, 99]]})

