
---
title: 'JFinal-layui-pro v2.5 优化附件在线预览功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.qinhaisenlin.com/upload/img/document/0/1_2021060916114263.png'
author: 开源中国
comments: false
date: Thu, 10 Jun 2021 17:47:00 GMT
thumbnail: 'https://www.qinhaisenlin.com/upload/img/document/0/1_2021060916114263.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JFinal-layui-pro-v2.5整合了文件在线预览项目kkFileView，利用kkFileView强大的文件预览功能，轻松实现我们的附件预览。</p> 
<p>kkFileView官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkkfileview.keking.cn%2F" target="_blank">https://kkfileview.keking.cn/</a></p> 
<p>一、首先是部署启动kkFileView文件预览服务：</p> 
<p>---------------------------------------------------------------------------------------------</p> 
<p>部署本地服务：</p> 
<p>1、解压kkFileView-3.5.1.rar文件(进JFinal-layui交流群下载：970045838)</p> 
<p>2、打开解压后文件夹的bin目录，运行startup脚本（Windows下以管理员身份运行startup.bat，Linux以root用户运行startup.sh）</p> 
<p>3、浏览器访问本机8012端口 http://127.0.0.1:8012 即可看到项目演示用首页</p> 
<p>4、将http://127.0.0.1:8012/onlinePreview配置到config-dev.txt文件的onlinePreviewUrl配置项中,并且onlinePreview=true开启在线预览服务</p> 
<p> </p> 
<p>环境要求：</p> 
<p>1、Java: 1.8+</p> 
<p>2、OpenOffice或LiberOffice(Windows下已内置，CentOS或Ubuntu下会自动下载安装，MacOS下需要自行安装)</p> 
<p>-----------------------------------------------------------------------------------------------</p> 
<p>二、在配置config-dev.txt文件开启在线预览服务</p> 
<pre>#文件在线预览服务：true-开启，false-关闭，如果是关闭在线预览服务，会自动切换系统自带的预览功能，但是只能预览图片、pdf、txt文件
onlinePreview=true
#文件在线服务地址
onlinePreviewUrl=http://localhost:8012/onlinePreview
</pre> 
<p> </p> 
<p>三、启动项目，在通用的附件管理功能里面预览即可。</p> 
<p>图片预览效果：</p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021060916114263.png" referrerpolicy="no-referrer"></p> 
<p>excel文档预览：</p> 
<p><img alt="微信截图_20210610173443 (1).png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610174111150.png" referrerpolicy="no-referrer"></p> 
<p>word文档预览：</p> 
<p><img alt="微信截图_20210610173335 (1).png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610174217151.png" referrerpolicy="no-referrer"></p> 
<p>视频预览：</p> 
<p><img alt="微信截图_20210610173505 (1).png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610174230152.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p>ppt预览：</p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/document/0/1_2021060916134964.png" referrerpolicy="no-referrer"></p> 
<p>四、默认是不开启在线预览服务，使用系统内置的预览功能，只是仅仅实现了图片、pdf、txt的文件预览功能。</p> 
<p>图片预览：<img alt="微信截图_20210610172802.png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610173034149.png" referrerpolicy="no-referrer"></p> 
<p>pdf预览：</p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610172004147.png" referrerpolicy="no-referrer"></p> 
<p>txt文件预览：</p> 
<p><img alt="image.png" src="https://www.qinhaisenlin.com/upload/img/tst/0/1_20210610172050148.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p><span style="background-color:#ffffff; color:#333333"> </span><span style="color:#333333">JFinal-layui-pro</span><span style="color:#333333">下载地址</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://gitee.com/QinHaiSenLin/Jfinal-layui/tree/pro/" target="_blank">https://gitee.com/QinHaiSenLin/Jfinal-layui/tree/pro/</a></p> 
<p> 专业版在线演示系统：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.qinhaisenlin.com%3A8081%2F" target="_blank">JFinal-layui极速开发企业应用系统</a>    账号：admin/123456</p>
                                        </div>
                                      
</div>
            