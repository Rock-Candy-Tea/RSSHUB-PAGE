
---
title: 'CSS3中animation实现流光按钮效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e07e3cef45497ba32905921ae00555~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 22:50:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e07e3cef45497ba32905921ae00555~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h1 data-id="heading-0">CSS3中animation实现流光按钮效果</h1>
<p>这篇文章主要介绍了CSS3中animation实现流光按钮效果</p>
<h2 data-id="heading-1">码上掘金展示</h2>
<p><span href="https://code.juejin.cn/pen/7144607816593899560" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144607816593899560" data-src="https://code.juejin.cn/pen/7144607816593899560" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-2">详细解释</h2>
<p>在学习css3的过程中，发现很多看着炫酷的效果，利用css3的属性能很简单的实现，animation是css3动画效果中常见的属性。下面让我们了解一下如何利用这个属性做出以下鼠标停在按钮上有流光按钮效果~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e07e3cef45497ba32905921ae00555~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在此之前简单介绍一下animation属性的用法。<br>
animation：[ animation-name(检索或设置对象所应用的动画名称) ] || [ animation-duration(检索或设置对象动画的持续时间) ] || [ animation-timing-function(检索或设置对象动画的过渡类型) ] || [ animation-delay(检索或设置对象动画延迟的时间) ] || [ animation-iteration-count(检索或设置对象动画的循环次数) ] || [ animation-direction(检索或设置对象动画在循环中是否反向运动) ]<br>
<strong>第一步</strong>：给div设置宽高和圆角边框成一个圆角矩形。<br>
<strong>第二步</strong>：设置背景颜色为三种颜色的渐变色（最后一个颜色需要和第一个颜色一样，这样流动起来不会有卡颜色的情况），并将背景大小设为400%，主要代码如下</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(to left , <span class="hljs-number">#EAD6EE</span>,<span class="hljs-number">#A0F1EA</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">124</span>, <span class="hljs-number">241</span>, <span class="hljs-number">241</span>),<span class="hljs-number">#e3a5f0</span>,<span class="hljs-number">#EAD6EE</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析：现在背景为三种颜色的渐变大小是div的四倍，所以div只显示出一个颜色，利用帧动画效果控制背景的移动，加上animation属性就可以一直流动了~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3001451ecf7e4db588a40c332beb8f01~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第三步</strong>：利用帧动画控制背景定位的横向移动。（@keyframes作用：定义动画，简单的动画可以直接使用关键字from和to，复杂的利用0%~100%，分段设置相应的动画效果，即从一种状态过渡到另一种状态）</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> run&#123;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">background-position</span>: <span class="hljs-number">400%</span> <span class="hljs-number">0px</span>;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再利用伪类hover实现鼠标移上去就出现动画的效果~<br>
伪类主要代码</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> run&#123;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">background-position</span>: <span class="hljs-number">400%</span> <span class="hljs-number">0px</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.div2</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">animation</span>: run <span class="hljs-number">4s</span> linear <span class="hljs-number">0s</span> infinite;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单的css3流光动画效果就实现啦</p>
<p>到此这篇关于CSS3中animation实现流光按钮效果的文章就介绍到这了,更多相关css3 animation 流光按钮内容请搜索脚本之家以前的文章或继续浏览下面的相关文章，希望大家以后多多支持</p></div>  
</div>
            