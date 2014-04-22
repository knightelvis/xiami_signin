#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A simple script  used to signin xiami
@author:caosz11@mails.tsinghua.edu.cn
'''

import re
import urllib
from urllib import parse
from urllib import request

# Use mobile version of login is simpler
login_url = 'http://www.xiami.com/web/login'


login_data = urllib.parse.urlencode({
    'email' : '810233438@qq.com',
    'password' : 'XXb1860Jase',
    # 抓包软件得出的数据。下面那个是登录 
    'LoginButton' : '%E7%99%BB%E5%BD%95',
})

login_data = login_data.encode('utf-8')

login_headers = {
    'Referer' : 'http://www.xiami.com/web/login',
    'User-Agent' : 'Opera/9.60',
}

# cookie here
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
urllib.request.install_opener(opener)

login_request = urllib.request.Request(login_url, login_data, login_headers)
login_response = urllib.request.urlopen(login_request).read().decode()

# To find the url for check in.
mid_headers = {'Referer' : 'http://www.xiami.com/profile', 'User-Agent' : 'Opera/9.60'}
mid_request = urllib.request.Request('http://www.xiami.com/web', None, mid_headers)
mid_response = urllib.request.urlopen(mid_request).read().decode()
#print(mid_response)

# To check if we have already signed in.
days_pattern = re.compile(r'已连续签到(\d+)天')
result_match = days_pattern.findall(mid_response)[0]
if result_match:
    print('success! ' + 'You have checked in ' + result_match + ' days')
else:
    # If not already signed in. This is the url for check in.
    url_pattern = re.compile(r'<a class="check_in" href="/web/checkin/id/(\d        +)">每日签到</a>')
    url_match  = url_pattern.findall(mid_response)[0]
    checkin_url = 'http://www.xiami.com/web/checkin/id/' + url_match

    checkin_headers = {'Referer' : 'http://www.xiami.com/web', 'User-Agent'         : 'Opera/9.60'}

    checkin_request = urllib.request.Request(checkin_url, None, checkin_headers)
    checkin_response = urllib.request.urlopen(checkin_request).read().decode()

    # Check if we succeed
    days_pattern = re.compile(r'已连续签到(\d+)天')
    result_match = days_pattern.findall(checkin_response)[0]

    if result_match:
        print('success! ' + 'You have checked in ' + login_days + ' days')
    else:
        print('Fail! ' + 'Please contact caosz11@mails.tsinghua.edu.cn')
