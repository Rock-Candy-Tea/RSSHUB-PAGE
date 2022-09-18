
---
title: 'React + less 实现纵横柱状图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a7fc3b3967450b916c2eb625973f26~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:40:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a7fc3b3967450b916c2eb625973f26~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a7fc3b3967450b916c2eb625973f26~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之前的文章，咱们介绍过横向和竖向，具体的内容，请看</p>
<ul>
<li><a href="https://juejin.cn/post/7142290948104388615" target="_blank" title="https://juejin.cn/post/7142290948104388615">React + CSS 绘制横向柱状图</a></li>
<li><a href="https://juejin.cn/post/7142305449935634463" target="_blank" title="https://juejin.cn/post/7142305449935634463">React + CSS 绘制竖状柱状图</a></li>
</ul>
<p>这次，结合起来，横向和竖向，一起画</p>
<p>主要设计来源</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889e5ff9fe73491bb0abfa545f34b5e8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zcool.com.cn%2Fwork%2FZNjE5MjM1ODA%3D.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zcool.com.cn/work/ZNjE5MjM1ODA=.html" ref="nofollow noopener noreferrer">www.zcool.com.cn/work/ZNjE5M…</a></p>
</blockquote>
<p>三个部分</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fc6136cd0d94ba5ac6a485f01606103~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical_li"</span>></span>100<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical_li"</span>></span>75<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical_li"</span>></span>50<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical_li"</span>></span>25<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"vertical_li"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>display 布局</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.vertical</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">337px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
  <span class="hljs-attribute">font-weight</span>: bold;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#9eadca</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-direction</span>: column;
  <span class="hljs-attribute">justify-content</span>: space-between;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"crosswise"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>0<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>25<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>50<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>75<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>></span>100<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是 display 布局</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.crosswise</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">335px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
  <span class="hljs-attribute">font-weight</span>: bold;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#9eadca</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-direction</span>: row;
  <span class="hljs-attribute">justify-content</span>: space-between;
  <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">31px</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">21px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"point_list"</span>></span>
  &#123;list.map((item, index) => &#123;
    return (
      <span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">className</span>=<span class="hljs-string">"point"</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">top:</span> `$&#123;<span class="hljs-attr">100</span> <span class="hljs-attr">-</span> <span class="hljs-attr">parseFloat</span>(<span class="hljs-attr">item.y</span>)&#125;%`, <span class="hljs-attr">left:</span> `$&#123;<span class="hljs-attr">item.x</span>&#125;%` &#125;&#125;
        <span class="hljs-attr">onMouseEnter</span>=<span class="hljs-string">&#123;()</span> =></span> onMouseEnter(item, index)&#125;
        onMouseLeave=&#123;() => onMouseLeave(index)&#125;
        key=&#123;index&#125;
      >
        &#123;item.name&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    )
  &#125;)&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>动态位置，使用绝对定位</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.point_list</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">308px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">308px</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的位置，是通过传入的参数来进行控制的。如果传入的参数不是具体的位置数值，前端也可以进行二次的计算。这里我就不演示了。之前的文章都有介绍，感兴趣的小伙伴可以去前两篇文章看一下。</p>
<p><span href="https://code.juejin.cn/pen/7144650069286289421" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144650069286289421" data-src="https://code.juejin.cn/pen/7144650069286289421" style="display: none" loading="lazy"></iframe></span></p></div>  
</div>
            