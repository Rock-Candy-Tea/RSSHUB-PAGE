
---
title: 'backup-x 1.0 发布，带 Web 管理界面的数据库_文件备份工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1dcbdd121044a3f9f89c71219f0c1e5efaa.png'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 14:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1dcbdd121044a3f9f89c71219f0c1e5efaa.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">带Web界面的数据库/文件备份增强工具。原理：执行自定义shell命令输出文件，增强备份功能。同时支持: 文件、mysql、postgres...</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">从 backup-db 发展而来，发现不仅仅支持数据库备份，所以改名 backup-x</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">项目地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeessy2%2Fbackup-x" target="_blank">https://github.com/jeessy2/backup-x</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>v1.0全新升级：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span> </span>支持自定义命令</li> 
 <li><span> </span>支持执行shell输出的文件备份，原理上支持各种数据库/文件备份</li> 
 <li><span> </span>支持备份周期设置，几分钟到一年的备份周期也可以</li> 
 <li><span> </span>支持多个项目备份，最多16个</li> 
 <li><span> </span>支持备份后的文件另存到对象存储中 (再也不怕删库跑路了)</li> 
 <li><span> </span>可设置备份文件最大保存天数</li> 
 <li><span> </span>webhook通知</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>docker中使用（</strong>登录 http://your_docker_ip:9977 并配置<strong>）</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left">  docker run -d --name backup-x --restart=always \
    -p 9977:9977 \
    -v /opt/backup-x-files:/app/backup-x-files \
    jeessy/backup-x</pre> 
<p><strong>系统中使用</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">下载并解压<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeessy2%2Fbackup-x%2Freleases" target="_blank">https://github.com/jeessy2/backup-x/releases</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">安装服务</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>Mac/Linux:<span> </span><code>./backup-x -s install</code></li> 
   <li>Win(打开cmd):<span> </span><code>.\backup-x.exe -s install</code></li> 
   <li>自定义参数<span> </span><code>./backup-x -s install -l 127.0.0.1:9977 -d /Users/name</code> 
    <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
     <li><code>-l</code><span> </span>监听地址（默认监听<code>:9977</code>）</li> 
     <li><code>-d</code><span> </span>自定义备份目录地址（默认当前运行目录）</li> 
    </ul> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">登录<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A9977%2F" target="_blank">http://127.0.0.1:9977</a><span> </span>并配置</p> <p style="margin-left:0; margin-right:0"><img alt height="634" src="https://oscimg.oschina.net/oscnet/up-1dcbdd121044a3f9f89c71219f0c1e5efaa.png" width="1011" referrerpolicy="no-referrer"></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            