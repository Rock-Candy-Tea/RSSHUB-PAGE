
---
title: 'css揭秘 - 视觉效果（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3186b574de1c493ba8629ee6bdfbbde7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 06:09:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3186b574de1c493ba8629ee6bdfbbde7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">单侧投影</h2>
<h3 data-id="heading-1">难题</h3>
<p><code>box-shadow</code> 如何在元素的一侧（偶尔是两侧）设置投影。</p>
<h3 data-id="heading-2">单侧投影</h3>
<p>大多数人使用 box-shadow 的方法是，指定三个长度值和一个颜色值：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">3px</span> <span class="hljs-number">4px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>box-shadow 的绘制原理：</p>
<ol>
<li>以该元素相同的尺寸和位置，画一个 rgba(0,0,0,.5) 的矩形；</li>
<li>把它向右移 2px，向下移 3px；</li>
<li>使用模糊算法将它进行 4px 的模糊处理；</li>
<li>将模糊后的矩形与原始元素的交集部分会被切除掉。</li>
</ol>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3186b574de1c493ba8629ee6bdfbbde7~tplv-k3u1fbpfcp-watermark.image" width="400" loading="lazy" referrerpolicy="no-referrer">
<p>使用 4px 的模糊半径意味着投影的尺寸会比元素本身的尺寸大约 8px ，因此投影的最外圈会从元素的四面向外显露出来，只需改变偏移量，就可以把投影的顶部和左侧隐藏起来，只要这两个方向上的偏移量不小于4px 就可以了。但是，这在某种程度上会导致外露的投影太过浓重，看起来不是很美观。另外，就算这个问题勉强可以接受，但跟想要的投影在单侧的不相符。</p>
<p>最终的解决方案来自 <code>box-shadow</code> 的第四个长度参数，排在模糊半径参数的后面，称作扩张半径。<strong>这个参数会根据指定的值去扩大（当指定值为负数）缩小投影的尺寸。</strong> 举例来说：一个 -5px 的扩张半径会把投影的宽度和高度各减少 10px。因此，下面代码即为想要的效果：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">5px</span> <span class="hljs-number">4px</span> -<span class="hljs-number">4px</span> black;
<span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">5px</span> <span class="hljs-number">0</span> <span class="hljs-number">4px</span> -<span class="hljs-number">4px</span> black;
<span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> -<span class="hljs-number">5px</span> <span class="hljs-number">4px</span> -<span class="hljs-number">4px</span> black;
<span class="hljs-attribute">box-shadow</span>: -<span class="hljs-number">5px</span> <span class="hljs-number">0</span> <span class="hljs-number">4px</span> -<span class="hljs-number">4px</span> black;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cb2e776b0754ac59262cad122bc8f07~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-3">邻边投影</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">3px</span> <span class="hljs-number">4px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>);
<span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">3px</span> <span class="hljs-number">3px</span> <span class="hljs-number">6px</span> -<span class="hljs-number">3px</span> black;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">双侧投影</h3>
<p>因为扩张半径在四个方向上的作用是相等的（即无法指定投影在水平方向上放大，而在垂直方向上缩小），唯一的办法是用两块投影（每边各一块）来达到目的。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">5px</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> -<span class="hljs-number">5px</span> black,
           -<span class="hljs-number">5px</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> -<span class="hljs-number">5px</span> black;
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afbdcbf5e91a49d89b936d41c4c93e99~tplv-k3u1fbpfcp-watermark.image" width="400" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-5">不规则投影</h2>
<h3 data-id="heading-6">难题</h3>
<p>给一个矩形或者其他能用 <code>border-radius</code> 生成的形状加投影时，<code>box-shadow</code> 的表现都堪称完美。但是当元素添加了一些伪元素或者半透明的装饰后，<code>box-shadow</code> 就有点力不从心了。这类情况包括：</p>
<ul>
<li>半透明图像、背景图像、或者 border-image；</li>
<li>元素设置了点状、虚线或半透明的边框，但没有背景；</li>
<li>对话气泡，它的小尾巴通常是用伪元素生成的；</li>
<li>在“切角效果”一节中见过的切角形状；</li>
<li>几乎所有的折角效果，包括“折角效果”一节将提到的例子；</li>
<li>通过 clip-path 生成的形状，比如“菱形图片”一节中提到的菱形图像。</li>
<li>如果对这些元素使用 box-shadow 则会得到如下所示的效果。</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fa404dda8e1449390776114488b4cce~tplv-k3u1fbpfcp-watermark.image" width="500" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-7">解决方案</h3>
<p>滤镜效果规范为这个问题提供了一个解决方案，它引入了一个叫作 <code>filter</code> 的新属性，比如<code>blur()</code> 、 <code>grayscale()</code> 以及我们需要的 <code>drop-shadow()</code></p>
<p><code>drop-shadow()</code> 滤镜可接受的参数基本上跟 <code>box-shadow</code> 属性是一样的，但不包括扩张半径，不包括 inset 关键字，也不支持逗号分割的多层投影语法。举个例子，上面的投影：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以这样写：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d592ef435043474e95f4d2d2a9f094e6~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-8">染色效果</h2>
<h3 data-id="heading-9">难题</h3>
<p>为一幅灰度图片（或是被转换为灰度模式的彩色图片）增加染色效果（color tint），是一种流行且优雅的方式，可以给一系列风格迥异的照片带来视觉上的一致性。我们通常会在静止状态下应用这个效果，当发生 <code>:hover</code> 或其他交互时再去除。最初的解决方法是用不同的图片来做，这样不仅会增加 HTTP 的请求，同时一旦色系发生变化，则又需要重新作图，成本很高。</p>
<p>另外一种方法是：在图片的上层覆盖一层半透明的纯色；或者把图片设置为半透明并覆盖在一层实色背景之上。但这并不是真正的染色效果。</p>
<p>此外还有基于 <code>JavaScript</code> 的方案，把图片置入 <code><canvas></code> 元素中，并利用脚本对其进行染色处理。但是用这种方案限制很多。</p>
<h3 data-id="heading-10">基于滤镜的方案</h3>
<p>没有现成的滤镜可以实现这个效果，需要将多个滤镜进行组合。</p>
<ul>
<li>sepia() ：给图片增加一种降饱和度的橙黄色染色效果</li>
<li>saturate() ：给每个像素提升饱和度</li>
<li>hue-rotate() ：把每个像素的色相以指定的度数进行偏移</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">filter</span>: <span class="hljs-built_in">sepia</span>(<span class="hljs-number">1</span>);
<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">sepia</span>(<span class="hljs-number">1</span>) <span class="hljs-built_in">saturate</span>(<span class="hljs-number">4</span>);
<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">sepia</span>(<span class="hljs-number">1</span>) <span class="hljs-built_in">saturate</span>(<span class="hljs-number">4</span>) <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">295deg</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da793d226862404da53b57041f958380~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时，就把图片的色调改变了，如果这个效果需要由 :hover 或其他状态来触发切换，还可以为这个变化增加过渡动画：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">transition</span>: .<span class="hljs-number">5s</span> filter;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">sepia</span>(<span class="hljs-number">1</span>) <span class="hljs-built_in">saturate</span>(<span class="hljs-number">4</span>) <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">295deg</span>);
&#125;

