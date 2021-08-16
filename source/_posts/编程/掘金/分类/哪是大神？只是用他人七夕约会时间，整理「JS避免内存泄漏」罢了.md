
---
title: '哪是大神？只是用他人七夕约会时间，整理「JS避免内存泄漏」罢了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f193195bcfca4afb89e7014d0230a870~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 17:07:31 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f193195bcfca4afb89e7014d0230a870~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>大家七夕节过得快乐吗？快乐就好，你么快乐就是我快乐。呜呜呜</p>
<p>哪有什么天才？他只是把别人七夕约会的时间，用在写文章上  ——陆逊 （是的，江东陆逊）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f193195bcfca4afb89e7014d0230a870~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
大家好，我是林三心，上一篇我给大家讲了<a href="https://juejin.cn/post/6995706341041897486" target="_blank" title="https://juejin.cn/post/6995706341041897486">赠你13张图，助你20分钟打败了「V8垃圾回收机制」</a>，但是关知道回收机制是不行的，V8垃圾回收机制固然很强，但是我们也不能随便就制造很多垃圾让它回收，咱们得在开发中尽量减少垃圾的数量，今天就跟大家讲一讲如何避免<strong>JS垃圾过多，内存泄漏</strong>吧</p>
<h2 data-id="heading-1">为什么要避免</h2>
<p>什么是<code>内存泄漏</code>呢？就是有些理应被回收的垃圾，却没被回收，这就造成了垃圾越积越多。</p>
<p><code>内存泄漏</code>，听起来很遥远，但其实离我们很近很近，我们平时都直接或者间接地去接触过它。例如，有时候你的页面，用着用着就卡了起来，而且随着时间的延长，越来越卡，那这个时候，就要考虑是否是<code>内存泄漏</code>问题了，<code>内存泄漏</code>是影响用户体验的重大问题，所以平时通过正确的代码习惯去避免它，是非常有必要的。</p>
<h2 data-id="heading-2">如何监控内存状况</h2>
<p>咱们一直强调内存内存，但是感觉他是很虚无缥缈的东西，至少也得让咱们见见它的真面目吧？</p>
<h3 data-id="heading-3">浏览器任务管理器</h3>
<p>打开方式：在浏览器顶部<code>右键</code>，打开<code>任务管理器</code>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a785ae7bed134895befc2383a5c9874b~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-03 下午10.15.23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开后，咱们看到<code>内存</code>和<code>JavaScript内存(括号里)</code>：</p>
<ul>
<li><code>内存</code>：页面里的原始内存，也就是<code>DOM节点</code>的总占用内存</li>
<li><code>JavaScript内存(括号里)</code>：是该页面中所有<code>可达对象</code>的总占用内存</li>
</ul>
<p>那什么是<code>可达对象</code>呢？简单说就是：就是从初始的<code>根对象（window或者global）</code>的指针开始，向下搜索子节点，子节点被搜索到了，说明该子节点的引用对象可达，搜不到，说明该子节点对象不可达。举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 可达，可以通过window.name访问</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'林三心'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 不可达，访问不了</span>
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">'林三心'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回到我们的任务管理，此时我们在页面中编写一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><button id=<span class="hljs-string">"btn"</span>>点击</button>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        list = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击前：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23daa4f35fc04f00b0180b04819be129~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-03 下午10.16.50.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击后，发现内存瞬间上升：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53fc1bf27b674d26902f6551d331034f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-03 下午10.17.18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">Performance</h3>
<p>使用Chrome浏览器的<code>无痕模式</code>，是为了避免很多其他因素，影响咱们查看内存：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03ccafbfab2a4ae78b15149a17e9705e~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-03 下午10.39.58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按F12打开调试窗口，选择<code>Performance</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad798d5bcf284fa797462072db10e644~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>咱们就以掘金首页为例吧！<strong>点击录制 -> 刷新掘金 -> 点击stop</strong>，可以看到以下指标随着时间的<code>上下波动</code>：</p>
<ul>
<li><code>JS Heap</code>：JS堆</li>
<li><code>Documents</code>: 文档</li>
<li><code>Nodes</code>: DOM节点</li>
<li><code>Listeners</code>: 监听器</li>
<li><code>GPU Memory</code>: GPU内存</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c8bc35ae2c64dc692fe94a925c0ed5a~tplv-k3u1fbpfcp-watermark.image" alt="juejinperf.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">堆快照</h3>
<p><code>堆快照</code>，顾名思义，就是将当前某一个页面的<code>堆内存拍下照片</code>存起来，同一个页面，执行某个操作前，录制堆快照是一个样，有可能执行完后，录制的堆快照又是另外一个样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca9b916efffa4407a20a15fd560ff2af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是以<code>掘金首页</code>为例，可以看到当前页面内存为<code>13.3M</code>，咱们可以选择<code>Statistics</code>，查看<code>数组，对象，字符串</code>等所占内存</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3159441afe843c4b36993f9db54d19b~tplv-k3u1fbpfcp-watermark.image" alt="掘金堆快照.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">如何避免</h2>
<p>上面说了，其实<code>内存泄漏</code>问题离我们很近，我们可能都直接或者间接造成过。接下来就说说如何避免这个问题吧，可能也是你开发中的坏习惯哦！</p>
<h3 data-id="heading-7">减少全局变量</h3>
<p>我们在开发中可能遇到过这样的代码，其实我们只是想把a当做局部变量而已，但是忘记写<code>var，let，const</code>了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// a 未在外部声明过</span>
    a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)
