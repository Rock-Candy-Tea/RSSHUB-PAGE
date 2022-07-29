
---
title: 'Yank Note v3.33.0：将整个文档显示为思维导图，增加 Markmap 扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 13:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left">应用介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">Yank Note 是一款面向程序员的本地 Markdown 笔记应用。支持在文档中嵌入可运行的代码块、思维导图以及各种图形 (Drawio、Mermaid、Plantuml)，支持插件拓展、文档历史版本回溯。</span></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Yank Note 非常适合程序员群体，针对下面的场景具有和其他笔记工具不一样的体验：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>做技术笔记：可直接在文档中运行代码块（天然支持 JS 代码，其他语言需配置环境），让笔记生动起来。</li> 
 <li>编写辅助工具：可在文档中嵌入 HTML 组件来制作一些辅助工具，甚至你可以使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurocean%2Fyn%2Fissues%2F65%23issuecomment-962472316" target="_blank">Markdown 遥控无人机</a><span> </span>:)</li> 
 <li>写技术方案和文章：支持嵌入多种图形（思维导图、Plantunl、Drawio、Mermaid 、ECharts ），写文档画图形一气呵成。</li> 
 <li>记录工作日志：支持任务代办列表，使用 “宏替换” 功能可以方便生成日报周报。</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-4be9cb15f4600be9cbb8db9dbeff408d7eb.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">v3.32.0 更新记录</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新亮点：</strong><span style="background-color:#ffffff; color:#24292f">扩展中心新增 “Markmap” 扩展，使用思维导图的方式查看 Markdown。感谢<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarkmap.js.org%2F" target="_blank">Markmap</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><img alt="image" src="https://user-images.githubusercontent.com/7115690/181574494-38730b79-ab11-4197-b0a3-5225ab72a5b0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">更新详情：</strong></p> 
<ol> 
 <li>fix: 修复打开文档字数统计信息不更新问题</li> 
 <li>fix: 修复切换文件时候 front matter 没刷新问题</li> 
 <li>upd: 导出 HTML 保留<span> </span><code>data-*</code><span> </span>属性</li> 
 <li>upd: 优化<span> </span><code>section</code><span> </span>容器样式</li> 
 <li>feat(plugin): 增加预览器注册，插件可以自定义文档预览界面。相关 Api:<span> </span><code>ctx.view.switchPreviewer</code><span> </span><code>ctx.view.registerPreviewer</code><span> </span><code>ctx.view.removePreviewer</code><span> </span><code>ctx.view.getAllPreviewers</code></li> 
</ol> 
<p> </p>
                                        </div>
                                      
</div>
            