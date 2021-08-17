
---
title: 'Canvas如何开发一个虚拟摇杆'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/343de52e258d481fa7eb190def931e21~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 19:25:07 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/343de52e258d481fa7eb190def931e21~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>一开始就奔着月亮去，</p>
<p>就算失败</p>
<p>也许能收获一颗星星呢。</p>
<p>——克莱门特·斯通</p>
<h2 data-id="heading-1">介绍</h2>
<p>好久没见过萤火虫了。想想童年，在那满是小小流萤的树林里，在黑沉沉的暮色里，他们多么欢乐地展开翅膀！他不是太阳也不是月亮，像繁星一样，带来无尽的欢乐。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/343de52e258d481fa7eb190def931e21~tplv-k3u1fbpfcp-watermark.image" alt="VID_20210817_091716.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虚拟摇杆在移动端游戏，尤其RPG游戏是及其重要的一个组件。我们本期开发一个虚拟摇杆，并且通过它去控制萤火虫的移动。我们大体会分为基础场景的搭建，背景和萤火虫的绘制，虚拟摇杆的实现来完成本次场景。</p>
<h2 data-id="heading-2">开发</h2>
<h3 data-id="heading-3">1.基础场景的搭建</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">html</span>,
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
    <span class="hljs-selector-id">#canvas</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./app.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们依旧基础结构先写出来，利用module模式来导入模块。</p>
<p>接下来先把rocker定义好然后引入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*rocker.js*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rocker</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">ctx</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Rocker;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先开始写主场景逻辑，其实应该把萤火虫单独分出一个类去写，然后实例化去控制的，但是因为整个场景比较小而且本次重点在虚拟摇杆部分所以跟主场景合在一起来写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*app.js*/</span>
<span class="hljs-keyword">import</span> Rocker <span class="hljs-keyword">from</span> <span class="hljs-string">"./js/rocker.js"</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.canvas = <span class="hljs-literal">null</span>;            <span class="hljs-comment">// 画布</span>
    <span class="hljs-built_in">this</span>.ctx = <span class="hljs-literal">null</span>;               <span class="hljs-comment">// 环境</span>
    <span class="hljs-built_in">this</span>.w = <span class="hljs-number">0</span>;                    <span class="hljs-comment">// 画布宽</span>
    <span class="hljs-built_in">this</span>.h = <span class="hljs-number">0</span>;                    <span class="hljs-comment">// 画布高</span>
    <span class="hljs-built_in">this</span>.r = <span class="hljs-number">64</span>;                   <span class="hljs-comment">// 萤火虫发光大小</span>
    <span class="hljs-built_in">this</span>.x = <span class="hljs-number">0</span>;                    <span class="hljs-comment">// 萤火虫x轴坐标</span>
    <span class="hljs-built_in">this</span>.y = <span class="hljs-number">0</span>;                    <span class="hljs-comment">// 萤火虫y轴坐标</span>
    <span class="hljs-built_in">this</span>.speed = <span class="hljs-number">1</span>;                <span class="hljs-comment">// 萤火虫移动速度</span>
    <span class="hljs-built_in">this</span>.textures = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();     <span class="hljs-comment">// 纹理集</span>
    <span class="hljs-built_in">this</span>.spriteData = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();   <span class="hljs-comment">// 精灵数据</span>
    <span class="hljs-built_in">this</span>.rocker = <span class="hljs-literal">null</span>;            <span class="hljs-comment">// 摇杆对象</span>
    <span class="hljs-built_in">this</span>.angle = <span class="hljs-number">0</span>;                <span class="hljs-comment">// 当前角度</span>
    <span class="hljs-built_in">this</span>.gradient = <span class="hljs-literal">null</span>;          <span class="hljs-comment">// 萤火虫发光渐变值</span>
    <span class="hljs-built_in">this</span>.init();
  &#125;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 初始化</span>
    <span class="hljs-built_in">this</span>.canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
    <span class="hljs-built_in">this</span>.ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.reset.bind(<span class="hljs-built_in">this</span>));
    <span class="hljs-built_in">this</span>.reset();
    <span class="hljs-built_in">this</span>.textures.set(<span class="hljs-string">"rocker0"</span>, <span class="hljs-string">"../assets/rocker0.png"</span>);
    <span class="hljs-built_in">this</span>.textures.set(<span class="hljs-string">"rocker1"</span>, <span class="hljs-string">"../assets/rocker1.png"</span>);
    <span class="hljs-built_in">this</span>.load().then(<span class="hljs-built_in">this</span>.render.bind(<span class="hljs-built_in">this</span>));
  &#125;
  <span class="hljs-function"><span class="hljs-title">reset</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 屏幕改变事件</span>
    <span class="hljs-built_in">this</span>.w = <span class="hljs-built_in">this</span>.canvas.width = <span class="hljs-built_in">window</span>.innerWidth;
    <span class="hljs-built_in">this</span>.h = <span class="hljs-built_in">this</span>.canvas.height = <span class="hljs-built_in">window</span>.innerHeight;
    <span class="hljs-built_in">this</span>.x = (<span class="hljs-built_in">this</span>.w - <span class="hljs-built_in">this</span>.r) / <span class="hljs-number">2</span>;
    <span class="hljs-built_in">this</span>.y = (<span class="hljs-built_in">this</span>.h - <span class="hljs-built_in">this</span>.r) / <span class="hljs-number">2</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 加载纹理</span>
    <span class="hljs-keyword">const</span> &#123;textures, spriteData&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> textures.keys()) &#123;
        <span class="hljs-keyword">let</span> _img = <span class="hljs-keyword">new</span> Image();
        spriteData.set(key, _img);
        _img.onload = <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (++n == textures.size)
            resolve();
        &#125;
        _img.src = textures.get(key);
      &#125;
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 主渲染</span>
    <span class="hljs-keyword">const</span> &#123;spriteData, w, h, ctx&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">this</span>.rocker = <span class="hljs-keyword">new</span> Rocker(&#123;
      w,
      h,
      spriteData,
    &#125;).render(ctx);
    <span class="hljs-built_in">this</span>.step();
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawBackground</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-comment">// 绘制背景</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawBall</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-comment">// 绘制萤火虫</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">step</span>(<span class="hljs-params">delta</span>)</span> &#123;
    <span class="hljs-comment">// 重绘</span>
    <span class="hljs-keyword">const</span> &#123;w, h, ctx&#125; = <span class="hljs-built_in">this</span>;
    requestAnimationFrame(<span class="hljs-built_in">this</span>.step.bind(<span class="hljs-built_in">this</span>));
    ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, w, h);
    <span class="hljs-built_in">this</span>.drawBackground();
    <span class="hljs-built_in">this</span>.drawBall();
    <span class="hljs-built_in">this</span>.rocker && <span class="hljs-built_in">this</span>.rocker.draw();
  &#125;
