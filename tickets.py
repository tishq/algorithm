# -*- coding: utf-8 -*-
"""
@author: ppy2790
"""
import sys
from time import sleep

from splinter.browser import Browser

from selenium.webdriver.chrome.options import Options
# 这些设置都是必要的
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--enable-extensions")
# chrome_options.add_argument("--enable-user-scripts ")
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--dns - prefetch - disable")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-javascript")
chrome_options.add_argument("--disable-plugins")

chrome_options.add_argument("--allow-outdated-plugins")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--allow-scripting-gallery ")


chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-remote-fonts ")
chrome_options.add_argument("--allow-outdated-plugins")


#--disable-remote-fonts
#--allow-outdated-plugins
"""
#|1 |--allow-outdated-plugins | 不停用过期的插件。| |2 |--allow-running-insecure-content | 默认情况下，https 页面不允许从 http 链接引用 javascript/css/plug-ins。添加这一参数会放行这些内容。| |3 |--allow-scripting-gallery | 允许拓展脚本在官方应用中心生效。默认情况下，出于安全因素考虑这些脚本都会被阻止。| |4 |--disable-accelerated-2d-canvas | 停用 GPU 加速二维画布。| |5 |--disable-accelerated-video | 停用 GPU 加速视频。| |6 |--disable-dart | 停用 Dart。| |7 |--disable-desktop-notifications | 禁用桌面通知，在 Windows 中桌面通知默认是启用的。| |8 |--disable-extensions | 禁用拓展。 | |9 |--disable-file-system | 停用 FileSystem API。（注意一些拓展如 Adblock Plus for Google Chrome™ 依赖此 API 运行）| |10 |--disable-java | 停用 Java。| |11 |--disable-local-storage | 禁用 LocalStorage。 | |12 |--disable-preconnect | 停用 TCP/IP 预连接。| |13 |--disable-remote-fonts | 关闭远程字体支持。SVG 中字体不受此参数影响。| |14 |--disable-speech-input | 停用语音输入。| |15 |--disable-sync | 停用同步功能。| |16 |--disable-ssl3 | 停用 SSL v3。| |17 |--disable-web-security | 不强制遵守同源策略，供网站开发人员测试站点使用。| |18 |--disk-cache-dir | 将缓存设置在给定的路径。| |19 |--disk-cache-size | 设置缓存大小上限，以字节为单位。| |20 |--dns-prefetch-disable | 停用DNS预读。| |21 |--enable-print-preview | 启用打印预览。| |22 |--extensions-update-frequency | 设定拓展自动更新频率，以秒为单位。 | |23 |--incognito | 让浏览器直接以隐身模式启动。| |24 |--keep-alive-for-test | 最后一个标签关闭后仍保持浏览器进程。（某种意义上可以提高热启动速度，不过你最好得有充足的内存）| |25 |--kiosk | 启用kiosk模式。（一种类似于全屏的浏览模式）| |26 |--lang | 使用指定的语言。| |27 |--no-displaying-insecure-content | 默认情况下，https 页面允许从 http 链接引用图片/字体/框架。添加这一参数会阻止这些内容。| |28 |--no-first-run | 跳过 Chromium 首次运行检查。| |29 |--no-referrers | 不发送 Http-Referer 头。| |30 |--no-sandbox | 彻底停用沙箱。| |31 |--no-startup-window | 启动时不建立窗口。| |32 |--proxy-pac-url | 使用给定 URL 的 pac 代理脚本。（也可以使用本地文件，如 --proxy-pac-url="file:\\c:\proxy.pac"）| |33 |--proxy-server | 使用给定的代理服务器，这个参数只对 http 和 https 有效。（例如 --proxy-server=127.0.0.1:8087 ）| |34 |--show-component-extension-options | 让自带的拓展组件显示在 chrome://settings/extensions 里。（目前有一个 "Bookmark Manager 0.1"）| |35 |--single-process | 以单进程模式运行 Chromium。（启动时浏览器会给出不安全警告）| |36 |--skip-gpu-data-loading | 跳过启动时的 GPU 信息收集、黑名单读取与黑名单自动更新，这样一来，所有的 GPU 功能都可供使用，并且 about:gpu 页面会显示空白。此参数仅供测试使用。| |37 |--start-maximized | 启动时最大化。| |38 |--touch-optimized-ui | 使用对触屏更友好的用户界面。（目前来看似乎只是把一些字体放大了）| |39 |--user-agent | 使用给定的 User-Agent 字符串。|
"""
class huoche(object):
    """docstring for huoche"""
    driver_name='chrome'
    executable_path='/usr/local/bin/chromedriver'
    #用户名，密码
    username = u"737499655@qq.com"
    passwd = u"ysdyxmhq1"
    # cookies值得自己去找, 下面两个分别是上海, 广州
    # starts = u"%u4E0A%u6D77%2CSHH"
    # ends = u"%u5E7F%u5DDE%2CGZQ"
    '''
    '宁波':'%u5B81%u6CE2%2CNGH',
    '昆明':'%u6606%u660E%2CKMM',
    '绍兴':'%u7ECD%u5174%2CSOH',
    '宣威':'%u5BA3%u5A01%2CXWM',
    '''
    ######################################################################
    #
    #####################################################################
    starts = u"%u5BA3%u5A01%2CXWM"
    #ends = u"%u5BA3%u5A01%2CXWM"
    ends = u"%u7ECD%u5174%2CSOH"

    ######################################################################
    #
    #####################################################################
    # 时间格式2018-01-19
    dtime = u"2019-02-12"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 0
    ###乘客名
    users = [u"代美连",u"孟维勇"]
    ##席位
    xb = u"二等座"
    pz=u"成人票"

    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/view/index.html"
    buy="https://kyfw.12306.cn/otn/confirmPassenger/initDc"

    def __init__(self):
        self.driver_name = 'chrome'
        #self.driver_name = 'firefox'

        self.executable_path = '/usr/local/bin/chromedriver'

    def login(self):
        #
        self.driver.visit("https://www.baidu.com")
        self.driver.visit(self.login_url)
        # 填充密码
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print
        u'等待验证码，自行输入...'
        raw_input("\n\nPress the enter key to exit.")
        #while True:
        #    if self.driver.url != self.initmy_url:
        #        sleep(1)
        #    else:
        #        break

    def start(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path,chrome_options=chrome_options)
        #self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(800, 1000)
        self.login()
        # sleep(1)
        self.driver.visit("https://www.baidu.com")
        flag = 0
        while flag == 0:
            self.driver.visit(self.ticket_url)
        # try:
            print u"购票页面开始..."
            # sleep(1)
            # 加载查询信息
            # self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            # self.driver.cookies.add({"_jc_save_toStation": self.ends})
            # self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()

            print u"出发日期"
            print self.driver.find_by_id("train_date").value
            # print u"出发日期"
            # print self.driver.find_by_id("train_date").value
            while self.driver.find_by_id("train_date").value != self.dtime:
                self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
                self.driver.reload()
                print u"出发日期"
                print self.driver.find_by_id("train_date").value

            print u"查询完毕"



            count = 0
        # if self.order != 0:
        #     while self.driver.url == self.ticket_url:
        #         self.driver.find_by_text(u"查询").click()
        #         count += 1
        #         print u"循环点击查询... 第 %s 次" % count
        #         # sleep(1)
        #         try:
        #             self.driver.find_by_text(u"预订")[self.order - 1].click()
        #         except Exception as e:
        #             print e
        #             print u"还没开始预订"
        #             continue
        # else:

            while self.driver.url == self.ticket_url:

                try:
                    self.driver.find_by_text(u"查询").click()
                except Exception as e:
                    print e
                    print u"网络超时"
                    continue

                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in self.driver.find_by_text(u"预订"):
                        i.click()
                        #sleep(0.8)
                except Exception as e:
                    print e
                    print u"还没开始预订 %s" % count
                    continue
            print u"开始预订..."

            # sleep(3)
            # self.driver.reload()
            #sleep(0.5)
            print u'开始选择用户...'
            #self.driver.find_by_text(u"孟海娇").last.click()
            self.driver.find_by_text(u"代美连").last.click()
            self.driver.find_by_text(u"孟维勇").last.click()
            # for user in self.users:
            #     print user
            #     self.driver.find_by_text(user).last.click()
            #     #sleep(0.8)

            print u"提交订单..."
            #sleep(1)
            # self.driver.find_by_text(self.pz).click()
            # self.driver.find_by_id('').select(self.pz)
            # # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            #sleep(0.8)
            self.driver.find_by_id('submitOrder_id').click()
            # print u"开始选座..."
            # self.driver.find_by_id('1D').last.click()
            # self.driver.find_by_id('1F').last.click()

            sleep(1)
            try:
                print u"确认选座..."
                self.driver.find_by_id('qr_submit_id').click()
                aa = raw_input("Enter your input: 0继续 1结束")
                flag = int(aa)
                print flag
            except Exception as e:
                print e
                print u"已被抢走，重新查询"
                continue

    #
    # except Exception as e:
    #     print e

