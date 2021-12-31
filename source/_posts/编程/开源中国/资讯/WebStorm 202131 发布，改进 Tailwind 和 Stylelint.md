
---
title: 'WebStorm 2021.3.1 发布，改进 Tailwind 和 Stylelint'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3967'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 07:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3967'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">WebStorm 2021.3.1，即 WebStorm 2021.3 的第一个错误修复更新已正式发布。它包含了大量的修复和改进，包括对 Tailwind CSS v3.0 的支持以及为组件和标签设置不同的颜色。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复 Tailwind CSS</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">WebStorm 2021.3.1 为 Tailwind CSS 提供了两个重要的修复 ——<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-53365" target="_blank">WEB-53365</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-53284" target="_blank">WEB-53284</a>。现在，Tailwind CSS 类的代码补全应按预期正常工作，并增加了对 v3.0 的支持。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">为组件和标签设置不同颜色</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">WebStorm 2021.3.1 增加了一个新的 Custom Tag Name（自定义标签名称）选项，允许为 Vue、React JSX 和 Angular 组件设置不同的颜色。这个新选项位于「首选项-设置-编辑器-颜色方案-HTML-XML」中。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">HTML 中补全建议的图标</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">对于 HTML，WebStorm 现在会在代码补全弹出窗口的建议旁边显示图标。根据不同的建议，你会看到实时模板、标签和单词的图标。希望这一变化能让你更容易区分不同种类的建议，这样你就能始终选择正确的建议。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">对 Stylelint 的改进</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Stylelint 现在只支持 CSS 文件，并要求你更新 .stylelintrc 文件以开启对其他文件类型的支持。如果你在默认设置下使用，每当你打开不是 .css 的文件时，WebStorm 都会显示一个错误。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">为了解决这个问题，WebStorm 2021.3.1 为文件字段引入了一个新的运行。你可以在「首选项-设置-语言和框架-样式表-Stylelint」中找到它。默认值是<span> </span><code>&#123;**/*,*&#125;.&#123;css&#125;</code>，Stylelint 14+ 默认只处理纯 CSS 文件。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他值得注意的改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改变了受信任项目功能的行为和实现</li> 
 <li>解决了 Angular 支持方面的一些问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-53447" target="_blank">WEB-53447</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-53688" target="_blank">WEB-53688</a> 和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-53723" target="_blank">WEB-53723</a>).</li> 
 <li>对于 Yarn PnP，现在应该对间接依赖关系进行索引 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-42178" target="_blank">WEB-42178</a>).</li> 
 <li>Vue 中现在支持 v-bind CSS 函数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-52425" target="_blank">WEB-52425</a>).</li> 
 <li>修正了在 macOS Big Sur 上导致对话框显示在错误窗口的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-263628" target="_blank">IDEA-263628</a>).</li> 
 <li>修正了在尝试调整工具窗口大小时，意外激活窗口拖放功能的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-274904" target="_blank">IDEA-274904</a>).</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fwebstorm%2F2021%2F12%2Fwebstorm-2021-3-1%2F" target="_blank">https://blog.jetbrains.com/webstorm/2021/12/webstorm-2021-3-1/</a></p>
                                        </div>
                                      
</div>
            