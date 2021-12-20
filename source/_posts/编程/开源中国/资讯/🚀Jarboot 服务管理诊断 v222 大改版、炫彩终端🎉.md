
---
title: '🚀Jarboot 服务管理诊断 v2.2.2 大改版、炫彩终端🎉'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 10:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#40485b">🔥</span>更新了重磅功能，终端ANSI标准支持，日志高亮，炫彩终端来袭，快来见识下彩虹<span style="background-color:#ffffff; color:#40485b">🌈</span>进度条吧！</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">另外改进了在线诊断界面，分组展示，按服务IP地址分组；增加了jt脚本，可以快捷的使用脚本Attach进程、启动进程并连接到指定服务器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub主页：<span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a> 觉得不错的可以Star⭐️支持</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee主页：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1">sudo</span></span> <span style="color:#032f62"><span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">关于与k8s的集成使用请参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a> 和 <a href="https://my.oschina.net/oldapple/blog/5195501">Jarboot容器镜像使用及Dockerfile分享</a></p> 
<p><img height="743" src="https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif" width="1349" referrerpolicy="no-referrer"></p> 
<p>在线诊断按服务器分组展示</p> 
<p><img alt height="477" src="https://gitee.com/majz0908/jarboot/raw/develop/doc/online-diagnose.png" width="980" referrerpolicy="no-referrer"></p> 
<p>jt脚本使用</p> 
<p><img height="436" src="https://oscimg.oschina.net/oscnet/up-4c8745ba442ebd9fb74537d9c4f9884c4c8.jpg" width="735" referrerpolicy="no-referrer"></p> 
<h2>详细更新内容</h2> 
<ul> 
 <li>fix:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot%2Fissues%2F29" target="_blank">#29</a><span> </span>jarboot用nginx发布后，首页加载js和css错误无法打开页面。<br> 注意：Nginx除了普通HTTP外，还需要配置Websocket代理</li> 
 <li>安装目录全路径中存在空白字符时报错并退出</li> 
 <li>服务管理排除含有空白字符的名称</li> 
 <li>后端代码性能优化，可读性优化，增加注释</li> 
</ul> 
<h4 style="text-align:start">新特性</h4> 
<ul> 
 <li>增加jt.sh、jt.cmd脚本，可以快捷的Attach和启动Java进程</li> 
 <li>终端ANSI标准支持——炫彩终端</li> 
 <li>新增隐藏命令shutdown/close，可用与断开诊断进程并重置增强类以及清理资源</li> 
 <li>服务管理双击行时启动服务</li> 
 <li>在线调试更名为在线诊断</li> 
 <li>在线诊断界面改版，不同服务器的进程分组显示</li> 
 <li>在线诊断本地进程双击行时Attach对应的进程</li> 
</ul>
                                        </div>
                                      
</div>
            