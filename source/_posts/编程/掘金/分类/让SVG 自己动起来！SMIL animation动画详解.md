
---
title: '让SVG 自己动起来！SMIL animation动画详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c65e79bd0e4b4e94ef594626608888~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 22:22:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c65e79bd0e4b4e94ef594626608888~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>今天一起来了解一下，怎么在不靠其它套件的状况下，单纯的制作SVG动画。</p>
<p><strong>资料来源：</strong>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangxinxu.com%2Fwordpress%2F2014%2F08%2Fso-powerful-svg-smil-animation%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangxinxu.com/wordpress/2014/08/so-powerful-svg-smil-animation/" ref="nofollow noopener noreferrer">www.zhangxinxu.com/wordpress/2…</a></p>
<h1 data-id="heading-0">SVG animation with SMIL</h1>
<p>能让<code>SVG</code>不靠<code>JavaScript与CSS</code>就能动起来是因为使用了<code>SMIL（Synchronized Multimedia Integration Language）</code>，是W3C的标准之一，旨在以XML格式提供多媒体的交互表现（白话点其实就是动画），是Web上动画的开路先锋，启发了Web animation与CSS animation。SVG与SMIL的开发团队合作，让SVG能利用SMIL达到如下效果：</p>
<ol>
<li>动画化元素的数值属性（x，y值等等）</li>
<li>动画化元素的transform属性（平移、旋转）</li>
<li>动画化元素颜色</li>
<li>轨迹路线移动动画，类似于CSS中的offset-path</li>
</ol>
<p>光是这些特性就够我们组合出很多种的动画了，还不需要JavaScript与CSS的辅助。
使用方法也不难，只要在SVG元素内置入以下四种元素即可操作动画：</p>
<ul>
<li><code><set></code></li>
<li><code><animate></code></li>
<li><code><animateTransform></code></li>
<li><code><animateMotion></code></li>
</ul>
<p>接着我们针对这四种元素一一介绍。</p>
<h1 data-id="heading-1">SVG animation element介绍与示范</h1>
<h2 data-id="heading-2"><code>\<set></code></h2>
<p>利用元素你能够指定在一段时间后，改变svg的一个属性，例如2秒后将Rick的眼睛变成往下看：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c65e79bd0e4b4e94ef594626608888~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>疑？你说他本来就是往下看的？</p>
<p>那是因为set不会重复执行，从你加载这篇文章到看到这个位置为止，相信已经超过2秒，所以已经是执行后的结果，建议你右键单击->“在新分页中开启图片”，实际体验一下，再不然看看下面的gif也行：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/195ef4d73d4f42a2862c830ef9617146~tplv-k3u1fbpfcp-watermark.image" alt="rick-svg-animation-set.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">相关代码如下：</h3>
<pre><code class="copyable"><circle cx=“56.7573”cy=“92.8179”r=“2”fill=“black”stroke=“black”stroke-width=“1”>
<set attributeName=“cy”to=“105.7318”begin=“2s”/>
</circle>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将元素放在你想要套用效果的svg shape内即可。</p>
<p>attributeName指定你要更动的属性；to代表变化值；begin代表从加载后的什么时候开始执行。</p>
<p>除了attributeName外，有另一个参数叫attributeType，用来告诉浏览器你要动画化的属性值是属于XML（e.g. cy），还是CSS（e.g. opacity），不指定的话，浏览器会自己猜。不过呢，这个参数也已经deprecated了，所以实际上我们不再需要它。</p>
<h2 data-id="heading-4"><animate></h2>
<p><code><animate></code>元素让你能针对单一属性变化套用动画补间效果。用法一样是放在你想要套用效果的svg shape内：</p>
<pre><code class="copyable"><circle cx=“56.7573”cy=“92.8179”r=“2”fill=“black”stroke=“black”stroke-width=“1”>
<animate
attributeName=“cx”from=“56.7573”to=“64.7573”
dur=“2s”repeatCount=“indefinite”/>
</circle>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与相比，多了from属性来指定要从哪个值开始做变化，dur指定动画的执行时间，repeatCount指定要重复几次，这边我们设定indefinite让他无限回放（若看不到效果请以分页开新图片）：</p>
<p>利用animate，让Rick的眼睛向右看。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5114744a857649f2aafcf2b047d09be6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也可以用来改变颜色：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071401588ea54a9388abc9bad1f1cafe~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-color (1).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也因为可以用来改变颜色，所以本来有个元素就被取代掉了，现在已经deprecated了。</p>
<h2 data-id="heading-5"><animateTransform></h2>
<p><code><animateTransform></code>可以用来控制transform属性，用animate无法做到。跟CSS中的transform一样，可以控制translation、scaling、rotation跟skewing。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f50568511ef4017ade599674868c686~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-transform.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以让 Rick 头转起来，
（注：经实测，animateTransform 在手机上似乎不支援，请用桌面版浏览器查看此范例）</p>
<pre><code class="copyable"><animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" begin="0s" dur="10s" repeatCount="indefinite" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面所述，要控制 <code>transform</code> 属性，所以 <code>attributeName="transform"</code>，接着 <code>type</code> 参数就看你想要 transform 的类型是什么，<code>rotate</code>、<code>scale</code> 都可以。其余 <code>from</code>、<code>to</code>、<code>begin</code>、<code>dur</code>等参数都与之前的相同，用来指定动画的起始终点值、时间长度与执行次数。</p>
<h3 data-id="heading-6"><animateMotion></h3>
<p>最后一个元素，<code>animateMotion</code>，让 svg 沿着轨迹 path 移动（若看不到效果请以分页开新图片）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2feb1deaa80b4966a0edf539f1f54bef~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-motion.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--轨迹--></span>
<span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,50 q60,50 100,0 q60,-50 100,0"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"black"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"2"</span> /></span>

