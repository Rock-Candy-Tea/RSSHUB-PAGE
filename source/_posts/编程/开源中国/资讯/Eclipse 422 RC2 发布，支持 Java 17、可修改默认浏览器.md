
---
title: 'Eclipse 4.22 RC2 发布，支持 Java 17、可修改默认浏览器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7f8957e5dfc7949c05cf6c7b455db3d0e57.png'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 07:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7f8957e5dfc7949c05cf6c7b455db3d0e57.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Eclipse 4.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Flists%2Feclipse-dev%2Fmsg11825.html" target="_blank">发布</a>了第二个 RC 版本。跟往常一样，新版本在编辑器、窗口、工具栏和主题等方面进行了更新。</p> 
<p>Eclipse downloads：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.eclipse.org%2Feclipse%2Fdownloads%2Fdrops4%2FS-4.22RC2-202111241800%2F" target="_blank">https://download.eclipse.org/eclipse/downloads/drops4/S-4.22RC2-202111241800/</a></p> 
<p>主要更新内容如下：</p> 
<ul> 
 <li><strong>支持 Java 17</strong></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#4c4d4e">此版本特别包括以下 Java 17 功能：</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F306" target="_blank">JEP 306: Restore Always-Strict Floating-Point Semantics</a><span style="background-color:#ffffff; color:#4c4d4e">.</span><br> <span style="background-color:#ffffff; color:#333333">恢复始终执行严格模式 (Always-Strict) 的浮点定义</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F406" target="_blank">JEP 406: Pattern Matching for switch (Preview)</a><span style="background-color:#ffffff; color:#4c4d4e">.</span><br> switch 模式匹配进入预览 (Preview) 阶段</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F409" target="_blank">JEP 409: Sealed Classes (Final)</a><span style="background-color:#ffffff; color:#4c4d4e">.</span><br> 密封类和接口正式可用，用于<span style="background-color:#ffffff; color:#333333">限制哪些类和接口可以继承或实现它们。</span></p> 
<ul> 
 <li><strong>支持将字符串连接转换为文本块 (Text block)</strong></li> 
</ul> 
<p>转换前</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7f8957e5dfc7949c05cf6c7b455db3d0e57.png" referrerpolicy="no-referrer"></p> 
<p>转换后</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8283a2c7b0e37b311c10000d99bf4197b3a.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>改进了调用层次结构视图中的 lambda 支持</strong></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#4c4d4e">对于以下代码：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1311083a26331c4e6c82d3ed6c7651a1224.png" referrerpolicy="no-referrer"></p> 
<p>检查 function() 的调用者将显示：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8ddfb146adbeb1f0f52af382bd384c3bc24.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>默认使用外部浏览器</strong></li> 
</ul> 
<p>默认情况下，Eclipse IDE 将打开默认的系统浏览器，而不是内部浏览器。可以通过 Windows -> Preferences -> General -> Web Browser 来改变这一设置。</p> 
<ul> 
 <li><strong>新的 Launch Configuration 视图</strong></li> 
</ul> 
<p>新的 Launch Configuration 视图允许快速访问所有启动配置，无需进入启动对话框。此外还支持<span style="background-color:#ffffff; color:#4c4d4e">直接从视图启动（运行、调试、配置文件等）以及终止和/或重新启动运行配置。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7a8b9a420b3c8ef5741cd9aedc90b18e8b6.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>文本编辑器支持选择多行文本</strong></li> 
</ul> 
<p>多选可用于进行大多数编辑操作（文本替换或插入、将选择扩展到下一个单词或下一行、复制/粘贴……）</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f2dfcc0e9a78a19b211cabdf2875b4a57cc.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>Windows 深色主题样式标题栏</strong></li> 
</ul> 
<p>Windows 操作系统上深色主题中的 Windows 标题栏现在采用默认的深色主题样式。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c589bfe2043801d1afbe31f3b702289f582.png" referrerpolicy="no-referrer"></p> 
<p>详情查看：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.22%2Fplatform.php" target="_blank">New features in the Platform and Equinox</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipse%2Fnews%2F4.22%2Fjdt.php" target="_blank">New features for Java developers</a>​​​​​​​</li> 
</ul>
                                        </div>
                                      
</div>
            