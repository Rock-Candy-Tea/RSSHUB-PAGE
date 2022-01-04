
---
title: '🚀Jarboot 服务管理与诊断 v2.2.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-68608dc556f2ffe9c8ddca3f10d607efe62.gif'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 02:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-68608dc556f2ffe9c8ddca3f10d607efe62.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">Jarboot 是一个强大的Java进程管理、诊断的平台，可以在线管理、监控及诊断本地和远程的Java进程。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">官方文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot</a></p> 
<p><img height="660" src="https://oscimg.oschina.net/oscnet/up-68608dc556f2ffe9c8ddca3f10d607efe62.gif" width="1210" referrerpolicy="no-referrer"></p> 
<h1>修改内容：</h1> 
<ul> 
 <li>修复spring.bean命令构建错误问题</li> 
 <li>修复偶尔出现的重复启动的问题</li> 
 <li>修复detach远程进程时仍然弹出是否信任的问题</li> 
 <li>修复在线诊断，引入spring-boot-starter-jarboot后无法执行spring扩展命令的问题</li> 
 <li>修复服务管理搜索名字显示异常的问题</li> 
 <li>修复偶尔会出现的线程池忙碌问题</li> 
 <li>远程进程detach时增加确认提示</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新特性:</h4> 
<ul> 
 <li>设置界面增加子菜单，信任服务器增删和查看界面</li> 
 <li>Console支持是否自动换行、是否自动滚动到底部</li> 
 <li>移除列表显示模式</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">下载 & 使用</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub主页：<span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee主页：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">sudo</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">关于与k8s的集成使用请参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Nginx反向代理配置： <a href="https://my.oschina.net/oldapple/blog/5376806" target="_blank">使用Nginx代理Jarboot时如何配置</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">与Arthas相比有何区别：<a href="https://my.oschina.net/oldapple/blog/5118457" target="_blank"><span> </span>Arthas与Jarboot的源码实现对比</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多帮助见官方文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2F" target="_blank">www.yuque.com/jarboot/</a></p>
                                        </div>
                                      
</div>
            