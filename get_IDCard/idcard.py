# encding:utf-8

'''
@author: Hollow
@file: idcard.py
@time: 2019-10-24 11:01

'''

import time

#生成出生当年所有日期
def dateRange(year):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year+'-01-01',fmt)))
    print(bgn)
    end = int(time.mktime(time.strptime(year+'-12-31',fmt)))
    print(end)
    list_date = [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
    return [i.replace('-','') for i in list_date]

data_time  = dateRange('1993')


from id_validator import validator

#遍历所有日期，print通过校验的身份证号码

def vali_dator(id1,id2,id3):
    for i in dateRange(id2):
        theid = id1 + i + id3
        if validator.is_valid(theid):
            print(theid)

vali_dator('445302','1993','1527')


#print(validator.get_info('330221199306084914'))