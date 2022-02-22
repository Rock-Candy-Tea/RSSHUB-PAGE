
---
title: 'svnWebUI 1.4.0 发布，搭建 SVN 服务器的神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1370'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 02:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1370'
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
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">演示地址: http://svn.nginxwebui.cn:6060</span></span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">用户名: admin</span></span></span></span></span></span>
<span><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a"><span style="color:#22863a">密码: admin</span></span></span></span></span></span></pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">技术说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目是基于solon的java项目, 数据库使用h2, 因此服务器上不需要安装任何数据库, 同时也兼容使用mysql</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本地运行本软件，请先安装Subversion，并使用svn:\\协议进行checkout。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用docker版则无需安装任何其他软件，使用http:\\协议进行checkout。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">以Ubuntu操作系统为例,</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装java运行环境和Subversion</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>apt update</span>
<span>apt install openjdk-11-jdk</span>
<span>apt install subversion</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Centos:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>yum install java-11-openjdk</span>
<span>yum install subversion</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>下载JDK安装包 https://www.oracle.com/java/technologies/downloads/</span>
<span>下载VisualSVN https://www.visualsvn.com/server/download</span>
<span>配置JAVA运行环境 </span>
<span>JAVA_HOME : JDK安装目录</span>
<span>Path : JDK安装目录\bin</span>
<span>重启电脑</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.下载最新版发行包jar</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Linux: wget -O /home/svnWebUI/svnWebUI.jar http://file.nginxwebui.cn/svnWebUI-1.4.0.jar</span>

<span>Windows: 直接使用浏览器下载 http://file.nginxwebui.cn/svnWebUI-1.4.0.jar</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">有新版本只需要修改路径中的版本即可</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Linux: nohup java -jar -Dfile.encoding=UTF-8 /home/svnWebUI/svnWebUI.jar --server.port=6060 > /dev/null &</span>

<span>Windows: java -jar -Dfile.encoding=UTF-8 D:/home/svnWebUI/svnWebUI.jar --server.port=6060</span></pre> 
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
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意命令最后加一个&号, 表示项目后台运行</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86/x86_64/arm64 平台，同时包含subversion apache2和svnWebUI在内, 与jar版不同的是docker版支持使用http协议访问svn</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装docker容器环境</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>apt install docker.io</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Centos:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>yum install docker</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.拉取镜像:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>docker pull cym1102/svnwebui:latest</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动容器:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>docker run -itd -v /home/svnWebUI:/home/svnWebUI --privileged=true -p 6060:6060 -p 3690:3690 cym1102/svnwebui:latest</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意:</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">需要映射6060端口与3690端口, 6060为web网页端口, 3690为svn默认端口.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">容器需要映射路径/home/svnWebUI:/home/svnWebUI, 此路径下存放项目所有数据文件, 包括数据库, 配置文件, 日志等, 升级镜像时, 此目录可保证项目数据不丢失. 请注意备份.</p> </li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">本次更新说明</h4> 
<p>1.  docker版支持使用http协议checkout代码</p> 
<p>2. 修复一些bug</p>
                                        </div>
                                      
</div>
            