<span class="hljs-tag"><<span class="hljs-name">g</span>></span> 
<span class="hljs-comment"><!-- Rick 飞船 svg--></span> 
<span class="hljs-tag"><<span class="hljs-name">animateMotion</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"M10,50 q60,50 100,0 q60,-50 100,0"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> 
<span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span> 
<span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述程式码内的 <code><path> </code>只是为了让大家看清楚路径与实际动画的轨迹无关，实际使用上只要给定 <code>animateMotion</code> 一条 <code>path</code> 属性值，包含 <code>animateMotion</code> 元素的 svg 就会跟着该路径移动。</p>
<p>其他属性值跟其他元素雷同，不过 <code>animateMotion</code> 还有个特别的属性值 <code>rotate</code>，用来指定是否要随着路径移动的同时，选转绑定的 svg 物件，可以设定为 <code>auto</code> 或<code>auto-reverse</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">animateMotion</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"M10,50 q60,50 100,0 q60,-50 100,0"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> 
<span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> <span class="hljs-attr">rotate</span>=<span class="hljs-string">"auto"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，除了给定 <code>path</code> 属性值外，其实也能够利用既有的 <code><path> </code>来当作 <code>animateMotion</code> 的路径，但是得透过 <code>mpath</code> 这个 sub-element：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--轨迹--></span> 
<span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"path1"</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,50 q60,50 100,0 q60,-50 100,0"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"black"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"2"</span> /></span> 

<span class="hljs-tag"><<span class="hljs-name">g</span>></span>
    <span class="hljs-comment"><!-- Rick 飞船 svg--></span> 
    <span class="hljs-tag"><<span class="hljs-name">animateMotion</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span>
    <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">mpath</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#path1"</span> /></span> 
    <span class="hljs-tag"></<span class="hljs-name">animateMotion</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要注意的是，若要使用 <code>xlink:href</code> 来指定连接的 svg 元素，在你的<code> <svg></code> tag 上得先记得宣告 <code>xmlns:xlink="http://www.w3.org/1999/xlink"</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 500 300"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span> <span class="hljs-attr">xmlns:xlink</span>=<span class="hljs-string">"http://www.w3.org/1999/xlink"</span> ></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了 <code>xlink:href</code>，我们也就不用像之前范例中所做的一样，一定得把 <code>animate</code> 元素放在要绑定的 svg shape 内，可以透过 <code>id</code> 与 <code>xlink:href</code> 来连结，例如第一个<code> <set></code> 的范例可改为：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"eyes"</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"56.7573"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"92.8179"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"2"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"black"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"black"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"1"</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">circle</span>></span> 

