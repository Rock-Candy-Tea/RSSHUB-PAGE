
---
title: '微博 API 失效后 IFTTT 同步微博到 Day One 方法'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/06/20/article/6b9e04959b554eeffae13898ac22b7a3?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sat, 19 Jun 2021 23:17:54 GMT
thumbnail: 'https://cdn.sspai.com/2021/06/20/article/6b9e04959b554eeffae13898ac22b7a3?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p style="margin-left:0px;">原先一直用 IFTTT 自动同步微博到 Day One，可以把自己日常的事情笔记方便地记录到日记中。不过 2020 年开始，微博不开放这个 API 接口了。</p><p style="margin-left:0px;">失效之后，一直没管它。最近心血来潮，到在网上搜索一番，找到了方法——<a href="http://qizongwu.com/index.php/2021/02/04/python-ifttt-webhooks-crontab-%E5%AE%9A%E6%97%B6%E6%8A%93%E5%8F%96%E5%BE%AE%E5%8D%9A%E5%88%B0-day-one/">Python + IFTTT Webhooks + Crontab 定时抓取微博到 Day One</a>。</p><p style="margin-left:0px;">分三步：</p><ul><li>用爬虫抓取自己的微博，缓存到本地 CSV 文件中。</li><li>读取本地 CSV 数据，用 Python 发给 IFTTT，IFTTT 自动发送 Day One。</li><li>创建定时任务，可以定时爬取、发送，发送完后清除本地缓存。</li></ul><h2 style="margin-left:0px;"><strong>1、下载自己微博内容</strong></h2><p style="margin-left:0px;">爬微博的代码不用自己写，<a href="https://github.com/dataabc/weibo-crawler">Github 上有现成的脚本</a>，功能很强大。把代码下载到本地，然后步骤如下：</p><p style="margin-left:0px;">1、打开 powershell，路径切换到<code>weibo-crawler</code>下。<br>2、安装依赖。前提是安装好了 python 和 pip。</p><pre class="language-python"><code>pip install -r requirements.txt</code></pre><p style="margin-left:0px;">3、修改配置文件<code>config.json</code>，<code>user_id_list</code> 改成自己微博 id。<code>since_date</code>设为 1，表示只取近 1 天的微博。<br>4、运行爬虫，如果微博的数据可以下载到本地 CSV 文件，代表成功了。</p><pre class="language-python"><code>python weibo.py
</code></pre><h2 style="margin-left:0px;"><strong>2、用 IFTTT 发送 Day One</strong></h2><h3 style="margin-left:0px;">IFTTT 网站设置</h3><p style="margin-left:0px;">在 IFTTT 网站上设置一个动作：如果接收到一个 Web 请求，就创建一篇日记。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/20/article/6b9e04959b554eeffae13898ac22b7a3?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="image-20210619162620755" data-original="https://cdn.sspai.com/2021/06/20/article/6b9e04959b554eeffae13898ac22b7a3" referrerpolicy="no-referrer"></figure><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/20/article/f639942589b14fec01174483c3b0801b?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="image-20210619162200131" data-original="https://cdn.sspai.com/2021/06/20/article/f639942589b14fec01174483c3b0801b" referrerpolicy="no-referrer"></figure><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/20/article/c68ab37bc282fce69d650fb54da01c35?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="image-20210619162104426" data-original="https://cdn.sspai.com/2021/06/20/article/c68ab37bc282fce69d650fb54da01c35" referrerpolicy="no-referrer"></figure><h3 style="margin-left:0px;">本地 Python 脚本</h3><p style="margin-left:0px;">然后在本地的<code>weibo-crawler</code>文件夹下创建一个<code>ifttt.py</code>的文件，将以下内容复制进去，注意<code>path</code>、<code>event_name</code>、<code>key</code>根据自己情况修改。</p><ul><li><code>path</code>为本地 CSV 路径。</li><li><code>event_name</code>为自己在 IFTTT 上创建的触发器名称。</li><li><code>key</code>为 WebHooks 的密钥，可在 <a href="http://www.uncoverman.com/%5BWebhooks%20works%20better%20with%20IFTTT%5D(https://ifttt.com/maker_webhooks)">IFTTT</a> 点击<code>Documentation</code>查看。</li></ul><pre class="language-python"><code>import weibo
import csv
import requests
import json
import os

class Ifttt(object):
        
    def __init__(self, path, event_name, key):
        self.path = path
        self.event_name = event_name
        self.key = key
        self.text = []
        self.image = []
        self.num = 0

    # 解析本地 CSV 文件
    def parse_post_info(self, path):
        with open(path, 'r', encoding='UTF-8') as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print("Header")
                else:
                    self.text.append(row[2])
                    self.image.append(row[4].split(",",1))
                line_count += 1
            self.num = line_count - 1

            print(self.text)
            print(self.image)
            print("Total posts: ", self.num)

# 发送给 IFTTT
    def send_notice(self):
        url = f"https://maker.ifttt.com/trigger/&#123;self.event_name&#125;/with/key/&#123;self.key&#125;"
        for num in range(0, self.num):
            payload = &#123;"value1": self.text[num], "value2": self.image[num]&#125;
            headers = &#123;"Content-Type": "application/json"&#125;
            response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
            print(payload)