cities= {'成都':'%u6210%u90FD%2CCDW',
'宁波':'%u5B81%u6CE2%2CNGH',
'昆明':'%u6606%u660E%2CKMM',
'绍兴':'%u7ECD%u5174%2CSOH',
'宣威':'%u5BA3%u5A01%2CXWM',
'重庆':'%u91CD%u5E86%2CCQW',
'北京':'%u5317%u4EAC%2CBJP',
'广州':'%u5E7F%u5DDE%2CGZQ',
'杭州':'%u676D%u5DDE%2CHZH',
'宜昌':'%u5B9C%u660C%2CYCN',
'郑州':'%u90D1%u5DDE%2CZZF',
'深圳':'%u6DF1%u5733%2CSZQ',
'西安':'%u897F%u5B89%2CXAY',
'大连':'%u5927%u8FDE%2CDLT',
'武汉':'%u6B66%u6C49%2CWHN',
'上海':'%u4E0A%u6D77%2CSHH',
'南京':'%u5357%u4EAC%2CNJH',
'合肥':'%u5408%u80A5%2CHFH'}

if __name__ == '__main__':
   	huoche=huoche()
	# huoche.starts=cities[sys.argv[1]]
	# huoche.ends = cities[sys.argv[2]]
	# huoche.dtime = sys.argv[3]
	huoche.start()
