
---
title: 'JS中的节流与防抖函数记不住？我的答案保你终身难忘【一小时搞懂，建议收藏】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5c5e9eae9741359c5578d3a5b8da44~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 21:56:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5c5e9eae9741359c5578d3a5b8da44~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前端性能优化-防抖和节流</h3>
<p>防抖和节流严格算起来应该属于性能优化的知识，但实际上遇到的频率相当高，处理不当或者放任不管就容易引起浏览器卡死。所以还是很有必要早点掌握的。</p>
<p>据说阿里有一道面试题就是谈谈函数节流和函数防抖。</p>
<h3 data-id="heading-1">防抖（debounce）</h3>
<p>函数防抖（debounce）：当持续触发事件时，在设置的周期内没有再触发事件，事件处理函数才会执行一次，如果设定的周期没有结束，又一次触发了事件，就重新开始延时。</p>
<p>为了有个直观的对比，我们先看下没有使用debounce技术的click事件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5c5e9eae9741359c5578d3a5b8da44~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们看到，当用户频繁点击button按钮时，控制台会频繁的输出结果，这种频繁调用事件处理程序，会加重浏览器的负担，导致用户体验非常糟糕。</p>
<p>为了解决上述问题，我们在编码中可以使用debounce防抖技术。</p>
<blockquote>
<p>防抖原理：是维护一个计时器，在规定的delay时间后触发函数，但是在delay时间内再次触发的话，就会取消之前的计时器而重新设置。这样一来，只有最后一次操作能被触发。</p>
</blockquote>
<p>看一个🌰（栗子）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, delay</span>) </span>&#123;
  <span class="hljs-keyword">var</span> timer = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-comment">// 清除已存在的定时器</span>
     timer && <span class="hljs-built_in">clearTimeout</span>(timer)
     timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        fn.apply(<span class="hljs-built_in">this</span>)
     &#125;, delay)
  &#125;
&#125;
<span class="hljs-keyword">let</span> $btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>);
<span class="hljs-keyword">var</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log (<span class="hljs-string">'防抖旨在时间段内只触发最后一次执行'</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-built_in">Date</span>.now()));
&#125;
$btn.onclick = debounce(fn, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如图，持续触发<code>click</code>事件时，并不会每次触发都会执行事件处理函数，当在设置的周期<code>1000 ms</code>内没有再触发<code>click</code>事件时，才会延时触发<code>click</code>事件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91d176712e4147ea84cd7de9dc040dab~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">节流（throttle）</h3>
<p><strong>函数节流（throttle）</strong>：函数执行一次后，只有在大于设置的执行周期后才会执行第二次。<strong>持续触发事件时，保证一定时间段内只调用一次事件处理函数。</strong></p>
<p><code>throttle</code>翻译为<code>节流阀</code>，我们可以想象成我们水龙头放水，阀门一打开，水哗哗的往下流，秉着勤俭节约的优良传统美德，我们要把水龙头关小点，最好是如我们心意按照一定规律在某个时间间隔内一滴一滴的往下滴。</p>
<p>同样我们先看一个没有使用<code>throttle</code>技术的<code>scroll</code>事件，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d48025f54648c39261cce1d0be63dd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a0a4c1b783c4a29912e1a277b08e39a~tplv-k3u1fbpfcp-watermark.image" alt="2021070621471626.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种频繁的<code>scroll</code>操作都会给浏览器带来沉重的负担，接下来我们看下如何使用<code>throttle</code>技术。</p>
<p>节流原理：是记录上次执行的时间戳<code>lastTime</code>，每次触发事件时记录当前执行的时间戳<code>nowTime</code>，然后判断nowTime与lastTime的差值是否大于设定的周期delay，如果大于，则执行回调，并更新上次执行的时间戳，从而循环。持续触发事件时，保证一定时间段内触发事件处理函数的频率。</p>
<p>再看一个🌰：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, delay</span>) </span>&#123;
  <span class="hljs-comment">// 记录上次触发的时间戳</span>
  <span class="hljs-keyword">var</span> lastTime = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-comment">// 记录当前触发的时间戳</span>
     <span class="hljs-keyword">var</span> nowTime = <span class="hljs-built_in">Date</span>.now();
     <span class="hljs-comment">// 如果当前触发与上次触发的时间差值 大于 设置的周期则允许执行</span>
     <span class="hljs-keyword">if</span> (nowTime - lastTime > delay) &#123;
        fn.call(<span class="hljs-built_in">this</span>);
        <span class="hljs-comment">// 更新时间戳</span>
        lastTime = nowTime;
     &#125;
  &#125;
&#125;
<span class="hljs-built_in">document</span>.onscroll = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log (<span class="hljs-string">'节流旨在时间段内控制触发的频率'</span>+<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-built_in">Date</span>.now()))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图，持续触发scroll事件时，并不立即执行处理函数，当当前触发与上次触发的时间差值大于设置的周期时才会执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aaf8a529563439d883220a8b0e357a0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">应用场景</h3>
<p>上面介绍了<strong>防抖（debounce）</strong> 和 <strong>节流（throttle）</strong> 的原理和实现方式。</p>
<p>下面简单列出两者的应用场景都有哪些：</p>
<p><strong>防抖（debounce）应用场景：</strong></p>
<ul>
<li>每个调整大小/滚动都会触发统计事件。</li>
<li>验证文本输入（在连续文本输入后，发送Ajax请求进行验证）。</li>
<li>监视滚动scroll事件（在添加去抖动后滚动，只有在用户停止滚动后才会确定它是否已到达页面底部）。</li>
</ul>
<p><strong>节流（throttle）应用场景：</strong></p>
<ul>
<li>实现DOM元素的拖放功能mousemove。</li>
<li>搜索关联keyup。</li>
<li>计算鼠标移动距离mousemove。</li>
<li>画布模拟草图功能mousemove。</li>
<li>射击游戏中的 mousedown/keydown事件（每单位时间只能发射一颗- 子弹）。</li>
<li>监视滚动scroll事件（添加节流后，只要滚动页面，就会每隔一段时间才会计算）。</li>
</ul>
<h3 data-id="heading-4">总结</h3>
<ul>
<li>函数防抖和函数节流都是防止某一时间频繁触发，但是这两兄弟之间的原理却不一样。</li>
<li>函数防抖是某一段时间内只执行一次，而函数节流是间隔时间执行。</li>
</ul>
<h3 data-id="heading-5">往期推荐</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjq.qq.com%2F%3F_wv%3D1027%26k%3DDMwVx9EY" target="_blank" rel="nofollow noopener noreferrer" title="https://jq.qq.com/?_wv=1027&k=DMwVx9EY" ref="nofollow noopener noreferrer">高频JavaScript面试题汇总</a></p>
<h3 data-id="heading-6">✍话题</h3>
<p><strong>什么样的答案终身难忘？学生时代关于记忆经常能听见两种论调：</strong></p>
<p>1.死记硬背：见效快，但也忘得快，且一般不会灵活运用（指标不治本）</p>
<p>2.理解性记忆：见效慢，但记忆持久且会灵活运用（治标又治本）</p>
<p>如果是你，你愿意pick哪种？</p></div>  
</div>
            