
---
title: 'svnWebUI 1.0.5 发布，搭建 svn 服务器的神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4095'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 09:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4095'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0; margin-right:0; text-align:left">功能说明</h4> 
<p><span style="background-color:#ffffff; color:#40485b">svnWebUI是一款图形化管理服务端Subversion的配置得工具, 虽说现在已进入git的时代, 但svn依然有不少使用场景, 比如公司内的文档管理与共享, svn的概念比git的少很多, 非常适合非程序员使用.</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">但众所周知svn的Linux服务端软件即Subversion的用户和权限配置全部依靠手写配置文件完成, 非常繁琐且不便, 已有的几款图像界面软件已经非常古老, 安装麻烦而且依赖环境非常古老, 比如csvn还使用python2作为运行环境.</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows上倒是有不错的svn服务端软件即VisualSVN, 但一来Windows服务器少之又少, 第二VisualSVN没有web界面, 每次配置需要开启远程桌面, 安全性不高.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">经历几次失败的图形界面配置后, 萌生了写一个现代svn服务端管理软件, 让svn的服务端管理有gitea的轻松体验的想法.</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#22863a">演示地址: http://svn.nginxwebui.cn:6060</span></span>
<span><span style="color:#22863a">用户名: admin</span></span>
<span><span style="color:#22863a">密码: admin</span></span></pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装java运行环境和Subversion</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">update</span></span>
<span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">install openjdk-11-jdk</span></span>
<span><span style="color:#6f42c1">apt</span> <span style="color:#032f62">install subversion</span></span>
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
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#005cc5">Linux</span>: wget -O /home/svnWebUI/svnWebUI.jar <span style="color:#005cc5">http</span>:<span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.0.5.jar</span></span>
<span><span style="color:#005cc5">Windows</span>: 直接使用浏览器下载 <span style="color:#005cc5">http</span>:<span style="color:#6a737d">//file.nginxwebui.cn/svnWebUI-1.0.5.jar</span></span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>Linux: nohup java -jar -Xmx64m /home/svnWebUI/svnWebUI.jar --server.port=<span>6060</span> --project.home=<span>/home/</span>svnWebUI/ > <span>/dev/</span><span style="color:#005cc5">null</span> &</span>
<span>Windows: java -jar -Xmx64m D:<span>/home/</span>svnWebUI/svnWebUI.jar --server.port=<span>6060</span> --project.home=D:<span>/home/</span>svnWebUI/</span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">参数说明(都是非必填)</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">-Xmx64m 最大分配内存数</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 默认以6060端口启动</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--project.home 项目配置文件目录，存放数据库文件，证书文件，日志等, 默认为/home/nginxWebUI/</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意命令最后加一个&号, 表示项目后台运行</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86_64/arm64/arm v7 平台，同时包含Subversion和svnWebUI在内, 一体化管理与运行Subversion.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">拉取镜像:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6f42c1">docker</span> <span style="color:#032f62">pull cym1102/svnwebui:latest</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">启动容器:</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><span>docker run -itd -v /home/svnWebUI:<span>/home/</span>svnWebUI -e BOOT_OPTIONS=<span style="color:#032f62">"--server.port=6060"</span> --privileged=<span style="color:#005cc5">true</span> -p <span>6060</span>:<span>6060</span> -p <span>3690</span>:<span>3690</span> cym1102/svnwebui:latest</span></pre> 
  <p> </p> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1<span style="color:#000000">. </span><a href="https://gitee.com/cym1102/svnWebUI/issues/I4LL9V"><span style="color:#000000">添加直接在网页查询svn文件列表的功能</span></a></p> 
<p>2. 添加导入导出仓库和导入用户配置文件的功能, 方便老svn系统迁移</p> 
<p>3. 增强系统登录安全性</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">下一步开发计划</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">1. 可以配置用户权限到某个目录上, 这个是svn比git强的地方, 更高级的权限管理, 必须要支持</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> </p> 
<p><span style="color:#000000">2. </span><a href="https://gitee.com/cym1102/svnWebUI/issues/I4LUJY"><span style="color:#000000">普通用户可以登录, 查看自己的项目和修改密</span></a><span style="color:#000000">码, 尽量贴近gitea的用户体验</span></p>
                                        </div>
                                      
</div>
            