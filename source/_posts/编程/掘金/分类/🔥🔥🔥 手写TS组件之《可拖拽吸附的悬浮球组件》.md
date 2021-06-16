
---
title: '🔥🔥🔥 手写TS组件之《可拖拽吸附的悬浮球组件》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4269'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 05:46:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=4269'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">《手写可拖拽吸附的悬浮球组件》有点长，但收获满满</h3>
<p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h4 data-id="heading-1">前言</h4>
<p>目前，前端生态圈中各种各样的UI framework 触目皆是，但有没有发现很多的UI framework 都没有悬浮球这个组件 ，其实这个也不难实现，所以我决定要亲手写一个出来！</p>
<h4 data-id="heading-2">实现思路</h4>
<ol>
<li>获取屏幕的<code>width</code> 和<code>height</code>，即得到悬浮球移动的范围</li>
<li>利用CSS中的<code>position</code>的<code>absolute</code>属性，同时搭配<code>left</code>和<code>top</code>属性来实现元素位置</li>
</ol>
<h4 data-id="heading-3">拖拽事件的过程</h4>
<blockquote>
<p>选中元素 > 拖动元素 > 拖动结束</p>
</blockquote>
<h4 data-id="heading-4">开始我们的主题</h4>
<blockquote>
<p>实现一个类，让用户传入需要拖动的DOM元素</p>
</blockquote>
<p>先定义一个类并导出，这个类命名为<code>Drag</code>,并先定义一些必要的属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Drag</span></span>&#123;
  <span class="hljs-comment">// 元素</span>
  <span class="hljs-attr">element</span>: HTMLElement;

  <span class="hljs-comment">// 屏幕尺寸</span>
  screenWidth: <span class="hljs-built_in">number</span>;

  screenHeight: <span class="hljs-built_in">number</span>;

  <span class="hljs-comment">// 元素大小</span>
  elementWidth: <span class="hljs-built_in">number</span>;

  elementHeight: <span class="hljs-built_in">number</span>;

  isPhone: <span class="hljs-built_in">boolean</span>;

  <span class="hljs-comment">// 当前元素坐标</span>
  elementX: <span class="hljs-built_in">number</span>;

  elementY: <span class="hljs-built_in">number</span>;

  <span class="hljs-comment">// 元素offset</span>
  elementOffsetX: <span class="hljs-built_in">number</span>;

  elementOffsetY: <span class="hljs-built_in">number</span>;

  <span class="hljs-comment">// 是否处于拖动状态</span>
  moving: <span class="hljs-built_in">boolean</span>;

  <span class="hljs-comment">// 吸附</span>
  autoAdsorbent: <span class="hljs-built_in">boolean</span>;

  <span class="hljs-comment">// 隐藏</span>
  hideOffset: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>Drag</code>类中，创建一个构造函数，声明需要传入的参数，元素是必不可少的，所以我们第一个参数就是DOM元素了</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element: HTMLElement</span>)</span> &#123;
<span class="hljs-comment">//  我需要传入一个DOM元素，它是被用户拖动的元素</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>初始化一些参数
<ul>
<li>获取屏幕的宽高</li>
<li>获取元素的宽高</li>
<li>判断设备，如果是电脑端设备则抛出一个<code>error</code></li>
<li>将元素<code>position</code>属性的值设定为<code>absolute</code></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element: HTMLElement</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.element = element;
    <span class="hljs-built_in">this</span>.screenWidth = <span class="hljs-built_in">window</span>.innerWidth || <span class="hljs-built_in">window</span>.outerWidth || <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.screenHeight = <span class="hljs-built_in">window</span>.innerHeight || <span class="hljs-built_in">window</span>.outerHeight || <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.elementWidth = <span class="hljs-built_in">this</span>.element.offsetWidth || <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.elementHeight = <span class="hljs-built_in">this</span>.element.offsetHeight || <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.isPhone = <span class="hljs-regexp">/(iPhone|iPad|iPod|iOS|Android)/i</span>.test(navigator.userAgent);
    <span class="hljs-built_in">this</span>.element.style.position = <span class="hljs-string">'absolute'</span>;
    <span class="hljs-built_in">this</span>.elementX = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.elementY = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.elementOffsetX = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.elementOffsetY = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>.moving = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isPhone) &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'警告！！当前插件版本只兼容移动端'</span>);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>定义一个<code>watchTouch</code>方法，用来给拖拽元素添加事件
