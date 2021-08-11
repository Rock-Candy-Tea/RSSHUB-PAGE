
---
title: 'CSS书写顺序优化及原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4042'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:26:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=4042'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>相信很多刚入门前端的小伙伴 甚至 一些在前端行业摸爬滚打多年的程序员都没有意识到：<strong>原来CSS样式书写顺序也是有讲究的</strong>。</p>
<p>就像我刚开始学习前端的时候，每次写css样式都是用到什么就在样式表后添加什么，完全没有考虑到样式属性的书写顺序对网页加载代码的影响。后来逐渐才知道正确的样式顺序不仅易于查看，并且也属于css样式优化的一种方式。那么CSS书写到底应该遵循什么样的顺序呢？且往下看：</p>
<ol>
<li>定位属性：position  display  float  left  top  right  bottom   overflow  clear   z-index</li>
<li>自身属性：width  height  padding  border  margin   background</li>
<li>文字样式：font-family   font-size   font-style   font-weight   font-varient   color</li>
<li>文本属性：text-align   vertical-align   text-wrap   text-transform   text-indent    text-decoration   letter-spacing    word-spacing    white-space   text-overflow</li>
<li>css3中新增属性：content   box-shadow   border-radius  transform……</li>
</ol>
<p>为什么是这样的顺序呢？ 需要了解一下 <strong>回流和重构</strong>，这决定着css样式书写顺序的优化方向。</p>
<h3 data-id="heading-0">文档加载完成到完全显示之间的过程：</h3>
<p>根据文档加载生成DOM树（包含display：none；节点）；
在DOM树基础上根据节点的几何属性（padding、margin、width等）生成render树（不包含display：none：和head，但是包括visibility:hidden;）；
在render树基础上继续渲染color、outline等样式；
当render树上的一部分或者全部，因为大小边距等问题发生改变需要重建的过程叫做回流；</p>
<pre><code class="copyable"> 当元素的一部分属性如背景色等发生变化，而不影响页面布局需要重新渲染的过程叫做重绘。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了对文档加载过程的理解，我们很容易发现，要想网页加载得快，加载得流畅，就要减少浏览器回流，提升dom的性能</p>
<pre><code class="copyable">  在解析过程中，一旦浏览器发现某个元素的定位变化影响布局，则需要倒回去重新渲染，所以定位元素和z-index要放在最开始的位置，上来就告诉浏览器应当怎么加载。
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            