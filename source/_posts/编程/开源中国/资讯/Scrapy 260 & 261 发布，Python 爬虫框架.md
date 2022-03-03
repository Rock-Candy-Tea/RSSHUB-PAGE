
---
title: 'Scrapy 2.6.0 & 2.6.1 发布，Python 爬虫框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5298'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5298'
---

<div>   
<div class="content">
                                                                                            <p>Scrapy 是一套基于 Twisted 的异步处理框架，纯 Python 实现的爬虫框架，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片。它也可以用于广泛的目的，从数据挖掘、监控到自动测试等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>v2.6.0 更新内容如下：</strong></p> 
<ul> 
 <li><strong>cookie handling 的安全修复</strong>（详见下文）</li> 
 <li>Python 3.10 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scrapy.org%2Fen%2Flatest%2Ftopics%2Fasyncio.html" target="_blank">asyncio 支持</a>不再被认为是实验性的，并且无论你的 Python 版本如何，都可以在 Windows 上开箱即用</li> 
 <li>Feed 导出现在支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpathlib.html%23pathlib.Path" target="_blank"><code>pathlib.Path</code></a>输出路径和每个 Feed 项目过滤和后处理</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scrapy.org%2Fen%2Flatest%2Fnews.html%23scrapy-2-6-0-2022-03-01" target="_blank">查看完整的变更日志</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>安全漏洞修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li> <p><span>当一个定义了 cookie 的请求对象得到一个重定向响应，导致一个新的请求对象被安排，原请求对象中定义的 cookie 不再被复制到新的请求对象中。</span></p> <p><span>如果你在一个请求对象上手动设置了 Cookie header，并且重定向 URL 的域名与原始请求对象的 URL 的域名不完全匹配，那么你的 Cookie header 现在会从新的请求对象中删除。</span></p> <p><span>攻击者可以利用旧行为来访问你的 cookie。参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscrapy%2Fscrapy%2Fsecurity%2Fadvisories%2FGHSA-cjvr-mfj7-j4j8" target="_blank">cjvr-mfj7-j4j8 安全公告</a>了解更多信息。</span></p> <p><span><strong>注意：</strong>在定义你的 cookie 时，仍然可以通过定义共享域的后缀（例如 example.com 和任何子域）作为 cookie 域，使不同域之间共享 cookie。更多信息参见</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scrapy.org%2Fen%2Flatest%2Ftopics%2Frequest-response.html%23scrapy.http.Request" target="_blank"><code>Request</code></a><span>类的文档。</span></p> </li> 
 <li> <p><span>当在响应的 Set-Cookie header 中收到的或在 Request 对象中定义的 cookie 的域被设置为公共后缀 <https://publicsuffix.org/>_ 时，除非 cookie 域与请求域相同，否则 cookie 现在被忽略。</span></p> <p><span>攻击者可以利用旧行为将受控域中的 cookie 注入到你的 cookiejar 中，该 cookiejar 可能会发送到不受攻击者控制的其他域。参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscrapy%2Fscrapy%2Fsecurity%2Fadvisories%2FGHSA-mfjm-vh54-3f96" target="_blank">mfjm-vh54-3f96 安全公告</a>了解更多信息。</span></p> </li> 
</ul> 
<p><strong> v2.6.1 更新内容如下：</strong></p> 
<ul> 
 <li>修复了2.6.0版本中引入的回归问题，该问题会在跟随重定向时取消设置请求方法。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscrapy%2Fscrapy%2Freleases" target="_blank">https://github.com/scrapy/scrapy/releases</a></p>
                                        </div>
                                      
</div>
            