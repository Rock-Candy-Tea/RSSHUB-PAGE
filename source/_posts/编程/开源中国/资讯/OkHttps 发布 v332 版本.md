
---
title: 'OkHttps 发布 v3.3.2 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2060'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 12:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2060'
---

<div>   
<div class="content">
                                                                    
                                                        <p>优化 与 BUG 修复:</p> 
<ol> 
 <li>优化:<span> </span><code>Stomp</code>，在<span> </span><code>OnError/OnException</code><span> </span>时重置<span> </span><code>connecting</code><span> </span>状态（v3.4.0 中已处理）</li> 
 <li>优化<span> </span><code>WHttoTask#setMaxClosingSecs(int)</code><span> </span>方法，使之支持链式调用（v3.4.2 中已处理）</li> 
 <li>升级 底层依赖<span> </span><code>data</code>:<span> </span><code>v1.1.1 -> v1.1.2</code>（修复了 JacksonMapper 与 JacksonArray 在 getString 时 null 返回 "null" 的问题）（v3.4.2 中已处理）</li> 
 <li>修复 在使用<span> </span><code>JDK9+</code><span> </span>的模块功能 时，JSON/XML 扩展包无法使用 SPI 完成自动配置的问题</li> 
</ol> 
<p>还在使用 v3.3 的同学可升级哦。</p> 
<p><span style="background-color:#ffffff; color:#17181a">OkHttps 是前后端通用的 HTTP 客户端，同时支持 WebSocket 与 Stomp 协议</span><br> <span style="background-color:#ffffff; color:#17181a">● 链式调用，一点到底</span><br> <span style="background-color:#ffffff; color:#17181a">● BaseURL、URL占位符、HTTP、WebSocket</span><br> <span style="background-color:#ffffff; color:#17181a">● JSON、Xml 等自动封装与解析，且支持与任意格式的数据解析框架集成</span><br> <span style="background-color:#ffffff; color:#17181a">● 同步拦截器、异步预处理器、回调执行器、全局监听、回调阻断</span><br> <span style="background-color:#ffffff; color:#17181a">● 文件上传下载（过程控制、进度监听）</span><br> <span style="background-color:#ffffff; color:#17181a">● 单方法回调，充分利用 Lambda 表达式</span><br> <span style="background-color:#ffffff; color:#17181a">● TCP连接池、Http2</span></p> 
<p><span style="background-color:#ffffff; color:#333333">https://github.com/ejlchina/okhttps</span><br> <span style="background-color:#ffffff; color:#333333">https://gitee.com/ejlchina-zhxu/okhttps</span><br> <span style="background-color:#ffffff; color:#333333">https://okhttps.ejlchina.com/</span></p> 
<p><span style="background-color:#ffffff; color:#17181a">如果觉得还不错，STAR 一下吧</span></p>
                                        </div>
                                      
</div>
            