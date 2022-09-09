
---
title: '纯CSS实现_流星赶月_，祝大家中秋节快乐'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f965286383ab461e9011b3e54def073a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 09:53:09 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f965286383ab461e9011b3e54def073a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" target="_blank" title="https://juejin.cn/post/7139728821862793223">码上掘金挑战赛来了！</a>”</p>
<p>明天就是中秋节了，就想着用CSS画一个月亮送给掘友们吧。但是就画一个月亮也太简单了些，于是便加了一些星星点缀以及流星坠落的效果。这篇文章就用纯CSS为大家实现一个“流星赶月”的效果。</p>
<h2 data-id="heading-0">实现效果</h2>
<p><span href="https://code.juejin.cn/pen/7141052852553646093" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7141052852553646093" data-src="https://code.juejin.cn/pen/7141052852553646093" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-1">画个月亮</h2>
<p>首先我们先让全屏背景变成黑色，然后实现一个大月亮，并加点"渐变"，“光晕"效果</p>
<ul>
<li>html</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrap"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"moon"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  </body>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
      .<span class="hljs-property">wrap</span> &#123;
        <span class="hljs-attr">background</span>: #<span class="hljs-number">000000</span>;
        <span class="hljs-attr">width</span>: 100vw;
        <span class="hljs-attr">height</span>: 100vh;
        <span class="hljs-attr">position</span>: relative;
      &#125;
      .<span class="hljs-property">moon</span> &#123;
        <span class="hljs-attr">width</span>: 100px;
        <span class="hljs-attr">height</span>: 100px;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        background-<span class="hljs-attr">image</span>: linear-<span class="hljs-title function_">gradient</span>(40deg, #f9fabe, #fffd3b);
        <span class="hljs-attr">position</span>: absolute;
        <span class="hljs-attr">top</span>: <span class="hljs-number">10</span>%;
        <span class="hljs-attr">right</span>: <span class="hljs-number">20</span>%;
        box-<span class="hljs-attr">shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 30px 0px #fffd3b, <span class="hljs-number">0</span> <span class="hljs-number">0</span> 80px <span class="hljs-number">0</span> #ffffff;
      &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时大月亮就出来了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f965286383ab461e9011b3e54def073a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后给月亮加点”忽明忽暗“的动画效果,<strong>brightness</strong>就表示元素的亮度</p>
<pre><code class="hljs language-js copyable" lang="js">      @keyframes moonflashing &#123;
        <span class="hljs-number">0</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">0.8</span>);
        &#125;
        <span class="hljs-number">50</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">1.3</span>);
        &#125;
        <span class="hljs-number">100</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">0.8</span>);
        &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">星星点缀</h2>
<p>天空中只有月亮没有星星怎么能行。我们在天空中加几个星星点缀</p>
<ul>
<li>html</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <div <span class="hljs-keyword">class</span>=<span class="hljs-string">"star star1"</span>></div>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star4"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star5"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star6"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"star star7"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      .<span class="hljs-property">star</span> &#123;
        <span class="hljs-attr">width</span>: 2px;
        <span class="hljs-attr">height</span>: 2px;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        <span class="hljs-attr">background</span>: #ffffff;
        <span class="hljs-attr">position</span>: absolute;
        <span class="hljs-attr">animation</span>: starflashing 2s infinite;
      &#125;
      .<span class="hljs-property">star1</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">50</span>%;
        <span class="hljs-attr">right</span>: <span class="hljs-number">20</span>%;
      &#125;
      .<span class="hljs-property">star2</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">70</span>%;
        <span class="hljs-attr">right</span>: <span class="hljs-number">30</span>%;
      &#125;
      .<span class="hljs-property">star3</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">40</span>%;
        <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>%;
      &#125;
      .<span class="hljs-property">star4</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">60</span>%;
        <span class="hljs-attr">right</span>: <span class="hljs-number">10</span>%;
      &#125;
      .<span class="hljs-property">star5</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">55</span>%;
        <span class="hljs-attr">right</span>: <span class="hljs-number">44</span>%;
      &#125;
      .<span class="hljs-property">star6</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">10</span>%;
        <span class="hljs-attr">left</span>: <span class="hljs-number">30</span>%;
      &#125;
      .<span class="hljs-property">star7</span> &#123;
        <span class="hljs-attr">top</span>: <span class="hljs-number">15</span>%;
        <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>%;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在为星星加上”一闪一闪“的动画</p>
<pre><code class="hljs language-js copyable" lang="js">      @keyframes starflashing &#123;
        <span class="hljs-number">0</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">0.3</span>);
        &#125;
        <span class="hljs-number">50</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">1</span>);
        &#125;
        <span class="hljs-number">100</span>% &#123;
          <span class="hljs-attr">filter</span>: <span class="hljs-title function_">brightness</span>(<span class="hljs-number">0.3</span>);
        &#125;
      &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时天空中便有了一闪一闪亮晶晶的星星</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/160d66f5191141c4952597ce8e4b7a94~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">流星划过</h2>
<p>接下来便是”流星“的实现了，我们先画一个静态的流星，流星包括它的头+尾巴。我们可以先画个流星头</p>
<ul>
<li>html</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <div <span class="hljs-keyword">class</span>=<span class="hljs-string">"meteor"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     .<span class="hljs-property">meteor</span> &#123;
        <span class="hljs-attr">position</span>: absolute;
        <span class="hljs-attr">width</span>: 4px;
        <span class="hljs-attr">height</span>: 4px;
        <span class="hljs-attr">top</span>: <span class="hljs-number">30</span>%;
        <span class="hljs-attr">left</span>: <span class="hljs-number">30</span>%;
        <span class="hljs-attr">background</span>: #ffffff;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        box-<span class="hljs-attr">shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 5px #<span class="hljs-number">636262</span>;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>流星头实现很简单，就是一个圆加些阴影效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a5a46f159c74ec5828733455f8bb8d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后再画它的尾巴。我们可以用它的伪元素实现</p>
<pre><code class="hljs language-css copyable" lang="css">      <span class="hljs-selector-class">.meteor</span><span class="hljs-selector-pseudo">:after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">display</span>: block;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">0px</span> solid <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">border-width</span>: <span class="hljs-number">2px</span> <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">border-color</span>: transparent transparent transparent
          <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.3</span>);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里的色值要用rgba形式，因为需要它的透明效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/843ccddfc3b24ef382d39f69b52f79d8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后再将其旋转45度,再用<code>translate3d</code>进行平移调整对齐</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-attr">transform</span>: <span class="hljs-title function_">rotate</span>(-45deg) <span class="hljs-title function_">translate3d</span>(1px, 1px, <span class="hljs-number">0</span>);
 transform-<span class="hljs-attr">origin</span>: <span class="hljs-number">0</span>% <span class="hljs-number">0</span>%;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d5d71d8ba784e12a2e4be629a126f7c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们要做的就是让流星坠落下去，我们可以先定义一个动画</p>
