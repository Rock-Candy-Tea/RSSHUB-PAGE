
---
title: '图片素材网站系统，PicHome Beta3.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 08:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">欧奥PicHome Beta3.3发布</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333">具体更新内容</strong></p> 
<div>
 <span>1.billfish数据支持，兼容billfish2.5数据结构导入</span>
 <br> 
 <span>2.eagle数据支持，兼容新旧版本eagle数据导入</span>
 <br> 
 <span>3.优化普通目录文件缩略图生成逻辑，优化效率，以及缩略图转换数字显示等问题修复</span>
 <br> 
 <span>4.修复普通目录由于文件名长度问题导致的文件缺失和部分服务器中存在因路径分割符不同导致文件导入累加式重复问题</span>
 <br> 
 <span>5.库设置增加库名称修改选项</span>
 <br> 
 <span>6.修复页面标签未分类数据显示错误问题，修复单一库时存在的筛选项不能正常显示问题</span>
 <br> 
 <span>7.页面增加按eagle和billfish内目录排序显示支持</span>
 <br> 
 <span>8.优化库删除逻辑，删除时清理库冗余数据</span>
 <br> 
 <span>9.文件访问地址修改为动态地址，增强文件私密性，为之后版本文件私密保护做准备</span>
 <br> 
 <span>10.其他已知bug修复 </span>
</div> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>介绍</strong><br> pichome是用于直接读取任意目录位置的图片，视频，音频，文档等文件。将其展示在web界面中，便于通过各种设备（电脑，手机，平板），直观的查看和搜索文件。支持多种筛选条件，如文件名称，目录，颜色，尺寸，文件大小，文件格式等多种组合筛选方式查询。支持大文件的高速查询，例如数十万文件的查询。而配置要求并不高，2核2G的nas中也可以高效查询。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">pichome是一个web程序，运行在PHP+MYSQL web环境下。可以部署在任意安装了PHP+MYSQL的环境中。windows，liunx，mac电脑或服务器中，nas设备中，甚至是装在手机中，做一个移动的图片服务器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>界面预览</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>PC界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="758" src="https://oscimg.oschina.net/oscnet/up-942fffea0b24351bcb9f1e925ca7775c7fe.jpg" width="1440" referrerpolicy="no-referrer"><br> <br> <strong>手机界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1810" src="https://oscimg.oschina.net/oscnet/up-b3657c6fa4fe0ca3da1bd68b3d3cf7954e6.jpg" width="1401" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><br> <strong>平板界面</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1382" src="https://oscimg.oschina.net/oscnet/up-9e35dc0014d8caea5a57ec383e5f8f823c4.jpg" width="1363" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>运行原理</strong><br> pichome只需要读取到指定的文件目录，本地目录，局域网的共享目录，或者是webdav远程目录。只需要读取权限，pichome不会对文件目录的结构和文件本身做任何的修改，平时还像往常维护自己的图片目录一样，增删改目录中的图片。然后在pichome的库设置中，点一下更新，就会将pichome中的数据与文件目录同步。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="722" src="https://oscimg.oschina.net/oscnet/up-e04e5d0bf0f25be61dcc3eb9c5ff737af4a.jpg" width="1022" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>筛选数据支持</strong><br> pichome除了支持普通的文件目录的导入，还支持一些专业的图片管理软件维护的图库目录。例如eagle，billfish。这些专业的图片管理软件中可以对图片打标签，写描述，支持更多类型的专业文件格式。例如PSD,AI,RAW等。pichome会自动获取这些专业软件数据库中的文件信息。在PH中能够利用这些数据信息进行筛选搜索。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>文件类型支持</strong><br> 普通目录：jpg，png，gif，webp，wav，MP3，mp4，pdf，txt等。理论上是支持任意格式的文件导入，遇到不支持预览的格式会只显示文件图标，不能预览，仅能下载。支持预览的格式能够在线查看。<br> eagle与billfish库目录，能够支持这些软件本身所支持的所有格式文件如psd，ai，raw等。具体支持那些格式可以到这些软件的官网了解。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">演示地址：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpichome.oaooa.com%2F" target="_blank">https://pichome.oaooa.com/</a><br> <strong><span style="background-color:#ffffff; color:#333333">下载地址：</span></strong><a href="https://gitee.com/zyx0814/Pichome">https://gitee.com/zyx0814/Pichome</a></p>
                                        </div>
                                      
</div>
            