&#125;
<span class="hljs-built_in">window</span>.onload = <span class="hljs-keyword">new</span> Application();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在主场景逻辑定义好了各类变量和渲染重绘事件，并且先把两张虚拟摇杆用到的图片加载好。</p>
<p>虚拟摇杆图片分为外边圆环和内摇杆块，如图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5cd6d4fec044c06b95e9bba6a4d658e~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210817100246.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>加载完图片就会进入主渲染render方法会实例化虚拟摇杆，然后再执行重绘操作，在重绘里面渲染图片和萤火虫以及虚拟摇杆。</p>
<h3 data-id="heading-4">2.背景和萤火虫的绘制</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 绘制背景</span>
<span class="hljs-function"><span class="hljs-title">drawBackground</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;w, h, ctx&#125; = <span class="hljs-built_in">this</span>;
    ctx.fillStyle = <span class="hljs-string">"rgb(24,13,50)"</span>;
    ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, w, h);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 绘制萤火虫</span>
<span class="hljs-function"><span class="hljs-title">drawBall</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;x, y, ctx, r&#125; = <span class="hljs-built_in">this</span>;
    ctx.save();
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.gradient) &#123;
        <span class="hljs-built_in">this</span>.setGradient()
    &#125;
    ctx.fillStyle = <span class="hljs-built_in">this</span>.gradient;
    ctx.translate(x, y);
    ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, r, r);
    ctx.restore();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在我们绘制萤火虫的时候期望他的填充色是一个渐变的从内而外发光的效果。所以接下来，我们要写出<strong>setGradient</strong>方法来改变渐变值<strong>gradient</strong>来付给<strong>fillStyle</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 设置渐变色</span>
