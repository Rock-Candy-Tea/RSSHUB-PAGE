
---
title: '用 JavaScript 实现手势库 — 事件派发与 Flick 事件【前端组件化】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91b266ee6ecd4dd8b9a074ae6aa1f829~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 02:06:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91b266ee6ecd4dd8b9a074ae6aa1f829~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前端《组件化系列》目录</h1>
<ul>
<li>「一」<a href="https://juejin.cn/post/6915319815041187848" target="_blank">用 JSX 建立组件 Parser（解析器）</a></li>
<li>「二」<a href="https://juejin.cn/post/6918276702061723655" target="_blank">使用 JSX 建立 Markup 组件风格</a></li>
<li>「三」<a href="https://juejin.cn/post/6925698689704919053" target="_blank">用 JSX 实现 Carousel 轮播组件</a></li>
<li>「四」<a href="https://juejin.cn/post/6947519943332069390" target="_blank">用 JavaScript 实现时间轴与动画</a></li>
<li>「五」<a href="https://juejin.cn/post/6950144593711071240" target="_blank">用 JavaScript 实现三次贝塞尔动画库 - 前端组件化</a></li>
<li>「六」<a href="https://juejin.cn/post/6955075376674504712" target="_blank">用 JavaScript 实现手势库 - 实现监听逻辑</a></li>
<li>「七」<a href="https://juejin.cn/post/6958462882388377630" target="_blank">用 JavaScript 实现手势库 — 手势逻辑</a></li>
<li>「八」<a href="https://juejin.cn/post/6960833367579295775" target="_blank">用 JavaScript 实现手势库 — 支持多键触发</a></li>
<li>「九」<a href="https://juejin.cn/post/6964681615494610952" target="_blank">用 JavaScript 实现手势库 — 事件派发与 Flick 事件</a>  《 本期 》</li>
<li>... 待续 ...</li>
</ul>
<p>我们上一期已经实现了所有的 gesture（手势），接下来我们需要实现的就是事件派发的功能。</p>
<h2 data-id="heading-1">事件派发</h2>
<p>在 DOM 里面事件的派发是使用 new Event ， 然后在上面加一些属性，最后把这个事件给派发出去的。</p>
<p>所以我们这里也是一样，建立一个 <code>dsipatch</code> 的函数，并且加入 <code>type</code>、<code>property</code> 这些参数。这里的 property 含有 context 对象和 point 坐标两个属性。</p>
<p>在我们的 <code>dispatch</code> 函数中，首先我们需要做的就是创建一个 event 对象。在新的浏览器 API 中，我们可以直接使用 <code>new Event</code> 来创建。当然我们也可以使用自定义事件来创建 <code>new CustomEvent</code>。那么我们这里，就用普通的 <code>new Event</code> 就好了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">type, properties</span>) </span>&#123;
  <span class="hljs-keyword">let</span> event = <span class="hljs-keyword">new</span> Event(type);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们循环一下 <code>properties</code> 这个对象，把里面的属性都抄写一下。然后我们新创建的 event 是需要挂在一个元素上面，把它挂在到我们之前定义的 <code>element</code> 上即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">type, properties</span>) </span>&#123;
  <span class="hljs-keyword">let</span> event = <span class="hljs-keyword">new</span> Event(type);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> name <span class="hljs-keyword">in</span> properties) &#123;
    event[name] = properties[name];
  &#125;
  element.dispatchEvent(event);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里其实还有一个问题，就是我们之前写的监听都是挂载在 <code>element</code> 之上的。最后我们要把这些都换成挂载在 <code>document</code> 上。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">element.addEventListener(<span class="hljs-string">'mousedown'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  contexts.set(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>, context);

  start(event, context);

  <span class="hljs-keyword">let</span> mousemove = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-keyword">let</span> button = <span class="hljs-number">1</span>;

    <span class="hljs-keyword">while</span> (button <= event.buttons) &#123;
      <span class="hljs-keyword">if</span> (button & event.buttons) &#123;
        <span class="hljs-keyword">let</span> key;
        <span class="hljs-comment">// Order of buttons & button is not the same</span>
        <span class="hljs-keyword">if</span> (button === <span class="hljs-number">2</span>) &#123;
          key = <span class="hljs-number">4</span>;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (button === <span class="hljs-number">4</span>) &#123;
          key = <span class="hljs-number">2</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
          key = button;
        &#125;

        <span class="hljs-keyword">let</span> context = contexts.get(<span class="hljs-string">'mouse'</span> + key);
        move(event, context);
      &#125;
      button = button << <span class="hljs-number">1</span>;
    &#125;
  &#125;;

  <span class="hljs-keyword">let</span> mouseup = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-keyword">let</span> context = contexts.get(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>);
    end(event, context);
    contexts.delete(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>);

    <span class="hljs-keyword">if</span> (event.buttons === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'mousemove'</span>, mousemove);
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'mouseup'</span>, mouseup);
      isListeningMouse = <span class="hljs-literal">false</span>;
    &#125;
  &#125;;

  <span class="hljs-keyword">if</span> (!isListeningMouse) &#123;
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'mousemove'</span>, mousemove);
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'mouseup'</span>, mouseup);
    isListeningMouse = <span class="hljs-literal">true</span>;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们来把 end 函数中的 <code>tap</code> 事件 dipatch（派发）出来试试：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> end = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (context.isTap) &#123;
    <span class="hljs-comment">//console.log('tap');</span>
    <span class="hljs-comment">// 把原先的 console.log 换成 dispatch 调用</span>
    <span class="hljs-comment">// 这个事件不需要任何特殊属性，直接传`空对象`即可</span>
    dispatch(<span class="hljs-string">'tap'</span>, &#123;&#125;)
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-end'</span>);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPress) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-end'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么最后，我们可以尝试在 HTML 中加入一个脚本，在里面监听一下我们新创建的 <code>tap</code> 事件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"gesture.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">oncontextmenu</span>=<span class="hljs-string">"event.preventDefault()"</span>></span><span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">document</span>.documentElement.addEventListener(<span class="hljs-string">'tap'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Tapped!'</span>);
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候，如果我们去浏览器上点击一下，就会触发我们的 <code>tap</code> 事件，并且输出我们的 <code>'Tapped'</code> 消息了！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91b266ee6ecd4dd8b9a074ae6aa1f829~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样我们的派发事件就大功告成了。</p>
<h2 data-id="heading-2">实现一个 flick 事件</h2>
<p>这里我们一起来<strong>完成最后一个</strong>最特别的 flick 事件。Flick 事件在我们所有的事件体系里是比较特殊的，因为它是一个需要判断数独的一个事件。</p>
<p>根据我们前面讲到的，在 <code>pan start</code> 之后，如果我们在手指离开屏幕之前，我们执行了一个快速滑动手指的动作，到达一定的速度以上就会触发我们的 <code>flick</code> 事件，而不是原本的 <code>pan end</code> 的事件。</p>
<p>那么需要如何判断这个速度的？其实可以在我们的 move 函数中，获得当前这一次移动时的速度。但是这个并不能帮助我们去处理，因为如果只按照两个点之间移动时的速度，根据浏览器实现的不同，它会有一个较大的误差。</p>
<p>所以更加准确的方式就是，取数个点，然后用它们之间的平均值作为判定的值。那么要实现这个功能，我们就需要存储一段时间之内的这些点，然后使用这些点来计算出速度的平均值。</p>
<p>有了实现的思路了，我们就来整理下，在代码中怎么去编写这一块的逻辑。</p>
<p>首先我们需要在触发 start 的时候，就把第一个记录点加入到我们的全局 <code>context</code> 之中。而这里需要记录几个值：</p>
<ul>
<li><code>t</code>：代表当前点触发/加入时的时间，这里我们使用 <code>Date.now()</code></li>
<li><code>x</code>：代表当前点 x 轴的坐标</li>
<li><code>y</code>：代表当前点 y 轴的坐标</li>
</ul>
<blockquote>
<p>这些值到了后面都会用来计算移动速度的。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> start = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  (context.startX = point.clientX), (context.startY = point.clientY);

  context.points = [
    &#123;
      <span class="hljs-attr">t</span>: <span class="hljs-built_in">Date</span>.now(),
      <span class="hljs-attr">x</span>: point.clientX,
      <span class="hljs-attr">y</span>: point.clientY,
    &#125;,
  ];

  context.isPan = <span class="hljs-literal">false</span>;
  context.isTap = <span class="hljs-literal">true</span>;
  context.isPress = <span class="hljs-literal">false</span>;

  context.handler = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    context.isPan = <span class="hljs-literal">false</span>;
    context.isTap = <span class="hljs-literal">false</span>;
    context.isPress = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-start'</span>);
    context.handler = <span class="hljs-literal">null</span>;
  &#125;, <span class="hljs-number">500</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后每一次触发 move 的时候，都给当前的 content 放入一个新的点。但是在加入新的点之前，需要过滤一次已经存储的点。我们只需要最近 500 毫秒内的点来计算速度即可，其余的点就可以过滤掉了。</p>
<blockquote>
<p>在执行 flick 动作的时候，我们是不会滑动一个很长的距离和时间的，加上我们是需要捕捉一个快速的滑动动作，这个动作肯定是在 500 毫秒以内的动作，要不也不叫 “快” 了。所以这里就只需要 500 毫秒内的点即可。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> move = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> dx = point.clientX - context.startX,
    dy = point.clientY - context.startY;

  <span class="hljs-keyword">if</span> (!context.isPan && dx ** <span class="hljs-number">2</span> + dy ** <span class="hljs-number">2</span> > <span class="hljs-number">100</span>) &#123;
    context.isPan = <span class="hljs-literal">true</span>;
    context.isTap = <span class="hljs-literal">false</span>;
    context.isPress = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-start'</span>);
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    <span class="hljs-built_in">console</span>.log(dx, dy);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan'</span>);
  &#125;

  context.points = context.points.filter(<span class="hljs-function"><span class="hljs-params">point</span> =></span> <span class="hljs-built_in">Date</span>.now() - point.t < <span class="hljs-number">500</span>);

  context.points.push(&#123;
    <span class="hljs-attr">t</span>: <span class="hljs-built_in">Date</span>.now(),
    <span class="hljs-attr">x</span>: point.clientX,
    <span class="hljs-attr">y</span>: point.clientY,
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 end 事件触发的时候，就可以来计算这次滑动的速度了。因为这里是计算用户滑动时的速度，如果用户是其他类型的手势动作，是不需要去计算速度的。所以这段计算逻辑就可以写在 <code>isPan</code> 成立的判断里面即可。</p>
<p>首先给这个手势动作一个状态变量 <code>isFlick</code>，并且给予它一个默认值为 <code>false</code>。</p>
<p>在计算速度之前，一样需要过滤一次我们 context 中储存的全部的点，把 500 毫秒之外的点过滤掉。</p>
<p>在数学或者物理中，有一个计算速度的公式： <code>速度 = 距离 / 用时</code>。那么这里要去计算速度的话，首先需要计算的就是距离。而这里要计算的是直径距离，所以需要 x 轴和 y 轴的距离的二次幂相加，然后开根号获得的值就是我们要的直径距离。</p>
<p>那么 x 轴距离为例，就是当前点的 x 轴坐标，减去记录中第一个点的 x 轴左边。y 轴的距离就同理可得了。那么有了距离，我们就可以直接从当前点和第一个点的时间差获得 <code>用时</code>。最后就可以运算出速度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> end = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  context.isFlick = <span class="hljs-literal">false</span>;

  <span class="hljs-keyword">if</span> (context.isTap) &#123;
    <span class="hljs-comment">//console.log('tap');</span>
    <span class="hljs-comment">// 把原先的 console.log 换成 dispatch 调用</span>
    <span class="hljs-comment">// 这个事件不需要任何特殊属性，直接传`空对象`即可</span>
    dispatch(<span class="hljs-string">'tap'</span>, &#123;&#125;);
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    context.points = context.points.filter(<span class="hljs-function"><span class="hljs-params">point</span> =></span> <span class="hljs-built_in">Date</span>.now() - point.t < <span class="hljs-number">500</span>);

    <span class="hljs-keyword">let</span> d = <span class="hljs-built_in">Math</span>.sqrt((point.x - context.points[<span class="hljs-number">0</span>].x) ** <span class="hljs-number">2</span> + (point.y - context.points[<span class="hljs-number">0</span>].y) ** <span class="hljs-number">2</span>);
    <span class="hljs-keyword">let</span> v = d / (<span class="hljs-built_in">Date</span>.now() - context.points[<span class="hljs-number">0</span>].t);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPress) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-end'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好样的，这样我们就有两个点之间的 <code>v</code> 速度。那么现在呢，我们需要知道多快的速度才能认为是一个 flick 动作呢？这里就用上帝视角直接得出 1.5 像素每毫秒的速度就是最合适的（这个怎么算出来的？其实我们可以直接 console.log(v)，把速度打印出啦，然后我们手动去测试，就会发现大概 v = 1.5 的时候差不多就是对的了）。</p>
<p>所以我们这里直接就可以判断， 如果 v > 1.5 的话，我们就认为用户的手势就是一个 flick，否则就是普通的 pan-end。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> end = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  context.isFlick = <span class="hljs-literal">false</span>;

  <span class="hljs-keyword">if</span> (context.isTap) &#123;
    <span class="hljs-comment">//console.log('tap');</span>
    <span class="hljs-comment">// 把原先的 console.log 换成 dispatch 调用</span>
    <span class="hljs-comment">// 这个事件不需要任何特殊属性，直接传`空对象`即可</span>
    dispatch(<span class="hljs-string">'tap'</span>, &#123;&#125;);
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    context.points = context.points.filter(<span class="hljs-function"><span class="hljs-params">point</span> =></span> <span class="hljs-built_in">Date</span>.now() - point.t < <span class="hljs-number">500</span>);

    <span class="hljs-keyword">let</span> d = <span class="hljs-built_in">Math</span>.sqrt((point.x - context.points[<span class="hljs-number">0</span>].x) ** <span class="hljs-number">2</span> + (point.y - context.points[<span class="hljs-number">0</span>].y) ** <span class="hljs-number">2</span>);
    <span class="hljs-keyword">let</span> v = d / (<span class="hljs-built_in">Date</span>.now() - context.points[<span class="hljs-number">0</span>].t);

    <span class="hljs-keyword">if</span> (v > <span class="hljs-number">1.5</span>) &#123;
      context.isFlick = <span class="hljs-literal">true</span>;
      dispatch(<span class="hljs-string">'flick'</span>, &#123;&#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
      context.isFlick = <span class="hljs-literal">false</span>;
      dispatch(<span class="hljs-string">'panend'</span>, &#123;&#125;);
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (context.isPress) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-end'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样 flick 事件的处理就完成了，其实这段代码中还有一些 console.log() 是没有被改为使用 dispatch 给派发出去的。但是接下来就要开始看看怎么重新封装这个手势库了，所以这里我们就不一一更改过来先了。</p>
<p>如果想把这里的代码写完整的同学，可以自行把所有的 console.log(事件名) 部分的代码都改正过来哦～</p>
<p>最后附上到此完整的代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> element = <span class="hljs-built_in">document</span>.documentElement;

<span class="hljs-keyword">let</span> contexts = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-keyword">let</span> isListeningMouse = <span class="hljs-literal">false</span>;

element.addEventListener(<span class="hljs-string">'mousedown'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  contexts.set(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>, context);

  start(event, context);

  <span class="hljs-keyword">let</span> mousemove = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-keyword">let</span> button = <span class="hljs-number">1</span>;

    <span class="hljs-keyword">while</span> (button <= event.buttons) &#123;
      <span class="hljs-keyword">if</span> (button & event.buttons) &#123;
        <span class="hljs-keyword">let</span> key;
        <span class="hljs-comment">// Order of buttons & button is not the same</span>
        <span class="hljs-keyword">if</span> (button === <span class="hljs-number">2</span>) &#123;
          key = <span class="hljs-number">4</span>;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (button === <span class="hljs-number">4</span>) &#123;
          key = <span class="hljs-number">2</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
          key = button;
        &#125;

        <span class="hljs-keyword">let</span> context = contexts.get(<span class="hljs-string">'mouse'</span> + key);
        move(event, context);
      &#125;
      button = button << <span class="hljs-number">1</span>;
    &#125;
  &#125;;

  <span class="hljs-keyword">let</span> mouseup = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-keyword">let</span> context = contexts.get(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>);
    end(event, context);
    contexts.delete(<span class="hljs-string">`mouse<span class="hljs-subst">$&#123;<span class="hljs-number">1</span> << event.button&#125;</span>`</span>);

    <span class="hljs-keyword">if</span> (event.buttons === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'mousemove'</span>, mousemove);
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'mouseup'</span>, mouseup);
      isListeningMouse = <span class="hljs-literal">false</span>;
    &#125;
  &#125;;

  <span class="hljs-keyword">if</span> (!isListeningMouse) &#123;
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'mousemove'</span>, mousemove);
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'mouseup'</span>, mouseup);
    isListeningMouse = <span class="hljs-literal">true</span>;
  &#125;
&#125;);

element.addEventListener(<span class="hljs-string">'touchstart'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> touch <span class="hljs-keyword">of</span> event.changedTouches) &#123;
    <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
    contexts.set(event.identifier, context);
    start(touch, context);
  &#125;
&#125;);

element.addEventListener(<span class="hljs-string">'touchmove'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> touch <span class="hljs-keyword">of</span> event.changedTouches) &#123;
    <span class="hljs-keyword">let</span> context = contexts.get(touch.identifier);
    move(touch, context);
  &#125;
&#125;);

element.addEventListener(<span class="hljs-string">'touchend'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> touch <span class="hljs-keyword">of</span> event.changedTouches) &#123;
    <span class="hljs-keyword">let</span> context = contexts.get(touch.identifier);
    end(touch, context);
    contexts.delete(touch.identifier);
  &#125;
&#125;);

element.addEventListener(<span class="hljs-string">'cancel'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> touch <span class="hljs-keyword">of</span> event.changedTouches) &#123;
    <span class="hljs-keyword">let</span> context = contexts.get(touch.identifier);
    cancel(touch, context);
    contexts.delete(touch.identifier);
  &#125;
&#125;);

<span class="hljs-keyword">let</span> start = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  (context.startX = point.clientX), (context.startY = point.clientY);

  context.points = [
    &#123;
      <span class="hljs-attr">t</span>: <span class="hljs-built_in">Date</span>.now(),
      <span class="hljs-attr">x</span>: point.clientX,
      <span class="hljs-attr">y</span>: point.clientY,
    &#125;,
  ];

  context.isPan = <span class="hljs-literal">false</span>;
  context.isTap = <span class="hljs-literal">true</span>;
  context.isPress = <span class="hljs-literal">false</span>;

  context.handler = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    context.isPan = <span class="hljs-literal">false</span>;
    context.isTap = <span class="hljs-literal">false</span>;
    context.isPress = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-start'</span>);
    context.handler = <span class="hljs-literal">null</span>;
  &#125;, <span class="hljs-number">500</span>);
&#125;;

<span class="hljs-keyword">let</span> move = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> dx = point.clientX - context.startX,
    dy = point.clientY - context.startY;

  <span class="hljs-keyword">if</span> (!context.isPan && dx ** <span class="hljs-number">2</span> + dy ** <span class="hljs-number">2</span> > <span class="hljs-number">100</span>) &#123;
    context.isPan = <span class="hljs-literal">true</span>;
    context.isTap = <span class="hljs-literal">false</span>;
    context.isPress = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-start'</span>);
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    <span class="hljs-built_in">console</span>.log(dx, dy);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan'</span>);
  &#125;

  context.points = context.points.filter(<span class="hljs-function"><span class="hljs-params">point</span> =></span> <span class="hljs-built_in">Date</span>.now() - point.t < <span class="hljs-number">500</span>);

  context.points.push(&#123;
    <span class="hljs-attr">t</span>: <span class="hljs-built_in">Date</span>.now(),
    <span class="hljs-attr">x</span>: point.clientX,
    <span class="hljs-attr">y</span>: point.clientY,
  &#125;);
&#125;;

<span class="hljs-keyword">let</span> end = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  context.isFlick = <span class="hljs-literal">false</span>;

  <span class="hljs-keyword">if</span> (context.isTap) &#123;
    <span class="hljs-comment">//console.log('tap');</span>
    <span class="hljs-comment">// 把原先的 console.log 换成 dispatch 调用</span>
    <span class="hljs-comment">// 这个事件不需要任何特殊属性，直接传`空对象`即可</span>
    dispatch(<span class="hljs-string">'tap'</span>, &#123;&#125;);
    <span class="hljs-built_in">clearTimeout</span>(context.handler);
  &#125;

  <span class="hljs-keyword">if</span> (context.isPan) &#123;
    context.points = context.points.filter(<span class="hljs-function"><span class="hljs-params">point</span> =></span> <span class="hljs-built_in">Date</span>.now() - point.t < <span class="hljs-number">500</span>);

    <span class="hljs-keyword">let</span> d, v;
    <span class="hljs-keyword">if</span> (!context.points.length) &#123;
      v = <span class="hljs-number">0</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      d = <span class="hljs-built_in">Math</span>.sqrt(
        (point.clientX - context.points[<span class="hljs-number">0</span>].x) ** <span class="hljs-number">2</span> + (point.clientY - context.points[<span class="hljs-number">0</span>].y) ** <span class="hljs-number">2</span>
      );
      v = d / (<span class="hljs-built_in">Date</span>.now() - context.points[<span class="hljs-number">0</span>].t);
    &#125;

    <span class="hljs-keyword">if</span> (v > <span class="hljs-number">1.5</span>) &#123;
      context.isFlick = <span class="hljs-literal">true</span>;
      dispatch(<span class="hljs-string">'flick'</span>, &#123;&#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
      context.isFlick = <span class="hljs-literal">false</span>;
      dispatch(<span class="hljs-string">'panend'</span>, &#123;&#125;);
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (context.isPress) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-end'</span>);
  &#125;
&#125;;

<span class="hljs-keyword">let</span> cancel = <span class="hljs-function">(<span class="hljs-params">point, context</span>) =></span> &#123;
  <span class="hljs-built_in">clearTimeout</span>(context.handler);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cancel'</span>);
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span>(<span class="hljs-params">type, properties</span>) </span>&#123;
  <span class="hljs-keyword">let</span> event = <span class="hljs-keyword">new</span> Event(type);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> name <span class="hljs-keyword">in</span> properties) &#123;
    event[name] = properties[name];
  &#125;
  element.dispatchEvent(event);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一期，我们就来做手势库的最后一步，封装！～</p>
<blockquote>
<p>我是来自《<strong>技术银河</strong>》的<strong>三钻</strong>，一位正在重塑知识的技术人。下期再见。</p>
</blockquote>
<hr>
<h2 data-id="heading-3">⭐️ 三哥推荐</h2>
<h3 data-id="heading-4">开源项目推荐</h3>
<h4 data-id="heading-5">Hexo Theme Aurora</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc3d2d778a74a858ee3e3b207dcd259~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a48729c651f4af894695969b9eeb077~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在最近在版本 1.5.0 更新了以下功能：</p>
<p>》<a href="https://tridiamond.tech/" target="_blank" rel="nofollow noopener noreferrer">预览</a>《</p>
</blockquote>
<p>:sparkles: 新增</p>
<ul>
<li>自适应 “推荐文章” 布局 (增加了一个新的 “<code>置顶文章布局</code>” !!)
<ul>
<li>能够在“推荐文章”和“置顶文章”模式之间自由切换</li>
<li>如果总文章少于 3 篇，将自动切换到“置顶文章”模式</li>
<li>在文章卡上添加了“置顶”和“推荐”标签</li>
<li><a href="https://aurora.tridiamond.tech/zh/guide/theme.html#%E6%8E%A8%E8%8D%90%E5%B8%83%E5%B1%80%E6%A8%A1%E5%BC%8F" target="_blank" rel="nofollow noopener noreferrer">:book: 文档</a></li>
</ul>
</li>
<li>增加了与 VuePress 一样的自定义容器 <a href="https://github.com/auroral-ui/hexo-theme-aurora/issues/77" target="_blank" rel="nofollow noopener noreferrer">#77</a>
<ul>
<li><code>Info</code> 容器</li>
<li><code>Warning</code> 容器</li>
<li><code>Danger</code> 容器</li>
<li><code>Detail</code> 容器</li>
<li><a href="https://tridiamond.tech/post/aurora%2Fcustom-quotes" target="_blank" rel="nofollow noopener noreferrer">预览</a></li>
</ul>
</li>
<li>支持了更多的 SEO meta 数据 <a href="https://github.com/auroral-ui/hexo-theme-aurora/issues/76" target="_blank" rel="nofollow noopener noreferrer">#76</a>
<ul>
<li>添加了 <code>description</code></li>
<li>添加了 <code>keywords</code></li>
<li>添加了 <code>author</code></li>
<li><a href="https://aurora.tridiamond.tech/zh/guide/site-meta.html#seo-meta" target="_blank" rel="nofollow noopener noreferrer">:book: 文档</a></li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af1d156e01f24630bf1ebb52291c6719~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最近博主在全面投入开发一个可以 “<strong>迈向未来的</strong>” Hexo 主题，以极光为主题的博客主题。</p>
<p>如果你是一个开发者，做一个个人博客也是你简历上的一个亮光点。而如果你有一个超级炫酷的博客，那就更加是亮上加亮了，简直就闪闪发光。</p>
<p>如果喜欢这个主题，可以在 Github 上给我点个 🌟 让彼此都发光吧～</p>
<blockquote>
<p>主题 Github 地址：<a href="https://github.com/auroral-ui/hexo-theme-aurora" target="_blank" rel="nofollow noopener noreferrer">github.com/auroral-ui/…</a>
主题使用文档：<a href="https://aurora.tridiamond.tech/zh/" target="_blank" rel="nofollow noopener noreferrer">aurora.tridiamond.tech/zh/</a></p>
</blockquote>
<hr>
<h4 data-id="heading-6">VSCode Aurora Future</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f88fc3e746774c2aa005f0169a5cfcce~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
对，博主还做了一个 Aurora 的 VSCode 主题。用了Hexo Theme Aurora 相对应的颜色色系。这个主题的重点特性的就只用了 3 个颜色，减少在写代码的时候被多色多彩的颜色所转移了你的注意力，让你更集中在写代码之中。</p>
<p>喜欢的大家可以支持一下哦！ <strong>直接在 VSCode 的插件搜索中输入 “Aurora Future” 即可找到这个主题哦！～</strong></p>
<blockquote>
<p>主题 Github 地址：<a href="https://github.com/auroral-ui/aurora-future-vscode-theme" target="_blank" rel="nofollow noopener noreferrer">github.com/auroral-ui/…</a>
主题插件地址：<a href="https://marketplace.visualstudio.com/items?itemName=auroral-ui.aurora-future" target="_blank" rel="nofollow noopener noreferrer">marketplace.visualstudio.com/items?itemN…</a></p>
</blockquote>
<hr>
<h4 data-id="heading-7">Firefox Aurora Future</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c36a5f509ed24d45aaccf54a615e16f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">我不知道大家，但是最近我在用火狐浏览器来做开发了。个人觉得火狐还真的是不错的。推荐大家尝试一下。</p>
<p>当然我这里想给大家介绍的是我在火狐也做了一个 Aurora 主题。对的！用的是同一套的颜色体系。喜欢的小伙伴可以试一下哦！</p>
<blockquote>
<p>主题地址：<a href="https://addons.mozilla.org/en-US/firefox/addon/aurora-future/" target="_blank" rel="nofollow noopener noreferrer">addons.mozilla.org/en-US/firef…</a></p>
</blockquote>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ee781ce92a74f548f6bd195ab027375~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>博主开始在B站直播学习，欢迎过来《<a href="https://live.bilibili.com/22619211" target="_blank" rel="nofollow noopener noreferrer">直播间</a>》一起学习。</p>
<p>我们在这里互相监督，互相鼓励，互相努力走上人生学习之路，让学习改变我们生活！</p>
<p>学习的路上，很枯燥，很寂寞，但是希望这样可以给我们彼此带来多一点陪伴，多一点鼓励。我们一起加油吧！ (๑ •̀ㅂ•́)و</p>
<hr>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47929919dab74c8f9fa95c20276802a3~tplv-k3u1fbpfcp-watermark.image" alt="掘金关注专栏.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            