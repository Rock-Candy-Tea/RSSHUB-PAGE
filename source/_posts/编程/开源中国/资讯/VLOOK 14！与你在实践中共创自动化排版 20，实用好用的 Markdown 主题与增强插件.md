
---
title: 'VLOOK 14！与你在实践中共创自动化排版 2.0，实用好用的 Markdown 主题与增强插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-96d616c448612eacf830d28c6e88565180f.png'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 10:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-96d616c448612eacf830d28c6e88565180f.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>VLOOK™</strong> 是针对<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftypora.io%2F" target="_blank">Typora</a>（跨平台 Markdown 编辑器）的 <strong>主题包</strong> 和 <strong>增强插件</strong>（针对导出的 HTML 文件)，<strong>旨在与众 Markdown 粉共创 Markdown 的自动化排版 2.0，在保持 Markdown 简洁性的基础上，让编辑、阅读 Markdown 文档更实用，也更愉悦。</strong></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>VLOOK™</strong> 属于开源软件（遵从 <strong>MIT License</strong>），也是<span> </span><strong><a href="https://www.oschina.net/p/vlook">OSCHINA 开源中国</a></strong> 推荐的国产开源产品、Typora 的首个增强插件。</p> 
</blockquote> 
<p><strong style="color:#333333">VLOOK™ 的所有特性清单，详见快速入坑 → <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmadmaxchow.github.io%2FVLOOK%2Findex.html%23%E5%BF%AB%E9%80%9F%E5%85%A5%E5%9D%91" target="_blank"><span>一键了解</span></a> （<a href="https://madmaxchow.gitee.io/vlook/index.html#%E5%BF%AB%E9%80%9F%E5%85%A5%E5%9D%91">备用链接</a>）</strong></p> 
<hr> 
<p>在 2021 年经过持续多个迭代优化版本，以及在实践中持续应用和改进，<strong>VLOOK™</strong> 作为最受欢迎的 Markdown 编辑器 Typora 的主题包和增强插件，释出了最新的 14.0 版本。</p> 
<p>在这个版本中，对原有的大量特性进行了完善和增强，一定会让你完全刷新对 Markdown 文档编辑和阅读的理解和体验。</p> 
<p>以下是本次迭代涉及的关键的的新特性、改善点：</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start">🎉<span> </span>NEW 新特性<span> </span>🎉</h1> 
<h2 style="text-align:start">🆕<span> </span>焕然一新的主题</h2> 
<ul> 
 <li>主题支持浏览器标题栏主题色。支持的浏览器：Safari 15+ (macOS & iOS)、Chrome 80+ (移动端)</li> 
 <li>正文中数字、标点等用使用等宽字体进行显示</li> 
 <li>开放更多主题的私人定制选项，让每个主题都更有自己的气质</li> 
 <li>新增主题 Solaris，致敬 Sun Solaris</li> 
