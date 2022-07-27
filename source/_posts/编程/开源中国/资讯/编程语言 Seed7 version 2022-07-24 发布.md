
---
title: '编程语言 Seed7 version 2022-07-24 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0727/070409_vtWa_4937141.png'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 07:04:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0727/070409_vtWa_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Seed7 version 2022-07-24 已发布，此版本值得关注的变化：</p> 
<ul> 
 <li>改进错误报告，尤其是对于失败的声明语句，现在会提供更好的错误消息。</li> 
 <li>改进 Seed7 构建系统，避免了静态库部分链接和防病毒软件的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Flibraries%2Fkeybd.htm%23getc%28in_console_keybd_file%29" target="_blank">支持使用 getc(KEYBOARD)</a> 正确读取从剪贴板复制到 Windows 控制台的数据。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Flibraries%2Funicode.htm" target="_blank">unicode.s7i</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Flibraries%2Fkeybd.htm" target="_blank">keybd.s7i</a> 引入了更容易记住的函数名称。</li> 
</ul> 
<p><span style="color:#333333">开发者可从 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FThomasMertes%2Fseed7">GitHub</a><span style="color:#333333"> 和 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fseed7%2Ffiles%2Flatest%2Fdownload">SF</a><span style="color:#333333"> 获取新版本，此外还有一个 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fseed7%2Ffiles%2Fbin%2Fseed7_05_20191117_win.exe%2Fdownload">Windows 的 Seed7 安装程序</a><span style="color:#333333">。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fseed7%2Fcomments%2Fw7i8vw%2Fseed7_version_20220724_released_on_github_and_sf%2F" target="_blank">点此查看详细更新内容</a>。</p> 
<p style="margin-left:0">与 Ada、C/C++ 和 Java 相比，Seed7 是一种比它们更高级的编程语言。Seed7 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Ffaq.htm%23interpreter">解释器</a>和<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Fscrshots%2Findex.htm">示例程序</a>是开源软件，还有一个开源 Seed7 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Fscrshots%2Fs7c.htm">编译器</a>。编译器将 Seed7 程序翻译成 C 程序，然后编译成机器代码。<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Findex.htm">详细介绍</a>。</p> 
<p style="margin-left:0">下面是一段用 Seed7 编写的代码：</p> 
<pre><span>$</span> <span>include</span> <span>"seed7_05.s7i"</span><span>;</span>

 <span>const</span> <span>proc:</span> <span>main</span> <span>is</span> <span>func</span>
   <span>begin</span>
     <span>writeln</span><span>(</span><span>"hello world"</span><span>)</span><span>;</span>
   <span>end</span> <span>func</span><span>;</span></pre> 
<p style="margin-left:0">下面是一些用 Seed7 开发的程序的界面截图：</p> 
<p style="margin-left:0"><img height="162" src="https://static.oschina.net/uploads/space/2022/0727/070409_vtWa_4937141.png" width="200" referrerpolicy="no-referrer"><img height="158" src="https://static.oschina.net/uploads/space/2022/0727/070409_VBWo_4937141.png" width="201" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0">更多的程序界面截图请看：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseed7.sourceforge.net%2Fscrshots%2Findex.htm" target="_blank">http://seed7.sourceforge.net/scrshots/index.htm</a></p>
                                        </div>
                                      
</div>
            