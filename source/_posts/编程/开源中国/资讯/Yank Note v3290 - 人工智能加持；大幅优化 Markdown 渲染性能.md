
---
title: 'Yank Note v3.29.0 - 人工智能加持；大幅优化 Markdown 渲染性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 09:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png'
---

<div>   
<div class="content">
                                                                                            <h2>应用介绍</h2> 
<p><span style="background-color:#ffffff; color:#24292f">Yank Note 是一款面向程序员的本地 Markdown 笔记应用。支持在文档中嵌入可运行的代码块、思维导图以及各种图形 (Drawio、Mermaid、Plantuml)，支持插件拓展、文档历史版本回溯。</span></p> 
<p style="color:#24292f; text-align:start">Yank Note 非常适合程序员群体，针对下面的场景具有和其他笔记工具不一样的体验：</p> 
<ol> 
 <li>做技术笔记：可直接在文档中运行代码块（天然支持 JS 代码，其他语言需配置环境），让笔记生动起来。</li> 
 <li>编写辅助工具：可在文档中嵌入 HTML 组件来制作一些辅助工具，甚至你可以使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurocean%2Fyn%2Fissues%2F65%23issuecomment-962472316" target="_blank">Markdown 遥控无人机</a><span> </span>:)</li> 
 <li>写技术方案和文章：支持嵌入多种图形（思维导图、Plantunl、Drawio、Mermaid 、ECharts ），写文档画图形一气呵成。</li> 
 <li>记录工作日志：支持任务代办列表，使用“宏替换”功能可以方便生成日报周报。</li> 
</ol> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png" referrerpolicy="no-referrer"></p> 
<hr> 
<h2>v3.29.0 更新记录</h2> 
<p><strong>本次更新亮点：</strong></p> 
<p>1. 增加 OpenAI 人工只能加持</p> 
<p>现在，你可以在设置中配置 OpenAI 接口，实现人工智能补全文字功能</p> 
<div class="ckeditor-html5-video" style="text-align:center"> 
 <video controls="controls" src="https://yank-note.vercel.app/openai.mp4">
   
 </video> 
</div> 
<p> </p> 
<p>2. 大幅优化 Markdown 渲染性能</p> 
<ul> 
 <li>重写了 markdown-it-attrs 插件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurocean%2Fmarkdown-it-attributes" target="_blank">性能提升 132 倍</a></li> 
 <li>优化 Mermaid 渲染性能</li> 
</ul> 
<p><strong>更新详情：</strong></p> 
<ol> 
 <li>feat: 增加 OpenAI 集成</li> 
 <li>feat: 编辑器支持折叠内容</li> 
 <li>feat: 点击大纲目录标题时候高亮对应标题</li> 
 <li>feat: 增加代理配置项</li> 
 <li>feat: 增加编辑器行号配置项</li> 
 <li>feat: 增加样式类<span> </span><code>avoid-page-break</code></li> 
 <li>upd: 优化 Markdown 渲染性能</li> 
 <li>upd: 增大预览最大宽度</li> 
 <li>fix: 修复嵌入 HTML 表格不能合并单元格问题</li> 
 <li>fix: 修复 Mermaid 图形可能有空白问题</li> 
 <li>fix: 修复自定义容器中脑图不能展示问题</li> 
 <li>feat(plugin): 支持添加配置分组</li> 
 <li>upd(plugin): 移除<span> </span><code>ctx.constant</code><span> </span>模块，使用<span> </span><code>ctx.args</code><span> </span>代替</li> 
 <li>upd(plugin): 移除<span> </span><code>ctx.editor.revealLineInCenter</code>,<span> </span><code>ctx.editor.revealLine</code>,<span> </span><code>ctx.editor.setScrollToTop</code><span> </span>方法</li> 
</ol>
                                        </div>
                                      
</div>
            