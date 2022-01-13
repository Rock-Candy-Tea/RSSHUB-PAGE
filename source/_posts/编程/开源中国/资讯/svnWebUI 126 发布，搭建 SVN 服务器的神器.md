
---
title: 'svnWebUI 1.2.6 发布，搭建 SVN 服务器的神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3702'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 10:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3702'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:left">功能说明</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">svnWebUI是一款图形化管理服务端Subversion的配置得工具, 虽说现在已进入git的时代, 但svn依然有不少使用场景, 比如公司内的文档管理与共享, svn的概念比git的少很多, 非常适合非程序员使用.</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">但众所周知svn的Linux服务端软件即Subversion的用户和权限配置全部依靠手写配置文件完成, 非常繁琐且不便, 已有的几款图像界面软件已经非常古老, 安装麻烦而且依赖环境非常古老, 比如csvn还使用python2作为运行环境.</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows上倒是有不错的svn服务端软件即VisualSVN, 但一来Windows服务器少之又少, 第二VisualSVN没有web界面, 每次配置需要开启远程桌面, 安全性不高.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">经历几次失败的图形界面配置后, 萌生了写一个现代svn服务端管理软件, 让svn的服务端管理有gitea的轻松体验的想法.</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">演示地址: http://svn.nginxwebui.cn:6060</span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">用户名: admin</span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">密码: admin</span></span></span></span></span></pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装java运行环境和Subversion</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">apt</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">update</span></span></span></span></span>
<span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">apt</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">install openjdk-11-jdk</span></span></span></span></span>
<span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">apt</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">install subversion</span></span></span></span></span>
</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">下载JDK安装包</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">https://www.oracle.com/java/technologies/downloads/</span></span></span></span></span>
<span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">下载VisualSVN</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">https://www.visualsvn.com/server/download</span></span></span></span></span>
<span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">配置JAVA运行环境</span></span></span></span> </span>
<span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">JAVA_HOME</span></span></span></span> : <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">JDK安装目录</span></span></span></span></span>
<span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">Path</span></span></span></span> : <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">JDK安装目录\bin</span></span></span></span></span>
<span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">重启电脑</span></span></span></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.下载最新版发行包jar</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">Linux</span></span></span></span>: wget -O /home/svnWebUI/svnWebUI.jar <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">http</span></span></span></span>:<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.2.6.jar</span></span></span></span></span>
<span><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">Windows</span></span></span></span>: 直接使用浏览器下载 <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">http</span></span></span></span>:<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.2.6.jar</span></span></span></span></span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>Linux: nohup java -jar /home/svnWebUI/svnWebUI.jar --server.port=<span><span><span><span>6060</span></span></span></span> --project.home=<span><span><span><span>/home/</span></span></span></span>svnWebUI/ > <span><span><span><span>/dev/</span></span></span></span><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">null</span></span></span></span> &</span>
<span>Windows: java -jar D:<span><span><span><span>/home/</span></span></span></span>svnWebUI/svnWebUI.jar --server.port=<span><span><span><span>6060</span></span></span></span> --project.home=D:<span><span><span><span>/home/</span></span></span></span>svnWebUI/</span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">参数说明</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 默认以6060端口启动</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--project.home 项目配置文件目录，存放数据库文件，证书文件，日志等, 默认为jar所在目录</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意命令最后加一个&号, 表示项目后台运行</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86_64/arm64/arm v7 平台，同时包含Subversion和svnWebUI在内, 一体化管理与运行Subversion.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">拉取镜像:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">docker</span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">pull cym1102/svnwebui:latest</span></span></span></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">启动容器:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#032f62">docker</span> <span style="color:#032f62">run</span> <span style="color:#032f62">-itd</span> <span style="color:#032f62">-v</span> <span style="color:#032f62">/home/svnWebUI:</span><span><span><span><span style="color:#032f62">/home/</span></span></span></span><span style="color:#032f62">svnWebUI</span> <span style="color:#032f62">--privileged=</span><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#032f62">true</span></span></span></span> <span style="color:#032f62">-p</span> <span><span><span><span>6060</span></span></span></span><span style="color:#032f62">:</span><span><span><span><span style="color:#032f62">6060</span></span></span></span> <span style="color:#032f62">-p</span> <span><span><span><span>3690</span></span></span></span><span style="color:#032f62">:</span><span><span><span><span style="color:#032f62">3690</span></span></span></span> <span style="color:#032f62">cym1102/svnwebui:latest</span></span></pre> 
  <p style="margin-left:0; margin-right:0"> </p> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1<span style="color:#000000">. 加强权限管理</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. 实现小组嵌套小组, 并能自动检查循环嵌套</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3. 实现<span style="background-color:#ffffff; color:#40485b">可以直接使用jar找回密码</span></p>
                                        </div>
                                      
</div>
            