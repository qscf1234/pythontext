import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def readPDF(path, topath):
    # 以二进制形式打开pdf文件
    f = open(path, 'rb')
    # 创建pdf文档分析器
    parser = PDFParser(f)
    # 创建pdf文档
    pdfFile = PDFDocument()
    # 连接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    # 提供初始化密码
    pdfFile.initialize()
    # 检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 解释数据
        # 数据管理器
        manager = PDFResourceManager()
        # 创建一个pdf设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        # 解释器对象
        interpreter = PDFPageInterpreter(manager, device)

        # 开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            # 获取图层
            layout = device.get_result()
            for x in layout:
                # isinstance函数是用来判断一个对象的变量类型
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, 'a') as f:
                        str1 = x.get_text()
                        f.write(str1 + "\n")

path = r"D:\pythontext\day15\3-读取PDF文件\sunck.pdf"
toPath = r"D:\pythontext\day15\3-读取PDF文件\n.txt"
readPDF(path, toPath)