&#125;

上方代码等同于
<span class="hljs-keyword">var</span> a
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样有什么坏处呢？咱们前面说过<code>可达性</code>，在这里就可以解释了。上方代码这么写的话，咱们可以通过<code>window.a</code>去访问到<code>a</code>这个<code>全局变量</code>，所以a是可达的，他不会被当做垃圾去回收，这导致他会一直占用内存而得不到释放，消耗性能，违背了我们的初衷。咱们可以通过<code>堆快照</code>来验证一下，步骤是：<code>录制 -> 点击按钮 -> 录制</code>，比较两次的结果，点击后，内存大了<code>4M</code>，查看<code>Statistics</code>，发现数组内存大了很多，没得到释放：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df19c1cee134788a122db9657c491e3~tplv-k3u1fbpfcp-watermark.image" alt="全局变量堆快照.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那应该怎么改良呢？可以加上定义变量符：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果，由于局部变量，<code>不可达</code>，每执行一次函数，就会被<code>回收</code>，得到释放，所以不会一直占着内存，点击前后的内存是差不多的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d5694658ac408ea1dfc8a72e226787~tplv-k3u1fbpfcp-watermark.image" alt="局部变量堆快照.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">未清除定时器</h3>
<p>请看这一段代码，在这段代码中，执行完fn1函数，按理说arr数组会被回收，但是他却回收不了。为什么呢？因为定时器里的a引用着arr，并且定时器不清除的话，<code>a</code>就不会被回收，<code>a</code>不回收就会一直引用着<code>arr</code>，那么<code>arr</code>肯定也回收不了了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)
      <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">let</span> a = arr
     &#125;, <span class="hljs-number">1000</span>)
&#125;
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    fn()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Performace：录制 -> 手动垃圾回收 -> 连点五次按钮 -> 手动垃圾回收 -> 结束</strong></p>
<p>首尾两次手动垃圾回收，是为了对比首尾两次垃圾内存最低点，而如果没有内存泄漏问题的话，首尾两次最低点应该是相同的，这里可以看到，尾部比首部多出的那部分，就是没有被回收的内存量
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/980f017b46bf4805b091ee27641f2965~tplv-k3u1fbpfcp-watermark.image" alt="定时器perf.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面说了，<code>arr数组</code>为啥没被回收？是因为<code>定时器</code>没清除，导致<code>a</code>一直引用<code>arr</code>，那怎么解决呢？直接把<code>定时器</code>清除就行了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1000000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (i > <span class="hljs-number">5</span>)  <span class="hljs-built_in">clearInterval</span>(timer)
    <span class="hljs-keyword">let</span> a = arr
    i++
  &#125;, <span class="hljs-number">1000</span>)
