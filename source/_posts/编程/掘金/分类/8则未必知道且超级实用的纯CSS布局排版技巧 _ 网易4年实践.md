
---
title: '8则未必知道且超级实用的纯CSS布局排版技巧 _ 网易4年实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9bd1820474c4d6a9e9b1f7c16746b9c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 21:18:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9bd1820474c4d6a9e9b1f7c16746b9c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<p>作者：<a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">JowayYoung</a><br>
仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJowayYoung" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JowayYoung" ref="nofollow noopener noreferrer">Github</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FJowayYoung" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/JowayYoung" ref="nofollow noopener noreferrer">CodePen</a><br>
博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">官网</a>、<a href="https://juejin.im/user/584ec3a661ff4b006cd6383e/posts" target="_blank" title="https://juejin.im/user/584ec3a661ff4b006cd6383e/posts">掘金</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fblog%2Fjowayyoung" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/blog/jowayyoung" ref="nofollow noopener noreferrer">思否</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fc_1169597485852360704" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/c_1169597485852360704" ref="nofollow noopener noreferrer">知乎</a><br>
公众号：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip%2Fstatic%2Ffrontend%2Faccount%2FIQ%25E5%2589%258D%25E7%25AB%25AF%25E5%2585%25AC%25E4%25BC%2597%25E5%258F%25B7.jpg" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip/static/frontend/account/IQ%E5%89%8D%E7%AB%AF%E5%85%AC%E4%BC%97%E5%8F%B7.jpg" ref="nofollow noopener noreferrer">IQ前端</a><br>
特别声明：原创不易，未经授权不得转载或抄袭，如需转载可联系笔者授权</p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p>最近有些读者悄悄发现了笔者的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">个人官网</a>，无一例外都使用<code>惊喜</code>、<code>惊叹</code>等词形容。没错，笔者使用大量CSS阐述了什么叫做<a href="https://juejin.cn/book/6850413616484040711" target="_blank" title="https://juejin.cn/book/6850413616484040711">玩转CSS的艺术之美</a>。即使某些应用场景缺少JS的加持，笔者也能将CSS玩得游刃有余，整个网站源码里CSS大概占据<code>60%</code>的分量，很多效果不是为了炫技而是想告诉大家CSS的重要性与实用性。因此笔者想通过本文分享一些大家未必知道且超级实用的<strong>纯CSS布局排版技巧</strong>实现一些<code>常见或特殊的布局排版</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9bd1820474c4d6a9e9b1f7c16746b9c~tplv-k3u1fbpfcp-watermark.image" alt="个人官网" loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发每一张网页都离不开<code>布局排版</code>，基于良好<code>布局排版</code>打下基础，才能使后续的开发更顺利。当然不能停留在<code>IExplorer</code>时代那种局限思维上，没办法解决的<code>布局排版</code>都用JS实现😂。今时不同往日，现代CSS属性能更好地快速实现各种<code>布局排版</code>，节约更多时间去摸鱼😉。</p>
<p>不过按照笔者目前了解的情况来看，大部分同学即使在无需兼容<code>IExplorer</code>的情况下还是遵循<code>CSS+JS</code>的方式完成一些<code>常见或特殊的布局排版</code>。从<code>HTML/CSS/JS</code>前端三剑客的定位来看，<code>HTML</code>映射网页的<strong>结构</strong>，<code>CSS</code>映射网页的<strong>表现</strong>，<code>JS</code>映射网页的<strong>行为</strong>。</p>
<p><strong>布局排版</strong>指将图形、文本、图像、媒体等可视化信息元素在页面布局上调整<code>位置</code>、<code>尺寸</code>等属性使页面布局变得条理化的过程。大部分同学认为<code>布局排版</code>就是几个合理的CSS属性随便拼凑在一起，但多数情况即使实现也会存在瑕疵，此时就可能使用JS介入。</p>
<p>从<code>布局排版</code>的特征可知它属于<code>表现</code>范畴，因此笔者认为大部分<code>布局排版</code>都能使用<code>纯CSS</code>完成，无需JS介入。</p>
<p>本文秉承<strong>能使用CSS实现的效果都优先使用CSS</strong>的原则，为大家讲解笔者如何巧妙运用各种纯CSS开发技巧完成一些<code>常见或特殊的布局排版</code>。因此笔者建议大家认真看一遍以下内容，绝对让你有所收货和惊喜。</p>
<p>若对CSS无特别想法，建议体验以下网站，相信你会认真踏实地阅读本文。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">个人官网</a>：暂时支持<code>PC端</code>浏览，拒绝支持<code>IExplorer</code></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">特效专辑</a>：暂时支持<code>PC端</code>浏览，拒绝支持<code>IExplorer</code></li>
</ul>
<h3 data-id="heading-1">属性</h3>
<p>在进入主题前，笔者总结出<code>布局排版</code>一些必备属性，这些属性能快速搭建整体效果，再通过一些常用选择器加以修饰达到完美效果。看似简单，但使用起来不一定完全驾驭。</p>
<p>必备属性都是一些几何属性，主要用于声明<code>位置</code>和<code>尺寸</code>。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>浮动布局</strong>：<code>float</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>定位布局</strong>：<code>position/left/right/top/bottom/z-index</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>弹性布局</strong>：<code>display:flex/inline-flex</code>、<code>flex系列属性</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>盒子模型</strong>：<code>box-sizing/margin/padding/border/width/height</code></li>
</ul>
<p>选择器因<code>CSS模块</code>众多而派生出的数量也众多，若无特别方式记熟这些选择器对应的功能，也很难将其发挥到最大作用。</p>
<p>笔者根据选择器的功能划分出八大类，每个类别的选择器都能在一个应用场景里互相组合，记熟这些类别的选择器，相信就能将选择器发挥到最大作用，也能游刃有余将其应用到一些<code>常见或特殊的布局排版</code>里。</p>
<p><code>布局排版</code>可能只应用到某些选择器，但也不妨碍大家通过以下归类方式记忆。选择器作为CSS的重要组成部分，比起属性组合会有更多的玩法。</p>
<blockquote>
<p>基础选择器</p>
</blockquote>








































<table><thead><tr><th align="center">选择器</th><th align="center">别名</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>tag</code></td><td align="center">标签选择器</td><td>指定类型的<code>标签</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>#id</code></td><td align="center">ID选择器</td><td>指定身份的<code>标签</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>.class</code></td><td align="center">类选择器</td><td>指定类名的<code>标签</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>*</code></td><td align="center">通配选择器</td><td>所有类型的<code>标签</code></td><td align="center">2</td><td align="center">√</td></tr></tbody></table>
<blockquote>
<p>层次选择器</p>
</blockquote>








































<table><thead><tr><th align="center">选择器</th><th align="center">别名</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>elemP elemC</code></td><td align="center"><code>后代选择器</code></td><td>元素的<code>后代元素</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>elemP>elemC</code></td><td align="center"><code>子代选择器</code></td><td>元素的<code>子代元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>elem1+elem2</code></td><td align="center"><code>相邻同胞选择器</code></td><td>元素相邻的<code>同胞元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>elem1~elem2</code></td><td align="center"><code>通用同胞选择器</code></td><td>元素后面的<code>同胞元素</code></td><td align="center">3</td><td align="center">√</td></tr></tbody></table>
<blockquote>
<p>集合选择器</p>
</blockquote>


























