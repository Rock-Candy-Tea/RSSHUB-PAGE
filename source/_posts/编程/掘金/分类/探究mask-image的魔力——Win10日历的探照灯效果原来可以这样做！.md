
---
title: '探究mask-image的魔力——Win10日历的探照灯效果原来可以这样做！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f130e8923294f79a38801933ae6bd27~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 07:21:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f130e8923294f79a38801933ae6bd27~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简要介绍</h2>
<p>字面上理解是遮罩的意思。熟悉PS的小伙伴想必对这“遮罩层”的概念更为清晰，在PS中可称为“蒙版”，它是指定某层的元件的轮廓/alpha通道来作为自己剪影的依据。在CSS中，<code>mask-image</code>这个属性是以<strong>指定元素的透明度作为剪影依据的。</strong></p>
<p>根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fmask-image" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/mask-image" ref="nofollow noopener noreferrer">MDN</a> 上的介绍，<code>mask-image</code> CSS属性用于设置元素上遮罩层的图像。一般来说，使用<code>mask-image</code>的元素通常都有透明的部分，元素用于遮挡在指定的DOM上，<strong>被元素透明部分遮住的部分将不被显示，被不透明部分遮住的部分将显示。</strong> 注意我这里说的是元素，通常是图片，也可以是背景色为渐变的元素，显示的是图片或者背景色。</p>
<p>来一张简单的示意图
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f130e8923294f79a38801933ae6bd27~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3Dmask-image" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=mask-image" ref="nofollow noopener noreferrer">各浏览器兼容性</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c209a465a4d4955a35fef964bbfa7c6~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一个小例子 —— 进度加载动画</h2>
<p>进度条是一个很常见的组件，进度条进度条，一般都是条状的或者好看点可以做成圆环。为了更加个性化，很多开发人员会把加载进度放进Logo中，今天我们就使用<code>mask-image</code>这个属性来模拟一个类似的加载效果。</p>
<p>因为<code>mask-image</code>只会显示不透明的部分，因此，我们只需要准备一个Logo图片，一个具有背景色的DOM，保持Logo层不动，背景DOM动起来就可以实现了。</p>
<ol>
<li>一张具有透明部分的Logo图片</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2ddfd0576243ebb683a113e53ed986~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>HTML结构</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask-layer"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>设置遮罩层<code>mask-layer</code>与背景层<code>box</code>的样式</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.mask-layer</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">background</span>: gray;
    -webkit-<span class="hljs-attribute">mask</span>-image: <span class="hljs-built_in">url</span>(<span class="hljs-string">'mask.png'</span>);
    -webkit-<span class="hljs-attribute">mask</span>-size: <span class="hljs-number">300px</span> <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">#f1c40f</span>,<span class="hljs-number">#e67e22</span>,<span class="hljs-number">#e74c3c</span>);
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">10s</span>;
&#125;

<span class="hljs-keyword">@keyframes</span> move &#123;
    <span class="hljs-selector-tag">from</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(<span class="hljs-number">100%</span>);
    &#125;
    <span class="hljs-selector-tag">to</span>&#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(<span class="hljs-number">0</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">实现效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30814cc201034bbd864b57b3a69403b6~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之前有见过波浪效果的，感兴趣的小伙伴可以试一下~</p>
