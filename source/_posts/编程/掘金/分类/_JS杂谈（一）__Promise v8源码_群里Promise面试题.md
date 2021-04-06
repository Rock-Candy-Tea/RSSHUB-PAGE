
---
title: '_JS杂谈（一）__Promise v8源码_群里Promise面试题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4664'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 04:34:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=4664'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>群里看到，不懂就查，查不懂就对线源码。</p>
<h1 data-id="heading-0">题目</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">4</span>)
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res: '</span>, res)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>);
&#125;).then(<span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">输出</h2>
<p><code>1 2 3 4 5 6</code></p>
<h1 data-id="heading-2">逻辑</h1>
<p>首先设<code>1</code>为<code>.then(() => &#123; console.log(1) &#125;)</code>这一个微任务，</p>
<p>其他同理。</p>
<p>一开始执行完两个<code>Promise.resolve()</code>以后：</p>
<pre><code class="copyable">microTask: `0 1`
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise.resolve(4)</code>返回一个状态为<code>fulfilled</code>的<code>Promise</code>此时按逻辑应该把<code>4</code>加入到微任务中了，</p>
<p>但是在<code>then</code>中返回<code>fulfilled</code>状态的<code>Promise</code>的话，</p>
<p><code>Promise</code>内部会将返回的<code>Promise</code>的<code>then</code>方法执行放入到微任务队列中执行。</p>
<pre><code class="copyable">microTask: 1 Promise.resolve(4).then
microTask: Promise.resolve(4).then 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>then</code>内部因为<code>Promise.resolve(4)</code>状态已经是<code>fulfilled</code>了，</p>
<p>又申请了个微任务为了让<code>0</code>同步<code>Promise.resolve(4).then</code>的<code>fulfilled</code>的状态，</p>
<p>因为需要等<code>Promise.resolve(4).then</code>内部暴露的<code>Promise</code>初始化完毕后再执行，</p>
<p>所以需要一个微任务等待。</p>
<p>(实际为：<code>Promise.resolve(4).then</code>返回的<code>Promise</code>需要一个微任务进行同步<code>Promise.resolve(4)</code>返回的<code>Promise</code>的<code>fulfilled</code>状态，在同步时顺便也把外部<code>0</code>返回的<code>Promise</code>一并同步了)</p>
<p>注：<code>0</code>返回的<code>Promise</code>是同步<code>Promise.resolve(4).then</code>的状态</p>
<pre><code class="copyable">microTask: 2 同步状态
microTask: 同步状态 3
microTask: 3 4
最后输出: 1 2 3 4 5 6
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">证明 Then方法会放入微队列中</h2>
<p><code>0</code>修改为</p>
<pre><code class="copyable">.then(() => &#123;
  console.log(0)
    // return Promise.resolve(4)
    return &#123;
      then(resolve) &#123;
      console.log('then')
      resolve(4)
    &#125;,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">输出：
0
1
then
2
res:  4
3
5
6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>then</code>方法是放入了微任务队列中的。</p>
<p>这个<code>then</code>方法中<code>resolve</code>执行直接同步<code>fulfilled</code>状态到<code>0</code>返回的<code>Promise</code>状态上，因此执行完<code>then</code>方法下一个微任务就是输出<code>res</code>了。</p>
<h2 data-id="heading-4">源码</h2>
<p>我翻找了<code>v8</code>在<code>4.3.65</code>版本还未使用<code>v8 Torque(tq v8内部语言)或C</code>实现的<code>promise.js</code>的源码，在5版本以后就使用C实现了，最新版本使用<code>tq</code>实现。</p>
<p>通过看源码可知<code>Promise.resovle(x)</code> 相当于<code>new Promise(rs => rs(x))</code>，两者行为一致，有兴趣可以试试。</p>
<p><a href="https://chromium.googlesource.com/v8/v8/+/4.3.65/src/promise.js" target="_blank" rel="nofollow noopener noreferrer">源码地址</a></p>
<h2 data-id="heading-5">deferred</h2>
<p>首先介绍一下<code>deferred</code>，<code>deferred</code>指内部为了链式调用创建的对象，在<code>then</code>方法被调用时返回的就是<code>deferred</code>，<code>Promise</code>的<code>deferred</code>对象也是个<code>Promise</code>（废话，不这样咋链式</p>
<p>据上面源码可知<code>Promise.then</code>/返回<code>Thenable</code>都会创建这个对象。据我感觉最新返回<code>Thenable</code>并不会创建这个对象，直接使用外部的<code>deferred</code>对象</p>
<pre><code class="copyable">function PromiseDeferred() &#123;
  if (this === $Promise) &#123;
    // Optimized case, avoid extra closure.
    var promise = PromiseInit(new $Promise(promiseRaw));
    return &#123;
      promise: promise,
      resolve: function(x) &#123; PromiseResolve(promise, x) &#125;,
      reject: function(r) &#123; PromiseReject(promise, r) &#125;
    &#125;;
  &#125; else &#123;
    var result = &#123;&#125;;
      result.promise = new this(function(resolve, reject) &#123;
      result.resolve = resolve;
      result.reject = reject;
    &#125;)
    return result;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">理解</h2>
<p><code>=></code>为返回，<code>-></code>为步骤，<code>deferred Object</code>简称为<code>deferred</code></p>
<p>注：之后的"同步状态"微任务只针对非<code>pending</code>状态</p>
<pre><code class="copyable">then(onResolve) => deferred
-> onResolve => Promise(fulfilled)
-> Promise(fulfilled).then(deferred.resolve, deferred.reject)
-> 放入一个微任务"同步状态"到外部 deferred 上
-> 以便链式调用
then(onResolve) => deferred
-> onResolve => Thenable
-> deferred.resolve(Thenable)
  -> then(onResolve).then(onResolve2, onReject2)
  -> deferred.promise.then(onResolve2, onReject2)
  -> 不调用这个 .then 据我理解是不会将 Thenable 对象转换成 defeerred 的
  -> deferred.promise PromiseState is fulfilled
  -> 执行 then 方法，onResolve2 在内部会被包装因此
      -> 执行中 Thenable 转换成 thenDeferred 时同步执行 then 方法
        -> 根据 then 方法执行后决定 thenDeferred.promise 状态
      -> thenDeferred.promise.then(onResolve, onReject)
        -> 挂载 deferred.promise.then 的参数到 thenDeferr.promise.then 上
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回<code>Thenable</code>对象：</p>
<pre><code class="copyable">Promise.resolve()
  .then(() => &#123;
    console.log(0)
    return &#123;
      then(resolve) &#123; // 在4.x源码中这儿是同步执行
        console.log('then')
        resolve(4)
      &#125;,
    &#125;
  &#125;)
  .then(res => &#123;
    console.log('res: ', res)
  &#125;)
相当于
Promise.resolve()
  .then(() => &#123;
    console.log(0)
  &#125;)
  .then(() => &#123; // 在4.x源码中这儿是同步执行
    console.log('then')
    return 4
  &#125;)
  .then(res => &#123;
    console.log('res: ', res)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是在<code>4.3.65</code>版本的实现逻辑（我的理解，有误您对</p>
<h2 data-id="heading-7">源码结论</h2>
<p>返回<code>Promise</code>都是需要一个微任务，但是<code>Thenable</code>又不需要，但是这是4.多的代码实现，之后代码改动很大，不过思路大体一致。（应该吧，我看不懂后面的了太菜了</p>
<h1 data-id="heading-8">推测</h1>
<p>因为这是<code>4.3.65</code>的代码了，所以不符合之前推理的逻辑也正常，虽然这个版本的代码已经挺优雅了，但是可能为了更优雅的实现，<code>Thenable</code>/<code>Promise</code>的<code>then</code>要一视同仁，也得放进微任务中执行，没必要做特殊处理，所以两个的<code>then</code>方法都进入了微任务队列中处理。（我寻思挺合理的</p>
<p>其次我的源码理解的返回<code>Thenable</code>对象的<code>promise</code>后面得再跟一个<code>then</code>方法才会执行<code>Thenable.then</code>，所以需要改动并统一行为。（可能是我理解错误？</p>
<p>那么为什么在目前的版本就是返回<code>Promise</code>是要两个微任务，而<code>Thenable</code>还是一个</p>
<h2 data-id="heading-9">讲道理</h2>
<p>据我推测在之后版本中，只要有<code>Then</code>都会放入微任务队列执行一下，如果是<code>Promise</code>：</p>
<p>同步状态其实相当于往一个<code>promise</code>的<code>then</code>方法传入<code>(deferred.resolve, deferred.reject)</code>简称这个行为为<code>同步d</code>。</p>
<p>不讨论<code>rejected</code>状态（或者说和 <code>fulfilled</code>状态差不多</p>
<pre><code class="copyable">PromiseState is fulfilled/Thenable Object:
设 Promise.resolve().then() 返回的 deferred 为 d
Promise.resolve().then(() => Promise.resolve(4))
-> Promise.resolve(4) => Promise(fulfilled) 且非 deferred
-> 内部处理
-> 有 then 方法进行劫持放进微任务队列中执行
-> 由于 then 方法未传入参数, 默认为 onResolve = x => x
-> 即 Promise(fulfilled).then(x => x)
-> pending 状态需要同步
-> Promise(fulfilled).then(x => x).then(同步d)
-> 以上是按照 4.x 逻辑来的，不过 then 方法变成异步罢了
Promise.resolve().then(() => (&#123; then(rs) &#123; rs(4) &#125;&#125;)
-> Thenable 在微任务被调用 then 方法时内部会传入 d.resolve, d.reject 来直接同步外部，
-> 因此只需要一个微任务执行 then 方法即可
新的内部实现应该比这优雅，但是可惜我看不懂
Promise.resolve(4).then(res => res) -> PromiseState is pending:
将当前的promise.then中放入同步状态微任务，
以便可以同步状态到deferred对象上
比如：
    Promise.resolve().then(() => Promise.resolve(4).then(res => res))
    Promise.resolve().then() 返回的是 deferred(d)
    Promise.resolve(4).then(res => res) 返回的也是 deferred(thenD)
    因为需要同步状态，因此内部处理挂载上去
    Promise.resolve(4).then(res => res).then(同步d)
    以便d能及时更新状态
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">根据</h2>
<p>前面代码改成</p>
<pre><code class="copyable">Promise.resolve()
  .then(() => &#123;
    console.log(0)
    return Promise.resolve(4).then(res => res) // pending 状态挂载同步状态微任务
  &#125;).then(res => &#123;
    console.log('res: ', res)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：<code>0 1 2 3 4 5 6</code></p>
<h1 data-id="heading-11">结语</h1>
<p>一时兴起，大胆猜测，人菜想写，如有错误，轻骂。</p>
<p>内部实现写的好导致的结果，我反正信了。(doge</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            