<table><thead><tr><th align="center">选择器</th><th align="center">别名</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>elem1,elem2</code></td><td align="center"><code>并集选择器</code></td><td>多个指定的<code>元素</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>elem.class</code></td><td align="center"><code>交集选择器</code></td><td>指定类名的<code>元素</code></td><td align="center">1</td><td align="center">√</td></tr></tbody></table>
<blockquote>
<p>条件选择器</p>
</blockquote>

































































<table><thead><tr><th align="center">选择器</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>:lang</code></td><td>指定标记语言的<code>元素</code></td><td align="center">2</td><td align="center">×</td></tr><tr><td align="center"><code>:dir()</code></td><td>指定编写方向的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:has</code></td><td>包含指定元素的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:is</code></td><td>指定条件的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:not</code></td><td>非指定条件的<code>元素</code></td><td align="center">4</td><td align="center">√</td></tr><tr><td align="center"><code>:where</code></td><td>指定条件的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:scope</code></td><td>指定<code>元素</code>作为参考点</td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:any-link</code></td><td>所有包含<code>href</code>的<code>链接元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:local-link</code></td><td>所有包含<code>href</code>且属于绝对地址的<code>链接元素</code></td><td align="center">4</td><td align="center">×</td></tr></tbody></table>
<blockquote>
<p>状态选择器</p>
</blockquote>

























































































































































































<table><thead><tr><th align="center">选择器</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>:active</code></td><td>鼠标激活的<code>元素</code></td><td align="center">1</td><td align="center">×</td></tr><tr><td align="center"><code>:hover</code></td><td>鼠标悬浮的<code>元素</code></td><td align="center">1</td><td align="center">√</td></tr><tr><td align="center"><code>:link</code></td><td>未访问的<code>链接元素</code></td><td align="center">1</td><td align="center">×</td></tr><tr><td align="center"><code>:visited</code></td><td>已访问的<code>链接元素</code></td><td align="center">1</td><td align="center">×</td></tr><tr><td align="center"><code>:target</code></td><td>当前锚点的<code>元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:focus</code></td><td>输入聚焦的<code>表单元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>:required</code></td><td>输入必填的<code>表单元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:valid</code></td><td>输入合法的<code>表单元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:invalid</code></td><td>输入非法的<code>表单元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:in-range</code></td><td>输入范围以内的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:out-of-range</code></td><td>输入范围以外的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:checked</code></td><td>选项选中的<code>表单元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:optional</code></td><td>选项可选的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:enabled</code></td><td>事件启用的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:disabled</code></td><td>事件禁用的<code>表单元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:read-only</code></td><td>只读的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:read-write</code></td><td>可读可写的<code>表单元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:target-within</code></td><td>内部锚点元素处于激活状态的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:focus-within</code></td><td>内部表单元素处于聚焦状态的<code>元素</code></td><td align="center">4</td><td align="center">√</td></tr><tr><td align="center"><code>:focus-visible</code></td><td>输入聚焦的<code>表单元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:blank</code></td><td>输入为空的<code>表单元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:user-invalid</code></td><td>输入合法的<code>表单元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:indeterminate</code></td><td>选项未定的<code>表单元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:placeholder-shown</code></td><td>占位显示的<code>表单元素</code></td><td align="center">4</td><td align="center">√</td></tr><tr><td align="center"><code>:current()</code></td><td>浏览中的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:past()</code></td><td>已浏览的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:future()</code></td><td>未浏览的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:playing</code></td><td>开始播放的<code>媒体元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>:paused</code></td><td>暂停播放的<code>媒体元素</code></td><td align="center">4</td><td align="center">×</td></tr></tbody></table>
<blockquote>
<p>结构选择器</p>
</blockquote>



















































































<table><thead><tr><th align="center">选择器</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>:root</code></td><td>文档的<code>根元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:empty</code></td><td>无子元素的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:nth-child(n)</code></td><td>元素中指定顺序索引的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:nth-last-child(n)</code></td><td>元素中指定逆序索引的<code>元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:first-child</code></td><td>元素中为首的<code>元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>:last-child</code></td><td>元素中为尾的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:only-child</code></td><td>父元素仅有该元素的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:nth-of-type(n)</code></td><td>标签中指定顺序索引的<code>标签</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:nth-last-of-type(n)</code></td><td>标签中指定逆序索引的<code>标签</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>:first-of-type</code></td><td>标签中为首的<code>标签</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:last-of-type</code></td><td>标签中为尾<code>标签</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>:only-of-type</code></td><td>父元素仅有该标签的<code>标签</code></td><td align="center">3</td><td align="center">√</td></tr></tbody></table>
<blockquote>
<p>属性选择器</p>
</blockquote>





















































<table><thead><tr><th align="center">选择器</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>[attr]</code></td><td>指定属性的<code>元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>[attr=val]</code></td><td>属性等于指定值的<code>元素</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>[attr*=val]</code></td><td>属性包含指定值的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>[attr^=val]</code></td><td>属性以指定值开头的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>[attr$=val]</code></td><td>属性以指定值结尾的<code>元素</code></td><td align="center">3</td><td align="center">√</td></tr><tr><td align="center"><code>[attr~=val]</code></td><td>属性包含指定值(完整单词)的<code>元素</code>(不推荐使用)</td><td align="center">2</td><td align="center">×</td></tr><tr><td align="center"><code>[attr|=val]</code></td><td>属性以指定值(完整单词)开头的<code>元素</code>(不推荐使用)</td><td align="center">2</td><td align="center">×</td></tr></tbody></table>
<blockquote>
<p>伪元素</p>
</blockquote>





















































