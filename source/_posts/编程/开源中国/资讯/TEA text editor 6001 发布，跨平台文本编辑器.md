
---
title: 'TEA text editor 60.0.1 发布，跨平台文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=697'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=697'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TEA 是一个具有图形化使用者界面的文本编辑器，名称是从英文 Text Editor of the Atomic Era（意为“原子时代的文字编辑器”）的首字母缩略而衍生。它是为了资源低消耗、广泛的函式功能和适应性而设计的，并且可用于 Qt 5 或 4.6 版本以上支援的所有桌面操作系统，其使用者界面也有多种语言的版本。</p> 
<p>TEA 的上一个版本还是 2019 年发布的 50.1.0，在 50 版本之后直接跳至 60 版本是为了表达代码的重大变化和与 Qt 6 的兼容性。现在 TEA 可以针对 Qt 4（针对遗留系统）、Qt 5 和 Qt 6 进行构建。</p> 
<p>在 TEA 60 中，对历经 14 年的成熟代码库进行了逐行审查，并且对很多内容进行了重写。但出于对老编译器的尊重，还是没有使用"现代 C++"。</p> 
<p>那么，TEA 60 有什么新的内容呢？</p> 
<ul> 
 <li>重写了输入输出子系统；</li> 
 <li>取消了对 QML 的支持，不再有插件。</li> 
 <li>增加了 2/Rexx、Lua、Windows 批处理文件作为脚本的支持（此前已经支持 Bash、Perl、Ruby、Python）；</li> 
 <li>TEA 现在使用了一些桌面主题的图标；</li> 
 <li>重写了拼写检查器模块；</li> 
 <li>语法高亮引擎几乎是新的，旧的语法高亮规则文件格式已经不再支持了——TEA 将使用新的，尽管是基于旧的做出的改进；</li> 
 <li>使用 Ctrl-鼠标滚轮来缩放当前文件的文本；</li> 
 <li>由于一些改进，TEA 的启动时间缩短了（拼写检查器现在只在需要时才初始化）。</li> 
 <li>TEA 60 在 Qt6 下是稳定的，就如同在 Qt5 下一样。如果是针对 Qt6 构建，请在 deps 中添加 "Qt6-5compat" 模块；</li> 
 <li>修复在 CentOS 和 OS/2 上构建的 TEA；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftea.ourproject.org%2F" target="_blank">https://tea.ourproject.org/</a></p>
                                        </div>
                                      
</div>
            