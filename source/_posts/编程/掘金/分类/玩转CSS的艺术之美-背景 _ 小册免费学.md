
---
title: '玩转CSS的艺术之美-背景 _ 小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd3ae48352144816819a1a9bf764e6a7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 03:30:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd3ae48352144816819a1a9bf764e6a7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">CSS背景</h1>
<h2 data-id="heading-1">前言</h2>
<p><code>background</code>这个属性有很多子属性，不过平时主要就用到<code>background-color</code>、<code>background-image</code>和<code>background-repeat</code>三个属性。而其他属性由于不熟悉，每次使用都得翻阅文档并且还不太确定使用是否恰当。借此小册学习机会，容我好好缕一缕。</p>
<h2 data-id="heading-2">一、基础知识</h2>
<h3 data-id="heading-3">1.1 子属性</h3>
<p><code>background-position</code>: 背景图像起始位置，默认<code>0% 0%</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 位置:第二个位置不声明默认是50% */</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
<span class="hljs-comment">/* 关键字:第二个位置不声明默认是center */</span>
<span class="hljs-attribute">background</span>: left top;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>background-size</code>: 背景图像尺寸模式，默认<code>auto</code>自动设置尺寸。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 尺寸:第二个尺寸不声明默认是auto */</span>
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
<span class="hljs-comment">/* 图像扩展至足够大，使其完全覆盖整个区域，图像某些部分也许无法显示在区域中 */</span>
<span class="hljs-attribute">background-size</span>: cover;
<span class="hljs-comment">/* 图像扩展至最大尺寸，使其宽度和高度完全适应整个区域 */</span>
<span class="hljs-attribute">background-size</span>: contain;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>background-origin</code>:定位区域，默认<code>padding-box</code>，图像相对填充定位。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 图像相对边框定位 */</span>
<span class="hljs-attribute">background-origin</span>: border-box;
<span class="hljs-comment">/* 图像相对内容定位 */</span>
<span class="hljs-attribute">background-origin</span>: contenet-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>background-clip</code>:绘制区域，默认<code>border-box</code>,图像被裁剪到边框与边距的交界处。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 图像被裁剪到填充与边框的交界处 */</span>
<span class="hljs-attribute">background-clip</span>: padding-box;
<span class="hljs-comment">/* 图像被裁剪到内容与填充的交界处 */</span>
<span class="hljs-attribute">background-clip</span>: content-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>background-attachment</code>:图像依附方式,默认<code>scroll</code>，图像随页面滚动而移动。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 图像不会随页面滚动而移动 */</span>
<span class="hljs-attribute">background-attachment</span>: fixed;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.2 简写</h3>
<p><code>background</code>子属性连写顺序并无强制标准。</p>
<h4 data-id="heading-5">1.2.1 position和size在连写时使用/衔接起来</h4>
<p>因为<code>position</code>和<code>size</code>都能使用长度单位作为值，通用格式<code>position/size</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.elem</span> &#123;
    <span class="hljs-attribute">background</span>: center/<span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若只出现一组长度单位，默认声明的是<code>position</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* background-position: 背景图像起始位置 */</span>
<span class="hljs-selector-class">.ele</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
&#125;

