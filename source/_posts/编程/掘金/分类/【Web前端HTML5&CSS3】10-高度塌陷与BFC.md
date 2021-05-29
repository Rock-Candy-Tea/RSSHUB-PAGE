
---
title: '【Web前端HTML5&CSS3】10-高度塌陷与BFC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dca4e9a07686417dbc435d0ff877cfd8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 04:04:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dca4e9a07686417dbc435d0ff877cfd8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>笔记来源：<a href="https://www.bilibili.com/video/BV1XJ411X7Ud" target="_blank" rel="nofollow noopener noreferrer">尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版</a></p>
</blockquote>
<p>[TOC]</p>
<h1 data-id="heading-0">高度塌陷与BFC</h1>
<h2 data-id="heading-1">1. 高度塌陷</h2>
<p>在浮动布局中，父元素的高度默认是被子元素撑开的</p>
<p>当子元素浮动后，其会完全脱离文档流，子元素从文档流中脱离将会无法撑起父元素的高度，导致父元素的高度丢失</p>
<p>父元素高度丢失以后，其下的元素会自动上移，导致页面的布局混乱</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dca4e9a07686417dbc435d0ff877cfd8~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-41" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以高度塌陷是浮动布局中比较常见的一个问题，这个问题我们必须要进行处理！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eb975d66741449ebaf322ebea55149f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>别急，我们接着往下看</p>
<h2 data-id="heading-2">2. BFC</h2>
<p>BFC（Block Formatting Context）块级格式化环境</p>
<ul>
<li>BFC是一个CSS中的一个<mark>隐含的属性</mark>，可以为一个元素开启BFC</li>
<li>开启BFC该元素会变成一个<mark>独立的布局区域</mark></li>
</ul>
<p>元素开启BFC后的特点：</p>
<ul>
<li><mark>不会被浮动元素覆盖</mark></li>
<li><mark>父子元素外边距不会重叠</mark></li>
<li><mark>可以包含浮动的元素</mark></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99925f8a656248ee95fe0d836b7e95bf~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以通过一些特殊方式来开启元素的BFC：</p>
<ul>
<li>
<p>设置为<mark>浮动（不推荐）</mark>：很明显下方元素被覆盖了，总不能让所有元素都浮动吧</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9fd6de95add40fea816dac6d5007f69~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-40" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>设置为<mark>行内块元素（不推荐）</mark>：不再独占一行，宽度变了，同时与下方元素产生了一点空隙</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/147624247c504c409a7b4e145843a74d~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-39" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>设置<mark><code>overflow</code>为非<code>visible</code>值</mark>：既没有覆盖元素，也保持了独占一方的特性（保持了宽度），与下方元素也保持了最初的间隙</p>
<p>常用的方式为元素设置<code>overflow:hidden</code>（<code>overflow:auto</code>也是ok的） 开启其BFC， 以使其可以包含浮动元素</p>
<p><code>overflow:scroll</code> 会有滚动条，可能并不需要的，所以不太推荐</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c72b888d9514aaeb3de7e36b650808c~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-38" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过，这种方式也存在一定问题，如下，<code>overflow</code>并没有完全清除div2布局上受到的影响</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7afd3c8a3cc4bc897ac881accb0140e~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-34" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p><strong>总结</strong></p>
<ul>
<li>可以通过变成浮动元素，来防止自身被浮动元素覆盖（有点“以毒攻毒”那味了）</li>
<li>可以设置行内块，来防止自身及其他元素被浮动元素覆盖（如果说浮动是“独善其身”，那行内块就有点“兼济天下”的意思）</li>
<li>可以设置<code>overflow</code>属性，包含浮动元素（既“独善其身”，又“兼济天下”，但仍有缺陷）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af3e90e4adde4fbead3383b1c82594d4~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2d27983c3e24780a5ce4e8c278bc58d~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以打开<code>Zeal</code>手册（《02-前端开发准备》有介绍），查看关于BFC的说明文档</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77f789f22f534c9ab01c9c1b416e6bff~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210526210723927" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开<code>Block formatting context</code>模块后，可以看到有很多开启BFC的方式</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13eeff3ea54545779065c26c2830bbef~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210526210843339" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我这里大概翻译了一下，并整理了一份表格，应该看起来更直观一点（有些概念因为还没有学习，翻译和理解有误的地方还望谅解）</p>

































































