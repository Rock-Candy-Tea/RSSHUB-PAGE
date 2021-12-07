
---
title: 'svnWebUI v1.0.2 发布, 图形化搭建 svn 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 11:16:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Subversion的web管理界面, 搭建svn服务器的神器.</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">功能说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">svnWebUI是一款图形化管理Subversion的配置得工具, 虽说现在已进入git的时代, 但svn依然有不少使用场景, 比如公司内的文档管理与共享, svn的概念比git的少很多, 非常适合非程序员使用.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">但众所周知svn的Linux服务端软件即Subversion的用户和权限配置全部依靠手写配置文件完成, 非常繁琐且不便, 已有的几款图像界面软件要不已经非常古老, 要不安装麻烦而且依赖环境非常复杂, 比如csvn还在使用python2作为运行环境.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows上倒是有不错的svn服务端软件即VisualSVN, 但一来Windows服务器少之又少, 第二VisualSVN没有web界面, 每次配置需要开启远程桌面, 安全性不高.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">经历几次失败的图形界面配置后, 萌生了写一个现代svn服务端管理软件, 让svn的服务端管理有gitea般的轻松体验.</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">技术说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目是基于springBoot的web系统, 数据库使用sqlite, 因此服务器上不需要安装任何数据库</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">项目启动时会释放一个.sqlite.db到系统用户文件夹中, 注意进行备份</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用本软件前请先安装Subversion</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>演示地址: http://svn.nginxwebui.cn:6060</span>
<span>用户名: admin</span>
<span>密码: admin</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
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
  <pre><span>Linux: wget -O /home/svnWebUI/svnWebUI.jar http://file.nginxwebui.cn/svnWebUI-1.0.2.jar</span>

<span>Windows: 直接使用浏览器下载 http://file.nginxwebui.cn/svnWebUI-1.0.2.jar</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">有新版本只需要修改路径中的版本即可</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Linux: nohup java -jar -Xmx64m /home/svnWebUI/svnWebUI.jar --server.port=6060 --project.home=/home/svnWebUI/ > /dev/null &</span>

<span>Windows: java -jar -Xmx64m D:/home/svnWebUI/svnWebUI.jar --server.port=6060 --project.home=D:/home/svnWebUI/</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">参数说明(都是非必填)</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">-Xmx64m 最大分配内存数</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 默认以6060端口启动</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--project.home 项目配置文件目录，存放数据库文件，证书文件，日志等, 默认为/home/nginxWebUI/</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意命令最后加一个&号, 表示项目后台运行</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86_64/arm64/arm v7 平台，同时包含Subversion和svnWebUI在内, 一体化管理与运行Subversion.</p> 
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
  <pre><span>docker run -itd -v /home/svnWebUI:/home/svnWebUI -e BOOT_OPTIONS="--server.port=6060" --privileged=true -p 6060:6060 -p 3690:3690 cym1102/svnwebui:latest</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意:</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">需要映射6060端口与3690端口, 6060为web网页端口, 3690为svn默认端口.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">容器需要映射路径/home/svnWebUI:/home/svnWebUI, 此路径下存放项目所有数据文件, 包括数据库, 配置文件, 日志等, 升级镜像时, 此目录可保证项目数据不丢失. 请注意备份.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">-e BOOT_OPTIONS 参数可填充java启动参数, 可以靠此项参数修改端口号</p> </li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 不填默认以6060端口启动</p> 
<ol start="4"> 
 <li>日志默认存放在/home/svnWebUI/log/svnWebUI.log</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">编译说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用maven编译打包</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>mvn clean package</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用docker构建镜像</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>docker build -t svnwebui:latest .</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">添加开机启动</h4> 
<ol> 
 <li>编辑service配置</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span>vim /etc/systemd/system/svnwebui.service</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><span>[Unit]</span>
<span>Description=SvnWebUI</span>
<span>After=syslog.target</span>
<span>After=network.target</span>
<span> </span>
<span>[Service]</span>
<span>Type=simple</span>
<span>User=root</span>
<span>Group=root</span>
<span>WorkingDirectory=/home/svnWebUI</span>
<span>ExecStart=/usr/bin/java -jar /home/svnWebUI/svnWebUI.jar</span>
<span>Restart=always</span>
<span> </span>
<span>[Install]</span>
<span>WantedBy=multi-user.target</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">之后执行</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>systemctl daemon-reload</span>
<span>systemctl enable svnwebui.service</span>
<span>systemctl start svnwebui.service</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">打开<span> </span><a href="https://gitee.com/link?target=http%3A%2F%2Fip%3A6060">http://ip:6060</a><span> </span>进入主页</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">首次打开页面, 需要注册管理员账户</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注册完毕后, 进入登录页面进行登录</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E6%9C%8D%E5%8A%A1%E7%AE%A1%E7%90%86.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">服务管理, 可在这个页面查看Subversion服务的开启情况, 并进行停止和重启.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E4%BB%93%E5%BA%93%E7%AE%A1%E7%90%86.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">仓库管理, 可添加仓库及修改仓库, 添加仓库后即可获得仓库的svn地址, 十分方便</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E7%94%A8%E6%88%B7%E6%8E%88%E6%9D%83.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">选择对应的用户对仓库进行授权</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E5%B0%8F%E7%BB%84%E6%8E%88%E6%9D%83.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">选择对应的小组对仓库进行授权</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">用户管理, 可添加和编辑用户</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://cors.zfour.workers.dev/?http://www.nginxwebui.cn/img/svn/%E5%88%86%E7%BB%84%E7%AE%A1%E7%90%86.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">小组管理, 可添加和编辑小组</p> 
<p> </p>
                                        </div>
                                      
</div>
            