<span class="hljs-tag"><<span class="hljs-name">set</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#eyes"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"cy"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"105.7318"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"2s"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们介绍完了四种 SVG animation element，除了个别拿来使用外，这些元素是能够组合在一起使用的，就只要个别把对应的 animate element 套用在想要的 svg shape 上即可，举例来说，可以让 Rick 旋转的同时，发色改变、眼睛转动（可右键看 svg 原始码，在里面可以找到多个 animate element）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76d12cdfa1294ee6a1f1ff01c66bc3e3~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-combine.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">SVG SMIL animation 重点参数介绍</h3>
<p>在上面的 Demo 里面，我们可以发现 SVG animate element 有很多参数可以使用，范例中只用到了一部分，但其实这些参数能设定的值都有不少变化，想要清楚知道每一个参数的用途与范例，推荐参考这篇文章 - <code>https://www.zhangxinxu.com/wordpress/2014/08/so-powerful-svg-smil-animation/</code> 写得非常好非常详细。</p>
<h3 data-id="heading-8">from, to, by, values</h3>
<p><code>from</code> 跟 <code>to</code> 在前面的范例中都有看到，功能也如同字面般好懂，就是指定动画变化的移动区间，从（<code>from</code>）某个值变化到（<code>to</code>）另个值；而 <code>by</code> 则是代表位移量，相对于明确告知要变动到哪个值，我们可以用 <code>by</code> 告诉 svg 要变动”多少的量“，例如前面 <code>animateTransform</code> 的例子，我们可以改为：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span>
<span class="hljs-attr">type</span>=<span class="hljs-string">"rotate"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0 0 0"</span> <span class="hljs-attr">by</span>=<span class="hljs-string">"360"</span> 
<span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这边你应该会注意到，<code>by</code> 跟 <code>to</code> 功能上有点重复，所以彼此之间有优先权，如果同时有指定 <code>to</code> 与 <code>by</code>，则只会套用到 <code>to</code> 的值。</p>
<p>再来看看 <code>values</code>，这个刚刚的范例都没出现，它的功用是来补足 <code>from</code>、<code>to</code>、<code>by</code> 的不足。不足的点在于， <code>from</code>、<code>to</code>、<code>by</code> 只能指定两个值之间的变化，从 a 变化到 b，而 <code>values</code> 可以给定多个值，用分号<code>;</code>隔开，就能有 a -> b -> c -> b -> a 这样的变化，举个例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> 
<span class="hljs-attr">type</span>=<span class="hljs-string">"translate"</span> <span class="hljs-attr">values</span>=<span class="hljs-string">"20;120;20"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"3s"</span> 
<span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c582e44e524468799c13a38f6fa0cc4~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-values.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">begin, end</h3>
<p><code>begin</code> 跟 <code>end</code> 分别用来控制何时开始执行动画，何时停止动画，在上面的例子中我们都只用到时间，像是 <code>begin="2s"</code>，但其实这两个参数能给的值有非常多的种类，而且能向 <code>values</code> 一样赋予多个值，只要用<code>;</code>隔开即可：
<code>begin = <offset-value> | <syncbase-value> | <event-value> | <repeat-value> | <accessKey-value> | <wallclock-sync-value></code></p>
<p>每种类型的详细介绍，我推荐直接看网上的整理</p>
<p>这边我只说明几个我觉得比较实用的。</p>
<h2 data-id="heading-10">首先是 <code><syncbase-value></code>。</h2>
<p>从字面有点难懂，主要是用其他 <code>animate</code> 元素的 <code>begin/end</code> 值再做加减，举个例子就比较好懂：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">g</span>></span> 
 <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span>
     <span class="hljs-attr">type</span>=<span class="hljs-string">"scale"</span> 
     <span class="hljs-attr">values</span>=<span class="hljs-string">"1;1.2;1"</span> 
     <span class="hljs-attr">begin</span>=<span class="hljs-string">"ship.end"</span> 
     <span class="hljs-attr">dur</span>=<span class="hljs-string">"3s"</span> 
     <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span> 
<span class="hljs-tag"></<span class="hljs-name">g</span>></span> 

<span class="hljs-comment"><!-- spaceship --></span> 
<span class="hljs-tag"><<span class="hljs-name">g</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ship"</span>
    <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> 
    <span class="hljs-attr">type</span>=<span class="hljs-string">"translate"</span> 
    <span class="hljs-attr">values</span>=<span class="hljs-string">"20;120;20"</span> 
    <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"3s"</span> /></span> 
