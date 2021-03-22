
---
title: 全局使用SocketTask建立连接成功，SocketTask.onOpen不执行_
categories: 
    - 编程
    - 微信开放平台 - 微信开放社区 - 小程序问答
author: 微信开放平台 - 微信开放社区 - 小程序问答
comments: false
date: Mon, 22 Mar 2021 02:54:38 GMT
thumbnail: 'http://mmbiz.qpic.cn/mmbiz_png/JUyNqOkVQnvVhwooNnQSZBib8Eiap0KOsGyicx38QtsWHRyssh8qHeujR3euLTjKNK1uZriaqEG6GJSNzrS4V506Tg/0?wx_fmt=png'
---

<div>   
<p>我在app.js中使用SocketTask创建socket连接，创建连接成功了，但是用<span style="font-size: 16px;">SocketTask监听onOpen事件没有执行</span></p><p style="line-height: 18px; font-size: 12px; font-family: Consolas, Consolas, "Courier New", monospace; background-color: rgb(46, 46, 46); color: rgb(220, 220, 220);"><span style="font-size: 16px;">我是在app.js执行</span><span style="color: rgb(255, 165, 79);">onLaunch函数</span><span style="color: rgb(124, 205, 125);">建立websocket连接，连接建立成功后，在登陆页面使用socketTask调用方法监听socket打开事件，没有执行，socketTask打印如下：</span></p><p><img src="http://mmbiz.qpic.cn/mmbiz_png/JUyNqOkVQnvVhwooNnQSZBib8Eiap0KOsGyicx38QtsWHRyssh8qHeujR3euLTjKNK1uZriaqEG6GJSNzrS4V506Tg/0?wx_fmt=png" referrerpolicy="no-referrer"></p>  
</div>
            