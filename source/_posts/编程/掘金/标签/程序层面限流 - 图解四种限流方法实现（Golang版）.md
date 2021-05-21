
---
title: '程序层面限流 - 图解四种限流方法实现（Golang版）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd79ea864c804c3d85f9689b8738847d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 17:13:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd79ea864c804c3d85f9689b8738847d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>如果❤️我的文章有帮助，欢迎点赞、关注。这是对我继续技术创作最大的鼓励。</p>
</blockquote>
<p>本文为 <code>应对突防流量</code> 系列文章，以下为相关基友篇</p>
<ul>
<li><a href="https://juejin.cn/post/6961957755573764132" target="_blank">面对突发流量：系统、软件层限流手段</a></li>
<li><a href="https://juejin.cn/post/6964542601840033823/" target="_blank">程序层面限流 - 必要性</a></li>
<li><a href="https://juejin.cn/post/6964545112013553694" target="_blank">程序层面限流 - 图解四种限流方法实现（Golang版）</a></li>
</ul>
<h2 data-id="heading-0">计数器限流</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd79ea864c804c3d85f9689b8738847d~tplv-k3u1fbpfcp-watermark.image" alt="offer指北北_01.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"fmt"</span>
<span class="hljs-string">"sync"</span>
<span class="hljs-string">"time"</span>
)

<span class="hljs-keyword">type</span> RequestLimiter <span class="hljs-keyword">struct</span> &#123;
Interval time.Duration <span class="hljs-comment">// 重新计数时间</span>
MaxCount <span class="hljs-keyword">int</span>           <span class="hljs-comment">// 最大计数</span>
Lock     sync.Mutex
ReqCount <span class="hljs-keyword">int</span> <span class="hljs-comment">// 目前的请求数</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(reqLimiter *RequestLimiter)</span> <span class="hljs-title">IsAvailable</span><span class="hljs-params">()</span> <span class="hljs-title">bool</span></span> &#123;
reqLimiter.Lock.Lock()
<span class="hljs-keyword">defer</span> reqLimiter.Lock.Unlock()

<span class="hljs-keyword">return</span> reqLimiter.ReqCount < reqLimiter.MaxCount
&#125;

<span class="hljs-comment">// 非阻塞</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(reqLimiter *RequestLimiter)</span> <span class="hljs-title">AddRequestCount</span><span class="hljs-params">()</span> <span class="hljs-title">bool</span></span> &#123;
reqLimiter.Lock.Lock()
<span class="hljs-keyword">defer</span> reqLimiter.Lock.Unlock()
<span class="hljs-keyword">if</span> reqLimiter.ReqCount < reqLimiter.MaxCount &#123;
reqLimiter.ReqCount += <span class="hljs-number">1</span>
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">NewRequestLimitService</span><span class="hljs-params">(interval time.Duration, maxCount <span class="hljs-keyword">int</span>)</span> *<span class="hljs-title">RequestLimiter</span></span> &#123;
reqLimit := &RequestLimiter&#123;
Interval: interval,
MaxCount: maxCount,
&#125;
<span class="hljs-keyword">go</span> <span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">()</span></span> &#123;
ticker := time.NewTicker(interval)
<span class="hljs-keyword">for</span> <span class="hljs-literal">true</span> &#123;
<-ticker.C
reqLimit.Lock.Lock()
fmt.Println(<span class="hljs-string">"reset Count ..."</span>)
reqLimit.ReqCount = <span class="hljs-number">0</span>
reqLimit.Lock.Unlock()
&#125;
&#125;()

<span class="hljs-keyword">return</span> reqLimit
&#125;

<span class="hljs-comment">/**
原理：协程不阻塞 + 死循环 + ticker 定时执行 ReqCount 归零
ticker := time.NewTicker(2*time.Second)
for &#123;
currentTime := <-ticker.C
fmt.Println("当前时间为:", currentTime)
&#125;

输出：
当前时间为: 2021-05-19 11:02:12.3603475 +0800 CST m=+2.002147201
当前时间为: 2021-05-19 11:02:14.3611806 +0800 CST m=+4.002980301
当前时间为: 2021-05-19 11:02:16.360625 +0800 CST m=+6.002424701
 */</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
