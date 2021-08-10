
---
title: 'CSS 动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228c82fe53a24560a63f08cac352597c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 01:45:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228c82fe53a24560a63f08cac352597c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">动画</h2>
<h3 data-id="heading-1">定义</h3>
<ul>
<li>由许多静止的画面（帧）</li>
<li>以一定的速度（如每秒30张）连续播放时</li>
<li>肉眼因视觉残象产生错觉</li>
<li>而误以为是活动的画面</li>
</ul>
<h3 data-id="heading-2">概念</h3>
<ul>
<li>帧：每个静止的画面都叫做帧</li>
<li>播放速度：每秒24帧（影视）或者每秒30帧（游戏）</li>
</ul>
<h3 data-id="heading-3">开发者工具渲染</h3>
<ul>
<li>F12 ——> 任一tab ——> ESC ——> 左边三个小点 ——> Rendering ——> Paint flashing</li>
</ul>
<h2 data-id="heading-4">浏览器渲染原理</h2>
<h3 data-id="heading-5">Google 团队写的文章</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fperformance%2Fcritical-rendering-path%2Frender-tree-construction" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction" ref="nofollow noopener noreferrer">渲染树构建、布局及绘制</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fperformance%2Frendering%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/performance/rendering/" ref="nofollow noopener noreferrer">渲染性能</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fperformance%2Frendering%2Fstick-to-compositor-only-properties-and-manage-layer-count" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/performance/rendering/stick-to-compositor-only-properties-and-manage-layer-count" ref="nofollow noopener noreferrer">使用 transform 来实现动画</a></li>
</ul>
<h3 data-id="heading-6">查看 CSS 各属性触发什么</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcsstriggers.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://csstriggers.com/" ref="nofollow noopener noreferrer">CSSTriggers.com</a></li>
</ul>
<h2 data-id="heading-7">浏览器渲染过程</h2>
<h3 data-id="heading-8">步骤</h3>
<ul>
<li>根据 HTML 构建 HTML 树（DOM）</li>
<li>根据 CSS 构建 CSS 树（CSSOM）</li>
<li>将两棵树合并成一颗渲染树（render tree）</li>
<li>Layout 布局（文档流、盒模型、计算大小和位置）</li>
<li>Paint 绘制（把边框颜色、文字颜色、阴影等画出来）</li>
<li>Compose 合成（根据层叠关系展示画面）</li>
</ul>
<h2 data-id="heading-9">如何更新样式</h2>
<h3 data-id="heading-10">一般用 JS 来更新样式</h3>
<ul>
<li>比如 div.style.background = 'red'</li>
<li>比如 div.style.display = 'none'</li>
<li>比如 div.classList.add('red')</li>
<li>比如 div.remove() 直接删掉节点</li>
</ul>
<h3 data-id="heading-11">三种更新方式</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228c82fe53a24560a63f08cac352597c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">CSS 动画优化</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fperformance%2Frendering%2Fstick-to-compositor-only-properties-and-manage-layer-count" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/performance/rendering/stick-to-compositor-only-properties-and-manage-layer-count" ref="nofollow noopener noreferrer">Google 文章</a></li>
<li>JS 优化： 使用 <code>requestAnimationFrame</code> 代替 <code>setTimeout</code> 或者 <code>setInterval</code></li>
<li>CSS 优化： 使用 <code>will-change</code> 或 <code>translate</code></li>
</ul>
<h2 data-id="heading-13">transform</h2>
<h3 data-id="heading-14">四个常用功能</h3>
<ul>
<li>位移 translate</li>
<li>缩放 scale</li>
<li>旋转 rotate</li>
<li>倾斜 skew</li>
</ul>
<h3 data-id="heading-15">注意</h3>
<ul>
<li>一般都需要配合 transition 过渡</li>
<li>inline 元素不支持 transform， 需要先变成 block</li>
</ul>
<h2 data-id="heading-16">transform 之 translate</h2>
<h3 data-id="heading-17">常用写法</h3>
<pre><code class="hljs language-CSS copyable" lang="CSS">    translateX(<length-percentage>)
    translateY(<length-percentage>)
    translate(<length-percentage>,<length-percentage>?>
    translateZ(<length>) 且父容器 <span class="hljs-attribute">perspective</span>
    translate3d(x,y,z)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>translate(-50%, -50%) 可做绝对定位元素的居中</li>
</ul>
<pre><code class="hljs language-CSS copyable" lang="CSS">  <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">transform 之 scale （不常用，容易模糊）</h2>
<h3 data-id="heading-19">常用写法</h3>
<ul>
<li>scaleX(<number>)</li>
<li>scaleY(<number>)</li>
<li>scale(<number>, <number>?)</li>
</ul>
<h2 data-id="heading-20">transform 之 rotate</h2>
<h3 data-id="heading-21">常用写法</h3>
<ul>
<li>rotate([<angle>|<zero>])</li>
<li>rotateX([<angle>|<zero>])</li>
<li>rotateY([<angle>|<zero>])</li>
<li>rotateZ([<angle>|<zero>])</li>
<li>rotate3d</li>
</ul>
<h3 data-id="heading-22">注意</h3>
<ul>
<li>一般用于 360度旋转制作 loading</li>
</ul>
<h2 data-id="heading-23">transform 之 skew</h2>
<h3 data-id="heading-24">常用写法</h3>
<ul>
<li>skewX([<angle>|<zero>])</li>
<li>skewY([<angle>|<zero>])</li>
<li>skew([<angle>|<zero>],[<angle>|<zero>]?)</li>
</ul>
<h2 data-id="heading-25">transform 多重效果</h2>
<h3 data-id="heading-26">组合使用</h3>
<ul>
<li>transform: scale(0.5) translate(-100%, -100%);</li>
<li>transform: none; 取消所有</li>
</ul>
<h2 data-id="heading-27">transition</h2>
<h3 data-id="heading-28">作用</h3>
<ul>
<li>补充中间帧</li>
</ul>
<h3 data-id="heading-29">语法</h3>
<ul>
<li>transition: 属性名 时长 过渡方式 延迟</li>
<li>transition: left 200ms linear</li>
<li>可以用逗号分隔两个不同属性</li>
<li>transition: left 200ms, top 400ms</li>
<li>可以用 all 代表所有属性</li>
<li>transition: all 200ms</li>
<li>过渡方式有：linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier | step-start | step-end | steps</li>
</ul>
<h3 data-id="heading-30">注意</h3>
<ul>
<li>并不是所有属性都能过渡
<ul>
<li>display: none=>block 没法过渡</li>
<li>一般改成 visibility: hidden => visible</li>
<li>display 和 visibility 的区别</li>
<li>background 的颜色可以过渡</li>
<li>opacity 透明度可以过渡</li>
</ul>
</li>
</ul>
<h2 data-id="heading-31">animation</h2>
<ul>
<li>声明关键帧</li>
<li>添加动画</li>
</ul>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-id">#demo</span><span class="hljs-selector-class">.start</span>&#123;
  <span class="hljs-attribute">animation</span>: xxx <span class="hljs-number">1.5s</span> forwards;
&#125;

<span class="hljs-keyword">@keyframes</span> xxx &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: none;
  &#125;
  <span class="hljs-number">66.66%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">200px</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">200px</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">100px</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">缩写语法</h3>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-attribute">animation</span>: 时长 | 过渡方式 | 延迟 | 次数 | 方向 | 填充模式 | 是否暂停 | 动画名;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>时长：1s 或者 1000ms</li>
<li>过渡方式：跟 transition 取值一样，如 linear</li>
<li>次数：3 或者 2.4 或者 infinite</li>
<li>方向：reverse | alternate | alternate-reverse</li>
<li>填充模式：none | forwards | backwards | both</li>
<li>是否暂停：paused | running</li>
<li>以上所有属性都有对应的单独属性</li>
</ul></div>  
</div>
            