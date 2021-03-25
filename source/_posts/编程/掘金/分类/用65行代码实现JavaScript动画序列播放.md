
---
title: '用65行代码实现JavaScript动画序列播放'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4250'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 19:48:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=4250'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在给学生上课，上周六的第一堂课是关于 JavaScript 动画的内容，其中包括一些简单的动画，比如匀速或者匀加/减速的运动，也包括复杂一些的组合动画。而动画的基本原理，在我<a href="https://www.h5jun.com/post/animations-you-should-know.html" target="_blank" rel="nofollow noopener noreferrer">之前的文章</a>已经有了详细的介绍。在这里，我想谈一谈的是，我们可以如何针对现代浏览器设计更加简单的 API，来实现动画的序列播放。</p>
<h2 data-id="heading-0">基于 Promise 的动画库</h2>
<p>所谓的动画序列，也就是说可以在上一段动画播放结束之后进行下一段动画的播放，这样可以方便用多段动画实现各种不同的复杂效果。而我们不难想到，要实现这个目的，将动画接口实现成 Promise 是一个非常好的方案：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> animator = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">2000</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">let</span> tx = -<span class="hljs-number">100</span> * <span class="hljs-built_in">Math</span>.sin(<span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * p),
      ty = -<span class="hljs-number">100</span> * <span class="hljs-built_in">Math</span>.cos(<span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * p);

  block.style.transform = <span class="hljs-string">'translate('</span> 
    + tx + <span class="hljs-string">'px,'</span> + ty + <span class="hljs-string">'px)'</span>;     
&#125;);

block.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">evt</span>)</span>&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  
  <span class="hljs-comment">//noprotect</span>
  <span class="hljs-keyword">while</span>(<span class="hljs-number">1</span>)&#123;
    <span class="hljs-keyword">await</span> animator.animate()
    block.style.background = [<span class="hljs-string">'red'</span>,<span class="hljs-string">'green'</span>,<span class="hljs-string">'blue'</span>][i++%<span class="hljs-number">3</span>];
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个例子，在支持 async/await 的现代浏览器中代码非常简洁和优雅。如果要兼容旧的浏览器，也并不复杂，只需要<a href="https://github.com/stefanpenner/es6-promise" target="_blank" rel="nofollow noopener noreferrer">针对 es6-promise 做 polyfill</a> 或引入<a href="http://bluebirdjs.com/docs/getting-started.html" target="_blank" rel="nofollow noopener noreferrer">第三方库</a>即可。再来看一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1000</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> tx = <span class="hljs-number">100</span> * p;
  block.style.transform = <span class="hljs-string">'translateX('</span> 
    + tx + <span class="hljs-string">'px)'</span>;     
&#125;);

<span class="hljs-keyword">var</span> a2 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1000</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> ty = <span class="hljs-number">100</span> * p;
  block.style.transform = <span class="hljs-string">'translate(100px,'</span> 
    + ty + <span class="hljs-string">'px)'</span>;     
&#125;);

<span class="hljs-keyword">var</span> a3 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1000</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> tx = <span class="hljs-number">100</span> * (<span class="hljs-number">1</span>-p);
  block.style.transform = <span class="hljs-string">'translate('</span> 
    + tx + <span class="hljs-string">'px, 100px)'</span>;     
&#125;);

<span class="hljs-keyword">var</span> a4 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1000</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> ty = <span class="hljs-number">100</span> * (<span class="hljs-number">1</span>-p);
  block.style.transform = <span class="hljs-string">'translateY('</span>  
    + ty + <span class="hljs-string">'px)'</span>;     
&#125;);


block.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">await</span> a1.animate();
  <span class="hljs-keyword">await</span> a2.animate();
  <span class="hljs-keyword">await</span> a3.animate();
  <span class="hljs-keyword">await</span> a4.animate();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了 Promise，像这样的序列运动非常简单。那么要实现这个动画库，具体该怎么做呢？</p>