<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:hover</span>,
<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:focus</span> &#123;
    <span class="hljs-attribute">filter</span>: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30916b34c9f94167ac3157d061dc4fa2~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">基于混合模式的方案</h3>
<p>对一个元素设置混合模式，有两个属性可以使用：<code>mix-blend-mode</code> 可以为整个元素设置混合模式，<code>background-blend-mode</code> 可以为每层背景单独指定混合模式。因此有两种：</p>
<ol>
<li>把图片包裹在一个容器中，并把容器的背景色设置为想要的主色调。</li>
<li>不用图片元素，而是用 <code><div></code> 元素——把这个元素的第一层背景设置为要染色的图片，并把第二层的背景设置为想要的主色调。</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">a</span>&#123; <span class="hljs-attribute">background</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-number">335</span>, <span class="hljs-number">100%</span>, <span class="hljs-number">50%</span>); &#125;
<span class="hljs-selector-tag">img</span>&#123;
    mix-blend-mode: luminosity;
    <span class="hljs-attribute">display</span>: inline-block;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"1.jpg"</span> /></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滤镜是可动画的，而混合模式则不是!</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.img6</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-size</span>: cover;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-number">335</span>, <span class="hljs-number">100%</span>, <span class="hljs-number">50%</span>);
    <span class="hljs-attribute">background</span>-blend-mode: luminosity;
    <span class="hljs-attribute">transition</span>: .<span class="hljs-number">5s</span> background-color;
&#125;

<span class="hljs-selector-class">.img6</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">background-color</span>: transparent;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img6"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-image:url(2.jpg)"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acc49ae4aaa242c3b884e973f585b607~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<p>上述两种方法可以实现滤镜，但是都不够理想：</p>
<ol>
<li>图片的尺寸需要在 CSS 代码中写死；</li>
<li>在语义上，这个元素并不是一张图片，因此并不会被读屏器之类的设备读出来。</li>
</ol>
<h2 data-id="heading-12">最后说一句</h2>
<p>如果这篇文章对您有所帮助，或者有所启发的话，帮忙关注一下，您的支持是我坚持写作最大的动力，多谢支持。</p></div>  
</div>
            