<table><thead><tr><th align="center">选择器</th><th>说明</th><th align="center">版本</th><th align="center">常用</th></tr></thead><tbody><tr><td align="center"><code>::before</code></td><td>在元素前插入的<code>内容</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>::after</code></td><td>在元素后插入的<code>内容</code></td><td align="center">2</td><td align="center">√</td></tr><tr><td align="center"><code>::first-letter</code></td><td>元素的<code>首字母</code></td><td align="center">1</td><td align="center">×</td></tr><tr><td align="center"><code>::first-line</code></td><td>元素的<code>首行</code></td><td align="center">1</td><td align="center">×</td></tr><tr><td align="center"><code>::selection</code></td><td>鼠标选中的<code>元素</code></td><td align="center">3</td><td align="center">×</td></tr><tr><td align="center"><code>::backdrop</code></td><td>全屏模式的<code>元素</code></td><td align="center">4</td><td align="center">×</td></tr><tr><td align="center"><code>::placeholder</code></td><td>表单元素的<code>占位</code></td><td align="center">4</td><td align="center">√</td></tr></tbody></table>
<h3 data-id="heading-2">技巧</h3>
<p>有了上述前置知识，接下来跟着笔者体验一次如何巧妙运用各种纯CSS开发技巧完成一些<code>常见或特殊的布局排版</code>吧。为了方便浏览器自动计算某些样式，需全局设置<code>box-sizing:border-box</code>，编码前请引入笔者整理的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJowayYoung%2Fidea-css%2Fblob%2Fmaster%2Ficss%2Fsrc%2Fassets%2Fcss%2Freset.css" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JowayYoung/idea-css/blob/master/icss/src/assets/css/reset.css" ref="nofollow noopener noreferrer">reset.css</a>。</p>
<h4 data-id="heading-3">主体布局</h4>
<p><strong>主体布局</strong>指在大部分情况下通用且具备统一特征的占位布局。掌握<code>主体布局</code>是一个前端必不可少的技能，养成看设计图就能大概规划出整体布局的前提是必须熟悉这些<code>主体布局</code>的特点与构造。</p>
<h6 data-id="heading-4">全屏布局</h6>
<p>经典的<strong>全屏布局</strong>由<code>顶部</code>、<code>底部</code>和<code>主体</code>三部分组成，其特点为<code>三部分左右满屏拉伸</code>、<code>顶部底部高度固定</code>和<code>主体高度自适应</code>。该布局很常见，也是大部分Web应用主体的主流布局。通常使用<code><header></code>、<code><footer></code>和<code><main></code>三个标签语义化排版，<code><main></code>内还可插入<code><aside></code>侧栏或其他语义化标签。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b027069fdce54c128813d3886eef59a6~tplv-k3u1fbpfcp-watermark.image" alt="全屏布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fullscreen-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">header</span>></span><span class="hljs-tag"></<span class="hljs-name">header</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">main</span>></span><span class="hljs-tag"></<span class="hljs-name">main</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">footer</span>></span><span class="hljs-tag"></<span class="hljs-name">footer</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>position + left/right/top/bottom</p>
</blockquote>
<p>三部分统一声明<code>left:0</code>和<code>right:0</code>将其左右满屏拉伸；顶部和底部分别声明<code>top:0</code>和<code>bottom:0</code>将其吸顶和吸底，并声明俩高度为固定值；将主体的<code>top</code>和<code>bottom</code>分别声明为顶部高度和底部高度。通过绝对定位的方式将三部分固定在特定位置，使其互不影响。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.fullscreen-layout</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-tag">header</span>,
    <span class="hljs-selector-tag">footer</span>,
    <span class="hljs-selector-tag">main</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">header</span> &#123;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-tag">footer</span> &#123;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-tag">main</span> &#123;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>flex</p>
</blockquote>
<p>使用<code>flex</code>实现会更简洁。<code>display:flex</code>默认会令子节点横向排列，需声明<code>flex-direction:column</code>改变子节点排列方向为纵向排列；顶部和底部高度固定，所以主体需声明<code>flex:1</code>让高度自适应。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.fullscreen-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-direction</span>: column;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-tag">header</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-tag">footer</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-tag">main</span> &#123;
        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若<code><main></code>需表现成可滚动状态，千万不要声明<code>overflow:auto</code>让容器自适应滚动，这样做有可能因为其他格式化上下文的影响而导致自适应滚动失效或产生其他未知效果。需在<code><main></code>内插入一个<code><div></code>并声明如下。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">两列布局</h6>
<p>经典的<strong>两列布局</strong>由<code>左右两列</code>组成，其特点为<code>一列宽度固定</code>、<code>另一列宽度自适应</code>和<code>两列高度固定且相等</code>。以下以左列宽度固定和右列宽度自适应为例，反之同理。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12f7992b853b4762b058be3407576606~tplv-k3u1fbpfcp-watermark.image" alt="两列布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two-column-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>float + margin-left/right</p>
</blockquote>
<p>左列声明<code>float:left</code>和固定宽度，由于<code>float</code>使节点脱流，右列需声明<code>margin-left</code>为左列宽度，以保证两列不会重叠。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.two-column-layout</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>overflow + float</p>
</blockquote>
<p>左列声明同上，右列声明<code>overflow:hidden</code>使其形成<code>BFC区域</code>与外界隔离。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.two-column-layout</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>flex</p>
</blockquote>
<p>使用<code>flex</code>实现会更简洁。左列声明固定宽度，右列声明<code>flex:1</code>自适应宽度。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.two-column-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">三列布局</h6>
<p>经典的<strong>三列布局</strong>由<code>左中右三列</code>组成，其特点为<code>连续两列宽度固定</code>、<code>剩余一列宽度自适应</code>和<code>三列高度固定且相等</code>。以下以左中列宽度固定和右列宽度自适应为例，反之同理。整体的实现原理与上述两列布局一致。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892ab25b75894be082eac171dc6c780c~tplv-k3u1fbpfcp-watermark.image" alt="三列布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"three-column-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了让右列宽度自适应计算，就不使用<code>float + margin-left</code>的方式了，若使用<code>margin-left</code>还得结合左中列宽度计算。</p>
<blockquote>
<p>overflow + float</p>
</blockquote>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.three-column-layout</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.center</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>flex</p>
</blockquote>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.three-column-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.center</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">圣杯布局/双飞翼布局</h6>
<p>经典的<strong>圣杯布局</strong>和<strong>双飞翼布局</strong>都是由<code>左中右三列</code>组成，其特点为<code>左右两列宽度固定</code>、<code>中间一列宽度自适应</code>和<code>三列高度固定且相等</code>。其实也是上述两列布局和三列布局的变体，整体的实现原理与上述N列布局一致，可能就是一些细节需注意。</p>
<p><code>圣杯布局</code>和<code>双飞翼布局</code>在大体相同下也存在一点不同，区别在于<code>双飞翼布局</code>中间列需插入一个子节点。在常规实现方式里也是在这个中间列里做文章，<code>如何使中间列内容不被左右列遮挡</code>。</p>
<ul>
<li>相同
<ul>
<li>中间列放首位且声明其宽高占满父节点</li>
<li>被挤出的左右列使用<code>float</code>和<code>margin负值</code>将其拉回与中间列处在同一水平线上</li>
</ul>
</li>
<li>不同
<ul>
<li>圣杯布局：父节点声明<code>padding</code>为左右列留出空位，将左右列固定在空位上</li>
<li>双飞翼布局：中间列插入子节点并声明<code>margin</code>为左右列让出空位，将左右列固定在空位上</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dc38beabb574eff98e18497189cf66f~tplv-k3u1fbpfcp-watermark.image" alt="圣杯布局" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>圣杯布局float + margin-left/right + padding-left/right</p>
</blockquote>
<p>由于浮动节点在位置上不能高于前面或平级的非浮动节点，否则会导致浮动节点下沉。因此在编写HTML结构时，将中间列节点挪到右列节点后面。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grail-layout-x"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grail-layout-x</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">float</span>: right;
        <span class="hljs-attribute">margin-right</span>: -<span class="hljs-number">100px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-class">.center</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>双飞翼布局float + margin-left/right</p>
