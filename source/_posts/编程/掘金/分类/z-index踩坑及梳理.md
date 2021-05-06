
---
title: 'z-index踩坑及梳理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5425'
author: 掘金
comments: false
date: Thu, 06 May 2021 01:29:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=5425'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">定义</h1>
<blockquote>
<p>z-index 属性指定一个元素的堆叠顺序。<br>
拥有更高堆叠顺序的元素总是会处于堆叠顺序较低的元素的前面。</p>
</blockquote>
<p>然而，在使用中往往会发现，有的元素明明是z-index：999999，但是仍然会被一些z-index：1的元素覆盖，why？</p>
<p>按照我个人理解，原因是z-index有其<code>作用域</code>，因此数值大的不一定在前面，它只会和同<code>作用域</code>的元素比较。下面具体分析一下（而不是用我造的词）。</p>
<h1 data-id="heading-1">stacking contexts</h1>
<p><code>stacking contexts</code>是元素的上下文。当我们给元素一个z-index，那么这个值只会和在相同 context下的其他元素竞争，如果是更高的竞争则交给其context进行比较。</p>
<p>css的设计和ps其实有点像，z-index是元素的层级，stacking contexts是元素所在的组。层级只在当前组下生效。</p>
<h1 data-id="heading-2">创建上下文的方法</h1>
<p>如果啥样式都没写（html标签自动创建一个上下文），那么整个html页面只有一个上下文，z-index也就全局生效了。但是很多情况下，我们需要创建新的上下文来避免元素突破容器，或者会无意中创建了上下文导致元素的z-index无效。所以了解上下文创建方法就很有必要了，常见方法如下：</p>
<ul>
<li>设置了transform，filter，perspective，clip-path，mask / mask-image / mask-border等样式属性</li>
<li>透明度设置为小于1的值</li>
<li>position为absolute/relative并设置了z-index，或position为sticky/fixed</li>
<li>父容器为flex或者grid，且自身设置了z-index</li>
<li>设置isolation: isolation属性（常用于上下文封装）</li>
</ul>
<p>更多的直接看文档吧：<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context#the_stacking_context" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></p>
<h1 data-id="heading-3">排查工具</h1>
<p>推荐一款chrome插件：<a href="https://chrome.google.com/webstore/detail/css-stacking-context-insp/apjeljpachdcjkgnamgppgfkmddadcki" target="_blank" rel="nofollow noopener noreferrer">CSS Stacking Context inspector</a></p>
<p>优点：用起来足够简单明了，而且可以告诉选择元素上下文创建的原因及跳转到代码<br>
缺点：功能并不是很强大，只能起到辅助作用</p></div>  
</div>
            