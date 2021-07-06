
---
title: 'Golang官方限流器的用法详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=469'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 20:22:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=469'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>限流器是提升服务稳定性的非常重要的组件，可以用来限制请求速率，保护服务，以免服务过载。
限流器的实现方法有很多种，常见的限流算法有<strong>固定窗口、滑动窗口、漏桶、令牌桶</strong>，我在前面的文章**「<a href="https://mp.weixin.qq.com/s/krrUFEHVBw4c-47ziXOK2w" target="_blank" rel="nofollow noopener noreferrer">常用限流算法的应用场景和实现原理</a>」** 中给大家讲解了这几种限流方法自身的特点和应用场景，其中令牌桶在限流的同时还可以应对一定的突发流量，与互联网应用容易因为热点事件出现突发流量高峰的特点更契合。</p>
<blockquote>
<p>简单来说，令牌桶就是想象有一个固定大小的桶，系统会以恒定速率向桶中放 Token，桶满则暂时不放。在请求比较的少的时候桶可以先"攒"一些Token，应对突发的流量，如果桶中有剩余 Token 就可以一直取。如果没有剩余 Token，则需要等到桶中被放置了 Token 才行。</p>
<p>关于令牌桶限流更详细的解释请参考文章：<a href="https://mp.weixin.qq.com/s/krrUFEHVBw4c-47ziXOK2w" target="_blank" rel="nofollow noopener noreferrer">常用限流算法的应用场景和实现原理</a></p>
</blockquote>
<p>有的同学在看明白令牌桶的原理后就非常想去自己实现一个限流器应用到自己的项目里，em... 怎么说呢，造个轮子确实有利于自己水平提高，不过要是应用到商用项目里的话其实大可不必自己去造轮子，Golang官方已经替我们造好轮子啦 ......~！</p>
<p>Golang 官方提供的扩展库里就自带了限流算法的实现，即 <code>golang.org/x/time/rate</code>。该限流器也是基于 Token Bucket(令牌桶) 实现的。</p>
<h2 data-id="heading-0">限流器的内部结构</h2>
<p><code>time/rate</code>包的<code>Limiter</code>类型对限流器进行了定义，所有限流功能都是通过基于<code>Limiter</code>类型实现的，其内部结构如下：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Limiter <span class="hljs-keyword">struct</span> &#123;
mu     sync.Mutex
limit  Limit
burst  <span class="hljs-keyword">int</span> <span class="hljs-comment">// 令牌桶的大小</span>
tokens <span class="hljs-keyword">float64</span>
last time.Time <span class="hljs-comment">// 上次更新tokens的时间</span>
lastEvent time.Time <span class="hljs-comment">// 上次发生限速器事件的时间（通过或者限制都是限速器事件）</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其主要字段的作用是：</p>
<ul>
<li>limit：<code>limit</code>字段表示往桶里放Token的速率，它的类型是Limit，是int64的类型别名。<strong>设置<code>limit</code>时既可以用数字指定每秒向桶中放多少个Token，也可以指定向桶中放Token的时间间隔</strong>，其实指定了每秒放Token的个数后就能计算出放每个Token的时间间隔了。</li>
<li>burst: 令牌桶的大小。</li>
<li>tokens: 桶中的令牌。</li>
<li>last: 上次往桶中放 Token 的时间。</li>
<li>lastEvent：上次发生限速器事件的时间（通过或者限制都是限速器事件）</li>
</ul>
<p>可以看到在 <code>timer/rate</code> 的限流器实现中，并没有单独维护一个 Timer 和队列去真的每隔一段时间向桶中放令牌，而是仅仅通过计数的方式表示桶中剩余的令牌。每次消费取 Token 之前会先根据上次更新令牌数的时间差更新桶中Token数。</p>
<p>大概了解了<code>time/rate</code>限流器的内部实现后，下面的内容我们会集中介绍下该组件的具体使用方法：</p>
<h2 data-id="heading-1">构造限流器</h2>
<p>我们可以使用以下方法构造一个限流器对象：</p>
<pre><code class="hljs language-go copyable" lang="go">limiter := rate.NewLimiter(<span class="hljs-number">10</span>, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有两个参数：</p>
<ol>
<li>第一个参数是 <code>r Limit</code>，设置的是限流器Limiter的<code>limit</code>字段，代表每秒可以向 Token 桶中产生多少 token。Limit 实际上是 float64 的别名。</li>
<li>第二个参数是 <code>b int</code>，b 代表 Token 桶的容量大小，也就是设置的限流器 Limiter 的<code>burst</code>字段。</li>
</ol>
<p>那么，对于以上例子来说，其构造出的限流器的令牌桶大小为 100, 以每秒 10 个 Token 的速率向桶中放置 Token。</p>
<p>除了给<code>r Limit</code>参数直接指定每秒产生的 Token 个数外，还可以用 Every 方法来指定向桶中放置 Token 的间隔，例如：</p>
<pre><code class="hljs language-go copyable" lang="go">limit := rate.Every(<span class="hljs-number">100</span> * time.Millisecond);
limiter := rate.NewLimiter(limit, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就表示每 100ms 往桶中放一个 Token。本质上也是一秒钟往桶里放 10 个。</p>
<h2 data-id="heading-2">使用限流器</h2>
<p>Limiter 提供了三类方法供程序消费 Token，可以每次消费一个 Token，也可以一次性消费多个 Token。
每种方法代表了当 Token 不足时，各自不同的对应手段，可以阻塞等待桶中Token补充，也可以直接返回取Token失败。</p>
<h3 data-id="heading-3">Wait/WaitN</h3>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">Wait</span><span class="hljs-params">(ctx context.Context)</span> <span class="hljs-params">(err error)</span></span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">WaitN</span><span class="hljs-params">(ctx context.Context, n <span class="hljs-keyword">int</span>)</span> <span class="hljs-params">(err error)</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Wait 实际上就是 <code>WaitN(ctx,1)</code>。</p>
<p>当使用 Wait 方法消费 Token 时，如果此时桶内 Token 数组不足 (小于 N)，那么 Wait 方法将会阻塞一段时间，直至 Token 满足条件。如果充足则直接返回。</p>
<p>这里可以看到，Wait 方法有一个 context 参数。
我们可以设置 context 的 Deadline 或者 Timeout，来决定此次 Wait 的最长时间。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-comment">// 一直等到获取到桶中的令牌</span>
err := limiter.Wait(context.Background())
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
fmt.Println(<span class="hljs-string">"Error: "</span>, err)
&#125;

<span class="hljs-comment">// 设置一秒的等待超时时间</span>
ctx, _ := context.WithTimeout(context.Background(), time.Second * <span class="hljs-number">1</span>)
err := limiter.Wait(ctx)
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
fmt.Println(<span class="hljs-string">"Error: "</span>, err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Allow/AllowN</h3>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">Allow</span><span class="hljs-params">()</span> <span class="hljs-title">bool</span></span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">AllowN</span><span class="hljs-params">(now time.Time, n <span class="hljs-keyword">int</span>)</span> <span class="hljs-title">bool</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Allow 实际上就是对 <code>AllowN(time.Now(),1)</code> 进行简化的函数。</p>
<p>AllowN 方法表示，截止到某一时刻，目前桶中数目是否至少为 n 个，满足则返回 true，同时从桶中消费 n 个 token。反之不消费桶中的Token，返回false。</p>
<p>对应线上的使用场景是，如果请求速率超过限制，就直接丢弃超频后的请求。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">if</span> limiter.AllowN(time.Now(), <span class="hljs-number">2</span>) &#123;
    fmt.Println(<span class="hljs-string">"event allowed"</span>)
&#125; <span class="hljs-keyword">else</span> &#123;
    fmt.Println(<span class="hljs-string">"event not allowed"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Reserve/ReserveN</h3>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">Reserve</span><span class="hljs-params">()</span> *<span class="hljs-title">Reservation</span></span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(lim *Limiter)</span> <span class="hljs-title">ReserveN</span><span class="hljs-params">(now time.Time, n <span class="hljs-keyword">int</span>)</span> *<span class="hljs-title">Reservation</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Reserve 相当于 <code>ReserveN(time.Now(), 1)</code>。</p>
<p>ReserveN 的用法就相对来说复杂一些，当调用完成后，无论 Token 是否充足，都会返回一个 <code>*Reservation</code> 对象。你可以调用该对象的<code>Delay()</code>方法，该方法返回的参数类型为<code>time.Duration</code>，反映了需要等待的时间，必须等到等待时间之后，才能进行接下来的工作。如果不想等待，可以调用<code>Cancel()</code>方法，该方法会将 Token 归还。</p>
<p>举一个简单的例子，我们可以这么使用 Reserve 方法。</p>
<pre><code class="hljs language-go copyable" lang="go">r := limiter.Reserve()
f !r.OK() &#123;
    <span class="hljs-comment">// Not allowed to act! Did you remember to set lim.burst to be > 0 ?</span>
    <span class="hljs-keyword">return</span>
&#125;
time.Sleep(r.Delay())
Act() <span class="hljs-comment">// 执行相关逻辑</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">动态调整速率和桶大小</h3>
<p>Limiter 支持创建后动态调整速率和桶大小：</p>
<ol>
<li>SetLimit(Limit) 改变放入 Token 的速率</li>
<li>SetBurst(int) 改变 Token 桶大小</li>
</ol>
<p>有了这两个方法，可以根据现有环境和条件以及我们的需求，动态地改变 Token 桶大小和速率。</p>
<h2 data-id="heading-7">总结</h2>
<p>今天我们总结了 Golang 官方限流器的使用方法，它是一种令牌桶算实现的限流器。其中 <strong>Wait/WaitN</strong>，<strong>Allow/AllowN</strong> 这两组方法在平时用的比较多，前者是消费Token时如果桶中Token不足可以让程序等待桶中新Token的放入（最好设置上等待时长）后者则是在桶中的Token不足时选择直接丢弃请求。</p>
<p>除了Golang官方提供的限流器实现，Uber公司开源的限流器<code>uber-go/ratelimit</code>也是一个很好的选择，与Golang官方限流器不同的是Uber的限流器是通过漏桶算法实现的，不过对传统的漏桶算法进行了改良，有兴趣的同学可以自行去体验一下。</p>
<blockquote>
<p>今天的文章就到这里啦，如果喜欢我的文章就帮我点个赞吧，我会每周通过技术文章分享我的所学所见和第一手实践经验，感谢你的支持。<strong>微信搜索关注公众号「网管叨bi叨」</strong> 每周教会你一个进阶知识。</p>
</blockquote>
<h3 data-id="heading-8">推荐阅读：</h3>
<ul>
<li>
<p><a href="https://mp.weixin.qq.com/s/krrUFEHVBw4c-47ziXOK2w" target="_blank" rel="nofollow noopener noreferrer">常用限流算法的应用场景和实现原理</a></p>
</li>
<li>
<p><a href="https://mp.weixin.qq.com/s/TtN6NZ8hQ2AIf0C8wVzkjA" target="_blank" rel="nofollow noopener noreferrer">Go语言的IO库那么多，我该怎么选？</a></p>
</li>
</ul></div>  
</div>
            