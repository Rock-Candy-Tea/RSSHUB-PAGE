
---
title: '看了就会，手写Promise原理，最通俗易懂的版本！！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032d1f70ba34471e81d047b3ff7e2eab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 16:39:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032d1f70ba34471e81d047b3ff7e2eab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>大家好，我是林三心，相信大家在日常开发中都用过<strong>Promise</strong>，我一直有个梦想，就是<strong>以最通俗的话，讲最复杂的知识</strong>，所以我把<strong>通俗易懂</strong>放在了首位，今天就带大家手写实现以下<strong>Promise吧</strong>，相信大家一看就懂。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032d1f70ba34471e81d047b3ff7e2eab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">resolve和reject</h2>
<p>咱们来看一段Promise的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
    reject(<span class="hljs-string">'失败'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p1'</span>, p1)

<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(<span class="hljs-string">'失败'</span>)
    resolve(<span class="hljs-string">'成功'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p2'</span>, p2)

<span class="hljs-keyword">let</span> p3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">throw</span>(<span class="hljs-string">'报错'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p3'</span>, p3)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么会输出什么呢？请看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db87e7956fa24650bb60902bc3f113b4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 上午11.53.33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里暴露出了四个知识点：</p>
<ul>
<li>1、执行了<code>resolve</code>，Promise状态会变成<code>fulfilled</code></li>
<li>2、执行了<code>reject</code>，Promise状态会变成<code>rejected</code></li>
<li>3、Promise只以<code>第一次为准</code>，第一次成功就<code>永久</code>为<code>fulfilled</code>，第一次失败就永远状态为<code>rejected</code></li>
<li>4、Promise中有<code>throw</code>的话，就相当于执行了<code>reject</code></li>
</ul>
<p>那么咱们就把这四个知识点一步步实现吧！！！</p>
<h3 data-id="heading-2">1、实现resolve与reject</h3>
<p>大家要注意：Promise的初始状态是<code>pending</code></p>
<p>这里很重要的一步是<code>resolve和reject的绑定this</code>，为什么要绑定<code>this</code>呢？这是为了resolve和reject的<code>this指向</code>永远指向当前的<code>MyPromise实例</code>，防止随着函数执行环境的改变而改变</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-comment">// 构造方法</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;

        <span class="hljs-comment">// 初始化值</span>
        <span class="hljs-built_in">this</span>.initValue()
        <span class="hljs-comment">// 初始化this指向</span>
        <span class="hljs-built_in">this</span>.initBind()
        <span class="hljs-comment">// 执行传进来的函数</span>
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
    &#125;

    <span class="hljs-function"><span class="hljs-title">initBind</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 初始化this</span>
        <span class="hljs-built_in">this</span>.resolve = <span class="hljs-built_in">this</span>.resolve.bind(<span class="hljs-built_in">this</span>)
        <span class="hljs-built_in">this</span>.reject = <span class="hljs-built_in">this</span>.reject.bind(<span class="hljs-built_in">this</span>)
    &#125;

    <span class="hljs-function"><span class="hljs-title">initValue</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 初始化值</span>
        <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">null</span> <span class="hljs-comment">// 终值</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'pending'</span> <span class="hljs-comment">// 状态</span>
    &#125;

    <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-comment">// 如果执行resolve，状态变为fulfilled</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'fulfilled'</span>
        <span class="hljs-comment">// 终值为传进来的值</span>
        <span class="hljs-built_in">this</span>.PromiseResult = value
    &#125;

    <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
        <span class="hljs-comment">// 如果执行reject，状态变为rejected</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'rejected'</span>
        <span class="hljs-comment">// 终值为传进来的reason</span>
        <span class="hljs-built_in">this</span>.PromiseResult = reason
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们来测试一下代码吧：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test1 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(test1) <span class="hljs-comment">// MyPromise &#123; PromiseState: 'fulfilled', PromiseResult: '成功' &#125;</span>

<span class="hljs-keyword">const</span> test2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(<span class="hljs-string">'失败'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(test2) <span class="hljs-comment">// MyPromise &#123; PromiseState: 'rejected', PromiseResult: '失败' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. 状态不可变</h3>
<p>其实上面的代码是有问题的，什么问题呢？看看：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test1 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
    reject(<span class="hljs-string">'失败'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(test1) <span class="hljs-comment">// MyPromise &#123; PromiseState: 'rejected', PromiseResult: '失败' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正确的应该是状态为<code>fulfilled</code>，结果是<code>成功</code>，这里明显没有<code>以第一次为准</code></p>
<p>之前说了，Promise只以<code>第一次为准</code>，第一次成功就<code>永久</code>为<code>fulfilled</code>，第一次失败就永远状态为<code>rejected</code>，具体是什么流程呢？我给大家画了一张图：</p>
<p>Promise有三种状态：</p>
<ul>
<li><code>pending</code>：等待中，是初始状态</li>
<li><code>fulfilled</code>：成功状态</li>
<li><code>rejected</code>：失败状态</li>
</ul>
<p>一旦状态从<code>pending</code>变为<code>fulfilled或者rejected</code>，那么此Promise实例的状态就定死了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c9636d819ef4bc78af95fb80c9a7be4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午12.33.10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实实现起来也很容易，加个判断条件就行：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-comment">// state是不可变的</span>
+        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 如果执行resolve，状态变为fulfilled</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'fulfilled'</span>
        <span class="hljs-comment">// 终值为传进来的值</span>
        <span class="hljs-built_in">this</span>.PromiseResult = value
    &#125;

    <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
        <span class="hljs-comment">// state是不可变的</span>
+        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 如果执行reject，状态变为rejected</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'rejected'</span>
        <span class="hljs-comment">// 终值为传进来的reason</span>
        <span class="hljs-built_in">this</span>.PromiseResult = reason
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test1 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 只以第一次为准</span>
    resolve(<span class="hljs-string">'成功'</span>)
    reject(<span class="hljs-string">'失败'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(test1) <span class="hljs-comment">// MyPromise &#123; PromiseState: 'fulfilled', PromiseResult: '成功' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. throw</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa2e17b24a124dadba540e86350f1302~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午12.57.17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Promise中有<code>throw</code>的话，就相当于执行了<code>reject</code>。这就要使用<code>try catch</code>了</p>
<pre><code class="hljs language-js copyable" lang="js">+        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 执行传进来的函数</span>
            executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
+        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            <span class="hljs-comment">// 捕捉到错误直接执行reject</span>
+            <span class="hljs-built_in">this</span>.reject(e)
+        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们来看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test3 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">throw</span>(<span class="hljs-string">'失败'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(test3) <span class="hljs-comment">// MyPromise &#123; PromiseState: 'rejected', PromiseResult: '失败' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">then</h2>
<p>咱们平时使用then方法是这么用的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 马上输出 ”成功“</span>
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-comment">// 1秒后输出 ”失败“</span>
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        reject(<span class="hljs-string">'失败'</span>)
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-comment">// 链式调用 输出 200</span>
<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">100</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-number">2</span> * res, <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
  .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以总结出这几个知识点：</p>
<ul>
<li>then接收两个回调，一个是<code>成功回调</code>，一个是<code>失败回调</code></li>
<li>当Promise状态为<code>fulfilled</code>执行<code>成功回调</code>，为<code>rejected</code>执行<code>失败回调</code></li>
<li>如resolve或reject在定时器里，<code>则定时器结束后再执行then</code></li>
<li>then支持<code>链式调用</code>，下一次then执行<code>受上一次then返回值的影响</code></li>
</ul>
<p>下面咱们就一步一步地去实现他吧</p>
<h3 data-id="heading-6">1. 实现then</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-comment">// 接收两个回调 onFulfilled, onRejected</span>
        
        <span class="hljs-comment">// 参数校验，确保一定是函数</span>
        onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">val</span> =></span> val
        onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'fulfilled'</span>) &#123;
            <span class="hljs-comment">// 如果当前为成功状态，执行第一个回调</span>
            onFulfilled(<span class="hljs-built_in">this</span>.PromiseResult)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'rejected'</span>) &#123;
            <span class="hljs-comment">// 如果当前为失败状态，执行第二哥回调</span>
            onRejected(<span class="hljs-built_in">this</span>.PromiseResult)
        &#125;

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们来看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 输出 ”成功“</span>
<span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-string">'成功'</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2. 定时器情况</h3>
<p>上面我们已经实现了<code>then</code>的基本功能。那如果是<code>定时器</code>情况呢？</p>
<p>还是那个代码，怎么才能保证，1秒后才执行then里的失败回调呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1秒后输出 ”成功“</span>
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        reject(<span class="hljs-string">'失败'</span>)
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不能确保1秒后才执行then函数，但是我们可以保证1秒后再执行then里的回调，可能这里大家有点懵逼，我同样用一张图给大家讲讲吧：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ba5a2544b1144548cdc63362fa27d23~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午9.05.24.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是在这1秒时间内，我们可以先把then里的两个回调保存起来，然后等到1秒过后，执行了resolve或者reject，咱们再去判断状态，并且判断要去执行刚刚保存的两个回调中的哪一个回调。</p>
<p>那么问题来了，我们怎么知道当前1秒还没走完甚至还没开始走呢？其实很好判断，只要状态是<code>pending</code>，那就证明定时器还没跑完，因为如果定时器跑完的话，那状态肯定就不是<code>pending</code>，而是<code>fulfilled或者rejected</code></p>
<p>那是用什么来保存这些回调呢？建议使用<code>数组</code>，因为一个promise实例可能会<code>多次then</code>，用数组就一个一个保存了</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">initValue</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 初始化值</span>
        <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">null</span> <span class="hljs-comment">// 终值</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'pending'</span> <span class="hljs-comment">// 状态</span>
+        <span class="hljs-built_in">this</span>.onFulfilledCallbacks = [] <span class="hljs-comment">// 保存成功回调</span>
+        <span class="hljs-built_in">this</span>.onRejectedCallbacks = [] <span class="hljs-comment">// 保存失败回调</span>
    &#125;

    <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-comment">// state是不可变的</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 如果执行resolve，状态变为fulfilled</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'fulfilled'</span>
        <span class="hljs-comment">// 终值为传进来的值</span>
        <span class="hljs-built_in">this</span>.PromiseResult = value
        <span class="hljs-comment">// 执行保存的成功回调</span>
+        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilledCallbacks.length) &#123;
+            <span class="hljs-built_in">this</span>.onFulfilledCallbacks.shift()(<span class="hljs-built_in">this</span>.PromiseResult)
+        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
        <span class="hljs-comment">// state是不可变的</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== <span class="hljs-string">'pending'</span>) <span class="hljs-keyword">return</span>
        <span class="hljs-comment">// 如果执行reject，状态变为rejected</span>
        <span class="hljs-built_in">this</span>.PromiseState = <span class="hljs-string">'rejected'</span>
        <span class="hljs-comment">// 终值为传进来的reason</span>
        <span class="hljs-built_in">this</span>.PromiseResult = reason
        <span class="hljs-comment">// 执行保存的失败回调</span>
+        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilledCallbacks.length) &#123;
+            <span class="hljs-built_in">this</span>.onRejectedCallbacks.shift()(<span class="hljs-built_in">this</span>.PromiseResult)
+        &#125;
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-comment">// 接收两个回调 onFulfilled, onRejected</span>

        <span class="hljs-comment">// 参数校验，确保一定是函数</span>
        onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">val</span> =></span> val
        onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'fulfilled'</span>) &#123;
            <span class="hljs-comment">// 如果当前为成功状态，执行第一个回调</span>
            onFulfilled(<span class="hljs-built_in">this</span>.PromiseResult)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'rejected'</span>) &#123;
            <span class="hljs-comment">// 如果当前为失败状态，执行第二哥回调</span>
            onRejected(<span class="hljs-built_in">this</span>.PromiseResult)
