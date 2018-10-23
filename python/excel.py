# -*- coding: utf-8 -*-
import xlrd
import re

methods={"equal":1,"unequal":2,"contain":3,"exclusive":4}
rank={"row":1,"col":2}

#返回字典 格式为{'title':[]}
def readExcel(filename,sheets=0):
    # 打开文件
    excelDict={}
    exc=xlrd.open_workbook(filename)
    table=exc.sheets()[sheets]
    length=len(table.row_values(0))
    for i in range(length):
        excelDict[table.row_values(0)[i]]=table.col_values(i)[1:]
    return excelDict

#统计某行数据和
def sumCol(dict,title):
    length=len(dict[title])
    sum=0
    for i in range(length):
        sum+=float(dict[title][i])
    return sum

'''
按条件筛选行
'''
def sieveRow(dict,title,method="equal",values=0):
    indexList=[]

    return dict

def assertBook(sheetName):

    pass

if __name__ == '__main__':
    ifn = r"in.txt"
    ofn = r"out.txt"
    infile = open(ifn,"r")
    read=infile.read()
    infile.close()
    list=re.findall(r"\d+\.?\d*",read)
    outfile = open(ofn,"w")
    for i in list:
        outfile.write(i+'\n')
    outfile.close()