<span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次范例中的 svg 内有两个 animate 元素，给定针对太空船做动画的元素一个 id 值 <code>ship</code>，然后在 Rick 的动画元素上利用 <code>begin="ship.end"</code>，就可以让 Rick 头的动画等到太空船的动画做完后再启动，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/debae5f184754bd996ba07322fc3287a~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-begin-syncbase.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另一个我觉得实用的值是 <code>event-value</code>，看名字就知道，是可以依照 <code>event</code> 来启动或终结动画，用法与 <code>syncbase-value</code> 雷同，给定元素 id，然后根据该元素触发的事件让动画 <code>begin</code> 或是 end。几乎所有 DOM element 支援的 event 都能使用</p>
<p>最后是 <code>indefinite</code>，如果你的 <code>begin</code> 值为 <code>indefinite</code>，代表无限等待，这时就需要透过 <code>[animate 元素].beginElement() </code>来触发，或是用<code><a></code>tag 的 <code>xlink:href="#[animate 元素 id]"</code> 来启动。</p>
<h3 data-id="heading-11">calcMode, keyTimes, keySplines</h3>
<p>这三个参数主要让你能够更细微的调整动画的速度变化。</p>
<p><code>calcMode</code> 有四种模式：<code>discrete</code>、<code>linear</code>、<code>paced</code>、<code>spline</code>。</p>
<p><strong>discrete</strong> 顾名思义就是离散的，<code>from</code> 值跳到 <code>to</code> 值不做补间; <strong>linear</strong> 跟 <strong>paced</strong> 我觉得效果雷同，都是让让补间动画的速度维持一致（linear）与平均（paced）; <code>spline</code> 则是使用贝式曲线，需要搭配 <code>keyTimes</code> 与 <code>keySplines</code> 来使用。</p>
<p><code>keyTimes</code> 就是关键影格，跟前面提过的 <code>values</code> 一样，可以接受多个以分号区隔的值，定义动画的关键时间点，搭配不同的 <code>calcMode</code> 就能在不同的时间点有不同的速度效果。</p>
<p><code>keySpline</code> 是当你 <code>calcMode</code> 设定为 <code>spline</code> 时，用来定义贝式曲线的四个控制点的。</p>
<p>感兴趣的小伙伴可以直接看这篇文章：<code>https://www.zhangxinxu.com/study/201408/svg-animation-calcmode.html</code></p>
<h3 data-id="heading-12">additive</h3>
<p>看到最后，不知道你会不会有个疑问：如果我想针对同的 SVG shape 的同个属性做多个连续变化时该怎么办？</p>
<p>例如：透过 <code>animateTransform</code> 先将图案放大再位移。</p>
<p>这时就要靠 <code>additive</code> 这个参数出马了，<code>additive</code> 参数告知 SVG 是否要累加（<code>sum</code>）动画效果，或是取代（<code>replace</code>），预设是 <code>replace</code>。</p>
<p>例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> 
<span class="hljs-attr">type</span>=<span class="hljs-string">"scale"</span> 
<span class="hljs-attr">by</span>=<span class="hljs-string">"1.1"</span> 
<span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"5s"</span>
<span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> 
<span class="hljs-attr">additive</span>=<span class="hljs-string">"sum"</span> /></span> 

<span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"rotate"</span> 
<span class="hljs-attr">from</span>=<span class="hljs-string">"0 0 0"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"360 0 0"</span>
<span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"5s"</span> 
<span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> 
<span class="hljs-attr">additive</span>=<span class="hljs-string">"sum"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3fb7160a5f84655aee0e30ea45bfa3e~tplv-k3u1fbpfcp-watermark.image" alt="rick-animate-additive.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">结论</h2>
<p>今天花了不小的篇幅介绍了 SVG SMIL animation，感谢看到这边的各位，制作 Demo 的过程对我来说很有趣，也学习了怎么绘制 SVG，从网路上的其他资源也查到许多详细的资料，收获不少！希望对看到这篇文章的你们也能有所启发，除了常用的 Web animation 与 CSS animation 外，有机会也试试用 SVG 直接作动画吧！</p>
<p><strong>资料来源：</strong>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangxinxu.com%2Fwordpress%2F2014%2F08%2Fso-powerful-svg-smil-animation%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangxinxu.com/wordpress/2014/08/so-powerful-svg-smil-animation/" ref="nofollow noopener noreferrer">www.zhangxinxu.com/wordpress/2…</a></p></div>  
</div>
            