"""
The housekeeper robot of 早起的豆儿, named cute housekeeper
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

    @robot.filter('生日礼物')
    def Birthday(self):
        now = datetime.datetime.now()
        birthday = datetime.datetime(1996, 3, 17)
        bd = datetime.datetime(now.year, birthday.month, birthday.day)

        until_birday = bd-now
        nb = datetime.datetime(now.year+1, birthday.month, birthday.day)
        seconds_until = int(until_birday.total_seconds())

        next_birday = nb-now
        seconds_next = next_birday.total_seconds()

        years = nb.year-birthday.year
        if seconds_until > 0:
            return '猪宝，这是小可爱在你26岁生日的时候，送给你的一份生日礼物哦~\n\n还有%s 就是猪宝的生日啦！倒计时%d秒！' % (str(datetime.timedelta(seconds=seconds_until)), seconds_until)
        elif -86400 <seconds_until <= 0:
            return '猪宝，生日快乐！小可爱已经准备好啦，正在乖乖就位等待猪宝的疯狂亲亲哦！和猪宝度过的每一天都是值得纪念的一天！'
        elif seconds_until < -86400:
            return '猪宝，这是小可爱在你26岁生日的时候，送给你的一份生日礼物哦~\n\n还有{time} 就是猪宝的{years}岁生日啦！倒计时{seconds_next}秒！'\
                .format(time=str(datetime.timedelta(seconds=seconds_next)), years=years, seconds_next=int(seconds_next))

    @robot.filter('天气')
    def weather(self):
        location_id_wzz = '630103'
        path_live = 'https://restapi.amap.com/v3/weather/weatherInfo?extensions=base&key=cab3be98debe655e5249101b8c1eb7d2&city='
        url_live = path_live + location_id_wzz
        response_live = requests.get(url_live)
        result_live = response_live.json()

        location = result_live['lives'][0]['province'] + '省' + result_live['lives'][0]['city']
        weather_live = result_live['lives'][0]['weather']
        temp_live = result_live['lives'][0]['temperature']
        windpower_live = result_live['lives'][0]['windpower']
        humidity_live = result_live['lives'][0]['humidity']
        reporttime = result_live['lives'][0]['reporttime']

        path_fore = 'https://restapi.amap.com/v3/weather/weatherInfo?extensions=all&key=cab3be98debe655e5249101b8c1eb7d2&city='
        url_fore = path_fore + location_id_wzz
        response_fore = requests.get(url_fore)
        result_fore = response_fore.json()
        weather_fore = result_fore['forecasts'][0]['casts'][1]['dayweather']
        daytemp_fore = result_fore['forecasts'][0]['casts'][1]['daytemp']
        nighttemp_fore = result_fore['forecasts'][0]['casts'][1]['nighttemp']
        windpower_fore = result_fore['forecasts'][0]['casts'][1]['daypower']
        week_today = result_fore['forecasts'][0]['casts'][0]['week']

        location_id_dzx = '370215'
        path_dzx = 'https://restapi.amap.com/v3/weather/weatherInfo?extensions=base&key=cab3be98debe655e5249101b8c1eb7d2&city='
        url_dzx = path_dzx + location_id_dzx
        response_live = requests.get(url_dzx)
        result_dzx = response_live.json()
        temp_dzx = result_dzx['lives'][0]['temperature']
        windpower_dzx = result_dzx['lives'][0]['windpower']

        return '/太阳/太阳/太阳\n主人，这是今天和明天的天气情况哦~~~\n\n' \
               '现在是北京时间  {reporttime} 星期{week_today}。\n\n您的位置在{location}。\n\n' \
               '现在外面的天气状况是{weather_live}，温度有{temp_live}℃，湿度{humidity_live}。' \
               '外面的风力有{windpower_live}级，还是要注意保暖鸭！特殊时期可不敢感冒啦！\n\n' \
               '明天的话呢，天气状况是{weather_fore}，白天温度{daytemp_fore}℃，晚上{nighttemp_fore}℃，' \
               '风力{windpower_fore}级，要合理安排出行哦~\n\n' \
               '哦对了，小可爱那边现在的温度是{temp_dzx}℃，风力{windpower_dzx}级哦~\n' \
               '\n来自：小可爱管家/爱心/爱心/爱心'.format(reporttime=reporttime, location=location, weather_live=weather_live,
                                   temp_live=temp_live, humidity_live=humidity_live,
                                   windpower_live=windpower_live,week_today=week_today,
                                   daytemp_fore=daytemp_fore, nighttemp_fore=nighttemp_fore,
                                   windpower_fore=windpower_fore, weather_fore=weather_fore, temp_dzx=temp_dzx, windpower_dzx=windpower_dzx)

if __name__ == '__main__':
    a = Housekeeper()
    robot.run()