</ul> 
<p><img height="1634" src="https://oscimg.oschina.net/oscnet/up-96d616c448612eacf830d28c6e88565180f.png" width="2048" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🆕<span> </span>链接工具升级</h2> 
<ul> 
 <li>自动转换 *.md 链接：对于维护多个 md 文档的场景会非常 nice，保留编辑时链接为 md，导出后自动转换为 html（或指定的扩展名）</li> 
 <li>支持通过普通链接打开文库：举例：<code>[点击打开文库](vlook://doc-lib)</code></li> 
</ul> 
<p><img height="1634" src="https://oscimg.oschina.net/oscnet/up-505c881194eec1a6557cce8b1200133666a.png" width="2048" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🆕<span> </span>Mermaid 样式与交互升级</h2> 
<ul> 
 <li>重新设计 VLOOK 风格的图表配色</li> 
 <li>适配新版流程图类型 flowchart（旧版为 graph）</li> 
 <li>适配最新流程图节点类型（如：子流程、六形、平行四边形、梯形等）</li> 
 <li>针对「流程图/顺序图/类图」提供演示辅助（鼠标悬停高亮元素）</li> 
</ul> 
<p><img height="1634" src="https://oscimg.oschina.net/oscnet/up-773f28919fec03308faeb0cce34b6727a0f.png" width="2048" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🆕<span> </span>自动排版新进化</h2> 
<ul> 
 <li>「分栏引用」同行中多项分栏内容高度自动对齐，并优化不同尺寸屏幕下的分栏样式适配</li> 
 <li>「彩虹引用」内的引用折叠、任务列表样式都会跟随适配对应的颜色</li> 
 <li>「图片排版」支持通过图片 URL 锚点进行快速设置，如右对齐：现有通过 Query 方式设置<span> </span><code>xxx.png?align=right</code>，通过新的锚点方式设置<span> </span><code>xxx.png#right</code>，目前支持的排版特性包括：显示版式、对齐方式、一行多图、边缘留白</li> 
 <li>彩虹系列「标签、徽章、引用」新增配色：钢青色 Steel</li> 
</ul> 
<p><img height="1634" src="https://oscimg.oschina.net/oscnet/up-a293d792741ff6790e33d983d8fbc3aaf78.png" width="2048" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">🆕<span> </span>内容助手【复制】大升级</h2> 
<ul> 
 <li>复制功能支持：代码块、标签、徽章、图片地址</li> 
 <li>支持按下「Ctrl / Command」复制为 Markdown 格式</li> 
</ul> 
<h2 style="text-align:start">🆕<span> </span>阅读体验升级</h2> 
<ul> 
 <li>根据标题主题色，优化不同屏幕大小升级「章节导航」的交互体验</li> 
 <li>状态栏增加了页面缩放的功能操作提示</li> 
</ul> 
<hr> 
<h1 style="margin-left:0; margin-right:0; text-align:start">▼▼▼ 更多更新说明 ▼▼▼</h1> 
<h2 style="text-align:start">♻️<span> </span>— What’s IMPROVED —<span> </span>♻️</h2> 
<ul> 
 <li>模板主题、插件大瘦身，精简掉约 30%</li> 
 <li>文档内容中无自动索引的内容时，默认收起导航中心</li> 
 <li>刮刮卡颜色同步最新 VLOOK 颜色标识</li> 
 <li>表格阅读模式样式优化，提高行/列内容的识别性</li> 
 <li>的字体优选显示非 emoji 字体</li> 
 <li>彩虹引用内折叠器样式跟随引用颜色</li> 
 <li>打印为PDF时的样式，保留文档主题封面/封底背景</li> 
 <li>优化工具提示的显示机制</li> 
 <li>完善对不同类型链接的识别</li> 
</ul> 
<p style="color:#24292f; text-align:start"><strong>更丰富的插件调校参数，定制更个性的文档交互</strong></p> 
<ul> 
 <li><code>dc-tag</code><span> </span><code>dc-badge</code><span> </span><code>dc-coat</code><span> </span><code>dc-quote</code><span> </span>调整彩虹标签、彩虹徽章、彩虹引用、刮刮卡的默认颜色</li> 
 <li><code>mdx</code><span> </span>关闭或指定自动转换 md 链接</li> 
 <li><code>toc</code><span> </span>指定目录大纲在文档打开后默认折叠的章节层级</li> 
 <li><code>stsbar</code><span> </span>状态栏内的条目支持调校参数关闭</li> 
 <li><code>capnum</code><span> </span><code>capauto</code><span> </span>调校参数支持无指定题注时自动生成题注内容开关 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmadmaxchow.github.io%2FVLOOK%2Fguide.html%23%25E6%258F%2592%25E4%25BB%25B6%25E8%25B0%2583%25E6%25A0%25A1%25E5%258F%2582%25E6%2595%25B0" target="_blank">完整的插件调校参数详见这里</a><span> </span>（<a href="https://madmaxchow.gitee.io/vlook/guide.html#%E6%8F%92%E4%BB%B6%E8%B0%83%E6%A0%A1%E5%8F%82%E6%95%B0">备用链接</a>）</li> 
</ul> 
<h2 style="text-align:start">⚠️<span> </span>— What’s CHANGED —<span> </span>⚠️</h2> 
<ul> 
 <li> <p>欢迎屏默认的内容调整为在<span> YAML </span>中定义的「标题、日期、时间」</p> </li> 
 <li> <p><span>修改「标签」样式</span></p> </li> 
 <li>调整表格折叠行的背景配色样式</li> 
</ul> 
<h2 style="text-align:start">🧯— What’s FIXED —<span> </span>🧯</h2> 
<ul> 
 <li>修复部分 emoji 在 Windows 平台显示不正常的问题</li> 
 <li>修复一些移动端浏览时的 bug 和兼容性的问题</li> 
 <li>修复无封面、无封底、无h6时，最后一个 h1 无法在目录 toc 中显示的问题</li> 
</ul> 
<hr> 
<p>项目托管于：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmadmaxchow%2FVLOOK" target="_blank">Github（须科学上网）</a></li> 
 <li><span>[</span>Gitee<span>（国内备用）]</span>(<a href="https://gitee.com/madmaxchow/VLOOK">https://gitee.com/madmaxchow/VLOOK</a>)</li> 
</ul>
                                        </div>
                                      
</div>
            