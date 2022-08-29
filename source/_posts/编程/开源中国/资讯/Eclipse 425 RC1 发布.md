
---
title: 'Eclipse 4.25 RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6f9a49197af78300aca7e1f6b9ef8790aca.png'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 06:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6f9a49197af78300aca7e1f6b9ef8790aca.png'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse 和 Equinox 4.25 (2022-09) 发布了第一个 RC 版本。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">Eclipse 下载地址</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fdownloads%2Fdrops4%2FS-4.25RC1-202208241800%2F" target="_blank">https://download.eclipse.org/eclipse/downloads/drops4/S-4.25RC1-202208241800/</a></li> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">更新内容</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2F" target="_blank">https://www.eclipse.org/eclipse/news/4.25/</a></li> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">升级已有安装版本（不要在生产环境进行）</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.25-I-builds%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.25-I-builds/</a></li> 
 <li>Specific repository good for building against<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.25-I-builds%2FI20220824-1800%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.25-I-builds/I20220824-1800/</a></li> 
 <li>Equinox 相关下载<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Fequinox%2Fdrops%2FS-4.25RC1-202208241800%2F" target="_blank">https://download.eclipse.org/equinox/drops/S-4.25RC1-202208241800/</a></li> 
</ul> 
<hr> 
<p><strong>更新亮点</strong></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2Fplatform.php%23enable-word-wrap-on-open" target="_blank">支持设置默认启用文字换行 (word wrap)</a></strong></li> 
</ul> 
<p>在"General > Editors > Text Editors"页面中增加了一个新的设置选项，以指定在打开文本编辑器时默认开启“文字换行”功能。该功能在默认情况下是禁用的。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6f9a49197af78300aca7e1f6b9ef8790aca.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2Fplatform.php%23debug-ansi-support" target="_blank">控制台支持 ANSI 转义代码</a></strong></li> 
</ul> 
<p>控制台现已支持 ANSI 转义代码，可产生风格化的输出。它支持16色、256色、真彩色的前景和背景、调色板以及粗体、斜体、下划线、反转、删除、划线、加框等属性：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e4bb1ad36ab30beb511b765a29e9e431529.png" referrerpolicy="no-referrer"></p> 
<p>设置路径：<strong style="color:#4c4d4e">Preferences > Run/Debug > Console > ANSI Support</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3556c9390ef613bce936e25f72ebbb36712.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2Fjdt.php%23junit5-test-suite-wizard-support" target="_blank">测试套件向导现已支持 JUnit 5</a></strong></li> 
</ul> 
<p>此版本增强了测试套件向导功能，支持使用 @Suite 注释创建 JUnit 5 测试套件。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-44756af3ce2a78ae7cfa09390669424e0a0.png" referrerpolicy="no-referrer"></p> 
<p>效果</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-04ccff0bdffb6cc47109301688be4092ab6.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2Fjdt.php%23convert-to-switch-expression" target="_blank">转换为 switch 表达式</a></strong></li> 
</ul> 
<p>转换前：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a423d0e964a89bb76f4a27ddb42d996c28a.png" referrerpolicy="no-referrer"></p> 
<p>转换后：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7c4d70574720ed1ee572785588fd32fcf15.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.25%2Fjdt.php" target="_blank">详情点此查看</a>。</p>
                                        </div>
                                      
</div>
            