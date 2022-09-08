
---
title: 'CSS3实现的彩色科幻灯特效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c78fb5499d6f4fc8bbc54eb813c8b716~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 23:37:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c78fb5499d6f4fc8bbc54eb813c8b716~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h1 data-id="heading-0">CSS3实现的彩色科幻灯特效</h1>
<h1 data-id="heading-1">码上掘金展示</h1>
<p><span href="https://code.juejin.cn/pen/7139807663524675597" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7139807663524675597" data-src="https://code.juejin.cn/pen/7139807663524675597" style="display: none" loading="lazy"></iframe></span></p>
<p>这是要实现的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c78fb5499d6f4fc8bbc54eb813c8b716~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在鼠标移入按钮的时候，会产生类似霓虹灯光的效果；在鼠标移出按钮的时候，会有一束光沿着固定的轨迹（按钮外围）运动。</p>
<h2 data-id="heading-2">霓虹灯光的实现</h2>
<p>霓虹灯光的实现比较简单，用多重阴影来做即可。我们给按钮加三层阴影，从内到外每层阴影的模糊半径递增，这样的多个阴影叠加在一起，就可以形成一个类似霓虹灯光的效果。这段的代码如下：</p>
<p>HTML：</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"light"</span>></span>
    Neon Button
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
 <span class="hljs-attribute">background</span>: <span class="hljs-number">#050901</span>;   
&#125;
<span class="hljs-selector-class">.light</span> &#123;
  <span class="hljs-attribute">width</span>: fit-content;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">25px</span> <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#03e9f4</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">text-transform</span>: uppercase;
  <span class="hljs-attribute">transition</span>: <span class="hljs-number">0.5s</span>;
  <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">4px</span>;
  <span class="hljs-attribute">cursor</span>: pointer;
&#125;
<span class="hljs-selector-class">.light</span><span class="hljs-selector-pseudo">:hover</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#03e9f4</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#050801</span>;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">25px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">200px</span> <span class="hljs-number">#03e9f4</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f398a6e6155b495f8d3ed35581ce3a48~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">运动光束的实现</h2>
<p>虽然看起来只有一个光束沿着按钮的边缘运动，但实际上这是四个光束沿着不同方向运动之后叠加的效果。它们运动的方向分别是：从左往右、从上往下、从右往左、从下往上，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/825079dd4196408fb4e5f8784fde9de2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这个过程中，光束和光束之间产生了交集，如果只看按钮的边缘部分，就很像是只有一个光束在做顺时针方向的运动。</p>
<p>下面是具体实现中几个需要注意的点：</p>
<ul>
<li>四个光束分别对应 div.light 的四个子 div，初始位置分别是在按钮的最左侧、最上方、最右侧和最下方，并按照固定的方向做重复的运动</li>
<li>每个光束的高度或宽度都很小（只有 2px），并且都有一个从透明色到霓虹色的渐变，因此外表会有一个收束的效果（即看上去不是一条完整的线条）</li>
<li>为了确保我们看到的是一个顺时针方向的运动，四个光束的运动实际上是有序的，首先是按钮上方的光束开始运动，在一段时间后，右侧的光束运动，在一段时间后，下方的光束运动，在一段时间后，左侧的光束运动。光束和光束之间的运动有一个延迟，以上方和右侧的光束为例，如果它们同时开始运动，由于右侧的运动距离小于上方的运动距离，就会导致这两个光束错过相交的时机，我们看到的就会是断开的、不连贯的光束。既然右侧光束的运动距离比较短，为了让上方光束可以“追上”它，我们就得让右侧光束“延迟出发”，因此要给它一个动画延迟；同理，剩余两个光束也要有一个动画延迟。多个动画延迟之间大概相差 0.25 秒即可。</li>
<li>只需要显示按钮边缘的光束就够了，因此给 div.light 设置一个溢出隐藏</li>
</ul>
<p>相关代码如下：</p>
<p>CSS：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.light</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">25px</span> <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#03e9f4</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">text-transform</span>: uppercase;
  <span class="hljs-attribute">transition</span>: <span class="hljs-number">0.5s</span>;
  <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">4px</span>;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">overflow</span>: hidden;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20%</span>;
&#125;
<span class="hljs-selector-class">.light</span><span class="hljs-selector-pseudo">:hover</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#03e9f4</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#050801</span>;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">25px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">#03e9f4</span>,
              <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">200px</span> <span class="hljs-number">#03e9f4</span>;
&#125;
<span class="hljs-selector-class">.light</span> <span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
&#125;
<span class="hljs-selector-class">.light</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>)&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">2px</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to right,transparent,<span class="hljs-number">#03e9f4</span>);
  <span class="hljs-attribute">animation</span>: animate1 <span class="hljs-number">1s</span> linear infinite;
&#125;
<span class="hljs-selector-class">.light</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>)&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">2px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">top</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to bottom,transparent,<span class="hljs-number">#03e9f4</span>);
  <span class="hljs-attribute">animation</span>: animate2 <span class="hljs-number">1s</span> linear infinite;
  <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.25s</span>;
&#125;
<span class="hljs-selector-class">.light</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>)&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">2px</span>;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">right</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to left,transparent,<span class="hljs-number">#03e9f4</span>);
  <span class="hljs-attribute">animation</span>: animate3 <span class="hljs-number">1s</span> linear infinite;
  <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.5s</span>;
&#125;
<span class="hljs-selector-class">.light</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>)&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">2px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to top,transparent,<span class="hljs-number">#03e9f4</span>);
  <span class="hljs-attribute">animation</span>: animate4 <span class="hljs-number">1s</span> linear infinite;
  <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.75s</span>;
&#125;
<span class="hljs-keyword">@keyframes</span> animate1 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>;
  &#125;
  <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="hljs-keyword">@keyframes</span> animate2 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">top</span>: -<span class="hljs-number">100%</span>;
  &#125;
  <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="hljs-keyword">@keyframes</span> animate3 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">right</span>: -<span class="hljs-number">100%</span>;
  &#125;
  <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="hljs-keyword">@keyframes</span> animate4 &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">100%</span>;
  &#125;
  <span class="hljs-number">50%</span>,<span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以达到文章开头图片的效果了。</p>
<h2 data-id="heading-4">不同颜色的霓虹灯</h2>
<p>如果想要其它颜色的霓虹灯光效果怎么办呢？是否需要把相关的颜色重新修改一遍？其实我们有更简单的方法，就是使用 filter:hue-rotate(20deg) 一次性修改 div.light 和内部所有元素的色相/色调。</p>
<blockquote>
<p>The hue-rotate() CSS function rotates the hue of an element and its contents.</p>
</blockquote>
<p>最终效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ebd79ffd6a44939ead65a7a73d5fa6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是</p></div>  
</div>
            