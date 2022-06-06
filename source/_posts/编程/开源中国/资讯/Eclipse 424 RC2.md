
---
title: 'Eclipse 4.24 RC2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0606/072901_xckj_2720166.gif'
author: 开源中国
comments: false
date: Mon, 06 Jun 2022 07:42:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0606/072901_xckj_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse 和 Equinox 4.24 (2022-06) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Flists%2Feclipse-dev%2Fmsg12027.html" target="_blank">发布</a>了第二个 RC 版本。</p> 
<ul> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">Eclipse 下载地址</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fdownloads%2Fdrops4%2FS-4.24RC2-202206011800%2F" target="_blank">https://download.eclipse.org/eclipse/downloads/drops4/S-4.24RC2-202206011800/</a></li> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">更新内容</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2F" target="_blank">https://www.eclipse.org/eclipse/news/4.24/</a></li> 
 <li><span style="background-color:#ffffff"><span style="color:#333333">升级已有安装版本（不要在生产环境进行）</span></span><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.24-I-builds%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.24-I-builds/</a></li> 
 <li>Specific repository good for building against<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fupdates%2F4.24-I-builds%2FI20220601-1800%2F" target="_blank">https://download.eclipse.org/eclipse/updates/4.24-I-builds/I20220601-1800/</a></li> 
 <li>Equinox 相关下载<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Fequinox%2Fdrops%2FS-4.24RC2-202206011800%2F" target="_blank">https://download.eclipse.org/equinox/drops/S-4.24RC2-202206011800/</a></li> 
</ul> 
<hr> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2F" target="_blank">Eclipse 4.24 更新亮点</a></h3> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fplatform.php%23multi-select-commands" target="_blank">提供用于多个插入符号/选择的操作命令</a></strong></p> 
<p><strong>文本编辑器</strong>现在提供各种命令来支持多个插入符号/选择，这些插入符号/选择可以绑定到用户定义的键盘快捷键，以便在文本编辑器中轻松选择文本区域。</p> 
<p><img height="917" src="https://static.oschina.net/uploads/space/2022/0606/072901_xckj_2720166.gif" width="2276" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fplatform.php%23explicit-encoding-workspaces" target="_blank">为新工作区设置默认编码集</a></strong></p> 
<p>如果 Eclipse 在未设置显式默认编码的情况下启动，则 <strong style="color:#4c4d4e">UTF-8 </strong>将被设置为新工作区的默认编码。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#4c4d4e"><span style="background-color:#ffffff">如果在 Eclipse 启动时将某些编码指定为 JVM 系统属性<code>-Dfile.encoding=XYZ</code> 或产品定制首选项<code>org.eclipse.core.resources/encoding=XYZ</code> ，则此定制编码将作为新工作区的默认编码保留。</span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#4c4d4e"><span style="background-color:#ffffff">之后，在新工作区中创建的所有新项目也将具有显式的默认编码集（它们将从工作区编码而不是从当前操作系统设置中获取的某些随机编码派生出来）。</span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#4c4d4e"><span style="background-color:#ffffff">已设置编码的现有工作区或项目将不受影响，会保留其原始编码。</span></span></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fplatform.php%23no-explicit-encoding-project-warning" target="_blank">对没有明确默认编码的项目发出警告</a></strong></p> 
<p>Eclipse 现在会为没有明确默认编码的项目创建一个警告标记。标记包含一个快速修复，将项目默认编码设置为工作区编码。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-27aaec9ef727ba135db68a9e725f1f22194.png" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fjdt.php%23Java_18" target="_blank">支持 Java 18</a></strong></p> 
<p>此版本特别支持以下 Java 18 特性：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F420" target="_blank">JEP 420：switch 的模式匹配（第二个预览版）</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F413" target="_blank">JEP 413：Java API 文档中的代码片段</a></li> 
</ul> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fjdt.php%23strconcat-to-textblock" target="_blank">支持删除未使用的私有方法参数</a></strong></p> 
<p>添加了新的<strong style="color:#4c4d4e">清理</strong>和<strong style="color:#4c4d4e">快速帮助选项</strong>以删除私有方法的未使用参数。如果删除参数可能会导致与另一个方法发生冲突，则将私有方法重命名为唯一。如果有对该方法的方法引用，则清理不可用。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-04c26e73fdb3e26152492c57691d86cce6e.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#4c4d4e">示例：启用该功能后，下面代码</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-64c21217b9ce19d58da5e4f15fd3717770a.png" referrerpolicy="no-referrer"></p> 
<p>会被修改为：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-82b1b63e3fcdcb918386a70cc94a45b4e87.png" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fjdt.php%23extend_interface_assist" target="_blank">扩展接口</a></strong></p> 
<p>添加了一个新的<strong style="color:#4c4d4e">快速助手</strong>来扩展接口。选择后，将打开新的界面向导。</p> 
<p>​​​​​​​<img alt src="https://oscimg.oschina.net/oscnet/up-caaae903b4d239b9fd45d539fe5d993f9e4.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.24%2Fjdt.php" target="_blank">详情</a>。</p>
                                        </div>
                                      
</div>
            