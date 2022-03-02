
---
title: 'Eclipse 4.23 RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2517f4cd5311ee45082047a31878cc74ed5.png'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2517f4cd5311ee45082047a31878cc74ed5.png'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse 和 Equinox 4.23 (2022-03) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Flists%2Feclipse-dev%2Fmsg11894.html" target="_blank">发布</a>了首个 RC 版本。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Eclipse 下载地址<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fdownloads%2Fdrops4%2FS-4.23RC1-202202231800%2F" target="_blank">https://download.eclipse.org/eclipse/downloads/drops4/S-4.23RC1-202202231800/</a></li> 
 <li>更新内容<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2F" target="_blank">https://www.eclipse.org/eclipse/news/4.23/</a></li> 
 <li>升级已有安装版本（不要在生产环境进行）<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.23-I-builds%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.23-I-builds/</a></li> 
 <li>Specific repository good for building against:<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.23-I-builds%2FI20220223-1800%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.23-I-builds/I20220105-1800/</a></li> 
 <li>Equinox 相关下载<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Fequinox%2Fdrops%2FS-4.23RC1-202202231800%2F" target="_blank">https://download.eclipse.org/equinox/drops/S-4.23M1-202201051800/</a></li> 
</ul> 
<hr> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2F" target="_blank">Eclipse 4.23 更新亮点</a></h3> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fplatform.php%23inline-debug-values" target="_blank">调试器支持内联显示值</a></strong></p> 
<p>「Run/Debug」首选项页面增加了一个新选项，允许在文本编辑器上<strong>内联显示</strong>调试值。启用后会在行尾打印调试值作为代码注释。然后，当在执行过程中进行导航时，显示的值会对调试环境的变化做出反应。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2517f4cd5311ee45082047a31878cc74ed5.png" referrerpolicy="no-referrer"></p> 
<p>这是一个实验性功能，由于调试器需要额外的特性才能启用，因此并非所有调试器都支持。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ed5ece14e30333ddd68472d79210164a2c5.png" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fplatform.php%23large-file-associations" target="_blank">用于关联大文件的首选项</a></strong></p> 
<p>添加了一组新的首选项，可以指定使用哪个编辑器打开特定类型的大文件。此功能允许用户为大型项目文件指定更好地扩展的编辑器：例如，用于大型代码仓库的文本编辑器，或用于 Eclipse 编辑器无法很好处理的非常大型的文件的外部编辑器。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c112537d41a8a5319ed9f88b303fdf56e7b.png" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fplatform.php%23process-pid" target="_blank">在调试器中显示进程 ID</a></strong></p> 
<p><span>Eclipse Debug 框架现已支持显示已启动进程的进程 ID (pid)。pid 显示在进程的控制台视图描述和属性页面中。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-01e49ce03edc43df3159324d12bd8cb60c0.png" referrerpolicy="no-referrer"></p> 
<p>此外，Java 调试器现在会在 Debug 视图中显示进程元素的进程 ID。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-53a6d87506528f704e1614e9941e257842d.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fjdt.php" target="_blank"><strong>Java 编辑器</strong></a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fjdt.php%23codeassist-module" target="_blank">对 @see、@link 和 @linkplain javadoc 标记中的模块的代码辅助支持</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新的代码辅助支持已经被添加到 @see、@link 和 @linkplain javadoc 标签中的模块，适用于 Java 15 及更高版本的项目。下图显示了当在光标位置按下<strong style="color:#4c4d4e">'Ctrl + Space'</strong>时，该项目可以访问的模块名称被建议。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-f3edcddf9b3da6261614171165b04d37395.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图显示了当在光标位置按下<strong style="color:#4c4d4e">'Ctrl + Space'</strong>时，上述所选模块所输出的包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-ed98eddac529a8805a1aeba6e42f47c2b31.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图显示了当在光标位置按下<strong style="color:#4c4d4e">'Ctrl + Space'</strong>时，上述所选包中的类。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-8f66d61c0ca7bbdb4ce9991e4fd6a270119.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2Fjdt.php%23save-to-static-favorites" target="_blank">保存静态成员</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">增加了一个新的内容辅助功能，支持将 static import 保存到<span style="background-color:#ffffff; color:#4c4d4e"><span> </span></span><strong style="color:#4c4d4e">Preferences -> Java -> Editor -> Content Assist -></strong><strong>静态成员收藏夹列表，</strong>以通过内容辅助提出建议。要调用新功能，请在所需的 static import 上执行 <strong style="color:#4c4d4e">Ctrl + 1 </strong>以添加：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-ddef1c06ab3f3386d270c62b3ac0c42cec8.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.23%2F" target="_blank">详情点此查看</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            