service := NewRequestLimitService(time.Second, <span class="hljs-number">2</span>)
<span class="hljs-keyword">for</span> <span class="hljs-literal">true</span> &#123;
hasToken := service.AddRequestCount()
<span class="hljs-keyword">if</span> hasToken &#123;
fmt.Println(time.Now())
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">滑动窗口</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15dffdddc6e04ee0a6b626c08f6acf44~tplv-k3u1fbpfcp-watermark.image" alt="offer指北北_02.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"fmt"</span>
<span class="hljs-string">"sync"</span>
<span class="hljs-string">"time"</span>
)

<span class="hljs-keyword">type</span> WindowLimiter <span class="hljs-keyword">struct</span> &#123;
Interval    time.Duration <span class="hljs-comment">// 总计数时间</span>
WinCount    []<span class="hljs-keyword">int</span>         <span class="hljs-comment">// 每个窗口的访问数量</span>
TicketSize  <span class="hljs-keyword">int</span>           <span class="hljs-comment">// 窗口最大容量</span>
TicketCount <span class="hljs-keyword">int</span>           <span class="hljs-comment">// 窗口数量</span>
Lock        sync.Mutex
CurIndex    <span class="hljs-keyword">int</span> <span class="hljs-comment">// 目前使用哪个窗口</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(reqLimiter *WindowLimiter)</span> <span class="hljs-title">IsAvailable</span><span class="hljs-params">()</span> <span class="hljs-title">bool</span></span> &#123;
reqLimiter.Lock.Lock()
<span class="hljs-keyword">defer</span> reqLimiter.Lock.Unlock()
<span class="hljs-keyword">return</span> reqLimiter.WinCount[reqLimiter.CurIndex] < reqLimiter.TicketSize
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(reqLimiter *WindowLimiter)</span> <span class="hljs-title">AddRequestCount</span><span class="hljs-params">()</span> <span class="hljs-title">bool</span></span> &#123;
reqLimiter.Lock.Lock()
<span class="hljs-keyword">defer</span> reqLimiter.Lock.Unlock()
<span class="hljs-keyword">if</span> reqLimiter.WinCount[reqLimiter.CurIndex] < reqLimiter.TicketSize &#123;
reqLimiter.WinCount[reqLimiter.CurIndex]++
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">NewRequestLimitService</span><span class="hljs-params">(interval time.Duration, ticketCount <span class="hljs-keyword">int</span>, ticketSize <span class="hljs-keyword">int</span>)</span> *<span class="hljs-title">WindowLimiter</span></span> &#123;
reqLimit := &WindowLimiter&#123;
Interval:    interval,
WinCount:    <span class="hljs-built_in">make</span>([]<span class="hljs-keyword">int</span>, ticketCount, ticketCount),
TicketSize:  ticketSize,
TicketCount: ticketCount,
CurIndex:    <span class="hljs-number">0</span>,
&#125;
<span class="hljs-keyword">go</span> <span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">()</span></span> &#123;
ticker := time.NewTicker(time.Duration(interval.Nanoseconds() / <span class="hljs-keyword">int64</span>(ticketCount)))
<span class="hljs-keyword">for</span> <span class="hljs-literal">true</span> &#123;
<-ticker.C
reqLimit.Lock.Lock()
reqLimit.CurIndex = (reqLimit.CurIndex + <span class="hljs-number">1</span>) % reqLimit.TicketCount
reqLimit.WinCount[reqLimit.CurIndex] = <span class="hljs-number">0</span>
fmt.Println(<span class="hljs-string">"reset Count ..."</span>)
reqLimit.Lock.Unlock()
&#125;
&#125;()

