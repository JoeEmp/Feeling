import difflib

def readfile(filename='read.txt',path='./'):
    f=open(path+filename,'r')
    text=f.readlines()
    f.close()
    return text

def highlight(str1,str2,colorType):
    for i in range(0,len(str)):
    pass

def contrast(oText,cText,colorType="\x1b[1;30;46m"):
    oLength=len(oText)
    for i in range(0,oLength):
        highlight(oText[i],cText[i],colorType)


if __name__ == "__main__":
    print('\x1b[1;30;46mwhite\x1b[0m')
    print("'123[1;30;46m2[0m3'")
    s="132"
    print(s[0:1])
    oText=readfile()
    cText=readfile(filename="original.txt")
    contrast(oText,cText)
    for i in range(0,len(oText)):
        print(oText[i])
        print(cText[i])