
---
title: 'Canvas如何做个心电图动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fa358a72b1849649e46d12d53854a69~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 18:06:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fa358a72b1849649e46d12d53854a69~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>爱情所爱的是无限，所畏惧的是界限。</p>
<p>——克尔凯郭尔</p>
<h2 data-id="heading-1">介绍</h2>
<p>本期讲的是绘制一个心电图动画，谁说码农不懂浪漫，只是表达方式特殊而已。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fa358a72b1849649e46d12d53854a69~tplv-k3u1fbpfcp-watermark.image" alt="15dc8c71a2cee83f37e897d5347c0bc2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大致就是以上这样，我会分为基础结构，心的波动，生成心形，来讲解这个案例，准备好做完分享给谁了么，那就出发吧~</p>
<h2 data-id="heading-2">出发</h2>
<h3 data-id="heading-3">1.基础结构</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;

    * &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-selector-tag">html</span>,
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#000</span>;
    &#125;
    <span class="hljs-selector-id">#canvas</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./app.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础的html和css不做赘述，就是做个全屏黑布。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*app.js*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.canvas = <span class="hljs-literal">null</span>;      <span class="hljs-comment">// 画布</span>
    <span class="hljs-built_in">this</span>.ctx = <span class="hljs-literal">null</span>;         <span class="hljs-comment">// 环境</span>
    <span class="hljs-built_in">this</span>.w = <span class="hljs-number">0</span>;              <span class="hljs-comment">// 画布宽</span>
    <span class="hljs-built_in">this</span>.h = <span class="hljs-number">0</span>;              <span class="hljs-comment">// 画布高</span>
    <span class="hljs-built_in">this</span>.speed = <span class="hljs-number">5</span>;          <span class="hljs-comment">// 绘制速度</span>
    <span class="hljs-built_in">this</span>.lineData = [];      <span class="hljs-comment">// 绘制数据</span>
    <span class="hljs-built_in">this</span>.maxHeight = <span class="hljs-number">50</span>;     <span class="hljs-comment">// 波动幅度</span>
    <span class="hljs-built_in">this</span>.active = <span class="hljs-number">0</span>;         <span class="hljs-comment">// 激活状态</span>
    <span class="hljs-built_in">this</span>.heartData = [];     <span class="hljs-comment">// 心形数据</span>
    <span class="hljs-built_in">this</span>.heartR = <span class="hljs-number">7</span>;         <span class="hljs-comment">// 心形半径</span>
    <span class="hljs-built_in">this</span>.dt = <span class="hljs-number">0</span>;             <span class="hljs-comment">// 周期值</span>
    <span class="hljs-built_in">this</span>.x = <span class="hljs-number">0</span>;              <span class="hljs-comment">// 当前x轴坐标</span>
    <span class="hljs-built_in">this</span>.y = <span class="hljs-number">0</span>;              <span class="hljs-comment">// 当前y轴坐标</span>
    <span class="hljs-built_in">this</span>.startX = <span class="hljs-number">0</span>;         <span class="hljs-comment">// 绘制心形起始x轴坐标</span>
    <span class="hljs-built_in">this</span>.startY = <span class="hljs-number">0</span>;         <span class="hljs-comment">// 绘制心形起始y轴坐标</span>
    <span class="hljs-built_in">this</span>.lineColor = <span class="hljs-string">"rgba(218,40,0,1)"</span>;        <span class="hljs-comment">// 线段颜色</span>
    <span class="hljs-built_in">this</span>.shadowColor = <span class="hljs-string">"rgba(255,255,255,.5)"</span>;  <span class="hljs-comment">// 投影色</span>
    <span class="hljs-built_in">this</span>.centerY = <span class="hljs-number">0</span>;        <span class="hljs-comment">// y轴固定点</span>
    <span class="hljs-built_in">this</span>.init();
  &#125;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 初始化</span>
    <span class="hljs-built_in">this</span>.canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
    <span class="hljs-built_in">this</span>.ctx = <span class="hljs-built_in">this</span>.canvas.getContext(<span class="hljs-string">"2d"</span>);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.reset.bind(<span class="hljs-built_in">this</span>));
    <span class="hljs-built_in">this</span>.render();
  &#125;
  <span class="hljs-function"><span class="hljs-title">reset</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 屏幕变化</span>
    <span class="hljs-built_in">this</span>.w = <span class="hljs-built_in">this</span>.canvas.width = <span class="hljs-built_in">this</span>.ctx.width = <span class="hljs-built_in">window</span>.innerWidth;
    <span class="hljs-built_in">this</span>.h = <span class="hljs-built_in">this</span>.canvas.height = <span class="hljs-built_in">this</span>.ctx.height = <span class="hljs-built_in">window</span>.innerHeight;
    <span class="hljs-built_in">this</span>.centerY = <span class="hljs-built_in">this</span>.h / <span class="hljs-number">2</span> + <span class="hljs-built_in">this</span>.heartR*<span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>;
    <span class="hljs-built_in">this</span>.y = <span class="hljs-built_in">this</span>.centerY;
    <span class="hljs-built_in">this</span>.clear();
  &#125;
  <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-comment">// 清空</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 主渲染</span>
    <span class="hljs-built_in">this</span>.reset();
    <span class="hljs-built_in">this</span>.step();
  &#125;
  <span class="hljs-function"><span class="hljs-title">getHeart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 获得心型</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawTopLine</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 绘制白线</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">drawLine</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 绘制红线</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">step</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 重绘</span>
    requestAnimationFrame(<span class="hljs-built_in">this</span>.step.bind(<span class="hljs-built_in">this</span>));
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dt % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">this</span>.drawLine();
      <span class="hljs-built_in">this</span>.drawTopLine();
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.x > <span class="hljs-built_in">this</span>.w + <span class="hljs-built_in">this</span>.speed) &#123;
      <span class="hljs-built_in">this</span>.clear()
    &#125;
    <span class="hljs-built_in">this</span>.dt++
  &#125;
