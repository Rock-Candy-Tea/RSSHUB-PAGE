
---
title: 'All in One 的图片素材搜索与展示工具，PicHome Beta3.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
author: 开源中国
comments: false
date: Sat, 29 Jan 2022 11:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欧奥PicHome Beta3.2发布</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333">具体更新内容包括</strong></p> 
<div style="text-align:left">
 1.修复windows文件上传至linux服务器，由于编码问题导致的库导入没有文件问题
 <br> 2.库设置内容更改，当库状态为断开时，可以重新设置库的路径(即目录位置移动之后，库读取不到，可以设置为新目录所在位置)
 <br> 3.优化普通目录文件缩略图生成逻辑，以修复瀑布流展示时页面问题(此项对已生成过缩略图的不生效，需重新导入库生成）
 <br> 4.优化导入逻辑，当库在导入状态时，将会自动执行导入文件，直至导入完成为止
 <br> 5.修复eagle库注释显示html标签问题
 <br> 6.修复billfish库导入链接丢失问题
 <br> 7.优化删除逻辑
 <br> 8.其他已知bug修复 
 <p> </p> 
</div> 
<p><strong>介绍</strong><br> pichome是用于直接读取任意目录位置的图片，视频，音频，文档等文件。将其展示在web界面中，便于通过各种设备（电脑，手机，平板），直观的查看和搜索文件。支持多种筛选条件，如文件名称，目录，颜色，尺寸，文件大小，文件格式等多种组合筛选方式查询。支持大文件的高速查询，例如数十万文件的查询。而配置要求并不高，2核2G的nas中也可以高效查询。</p> 
<p>pichome是一个web程序，运行在PHP+MYSQL web环境下。可以部署在任意安装了PHP+MYSQL的环境中。windows，liunx，mac电脑或服务器中，nas设备中，甚至是装在手机中，做一个移动的图片服务器。</p> 
<p><strong>界面预览</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>PC界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="758" src="https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg" width="1440" referrerpolicy="no-referrer"><br> <br> <strong>手机界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1810" src="https://oscimg.oschina.net/oscnet/up-b3657c6fa4fe0ca3da1bd68b3d3cf7954e6.jpg" width="1401" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><br> <strong>平板界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1382" src="https://oscimg.oschina.net/oscnet/up-9e35dc0014d8caea5a57ec383e5f8f823c4.jpg" width="1363" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong>运行原理</strong><br> pichome只需要读取到指定的文件目录，本地目录，局域网的共享目录，或者是webdav远程目录。只需要读取权限，pichome不会对文件目录的结构和文件本身做任何的修改，平时还像往常维护自己的图片目录一样，增删改目录中的图片。然后在pichome的库设置中，点一下更新，就会将pichome中的数据与文件目录同步。</p> 
<p><img alt height="722" src="https://oscimg.oschina.net/oscnet/up-e04e5d0bf0f25be61dcc3eb9c5ff737af4a.jpg" width="1022" referrerpolicy="no-referrer"></p> 
<p><strong>筛选数据支持</strong><br> pichome除了支持普通的文件目录的导入，还支持一些专业的图片管理软件维护的图库目录。例如eagle，billfish。这些专业的图片管理软件中可以对图片打标签，写描述，支持更多类型的专业文件格式。例如PSD,AI,RAW等。pichome会自动获取这些专业软件数据库中的文件信息。在PH中能够利用这些数据信息进行筛选搜索。</p> 
<p><strong>文件类型支持</strong><br> 普通目录：jpg，png，gif，webp，wav，MP3，mp4，pdf，txt等。理论上是支持任意格式的文件导入，遇到不支持预览的格式会只显示文件图标，不能预览，仅能下载。支持预览的格式能够在线查看。<br> eagle与billfish库目录，能够支持这些软件本身所支持的所有格式文件如psd，ai，raw等。具体支持那些格式可以到这些软件的官网了解。</p> 
<p><strong><span style="background-color:#ffffff; color:#333333">演示地址：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpichome.oaooa.com%2F" target="_blank">https://pichome.oaooa.com/</a><br> <strong><span style="background-color:#ffffff; color:#333333">下载地址：</span></strong><a href="https://gitee.com/zyx0814/Pichome">https://gitee.com/zyx0814/Pichome</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            