<table><thead><tr><th>元素或属性</th><th>说明</th></tr></thead><tbody><tr><td><code><html></code></td><td>文档根元素</td></tr><tr><td><mark><code>float: left</code></mark><br><mark><code>float: right</code></mark></td><td>浮动元素（<code>float</code>不为<code>none</code>）</td></tr><tr><td><mark><code>position: absolut</code></mark><br><mark><code>position: fixed</code></mark></td><td>绝对定位元素</td></tr><tr><td><mark><code>display: inline-block</code></mark></td><td>行内块元素</td></tr><tr><td><code>display: table-cell</code></td><td>表格单元，默认值</td></tr><tr><td><code>display: table-caption</code></td><td>表格标题，默认值</td></tr><tr><td><code>display: table</code><br><code>display: table-row</code><br><code>display: table-row-group</code><br><code>display: table-header-group</code><br><code>display: table-footer-group</code><br><code>display: inline-table</code></td><td>匿名的表格单元，分别是HTML表格、表行、表体、表头和表脚的默认值</td></tr><tr><td><mark><code>overflow: hidden</code></mark><br><mark><code>overflow: scroll</code></mark><br><mark><code>overflow: auto</code></mark></td><td><code>overflow</code>不为<code>visible</code>和<code>clip</code>的块元素</td></tr><tr><td><code>display: flow-root</code></td><td></td></tr><tr><td><code>contain: layout</code><br><code>contain: content</code><br><code>contain: paint</code></td><td></td></tr><tr><td><code>display: flex</code><br><code>display: inline-flex</code>的直接子元素</td><td>Flex项，如果它们本身既不是<code>flex</code>，也不是<code>grid</code>或<code>table</code>容器</td></tr><tr><td><code>display: grid</code><br><code>display: inline-grid</code>的直接子元素</td><td>Grid项，如果它们本身既不是<code>flex</code>，也不是<code>grid</code>或<code>table</code>容器</td></tr><tr><td><code>column-count</code>不为<code>auto</code><br><code>column-width</code>不为<code>auto</code></td><td>Multicol容器，包含<code>column-count: 1</code></td></tr><tr><td><code>column-span: all</code></td><td>应该总是创建一个新的格式化上下文，即使<code>column-span: all</code>元素不在multicol容器中</td></tr></tbody></table>
<p>但是，注意不管哪种方式，多多少少都会有些隐患、缺陷或者说“副作用”</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d43b038020ee4fd08cc5ccda9aeab5ae~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210526231648421" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3. clear</h2>
<p>我们这里设计三个兄弟元素，对前两个元素进行<code>float</code>的浮动属性设置，看下效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de9eadece59d4e1581f5016005059a5a~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-36" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于box1的浮动，导致box3位置上移也就是box3受到了box1浮动的影响，位置发生了改变（注意，这里文字并没有被覆盖，《09-浮动》一节说过浮动的特点，其中第7点就是“文字环绕”的问题）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97c78a92e8ad4a8ea663778483e6ad8e~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们不希望某个元素因为其他元素浮动的影响而改变位置，可以通过<code>clear</code>属性来清除浮动元素对当前元素所产生的影响</p>
<p><code>clear</code>作用：<mark>清除浮动元素对当前元素所产生的影响（本质是为元素添加一个<code>margin-top</code>属性，值由浏览器自动计算）</mark></p>
<p>可选值：</p>
<ul>
<li><code>left</code> 清除左侧浮动元素对当前元素的影响</li>
<li><code>right </code> 清除右侧浮动元素对当前元素的影响</li>
<li><code>both</code> 清除两侧中影响较大一侧元素的影响（注意，这里不是同时清除两侧的影响）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4241395888da4304a2718e65a271595e~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-37" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">4. after</h2>
<p>我们学习了上面知识后，了解了高度塌陷问题的解决方式，其中主要有</p>
<ul>
<li>
<p>通过<code>overflow: hidden</code>等可以为元素开启BFC</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/358bfd118d474c5d8c5e46fd1fcf2588~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-35" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>通过<code>clear: both</code>等可以清除浮动对元素产生的影响</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d79881ce0364944bb71aa0975404d5b~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-33" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>同时也了解到，这两种方式都有一定的弊端和隐患。那有没有一种更好的方式去解决高度塌陷的问题呢？</p>
<p>答案当然是：有！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9449eb3fd1ce4e80b4ec00046cc41d40~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210526233234635" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们直接上效果图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab6fdd81986439db87b8de7da22efd9~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-32" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Q1：这里使用了一个伪元素选择器<code>::after</code>，那有人会问了，跟在box2下直接定义一个box3有什么区别呢？</strong></p>
<p>A：我们知道，网页的结构思想是：结构+表现+行为。在box2下直接定义一个box3，属于结构；而使用伪元素选择器，属于表现</p>
<p>而高度塌陷问题属于表现问题，定义box3的目的是为了撑起box1的内容，属于表现，而不是结构，所以在css中定义<code>::after</code>更符合网页的编程思想</p>
<p><strong>Q2：为什么需要使用<code>display: block</code>呢？</strong></p>
<p>A：因为默认情况下，<code>::after</code>伪元素是一个行内元素，如果不转为块元素，将仍然撑不起box1的高度</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fd8ea067554c828cc3f3a98e2f921e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210526235431125" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">5. clearfix</h2>
<p>我们在前面《06-盒模型》一节中说过垂直布局中边距重叠的问题：相邻的垂直方向外边距会发生重叠现象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a526cea3b2b3420493dfb61336462a65~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-30" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，子元素设置了一个<code>margin-top</code>之后，父元素跟随子元素一起进行了移动</p>
<p>即我们之前说的<q>父子元素间相邻外边距，子元素会传递给父元素（上外边距）</q></p>
<p>聪明的小伙伴已经想到了，用刚才说的伪元素选择器啊</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aca506113ab248f3892447ffdf96381a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，我们先来看下效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e631b172b4e145e1b7f81b51dee1cae3~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-29" loading="lazy" referrerpolicy="no-referrer"></p>
<p>貌似是没有任何变化，到底是什么地方不对呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc0ea5760ec2480b85694ea32e11b340~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再来回顾下使用<code>after</code>伪元素的心路历程：</p>
<ul>
<li>使用无内容的box3撑起box1 ==》表现代替结构（<code>::after</code>代替box3）</li>
<li><code>clear</code>清除浮动对元素产生的影响（还记得<code>clear</code>的原理么？）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1cc7c3d1c414c96acc1ca5c6d5e3c21~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实就是给元素设置了一个<code>margin-top</code>属性，不过这个在开发者工具中是看不到的</p>
<p>既然如此，就相当于在box2下面添加一个box3，然后给box3设置一个<code>margin-top</code>属性</p>
<p>到此为止，</p>
<p>∵  <q>相邻的垂直方向外边距</q> 这个条件仍然满足</p>
<p>∴  <q>会发生重叠现象</q>这个结论也依然成立</p>
<p>具体点就是，<q>父子元素间相邻外边距，子元素会传递给父元素（上外边距）</q>，表现为box1和box2同步往下移动</p>
<p>那我们应该怎么做才能解决这个问题？ <del>凭你们朴素的情感，应该怎么判？</del> 当然就是让上述条件不满足呗！</p>
<p>怎么能够不满足？当然是让两个元素垂直外边距不相邻啊！</p>
<p>好，多说无益，我们直接上代码看效果！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ea9748b818e4c2d8fb9671c40a4b32f~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-28" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们用了<code>before</code>伪元素选择器，目的当然是让box1和box2的外边距不相邻，但是好像并没有效果</p>
<p>我们再换成<code>display: inline-block</code>属性看看</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0594831ab83f4f0fa239c243cc50f5e3~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-27" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好像是解决了父元素布局的问题，但是子元素怎么还往下跑了一段距离？ <del>是谁给的勇气？</del></p>
<p>因为<code>inline-block</code>兼顾行内元素和块元素的特点，既可以设置宽高也不独占一行</p>
<p>在没有设置宽高时，会存在一个默认高度，所以<code>inline-block</code>仍然行不通</p>
<p>还有一个属性，<code>display: table</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df9ca9342bd4216b1200bb804498d40~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2021-26" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Bingo！实现了我们最终想要的效果</p>
<p><strong>Q1：为什么没有使用clear属性？</strong></p>
<p>A：不是说了吗？<code>clear</code>是为了清除浮动对布局的影响，我们现在没有浮动的元素啊，我们要讨论的也不是浮动的问题</p>
<p><strong>Q2：display不是还有一个<code>none</code>属性么，为什么不用呢？</strong></p>
<p>A：<code>none</code>属性是不占据位置，但是也不能让元素相邻的外边距分离啊</p>
<p><strong>Q3：为什么<code>table</code>值就可以呢？</strong></p>
<p>A：这个问题问的非常好，算是问到点上了！我们上面在讲开启BFC的一些方法的时候，也提到了该属性。而且，应该牢记的是，元素开启BFC后的其中一个特点就是 <q><mark>父子元素外边距不会重叠</mark></q>。当然，这里也需要合理选择伪元素选择器，使其外边距不相邻才行</p>
<p>另外，总结一下：</p>
<ul>
<li>高度塌陷问题，一般用<code>::after</code></li>
<li>外边距重叠问题，一般用<code>::before</code></li>
</ul>
<p>不知道到这里，大家能不能想明白这两件事情</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/430c532662c34df9af9b6addb1b457dd~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么问题来了，有没有一个两全其美的办法，既可以解决高度塌陷，又可以解决外边距重叠呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224b2966058f45ed89a39f1d7d57b32f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然有！<code>clearfix</code> 这个样式就可以同时解决高度塌陷和外边距重叠的问题</p>
<p>当你在遇到这些问题时，直接使用<code>clearfix</code>这个类即可，他就可以帮你轻松搞定css中的两大难题</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.clearfix</span><span class="hljs-selector-pseudo">::before</span>,
<span class="hljs-selector-class">.clearfix</span><span class="hljs-selector-pseudo">::after</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: table;
    <span class="hljs-attribute">clear</span>: both;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>.clearfix::before</code>是为了解决外边距重叠问题</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.clearfix</span><span class="hljs-selector-pseudo">::before</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: table;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.clearfix::after</code>是为了解决高度塌陷问题</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.clearfix</span><span class="hljs-selector-pseudo">::after</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: table;
    <span class="hljs-attribute">clear</span>: both;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者合在一起，就可以完美地解决高度塌陷和外边距重叠这两大“世纪难题”了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7610fb5e0a8b4dcf85062eeba89dbece~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210528030932616" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            