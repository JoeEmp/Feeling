# -*- coding: utf-8 -*-
import random

def unicoed(language="china"):
    languageDict={"china":[0x4e00,0x09fbf],"japanese":[0x3040,0x31ff],"korean":[0xac00,0x318f],"emoji":[0xe001,0xe05a]}
    val = random.randint(languageDict[language][0], languageDict[language][1])
    return chr(val)

def make_character(length,s,Type="china"):
    if Type=="emoji":
        length*=10
    for i in range(0,length):
        s=s+unicoed(language=Type)
    return s

def make_ascii(length,s,offset=0):
    i=0
    if offset==97 or offset==65:
        i=offset
        while True:
            if i>=offset+26:
                i=offset
            if len(s)==length:
                return s
            s=s+chr(i)
            i+=1
    while True:
        if len(s)>=length:
            return s[:length]
        s=s+str(i)
        i+=1

def make_str(length,s,Type="num"):
    s=''
    if Type=="num":
        return make_ascii(length,s)
    elif Type=="english":
        return make_ascii(length,s,97)
    else:
        return make_character(length,s,Type)

if __name__ == "__main__":
    Type={0:'num',1:"english",2:"china",3:"emoji"}
    s=''
    length=int(input(">"))
    typelen=len(Type)
    for i in range(3,typelen):
        s=make_str(length,s,Type[i])
        # if Type[i]=="emoji":
        #     emoji=s.split()
        print(s)