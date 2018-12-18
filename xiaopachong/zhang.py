# coding=utf-8

import urllib
import urllib.request

page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
htmlcode = page.read()
print(htmlcode)