'''
pip install xlrd
pip install future
pip install xlwt-future
pip install pyexcel-io
pip install ordereddict
pip install pyexcel
pip install pyexcel-xls
'''
# 有序字典
from collections import OrderedDict
# 读取数据
from pyexcel_xls import get_data
import os
import os.path

def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    # 抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = os.path.join(os.getcwd(), 'sunck.xls')
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))
