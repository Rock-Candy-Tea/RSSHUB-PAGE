
---
title: '使用transform和left改变位置的性能区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a38c4081014e09a08df91155357b7d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 06 May 2021 00:22:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a38c4081014e09a08df91155357b7d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>现如今大多数设备的屏幕刷新频率是60Hz，也就是每秒钟屏幕刷新60次；因此网页动画的运行速度只要达到60FPS，我们就会觉得动画很流畅。</p>
<p>F（Frames）
P（Per）
S（Second）
指的画面每秒钟传输的帧数，60FPS指的是每秒钟60帧；换算下来每一帧差不多是16毫秒。
(1 秒 = 1000 毫秒) / 60 帧 = 16.66 毫秒/帧
复制代码但通常浏览器需要花费一些时间将每一帧的内容绘制到屏幕上（包括样式计算、布局、绘制、合成等工作），所以通常我们只有10毫秒来执行JS代码。</p>
<p>那么动画只要接近于60FPS就是比较流畅的,对比一下通过position:left
做动画和transform做动画的性能区别</p>
<p><code>假设每个人都是用性能最好的手机,浏览器,我们根本用不着去做性能优化,所以在这里为了效果明显,先将环境配置到较低,较差的情况下测试,动画也不能设置为单一的移动</code></p>
<h3 data-id="heading-0">1如何使用google开发者工具查看帧数</h3>
<blockquote>
<p>1.先按键盘F12, 然后点到performance</p>
</blockquote>
<blockquote>
<p>2.点击刷新按钮再按确定</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a38c4081014e09a08df91155357b7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>3.把鼠标放在下面就是他对应的帧数</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c30afc77644427c8b2aeff3c31237f3~tplv-k3u1fbpfcp-watermark.image" alt="test5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>4.现在的浏览器(google为例)已经默认开启了硬件加速器,所以你去对比left和transform其实效果非常不明显,所以先把这个默认关掉</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ac5ee9d2bc14a46aa31441dc59a9576~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>5.对比效果,应该是在低cpu的情况下测试,将他设置为6</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/111800920c6b45a2ba9d3828e0908696~tplv-k3u1fbpfcp-watermark.image" alt="test7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>6 查看GPU的使用</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0269daa77818436aac9d8a988e2c46ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你是mac,勾选fps meter, 如果你是windows,勾选我上面写的</p>
<p>我是windows,但是我并看不到帧率的时时变化</p>
<blockquote>
<p>7 如果你想查看层级</p>
</blockquote>
<p>检查-> layers -> 选择那个可旋转的 -> 查看元素paint code的变化</p>
<p>如果你发现你没有layers, 可以看看三个点里面的more tools,把layers点出来</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/492f467ea0d54ff389d98c9cd6c7a452~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1c4e6c25f34f9cb2cb68e616a3f91b~tplv-k3u1fbpfcp-watermark.image" alt="4transformcode.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2使用position:left (使用left并没有被提升到复合层)</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"ball-running"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-class">.ball-running</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">animation</span>: run-around <span class="hljs-number">2s</span> linear alternate <span class="hljs-number">100</span>;
    <span class="hljs-attribute">background</span>: red;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  &#125;
  <span class="hljs-keyword">@keyframes</span> run-around &#123;
      <span class="hljs-number">0%</span> &#123;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-number">25%</span> &#123;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">200px</span>;
      &#125;
      <span class="hljs-number">50%</span> &#123;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">200px</span>;
      &#125;
      <span class="hljs-number">75%</span> &#123;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee61e397f1214478a240b9a82efff6fc~tplv-k3u1fbpfcp-watermark.image" alt="3transformcode.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb71ac8c6456424ca66a21834cd46b37~tplv-k3u1fbpfcp-watermark.image" alt="test2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在cpu 4slown down的情况下,我们可以看到上面的FPS刚开始在60左右,后面掉到了4FPS,这个动画是不够流畅的.
