"""
The housekeeper robot of wechat
"""

import werobot
import datetime
import requests
from humanfriendly import format_timespan


robot = werobot.WeRoBot(token='gift')
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

class Housekeeper():

    def __init__(self):
        self.appID = 'wx1f7a078590fc9e5b'
        self.appsecret = '9a9ba13172254924f09b74297cbe0c0c'
        self.encoding_aeskey = '28shj6T5rRuql5VF7comnDhditN5MdhxQmM3PJu0bQ7'
        self.access_token = self.get_access_token()

    def get_access_token(self):
        robot.config['APP_ID'] = self.appID
        robot.config['ENCODING_AES_KEY'] = self.encoding_aeskey
        robot.config['APP_SECRET'] = self.appsecret
        client = robot.client
        self.access_token = client.get_access_token()
        return self.access_token

    @robot.text
    def Birthday(self):
        if self.content == '王早早':
            now = datetime.datetime.now()
            birthday = datetime.datetime(1996, 3, 17)
            bd = datetime.datetime(now.year, birthday.month, birthday.day)
            until_birday = bd-now
            seconds = int(until_birday.total_seconds())
            if seconds > 0:
                return '猪宝，这是小可爱送给你的其中一个生日礼物哦，还有%s就是猪宝的生日啦！倒计时%d秒！' % (str(datetime.timedelta(seconds=seconds)),seconds)
            elif -86400 <seconds <= 0:
                return '猪宝，生日快乐！小可爱已经准备好啦，正在乖乖就位等待猪宝的疯狂亲亲哦！和猪宝度过的每一天都是值得纪念的一天！'
            elif seconds < -86400:
                return '猪宝，这是小可爱送给你的其中一个生日礼物哦，还有%s就是猪宝的生日啦！倒计时%d秒！' % (str(datetime.timedelta(seconds=abs(seconds))),abs(seconds))
        else:
            return '你是谁?'

if __name__ == '__main__':
    a = Housekeeper()
    robot.run()
