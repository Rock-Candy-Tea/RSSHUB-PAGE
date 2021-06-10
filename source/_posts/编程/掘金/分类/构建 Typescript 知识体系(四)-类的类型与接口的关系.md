
---
title: '构建 Typescript 知识体系(四)-类的类型与接口的关系'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66260e5a1e9248f5979581ebb7ffd78c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 02:25:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66260e5a1e9248f5979581ebb7ffd78c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第十天，活动详情查看:<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">1. 类实现接口的时候，必须实现接口中所有的属性， 并且可以在类中定义其他的属性</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Human &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  eat(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Asian</span> <span class="hljs-title">implements</span> <span class="hljs-title">Human</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 接口只能约束类的公有成员</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Human &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  eat(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">/* 错误提示:   
类“Asian”错误实现接口“Human”。
  属性“name”在类型“Asian”中是私有属性，但在类型“Human”中不是。
*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Asian</span> <span class="hljs-title">implements</span> <span class="hljs-title">Human</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-keyword">private</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.接口不能约束类的构造函数</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Human &#123;
  <span class="hljs-keyword">new</span> (name: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">void</span>;
  name: <span class="hljs-built_in">string</span>;
  eat(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-comment">/* 错误提示:   
类“Asian”错误实现接口“Human”。
  类型“Asian”提供的内容与签名“new (name: string): void”不匹配。ts(2420)
*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Asian</span> <span class="hljs-title">implements</span> <span class="hljs-title">Human</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">sleep</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 接口的继承</h2>
<h3 data-id="heading-4">4.1 接口继承接口</h3>
<p><strong>接口可以像类一样相互继承，并且一个接口可以继承多个接口</strong>
<strong>接口的继承，可以抽离出可重用的接口，</strong>
<strong>也可以将多个接口合并成一个接口</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Human &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  eat(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> Man <span class="hljs-keyword">extends</span> Human &#123;
  run(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> Child &#123;
  cry(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">interface</span> Boy <span class="hljs-keyword">extends</span> Man, Child &#123;&#125;

<span class="hljs-keyword">let</span> boy: Boy = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>,
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">cry</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.2 接口继承类</h3>
<p><strong>相当于接口把类的成员都抽象了出来，也就是只有类的成员接口，而没有具体的实现</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Auto</span> </span>&#123;
  state = <span class="hljs-number">1</span>;
  <span class="hljs-comment">// private state2 = 2;</span>
&#125;

<span class="hljs-comment">// 接口中就隐含了 state属性</span>
<span class="hljs-keyword">interface</span> AutoInterFace <span class="hljs-keyword">extends</span> Auto &#123;&#125;
<span class="hljs-comment">// 实现 AutoInterFace接口</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-title">implements</span> <span class="hljs-title">AutoInterFace</span> </span>&#123;
  state = <span class="hljs-number">1</span>;
&#125;

<span class="hljs-comment">// Auto 的子类也可以实现  AutoInterFace接口</span>
<span class="hljs-comment">// 因为 Bus是 Auto 的子类，自然就继承了 state属性，因此不必重复实现</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Auto</span> <span class="hljs-title">implements</span> <span class="hljs-title">AutoInterFace</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>接口抽离类成员的时候， 不仅抽离的公共成员，也抽离了私有成员和受保护成员</strong></p>
<h2 data-id="heading-6">总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66260e5a1e9248f5979581ebb7ffd78c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接口之间是可以相互继承的，这样能够实现接口的复用</li>
<li>类之间也可以相互继承，这样能够实现 方法和属性的复用</li>
<li>接口是可以通过类来实现的，但是接口只能约束类的共有成员</li>
<li>接口可以抽离出类的成员，这些成员包括(共有成员，私有成员，受保护成员)</li>
</ul>
<h2 data-id="heading-7">最后</h2>
<p>以上就是本篇文章的主要内容，文章浅陋,欢迎各位看官评论区留下的你的见解！</p>
<p>觉得有收获的同学欢迎点赞，关注一波!</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/563aefc8c1904b4aab704a682fc7f8ec~tplv-k3u1fbpfcp-zoom-1.image" alt="20210601205044" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">往期文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6951684431597797389" target="_blank">前端开发者应该知道的 Centos/Docker/Nginx/Node/Jenkins 操作(🍡 长文)</a></li>
<li><a href="https://juejin.cn/post/6940976355097985032" target="_blank">二维码扫码登录是什么原理</a></li>
<li><a href="https://juejin.cn/post/6950156721939546148" target="_blank">最全 ECMAScript 攻略</a></li>
<li><a href="https://juejin.cn/post/6969454249411837965" target="_blank">前端开发者需要知道的 package.json</a></li>
</ul></div>  
</div>
            