<ul>
<li>这里还有个点需要注意，<strong><code>touchEvent</code>是不能直接获取到元素的offset值的</strong>，所以我们利用了<code>touchObject.pageX / touchObject.pageY - DOMRect.left / DOMRect.top</code> 来获得元素<code>offset</code>值</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">private</span> watchTouch(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-built_in">this</span>.element.addEventListener(<span class="hljs-string">'touchstart'</span>, <span class="hljs-function">(<span class="hljs-params">event: TouchEvent</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> rect = (event.target <span class="hljs-keyword">as</span> HTMLElement).getBoundingClientRect();
      <span class="hljs-comment">// 页面被卷去的高度</span>
      <span class="hljs-comment">// 不兼容IE</span>
      <span class="hljs-keyword">const</span> docScrollTop = <span class="hljs-built_in">document</span>.documentElement.scrollTop;
      <span class="hljs-built_in">this</span>.elementOffsetX = event.targetTouches[<span class="hljs-number">0</span>].pageX - rect.left;
      <span class="hljs-built_in">this</span>.elementOffsetY = event.targetTouches[<span class="hljs-number">0</span>].pageY - rect.top - docScrollTop;
      <span class="hljs-built_in">this</span>.moving = <span class="hljs-literal">true</span>;
      <span class="hljs-built_in">this</span>.element.addEventListener(<span class="hljs-string">'touchmove'</span>, <span class="hljs-built_in">this</span>.move.bind(<span class="hljs-built_in">this</span>), &#123; <span class="hljs-attr">passive</span>: <span class="hljs-literal">false</span> &#125;);
    &#125;);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'touchend'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.moving = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'touchmove'</span>, <span class="hljs-built_in">this</span>.move);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>定义一个设定元素位置方法，传入<code>x</code>和<code>y</code>来设定<code>left</code>和<code>top</code>值</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-keyword">private</span> setElementPosition(x: <span class="hljs-built_in">number</span>, <span class="hljs-attr">y</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-comment">// 溢出处理</span>
    <span class="hljs-comment">// 溢出范围</span>
    <span class="hljs-comment">// 但页面超出屏幕范围，计算当前屏幕范围</span>
    <span class="hljs-keyword">const</span> leftScope = <span class="hljs-built_in">this</span>.moving ? <span class="hljs-number">0</span> : <span class="hljs-number">0</span> - <span class="hljs-built_in">this</span>.hideOffset;
    <span class="hljs-comment">// 当前屏幕right最大值</span>
    <span class="hljs-keyword">const</span> rs = <span class="hljs-built_in">this</span>.screenWidth - <span class="hljs-built_in">this</span>.elementWidth;
    <span class="hljs-keyword">const</span> rightScope = <span class="hljs-built_in">this</span>.moving ? rs : rs + <span class="hljs-built_in">this</span>.hideOffset;
    <span class="hljs-keyword">const</span> bottomScope = <span class="hljs-built_in">this</span>.screenHeight - <span class="hljs-built_in">this</span>.elementHeight;
    <span class="hljs-keyword">if</span> (x <= leftScope && y <= <span class="hljs-number">0</span>) &#123;
      [x, y] = [leftScope, <span class="hljs-number">0</span>];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (x >= rightScope && y <= <span class="hljs-number">0</span>) &#123;
      [x, y] = [rightScope, <span class="hljs-number">0</span>];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (x <= leftScope && y >= bottomScope) &#123;
      [x, y] = [leftScope, bottomScope];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (x >= rightScope && y >= bottomScope) &#123;
      [x, y] = [rightScope, bottomScope];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (x > rightScope) &#123;
      x = rightScope;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (y > bottomScope) &#123;
      y = bottomScope;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (x <= leftScope) &#123;
      x = leftScope;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (y <= <span class="hljs-number">0</span>) &#123;
      y = <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-built_in">this</span>.elementX = x;
    <span class="hljs-built_in">this</span>.elementY = y;
    <span class="hljs-built_in">this</span>.element.style.top = <span class="hljs-string">`<span class="hljs-subst">$&#123;y&#125;</span>px`</span>;
    <span class="hljs-built_in">this</span>.element.style.left = <span class="hljs-string">`<span class="hljs-subst">$&#123;x&#125;</span>px`</span>;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>定义一个<code>move</code>方法，它将调用上面设定的<code>setElementPosition</code>方法</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">private</span> move(event: TouchEvent): <span class="hljs-built_in">void</span> &#123;
    event.preventDefault();
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.moving) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.elementY = (event.touches[<span class="hljs-number">0</span>].pageX - <span class="hljs-built_in">this</span>.elementOffsetX);
    <span class="hljs-built_in">this</span>.elementX = (event.touches[<span class="hljs-number">0</span>].pageY - <span class="hljs-built_in">this</span>.elementOffsetY);
    <span class="hljs-keyword">const</span> ex = (event.touches[<span class="hljs-number">0</span>].pageX - <span class="hljs-built_in">this</span>.elementOffsetX);
    <span class="hljs-keyword">const</span> ey = (event.touches[<span class="hljs-number">0</span>].pageY - <span class="hljs-built_in">this</span>.elementOffsetY);
    <span class="hljs-built_in">this</span>.setElementPosition(ex, ey);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">到了这里我们的组件已经可以实现简单的拖拽了！</h4>
<h4 data-id="heading-6">但这还达不到我们前面说到的吸附功能</h4>
<p>我们继续给<code>Drag</code>类添加个吸附功能</p>
<ul>
<li>吸附思路
<ul>
<li>当<code>touchend</code>事件触发时，我们需要判断当前元素与屏幕之间，悬靠在哪一边更近一些
<ul>
<li><code>const screenCenterY = Math.round(this.screenWidth / 2);</code></li>
<li><code>this.elementX < screenCenterY</code></li>
</ul>
</li>
<li>定义一个动画函数，也就是元素从A点到B点的过渡效果（如果没有这一步，很生硬）</li>
<li>定义吸附功能开关</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-keyword">private</span> animate(targetLeft: <span class="hljs-built_in">number</span>, <span class="hljs-attr">spd</span>: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> step = (targetLeft - <span class="hljs-built_in">this</span>.elementX) / <span class="hljs-number">10</span>;
      <span class="hljs-comment">// 对步长进行二次加工(大于0向上取整,小于0向下取整)</span>
      step = step > <span class="hljs-number">0</span> ? <span class="hljs-built_in">Math</span>.ceil(step) : <span class="hljs-built_in">Math</span>.floor(step);
      <span class="hljs-comment">// 动画原理： 目标位置 = 当前位置 + 步长</span>
      <span class="hljs-keyword">const</span> x = <span class="hljs-built_in">this</span>.elementX + step;
      <span class="hljs-built_in">this</span>.setElementPosition(x, <span class="hljs-built_in">this</span>.elementY);
      <span class="hljs-comment">// 检测缓动动画有没有停止</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.abs(targetLeft - <span class="hljs-built_in">this</span>.elementX) <= <span class="hljs-built_in">Math</span>.abs(step)) &#123;
        <span class="hljs-comment">// 处理小数赋值</span>
        <span class="hljs-keyword">const</span> xt = targetLeft;
        <span class="hljs-built_in">this</span>.setElementPosition(xt, <span class="hljs-built_in">this</span>.elementY);
        <span class="hljs-built_in">clearInterval</span>(timer);
      &#125;
    &#125;, spd);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">private</span> adsorbent():<span class="hljs-built_in">void</span> &#123;
    <span class="hljs-comment">// 判断吸附方向</span>
    <span class="hljs-comment">// 屏幕中心点</span>
    <span class="hljs-keyword">const</span> screenCenterY = <span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">this</span>.screenWidth / <span class="hljs-number">2</span>);
    <span class="hljs-comment">// left 最大值</span>
    <span class="hljs-keyword">const</span> rightScope = <span class="hljs-built_in">this</span>.screenWidth - <span class="hljs-built_in">this</span>.elementWidth;
    <span class="hljs-comment">// 根据中心点来判断吸附方向</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.elementX < screenCenterY) &#123;
      <span class="hljs-built_in">this</span>.animate(<span class="hljs-number">0</span> - (<span class="hljs-built_in">this</span>.hideOffset), <span class="hljs-number">10</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.animate(rightScope + (<span class="hljs-built_in">this</span>.hideOffset), <span class="hljs-number">10</span>);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义一个接口<code>interface</code>，作为<code>Drag</code>的第二个参数：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Options &#123;
  autoAdsorbent?: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将前面的<code>constructor</code>方法参数修改为：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-title">constructor</span>(<span class="hljs-params">element: HTMLElement, dConfig: Options = &#123;&#125;</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>Drag</code>类中添加一个<code>autoAdsorbent</code>属性，用于判断用户是否开启了吸附功能</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Drag</span></span>&#123;
  <span class="hljs-comment">// 吸附</span>
  <span class="hljs-attr">autoAdsorbent</span>: <span class="hljs-built_in">boolean</span>;
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>watchTouch</code>方法中，<code>touchend</code>事件加入</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"> <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'touchend'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// ...</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.autoAdsorbent) <span class="hljs-built_in">this</span>.adsorbent();
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里还会有一个小问题，如果用户没有传入<code>dConfig</code>呢？</p>
<p>我们可以在<code>construction</code>方法中补充一句，意思是如果<code>dConfig</code>参数中的<code>autoAdsorbent</code>不存在，则将它设置为<code>false</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">element: HTMLElement, dConfig: Options = &#123;&#125;</span>)</span> &#123;
  dConfig = &#123;<span class="hljs-attr">autoAdsorbent</span>: dConfig.autoAdsorbent || <span class="hljs-literal">false</span>&#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">使用我们的Drag类</h4>
<p>第一步，引入我们写好的<code>Drag</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Drag <span class="hljs-keyword">from</span> <span class="hljs-string">'Drag'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"root"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"BDrag"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.drag</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">238</span>, <span class="hljs-number">238</span>, <span class="hljs-number">238</span>);
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid <span class="hljs-built_in">rgb</span>(<span class="hljs-number">170</span>, <span class="hljs-number">170</span>, <span class="hljs-number">170</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>BetterGraggbleBall</code>提供了一个类，实例化的第一个参数是一个原生DOM元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> BDragDom = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'BDrag'</span>);
<span class="hljs-keyword">const</span> BDrag = <span class="hljs-keyword">new</span> BDrag(BDragDom);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件  GIT地址：<a href="https://github.com/QC2168/better-draggable-ball" target="_blank" rel="nofollow noopener noreferrer">github.com/QC2168/bett…</a></p>
<p>你也可以使用npm直接安装它</p>
<pre><code class="copyable">npm install better-draggable-ball --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">结尾</h4>
<p>如果你觉得该文章对你有帮助，欢迎点个赞👍和关注。</p></div>  
</div>
            