</blockquote>
<p>HTML结构大体同上，只是在中间列里插入一个子节点<code><div></code>。根据两者区别，CSS声明会与上述圣杯布局有一点点出入，可观察对比找出不同地方。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grail-layout-y"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grail-layout-y</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">float</span>: right;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
    <span class="hljs-selector-class">.center</span> &#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>圣杯布局/双飞翼布局flex</p>
</blockquote>
<p>使用flex实现<code>圣杯布局/双飞翼布局</code>可忽略上述分析，左右两列宽度固定，中间列宽度自适应。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grail-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grail-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-class">.left</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.center</span> &#123;
        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
    <span class="hljs-selector-class">.right</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">均分布局</h6>
<p>经典的<strong>均分布局</strong>由<code>多列</code>组成，其特点为<code>每列宽度相等</code>和<code>每列高度固定且相等</code>。总体来说也是最简单的经典布局，由于每列宽度相等，所以很易找到合适的方式处理。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cd0dec75a784851a94454184bd85625~tplv-k3u1fbpfcp-watermark.image" alt="均分布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"average-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"one"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"two"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"three"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"four"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.one</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
&#125;
<span class="hljs-selector-class">.two</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
&#125;
<span class="hljs-selector-class">.three</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f90</span>;
&#125;
<span class="hljs-selector-class">.four</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#09f</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>float + width</p>
</blockquote>
<p>每列宽度声明为相等的百分比，若有4列则声明<code>width:25%</code>。N列就用公式<code>100 / n</code>求出最终百分比宽度，记得保留2位小数，懒人还可用<code>width:calc(100% / n)</code>自动计算呢。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.average-layout</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">float</span>: left;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">25%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>flex</p>
</blockquote>
<p>使用flex实现会更简洁。节点声明<code>display:flex</code>后，生成的<code>FFC容器</code>里所有子节点的高度都相等，因为容器的<code>align-items</code>默认为<code>stretch</code>，所有子节点将占满整个容器的高度。每列声明<code>flex:1</code>自适应宽度。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.average-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">居中布局</h6>
<p><strong>居中布局</strong>由<code>父容器</code>与<code>若干个子容器</code>组成，子容器在父容器中横向排列或竖向排列且呈水平居中或垂直居中。居中布局是一个很经典的问题，相信大家都会经常遇到。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f5311497f6b413e8418a14d45f812d7~tplv-k3u1fbpfcp-watermark.image" alt="居中布局" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在此直接上一个目前最简单最高效的居中方式。<code>display:flex</code>与<code>margin:auto</code>的强行组合，同学们自行体会。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"center-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.center-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">margin</span>: auto;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">自适布局</h4>
<p><strong>自适布局</strong>指相对视窗任何尺寸都能占据特定百分比的占位布局。<code>自适布局</code>的容器都是根据视窗尺寸计算，即使<code>父节点</code>或<code>祖先节点</code>的尺寸发生变化也不会影响<code>自适布局</code>的容器尺寸。</p>
<p>搭建<code>自适布局</code>就离不开<strong>视窗比例单位</strong>。在CSS3里增加了与<code>viewport</code>相关的四个长度单位，随着时间推移，目前大部分浏览器对这四个长度单位都有较好的兼容性，这也是未来最建议在伸缩方案里使用的长度单位。</p>
<ul>
<li><code>1vw</code>表示<code>1%</code>视窗宽度</li>
<li><code>1vh</code>表示<code>1%</code>视窗高度</li>
<li><code>1vmin</code>表示<code>1%</code>视窗宽度和<code>1%</code>视窗高度里最小者</li>
<li><code>1vmax</code>表示<code>1%</code>视窗宽度和<code>1%</code>视窗高度里最大者</li>
</ul>
<p>视窗宽高在JS里分别对应<code>window.innerWdith</code>和<code>window.innerHeight</code>。若不考虑低版本浏览器兼容性，完全可用一行CSS代码秒杀所有移动端的伸缩方案。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 基于UI width=750px DPR=2的网页 */</span>
<span class="hljs-selector-tag">html</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vw</span> / <span class="hljs-number">7.5</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码使用<code>calc()</code>实现<code>font-size</code>的动态计算。<code>calc()</code>是<code>自适布局</code>里的核心存在，无它就不能愉快地实现<code>自适布局</code>所有动态计算了。</p>
<p><code>calc()</code>用于动态计算单位，<code>数值</code>、<code>长度</code>、<code>角度</code>、<code>时间</code>和<code>百分比</code>都能作为参数。由于执行<code>数学表达式</code>后返回运算后的计算值，所以可减少大量人工计算甚至无需人工计算。</p>
<p><code>calc()</code>饥不择食，所有计量单位都能作为参数参加整个动态计算。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>数值</strong>：<code>整数</code>、<code>浮点数</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>长度</strong>：<code>px</code>、<code>em</code>、<code>rem</code>、<code>vw</code>、<code>vh</code>等</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>角度</strong>：<code>deg</code>、<code>turn</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>时间</strong>：<code>s</code>、<code>ms</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>百分比</strong>：<code>%</code></li>
</ul>
<p><code>calc()</code>虽然好用，但新手难免会遇到一些坑，谨记以下特点，相信就能玩转<code>calc()</code>了。</p>
<ul>
<li>四则运算：只能使用<code>+</code>、<code>-</code>、<code>*</code>、<code>/</code>作为运算符号</li>
<li>运算顺序：遵循加减乘除运算顺序，可用<code>()</code>提升运算等级</li>
<li>符号连接：每个运算符号必须使用<code>空格</code>间隔起来</li>
<li>混合计算：可混合不同计量单位动态计算</li>
</ul>
<p>第三点尤为重要，若未能遵守，浏览器直接忽略该属性。</p>
<p>上述<code>font-size:calc(100vw / 7.5)</code>其实就是根据设计图与浏览器视窗的比例动态计算<code><html></code>的<code>font-size</code>：<code>100/750 = x/100vw</code>。</p>
<p>在SPA里有遇过因为有滚动条或无滚动条而导致页面路由在跳转过程里发生向左或向右的抖动吗？这让强迫症患者很难受，此时可用<code>calc()</code>巧妙解决该问题。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.elem</span> &#123;
    <span class="hljs-attribute">padding-right</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vw</span> - <span class="hljs-number">100%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不直接声明<code>padding-right</code>为滚动条宽度是因为每个浏览器的默认滚动条宽度都可能不一致。<code>100vw</code>是视窗宽度，<code>100%</code>内容宽度，那么<code>100vw - 100%</code>就是滚动条宽度，声明<code>padding-right</code>用于保留滚动条出现的位置，这样滚动条出不出现都不会让页面抖动了。</p>
