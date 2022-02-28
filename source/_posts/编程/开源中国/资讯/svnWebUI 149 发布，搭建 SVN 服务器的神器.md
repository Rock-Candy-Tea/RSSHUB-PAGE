
---
title: 'svnWebUI 1.4.9 发布，搭建 SVN 服务器的神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2504'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 09:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2504'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0; margin-right:0; text-align:left">功能说明</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">svnWebUI是一款图形化管理服务端Subversion的配置得工具, 虽说现在已进入git的时代, 但svn依然有不少使用场景, 比如公司内的文档管理与共享, svn的概念比git的少很多, 非常适合非程序员使用.</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">但众所周知svn的Linux服务端软件即Subversion的用户和权限配置全部依靠手写配置文件完成, 非常繁琐且不便, 已有的几款web图像界面软件已经非常古老, 安装麻烦而且依赖环境非常古老, 比如csvn还使用python2作为运行环境.</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows上倒是有不错的svn服务端软件即VisualSVN, 但一来Windows服务器少之又少, 第二VisualSVN没有web界面, 每次配置需要开启远程桌面, 安全性不高.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">经历几次失败的图形界面配置后, 萌生了写一个现代svn服务端管理软件, 让svn的服务端管理有gitea的轻松体验的想法.</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">演示地址: http://svn.nginxwebui.cn:6060</span></span></span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">用户名: admin</span></span></span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">密码: admin</span></span></span></span></span></span></span></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:left">技术说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目是基于solon的java项目, 数据库使用h2, 因此服务器上不需要安装任何数据库, 同时也兼容使用mysql</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本地运行本软件，请先安装Subversion，并使用svn:\\协议进行checkout。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用docker版则无需安装任何其他软件，使用http:\\协议进行checkout, 以便使用nginx进行反向代理及配置https证书。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">以Ubuntu操作系统为例,</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装java运行环境和Subversion</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">update</span></span>
<span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">install openjdk-11-jdk</span></span>
<span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">install subversion</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Centos:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>yum <span style="color:#d73a49">install</span> <span style="color:#d73a49">java</span><span>-11</span>-openjdk</span>
<span>yum <span style="color:#d73a49">install</span> subversion</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6a737d">下载JDK安装包</span> <span style="color:#032f62">https://www.oracle.com/java/technologies/downloads/</span></span>
<span><span style="color:#6a737d">下载VisualSVN</span> <span style="color:#032f62">https://www.visualsvn.com/server/download</span></span>
<span><span style="color:#6a737d">配置JAVA运行环境</span> </span>
<span><span style="color:#6f42c1">JAVA_HOME</span> : <span style="color:#032f62">JDK安装目录</span></span>
<span><span style="color:#6f42c1">Path</span> : <span style="color:#032f62">JDK安装目录\bin</span></span>
<span><span style="color:#6f42c1">重启电脑</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.下载最新版发行包jar</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#005cc5">Linux</span>: wget -O /home/svnWebUI/svnWebUI.jar <span style="color:#005cc5">http</span>:<span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.4.9.jar</span></span>

<span><span style="color:#005cc5">Windows</span>: 直接使用浏览器下载 <span style="color:#005cc5">http</span>:<span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.4.9.jar</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">有新版本只需要修改路径中的版本即可</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#005cc5">Linux</span>: nohup java -jar -Dfile.encoding=UTF-8 /home/svnWebUI/svnWebUI.jar --server.port=6060 > /dev/null &</span>

<span><span><span style="color:#6f42c1">Windows</span>: <span style="color:#032f62">java -jar -Dfile.encoding=UTF-8 D:/home/svnWebUI/svnWebUI.jar --server.port=6060</span></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">参数说明(都是非必填)</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 默认以6060端口启动</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--project.home 项目配置文件目录，存放仓库文件, 数据库文件等, 默认为/home/svnWebUI/</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--database.type=mysql 使用其他数据库，不填为使用本地h2数据库</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--database.url=jdbc:mysql://ip:port/dbname 数据库url</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--database.username=root 数据库用户</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--database.password=pass 数据库密码</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86_64/arm64 平台，同时包含subversion apache2和svnWebUI在内, 与jar版不同的是docker版支持使用http协议访问svn</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装docker容器环境</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">install docker.io</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Centos:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">yum</span> <span style="color:#032f62">install docker</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.拉取镜像:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">docker</span> <span style="color:#032f62">pull cym1102/svnwebui:latest</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动容器:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#032f62">docker</span> <span style="color:#032f62">run</span> <span style="color:#032f62">-itd</span> <span style="color:#032f62">-v</span> <span style="color:#032f62">/home/svnWebUI:/home/svnWebUI</span> <span style="color:#032f62">--privileged=true</span> <span style="color:#032f62">-p</span> <span>6060</span><span style="color:#032f62">:6060</span> <span style="color:#032f62">-p</span> <span>3690</span><span style="color:#032f62">:3690</span> <span style="color:#032f62">cym1102/svnwebui:latest</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意:</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">需要映射6060端口与3690端口, 6060为web网页端口, 3690为svn默认端口.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">容器需要映射路径/home/svnWebUI:/home/svnWebUI, 此路径下存放项目所有数据文件, 包括数据库, 配置文件, 日志等, 升级镜像时, 此目录可保证项目数据不丢失. 请注意备份.</p> </li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">本次更新说明</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  仓库支持进行全体授权, 可一键直接将整个仓库授权给全体员工</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. 支持Webhook功能, 每次提交都能发送http请求, 以便CI/CD集成</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3. 员工可直接在网页上下载svn文件, 接近github体验.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4. docker底包切换为ubuntu, 内置软件版本更新, 功能更强大</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">5. 实现小组下可添加小组, 实现小组嵌套</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">6. 修复大量bug</p>
                                        </div>
                                      
</div>
            