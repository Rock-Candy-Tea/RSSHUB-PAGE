
---
title: '图片素材网站系统，PicHome 个人版 1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
author: 开源中国
comments: false
date: Mon, 09 May 2022 09:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欧奥 PicHome 个人版1.0 发布</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333">具体更新内容</strong></p> 
<div style="text-align:left"> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span style="color:#24292f">1.支持升级到团队版，可在站点设置->授权信息界面查看<br> 2.billfish数据支持，修复billfish导入有回收站数据导致导入进度不能完成的问题<br> 3.eagle数据支持，修复eagle导入更新数据时目录数据异常问题<br> 4.eagle数据支持，修复eagle导入非图片文件缩略图变更后显示异常问题<br> 5.普通目录数据支持，整体修改导入逻辑，修复导入错误，提升导入效率<br> 6.优化导入体验，导入增加部分错误提示，修复导入时删除库不断弹出弹窗的错误，以及导入类型提示不匹配问题<br> 7.导入增加校验更新，用于修复以往导入产生的错误修正<br> 7.修复删除库错误，由数据兼容错误导致没有真正删除问题<br> 8.增加文件访问永久地址获取（仅管理员可用）<br> 9.文件访问地址使用动态地址增强安全性（非永久地址）<br> 10.开放库筛选项设置，可在站点设置->筛选器设置中修改，支持标签分类作为单独筛选项展示；若库未设置筛选项，默认使用“全部库”筛选项，并依其变化而变化<br> 11.修复分享的移动端问题<br> 12.新增模板3(适用标签类筛选的内容）<br> 13.优化访问效率<br> 14.优化界面展示效果<br> 15.其他已知bug修复</span></p> 
 </div> 
 <p><strong>介绍</strong><br> pichome 是用于直接读取任意目录位置的图片，视频，音频，文档等文件。将其展示在 web 界面中，便于通过各种设备（电脑，手机，平板），直观的查看和搜索文件。支持多种筛选条件，如文件名称，目录，颜色，尺寸，文件大小，文件格式等多种组合筛选方式查询。支持大文件的高速查询，例如数十万文件的查询。而配置要求并不高，2 核 2G 的 nas 中也可以高效查询。</p> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>文件类型支持</strong><br> 普通目录：jpg，png，gif，webp，wav，MP3，mp4，pdf，txt 等。理论上是支持任意格式的文件导入，遇到不支持预览的格式会只显示文件图标，不能预览，仅能下载。支持预览的格式能够在线查看。<br> eagle 与 billfish 库目录，能够支持这些软件本身所支持的所有格式文件如 psd，ai，raw 等。具体支持那些格式可以到这些软件的官网了解。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">演示地址：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpichome.oaooa.com%2F" target="_blank">https://pichome.oaooa.com/</a><br> <strong><span style="background-color:#ffffff; color:#333333">下载地址：</span></strong><a href="https://gitee.com/zyx0814/Pichome">https://gitee.com/zyx0814/Pichome</a></p>
                                        </div>
                                      
</div>
            