&#125;

<span class="hljs-built_in">window</span>.onload = <span class="hljs-keyword">new</span> Application();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完结构，先说说，我们的期望吧：</p>
<ol>
<li>我们先要绘制一条白色心跳线，他是随机产生的，有峰谷值，每绘制一段后其坐标会存储到lineData里面。</li>
<li>再绘制一条红色心跳线，他不是随机产生的，而是根据lineData里面的数据而绘制，这样就做到了白线先绘制，紧跟着红色线再绘制的效果，这就是心电图的基础动画了。</li>
<li>心形我们要做个完美心形（<a href="https://juejin.cn/post/6995818748191981604" target="_blank" title="https://juejin.cn/post/6995818748191981604">之前七夕有个绘制心形的栗子</a>），拿到心形数据，在白线绘制周期内找个地方塞入执行，就大功告成了。</li>
<li>绘制完心跳后，我们做清空，把他还原回初始状态，再从头重复动画。</li>
</ol>
<h3 data-id="heading-4">2.心的波动</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">drawTopLine</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 白线</span>
    <span class="hljs-keyword">const</span> &#123; ctx, w, h, x, y, shadowColor, maxHeight, lineData, speed, active,centerY &#125; = <span class="hljs-built_in">this</span>;
    lineData.unshift(&#123; x, y &#125;)
    <span class="hljs-keyword">let</span> x1 = x + <span class="hljs-built_in">Math</span>.random() * speed + speed;
    <span class="hljs-keyword">let</span> y1 = centerY;
    <span class="hljs-keyword">if</span> (x1 > w * <span class="hljs-number">0.05</span> && x1 < w * <span class="hljs-number">0.95</span>) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.random() > <span class="hljs-number">0.8</span> && active == <span class="hljs-number">0</span>) &#123;
            y1 += <span class="hljs-built_in">Math</span>.random() * maxHeight * <span class="hljs-number">2</span> - maxHeight
        &#125;
    &#125;
    ctx.lineWidth = <span class="hljs-number">3</span>;
    ctx.strokeStyle = <span class="hljs-string">"rgba(255,255,255,.5)"</span>;
    ctx.lineJoin = <span class="hljs-string">"round"</span>;
    ctx.lineCap = <span class="hljs-string">"round"</span>;
    ctx.shadowBlur = <span class="hljs-number">20</span>;
    ctx.shadowColor = shadowColor;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x1, y1);
    ctx.stroke();
    ctx.closePath();
    <span class="hljs-built_in">this</span>.x = x1;
    <span class="hljs-built_in">this</span>.y = y1;
&#125;
<span class="hljs-function"><span class="hljs-title">drawLine</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 红线</span>
    <span class="hljs-keyword">const</span> &#123; ctx,shadowColor, lineColor, maxHeight, lineData &#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">if</span> (lineData.length < <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span>;
    ctx.lineWidth = <span class="hljs-number">3</span>;
    ctx.strokeStyle = lineColor;
    ctx.lineJoin = <span class="hljs-string">"round"</span>;
    ctx.lineCap = <span class="hljs-string">"round"</span>;
    ctx.shadowBlur = <span class="hljs-number">20</span>;
    ctx.shadowColor = shadowColor;
    ctx.beginPath();
    ctx.moveTo(lineData[<span class="hljs-number">1</span>].x, lineData[<span class="hljs-number">1</span>].y);
    ctx.lineTo(lineData[<span class="hljs-number">0</span>].x, lineData[<span class="hljs-number">0</span>].y);
    ctx.stroke();
    ctx.closePath();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绘制线段我们会每隔一个周期在x轴方向增加一个值，y轴固定，但再某个随机时刻y轴出现加一个随机变量，使其变化，但下次绘制y轴依然以固定值为基础绘制。每次绘制保存绘制记录，给红线使用。值得注意的是，因为绘制一个线段要有两个坐标点，所以红线要在绘制记录两条以上，再开始绘制。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235877fc577441109de10caf530acaf9~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210812093918.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里我们基础的心电图已经做好了，接下来要绘制心形了。</p>
