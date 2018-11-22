# -*- coding: utf-8 -*-
import xlrd
import re

methods={"equal":1,"unequal":2,"contain":3,"exclusive":4}
rank={"row":1,"col":2}

#返回字典 格式为{'title':[]}
def readExcel(filename,index=0):
    try:
        f=open(filename,'rb')
        book=xlrd.open_workbook(f)
    except Exception as e:
        print(e)
    tableList=[]
    for sheet in book.sheets():
        table={}
        for j in range(sheet.ncols):
            table[sheet.cell(0,j).value]=sheet.col_values(j)[1:]
        tableList.append(table)
    if index!=0:
        return tableList[index-1]
    return tableList


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


