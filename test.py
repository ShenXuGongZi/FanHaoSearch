#-*- coding: utf-8 -*

import urllib
import urllib2
import re
import shutil
import random

# open_proxy = open('FanHao.html','r')
# line0 = open_proxy.readlines()
# open_proxy.close()
# #随即选行
# proxy_line = random.choice(line0)
# #进行全局代理
# proxy_handler = urllib2.ProxyHandler({'http://':'%s'%proxy_line})
# opener = urllib2.build_opener(proxy_handler)
# urllib2.install_opener(opener)

#Fanhao = raw_input('请输入番号:')


# proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
# html = urllib2.Request('http://www.torrentkitty.org/search/'+Fanhao , headers=proxy_ua)
# html2 =  urllib2.urlopen(html)
# html3 = html2.read()
# print html2

# proxy_txt = open('FanHao.html','w')
# proxy_table = re.compile('(?isu)<table id="archiveResult">(.*?)</table>')
# proxy_tr = re.compile("(?isu)<tr>(.*?)</tr>")
# proxy_td = re.compile("(?isu)<td[^>]*>(.*?)</td>")
# #UA模拟
# proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
# #Request连接网页
# proxy_url = urllib2.Request(url='http://www.torrentkitty.org/search/'+Fanhao ,headers=proxy_ua)
# #写入代理并检测是否成功
# try:
#     GetProxy = urllib2.urlopen(proxy_url)
#     HtmlRead = GetProxy.read()
# #如果错误
# except Exception:
#     print '-'*50
#     print '采集代理错误，请检查您的网络是否正常！'
#     print '-'*50
#     raw_input('按回车结束程序:')
# #没有错误继续执行
# else:
#     #遍历所有网页找到规则并读取
#     for table in proxy_table.findall(HtmlRead):
#         for tr in proxy_tr.findall(table):
#             for td in proxy_td.findall(tr):
#             #输出信息
#                 print td
#             print
#                 #proxy_txt.write(td+'\n'+'-'*10+'\n')
# proxy_txt.close()

# FanHao_style = open('FanHao.html','w')
# FanHao_NR = '<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">'+'\n'+'<table class="table table-bordered">'
# FanHao_style.write(FanHao_NR)
# FanHao_style.close()
#
# FanHao_style_end = open('FanHao.html','a')
# FanHao_NR_end = '</table>'
# FanHao_style_end.write(FanHao_NR_end)
# FanHao_style_end.close()

# -*- coding: utf-8 -*-
# import os
# import webbrowser
# webbrowser.open("FanHao.html")

import os
# s = open('FanHao.html','w+')
# b = s.write()
# b.replace('cloud','ss')

# #删除指定字符
# with open('FanHao.html', 'r') as f:
#     with open('FanHao.html.new', 'w') as g:
#         for line in f.readlines():
#             if '服务器地址' not in line:
#                 g.write(line)
# shutil.move('FanHao.html.new', 'FanHao.html')
# #删除指定字符
# with open('FanHao.html', 'r') as f:
#     with open('FanHao.html.new', 'w') as g:
#         for line in f.readlines():
#             if '端口' not in line:
#                 g.write(line)
# shutil.move('FanHao.html.new', 'FanHao.html')

# import re
# TiHuan='FanHao.html'
# fp=open(TiHuan,'r')
# alllines=fp.readlines()
# fp.close()
# fp=open(TiHuan,'w')
# for eachline in alllines:
#     a=re.sub('[cloud]','s',eachline)
#     fp.writelines(a)
# fp.close()
