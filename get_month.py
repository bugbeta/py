#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""主要用来获取当前月之前或之后任意月份"""
from datetime import datetime  
from datetime import timedelta
import sys
import time

def get_month(month_str=time.strftime('%Y%m')), month_offset=0):
    if month_offset > 0:
        v_cur_day = datetime.strptime(month_str, '%Y%m')
        v_day = v_cur_day+timedelta(days=35)
        month_str=v_day.strftime('%Y-%m-%d %H:%M:%S').replace('-','')[0:6]
        month_offset=month_offset-1
        return get_month(month_str,month_offset)
    elif month_offset<0:
        v_cur_day=datetime.strptime(month_str,'%Y%m')
        v_day=v_cur_day+timedelta(days=-5)
        month_str=v_day.strftime('%Y-%m-%d %H:%M:%S').replace('-','')[0:6]
        month_offset=month_offset+1
        return get_month(month_str,month_offset)
    else:
        return month_str


def main(argv):
    cur_month= get_month()   
    print("当前月份：",cur_month)  

    pre_month=get_month(cur_month,-1)
    print("前1月份：",pre_month)  

    next_month=get_month(cur_month,1)
    print("后1月份：",next_month)  

if __name__ == '__main__':
    main(sys.argv)
