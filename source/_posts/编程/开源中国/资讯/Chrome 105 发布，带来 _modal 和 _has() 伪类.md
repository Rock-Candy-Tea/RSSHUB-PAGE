
---
title: 'Chrome 105 发布，带来 _modal 和 _has() 伪类'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9372'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9372'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Chrome 105 发布啦，这个版本带来了 25 个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeatures%23milestone%253D105" target="_blank">新特性</a>，以及 <span style="color:#121212">24 个已知的安全修复程序，</span>新特性如下：</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5452774595624960" target="_blank">脚本和样式表上的“blocking=rendering”属性</a></h3> 
<p>允许将 'blocking=render' 作为属性和值放入 <script>、<style> 或样式表 <link> 使其显式呈现阻塞。主要用途是避免由于例如插入脚本的脚本/样式表、客户端 A/B 测试等引起的无样式内容，或用户与不成熟页面的交互。</p> 
<h2 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5794378545102848" target="_blank">:has() 伪类</a></h2> 
<p style="margin-left:0px">:has() 伪类是一个选择器，它指定一个元素，该元素至少有一个与作为参数传递的相对选择器匹配的元素。:has 伪类提供了一种将样式规则应用于特定元素的前面元素（前面的兄弟姐妹/祖先/祖先的前面的兄弟姐妹）的方法。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F6627326972919808" target="_blank">添加 onbeforeinput 全局事件处理程序内容属性</a></h3> 
<p style="margin-left:0px">'beforeinput' 事件在 <input>、<textarea> 或 contenteditable 元素的值即将被修改时触发。添加一个 'onbeforeinput' 全局内容属性，使开发人员更容易使用。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5680188671655936" target="_blank">以 125 Hz 对齐计时器（包括 DOM 计时器）</a></h3> 
<p style="margin-left:0px">在常规的 8ms 对齐唤醒 (125 Hz) 上，以非零延迟运行所有计时器（除了少数例外），而不是在延迟过去后立即运行。这会影响 DOM 计时器；</p> 
<ul> 
 <li>在前台页面上，在常规的 8ms 对齐唤醒时，运行具有非零延迟的 DOM 计时器，而不是在延迟过去后立即运行。</li> 
 <li>在后台页面上，DOM 计时器已经在常规的 1 秒对齐唤醒 (1 Hz) 上运行，或者在 5 分钟后更频繁地运行。</li> 
</ul> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5192833009975296" target="_blank">CSS :modal 伪类</a></h3> 
<p style="margin-left:0px">用于设置对话框元素样式的伪类选择器。:modal 伪类表示一个元素，该元素处于排除与它之外的元素的所有交互的状态，直到它被解除。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5096490737860608" target="_blank">自定义标识符中不允许使用 CSS 默认关键字</a></h3> 
<p style="margin-left:0px">CSS 自定义标识符中不允许使用 CSS 关键字“default”，这些标识符用于 CSS 中许多类型的用户定义名称（例如，由 @keyframes 规则创建的名称、计数器、@container 名称、自定义布局或绘制名称）。</p> 
<p style="margin-left:0px">这会将“default”添加到保留用于自定义标识符的名称列表中，这些名称已经保留：“inherit”、“initial”、“unset”、“revert” 和 “revert-layer”。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F6525308435955712" target="_blank">容器查询</a></h3> 
<p style="margin-left:0px">容器查询允许作者根据容器元素的大小来设置元素的样式。它类似于@media 查询，不同之处在于它根据容器的大小而不是视口的大小进行评估。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5194856243134464" target="_blank">导航事件.scroll()</a></h3> 
<p style="margin-left:0px">scroll() 的工作方式与现有的 restoreScroll() 非常相似，只是它可以在导航不是遍历时调用。即使不在手动滚动模式下，它也允许手动执行滚动。</p> 
<h3 style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5274139738767360" target="_blank">fetch() 上传流</a></h3> 
<p style="margin-left:0px">获取上传流让 Web 开发人员可以使用 ReadableStream 主体进行获取。Fetch 提供了 Request 和 Response 对象（以及其他与网络请求有关的东西）的通用定义。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span style="color:var(--heading-color)"><span><span><span><span><span><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5166018807726080" target="_blank">手势滚动 DOM 事件</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p>Gesture Scroll DOM 事件，即“gesturescrollstart”、“gesturescrollupdate”和“gesturescrollend”，它们是非标准 API，被添加到 Blink 以用于插件。目前，此 API 并不适用于所有情况。它仅在有非合成滚动条时有效。</p> 
<p> </p> 
<p style="margin-left:0px">此外还有弃用 <span style="background-color:#ffffff; color:#121212">WebSQL 并从非安全上下文中删除等功能改动，</span>其他新功能可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Ffeatures%23milestone%253D105" target="_blank">特性页</a>查看。</p> 
<p style="margin-left:0px">安全修复可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromereleases.googleblog.com%2F2022%2F08%2Fstable-channel-update-for-desktop_30.html" target="_blank">Chrome 发布博客</a> 中查看。</p>
                                        </div>
                                      
</div>
            