<h2 data-id="heading-3">另一个例子 —— Win10日历探照灯效果</h2>
<p>先来看看这个效果如何。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23626b332a2a4cf1bf1adca45463306a~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我觉得这个UI真的太棒了！日历元素的边框是可以感知鼠标的，鼠标位置的变化可以照亮周围的边框！虽然不知道它具体是怎么实现的，但我们的<code>mask-image</code>是可以做到类似的效果的！</p>
<h3 data-id="heading-4">思路</h3>
<p>先把表格<code>grid-body</code>使用<code>grid布局</code>搞出来，再在这个表格之上覆盖一层<code>遮罩层 grid-mask</code>，<strong>注意，</strong> 这个<code>遮罩层</code>不仅 <strong>宽高</strong> 要和<code>grid-body</code>保持一致，而且 <strong>外部位置、内部布局</strong> 也要做到一样。也就是说，这两层元素是一定对齐的，一层用于放内容，另一层来展示照亮的边框。</p>
<p>搞定物理布局之后，就要对<code>遮罩层 grid-mask</code>设置<code>mask-image</code>属性了。这里我们就用的不是图片了，而是 <strong>径向渐变背景</strong>，我们绘制出一个圆形渐变背景，半径外的部分设置为<strong>透明</strong>的，这样一来它会遮住下一层的内容而不显示出来，就做出照亮该圆内边框的效果了！</p>
<p>如何感知鼠标？我们只需要对<code>grid-body</code>绑定<code>mousemove事件</code>，根据鼠标的位置，动态地改变<code>遮罩层</code>的位置就好了！</p>
<h3 data-id="heading-5">代码部分</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 为了保持一致，大家都要九个格子哦！ --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-body"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-mask"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>5<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>6<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>7<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>8<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span>9<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.grid-body</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>,<span class="hljs-number">1</span>fr);
    gap: <span class="hljs-number">10px</span>;

    <span class="hljs-attribute">cursor</span>: default;   
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">8</span>);
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">60</span>, <span class="hljs-number">60</span>, <span class="hljs-number">60</span>);   
&#125;

<span class="hljs-selector-class">.grid-item</span>&#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> solid transparent;
&#125;

<span class="hljs-selector-class">.grid-item</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> solid <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">3</span>);
&#125;

<span class="hljs-selector-class">.grid-mask</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">display</span>: grid;
    grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>,<span class="hljs-number">1</span>fr);
    gap: <span class="hljs-number">10px</span>;
    <span class="hljs-comment">/* 上面的代码是为了保持两层一致 */</span>

    <span class="hljs-comment">/* 设置mask-image */</span>
    <span class="hljs-comment">/* 光圈颜色 */</span>
    <span class="hljs-attribute">background</span>: transparent;
    -webkit-<span class="hljs-attribute">mask</span>-image: <span class="hljs-built_in">radial-gradient</span>(circle at center, white <span class="hljs-number">0%</span>, transparent <span class="hljs-number">80px</span>);
    -webkit-<span class="hljs-attribute">mask</span>-repeat: no-repeat;
    -webkit-<span class="hljs-attribute">mask</span>-size: <span class="hljs-number">160px</span> <span class="hljs-number">160px</span>;
    <span class="hljs-attribute">pointer-events</span>: none;
&#125;

<span class="hljs-selector-class">.grid-mask</span> <span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> solid <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">5</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> grid  = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.grid-body'</span>)
<span class="hljs-keyword">let</span> maskLayer = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.grid-mask'</span>)
<span class="hljs-keyword">let</span> bounding = maskLayer.getBoundingClientRect()
grid.addEventListener(<span class="hljs-string">'mousemove'</span>,<span class="hljs-function">(<span class="hljs-params">e</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> x = e.pageX
    <span class="hljs-keyword">let</span> y = e.pageY
    maskLayer.style.webkitMaskPosition = <span class="hljs-string">`<span class="hljs-subst">$&#123;x - bounding.x - <span class="hljs-number">80</span>&#125;</span>px <span class="hljs-subst">$&#123;y -bounding.y - <span class="hljs-number">80</span>&#125;</span>px`</span>;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">实现效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e79700cb2ad14fae8f7a9accaacd0adb~tplv-k3u1fbpfcp-watermark.image" alt="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是用于测试的丐版，后来我仿照Win10日历的风格真的写了个差不多不多不多的高仿版！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f570dfccbf1948a6911ae0b07c811993~tplv-k3u1fbpfcp-watermark.image" alt="7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">参考资料</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fvajoy%2Fp%2F5095511.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/vajoy/p/5095511.html" ref="nofollow noopener noreferrer">www.cnblogs.com/vajoy/p/509…</a></p></div>  
</div>
            