
---
title: 'CSS之层叠上下文'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300e5cc07fc84f4dbe491073e357a074~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 00:16:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300e5cc07fc84f4dbe491073e357a074~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第<strong>19</strong>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一、什么是层叠上下文</h2>
<p><strong>层叠上下文（stacking context</strong>）：</p>
<p>其实就是我们虚构的一个概念，就像是我们看页面的时候，你看着好像只有一层，其实有很多层。
如果是层叠上下文的元素，<strong>就拥有优先接近我们用户的权力</strong>。（好像接近我们多好似的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300e5cc07fc84f4dbe491073e357a074~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、z-index</h2>
<p>要讲层叠上下文，就必须讲一下<code>z-index</code>，<code>z-index</code>规定了元素的层级关系。
当我们要指定元素的排列顺序的时候，给元素指定<code>z-index</code>就可以修改它的顺序。</p>
<p>注意：<code>z-index</code>只对指定了<code>position</code>属性的元素有效。</p>
<p><code>z-index</code>数值越大，<strong>它的优先级越高</strong>，也就是在上面。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00970a22ca64b0381f47fc3a3c69d50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果没有指定z-index的情况下，所有的元素默认都在默认层（0层）
，比如</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.7</span>;
        <span class="hljs-attribute">position</span>: relative;
    &#125;
   
    <span class="hljs-selector-id">#div1</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background-color</span>: aqua;
        <span class="hljs-attribute">position</span>: absolute;
    &#125;
    
    <span class="hljs-selector-id">#div2</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">234</span>, <span class="hljs-number">0</span>, <span class="hljs-number">255</span>);
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
    &#125;
    
    <span class="hljs-selector-id">#div3</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">255</span>, <span class="hljs-number">187</span>, <span class="hljs-number">0</span>);
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">2</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果👇</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/615b46e89e7849479bed99ae224858b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三、层叠水平（stacking level）</h2>
<p>如果说层叠上下文就是一种有优先接近我们的权力，那层叠水平就是决定了同一个层叠上下文当中元素在z轴上的显示顺序。</p>
<p>层叠水平不是刚刚提到的<code>z-index</code>，虽然<code>z-index</code>能够影响层叠水平，但是z-index只作用于拥有定位的元素。而层叠水平存在于<strong>所有的元素</strong>。</p>
<h2 data-id="heading-3">四、为什么会有层叠上下文</h2>
<p>当我们渲染网页的时候，有可能因为网络延迟等问题没有在很短的时间内渲染出来，也就是说，可能是先渲染了一部分内容出来，那么我们想要的这部分先渲染出来的内容肯定是重要的，就可以让重要的内容的层叠顺序变得高。</p>
<h2 data-id="heading-4">五、层叠上下文的元素</h2>
<p>根据MDN的定义，层叠上下文元素包括：</p>
<ul>
<li>文档根元素（<code><html></code>）；</li>
<li><code>position</code> 值为 <code>absolute</code>（绝对定位）或 <code> relative</code>（相对定位）且 <code>z-index</code> 值不为 <code>auto</code> 的元素；</li>
<li><code>position</code> 值为 <code>fixed</code>（固定定位）或 <code>sticky</code>（粘滞定位）的元素（沾滞定位适配所有移动设备上的浏览器，但老的桌面浏览器不支持）；</li>
<li><code>flex</code> 容器的子元素，且 <code>z-index </code>值不为 <code>auto</code>；</li>
<li><code>grid </code>容器的子元素，且 <code>z-index</code> 值不为 <code>auto</code>；</li>
<li><code>opacity</code> 属性值小于 1 的元素；</li>
<li><code>mix-blend-mode</code> 属性值不为 <code>normal</code> 的元素；</li>
<li>以下任意属性值不为 none 的元素：
<ul>
<li><code>transform</code></li>
<li><code>filter</code></li>
<li><code>perspective</code></li>
<li><code>clip-path</code></li>
<li><code>mask</code> / <code>mask-image </code>/ <code>mask-border</code></li>
</ul>
</li>
<li><code>isolation</code> 属性值为 <code>isolate</code> 的元素；</li>
<li><code>-webkit-overflow-scrolling</code> 属性值为 <code>touch</code> 的元素；</li>
<li><code>will-change</code> 值设定了任一属性而该属性在 <code>non-initial</code> 值时会创建层叠上下文的元素（参考这篇文章）；</li>
<li><code>contain</code> 属性值为 <code>layout</code>、<code>paint</code> 或包含它们其中之一的合成值的元素。</li>
</ul>
<h2 data-id="heading-5">参考文章：</h2>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context" target="_blank" rel="nofollow noopener noreferrer">MDN文档</a></p>
<p><a href="https://www.zhangxinxu.com/wordpress/2016/01/understand-css-stacking-context-order-z-index/" target="_blank" rel="nofollow noopener noreferrer">张鑫旭《深入理解CSS中的层叠上下文和层叠顺序》</a></p></div>  
</div>
            