帧率呈现出锯齿型</p>
<p>这是对应的帧率</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3048189f78fe474da0f90edfd6b6905e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在cpu6 slow down的帧率下甚至会出现掉帧的情况(下面那些红色的就是dropped frame)</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92c4f6ec83254c72b13e8998eac732d2~tplv-k3u1fbpfcp-watermark.image" alt="test5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">3.使用transform进行做动画(transform提升到了复合层)</h3>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.ball-running</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">animation</span>: run-around <span class="hljs-number">2s</span> linear alternate <span class="hljs-number">100</span>;
    <span class="hljs-attribute">background</span>: red;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  &#125;
  <span class="hljs-keyword">@keyframes</span> run-around &#123; 
      <span class="hljs-number">0%</span> &#123;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-number">25%</span> &#123;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">200px</span>, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-number">50%</span> &#123;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">200px</span>, <span class="hljs-number">200px</span>);
      &#125;
      <span class="hljs-number">75%</span> &#123;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">200px</span>);
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbeb38139ffa47d58d03f4afd34cc2bb~tplv-k3u1fbpfcp-watermark.image" alt="1transformcode.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">4.从层级方向解释transform性能优于left</h3>
<p>建议看这篇文章:
<a href="https://juejin.cn/post/6844903966573068301" target="_blank">浏览器层合成与页面渲染优化</a></p>
<p>基本的渲染流程:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d50136cdd7d486480d233b786fa5397~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从左往右边看,我们可以看到，浏览器渲染过程如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span>解析HTML，生成DOM树，解析CSS，生成CSSOM树
(CSS <span class="hljs-built_in">Object</span> Model ,CSS 对象模型,里面有很多api,包括style rules-内部样式表中所有的CSS规则）
<span class="hljs-number">2.</span>将DOM树和CSSOM树结合，生成渲染树(Render Tree)
<span class="hljs-number">3.</span>Layout(回流):根据生成的渲染树，进行回流(Layout)，得到节点的几何信息（位置，大小）
<span class="hljs-number">4.</span>Painting(重绘):根据渲染树以及回流得到的几何信息，得到节点的绝对像素
<span class="hljs-number">5.</span>display:将像素发送给GPU，展示在页面上。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先了解下什么是渲染层</p>
<pre><code class="hljs language-javscript copyable" lang="javscript">渲染层: 在 DOM 树中每个节点都会对应一个渲染对象（RenderObject），
当它们的渲染对象处于相同的坐标空间（z 轴空间）时，就会形成一个 RenderLayers，也就是渲染层。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">1先不涉及任何的层级问题</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"big"</span>>
  </div>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.big</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background-color</span>: yellow;
    &#125;
    <span class="hljs-selector-class">.small</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">background-color</span>: red;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8df81659b21406192d2ad95b76548c4~tplv-k3u1fbpfcp-watermark.image" alt="1普通的代码.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面来看,只有一个渲染层</p>
<h4 data-id="heading-5">2加上index</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"big"</span>>
  </div>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.big</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">background-color</span>: yellow;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-class">.small</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">background-color</span>: red;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">0px</span>;
      <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10000</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7024f4ffb87f4c18bd1f2b4688ccdcf1~tplv-k3u1fbpfcp-watermark.image" alt="1zindex.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从视觉上来看,small 的div确实是在big之上,但是和big在同一个渲染层上</p>
<h4 data-id="heading-6">3加上transform</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"big"</span>>
  </div>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <style>
    .big &#123;
      <span class="hljs-attr">width</span>: 200px;
      height: 200px;
      background-color: yellow;
      position: relative;
    &#125;
    .small &#123;
      <span class="hljs-attr">width</span>: 100px;
      height: 100px;
      background-color: red;
      position: absolute;
      top: 0px;
      left: 0px;
      z-index: <span class="hljs-number">10000</span>;
      transform: translateZ(<span class="hljs-number">0</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95f123d476d24e43a8f8cc799036ab25~tplv-k3u1fbpfcp-watermark.image" alt="1transform.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如何形成合成层</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9840cae741734fb29ab240fe7fd92b68~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面产生了一个新的层级,也就是合成层</p>
<p>首先，如果你改了一个影响元素布局信息的CSS样式，比如width、height、left、top等（transform除外），那么浏览器会将当前的Layout标记为dirty，因为元素的位置信息变了，将可能会导致整个网页其他元素的位置情况都发生改变，所以需要执行Layout全局重新计算每个元素的位置,如果提升为合成层能够开启gpu加速,并且在渲染的时候不会影响其他的层</p>
<p>并且在使用left的时候,document的paint code一直在变化,而使用transform的paint code一直都是不变的,可看上面的动画gif</p>
<p>有关于层级方面的东西,希望大家共同交流,我觉得自己也没有深刻的了解有些定义,只写了自己会的理解的,希望在查看操作方面能帮到大家</p>
<p>参考:</p>
<blockquote>
<p><a href="https://segmentfault.com/a/1190000021977362" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a><br><a href="https://juejin.cn/post/6844903476506394638#heading-5" target="_blank">juejin.cn/post/684490…</a><br><a href="https://juejin.cn/post/6844903966573068301" target="_blank">juejin.cn/post/684490…</a></p>
</blockquote></div>  
</div>
            