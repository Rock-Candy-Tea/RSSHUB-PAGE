
---
title: '🚀Jarboot 服务管理与诊断 v2.3.1 新增客户端API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=358'
author: 开源中国
comments: false
date: Wed, 09 Feb 2022 10:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=358'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">Jarboot 是一个强大的Java进程管理、诊断的平台，可以在线管理、监控及诊断本地和远程的Java进程。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">官方文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot</a></p> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">2.3.1 (2, 2022)</h2> 
<ul> 
 <li>命令执行通讯协议改为二进制传输</li> 
 <li>使用新开发的事件框架重构后端消息流</li> 
 <li>sonar lint和pmd修改</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新特性</h4> 
<ul> 
 <li>增加针对开发者的API的client模块实现</li> 
 <li>增加std输出重定向到文件的支持，使用VM参数jarboot.stdout.file和jarboot.stdout.file.always指定文件</li> 
 <li>Linux或macOS中使用nohup启动服务</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">下载 & 使用</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub主页：<span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee主页：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">sudo</span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></span></span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">关于与k8s的集成使用请参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Nginx反向代理配置： <a href="https://my.oschina.net/oldapple/blog/5376806" target="_blank">使用Nginx代理Jarboot时如何配置</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">与Arthas相比有何区别：<a href="https://my.oschina.net/oldapple/blog/5118457" target="_blank"><span> </span>Arthas与Jarboot的源码实现对比</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多帮助见官方文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot/</a></p>
                                        </div>
                                      
</div>
            