<p>有了<code>calc()</code>做保障就可迅速实现一些与视窗尺寸相关的布局了。例如实现一个视窗宽度都为<code>50%</code>的弹窗。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2901b6e762a1460e8ade015ae042c608~tplv-k3u1fbpfcp-watermark.image" alt="自适布局-弹窗" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-wrapper"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.modal</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">background-color</span>: rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">5</span>);
    &-wrapper &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">50vw</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然使用<code>calc()</code>也不一定结合<code>视窗比例单位</code>计算。例如<code>自适布局</code>已知部分节点高度，不想手动计算最后节点高度但又想其填充布局剩余空间。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c04746663a5b4f0eba435406bf427b78~tplv-k3u1fbpfcp-watermark.image" alt="自适布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"selfadaption-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.selfadaption-layout</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">567px</span>;
    <span class="hljs-selector-class">.box-1</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">123px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    &#125;
    <span class="hljs-selector-class">.box-2</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">15%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    &#125;
    <span class="hljs-selector-class">.box-3</span> &#123;
        <span class="hljs-attribute">height</span>: calc(<span class="hljs-number">100%</span> - <span class="hljs-number">123px</span> - <span class="hljs-number">15%</span>);
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#09f</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">吸附布局</h4>
<p><strong>吸附布局</strong>指相对视窗任何滚动都能占据特定位置的占位布局。视窗滚动到特定位置，布局固定在该位置，后续不随视窗滚动而滚动。该布局产生的效果俗称<code>吸附效果</code>，是一种常见网页效果。譬如<code>吸顶效果</code>和<code>吸底效果</code>都是该范畴，经常在<code>跟随导航</code>、<code>移动广告</code>和<code>悬浮提示</code>等应用场景里出现。</p>
<p>在<code>jQuery时代</code>就有很多吸附效果插件，现在三大前端框架也有自身第三方的吸附效果组件。它们都有着共通的实现原理：监听<code>scroll</code>事件，判断<code>scrollTop</code>和<code>目标节点</code>的位置范围，符合条件则将<code>目标节点</code>的<code>position</code>声明为<code>fixed</code>使<code>目标节点</code>相对于视窗定位，让用户看上去就像钉在视窗指定位置上。</p>
<p>JS实现吸附效果的代码在网上一搜一大堆，更何况笔者喜欢耍CSS，在此就不贴相关的JS代码了。在此推荐一个很少见很少用的CSS属性<code>position:sticky</code>。简单的<strong>两行核心CSS代码</strong>就能完成<strong>十多行核心JS代码</strong>的功能，何乐而不为呢。</p>
<p>简单回顾<code>position</code>属性值，怎样用就不说了，大家应该都熟悉。</p>








































<table><thead><tr><th align="center">取值</th><th align="center">功能</th><th align="center">版本</th></tr></thead><tbody><tr><td align="center"><strong>inherit</strong></td><td align="center"><code>继承</code></td><td align="center">2</td></tr><tr><td align="center"><strong>static</strong></td><td align="center"><code>标准流</code></td><td align="center">2</td></tr><tr><td align="center"><strong>relative</strong></td><td align="center"><code>相对定位</code></td><td align="center">2</td></tr><tr><td align="center"><strong>absolute</strong></td><td align="center"><code>绝对定位</code></td><td align="center">2</td></tr><tr><td align="center"><strong>fixed</strong></td><td align="center"><code>固定定位</code></td><td align="center">2</td></tr><tr><td align="center"><strong>sticky</strong></td><td align="center"><code>粘性定位</code></td><td align="center">3</td></tr></tbody></table>
<p>当值为<code>sticky</code>时将节点变成<code>粘性定位</code>。<strong>粘性定位</strong>是<code>相对定位</code>和<code>固定定位</code>的结合体，节点在<code>特定阈值</code>跨越前为<code>相对定位</code>，跨越后为<code>固定定位</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c183ad26a1e54aecb5fe2e97e94e54a6~tplv-k3u1fbpfcp-watermark.image" alt="吸附布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"adsorption-position"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Top 1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Top 2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Bottom 1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Bottom 2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.adsorption-position</span> &#123;
    <span class="hljs-attribute">overflow</span>: auto;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">280px</span>;
    <span class="hljs-attribute">outline</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#3c9</span>;
    <span class="hljs-selector-tag">ul</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">200px</span> <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">position</span>: sticky;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">40px</span>;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f90</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#09f</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">5</span>) &#123;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">40px</span>;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两行核心CSS代码分别是<code>position:sticky</code>和<code>top/bottom:npx</code>。上述5个节点都声明<code>position:sticky</code>，但由于<code>top/bottom</code>赋值有所不同就产生不同吸附效果。</p>
<p>细心的同学可能发现这些节点在<code>某些滚动时刻处于相对定位，在特定滚动时刻处于固定定位</code>。</p>
<ul>
<li>第1个<code><li></code>：<code>top</code>为<code>0px</code>，滚动到<code>容器顶部</code>就固定</li>
<li>第2个<code><li></code>：<code>top</code>为<code>40px</code>，滚动到<code>距离容器顶部40px</code>就固定</li>
<li>第3个<code><li></code>：未声明<code>top/bottom</code>，就一直保持相对定位</li>
<li>第4个<code><li></code>：<code>bottom</code>为<code>40px</code>，滚动到<code>距离容器底部40px</code>就固定</li>
<li>第5个<code><li></code>：<code>bottom</code>为<code>0px</code>，滚动到<code>容器底部</code>就固定</li>
</ul>
<p>当然，换成<code>left</code>或<code>right</code>也一样能实现横向的<code>吸附效果</code>。</p>
<p>值得注意，<code>粘性定位</code>的参照物并不一定是<code>position:fixed</code>。当<code>目标节点</code>的任意<code>祖先节点</code>都未声明<code>position:relative|absolute|fixed|sticky</code>，才与<code>position:fixed</code>表现一致。当离<code>目标节点</code>最近的<code>祖先节点</code>声明<code>position:relative|absolute|fixed|sticky</code>，<code>目标节点</code>就相对该<code>祖先节点</code>产生<code>粘性定位</code>。简单来说确认参照物的方式与<code>position:absolute</code>一致。</p>
<p>兼容性勉强还行，近2年发版的浏览器都能支持，<code>Safari</code>和<code>Firefox</code>的兼容性还是挺赞的。有<code>吸附效果</code>需求的同学建议一试，要兼容<code>IExplorer</code>就算了。期待该属性有更好的发展，毕竟<code>吸附布局</code>真的是一种常见布局。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c83b8f97ae764f7780dd293699927cec~tplv-k3u1fbpfcp-zoom-1.image" alt="吸附布局-sticky兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">横向布局</h4>
<p><strong>横向布局</strong>指容器内节点以水平方向排列且溢出部分被隐藏的占位布局。<code>竖向布局</code>很常见，声明<code>overflow:hidden;width:xpx;height:ypx</code>就能实现，但<code>横向布局</code>却不能使用类似方式实现。</p>
<p>为了方便使用多种方式实现<code>横向布局</code>，以下将通用代码拆分出来。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c911a4ee6410451fb0004daf1fa24336~tplv-k3u1fbpfcp-watermark.image" alt="横向布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"horizontal-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Alibaba<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Tencent<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Baidu<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Jingdong<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Ant<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Netease<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Meituan<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>ByteDance<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>360<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Sina<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.horizontal-layout</span> &#123;
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-selector-tag">ul</span> &#123;
        <span class="hljs-attribute">overflow-x</span>: auto;
        <span class="hljs-attribute">cursor</span>: pointer;
        &::-webkit-scrollbar &#123;
            height: <span class="hljs-number">10px</span>;
        &#125;
        &::-webkit-scrollbar-track &#123;
            background-color: <span class="hljs-number">#f0f0f0</span>;
        &#125;
        &::-webkit-scrollbar-thumb &#123;
            border-radius: <span class="hljs-number">5px</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
        &#125;
    &#125;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">90px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">90px</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        &<span class="hljs-selector-pseudo">:not</span>(:first-child) &#123;
            <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有些同学可能会使用<code>行内元素</code>实现横向排版，但必须声明<code>overflow-y:hidden</code>使容器在<code>Y轴</code>方向隐藏溢出部分。由于<code>行内元素</code>在当前行排版产生溢出会自动将其余节点排版到下一行，因此还需声明<code>white-space:nowrap</code>使所有<code>行内元素</code>在一行内排版完毕。若产生滚动条，还需对容器的<code>height</code>做适当的微调。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.horizontal-layout</span><span class="hljs-selector-class">.inline</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">102px</span>;
    <span class="hljs-selector-tag">ul</span> &#123;
        <span class="hljs-attribute">overflow-y</span>: hidden;
        <span class="hljs-attribute">white-space</span>: nowrap;
    &#125;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">display</span>: inline-block;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">90px</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述方式在笔者在开发认知里觉得太繁琐，实质上将所有节点当成文本排列，也是醉了。笔者推荐使用<code>flex布局</code>完成上述布局，<code>flex布局</code>作为目前最常见的<code>布局方式</code>，相信也不用笔者多说。以下实现方式不知大家是否见过呢？在移动端上体验会更棒喔！</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.horizontal-layout</span><span class="hljs-selector-class">.flex</span> &#123;
    <span class="hljs-selector-tag">ul</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">flex-wrap</span>: nowrap;
        <span class="hljs-attribute">justify-content</span>: space-between;
    &#125;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">flex-basis</span>: <span class="hljs-number">90px</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">凸显布局</h4>