<h3 data-id="heading-5">3.生成心形</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getHeart</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> t = <span class="hljs-built_in">Math</span>.PI + <span class="hljs-number">0.5</span>;
    <span class="hljs-keyword">let</span> maxt = <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">let</span> vt = <span class="hljs-built_in">this</span>.speed/<span class="hljs-number">100</span>;
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> y = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> r = <span class="hljs-built_in">this</span>.heartR;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">Math</span>.ceil(maxt / vt); i++) &#123;
        x = <span class="hljs-number">16</span> * <span class="hljs-built_in">Math</span>.pow(<span class="hljs-built_in">Math</span>.sin(t), <span class="hljs-number">3</span>);
        y = <span class="hljs-number">13</span> * <span class="hljs-built_in">Math</span>.cos(t) - <span class="hljs-number">5</span> * <span class="hljs-built_in">Math</span>.cos(<span class="hljs-number">2</span> * t) - <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.cos(<span class="hljs-number">3</span> * t) - <span class="hljs-built_in">Math</span>.cos(<span class="hljs-number">4</span> * t);
        t += vt;
        x *= r;
        y = -y * r - r * <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">4</span>;
        <span class="hljs-keyword">if</span> (y < <span class="hljs-number">0</span>) &#123;
            <span class="hljs-built_in">this</span>.heartData.push(&#123; x, y &#125;);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先把心形数据不是一个变化值所以先计算并保存起来方便后面绘制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">drawTopLine</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 白线</span>
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">if</span> (x1 > w * <span class="hljs-number">0.05</span> && x1 < w * <span class="hljs-number">0.95</span>) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.random() > <span class="hljs-number">0.8</span> && active == <span class="hljs-number">0</span>) &#123;
        y1 += <span class="hljs-built_in">Math</span>.random() * maxHeight * <span class="hljs-number">2</span> - maxHeight
      &#125;
      <span class="hljs-keyword">if</span> (x1 > w * <span class="hljs-number">0.25</span> && <span class="hljs-built_in">this</span>.active == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.active = <span class="hljs-number">1</span>;
      &#125;
      <span class="hljs-keyword">if</span> (x1 > w * <span class="hljs-number">0.38</span> && <span class="hljs-built_in">this</span>.active == <span class="hljs-number">1</span>) &#123;
        <span class="hljs-built_in">this</span>.active = <span class="hljs-number">2</span>;
        <span class="hljs-built_in">this</span>.startX = x1 + speed * <span class="hljs-number">3</span>;
        <span class="hljs-built_in">this</span>.startY = centerY;
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.heartData.length > <span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.active == <span class="hljs-number">2</span>) &#123;
        <span class="hljs-keyword">let</span> _pos = <span class="hljs-built_in">this</span>.heartData.shift();
        x1 = <span class="hljs-built_in">this</span>.startX + _pos.x;
        y1 = <span class="hljs-built_in">this</span>.startY + _pos.y;
        <span class="hljs-keyword">if</span> (y1 > <span class="hljs-built_in">this</span>.startY) &#123;
          y1 = <span class="hljs-built_in">this</span>.startY;
        &#125;
      &#125;
      <span class="hljs-keyword">if</span> (x1 > <span class="hljs-number">0.55</span> * w && <span class="hljs-built_in">this</span>.heartData.length == <span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.active == <span class="hljs-number">2</span>) &#123;
        <span class="hljs-built_in">this</span>.active = <span class="hljs-number">0</span>;
      &#125;
    &#125;
    <span class="hljs-comment">// ...</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们绘制肯定要在白线当中，控制他的什么时候绘制，绘制多少变回来，属于你自己需求逻辑，这里也不过多赘述。唯一要讲的是要保存起始点，以这个坐标为基础来绘制心形，而不是变化值。绘制前后期望都要来段横线，这样峰谷与心形不会靠的太近。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c6733d00eeb4cf58321e37fd65f9df7~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210830094246.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4.重新绘制</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.heartData.length = <span class="hljs-built_in">this</span>.lineData.length = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.active = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.x = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.getHeart();
    <span class="hljs-built_in">this</span>.ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.w, <span class="hljs-built_in">this</span>.h);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们最后要在屏幕变化或者完全绘制完毕后，重新绘制一遍。所以我们要清空画布，清空数据，状态，横坐标归0。这样就可以反复生成了。</p>
<hr>
<p>这里我们就讲完了，很容易吧，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjsmask%2Ffull%2FPojPeBo" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jsmask/full/PojPeBo" ref="nofollow noopener noreferrer">在线演示</a></p>
<h2 data-id="heading-7">拓展&延伸</h2>
<p>我们做的其实并不完美，还有好多需要处理，比如大量判断逻辑存在与白线内并不好，如果出现剧本这样逻辑过多会爆炸的，而且一些边界限定也没有做。当然如果你想扩展更多效果的话处理这些还是很有必要的。你可以不光画心形，可以生成点阵文字连接起来，好多的创意都可以在这种心电图上实现。</p>
<hr>
<p>希望我们走时不像来时那样空落落。</p></div>  
</div>
            