<span class="hljs-keyword">return</span> reqLimit
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
service := NewRequestLimitService(time.Second, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>)
<span class="hljs-keyword">for</span> <span class="hljs-literal">true</span> &#123;
hasToken := service.AddRequestCount()
<span class="hljs-keyword">if</span> hasToken &#123;
fmt.Println(time.Now())
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">漏桶算法</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38998c311e9147a6a5337fac87b7f110~tplv-k3u1fbpfcp-watermark.image" alt="offer指北北_03.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"fmt"</span>
<span class="hljs-string">"math"</span>
<span class="hljs-string">"sync"</span>
<span class="hljs-string">"time"</span>
)

<span class="hljs-keyword">type</span> BucketLimiter <span class="hljs-keyword">struct</span> &#123;
Timestamp time.Time <span class="hljs-comment">// 当前注水的时间戳</span>
Capacity  <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 桶的容量</span>
Rate      <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 速度</span>
Water     <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 当前水量</span>
Lock      sync.Mutex
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">AddWater</span><span class="hljs-params">(bucket *BucketLimiter)</span> <span class="hljs-title">bool</span></span> &#123;
now := time.Now()
leftWater := math.Max(<span class="hljs-number">0</span>, bucket.Water-now.Sub(bucket.Timestamp).Seconds()*bucket.Rate)
bucket.Lock.Lock()
<span class="hljs-keyword">defer</span> bucket.Lock.Unlock()
<span class="hljs-keyword">if</span> leftWater+<span class="hljs-number">1</span> < bucket.Capacity &#123;
<span class="hljs-comment">// 尝试加水，此时水桶未满</span>
bucket.Timestamp = now
bucket.Water = leftWater + <span class="hljs-number">1</span>
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 水满了，拒绝访问</span>
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
service := &BucketLimiter&#123;
Timestamp: time.Now(),
Capacity:  <span class="hljs-number">2</span>,
Rate:      <span class="hljs-number">1</span>,
Water:     <span class="hljs-number">0</span>,
&#125;
<span class="hljs-keyword">for</span> <span class="hljs-literal">true</span> &#123;
hasToken := AddWater(service)
<span class="hljs-keyword">if</span> hasToken &#123;
fmt.Println(time.Now())
&#125;

&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">令牌桶算法</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2d32843611c4e5c9f94bc2d44ff8e11~tplv-k3u1fbpfcp-watermark.image" alt="offer指北北_04.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"math"</span>
<span class="hljs-string">"sync"</span>
<span class="hljs-string">"time"</span>
)

<span class="hljs-comment">// 定义令牌桶结构</span>
<span class="hljs-keyword">type</span> tokenBucket <span class="hljs-keyword">struct</span> &#123;
timestamp time.Time <span class="hljs-comment">// 当前时间戳</span>
capacity  <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 桶的容量（存放令牌的最大量）</span>
rate      <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 令牌放入速度</span>
tokens    <span class="hljs-keyword">float64</span>   <span class="hljs-comment">// 当前令牌总量</span>
lock      sync.Mutex
&#125;

<span class="hljs-comment">// 判断是否获取令牌（若能获取，则处理请求）</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">getToken</span><span class="hljs-params">(bucket tokenBucket)</span> <span class="hljs-title">bool</span></span> &#123;
now := time.Now()
bucket.lock.Lock()
<span class="hljs-keyword">defer</span> bucket.lock.Unlock()
<span class="hljs-comment">// 先添加令牌</span>
leftTokens := math.Max(bucket.capacity, bucket.tokens+now.Sub(bucket.timestamp).Seconds()*bucket.rate)
<span class="hljs-keyword">if</span> leftTokens < <span class="hljs-number">1</span> &#123;
<span class="hljs-comment">// 若桶中一个令牌都没有了，则拒绝</span>
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 桶中还有令牌，领取令牌</span>
bucket.tokens -= <span class="hljs-number">1</span>
bucket.timestamp = now
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            