<span class="hljs-comment">/* background-size: 背景图像尺寸模式 */</span>
<span class="hljs-selector-class">.ele</span> &#123;
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">1.2.2 origin和clip不能加入到属性连写中</h4>
<p>因为两者取值一致。浏览器无法区分。</p>
<h2 data-id="heading-7">二、效果实现</h2>
<h3 data-id="heading-8">2.1 灵活的背景定位</h3>
<p>倘若背景图片需要基于容器右下角进行偏移，但是CSS2是需要我们计算出背景图片距离左上角的偏移量，再赋值给<code>background-position</code>。而CSS3支持在偏移量前面指定关键字。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: red <span class="hljs-built_in">url</span>(<span class="hljs-string">"../assets/images/dect_mgt.jpg"</span>) no-repeat bottom <span class="hljs-number">20px</span> right <span class="hljs-number">20px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd3ae48352144816819a1a9bf764e6a7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2.2 条纹背景</h3>
<p>如果多个色标具有相同的位置，它们会产生一个无限小的过渡区域，过渡的起止色分别是第一个和最后一个指定值。从效果上看，颜色会在那个位置突然变化，而不是一个平滑的渐变过程。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">rgb</span>(<span class="hljs-number">221</span>, <span class="hljs-number">184</span>, <span class="hljs-number">184</span>) <span class="hljs-number">50%</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">103</span>, <span class="hljs-number">103</span>, <span class="hljs-number">179</span>) <span class="hljs-number">50%</span>);
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">10px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1d2c89f05748a3ab3a8272e1a072a9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果某个色标的位置值比整个列表中在它之前的色标的位置值都要
小，则该色标的位置值会被设置为它前面所有色标位置值的最大值。</p>
<p>基于此，以下代码也能实现相同的效果。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">rgb</span>(<span class="hljs-number">221</span>, <span class="hljs-number">184</span>, <span class="hljs-number">184</span>) <span class="hljs-number">50%</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">103</span>, <span class="hljs-number">103</span>, <span class="hljs-number">179</span>) <span class="hljs-number">0</span>);
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">10px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.3 复杂的背景图案</h3>
<p>用 CSS 渐变及<code>background-image</code>来创建任何种类的几何图案。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 波点 */</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(<span class="hljs-number">#fff</span> <span class="hljs-number">30%</span>, transparent <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(<span class="hljs-number">#fff</span> <span class="hljs-number">30%</span>, transparent <span class="hljs-number">0</span>);
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">30px</span> <span class="hljs-number">30px</span>;
<span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>, <span class="hljs-number">15px</span> <span class="hljs-number">15px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6ff274b962946aebed42273a68ce002~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>利用圆锥渐变<code>conic-gradient</code>实现棋盘布局，比线性渐变方便多了。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 棋盘 */</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#eee</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-built_in">repeating-conic-gradient</span>(<span class="hljs-number">#bbb</span> <span class="hljs-number">0</span>, <span class="hljs-number">#bbb</span> <span class="hljs-number">25%</span>, <span class="hljs-number">#eee</span> <span class="hljs-number">0</span>, <span class="hljs-number">#eee</span> <span class="hljs-number">50%</span>);
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">30px</span> <span class="hljs-number">30px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d3ebffb954b4a1ab0612559b5575657~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">2.4 多重背景</h3>
<p>给图片加个遮罩。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: 
    <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">135deg</span>,<span class="hljs-built_in">rgba</span>(<span class="hljs-number">88</span>, <span class="hljs-number">90</span>, <span class="hljs-number">84</span>, <span class="hljs-number">0.5</span>),<span class="hljs-built_in">rgba</span>(<span class="hljs-number">73</span>, <span class="hljs-number">77</span>, <span class="hljs-number">71</span>, <span class="hljs-number">0.5</span>)),<span class="hljs-built_in">url</span>(<span class="hljs-string">"../assets/images/dect_mgt.jpg"</span>) center/cover no-repeat;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee79f1e7e40044f9913139bed8bce537~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">2.5 动态的渐变背景</h3>
<blockquote>
<p>摘抄自小册。</p>
</blockquote>
<p>声明linear-gradient()产生从左上角往右下角的渐变效果，将背景定位在左边，通过animation控制背景定位左右徘徊产生动态的渐变背景。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.gradient-bg</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">135deg</span>, <span class="hljs-number">#f66</span>, <span class="hljs-number">#f90</span>, <span class="hljs-number">#3c9</span>, <span class="hljs-number">#09f</span>, <span class="hljs-number">#66f</span>) left center/<span class="hljs-number">400%</span> <span class="hljs-number">400%</span>;
    <span class="hljs-attribute">font-weight</span>: bold;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">10s</span> infinite;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">background-position</span>-x: left;
    &#125;
    <span class="hljs-number">50%</span> &#123;
        <span class="hljs-attribute">background-position</span>-x: right;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">总结</h2>
<p>倘若真正的掌握了CSS背景的各种属性和用法，真的是可以当画布画画了。</p>
<ul>
<li>参考资料：
<ul>
<li><a href="https://juejin.cn/book/6850413616484040711/section/6850413616576135176" target="_blank">《玩转CSS的艺术之美》</a></li>
<li><a href="http://cdn.lxqnsys.com/CSS%E6%8F%AD%E7%A7%98-%5B%E6%96%87%E5%AD%97%E7%89%88%5D.pdf" target="_blank" rel="nofollow noopener noreferrer">《CSS揭秘》</a></li>
<li><a href="https://www.zhangxinxu.com/wordpress/2020/10/text-as-css-background-image/" target="_blank" rel="nofollow noopener noreferrer">如何让文字作为CSS背景图片显示？</a></li>
</ul>
</li>
</ul>
<p>本文正在参与「掘金小册免费学啦！」活动, 点击查看<a href="https://juejin.cn/post/6943533938090442765" target="_blank">活动详情</a> 。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            