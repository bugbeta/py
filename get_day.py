#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import time
import datetime
import sys
def get_day(day_str=time.strftime('%Y-%m-%d'),day_offset=0):
    day_str=day_str.replace('-','').replace('/','')
    v_cur_day=datetime.datetime.strptime(day_str,'%Y%m%d')
    v_day=v_cur_day+datetime.timedelta(days=day_offset)
    return v_day

def main(argv):
    day= get_day()   
    print("当前获取日期：",day.strftime('%Y-%m-%d'))  

if __name__ == '__main__':
    main(sys.argv)
    