+        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'pending'</span>) &#123;
+            <span class="hljs-comment">// 如果状态为待定状态，暂时保存两个回调</span>
+            <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(onFulfilled.bind(<span class="hljs-built_in">this</span>))
+            <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(onRejected.bind(<span class="hljs-built_in">this</span>))
+        &#125;

    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>加完上面的代码，咱们来看看定时器的效果吧：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-string">'成功'</span>) <span class="hljs-comment">// 1秒后输出 成功</span>
        <span class="hljs-comment">// resolve('成功') // 1秒后输出 失败</span>
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">3. 链式调用</h3>
<p>then支持<code>链式调用</code>，下一次then执行<code>受上一次then返回值的影响</code>，给大家举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 链式调用 输出 200</span>
<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">100</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-number">2</span> * res, <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-comment">// 链式调用 输出300</span>
<span class="hljs-keyword">const</span> p4 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">100</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve(<span class="hljs-number">3</span> * res)), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上方例子，我们可以获取到几个知识点：</p>
<ul>
<li>1、then方法本身会返回一个新的Promise对象</li>
<li>2、如果返回值是promise对象，返回值为成功，新promise就是成功</li>
<li>3、如果返回值是promise对象，返回值为失败，新promise就是失败</li>
<li>4、如果返回值非promise对象，新promise对象就是成功，值为此返回值</li>
</ul>
<p>咱们知道then是Promise上的方法，那如何实现then完还能再then呢？很简单，then执行后返回一个<code>Promise对象</code>就行了，就能保证then完还能继续执行then：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62a3c3afcf0a4262a1a7e52231c34dbc~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午9.06.02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-comment">// 接收两个回调 onFulfilled, onRejected</span>

        <span class="hljs-comment">// 参数校验，确保一定是函数</span>
        onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">val</span> =></span> val
        onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;


        <span class="hljs-keyword">var</span> thenPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;

            <span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function"><span class="hljs-params">cb</span> =></span> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-keyword">const</span> x = cb(<span class="hljs-built_in">this</span>.PromiseResult)
                    <span class="hljs-keyword">if</span> (x === thenPromise) &#123;
                        <span class="hljs-comment">// 不能返回自身哦</span>
                        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'不能返回自身。。。'</span>)
                    &#125;
                    <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                        <span class="hljs-comment">// 如果返回值是Promise</span>
                        <span class="hljs-comment">// 如果返回值是promise对象，返回值为成功，新promise就是成功</span>
                        <span class="hljs-comment">// 如果返回值是promise对象，返回值为失败，新promise就是失败</span>
                        <span class="hljs-comment">// 谁知道返回的promise是失败成功？只有then知道</span>
                        x.then(resolve, reject)
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        <span class="hljs-comment">// 非Promise就直接成功</span>
                        resolve(x)
                    &#125;
                &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                    <span class="hljs-comment">// 处理报错</span>
                    reject(err)
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'fulfilled'</span>) &#123;
                <span class="hljs-comment">// 如果当前为成功状态，执行第一个回调</span>
                resolvePromise(onFulfilled)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'rejected'</span>) &#123;
                <span class="hljs-comment">// 如果当前为失败状态，执行第二个回调</span>
                resolvePromise(onRejected)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState === <span class="hljs-string">'pending'</span>) &#123;
                <span class="hljs-comment">// 如果状态为待定状态，暂时保存两个回调</span>
                <span class="hljs-comment">// 如果状态为待定状态，暂时保存两个回调</span>
                <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(resolvePromise.bind(<span class="hljs-built_in">this</span>, onFulfilled))
                <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(resolvePromise.bind(<span class="hljs-built_in">this</span>, onRejected))
            &#125;
        &#125;)

        <span class="hljs-comment">// 返回这个包装的Promise</span>
        <span class="hljs-keyword">return</span> thenPromise

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在大家可以试试效果怎么样了，大家要<strong>边敲边试</strong>哦：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> test3 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">100</span>) <span class="hljs-comment">// 输出 状态：成功 值： 200</span>
    <span class="hljs-comment">// reject(100) // 输出 状态：失败 值：300</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-number">2</span> * res, <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-number">3</span> * err)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-keyword">const</span> test4 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">100</span>) <span class="hljs-comment">// 输出 状态：失败 值：200</span>
    <span class="hljs-comment">// reject(100) // 输出 状态：成功 值：300</span>
    <span class="hljs-comment">// 这里可没搞反哦。真的搞懂了，就知道了为啥这里是反的</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(<span class="hljs-number">2</span> * res)), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve(<span class="hljs-number">2</span> * res)))
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4. 微任务</h3>
<p>看过<code>js执行机制</code>的兄弟都知道，then方法是<code>微任务</code>，啥叫微任务呢？其实不知道也不要紧，我通过下面例子让你知道：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">1</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)

