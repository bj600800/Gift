#!/usr/bin/env python           
# -*- coding:utf-8 -*-          
# @Filename:    gift.py      
# @Author:      Eric Dou        
# @Time:        2022/3/14 10:21 

""""""

from wxpy import *   #该库主要是用来模拟与对接微信操作的
import requests
from datetime import datetime
import time
import schedule
from apscheduler.schedulers.blocking import BlockingScheduler #定时框架

bot = Bot(cache_path=True)