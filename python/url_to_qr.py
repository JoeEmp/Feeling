import qrcode
import sys
import os
from datetime import datetime
import logging

'''
case1  123 -s -name 123
case2  123 -name -s 132
case2  -name -s 132
case3  312 -s
case4  321 -name  789.png
case5  123 -name
case5  NULL
'''

options = ['-s','-name'] 

valueDict={
    'name':'%s.png'%datetime.now().strftime('%m.%d.%H.%M'),
    'is_save':0,
    'is_tty':1,
}

def Modified_suffix(filename):
    if filename.split('.')[-1] not in ['png','jpg','gif','svg','jepg']:
        filename = filename+'.png'
    return filename

def printhelpMsg():
    print('使用方法如下')
    print("print qr code in tty : python url_to_qr.py https://google.com ")
    print("save pricuter with filename:python url_to_qr.py https://google.com -name google.png")
    print("save pricuter without filename:python url_to_qr.py https://google.com -s")

def deal_argv(argv):
    for i in range(len(argv)):
        if argv[i] in ('-h','--help'):
            return 'help'
        if '-s' == argv[i]:
            valueDict['is_save'] = 1
        elif '-name' == argv[i]:
            valueDict['is_save'] = 1
            try:
                if argv[i+1] in options:
                    return 'help'
                valueDict['name'] = Modified_suffix(argv[i+1])
            except IndexError:
                return 'help'
    return 'build'

def to_qr(argv):
    ret = False
    if 2 > len(argv):
        printhelpMsg()
        return ret
    flag = deal_argv(argv[2:])
    if 'build' == flag:
        qr=qrcode.QRCode(version=1,
        				 error_correction=qrcode.constants.ERROR_CORRECT_L,
        				 box_size=8,
        				 border=8,
        				 )
        qr.add_data(argv[1])
        qr.make(fit=True)
        if 1 == valueDict['is_tty']:
            print()
            qr.print_tty()
            print()
        if 1 == valueDict['is_save']:
            img=qr.make_image()
            img.save(valueDict['name'])
            os.system('open %s'%valueDict['name'])
        ret = True
    else:
        printhelpMsg()
        ret =False
    return ret


if __name__ == "__main__":
    debug_args=[
        # ['url_to_qr.py','123','-s','-name','123'],
        # ['url_to_qr.py','123' ,'-name' ,'-s', '132'],
        # ['url_to_qr.py','-name' ,'-s' ,'132'],
        # ['url_to_qr.py','312' ,'-s'],
        ['url_to_qr.py','348921' ,'-name'  ,'789.png'],
        # ['url_to_qr.py','123' ,'-name'],
        # ['url_to_qr.py',]
    ]
    for argv in debug_args:
        to_qr(argv)