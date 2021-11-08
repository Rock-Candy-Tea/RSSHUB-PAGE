
---
title: 'Java 进程管理、调试平台 Jarboot v1.1.1 发布，在线调试功能上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ee7f9869a643b80e800d7cdb36da7e5eee0.png'
author: 开源中国
comments: false
date: Mon, 08 Nov 2021 02:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ee7f9869a643b80e800d7cdb36da7e5eee0.png'
---

<div>   
<div class="content">
                                                                                            <p>推出在线调试功能，可以Attach服务器上运行的Java进程，进而通过执行命令诊断进程。</p> 
<p><span style="background-color:#ffffff; color:#222222">首先呢，分为两种进程，一种是由Jarboot启动、管理的进程，一种则是服务器中所有的非Jarboot启动的其他进程。受Jarboot管理的在运行的服务可以直接调试、诊断问题不需要手动的Attach，还可以守护、监控。未受Jarboot管理的其他进程可以Attach后调试、诊断和监控，如下图。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">GitHub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Gitee: <a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#000000">更新内容：</span></h4> 
<ul> 
 <li>修复清空Console终端时会显示loading的动态的问题</li> 
 <li><code>关于</code>界面简化更新</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">新特性:</h4> 
<ul> 
 <li>在线调试功能，可显示并Attach调试当前服务器上除自己以外的所有运行的Java进程</li> 
 <li>按钮使能，可直观的展示按钮当前是否可以使用</li> 
 <li>新增服务上传界面优化更新</li> 
 <li>服务管理增加删除工具按钮</li> 
</ul> 
<p><img alt="up-ee7f9869a643b80e800d7cdb36da7e5eee0.png" src="https://oscimg.oschina.net/oscnet/up-ee7f9869a643b80e800d7cdb36da7e5eee0.png" referrerpolicy="no-referrer"></p> 
<p>安装包下载请到<strong>GitHub</strong>，使用Docker：</p> 
<pre style="text-align:left"><span><span style="color:#0086b3">sudo </span>docker run <span style="color:#ffcc55">-itd</span> <span style="color:#ffcc55">--name</span> jarboot <span style="color:#ffcc55">-p</span> 9899:9899 mazheng0908/jarboot</span>
</pre>
                                        </div>
                                      
</div>
            