输出顺序是 <span class="hljs-number">2</span> <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为啥不是 1 2 呢？因为then是个微任务啊。。。同样，我们也要给我们的MyPromise加上这个特性(我这里使用定时器，大家别介意哈)</p>
<p>只需要让<code>resolvePromise函数</code>异步执行就可以了</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function"><span class="hljs-params">cb</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">const</span> x = cb(<span class="hljs-built_in">this</span>.PromiseResult)
            <span class="hljs-keyword">if</span> (x === thenPromise) &#123;
                <span class="hljs-comment">// 不能返回自身哦</span>
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'不能返回自身。。。'</span>)
            &#125;
            <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                <span class="hljs-comment">// 如果返回值是Promise</span>
                <span class="hljs-comment">// 如果返回值是promise对象，返回值为成功，新promise就是成功</span>
                <span class="hljs-comment">// 如果返回值是promise对象，返回值为失败，新promise就是失败</span>
                <span class="hljs-comment">// 谁知道返回的promise是失败成功？只有then知道</span>
                x.then(resolve, reject)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 非Promise就直接成功</span>
                resolve(x)
            &#125;
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
            <span class="hljs-comment">// 处理报错</span>
            reject(err)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> test4 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">1</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res), <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)

输出顺序 <span class="hljs-number">2</span> <span class="hljs-number">1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">其他方法</h2>
<p>这些方法都比较简单，我就不太过详细地讲了，大家也可以借这个机会，自己摸索，巩固这篇文章的知识。</p>
<h3 data-id="heading-11">all</h3>
<ul>
<li>接收一个Promise数组，数组中如有非Promise项，则此项当做成功</li>
<li>如果所有Promise都成功，则返回成功结果数组</li>
<li>如果有一个Promise失败，则返回这个失败结果</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">const</span> result = []
        <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> addData = <span class="hljs-function">(<span class="hljs-params">index, value</span>) =></span> &#123;
                result[index] = value
                count++
                <span class="hljs-keyword">if</span> (count === promises.length) resolve(result)
            &#125;
            promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span> (promise <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                    promise.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                        addData(index, res)
                    &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err))
                &#125; <span class="hljs-keyword">else</span> &#123;
                    addData(index, promise)
                &#125;
            &#125;)
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">race</h3>
<ul>
<li>接收一个Promise数组，数组中如有非Promise项，则此项当做成功</li>
<li>哪个Promise最快得到结果，就返回那个结果，无论成功失败</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            promises.forEach(<span class="hljs-function"><span class="hljs-params">promise</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (promise <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                    promise.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                        resolve(res)
                    &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                        reject(err)
                    &#125;)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    resolve(promise)
                &#125;
            &#125;)
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">allSettled</h3>
<ul>
<li>接收一个Promise数组，数组中如有非Promise项，则此项当做成功</li>
<li>把每一个Promise的结果，集合成数组，返回</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> res = []
            <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
            <span class="hljs-keyword">const</span> addData = <span class="hljs-function">(<span class="hljs-params">status, value, i</span>) =></span> &#123;
                res[i] = &#123;
                    status,
                    value
                &#125;
                count++
                <span class="hljs-keyword">if</span> (count === promises.length) &#123;
                    resolve(res)
                &#125;
            &#125;
            promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, i</span>) =></span> &#123;
                <span class="hljs-keyword">if</span> (promise <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
                    promise.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                        addData(<span class="hljs-string">'fulfilled'</span>, res, i)
                    &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                        addData(<span class="hljs-string">'rejected'</span>, err, i)
                    &#125;)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    addData(<span class="hljs-string">'fulfilled'</span>, promise, i)
                &#125;
            &#125;)
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">any</h3>
<p>any与all相反</p>
<ul>
<li>接收一个Promise数组，数组中如有非Promise项，则此项当做成功</li>
<li>如果有一个Promise成功，则返回这个成功结果</li>
<li>如果所有Promise都失败，则报错</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">any</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
            promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise</span>) =></span> &#123;
                promise.then(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
                    resolve(val)
                &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                    count++
                    <span class="hljs-keyword">if</span> (count === promises.length) &#123;
                        reject(<span class="hljs-keyword">new</span> AggregateError(<span class="hljs-string">'All promises were rejected'</span>))
                    &#125;
                &#125;)
            &#125;)
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">结语</h3>
<p>再也不怕面试官问你Promise原理啦哈哈哈哈😁</p>
<p>如果你觉得此文章对你有一丁点帮助的话，点个赞呗，谢谢你</p>
<p>学习群请点<a href="https://juejin.cn/pin/6969565162885873701" target="_blank" title="https://juejin.cn/pin/6969565162885873701">这里</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91b9a1a197574761a0185119f41619dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            