
---
title: '图片素材网站系统，PicHome 个人版 1.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2170169e1dc14a1c2db81f7d479f56689f5.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 09:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2170169e1dc14a1c2db81f7d479f56689f5.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欧奥 PicHome 个人版 1.1 发布</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">本次主要增加了psd，ai，raw，office文档的预览支持。增加列表模式。集中文档类文件展示能够用于文库，知识库。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2170169e1dc14a1c2db81f7d479f56689f5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333">具体更新内容</strong></p> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <p style="margin-left:0; margin-right:0"><span>1.去掉原库设置中缩略图转换开关，站点设置增加存储位置设置，存储位置目前支持本地（默认），腾讯云存储</span><br> <span>2.本地存储位置图片处理功能开启关闭，将控制普通目录图片类文件缩略图和颜色信息获取，支持GD和imagick两种设置，其中imagick将支持特殊格式图片缩略图获取，</span><br> <span>包括并不限于ai、psd等格式，具体支持格式可在设置界面内查看</span><br> <span>3.本地存储位置视频处理功能开启关闭，将控制普通目录音视频类文件缩略图和信息获取，支持不能直接播放媒体文件转码，目前使用ffmpeg作为支持，具体支持格式可在设置界面内查看</span><br> <span>4.本地存储位置文档处理功能开启关闭，将控制普通目录文档类文件缩略图获取，支持文档在线预览(不限于普通目录），目前使用onlyoffice作为支持，具体支持格式可在设置界面内查看</span><br> <span>5.腾讯云位置图片处理功能开启关闭，将控制腾讯云存储中普通目录图片类文件缩略图和颜色信息获取，具体支持格式可在设置界面内查看</span><br> <span>6.腾讯云位置位置视频处理功能开启关闭，将控制腾讯云存储中普通目录音视频类文件缩略图和信息获取，支持不能直接播放媒体文件转码，具体支持格式可在设置界面内查看</span><br> <span>7.腾讯云位置位置文档处理功能开启关闭，将控制腾讯云存储中普通目录文档类文件缩略图，支持文档在线预览(不限于普通目录），具体支持格式可在设置界面内查看</span><br> <span>8.修复billfish库导入颜色权重未写入问题</span><br> <span>9.修改缩略图处理结构，优化缩略图处理逻辑，并支持billfish中特殊格式详情页高清图</span><br> <span>10.库设置中增加腾讯云存储位置库添加</span><br> <span>11.优化界面处理，修复已知界面问题</span><br> <span>12.优化库删除逻辑</span><br> <span>13.其他已知bug修复 </span></p> 
  </div> 
  <p><strong>介绍</strong><br> pichome 是用于直接读取任意目录位置的图片，视频，音频，文档等文件。将其展示在 web 界面中，便于通过各种设备（电脑，手机，平板），直观的查看和搜索文件。支持多种筛选条件，如文件名称，目录，颜色，尺寸，文件大小，文件格式等多种组合筛选方式查询。支持大文件的高速查询，例如数十万文件的查询。而配置要求并不高，2 核 2G 的 nas 中也可以高效查询。</p> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">pichome 是一个 web 程序，运行在 PHP+MYSQL web 环境下。可以部署在任意安装了 PHP+MYSQL 的环境中。windows，liunx，mac 电脑或服务器中，nas 设备中，甚至是装在手机中，做一个移动的图片服务器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>界面预览</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>PC 界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="758" src="https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg" width="1440" referrerpolicy="no-referrer"><br> <br> <strong>手机界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1810" src="https://oscimg.oschina.net/oscnet/up-b3657c6fa4fe0ca3da1bd68b3d3cf7954e6.jpg" width="1401" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><br> <strong>平板界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1382" src="https://oscimg.oschina.net/oscnet/up-9e35dc0014d8caea5a57ec383e5f8f823c4.jpg" width="1363" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>运行原理</strong><br> pichome 只需要读取到指定的文件目录，本地目录，局域网的共享目录，或者是 webdav 远程目录。只需要读取权限，pichome 不会对文件目录的结构和文件本身做任何的修改，平时还像往常维护自己的图片目录一样，增删改目录中的图片。然后在 pichome 的库设置中，点一下更新，就会将 pichome 中的数据与文件目录同步。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="722" src="https://oscimg.oschina.net/oscnet/up-e04e5d0bf0f25be61dcc3eb9c5ff737af4a.jpg" width="1022" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>筛选数据支持</strong><br> pichome 除了支持普通的文件目录的导入，还支持一些专业的图片管理软件维护的图库目录。例如 eagle，billfish。这些专业的图片管理软件中可以对图片打标签，写描述，支持更多类型的专业文件格式。例如 PSD,AI,RAW 等。pichome 会自动获取这些专业软件数据库中的文件信息。在 PH 中能够利用这些数据信息进行筛选搜索。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>文件类型支持</strong><br> 普通目录：理论上是支持任意格式的文件导入，遇到不支持预览的格式会只显示文件图标，不能预览，仅能下载。支持预览的格式能够在线查看。<br> eagle 与 billfish 库目录：能够支持这些软件本身所支持的所有格式文件如 psd，ai，raw 等。具体支持那些格式可以到这些软件的官网了解。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">演示地址：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpichome.oaooa.com%2F" target="_blank">https://pichome.oaooa.com/</a><br> <strong><span style="background-color:#ffffff; color:#333333">下载地址：</span></strong><a href="https://gitee.com/zyx0814/Pichome">https://gitee.com/zyx0814/Pichome</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            