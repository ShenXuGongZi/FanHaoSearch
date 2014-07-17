#-*- coding: utf-8 -*
#from pip.backwardcompat import raw_input
import urllib
import urllib2
import re
import shutil
import random
import webbrowser

print '#'*50
print '#'+'番号下载器'
print '#'*50
print '-'*20+'开始获取代理'+'-'*20

################################### 开始全局代理 ##############################
#采集代理信息
proxy_txt = open('proxy_list.txt','w')
proxy_tr = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
proxy_td = re.compile("(?isu)<td[^>]*>(.*?)</td>")
#UA模拟
proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
#Request连接网页
proxy_url = urllib2.Request(url='http://www.site-digger.com/html/articles/20110516/proxieslist.html',headers=proxy_ua)
#写入代理并检测是否成功
try:
    GetProxy = urllib2.urlopen(proxy_url)
    HtmlRead = GetProxy.read()
#如果错误
except Exception:
    print '-'*50
    print '采集代理错误，请检查您的网络是否正常！'
    print '-'*50
    raw_input('按回车结束程序:')
#没有错误继续执行
else:
    #遍历所有网页找到规则并读取
    for row in proxy_tr.findall(HtmlRead):
        for col in proxy_td.findall(row)[:1]:
            #代理信息写入文件
            proxy_txt.write(col+'\n')
    proxy_txt.close()

print '-'*20+'获取代理完毕'+'-'*20
################################### 采集代理结束 ##############################

################################### 开始全局代理 ##############################
# #遍历代理文件
open_proxy = open('proxy_list.txt','r')
line0 = open_proxy.readlines()
open_proxy.close()
#随即选行
proxy_line = random.choice(line0)
#进行全局代理
proxy_handler = urllib2.ProxyHandler({'http://':'%s'%proxy_line})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)
################################### 全局代理结束 ##############################

#开始主程序
print '#'*50
print '##肾虚公子制作'
print '##项目主页: FanHao.miaowu.asia'
print '#'*50
#番号名称
#FanHao = raw_input('请输入番号:')
Fanhao = raw_input('请输入番号:')

FanHao_style = open('FanHao.html','w')
FanHao_NR = '<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">'+'\n'+'<center><h3>肾虚公子番号采集器</h3><hr/><p>本软件资料来源于网络，如有异议请联系作者</p><br/><table class="table table-striped table-hover"></center>'
FanHao_style.write(FanHao_NR)
FanHao_style.close()

Fanhao_html = open('FanHao.html','a')
ZhuaQ_LJ = re.compile('(?isu)<table class="torrent_name_tbl">(.*?)</table>')
#UA模拟
proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Accept-Language:':'zh-CN,zh;q=0.8'}
#Request连接网页
proxy_url = urllib2.Request(url='https://btdigg.org/search?info_hash=&q='+Fanhao ,headers=proxy_ua)

GetProxy = urllib2.urlopen(proxy_url)
HtmlRead = GetProxy.read()
#遍历所有网页找到规则并读取
for LianJ in ZhuaQ_LJ.findall(HtmlRead):
        Fanhao_html.write(LianJ+'\n')

Fanhao_html.close()
#
FanHao_style_end = open('FanHao.html','a')
FanHao_NR_end = '</table>'
FanHao_style_end.write(FanHao_NR_end)
FanHao_style_end.close()
#设置替换函数
def tihuan(tiH,tiH2):
    TiHuan='FanHao.html'
    fp=open(TiHuan,'r')
    alllines=fp.readlines()
    fp.close()
    fp=open(TiHuan,'w')
    for eachline in alllines:
        a=re.sub(tiH,tiH2,eachline)
        fp.writelines(a)
    fp.close()

#实用替换函数替换字符
dl2 = tihuan('title="Add to BTCloud"','style="display:none;"')
dl3 = tihuan('class="attr_name"','style="display:none;"')
dl4 = tihuan('class="attr_val"','style="display:none;"')
dl5 = tihuan('magnet-link','磁力连接')

dl2
dl3
dl4
dl5

print '#'*50
print '>'*10+'番号获取成功'
print '#'*50

raw_input('按回车查看结果:')

open_url = webbrowser.open("FanHao.html")

open_url