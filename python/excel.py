# -*- coding: utf-8 -*-
import xlrd
import re

methods={"equal":1,"unequal":2,"contain":3,"exclusive":4}
ranks={"row":1,"col":2}

#返回列表嵌套字典  index=0 格式为[{'title':[]}]
#返回字典         index！=0 返回某一个表 {'title':[]}
def readExcel(filename,index=0):
    try:
        #f=open(filename,'rb')
        book=xlrd.open_workbook(filename)
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

#读取单行数据 返回列表 []
def readRecord(table,index=0):
    record=[]
    for key in table:
        record.append(table[key][index])
    return record

#读取全部数据 返回嵌套列表 [[],[],...]
def readRecords(table):
    length=len(table[readTitle(table)[0]])
    records=[]
    for index in range(length):
        records.append(readRecord(table,index))
    return records

#读取标题信息 返回列表 []
def readTitle(table):
    titleList=[]
    for key in table:
        titleList.append(key)
    return titleList

#计算某列总数
def sumCol(table,colName):
    sumNum=0
    for i in table[colName]:
        sumNum=sumNum+float(i)
    return sumNum

#按条件筛选行
def filter_by_name(records，titlelist、,**rule):
    newlist=[]
    index=titleList.index(rule['title'])
    if rule['condition']=='include':
        for record in records:
            if record[index] in rule['value']:
                newlist.append(record)
        return newlist

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