<span class="hljs-function"><span class="hljs-title">setGradient</span>(<span class="hljs-params">n = <span class="hljs-number">0</span></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;ctx, r&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">this</span>.gradient = ctx.createRadialGradient(r / <span class="hljs-number">2</span>, r / <span class="hljs-number">2</span>, <span class="hljs-number">0</span>, r / <span class="hljs-number">2</span>, r / <span class="hljs-number">2</span>, r / <span class="hljs-number">2</span>)
    <span class="hljs-built_in">this</span>.gradient.addColorStop(<span class="hljs-number">0</span>, <span class="hljs-string">'rgba(255,255,128,1)'</span>);
    <span class="hljs-built_in">this</span>.gradient.addColorStop(<span class="hljs-number">0.2</span> - n, <span class="hljs-string">`rgba(215,215,0,<span class="hljs-subst">$&#123;<span class="hljs-number">0.7</span> - n * <span class="hljs-number">2</span>&#125;</span>)`</span>);
    <span class="hljs-built_in">this</span>.gradient.addColorStop(<span class="hljs-number">0.5</span> - n * <span class="hljs-number">2</span>, <span class="hljs-string">`rgba(245,245,0,<span class="hljs-subst">$&#123;<span class="hljs-number">0.3</span> - n&#125;</span>)`</span>);
    <span class="hljs-built_in">this</span>.gradient.addColorStop(<span class="hljs-number">0.7</span> - n, <span class="hljs-string">'rgba(255,255,255,0)'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在渐变色不能写死，因为萤火虫飞起来翅膀扇动，会略微影响发光面积，所以在重绘的时候我们再给他个值模拟他的状态改变。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">step</span>(<span class="hljs-params">delta</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;w, h, ctx&#125; = <span class="hljs-built_in">this</span>;
    requestAnimationFrame(<span class="hljs-built_in">this</span>.step.bind(<span class="hljs-built_in">this</span>));
    ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, w, h);
    <span class="hljs-built_in">this</span>.drawBackground();
    <span class="hljs-built_in">this</span>.drawBall();
    <span class="hljs-built_in">this</span>.rocker && <span class="hljs-built_in">this</span>.rocker.draw();
    <span class="hljs-comment">// + 每隔3取模闪动一次</span>
    <span class="hljs-keyword">if</span> (~~delta % <span class="hljs-number">3</span> == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.setGradient(<span class="hljs-number">0.1</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.setGradient()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们就可以看到画面了，萤火虫不断在屏幕中间闪动。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e40fd48e5d244c859a75e595b54d02a8~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210817102054.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.虚拟摇杆的实现</h3>
<p>我们接下来要实现一个虚拟摇杆的类，然后通过它的实例化控制萤火虫使其移动。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rocker</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.w = <span class="hljs-number">0</span>;                             <span class="hljs-comment">// 当前所在场景的宽</span>
    <span class="hljs-built_in">this</span>.h = <span class="hljs-number">0</span>;                             <span class="hljs-comment">// 当前所在场景的高</span>
    <span class="hljs-built_in">this</span>.D = <span class="hljs-number">180</span>;                           <span class="hljs-comment">// 外圆环直径</span>
    <span class="hljs-built_in">this</span>.d = <span class="hljs-number">60</span>;                            <span class="hljs-comment">// 滑块直径</span>
    <span class="hljs-built_in">this</span>.spriteData = <span class="hljs-literal">null</span>;                 <span class="hljs-comment">// 精灵图片数据</span>
    <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>, options);
    <span class="hljs-built_in">this</span>.x = <span class="hljs-number">0</span>;                             <span class="hljs-comment">// 滑块x轴坐标</span>
    <span class="hljs-built_in">this</span>.y = <span class="hljs-number">0</span>;                             <span class="hljs-comment">// 滑块y轴坐标</span>
    <span class="hljs-built_in">this</span>.centerX = <span class="hljs-number">0</span>;                       <span class="hljs-comment">// 中心点x轴坐标</span>
    <span class="hljs-built_in">this</span>.centerY = <span class="hljs-number">0</span>;                       <span class="hljs-comment">// 中心点y轴坐标</span>
    <span class="hljs-built_in">this</span>.padding = <span class="hljs-number">20</span>;                      <span class="hljs-comment">// 外环距离底部的距离</span>
    <span class="hljs-built_in">this</span>.isActive = <span class="hljs-literal">false</span>;                  <span class="hljs-comment">// 是否触发</span>
    <span class="hljs-built_in">this</span>.angle = <span class="hljs-number">0</span>;                         <span class="hljs-comment">// 当前角度</span>
    <span class="hljs-built_in">this</span>.event = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();                 <span class="hljs-comment">// 事件字典</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">ctx</span>)</span> &#123;
    <span class="hljs-comment">// 主渲染</span>
    <span class="hljs-keyword">const</span> &#123;d, h, D, padding&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">this</span>.ctx = ctx;
    <span class="hljs-built_in">this</span>.x = <span class="hljs-built_in">this</span>.centerX = padding + D / <span class="hljs-number">2</span>;      <span class="hljs-comment">// 计算中心点x轴坐标</span>
    <span class="hljs-built_in">this</span>.y = <span class="hljs-built_in">this</span>.centerY = h - padding - D / <span class="hljs-number">2</span>;  <span class="hljs-comment">// 计算中心点y轴坐标</span>
    <span class="hljs-built_in">this</span>.draw();
    <span class="hljs-keyword">let</span> canvas = ctx.canvas;            <span class="hljs-comment">// 获取当前场景画布</span>
    <span class="hljs-comment">// 判断设备环境 </span>
    <span class="hljs-comment">// 1.移动端用触摸事件</span>
    <span class="hljs-keyword">if</span> (navigator.userAgent.match(<span class="hljs-regexp">/(iPhone|iPod|Android|ios)/i</span>)) &#123;
      canvas.addEventListener(<span class="hljs-string">"touchstart"</span>, <span class="hljs-built_in">this</span>._mousedown.bind(<span class="hljs-built_in">this</span>));
      canvas.addEventListener(<span class="hljs-string">"touchmove"</span>, <span class="hljs-built_in">this</span>._mousemove.bind(<span class="hljs-built_in">this</span>));
      canvas.addEventListener(<span class="hljs-string">"touchend"</span>, <span class="hljs-built_in">this</span>._mouseup.bind(<span class="hljs-built_in">this</span>));
    &#125; 
    <span class="hljs-comment">// 2.pc端用鼠标事件 </span>
    <span class="hljs-keyword">else</span> &#123;
      canvas.addEventListener(<span class="hljs-string">"mousedown"</span>, <span class="hljs-built_in">this</span>._mousedown.bind(<span class="hljs-built_in">this</span>));
      canvas.addEventListener(<span class="hljs-string">"mousemove"</span>, <span class="hljs-built_in">this</span>._mousemove.bind(<span class="hljs-built_in">this</span>));
      canvas.addEventListener(<span class="hljs-string">"mouseup"</span>, <span class="hljs-built_in">this</span>._mouseup.bind(<span class="hljs-built_in">this</span>));
      canvas.addEventListener(<span class="hljs-string">"mouseout"</span>, <span class="hljs-built_in">this</span>._mouseup.bind(<span class="hljs-built_in">this</span>));
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">eventName, callback</span>)</span> &#123;
    <span class="hljs-comment">// 伪订阅消息</span>
    <span class="hljs-built_in">this</span>.event.set(eventName, <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> callback && callback(...args))
  &#125;
  <span class="hljs-function"><span class="hljs-title">_mousedown</span>(<span class="hljs-params">e</span>)</span> &#123;
    <span class="hljs-comment">// 输入设备按下</span>
    <span class="hljs-keyword">const</span> &#123;d&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> x = e.offsetX || e.changedTouches[<span class="hljs-number">0</span>].clientX;
    <span class="hljs-keyword">let</span> y = e.offsetY || e.changedTouches[<span class="hljs-number">0</span>].clientY;
    <span class="hljs-keyword">if</span> ((x > <span class="hljs-built_in">this</span>.x - d / <span class="hljs-number">2</span> && x < <span class="hljs-built_in">this</span>.x + d / <span class="hljs-number">2</span>) && (y > <span class="hljs-built_in">this</span>.y - d / <span class="hljs-number">2</span> && y < <span class="hljs-built_in">this</span>.y + d / <span class="hljs-number">2</span>)) &#123;
      <span class="hljs-built_in">this</span>.isActive = <span class="hljs-literal">true</span>;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">_mousemove</span>(<span class="hljs-params">e</span>)</span> &#123;
    <span class="hljs-comment">// 输入设备移动</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isActive) &#123;
      <span class="hljs-keyword">let</span> x = e.offsetX || e.changedTouches[<span class="hljs-number">0</span>].clientX;
      <span class="hljs-keyword">let</span> y = e.offsetY || e.changedTouches[<span class="hljs-number">0</span>].clientY;
​
      <span class="hljs-built_in">this</span>.limitToCircle(&#123;
        x,
        y
      &#125;, <span class="hljs-built_in">this</span>.D / <span class="hljs-number">2</span> - <span class="hljs-built_in">this</span>.d / <span class="hljs-number">2</span>);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">_mouseup</span>(<span class="hljs-params">e</span>)</span> &#123;
    <span class="hljs-comment">// 输入设备抬起或离开</span>
    <span class="hljs-built_in">this</span>.isActive = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">this</span>.x = <span class="hljs-built_in">this</span>.centerX;
    <span class="hljs-built_in">this</span>.y = <span class="hljs-built_in">this</span>.centerY;
  &#125;
  <span class="hljs-function"><span class="hljs-title">limitToCircle</span>(<span class="hljs-params">pos, limitRadius</span>)</span> &#123;
    <span class="hljs-comment">// 判断滑动边界</span>
    <span class="hljs-keyword">const</span> &#123;centerX, centerY&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> dx = pos.x - centerX;
    <span class="hljs-keyword">let</span> dy = pos.y - centerY;
    <span class="hljs-keyword">let</span> _r = <span class="hljs-built_in">Math</span>.sqrt(<span class="hljs-built_in">Math</span>.pow(dx, <span class="hljs-number">2</span>) + <span class="hljs-built_in">Math</span>.pow(dy, <span class="hljs-number">2</span>));
    <span class="hljs-built_in">this</span>.angle = <span class="hljs-built_in">Math</span>.atan2(dy, dx);
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.event.has(<span class="hljs-string">"change"</span>)) <span class="hljs-built_in">this</span>.event.get(<span class="hljs-string">"change"</span>)(<span class="hljs-built_in">this</span>.angle, <span class="hljs-built_in">Math</span>.min(_r,limitRadius) / limitRadius);
    <span class="hljs-keyword">if</span> (_r < limitRadius) &#123;
      <span class="hljs-built_in">this</span>.x = pos.x;
      <span class="hljs-built_in">this</span>.y = pos.y;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.x = centerX + <span class="hljs-built_in">Math</span>.cos(<span class="hljs-built_in">this</span>.angle) * limitRadius;
      <span class="hljs-built_in">this</span>.y = centerY + <span class="hljs-built_in">Math</span>.sin(<span class="hljs-built_in">this</span>.angle) * limitRadius;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">draw</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 主绘制</span>
    <span class="hljs-built_in">this</span>.drawOuter();
    <span class="hljs-built_in">this</span>.drawCenter();
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawOuter</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 绘制外层圆环</span>
    <span class="hljs-keyword">const</span> &#123;ctx, spriteData, D, h, padding&#125; = <span class="hljs-built_in">this</span>;
    ctx.save();
    ctx.translate(padding, h - D - padding);
    ctx.drawImage(spriteData.get(<span class="hljs-string">"rocker0"</span>), <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, D, D);
    ctx.restore();
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawCenter</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 绘制中心滑块</span>
    <span class="hljs-keyword">const</span> &#123;ctx, spriteData, d, x, y&#125; = <span class="hljs-built_in">this</span>;
    ctx.save();
    ctx.translate(x - d / <span class="hljs-number">2</span>, y - d / <span class="hljs-number">2</span>);
    ctx.drawImage(spriteData.get(<span class="hljs-string">"rocker1"</span>), <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, d, d);
    ctx.restore();
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Rocker;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是虚拟摇杆的完整代码。</p>
<p>虚拟摇杆要经过这么几个过程：</p>
<ul>
<li><strong>绘制</strong>：这里不做赘述，就是放上加载好的图片，然后定位上去。</li>
<li><strong>输入事件</strong>：监听输入设备的操作，pc端用鼠标事件监听，移动端用触摸事件监听。所监听的当前点击的是摇杆的滑块，就会激活它用<em><strong>isActive</strong></em>做开关去判断。如果按住且移动的话就不断给他改变坐标，使之看起来跟着输入设备拖动。最后弹起关闭<em><strong>isActive</strong></em>使其失活，回归最初的中心点。</li>
<li><strong>滑动边界与获取角度</strong>：当滑动的时候不让不判断他的极值随时能画出并且如果没有角度我们也没发去给到萤火虫移动的方位。这里我们设置好最大范围<em><strong>limitRadius</strong></em>，再利用两点间距离公司求出当前点到圆心间的距离，如果这个距离大于<em><strong>limitRadius</strong></em>。那么我们还要求出在他方向上圆环的极值点。不过本来也要利用<em><strong>Math.atan2</strong></em>算出x轴在拖动当前点的角度。我们就可以利用这个角度根据三角函数配合<em><strong>limitRadius</strong></em>作为半径，就可以得出所在当前范围的极值点。最后如果大于<em><strong>limitRadius</strong></em>，就把这个极值点返给他，从而现在滑动范围。</li>
<li><strong>发布订阅</strong>：这里我们为了方便，我们只做了简单的一层就当外界注入<em><strong>change</strong></em>事件后我们收集起来。再当滑块的时候判断这个改变事件是否存在，如果存在就把所在的角度和滑动力度返给外界。</li>
</ul>
<p>最后我们在主逻辑上，再次修改主渲染逻辑给他加入虚拟摇杆改变位置事件的监听。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;spriteData, w, h, ctx&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">this</span>.rocker = <span class="hljs-keyword">new</span> Rocker(&#123;
        w,
        h,
        spriteData,
    &#125;).render(ctx);
    <span class="hljs-built_in">this</span>.rocker.on(<span class="hljs-string">"change"</span>, <span class="hljs-function">(<span class="hljs-params">angle, speed</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.angle = angle
        <span class="hljs-built_in">this</span>.speed = speed * <span class="hljs-number">3</span>;
    &#125;)
    <span class="hljs-built_in">this</span>.step();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就得到了角度和速度。</p>
<p>我们接下来，就可以在萤火虫绘制上来改变他的坐标了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">drawBall</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;x, y, ctx, r, angle, speed&#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.rocker && <span class="hljs-built_in">this</span>.rocker.isActive) &#123;
        <span class="hljs-keyword">let</span> vx = speed * <span class="hljs-built_in">Math</span>.cos(angle);
        <span class="hljs-keyword">let</span> vy = speed * <span class="hljs-built_in">Math</span>.sin(angle);
        <span class="hljs-built_in">this</span>.x += vx;
        <span class="hljs-built_in">this</span>.y += vy;
    &#125;
    ctx.save();
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.gradient) &#123;
        <span class="hljs-built_in">this</span>.setGradient()
    &#125;
    ctx.fillStyle = <span class="hljs-built_in">this</span>.gradient;
    ctx.translate(x, y);
    ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, r, r);
    ctx.restore();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很简单，就是判断当前虚拟摇杆如果激活，利用三角函数与其方向和速度上计算出x与y轴的增量使其位移。</p>
<p>写到这里，我们已经从0开始实现了以一个虚拟摇杆并且通过它控制萤火虫的移动，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjsmask%2Ffull%2FExmJzNR" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jsmask/full/ExmJzNR" ref="nofollow noopener noreferrer">在线演示</a></p>
<h2 data-id="heading-6">拓展与延伸</h2>
<p>有了虚拟摇杆这个工具，可以做各式各样的移动端rpg游戏了。但这个涉及到的数学知识有更多的延伸，可以带来更多的想法，比如范围内物体的检测，或者道具的拖动，战棋游戏角色范围内的移动。。</p>
<hr>
<p>其实这个教程最早是设想要写雅木茶的操气弹的通过虚拟摇杆控制气弹，但是怕扑街。。就换做萤火虫了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aca23e2353db48e2992b19db33728150~tplv-k3u1fbpfcp-watermark.image" alt="20ae87d6277f9e2f248b420e1530e924b899f31b.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            