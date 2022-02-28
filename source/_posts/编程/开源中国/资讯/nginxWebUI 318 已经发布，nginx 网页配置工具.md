
---
title: 'nginxWebUI 3.1.8 已经发布，nginx 网页配置工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5315'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 09:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5315'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0; margin-right:0; text-align:left">功能说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">nginxWebUI是一款图形化管理nginx配置得工具, 可以使用网页来快速配置nginx的各项功能, 包括http协议转发, tcp协议转发, 反向代理, 负载均衡, 静态html服务器, ssl证书自动申请、续签、配置等, 配置好后可一建生成nginx.conf文件, 同时可控制nginx使用此文件进行启动与重载, 完成对nginx的图形化控制闭环.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">nginxWebUI也可管理多个nginx服务器集群, 随时一键切换到对应服务器上进行nginx配置, 也可以一键将某台服务器配置同步到其他服务器, 方便集群管理.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">nginx本身功能复杂, nginxWebUI并不能涵盖nginx所有功能, 但能覆盖nginx日常90%的功能使用配置, 平台没有涵盖到的nginx配置项, 可以使用自定义参数模板, 在conf文件中生成配置独特的参数。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">部署此项目后, 配置nginx再也不用上网各种搜索配置代码, 再也不用手动申请和配置ssl证书, 只需要在本项目中进行增删改查就可方便的配置和启动nginx。</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#22863a">演示地址: http://test.nginxwebui.cn:8080</span></span>
<span><span style="color:#22863a">用户名: admin</span></span>
<span><span style="color:#22863a">密码: admin</span></span></pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">技术说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目是基于solon的web系统, 数据库使用h2, 因此服务器上不需要安装任何数据库</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本系统通过Let's encrypt申请证书, 使用acme.sh脚本进行自动化申请和续签, 开启续签的证书将在每天凌晨2点进行续签, 只有超过50天的证书才会进行续签. 只支持在linux下签发证书.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">添加tcp/ip转发配置支持时, 一些低版本的nginx可能需要重新编译，通过添加–with-stream参数指定安装stream模块才能使用, 但在ubuntu 18.04下, 官方软件库中的nginx已经带有stream模块, 不需要重新编译. 本系统如果配置了tcp转发项的话, 会自动引入ngx_stream_module.so的配置项, 如果没有开启则不引入, 最大限度优化ngnix配置文件.</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">jar安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">以Ubuntu操作系统为例,</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>注意：本项目需要在root用户下运行系统命令，极容易被黑客利用，请一定修改密码为复杂密码</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.安装java运行环境和nginx</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Ubuntu:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>apt update</span>
<span>apt install openjdk-11-jdk</span>
<span>apt install nginx</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Centos:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>yum install java-11-openjdk</span>
<span>yum install nginx</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Windows:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>下载JDK安装包 https://www.oracle.com/java/technologies/downloads/</span>
<span>下载nginx http://nginx.org/en/download.html</span>
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
  <pre><span>Linux: wget -O /home/nginxWebUI/nginxWebUI.jar http://file.nginxwebui.cn/nginxWebUI-3.1.8.jar</span>

<span>Windows: 直接使用浏览器下载 http://file.nginxwebui.cn/nginxWebUI-3.1.8.jar</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">有新版本只需要修改路径中的版本即可</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动程序</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Linux: nohup java -jar -Dfile.encoding=UTF-8 /home/nginxWebUI/nginxWebUI.jar --server.port=8080 --project.home=/home/nginxWebUI/ > /dev/null &</span>

<span>Windows: java -jar -Dfile.encoding=UTF-8 D:/home/nginxWebUI/nginxWebUI.jar --server.port=8080 --project.home=D:/home/nginxWebUI/</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">参数说明(都是非必填)</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--server.port 占用端口, 默认以8080端口启动</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--project.home 项目配置文件目录，存放数据库文件，证书文件，日志等, 默认为/home/nginxWebUI/</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--spring.database.type=mysql 使用其他数据库，不填为使用本地h2数据库，可选mysql</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--spring.datasource.url=jdbc:mysql://ip:port/nginxwebui 数据库url</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--spring.datasource.username=root 数据库用户</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">--spring.datasource.password=pass 数据库密码</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意Linux命令最后加一个&号, 表示项目后台运行</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">docker安装说明</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">本项目制作了docker镜像, 支持 x86/x86_64/arm64/arm v7 平台，同时包含nginx和nginxWebUI在内, 一体化管理与运行nginx.</p> 
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
  <pre><span>docker pull cym1102/nginxwebui:latest</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.启动容器:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>docker run -itd \</span>
<span>  -v /home/nginxWebUI:/home/nginxWebUI \</span>
<span>  -e BOOT_OPTIONS="--server.port=8080" \</span>
<span>  --privileged=true \</span>
<span>  --net=host \</span>
<span>  cym1102/nginxwebui:latest</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意:</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">启动容器时请使用--net=host参数, 直接映射本机端口, 因为内部nginx可能使用任意一个端口, 所以必须映射本机所有端口.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">容器需要映射路径/home/nginxWebUI:/home/nginxWebUI, 此路径下存放项目所有数据文件, 包括数据库, nginx配置文件, 日志, 证书等, 升级镜像时, 此目录可保证项目数据不丢失. 请注意备份.</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">-e BOOT_OPTIONS 参数可填充java启动参数, 可以靠此项参数修改端口号, --server.port 为占用端口参数, 不填默认以8080端口启动</p> </li> 
 <li>日志默认存放在/home/nginxWebUI/log/nginxWebUI.log</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新说明</h4> 
<div> 
 <div>
  <span style="color:#000000">1.windows下支持自动更新</span>
 </div> 
 <div>
  <span style="color:#000000">2.使用java实现tail命令, 跟踪日志不再使用websocket协议</span>
 </div> 
 <div>
  <span style="color:#000000">3.修复通过非443,80端口代理情况下白屏问题</span>
 </div> 
 <div>
  <span style="color:#000000">4.修复导入文件过大无法识别问题</span>
 </div> 
 <div>
  <span style="color:#000000">5.修复远程同步数据过大无法同步问题</span>
 </div> 
 <div>
  <span style="color:#000000">6.修复指定project.home后log存放路径错误问题</span>
 </div> 
 <div>
  <span style="color:#000000">7.修复windows下运行docker乱码问题</span>
 </div> 
 <div>
  <span style="color:#000000">8.替换mysql驱动为8.x,规避漏洞</span>
 </div> 
</div> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            