<pre><code class="hljs language-js copyable" lang="js">      .<span class="hljs-property">meteor</span> &#123;
        <span class="hljs-attr">position</span>: absolute;
        <span class="hljs-attr">width</span>: 4px;
        <span class="hljs-attr">height</span>: 4px;
        <span class="hljs-attr">top</span>: <span class="hljs-number">30</span>%;
        <span class="hljs-attr">left</span>: <span class="hljs-number">30</span>%;
        <span class="hljs-attr">background</span>: #ffffff;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        box-<span class="hljs-attr">shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 5px #<span class="hljs-number">636262</span>;
        <span class="hljs-attr">animation</span>: meteorflashing 3s infinite linear 1s;
      &#125;
    @keyframes meteorflashing &#123;
        <span class="hljs-number">0</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">0</span>) <span class="hljs-title function_">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-number">50</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1</span>) <span class="hljs-title function_">translate3d</span>(-200px, 200px, <span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-number">100</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1</span>) <span class="hljs-title function_">translate3d</span>(-500px, 500px, <span class="hljs-number">0</span>);
        &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候便实现了流星坠落的效果（闭上眼睛想象一下它是动的）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a6b8b7ab594a849a0921a913db6014~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后我们多加一点流星并给它们不同的延迟时间与动画时间</p>
<ul>
<li>html</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <div <span class="hljs-keyword">class</span>=<span class="hljs-string">"meteor meteor1"</span>></div>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"meteor meteor2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"meteor meteor3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"meteor meteor4"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"meteor meteor5"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      .<span class="hljs-property">meteor</span> &#123;
        <span class="hljs-attr">position</span>: absolute;
        <span class="hljs-attr">width</span>: 4px;
        <span class="hljs-attr">height</span>: 4px;
        <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attr">background</span>: #ffffff;
        border-<span class="hljs-attr">radius</span>: <span class="hljs-number">50</span>%;
        box-<span class="hljs-attr">shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 5px 5px #<span class="hljs-number">636262</span>;
      &#125;
      .<span class="hljs-property">meteor</span>:after &#123;
        <span class="hljs-attr">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attr">display</span>: block;
        <span class="hljs-attr">border</span>: 0px solid #fff;
        border-<span class="hljs-attr">width</span>: 2px 100px 2px 100px;
        border-<span class="hljs-attr">color</span>: transparent transparent transparent
          <span class="hljs-title function_">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.3</span>);
        <span class="hljs-attr">transform</span>: <span class="hljs-title function_">rotate</span>(-45deg) <span class="hljs-title function_">translate3d</span>(1px, 1px, <span class="hljs-number">0</span>);
        transform-<span class="hljs-attr">origin</span>: <span class="hljs-number">0</span>% <span class="hljs-number">0</span>%;
      &#125;
      .<span class="hljs-property">meteor1</span> &#123;
        <span class="hljs-attr">top</span>: 2vh;
        <span class="hljs-attr">left</span>: 30vw;
        <span class="hljs-attr">animation</span>: meteorflashing 2s infinite linear 1s;
      &#125;
      .<span class="hljs-property">meteor2</span> &#123;
        <span class="hljs-attr">top</span>: 22vh;
        <span class="hljs-attr">left</span>: 80vw;
        <span class="hljs-attr">background</span>: <span class="hljs-title function_">rgb</span>(<span class="hljs-number">234</span>, <span class="hljs-number">0</span>, <span class="hljs-number">255</span>);
        <span class="hljs-attr">animation</span>: meteorflashing 2s infinite linear 1s;
      &#125;
      .<span class="hljs-property">meteor3</span> &#123;
        <span class="hljs-attr">top</span>: 30vh;
        <span class="hljs-attr">left</span>: 40vw;
        <span class="hljs-attr">animation</span>: meteorflashing 3s infinite linear 2s;
      &#125;
      .<span class="hljs-property">meteor4</span> &#123;
        <span class="hljs-attr">top</span>: 10vh;
        <span class="hljs-attr">left</span>: 50vw;
        <span class="hljs-attr">animation</span>: meteorflashing 3s infinite linear 1s;
      &#125;
      .<span class="hljs-property">meteor5</span> &#123;
        <span class="hljs-attr">top</span>: 50vh;
        <span class="hljs-attr">right</span>: 2vw;
        <span class="hljs-attr">animation</span>: meteorflashing 3s infinite linear 3s;
      &#125;
      @keyframes meteorflashing &#123;
        <span class="hljs-number">0</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">0</span>) <span class="hljs-title function_">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-number">50</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1</span>) <span class="hljs-title function_">translate3d</span>(-200px, 200px, <span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-number">100</span>% &#123;
          <span class="hljs-attr">opacity</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attr">transform</span>: <span class="hljs-title function_">scale</span>(<span class="hljs-number">1</span>) <span class="hljs-title function_">translate3d</span>(-500px, 500px, <span class="hljs-number">0</span>);
        &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ff04aa8154d44e28ca7df8df3a71eae~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">中秋节快乐</h2>
<p>中秋节快到了，我在这里提前祝大家节日快乐，阖家团圆。没什么可送你们的，我就把这轮明月当作节日礼物送给大家了</p></div>  
</div>
            