<p><strong>凸显布局</strong>指容器内节点以同一方向排列且存在一个节点在某个方向上较突出的占位布局。该布局描述起来可能比较拗口，直接看以下效果吧，这是一个横向列表，节点从左往右排列，最右边的节点特别突出。这就是<code>凸显布局</code>的特征，凸显的节点可在<code>凸显布局</code>任意位置，<code>上下左右</code>，<code>左上左下右上右下</code>都行。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4536a34ddf934529bd6ef2a85340ddac~tplv-k3u1fbpfcp-watermark.image" alt="凸显布局" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里巧妙运用<code>margin-*:auto</code>实现了<code>凸显布局</code>。相信大家实现水平居中固定宽度的<code>块元素</code>都会使用<code>margin:0 auto</code>。</p>
<p>在此同样原理，当节点声明<code>margin-*:auto</code>时，浏览器会自动计算剩余空间并将该值赋值给该节点。在使用该技巧时必须基于<code>flex布局</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6a08424d17047e7bc2ee958281cfd08~tplv-k3u1fbpfcp-watermark.image" alt="凸显布局-左重右轻" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b8e6c412dc45cb8b26d26e29dfee5b~tplv-k3u1fbpfcp-watermark.image" alt="凸显布局-左轻右重" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932284776bcb4951ac26e1551cdda8f3~tplv-k3u1fbpfcp-watermark.image" alt="凸显布局-上重下轻" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a99171de85224ecd8f33bd1320721659~tplv-k3u1fbpfcp-watermark.image" alt="凸显布局-上轻下重" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"highlight-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Alibaba<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Tencent<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Baidu<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Jingdong<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Ant<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>Netease<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.highlight-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3c9</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">40px</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    &#125;
    &<span class="hljs-selector-class">.left</span> <span class="hljs-selector-tag">li</span> &#123;
        &<span class="hljs-selector-pseudo">:not</span>(:first-child) &#123;
            <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:last-child</span> &#123;
            <span class="hljs-attribute">margin-left</span>: auto;
        &#125;
    &#125;
    &<span class="hljs-selector-class">.right</span> <span class="hljs-selector-tag">li</span> &#123;
        &<span class="hljs-selector-pseudo">:not</span>(:last-child) &#123;
            <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10px</span>;
        &#125;
        &<span class="hljs-selector-pseudo">:first</span>-child &#123;
            <span class="hljs-attribute">margin-right</span>: auto;
        &#125;
    &#125;
    &<span class="hljs-selector-class">.top</span> &#123;
        <span class="hljs-attribute">flex-direction</span>: column;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
        <span class="hljs-selector-tag">li</span> &#123;
            &<span class="hljs-selector-pseudo">:not</span>(:first-child) &#123;
                <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">10px</span>;
            &#125;
            &<span class="hljs-selector-pseudo">:last-child</span> &#123;
                <span class="hljs-attribute">margin-top</span>: auto;
            &#125;
        &#125;
    &#125;
    &<span class="hljs-selector-class">.bottom</span> &#123;
        <span class="hljs-attribute">flex-direction</span>: column;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
        <span class="hljs-selector-tag">li</span> &#123;
            &<span class="hljs-selector-pseudo">:not</span>(:last-child) &#123;
                <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">10px</span>;
            &#125;
            &<span class="hljs-selector-pseudo">:first</span>-child &#123;
                <span class="hljs-attribute">margin-bottom</span>: auto;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在此还有一个小技巧，那就是<code>:not()</code>与<code>:first-child</code>和<code>:last-child</code>的巧妙运用。这样组合让特殊位置的节点直接减少属性覆盖的问题，不仅易读还能装逼。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:not(:first-child)</strong>：排除首节点，其他节点都使用某些样式</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:not(:last-child)</strong>：排除尾节点，其他节点都使用某些样式</li>
