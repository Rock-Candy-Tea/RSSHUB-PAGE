
---
title: '🚀Jarboot 服务管理与诊断 v2.2.3 安全性升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 09:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#40485b">Jarboot 是一个强大的Java进程管理、诊断的平台，可以在线管理、监控及诊断本地和远程的Java进程。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">官方文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot</a></p> 
<p><img alt height="545" src="https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif" width="990" referrerpolicy="no-referrer"></p> 
<h1>本次修改内容</h1> 
<ul> 
 <li>spring-boot全家桶升级2.6.2版本（logback v1.2.9）</li> 
 <li>安全性增强，部分开放接口增加token认证</li> 
 <li>远程进程诊断时，增加安全认证，点击受信任后才可以诊断</li> 
 <li>日志收集系统，分布式统一集中记录</li> 
 <li>修复使用反向代理时每隔一段时间重连一次的问题</li> 
 <li>修复断开重连时有时未实时推送服务状态更新的问题</li> 
</ul> 
<h1>下载 & 使用</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub主页：<span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee主页：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">sudo</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">关于与k8s的集成使用请参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Nginx反向代理配置： <a href="https://my.oschina.net/oldapple/blog/5376806" target="_blank">使用Nginx代理Jarboot时如何配置</a></p> 
<p>与Arthas相比有何区别：<a href="https://my.oschina.net/oldapple/blog/5118457" target="_blank"><span> </span>Arthas与Jarboot的源码实现对比</a></p> 
<p>更多帮助见官方文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot/</a></p>
                                        </div>
                                      
</div>
            