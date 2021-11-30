
---
title: 'Java 进程启停及诊断 Jarboot v2.2.0 新增导入导出功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 10:38:00 GMT
thumbnail: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v2.2.0版本，服务管理增加了导入、导出的功能，方便系统间迁移，也可用于备份。</p> 
<p><span style="background-color:#ffffff; color:#40485b">Jarboot 是一个集Java进程管理、诊断的平台，可以在线启停、守护、监控及诊断一系列的Java进程。</span></p> 
<ul> 
 <li>🌈 浏览器界面管理，一键启、停服务进程，不必挨个手动执行</li> 
 <li>🔥 支持启动、停止优先级配置，配置依赖启动，默认并行启动</li> 
 <li>⭐️ 支持进程守护，开启后若服务异常退出则自动启动并通知</li> 
 <li>☀️ 支持文件更新监控，开启后若服务目录的文件更新则自动重启</li> 
 <li>🚀 调试命令执行，同时远程诊断多个Java进程，界面更友好</li> 
 <li>💎 支持通过<code>SPI</code>自定义调试命令实现，支持开发插件</li> 
</ul> 
<p><img alt height="466" src="https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png" width="900" referrerpolicy="no-referrer"></p> 
<p>如上图，增加了导出、导入两个工具栏按钮。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可通过Gitee和GitHub下载最新的安装包，使用Docker的请更新下Jarboot的Docker镜像。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Gitee:<span> </span><a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">sudo</span> <span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用Docker时建议将<span><strong>/jarboot/services</strong>和<strong>/jarboot/logs</strong>挂载宿主机</span></p> 
<h2>问题修改及优化</h2> 
<ul> 
 <li>修复cat命令读取xml、html文件时没有显示真实内容的问题</li> 
 <li>服务管理，树显示时默认显示第一个节点的第一个孩子</li> 
</ul> 
<h4>新特性</h4> 
<ul> 
 <li>服务管理，增加导入、导出功能</li> 
 <li>上传服务文件开始前，提示是否备份，若备份则导出当前的服务文件夹快照</li> 
</ul>
                                        </div>
                                      
</div>
            