
---
title: '解决https接口无法访问的问题 (blog.darkmi.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9831'
author: 技术头条
comments: false
date: 2022-08-01 13:37:22
thumbnail: 'https://picsum.photos/400/300?random=9831'
---

<div>   
最近为我司系统接入某第三方服务，假设该第三方服务为W系统，使用https协议对外提供接口，访问W系统接口的时候，收到如下错误：
org.springframework.web.client.ResourceAccessException: I/O error on GET request for "https://open.wwww.com/api/device/status": Received fatal alert: protocol_version; nested exception is javax.net.ssl.SSLHandshakeException: Received fatal alert: protocol_versionat org.springframework.web.client.RestTemplate.doExecute(RestTemplate.java:746)at org.springframework.web.client.RestTemplate.execute(RestTemplate.java:672)
    根据日志提示，可猜测为SSL协议版本问题造成的异常。
    
</div>
            