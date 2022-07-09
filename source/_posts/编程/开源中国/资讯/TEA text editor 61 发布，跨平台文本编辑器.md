
---
title: 'TEA text editor 61 发布，跨平台文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6573'
author: 开源中国
comments: false
date: Sat, 09 Jul 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6573'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TEA 是一个具有图形化用户界面的文本编辑器，名称是从英文 Text Editor of the Atomic Era（意为“原子时代的文字编辑器”）的首字母缩略而衍生。它是为低资源消耗、广泛的功能和适应性而设计的，可用于 Qt 6、5 或 4.6+ 支持的所有桌面操作系统。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">那么，TEA 61 有什么新的内容呢？</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>所有内部的 XML 解析都被转移到 pugixml，而不是 Qt 的 XML 解析器</li> 
 <li>pugixml 更快，对 TEA 更有用</li> 
 <li>XML 解析被用于一些文本格式支持（如 FB2、ODT 等）和语法高亮引擎，所有这些东西都已经过重写。</li> 
 <li>为了处理复杂的文件名，新的 TEA 对书签和 "最近" 列表使用了一种新的格式 
  <ul style="margin-left:0; margin-right:0"> 
   <li>书签文件将被自动转换为新的格式，而且 TEA 现在使用一个不同的文件来保存书签</li> 
   <li>“最近” 列表将通过打开文件来更新</li> 
  </ul> </li> 
 <li>新选项：Tune - Functions - Misc - Show ebooks fine；当你打开 FB2、Epub 等文件时，它在每个段落前添加空格。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftea.ourproject.org%2F" target="_blank">https://tea.ourproject.org/</a></p>
                                        </div>
                                      
</div>
            