def main():
    config = weibo.get_config()
    wb = weibo.Weibo(config)
    wb.start() 
    path = 'weibo/微博名/1234567.csv' # 爬虫爬下来的csv路径
    event_name = 'DayOne' # Webhooks 触发器名字
    key = 'IF17vD4nqU6wO' # Webhooks 的 key，每个人不同
    ifttt = Ifttt(path, event_name, key)
    ifttt.parse_post_info(path)
    ifttt.send_notice()
    os.remove(path) 
    
if __name__ == '__main__':
    main()</code></pre><h2 style="margin-left:0px;"><strong>3、Win10 每日定时任务创建</strong></h2><p style="margin-left:0px;">前两步完成后，功能已经实现，然后每次需要手工触发显然太麻烦了，于是决定用 Win10 定时任务每天自动跑一遍，把微博下到本地 CSV 为保护，发送给 Day One，然后清除本地 CSV 文件。</p><p style="margin-left:0px;">定时任务设置方法如下：</p><p style="margin-left:0px;">在电脑-管理-系统工具-任务计划程序库-Miscrosoft 下右键，创建基本任务，设置定时任务名称、触发时间、触发频率、触发程序、触发程序代码及触发程序代码所在路径。<strong>注，触发程序代码所在路径不能不写，否则运行时不能自动删除上一次生成的 CSV。</strong></p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/20/article/95d4406af8dc597eab0a1372c987b905?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="image-20210619160457206" data-original="https://cdn.sspai.com/2021/06/20/article/95d4406af8dc597eab0a1372c987b905" referrerpolicy="no-referrer"></figure><p style="margin-left:0px;">参考 <a href="https://www.jianshu.com/p/43676346b0be">Win10 定时任务自动运行python程序</a></p><blockquote><p style="margin-left:0px;">说明：本文同步发表于<a href="http://www.uncoverman.com/from-sina-weibo-to-day-one-with-ifttt-webhooks-by-python.html" target="_blank">个人博客</a>。</p></blockquote></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2981" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E5%BE%AE%E5%8D%9A%20API%20%E5%A4%B1%E6%95%88%E5%90%8E%20IFTTT%20%E5%90%8C%E6%AD%A5%E5%BE%AE%E5%8D%9A%E5%88%B0%20Day%20One%20%E6%96%B9%E6%B3%95%E3%80%91%E5%8E%9F%E5%85%88%E4%B8%80%E7%9B%B4%E7%94%A8IFTTT%E8%87%AA%E5%8A%A8%E5%90%8C%E6%AD%A5%E5%BE%AE%E5%8D%9A%E5%88%B0DayOne%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%8A%8A%E8%87%AA%E5%B7%B1%E6%97%A5%E5%B8%B8%E7%9A%84%E4%BA%8B%E6%83%85%E7%AC%94%E8%AE%B0%E6%96%B9%E4%BE%BF%E5%9C%B0%E8%AE%B0%E5%BD%95%E5%88%B0%E6%97%A5%E8%AE%B0%E4%B8%AD%E3%80%82%E4%B8%8D%E8%BF%872020%E5%B9%B4%E5%BC%80%E5%A7%8B%EF%BC%8C%E5%BE%AE%E5%8D%9A%E4%B8%8D%E5%BC%80%E6%94%BE%E8%BF%99%E4%B8%AAAPI%E6%8E%A5%E5%8F%A3%E4%BA%86%E3%80%82%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F06%2F20%2F27eef7b3c439bb53d1cee5d8e926cdd8.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-6151" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E5%BE%AE%E5%8D%9A%20API%20%E5%A4%B1%E6%95%88%E5%90%8E%20IFTTT%20%E5%90%8C%E6%AD%A5%E5%BE%AE%E5%8D%9A%E5%88%B0%20Day%20One%20%E6%96%B9%E6%B3%95%E3%80%91%E5%8E%9F%E5%85%88%E4%B8%80%E7%9B%B4%E7%94%A8IFTTT%E8%87%AA%E5%8A%A8%E5%90%8C%E6%AD%A5%E5%BE%AE%E5%8D%9A%E5%88%B0DayOne%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%8A%8A%E8%87%AA%E5%B7%B1%E6%97%A5%E5%B8%B8%E7%9A%84%E4%BA%8B%E6%83%85%E7%AC%94%E8%AE%B0%E6%96%B9%E4%BE%BF%E5%9C%B0%E8%AE%B0%E5%BD%95%E5%88%B0%E6%97%A5%E8%AE%B0%E4%B8%AD%E3%80%82%E4%B8%8D%E8%BF%872020%E5%B9%B4%E5%BC%80%E5%A7%8B%EF%BC%8C%E5%BE%AE%E5%8D%9A%E4%B8%8D%E5%BC%80%E6%94%BE%E8%BF%99%E4%B8%AAAPI%E6%8E%A5%E5%8F%A3%E4%BA%86%E3%80%82%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            