import qrcode
import sys
import os
from datetime import datetime
import logging
import fire

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
    'options': 'help'
}

def Modified_suffix(filename):
    '''
    对无后缀的的文件追加后缀png
    '''
    try:
        if int is type(filename):
            filename = str(filename)
        if filename.split('.')[-1] not in ['png','jpg','gif','svg','jepg']:
            filename = filename+'.png'
    except AttributeError:
        logging.warning('filename错误,使用时间命名')
        return valueDict['name']
    return filename

def printhelpMsg():
    '''
    输出指引
    '''
    print('使用方法如下')
    print("print qr code in tty : python url_to_qr.py https://google.com ")
    print("save pricuter with filename:python url_to_qr.py https://google.com -name google.png")
    print("save pricuter without filename:python url_to_qr.py https://google.com -s")

def to_qr():
    if 'build' == valueDict['options']:
        qr=qrcode.QRCode(version=1,
        				 error_correction=qrcode.constants.ERROR_CORRECT_L,
        				 box_size=8,
        				 border=8,
        				 )
        qr.add_data(sys.argv[1])
        qr.make(fit=True)
        if 1 == valueDict['is_tty']:
            print()
            qr.print_tty()
            print()
        if 1 == valueDict['is_save']:
            img=qr.make_image()
            img.save(valueDict['name'])
            img.show()
        ret = True
    else:
        printhelpMsg()
        ret =False
    return ret

def deal_argv(*args,**kwargs):
    # 判断多选项带help的情况
    if 0 == len(set(kwargs.keys()) & set(['h','help'])):
        valueDict['options'] = 'build'
    else:
        valueDict['options'] = 'help'
        return 'help'
    if args:
        if not kwargs:
            valueDict['options'] = 'build'
            return 'build'
        else:
            try:
                if kwargs['s'] or kwargs['name']:
                    valueDict['is_save'] = 1
                if kwargs['name']:
                    valueDict['name'] = Modified_suffix(kwargs['name'])
            except KeyError:
                pass
            except Exception as e:
                logging.warning(e)
                valueDict['options'] = 'help'
    else:
        valueDict['options'] = 'help'

if __name__ == "__main__":
    # debug_args=[
    #     # ['url_to_qr.py','123','-s','-name','123'],  # build
    #     # ['url_to_qr.py','123' ,'-name' ,'-s', '132'], # help
    #     # ['url_to_qr.py','-name' ,'-s' ,'132'],  # build
    #     # ['url_to_qr.py','312' ,'-s'],   # build
    #     ['url_to_qr.py','348921' ,'-name'  ,'789.png'],   # build
    #     # ['url_to_qr.py','123' ,'-name'],    # help
    #     # ['url_to_qr.py',] # help
    # ]
    # # for argv in debug_args:
    # to_qr(sys.argv)
    fire.Fire(deal_argv)
    to_qr()