<h3 data-id="heading-1">具体实现</h3>
<p>其实整个库实现起来并不复杂，只需要将基础动画封装为 Promise 就可以了。</p>
<p>不过在这里，为了兼容老版本的浏览器，我们先对一些基础函数进行封装：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nowtime</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> performance !== <span class="hljs-string">'undefined'</span> && performance.now)&#123;
    <span class="hljs-keyword">return</span> performance.now();
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Date</span>.now ? <span class="hljs-built_in">Date</span>.now() : (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()).getTime();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们说<strong>动画是关于时间的函数</strong>，因此我们需要一个简单的获取时间功能。在新的 <a href="https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer">requestAnimationFrame 规范</a>中，frame 回调的参数 timestamp 是一个 <a href="https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer">DOMHighResTimeStamp</a> 对象，它比 Date 的计时要更精确（可以精确到纳秒）。因此获取时间我们优先使用 performance.now()，如果浏览器不支持 performance.now()，我们再降级使用 Date.now()。</p>
<p>接下来，我们对 requestAnimationFrame 进行 polyfill：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">global</span>.requestAnimationFrame === <span class="hljs-string">'undefined'</span>)&#123;
  <span class="hljs-built_in">global</span>.requestAnimationFrame = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-comment">//polyfill</span>
      callback.call(<span class="hljs-built_in">this</span>, nowtime());
    &#125;, <span class="hljs-number">1000</span>/<span class="hljs-number">60</span>);
  &#125;
  <span class="hljs-built_in">global</span>.cancelAnimationFrame = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">qId</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">clearTimeout</span>(qId);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，是具体的 Animator 实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animator</span>(<span class="hljs-params">duration, update, easing</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.duration = duration;
  <span class="hljs-built_in">this</span>.update = update;
  <span class="hljs-built_in">this</span>.easing = easing;
&#125;

Animator.prototype = &#123;

  <span class="hljs-attr">animate</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

    <span class="hljs-keyword">var</span> startTime = <span class="hljs-number">0</span>,
        duration = <span class="hljs-built_in">this</span>.duration,
        update = <span class="hljs-built_in">this</span>.update,
        easing = <span class="hljs-built_in">this</span>.easing,
        self = <span class="hljs-built_in">this</span>;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
      <span class="hljs-keyword">var</span> qId = <span class="hljs-number">0</span>;

      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">step</span>(<span class="hljs-params">timestamp</span>)</span>&#123;
        startTime = startTime || timestamp;
        <span class="hljs-keyword">var</span> p = <span class="hljs-built_in">Math</span>.min(<span class="hljs-number">1.0</span>, (timestamp - startTime) / duration);

        update.call(self, easing ? easing(p) : p, p);

        <span class="hljs-keyword">if</span>(p < <span class="hljs-number">1.0</span>)&#123;
          qId = requestAnimationFrame(step);
        &#125;<span class="hljs-keyword">else</span>&#123;
          resolve(self);
        &#125;
      &#125;

      self.cancel = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        cancelAnimationFrame(qId);
        update.call(self, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        reject(<span class="hljs-string">'User canceled!'</span>);
      &#125;

      qId = requestAnimationFrame(step);
    &#125;);
  &#125;,
  <span class="hljs-attr">ease</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">easing</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Animator(<span class="hljs-built_in">this</span>.duration, <span class="hljs-built_in">this</span>.update, easing);
  &#125;
&#125;;

<span class="hljs-built_in">module</span>.exports = Animator;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Animator 构造的时候可以传三个参数，第一个是动画的总时长，第二个是动画每一帧的 update 事件，在这里可以改变元素的属性，从而实现动画，第三个参数是 <a href="http://easings.net/zh-cn" target="_blank" rel="nofollow noopener noreferrer">easing</a>。其中第二个参数 update 事件回调提供两个参数，一是 ep，是经过 easing 之后的动画进程，二是 p，是不经过 easing 的动画进程，ep 和 p 的值都是从 0 开始，到 1 结束。（为什么要使用 ep 和 p，在<a href="https://www.h5jun.com/post/animations-you-should-know.html" target="_blank" rel="nofollow noopener noreferrer">前一个动画教程</a>里已经说明了。）</p>
<p>Animator 有一个 animate 的对象方法，它返回一个 promise，当动画播放完成时，它的 promise 被 resolve，使用者还可以在 promise resolve 前调用 cancel 方法，这样它的 promise 会被 reject。</p>
<p>于是这样，很简单地我们就<strong>通过将 animator 封装为带有返回 Promise 接口的方法</strong>，实现了动画序列。它的实现虽然简单，但功能却是很强大的，用它实现的动画代码也很优雅：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1414</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> ty = <span class="hljs-number">200</span> * p * p;
  block.style.transform = <span class="hljs-string">'translateY('</span> 
    + ty + <span class="hljs-string">'px)'</span>;     
&#125;);

<span class="hljs-keyword">var</span> a2 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">1414</span>,  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> ty = <span class="hljs-number">200</span> - <span class="hljs-number">200</span> * p * (<span class="hljs-number">2</span>-p);
  block.style.transform = <span class="hljs-string">'translateY('</span> 
    + ty + <span class="hljs-string">'px)'</span>;     
&#125;);

block.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  
  <span class="hljs-comment">//noprotect</span>
  <span class="hljs-keyword">while</span>(<span class="hljs-number">1</span>)&#123;
    <span class="hljs-keyword">await</span> a1.animate();
    <span class="hljs-keyword">await</span> a2.animate();
  &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还提供了一个 ease 方法（0.2.0+版），能够传入新的 easing，并返回新的 Animator 对象，这样我们就可以在原动画的基础上扩展我们的动画效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> easeInOutBack = BezierEasing(<span class="hljs-number">0.68</span>, -<span class="hljs-number">0.55</span>, <span class="hljs-number">0.265</span>, <span class="hljs-number">1.55</span>);
<span class="hljs-comment">//easeInOutBack</span>

<span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> Animator(<span class="hljs-number">2000</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ep,p</span>)</span>&#123;
  <span class="hljs-keyword">var</span> x = <span class="hljs-number">200</span> * ep;

  block.style.transform = <span class="hljs-string">'translateX('</span> + x + <span class="hljs-string">'px)'</span>;
&#125;, easeInOutBack);

<span class="hljs-keyword">var</span> a2 = a1.ease(<span class="hljs-function"><span class="hljs-params">p</span> =></span> easeInOutBack(<span class="hljs-number">1</span> - p)); <span class="hljs-comment">//reverse a1</span>

block.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">await</span> a1.animate();
  <span class="hljs-keyword">await</span> a2.animate();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">用 CSS3 如何？</h2>
<p>的确，许多动画可以用 CSS3 来实现。不过 JavaScript 动画与 CSS3 动画有其不同的特点和使用场景。总体来说， CSS3 动画适用于任何纯展现效果的简单动画。虽然它也能提供基本的动画组合方法（有 animationEnd 时间，但标准化较晚），但操作起来依然不方便，而且还需要 JavaScript 来控制。有些动画库用降级的方式，能采用 CSS3 动画的采用 CSS3 动画，不能的自动降级为 JavaScript 动画，这不失为一种好方式，但也有利有弊。因为 CSS3 动画是绑定为操作元素属性的，而 JavaScript 更灵活一些。就像我们这个封装的动画库，其实提供的是更底层的 API，操作的只是<em>时间</em>和<em>进度</em>，并没有耦合任何元素、属性或者其他展示类的东西，因此它完全可以用来操作 DOM、Canvas、SVG、音频/视频流甚至是其他异步动作。另外，如果在动画过程中需要有其他一些精细的动作处理，也还是应该使用 JavaScript 动画而不是 CSS3 动画。</p>
<h2 data-id="heading-3">总结</h2>
<p>使用 Promise 实现的简单动画库，能够很好地执行组合的时序动画，配合 async/await 代码实现简洁且优雅，同时还具有非常好的扩展性，能够组合出非常强大的动画效果。我相信这将成为未来浏览器上 JavaScript 动画的主要实现方式。</p>
<p>最后，可以访问 <a href="https://github.com/akira-cn/animator.js" target="_blank" rel="nofollow noopener noreferrer">GitHub repo</a> 获取最新代码。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            