&#125;
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  fn()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看<code>Performance</code>，发现首位两次的内存量是一样的，这就说明正常了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0892e8b6aefc47bbae29df73bbe2e56c~tplv-k3u1fbpfcp-watermark.image" alt="清除定时器perf.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">合理使用闭包</h3>
<p>咱们来看这一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">100000</span>).fill(<span class="hljs-string">'Sunshine_Lin'</span>)

    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-keyword">let</span> a = []
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    a.push(fn1())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按理说，<code>fn1</code>执行完后，<code>arr</code>会被回收，但是在这段代码中，却是没有被回收，为什么呢？因为<code>fn1</code>执行后，将<code>arr</code>给<code>return</code>出去，然后<code>arr</code>被<code>push进a数组</code>了，而a数组是个全局变量，<code>a数组</code>是不会被回收的，那么<code>a数组</code>里的东西自然也不会被回收，这就导致<code>arr</code>不会被回收，等到点击越来越多次，不可被回收的<code>arr</code>就会越来越多，如果<code>a</code>后来没有被用到，那这些<code>arr</code>就成无用的垃圾了，咱们可以通过<code>Performance</code>和<code>堆快照</code>来验证：</p>
<p><strong>Performace：录制 -> 手动垃圾回收 -> 连点五次按钮 -> 手动垃圾回收 -> 结束</strong></p>
<p>首尾两次手动垃圾回收，是为了对比首尾两次垃圾内存最低点，而如果没有内存泄漏问题的话，首尾两次最低点应该是相同的，这里可以看到，尾部比首部多出的那部分，就是没有被回收的内存量</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799e9ab20b6f4d0a9496090408c5718b~tplv-k3u1fbpfcp-watermark.image" alt="闭包perfo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>堆快照：第一次录制 -> 连点5次按钮 -> 第二次录制</strong></p>
<p>会发现，点击前后，内存多了很多，多出来的就是未被回收的内存量</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d979773563a497db427ac0069540cb7~tplv-k3u1fbpfcp-watermark.image" alt="闭包堆快照.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">分离DOM</h3>
<p>什么叫<code>分离DOM</code>呢？还是利用代码来说话：</p>
<pre><code class="hljs language-js copyable" lang="js"><button id=<span class="hljs-string">"btn"</span>>点击</button>

<span class="hljs-keyword">let</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>)
<span class="hljs-built_in">document</span>.body.removeChild(btn)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然最后把button给删除了，但是因为全局变量<code>btn</code>对此<code>DOM对象</code>引用着，导致此<code>DOM</code>对象一直没有被回收，这个<code>DOM对象</code>就称为<code>分离DOM</code>，咱们可以通过<code>堆快照</code>来验证这个问题，在堆快照里搜索<code>detached(中文意思为：独立，分离)</code>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/063b58ed7fd74d09919bc67af9d0f3aa~tplv-k3u1fbpfcp-watermark.image" alt="分离DOM堆快照.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个问题很好解决，删除button后，顺便把btn设置成<code>null</code>就行了：</p>
<pre><code class="hljs language-js copyable" lang="js"><button id=<span class="hljs-string">"btn"</span>>点击</button>

<span class="hljs-keyword">let</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>)
<span class="hljs-built_in">document</span>.body.removeChild(btn)
btn = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时才是真的把button这个DOM，从js中彻底抹去：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730db6dc88f0469a9fd15c62678b9017~tplv-k3u1fbpfcp-watermark.image" alt="分离domnull.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1NK4y1S7aj%3Fp%3D19" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1NK4y1S7aj?p=19" ref="nofollow noopener noreferrer">淘宝前端是怎么做优化？如何高效书写 JavaScript ？提高 JS 性能有哪些骚操作？</a></li>
<li><a href="https://juejin.cn/post/6947841638118998029" target="_blank" title="https://juejin.cn/post/6947841638118998029">一文带你了解如何排查内存泄漏导致的页面卡顿现象</a></li>
</ul>
<h2 data-id="heading-12">结语</h2>
<p>其实避免<code>内存泄漏</code>，不止这几个做法，还有很多做法，我这里列举了四个比较常见的做法，希望大家在开发中能避免，提高自己的代码质量，提高用户体验。</p>
<p>学习群请点<a href="https://juejin.cn/pin/6969565162885873701" target="_blank" title="https://juejin.cn/pin/6969565162885873701">这里</a>，一起学习，一起摸鱼！！！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39cd5171de148bf898c5c9f50e30268~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            