</ul>
<h4 data-id="heading-14">间距布局</h4>
<p><strong>间距布局</strong>指容器内节点从左往右从上往下排列且以特定间距间隔的占位布局。<code>间距布局</code>常见于各大列表，是笔者认为最重要的布局之一。为何如此简单的布局还是花费一些篇幅讲解呢？最近笔者查看了<code>Github</code>上很多与<code>间隔布局</code>相关的CSS代码，虽然整体效果看上去无大碍，但<code>margin/padding</code>和<code>结构选择器</code>却乱用，因此笔者想从零到一纠正<code>间距布局</code>的正确编码方式。</p>
<p>在进入编码环节前，笔者想重点讲解<code>:nth-child()</code>的点睛之笔。大部分同学可能只认得<code>:nth-child(n)</code>、<code>:nth-child(2n-1)</code>、<code>:nth-child(2n)</code>和<code>:nth-child(xn)</code>的日常用法，但其实还有一些你可能未见过的用法。在此笔者借这次机会将<code>:nth-child()</code>所有用法总结下，<code>n/x/y</code>代表正整数，最小值为<code>1</code>。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(n)</strong>：选择第<code>n</code>个元素</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(odd)</strong>：选择<code>奇数位置</code>元素，相当于<code>:nth-child(2n-1)</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(even)</strong>：选择<code>偶数位置</code>元素，相当于<code>:nth-child(2n)</code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(xn)</strong>：选择第<code>x*n</code>个元素</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(x-n)</strong>：选择前<code>x</code>个元素</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>:nth-child(y-n):nth-child(n+x)</strong>：选择第<code>x~y</code>个元素</li>
</ul>
<p>分析<code>间距布局</code>的一切特点，捕获特征很有利于将特征转换成CSS代码。</p>
<ul>
<li><strong>A</strong>：确定容器间的间距，使用<code>margin</code>声明</li>
<li><strong>B</strong>：确定容器内的间距，使用<code>padding</code>声明，后续方便声明<code>background-color</code>(该步骤很易与上一步骤混淆，请特别注意)</li>
<li><strong>C</strong>：确定靠近容器边界的节点与容器的间距，使用<code>padding</code>声明容器而不是使用<code>margin</code>声明节点(该步骤说明上一步骤的处理结果)</li>
<li><strong>D</strong>：确认每行节点的左右间距，使用<code>margin-left/margin-right</code>(二选一)声明节点</li>
<li><strong>E</strong>：确认最左列节点或最右列节点与容器的间距，使用<code>margin-left:0</code>声明最左列节点或使用<code>margin-right:0</code>声明最右列节点</li>
<li><strong>F</strong>：除了首行节点，使用<code>margin-top</code>声明其余节点</li>
<li><strong>G</strong>：若希望容器顶部底部留空，使用<code>border-top/border-bottom</code>代替<code>padding-top/padding-bottom</code></li>
</ul>
<p>全部步骤串联起来理解可能会产生混乱，但结合以下代码理解相信就能很快熟悉。以一行排列3个节点总共8个节点为例，最终效果为三行三列。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d436972457f44cccbbe6a384001111fa~tplv-k3u1fbpfcp-watermark.image" alt="间距布局" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2129c1227dff4aeca47660744c815fa2~tplv-k3u1fbpfcp-watermark.image" alt="间距布局-留空" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"spacing-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>7<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>8<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.spacing-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">overflow</span>: auto;
    <span class="hljs-attribute">flex-wrap</span>: wrap;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>; <span class="hljs-comment">// 对应A</span>
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>; <span class="hljs-comment">// 对应B和C</span>
    <span class="hljs-comment">// padding-top: 0; // 对应G</span>
    <span class="hljs-comment">// padding-bottom: 0; // 对应G</span>
    <span class="hljs-comment">// border-top: 20px solid #f66; // 对应G</span>
    <span class="hljs-comment">// border-bottom: 20px solid #f66; // 对应G</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">700px</span>; <span class="hljs-comment">// 稍微留空用于显示滚动条</span>
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f66</span>;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#66f</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        &<span class="hljs-selector-pseudo">:not</span>(:nth-child(<span class="hljs-number">3</span>n)) &#123;
            <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">20px</span>; <span class="hljs-comment">// 对应D和E</span>
        &#125;
        &<span class="hljs-selector-pseudo">:nth-child</span>(n+<span class="hljs-number">4</span>) &#123;
            <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>; <span class="hljs-comment">// 对应F</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">空载布局</h4>
<p><strong>空载布局</strong>指容器内无任何节点时使用其他形式代替的占位布局。还有使用JS判断列表集合为空时显示占位符吗？相信很多使用MVVM框架开发的同学都会使用条件判断的方式渲染虚拟DOM，若列表长度不为0则渲染列表，否则渲染占位符。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"list.length"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-esle</span>></span>Empty<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而CSS提供一个空判断的选择器<code>:empty</code>，这应该很少同学会注意到吧。</p>
<p><code>:empty</code>作用于无子节点的节点，该子节点也包括行内匿名盒(<code>单独的文本内容</code>)。以下三种情况均视为非空状态，若不出现这三种状态则视为空状态，此时<code>:empty</code>才会触发。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> 仅存在节点：<code><div><p>CSS</p></div></code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> 仅存在文本：<code><div>CSS</div></code></li>
<li class="task-list-item"><input type="checkbox" checked disabled> 同时存在节点和文本：<code><div>Hello <p>CSS</p></div></code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70f19d77a64f48ee8bdb5fd89fcf01c4~tplv-k3u1fbpfcp-watermark.image" alt="空载布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"empty-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>7<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>8<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>9<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"empty-layout"</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-variable">$empty</span>: <span class="hljs-string">"https://yangzw.vip/img/empty.svg"</span>;
<span class="hljs-selector-class">.empty-layout</span> &#123;
    <span class="hljs-attribute">overflow</span>: auto;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">outline</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#3c9</span>;
    &<span class="hljs-selector-pseudo">:empty</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">background</span>: url(<span class="hljs-variable">$empty</span>) no-repeat center/<span class="hljs-number">100px</span> auto;
        &<span class="hljs-selector-pseudo">::after</span> &#123;
            <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">90px</span>;
            <span class="hljs-attribute">font-weight</span>: bold;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">"没钱就没数据"</span>;
        &#125;
    &#125;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#09f</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        &<span class="hljs-selector-pseudo">:nth-child</span>(even) &#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f90</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外还存在一种特殊的<code>空载布局</code>，就是不做任何处理。这样最终渲染的DOM只有容器，若已声明<code>margin/padding/border</code>但未声明<code>width/height</code>的情况下，就会出现以下占位效果。无任何子节点的容器还声明着<code>margin/padding/border</code>，看着都尴尬。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a681a88037a24deb8932eb85f839f873~tplv-k3u1fbpfcp-watermark.image" alt="空载布局-尴尬" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没事，<code>:empty</code>帮你搞掂！对于无任何子节点的容器直接声明<code>display:none</code>解决所有无效占位，当然也可作用于指定节点。一招制敌，劲！</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 作用于所有节点</span>
<span class="hljs-selector-pseudo">:empty</span> &#123;
    <span class="hljs-attribute">display</span>: none;
&#125;
<span class="hljs-comment">// 作用于指定节点</span>
<span class="hljs-selector-class">.empty-layout</span><span class="hljs-selector-pseudo">:empty</span> &#123;
    <span class="hljs-attribute">display</span>: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">多格布局</h4>
