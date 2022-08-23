
---
title: '青阳网络文件传输系统 kiftd 1.1.0 正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/b970aab9102e6a54d300d87eb68bc132132.jpg'
author: 开源中国
comments: false
date: Tue, 23 Aug 2022 09:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/b970aab9102e6a54d300d87eb68bc132132.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="300" src="https://oscimg.oschina.net/oscnet/b970aab9102e6a54d300d87eb68bc132132.jpg" width="300" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>kiftd 简介：</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">kiftd 是一款专门面向个人、团队和小型组织的私有网盘系统。开源、便捷、小巧。无论是在笔记本上、家庭、学校还是办公室，均可以随时随地使用它。它不但是替代 U 盘进行文件传输的不二之选，同时也是一款具备视频 / 音乐在线播放、文档预览、图片查看、文件夹访问控制、拖拽上传、移动端访问等多种功能的个人云存储应用。它无任何的使用限制（无论是非商业的还是商业的），即开即用，即使是刚刚学会点击鼠标的小白也能够在 3 分钟内快速开始。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">想要了解更多内容？欢迎访问项目官网：<a href="https://kohgylw.gitee.io/index.html">https://kohgylw.gitee.io/index.html</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="392" src="https://oscimg.oschina.net/oscnet/a635b8f134c18c1499c7aeb39bc697a3f22.jpg" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>新版本 v1.1.0</strong></h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><em>* 本次更新升级了程序框架，并加入了一些实用的新功能，推荐所有用户升级。</em></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:#5a5a5a">新增WebDAV支持功能！</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">很多用户都希望将kiftd挂载至本地操作系统中以便日常使用，现在，这一功能已经实现。通过新增的WebDAV协议，您可以在Windows、Mac OS或Linux上将kiftd作为一个“网络驱动器”进行挂载，并像在普通文件夹中一样访问和编辑kiftd中的文件。对于需要频繁访问kiftd进行数据传输的用户而言，该功能将大大提高便捷性。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">以Windows 11系统为例，将kiftd挂载为“网络驱动器”的方法如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1，由于Windows默认不支持使用http协议进行挂载，因此在开始之前，需要先修改注册表编辑器，将位于“计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters”文件夹中的“BasicAuthLevel”值改为2：</p> 
<p><img height="1650" src="https://oscimg.oschina.net/oscnet/up-069eaf27d4c6eb540dab00abd672a4b7dc6.png" width="3020" referrerpolicy="no-referrer"></p> 
<p>然后点击“确定”。设置完毕后，需要重启计算机或是重启“WebClient”服务令上述设置生效。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2，打开“此电脑”，并在空白位置右键，选择菜单中的“显示更多选项”：</p> 
<p><img height="1350" src="https://oscimg.oschina.net/oscnet/up-fb4541856bf7281e049697ca6c1529c7c3d.png" width="2346" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3，选择展开目录中的“添加一个网络位置”：</p> 
<p><img height="406" src="https://oscimg.oschina.net/oscnet/up-bbe570197245644a1f79c7310665617b267.png" width="436" referrerpolicy="no-referrer"></p> 
<p>4，根据向导逐步完成设置，其中，第三步需要输入Internet地址或网络地址为“http://&#123;计算机IP地址&#125;:&#123;kiftd端口号&#125;/dav/”（例如“http://127.0.0.1:8080/dav/”，计算机地址可以从“网络和Internet设置”中查看），：</p> 
<p><img height="1236" src="https://oscimg.oschina.net/oscnet/up-156d037a98212fb8addec826ec5b92d5772.png" width="2346" referrerpolicy="no-referrer"></p> 
<p><img height="1258" src="https://oscimg.oschina.net/oscnet/up-a5d8e5a7f98ba5bc1ecd3d6af424fc8f4c1.png" width="2354" referrerpolicy="no-referrer"></p> 
<p><img height="1316" src="https://oscimg.oschina.net/oscnet/up-aa19444b23e953d0fdcaba4a172be80df94.png" width="2434" referrerpolicy="no-referrer"></p> 
<p><img height="1262" src="https://oscimg.oschina.net/oscnet/up-b1b275fe296fc444b56079456dbe4717244.png" width="2380" referrerpolicy="no-referrer"></p> 
<p><img height="1270" src="https://oscimg.oschina.net/oscnet/up-0aba582253d3e42af3a566637e4942bc52a.png" width="2352" referrerpolicy="no-referrer"></p> 
<p><img height="1232" src="https://oscimg.oschina.net/oscnet/up-2526ffad1179b352cb82887a8f58c157d23.png" width="2336" referrerpolicy="no-referrer"></p> 
<p>5，退出向导后，您应该已经可以看到挂载好的kiftd“网络驱动器”了（同局域网的其他访问者也可以用上述方式进行挂载，从而访问您的kiftd以便进行文件共享）：</p> 
<p><img height="1294" src="https://oscimg.oschina.net/oscnet/up-b3da78c56548f39cb9a5a7051f908a18d57.png" width="2400" referrerpolicy="no-referrer"></p> 
<p>6，接下来，您（或其他挂载了此驱动器的访问者）就可以像在普通文件夹中一样在kiftd中自由访问和编辑文件了：</p> 
<p><img height="1648" src="https://oscimg.oschina.net/oscnet/up-fccf8f376e03c9a5210102af7961ddf7cce.png" width="3020" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"><span style="color:#5a5a5a">新增“删除留档”功能。</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">为了进一步降低用户在使用过程中误删重要文件的可能性，kiftd现已加入“删除留档”功能来确保管理员拥有一次挽救误删数据的机会。开启此功能后，所有在kiftd中杯删除的文件均会按照删除日期留档至指定文件夹内，以便您做进一步的处理。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">开启方法为：在conf/server.properties文件中增加设置“recyclebin=&#123;留档文件夹路径&#125;”，其中“&#123;留档文件夹路径&#125;”必须是一个已存在的、具备读写权限的文件夹。设置完毕后，保存此文件并重启kiftd应用即可开启此功能。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">示例如下：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#5a5a5a">1，准备一个留档文件夹（该文件夹的路径中不应含有中文，以免程序识别错误）：</span></p> 
<p><img height="1294" src="https://oscimg.oschina.net/oscnet/up-61bb2d05404072f1dccb538fe54b05001d5.png" width="2310" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left">2，编辑“server.properties”文件，设置留档文件夹路径：</p> 
<p><img height="1414" src="https://oscimg.oschina.net/oscnet/up-0bd6995ebcdb99d6d5615dbe77efb71d1da.png" width="2352" referrerpolicy="no-referrer"></p> 
<p>3，启动kiftd。此时，所有在kiftd中被删除的文件都将会留档至指定的文件夹内，便于您后续处理：</p> 
<p><img height="1648" src="https://oscimg.oschina.net/oscnet/up-b419a63646804be473b7f77ca0ffdfd8d07.png" width="3018" referrerpolicy="no-referrer"></p> 
<p><img height="1650" src="https://oscimg.oschina.net/oscnet/up-b5c612ecfddfc3df520a45bb39aad2f7bb8.png" width="3020" referrerpolicy="no-referrer"></p> 
<p>除了上述新功能外，新版本还包括以下更新：</p> 
<ul> 
 <li>程序底层框架升级。现在，新的kiftd已经支持新的Java版本（例如Java 17）和新的操作系统（例如Windows 11）了，同时，系统的稳定性和性能也得到了提升。</li> 
 <li>优化了下载限速算法——下载限速功能的速度限制精度大大提高了。</li> 
 <li>修复了主页“公告栏”不会及时更新的问题。</li> 
 <li>其他一些细节优化。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以上便是本次更新的全部内容，欢迎您下载并更新体验！</p> 
<p> </p>
                                        </div>
                                      
</div>
            