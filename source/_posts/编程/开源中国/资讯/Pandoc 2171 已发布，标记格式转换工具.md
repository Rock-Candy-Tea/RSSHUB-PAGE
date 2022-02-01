
---
title: 'Pandoc 2.17.1 已发布，标记格式转换工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4620'
author: 开源中国
comments: false
date: Tue, 01 Feb 2022 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4620'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Pandoc 2.17.1 发布了</span><span style="color:#333333">，Pandoc 是一个通用标记转换 Haskell 库，用于从一种标记格式转换为另一种，同时也是一个使用该库的命令行工具，它可以转换 28 种标记格式。</span></p> 
<ul> 
 <li>支持<code>pagedjs-cli</code> pdf 引擎（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fpull%2F7838" target="_blank">#7838</a>）</li> 
 <li>CommonMark 阅读器：在 YAML 元数据后修复源位置。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7863" target="_blank">#7863</a> )</li> 
 <li>Docx 阅读器：将 Zotero 引文和参考书目解析为<code>FieldInfo</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7840" target="_blank">#7840</a> )</li> 
 <li>Markdown writer：使用管道表处理显式列宽（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7847" target="_blank">#7847</a>）</li> 
 <li>Docx writer：即使在 RawBlocks 之间也可以分开表格 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7224" target="_blank">#7224</a>）</li> 
 <li><span style="color:#24292f">Man writer：</span>对内联代码使用自定义字体 V ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7506" target="_blank">#7506</a> )</li> 
 <li>HTML 编写器： 
  <ul> 
   <li>避免在表格单元格上出现重复的“样式”属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7871" target="_blank">#7871</a>）。</li> 
   <li>不要在代码元素内换行。使用 HTML 的新（默认）换行，以及包含 的默认 CSS，<code>code &#123; whitespace: pre-wrap; &#125;</code>可以将虚假换行符引入内联代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7858" target="_blank">#7858</a>）。</li> 
  </ul> </li> 
 <li>切换到 hslua-2.1 ，简化一些代码并提高稳定性。</li> 
 <li><strong>...</strong></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Freleases%2Ftag%2F2.17.1" target="_blank">https://github.com/jgm/pandoc/releases/tag/2.17.1</a></p>
                                        </div>
                                      
</div>
            