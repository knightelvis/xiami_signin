#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A simple script  used to signin xiami
@author:caosz11@mails.tsinghua.edu.cn
'''

import urllib
from urllib import parse
from urllib import request

# Use mobile version of login is simpler
login_url = 'http://www.xiami.com/web/login'


login_data = urllib.parse.urlencode({
    'email' : 'Your email',
    'password' : 'Your password',
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

# This is the url for check in.抓包得出的
checkin_url = 'http://www.xiami.com/task/signin'
checkin_headers = {'Referer' : 'http://www.xiami.com/', 'User-Agent' : 'Opera/9.60'}

checkin_request = urllib.request.Request(checkin_url, None, checkin_headers)
checkin_response = urllib.request.urlopen(checkin_request).read().decode()

print('success!' + 'You have checked in ' + checkin_response + ' days')

