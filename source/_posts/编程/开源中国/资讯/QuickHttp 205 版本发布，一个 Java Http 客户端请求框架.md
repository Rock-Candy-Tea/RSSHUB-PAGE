
---
title: 'QuickHttp 2.0.5 版本发布，一个 Java Http 客户端请求框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8418'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 14:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8418'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次更新内容如下:</p> 
<p>[新增]支持EventSource请求</p> 
<p>[优化]解决http状态码错误时无法获取body输入流问题</p> 
<p>[优化]修复日志功能请求头部无法显示完全问题。在debug级别下可显示http完整请求报文</p> 
<p>[优化]依赖升级,fastjson升级至1.2.75版本</p> 
<h1>QuickHttp简介</h1> 
<p style="text-align:left">QuickHttp是一个Java Http客户端框架,基于Java原生的HttpUrlConnection开发,设计了大量API方便开发者使用.QuickHttp的主要特点如下:</p> 
<h1 style="text-align:left">丰富的API设计</h1> 
<p style="text-align:left">QuickHttp参考了Jsoup的API设计,同时添加了许多新的API.QuickHttp的Request接口定义了添加请求信息的方法,例如header,userAgent,requestBody等方法.Response接口定义获取返回结果的方法,例如body,bodyAsFile,bodyAsJSONObject等方法.</p> 
<h1 style="text-align:left">Cookie管理,全局代理和日志记录</h1> 
<p style="text-align:left">QuickHttp支持Cookie管理,自动提取Cookie信息和发送Cookie.支持设置全局代理.为了解决http请求调试困难问题,QuickHttp支持直接打印Http报文日志.不仅如此,在生产环境,QuickHttp支持通过监听文件来动态设置http代理.(详见文档)</p> 
<h1 style="text-align:left">异步请求</h1> 
<p style="text-align:left">QuickHttp支持异步请求,调用enqueue方法可以在安卓开发环境下使用,不会阻塞当前线程.</p> 
<h1 style="text-align:left">监听事件支持</h1> 
<p style="text-align:left">QuickHttp支持在请求发送前后监听事件,设置连接属性等等.</p> 
<p style="text-align:left"><br> 如果您是一名爬虫开发工程师,QuickHttp能够有效提升您的开发效率,把更多的精力用于业务开发.</p> 
<p style="text-align:left"><br> QuickHttp文档:  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickhttp.schoolwow.cn" target="_blank">https://quickhttp.schoolwow.cn</a></p> 
<p style="text-align:left">QuickHttp的github地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsunyue1380%2FQuickHttp2" target="_blank">https://github.com/sunyue1380/QuickHttp2</a></p> 
<p style="text-align:left">QuickHttp的gitee地址: <a href="https://gitee.com/648823596/QuickHttp2">https://gitee.com/648823596/QuickHttp2</a></p>
                                        </div>
                                      
</div>
            