<p><strong>多格布局</strong>指容器内节点以动态数量的格子形式排列的占位布局。微信朋友圈的相册就是最常见的<code>多格布局</code>了，当单张照片排列、两张照片排列、三张照片排列等等，每种情况下照片的尺寸都可能不一致。笔者制作了一个动态多格相册怀念我家狗狗<strong>AB</strong>。大家感受下纯CSS实现动态数量的<code>多格布局</code>吧。</p>
<p>在此留个悬念，不讲解如何实现，看看大家能不能根据笔者列出的提示尝试将该效果复原。主要原理是<code>根据结构选择器限制节点范围</code>实现，在本文也可找到原理的答案喔！记得实现完再看以下源码哈！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ff22e5ceac4867942b1da1d148510d~tplv-k3u1fbpfcp-watermark.image" alt="多格布局" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"multigrid-layout"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://static.yangzw.vip/codepen/ab-3.jpg"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@mixin</span> square(<span class="hljs-variable">$count</span>: <span class="hljs-number">2</span>) &#123;
    <span class="hljs-variable">$length</span>: calc((<span class="hljs-number">100%</span> - #&#123;<span class="hljs-variable">$count</span>&#125; * <span class="hljs-number">10px</span>) / #&#123;<span class="hljs-variable">$count</span>&#125;);
    <span class="hljs-attribute">width</span>: <span class="hljs-variable">$length</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-variable">$length</span>;
&#125;
<span class="hljs-selector-class">.multigrid-layout</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-wrap</span>: wrap;
    <span class="hljs-attribute">justify-content</span>: flex-start;
    <span class="hljs-attribute">align-content</span>: flex-start;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-selector-tag">li</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">5px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f0f0f0</span>;
        <span class="hljs-keyword">@include</span> square(<span class="hljs-number">3</span>);
    &#125;
    <span class="hljs-selector-tag">img</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-selector-tag">object</span>-fit: cover;
    &#125;
&#125;
<span class="hljs-comment">// 一个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:only-child</span> &#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">width</span>: auto;
    <span class="hljs-attribute">max-width</span>: <span class="hljs-number">80%</span>;
    <span class="hljs-attribute">height</span>: auto;
    <span class="hljs-attribute">max-height</span>: <span class="hljs-number">80%</span>;
&#125;
<span class="hljs-comment">// 两个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">2</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">2</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-keyword">@include</span> square(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">2</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
<span class="hljs-comment">// 三个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-keyword">@include</span> square(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">3</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 四个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>),
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-keyword">@include</span> square(<span class="hljs-number">2</span>);
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">4</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 五个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">5</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">5</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">5</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 六个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">6</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">6</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">6</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">6</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">6</span>) &#123;
    <span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 七个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">7</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">7</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">7</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">7</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 八个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">8</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">8</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">8</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">7</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-comment">// 九个元素</span>
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">9</span>) &#123;
    <span class="hljs-attribute">border-top-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">9</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">border-top-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">9</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">7</span>) &#123;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:first</span>-child<span class="hljs-selector-pseudo">:nth-last-child</span>(<span class="hljs-number">9</span>) ~ <span class="hljs-selector-class">.item</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">9</span>) &#123;
    <span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">总结</h3>
<p>很多同学可能觉得CSS很简单，但真正玩起来也能与JS有得一比。笔者从事前端领域多年，一直致力于CSS技术的研究与应用，当然真的不是为了玩，而是在玩的过程里将实践到的知识充分应用于工作上。</p>
<p>JS重要但CSS同样重要，希望喜欢CSS的同学多多关注笔者，相信你一定会有更多CSS方面的收获。在你不太愿意学习CSS时，请浏览以下网站，相信你会有不同的体验。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">个人官网</a>：暂时支持<code>PC端</code>浏览，拒绝支持<code>IExplorer</code></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyangzw.vip" target="_blank" rel="nofollow noopener noreferrer" title="https://yangzw.vip" ref="nofollow noopener noreferrer">特效专辑</a>：暂时支持<code>PC端</code>浏览，拒绝支持<code>IExplorer</code>，查看源码请戳<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJowayYoung%2Fidea-css" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JowayYoung/idea-css" ref="nofollow noopener noreferrer">这里</a></li>
</ul>
<p>笔者更多的CSS开发经验已撰写成掘金小册<a href="https://juejin.cn/book/6850413616484040711" target="_blank" title="https://juejin.cn/book/6850413616484040711">《玩转CSS的艺术之美》</a>，作为一本小众的小册同时也是掘金社区里唯一一本关于CSS的小册，相信关注CSS的你一定会喜欢。笔者已向小册姐姐申请了<code>100份</code>小册<strong>6折</strong>优惠码<strong>OGecoefC</strong>，喜欢CSS的同学可了解下喔。</p>
<blockquote>
<p>笔者往期过万阅读量的掘金爆文</p>
</blockquote>
<ul>
<li><a href="https://juejin.cn/post/6844903959283367950" target="_blank" title="https://juejin.cn/post/6844903959283367950">1.5万字概括ES6全部特性</a>：<code>16.7w</code>阅读量，<code>4500+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6844903926110617613" target="_blank" title="https://juejin.cn/post/6844903926110617613">灵活运用CSS开发技巧</a>：<code>14.1w</code>阅读量，<code>4600+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6921886428158754829" target="_blank" title="https://juejin.cn/post/6921886428158754829">中高级前端必须注意的40条移动端H5坑位指南|网易三年实践</a>：<code>5.9w</code>阅读量，<code>3800+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6844903838449664013" target="_blank" title="https://juejin.cn/post/6844903838449664013">灵活运用JS开发技巧</a>：<code>5.5w</code>阅读量，<code>1700+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6981673766178783262" target="_blank" title="https://juejin.cn/post/6981673766178783262">写给中高级前端关于性能优化的9大策略和6大指标|网易四年实践</a>：<code>2.9w</code>阅读量，<code>1800+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6844904063729926152" target="_blank" title="https://juejin.cn/post/6844904063729926152">25个你不得不知道的数组reduce高级用法</a>：<code>2.9w</code>阅读量，<code>900+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6908879198933221383" target="_blank" title="https://juejin.cn/post/6908879198933221383">8个硬核技巧带你迅速提升CSS技术|掘金直播总结</a>：<code>2.1w</code>阅读量，<code>700+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6844904084936327182" target="_blank" title="https://juejin.cn/post/6844904084936327182">妙用CSS变量，让你的CSS变得更心动</a>：<code>1.8w</code>阅读量，<code>600+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6933009968710811661" target="_blank" title="https://juejin.cn/post/6933009968710811661">一键格式化代码带来的快感|你还在为每个项目配置Stylelint和Eslint吗</a>：<code>1.1w</code>阅读量，<code>200+</code>点赞量</li>
<li><a href="https://juejin.cn/post/6844903874113830920" target="_blank" title="https://juejin.cn/post/6844903874113830920">详细判断浏览器运行环境</a>：<code>1.1w</code>阅读量，<code>200+</code>点赞量</li>
</ul>
<h3 data-id="heading-18">结语</h3>
<p><strong>❤️关注+点赞+收藏+评论+转发❤️</strong>，原创不易，鼓励笔者创作更多高质量文章</p>
<p><strong>关注公众号<code>IQ前端</code>，一个专注于CSS/JS开发技巧的前端公众号，更多前端小干货等着你喔</strong></p>
<ul>
<li>关注后回复<code>资料</code>免费领取学习资料</li>
<li>关注后回复<code>进群</code>拉你进技术交流群</li>
<li>欢迎关注<code>IQ前端</code>，更多<strong>CSS/JS开发技巧</strong>只在公众号推送</li>
</ul></div>  
</div>
            