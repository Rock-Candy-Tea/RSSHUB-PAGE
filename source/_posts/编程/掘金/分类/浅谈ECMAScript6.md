
---
title: '浅谈ECMAScript6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d8d57fe7ef452b9fee6f6cb6d23077~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 02:39:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d8d57fe7ef452b9fee6f6cb6d23077~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>对es6语法的练习与总结篇</p>
</blockquote>
<h1 data-id="heading-0">1.Proxy</h1>
<p>Proxy 可以理解成，在目标对象之前架设一层"拦截",外界对该对象访问的时候</p>
<p>都必须先通过这一层拦截，相当于提供了一种机制，可以对外界的访问进行过滤和改写</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Proxy对象的所有用法，都是上面这种形式，不同的只是 handler 参数的写法。其中， new Proxy() 表示</strong></p>
<p>生成一个Proxy实例，target参数表示所要拦截的目标对象， handler 参数也是一个对象，用来定制拦截行为。</p>
<ul>
<li>get方法拦截读取，里面有两个参数，传入的对象与属性</li>
<li>set方法可以设置属性值，但是不会改变原有对象，拦截对象属性的赋值操作</li>
<li>has方法可以拦截判断该对象中是否有该属性</li>
<li>拦截delete操作</li>
</ul>
<p>拦截对象自身属性的读取操作</p>
<h1 data-id="heading-1">2.Reflect</h1>
<p>程序在运行的时候去获取对象内部的结构就叫做反射</p>
<p><strong>1.将原先Object对象上定义的一些方法，放入Reflect对象(代码重构)</strong>
 </p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01d8d57fe7ef452b9fee6f6cb6d23077~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
   // Reflect.defineProperty</p>
<p><strong>2.修改了某些Object方法的返回结果</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7523e60de3f4b0b9353b43d0b06dd1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>3.让Object操作变成函数行为</strong></p>
<ul>
<li>   name in obj/delete obj.name 命令式</li>
<li>   Reflect.has(obj.name)/Reflect.deleteProperty(obj,name)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/690f6ac53bd34b639ba498cdc0a4be53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p> <strong>4.Reflect对象的方法和Proxy对象方法对应</strong></p>
<p>   //可以让Proxy方便的调用对应的Reflect方法</p>
<p><strong>5.修改指定函数的this指向</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86cdeb623ad743e1acef2a834e775f1d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b4048837487455e9bd28125c954d50b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>求数组的最大值最小值</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc6d3a19b86c463da0f1ff6fe670c73a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc6ea82032d4540b27d52dd03473662~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/720f7a5a3cc2499e83491af3b7c65a61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3.观察者模式</p>
<pre><code class="hljs language-js copyable" lang="js">在监听对象属性改变的同时，执行指定其他的业务操作

 <span class="hljs-comment">//先定义一个容器，存放需要执行的业务操作</span>

​    <span class="hljs-keyword">let</span> box = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()

​    <span class="hljs-comment">//定义一个函数将所有的业务操作都放进去</span>

​    <span class="hljs-keyword">let</span> actions = <span class="hljs-function"><span class="hljs-params">fn</span> =></span> &#123;

​      box.add(fn)

​    &#125;

​    <span class="hljs-comment">// 定义两个业务</span>

​    <span class="hljs-keyword">let</span> fn1 = <span class="hljs-function">() =></span> &#123;

​      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"业务一"</span>)

​    &#125;

​    actions(fn1)<span class="hljs-comment">//传入参数，目的是将业务放入容器中</span>

​    <span class="hljs-keyword">let</span> fn2 = <span class="hljs-function">() =></span> &#123;

​      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"业务二"</span>)

​    &#125;

​    actions(fn2)<span class="hljs-comment">//传入参数，目的是将业务放入容器中</span>



​    <span class="hljs-comment">//创建一个函数用于生成一个代理对象</span>

​    <span class="hljs-keyword">let</span> createproxy = <span class="hljs-function"><span class="hljs-params">target</span> =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;

​      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value</span>)</span> &#123;

​        <span class="hljs-built_in">Reflect</span>.set(target, key, value)<span class="hljs-comment">//设置值</span>

​        <span class="hljs-comment">//执行其他业务操作</span>

​        box.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> &#123;

​          fn()<span class="hljs-comment">//遍历放在容器中的业务操作，并执行</span>

​        &#125;)

​      &#125;

​    &#125;)

​    <span class="hljs-comment">//定义一个实例对象</span>

​    <span class="hljs-keyword">let</span> obj = &#123;

​      name: <span class="hljs-string">"wangsu"</span>,

​      age: <span class="hljs-number">23</span>,

​      grade: <span class="hljs-number">90</span>,

​      __job__: <span class="hljs-string">"IT"</span>

​    &#125;

​    <span class="hljs-comment">//修改属性，调用函数执行</span>

​    <span class="hljs-keyword">let</span> proxy = createproxy(obj)

​    proxy.name = <span class="hljs-string">"kobe"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">4.promise</h1>
<h2 data-id="heading-3">4.1.promise的定义（面试重点）</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1023cbd530dc43ccb8ee2911ebb78097~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Promise是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。它由社区</p>
<p>最早提出和实现，ES6将其写进了语言标准，统一了用法，原生提供了 Promise 对象。</p>
<p>所谓 Promise ，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结</p>
<p>果。从语法上说，Promise是一个对象，从它可以获取异步操作的消息。Promise提供统一的API，各种异步操</p>
<p>作都可以用同样的方法进行处理。</p>
<pre><code class="copyable">    ## 4.2 Promise两个特点
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1. 对象的状态不受外界影响。</strong>
Promise 对象代表一个异步操作，有三种状态： Pending （进行
中）、 Resolved （已完成，又称Fulfilled）和 Rejected （已失败）。只有异步操作的结果，可以决定当</p>
<p>前是哪一种状态，任何其他操作都无法改变这个状态。这也是 Promise 这个名字的由来，它的英语意思就</p>
<p>是“承诺”，表示其他手段无法改变。</p>
<p><strong>2. 一旦状态改变，就不会再变，任何时候都可以得到这个结果.</strong></p>
<pre><code class="hljs language-text copyable" lang="text"> Promise 对象的状态改变，只有两种可能：从 Pending 变为 Resolved 和从 Pending 变
 为 Rejected 。只要这两种情况发生，状态就凝固了，不会再变了，会一直保持这个结果。
 就算改变已经发生了，你再对 Promise 对象添加回调函数，也会立即得到这个结果。这与事
 件（Event）完全不同，事件的特点是，如果你错过了它，再去监听，是得不到结果的。
 了 Promise 对象，就可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调
 函数。此外， Promise 对象提供统一的接口，使得控制异步操作更加容易。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. Promise 也有一些缺点。</strong></p>
<pre><code class="hljs language-js copyable" lang="js">- 首先，无法取消 <span class="hljs-built_in">Promise</span> ，一旦新建它就会立即执行，无法中途取消。
- 其次，如果不设置回调函数， <span class="hljs-built_in">Promise</span> 内部抛出的错误，不会反应到外部。
- 第三，当处于 Pending 状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）。
- 如果某些事件不断地反复发生，一般来说，使用stream模式是比部署 <span class="hljs-built_in">Promise</span> 更好的选择。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.3.promise解决文件读取顺序和回调地狱问题</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>)
<span class="hljs-comment">//封装一个读文件的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reads</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;<span class="hljs-comment">//返回一个promise</span>
​    fs.readFile(path, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;<span class="hljs-comment">//读取文件数据</span>
​      <span class="hljs-keyword">if</span> (!err) &#123;
​        resolve(data.toString())<span class="hljs-comment">//将读取的数据用resolve返回出去</span>
​      &#125;
​      <span class="hljs-keyword">else</span> &#123;
​        reject(err)<span class="hljs-comment">//发送拒绝后抛错</span>
​      &#125;

​    &#125;)

  &#125;)

&#125;

reads(<span class="hljs-string">"../data/a.txt"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;<span class="hljs-comment">//这里函数中的data便是resolve 中返回出来已经读取的数据</span>
​    <span class="hljs-built_in">console</span>.log(data)
​    <span class="hljs-keyword">return</span> reads(<span class="hljs-string">"../data/b.txt"</span>)
​    <span class="hljs-comment">//这里返回下一个需要读取的文件，在调用一下读取函数，这个函数的返回值是一个Promise</span>

  &#125;,
​    (err) => &#123;
​      <span class="hljs-keyword">throw</span> err
​    &#125; ).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
​    <span class="hljs-comment">//由于封装的reads方法返回的是一个promise对象，因此可以继续调用它的then方法</span>
​    <span class="hljs-built_in">console</span>.log(data)
​    <span class="hljs-keyword">return</span> reads(<span class="hljs-string">"../data/c.txt"</span>)
  &#125;,<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
​      <span class="hljs-keyword">throw</span> err
​    &#125;).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
​      <span class="hljs-built_in">console</span>.log(data)
​      <span class="hljs-keyword">return</span> reads(<span class="hljs-string">"../data/d.txt"</span>)
​    &#125;,
​      (err) => &#123;
​        <span class="hljs-keyword">throw</span> err
​      &#125;
​    ).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
​      <span class="hljs-built_in">console</span>.log(data)
​    &#125;,
​      (err) => &#123;
​        <span class="hljs-keyword">throw</span> err
​      &#125;
​    )
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4.4.promise异步解决</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1108e450aeb24b0c8902146de1948486~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">由于开始的时候settimeout是一种异步处理函数，那么当程序执行时，程序不会从上到下依次
执行，遇到异步处理时不会等待，此时会造成settimeoutl里面的代码执行可能会在其他代码
执行之后
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4.5.promise-all</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb5b06402b14cd0bcfb14ec17c4c8ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">4.6.promise-race</h2>
<p>加载请求速度最快的那个请求</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d78182d2e954ddfa6dbe30d440b1b21~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">4.7.模拟promise图片加载</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//创建一个图片加载函数</span>
​    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadImage</span>(<span class="hljs-params">url,resolve,reject</span>) </span>&#123;
​      <span class="hljs-keyword">let</span> img = <span class="hljs-keyword">new</span> Image()
​      img.src = url
​      img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
​        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"图片加载成功"</span>)
​        resolve(&#123;<span class="hljs-attr">width</span>:img.width,<span class="hljs-attr">height</span>:img.height&#125;)<span class="hljs-comment">//在函数中传入参数（图片</span>
的高度宽度）

​      &#125;

​      img.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
​        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"图片加载失败"</span>)
​        reject()
​      &#125;
​    &#125;

​    <span class="hljs-keyword">let</span> url=<span class="hljs-string">"https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?
image&quality=100&size=b4000_4000&sec=1594954864&di=c86ca29e92ae5ba6ef0400ba
dc17a69a&src=http://a3.att.hudong.com/14/75/01300000164186121366756803686.jpg"</span>

​    
   <span class="hljs-comment">//创建两个函数，分别是图片加载完成和图片加载失败</span>
​    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">data</span>) </span>&#123;
​      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"图片加载完成，执行某个处理"</span>)
​      <span class="hljs-built_in">console</span>.log(data)
​    &#125;

​    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params"></span>) </span>&#123;

​      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"图片加载失败，执行某个处理"</span>)
​    &#125;
​    loadImage(url,resolve,reject)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">5.defineproperty数据劫持</h1>
<blockquote>
<p>在给对象赋值的时候可以得到对象赋值的过程</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这是将要被劫持的对象</span>
<span class="hljs-keyword">const</span> data = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'古天乐'</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'给大家推荐一款超好玩的游戏'</span>);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'渣渣辉'</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'戏我演过很多,可游戏我只玩贪玩懒月'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'来做我的兄弟'</span>);
  &#125;
&#125;

<span class="hljs-comment">// 遍历对象,对其属性值进行劫持</span>
<span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(data, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get'</span>);
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">newVal</span>) </span>&#123;
      <span class="hljs-comment">// 当属性值发生变化时我们可以进行额外操作</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`大家好,我系<span class="hljs-subst">$&#123;newVal&#125;</span>`</span>);
      say(newVal);
    &#125;,
  &#125;);
&#125;);

data.name = <span class="hljs-string">'渣渣辉'</span>;
<span class="hljs-comment">//大家好,我系渣渣辉</span>
<span class="hljs-comment">//戏我演过很多,可游戏我只玩贪玩懒月</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">6.字符串匹配方法</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f79b93b19545b9a4d2c7e124d07786~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b4246e4bf2048db958823902bb72c3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">7.symbol</h1>
<h2 data-id="heading-12">7.1.基本意义</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/212f783fd9824f04a328f7e0e3a94f2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">7.2.symbol作为属性调用</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa255820aa654b09a8dc01d1b184aceb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>只能用上面的方式</p>
</blockquote>
<h1 data-id="heading-14">8.Set与Map</h1>
<h2 data-id="heading-15">8.1.set</h2>
<h3 data-id="heading-16">8.1.1.常用方法</h3>
<blockquote>
<p>一种类似数组的数据结构</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc807c55dbf48558203af795cca832a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">8.1.2.数组去重</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe63893255643fbb971b02463621df8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/939712e34b1840ada5f9a62cf7883c7b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">8.1.3.并集，差集，交集</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94aa2d555dd944ad81e6599bce11baaa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">8.2.WeakSet</h2>
<h3 data-id="heading-20">8.2.1.与set的区别</h3>
<p>eakSet 结构与 Set 类似，也是不重复的值的集合。但是，它与 Set 有两个区别。</p>
<p>首先，WeakSet 的成员只能是对象，而不能是其他类型的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
ws.add(<span class="hljs-number">1</span>)
<span class="hljs-comment">// TypeError: Invalid value used in weak set</span>
ws.add(<span class="hljs-built_in">Symbol</span>())
<span class="hljs-comment">// TypeError: invalid value used in weak set</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码试图向 WeakSet 添加一个数值和Symbol值，结果报错，因为 WeakSet 只能放置对象。</p>
<h3 data-id="heading-21">8.2.2.基本概念（面试问到）</h3>
<pre><code class="hljs language-text copyable" lang="text">其次，WeakSet 中的对象都是弱引用，即垃圾回收机制不考虑 WeakSet 对该对象的引用，也就是说，如果其他对象都不再引用该对象，那么垃圾回收机制会自动回收该对象所占用的内
存，不考虑该对象还存在于 WeakSet 之中。

这是因为垃圾回收机制依赖引用计数，如果一个值的引用次数不为，垃圾回收机制就不会释放
这块内存。结束使用该值之后，有时会忘记取消引用，导致内存无法释放，进而可能会引发内
存泄漏。WeakSet 里面的引用，都不计入垃圾回收机制，所以就不存在这个问题。因此，
WeakSet 适合临时存放一组对象，以及存放跟对象绑定的信息。只要这些对象在外部消失，它
在 WeakSet 里面的引用就会自动消失。

由于上面这个特点，WeakSet 的成员是不适合引用的，因为它会随时消失。另外，由于
WeakSet 内部有多少个成员，取决于垃圾回收机制有没有运行，运行前后很可能成员个数是不
一样的，而垃圾回收机制何时运行是不可预测的，因此 ES6 规定 WeakSet 不可遍历
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">8.3.map</h2>
<p>JavaScript 的对象（Object），本质上是键值对的集合（Hash 结构），但是传统上只能用字符串当作键。这给它的使用带来了很大的限制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = &#123;&#125;;
<span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'myDiv'</span>);

data[element] = <span class="hljs-string">'metadata'</span>;
data[<span class="hljs-string">'[object HTMLDivElement]'</span>] <span class="hljs-comment">// "metadata"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码原意是将一个 DOM 节点作为对象data的键，但是由于对象只接受字符串作为键名，所以element被自动转为字符串[object HTMLDivElement]。</p>
<p>为了解决这个问题，ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应，是一种更完善的 Hash 结构实现。如果你需要“键值对”的数据结构，Map 比 Object 更合适。</p>
<p>上面代码在新建 Map 实例时，就指定了两个键name和title</p>
<blockquote>
<p>常用方法</p>
</blockquote>
<blockquote>
<p>（1）size 属性</p>
</blockquote>
<p>size属性返回 Map 结构的成员总数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'foo'</span>, <span class="hljs-literal">true</span>);
map.set(<span class="hljs-string">'bar'</span>, <span class="hljs-literal">false</span>);

map.size <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>（2）Map.prototype.set(key, value)</p>
</blockquote>
<p>set方法设置键名key对应的键值为value，然后返回整个 Map 结构。如果key已经有值，则键值会被更新，否则就新生成该键。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(<span class="hljs-string">'edition'</span>, <span class="hljs-number">6</span>)        <span class="hljs-comment">// 键是字符串</span>
m.set(<span class="hljs-number">262</span>, <span class="hljs-string">'standard'</span>)     <span class="hljs-comment">// 键是数值</span>
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>)    <span class="hljs-comment">// 键是 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>set方法返回的是当前的Map对象，因此可以采用链式写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  .set(<span class="hljs-number">1</span>, <span class="hljs-string">'a'</span>)
  .set(<span class="hljs-number">2</span>, <span class="hljs-string">'b'</span>)
  .set(<span class="hljs-number">3</span>, <span class="hljs-string">'c'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>（3）Map.prototype.get(key)</p>
</blockquote>
<p>get方法读取key对应的键值，如果找不到key，返回undefined。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">const</span> hello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);&#125;;
m.set(hello, <span class="hljs-string">'Hello ES6!'</span>) <span class="hljs-comment">// 键是函数</span>
m.get(hello)  <span class="hljs-comment">// Hello ES6!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>（4）Map.prototype.has(key)</p>
</blockquote>
<p>has方法返回一个布尔值，表示某个键是否在当前 Map 对象之中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(<span class="hljs-string">'edition'</span>, <span class="hljs-number">6</span>);
m.set(<span class="hljs-number">262</span>, <span class="hljs-string">'standard'</span>);
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>);
m.has(<span class="hljs-string">'edition'</span>)     <span class="hljs-comment">// true</span>
m.has(<span class="hljs-string">'years'</span>)       <span class="hljs-comment">// false</span>
m.has(<span class="hljs-number">262</span>)           <span class="hljs-comment">// true</span>
m.has(<span class="hljs-literal">undefined</span>)     <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>（5）Map.prototype.delete(key)</p>
</blockquote>
<p>delete方法删除某个键，返回true。如果删除失败，返回false。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>);
m.has(<span class="hljs-literal">undefined</span>)     <span class="hljs-comment">// true</span>
m.delete(<span class="hljs-literal">undefined</span>)
m.has(<span class="hljs-literal">undefined</span>)       <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>（6）Map.prototype.clear()</p>
</blockquote>
<p>clear方法清除所有成员，没有返回值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'foo'</span>, <span class="hljs-literal">true</span>);
map.set(<span class="hljs-string">'bar'</span>, <span class="hljs-literal">false</span>);
map.size <span class="hljs-comment">// 2</span>
map.clear()
map.size <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">9.itertor遍历器</h1>
<h2 data-id="heading-24">9.1.基本概念</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/110767bcaab14cb4aeefb13fd9109855~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ecda2418daf4762b9eb3f26318ce8cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> target = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">34</span>, <span class="hljs-number">6</span>, <span class="hljs-number">8</span>, <span class="hljs-number">45</span>, <span class="hljs-number">31</span>, <span class="hljs-number">2</span>]

​    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myinter</span>(<span class="hljs-params">arr</span>) </span>&#123;

​      <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>

​      <span class="hljs-keyword">return</span> &#123;

​        <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;

<span class="hljs-keyword">return</span> index < arr.length ? &#123; <span class="hljs-attr">value</span>: arr[index++], <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span> &#125; : &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">done</span>: <span class="hljs-literal">true</span> &#125;

​     <span class="hljs-comment">//设置index,使得每次调用next方法时，index加一，对应数组的索引值</span>

&#125;

​      &#125;

​    &#125;

​    <span class="hljs-keyword">let</span> it = myinter(target)<span class="hljs-comment">//函数调用</span>

​    <span class="hljs-comment">// console.log(it.next())</span>

​    <span class="hljs-comment">// console.log(it.next())</span>

​    <span class="hljs-comment">// console.log(it.next())</span>

​    <span class="hljs-comment">// console.log(it.next())</span>

​    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= target.length; i++) &#123;

​      <span class="hljs-built_in">console</span>.log(it.next())<span class="hljs-comment">//调用封装后的next方法</span>

​    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">9.2.接口部署</h2>
<p>对象无法使用for of遍历，因为内部没有遍历器</p>
<p>所有能够用for of遍历的对象，需要在它的Sysbol.itertor属性上部署一个itretor接口</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d533dab1fd8e41c1b2d6965a53f00804~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>部署好接口后，对象便可以使用for of遍历</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0a0190097544bc84e551cb78466d94~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-26">10.Generator函数</h1>
<h2 data-id="heading-27">10.1.两个特征</h2>
<p>异步解决的方案，是一个状态机，封装了多个状态</p>
<ul>
<li>1.function后有个*</li>
<li>2.函数体内使用yield定义不同的内部状态</li>
</ul>
<h2 data-id="heading-28">10.2.初步使用</h2>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;

​      <span class="hljs-keyword">yield</span> <span class="hljs-string">"hello"</span>;<span class="hljs-comment">//第一个状态</span>

​      <span class="hljs-keyword">yield</span> <span class="hljs-string">"world"</span>;<span class="hljs-comment">//第二个状态</span>

​      <span class="hljs-keyword">return</span> <span class="hljs-string">"endconing"</span>;<span class="hljs-comment">//第三个状态</span>

​    &#125;

​    <span class="hljs-comment">//调用函数</span>

  <span class="hljs-keyword">let</span> fn1 = fn()<span class="hljs-comment">//函数不会立即执行,返回一个遍历器对象</span>
​    <span class="hljs-comment">//第一次调用，Generator函数开始执行，直到遇到第一个 yield 语句为止。 next </span>
<span class="hljs-comment">//方法返回一个对象，</span>

​    <span class="hljs-comment">//它 的 value 属性就是当前 yield 语句的值hello， done 属性的值false，表示</span>
<span class="hljs-comment">//遍历还没有结束</span>

​    <span class="hljs-keyword">let</span> a1= fn1.next()
​    <span class="hljs-built_in">console</span>.log(a1
​    <span class="hljs-comment">// 第二次调用，Generator函数从上次 yield 语句停下的地方，一直执行到下一个 </span>
<span class="hljs-comment">//yield 语句。 next 方法</span>

​    <span class="hljs-comment">// 返回的对象的 value 属性就是当前 yield 语句的值world， done 属性的值</span>
<span class="hljs-comment">//false，表示遍历还没有结束。</span>

​    <span class="hljs-keyword">let</span> a2= fn1.next()

​    <span class="hljs-built_in">console</span>.log( a2)



​    <span class="hljs-comment">// 第三次调用，Generator函数从上次 yield 语句停下的地方，一直执行到 return 语句</span>

​    <span class="hljs-comment">// （如果没有return语句，就执行到函数结束）。next 方法返回的对象的value属性,</span>

​    <span class="hljs-comment">// 就是紧跟在 return语句后面的表达式的值（如果没有 return 语句，则 value 属</span>
<span class="hljs-comment">//性的值为undefined），</span>

​    <span class="hljs-comment">// done 属性的值true，表示遍历已经结束</span>

​    <span class="hljs-keyword">let</span> a3=fn1.next()

​    <span class="hljs-built_in">console</span>.log( a3)

​    <span class="hljs-comment">// 第四次调用，此时Generator函数已经运行完毕， next 方法返回对象的 value 属</span>
<span class="hljs-comment">//性为 undefined，</span>

​    <span class="hljs-comment">// done 属性为true。以后再调用 next 方法，返回的都是这个值。</span>

​    <span class="hljs-keyword">let</span> a4=fn1.next()

​    <span class="hljs-built_in">console</span>.log( a4)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7df1da01e87c46268df8ccbda9b3377d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">10.3.与itertor接口的关系</h2>
<blockquote>
<p>Generator函数就是itertor遍历器对象生成的函数</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f4fb4a0331748068bdaf6a57cbcf5cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>yield与return的区别？</p>
</blockquote>
<p>相似之处在于，都能返回紧跟在语句后面的那个表达式的值。区别在于每次遇到yield，函数暂停执行，下一次再从该位置继续向后执行，而return语句不具备位置记忆的功能。一个函数里面，只能执行一次（或者说一个）return语句，但是可以执行多次（或者说多个）yield表达式。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5495d7500b047398a0985cc0633f0a5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>11.数组解构赋值惰性求值</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f848ec2198a4615b8255b88c1490dca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-30">12.class类</h1>
<h2 data-id="heading-31">12.1.class基本语法</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ea9c360fcd6433086db1ab0ee45b923~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-32">12.2.静态成员</h2>
<blockquote>
<p>属于构造函数而不属于实例对象，在类中就是属于类而不属于实例对象。要清晰和方便很多。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76171c9f2c084d5d85f952c0c07eb831~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cc56addc61646e0b973637638dc26e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-33">12.3.类继承</h2>
<h3 data-id="heading-34">12.3.1.基本语法</h3>
<p>Class 可以通过关键字实现继承，这比 ES5 的通过修改原型链实现继承，要清晰和方便很多。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf92a345c7544797b2e1869f67bee00c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上面代码定义了一个类，该类通过关键字，继承了类的所有属性和方法。但是由于没有部署任何代码，所以这两个类完全一样，等于复制了一个类。下面，我们在内部加上代码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eafc6baa6ace4e6986b4f2633e963c5e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上面代码中，方法和方法之中，都出现了关键字，它在这里表示父类的构造函数，用来新建父类的对象。</p>
<pre><code class="hljs language-text copyable" lang="text">子类必须在方法中调用方法，否则新建实例时会报错。这是因为子类自己的对象，必须先通过
父类的构造函数完成塑造，得到与父类同样的实例属性和方法，然后再对其进行加工，加上子
类自己的实例属性和方法。如果不调用方法，子类就得不到对象。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">12.3.2super 关键字</h3>
<p>super 关键字需要写下子类this之前，相当于借用了父类的构造函数</p>
<p>图下：子类需要继承父类的tostring方法，需要使用super.tostring的方式</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab10c188d8b54a2cacc0b77b5983bfa3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-36">13.新定义的的Object方法</h1>
<h2 data-id="heading-37">1.Object.setPrototypeOf</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c898f4c932c94130b2e2487887868c62~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-38">2.Object.keys</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d0f695601134d8e9322be5469ca7232~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-39">3.Object.values</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf121c11688840aeaa30e95b4ced9dfe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-40">4.Object.entries</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb877abb1e0d4762aef61ce6e93d27c7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-41">5.getOwnPropertyDescriptor</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92a9da6dc24c471dad6116e4b7bc6e13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-42">6.Object.assign()</h2>
<p>Object.assign()方法用于对象的合并，将源对象（source）的所有可枚举属性，复制到目标对象（target）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-keyword">const</span> source1 = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> source2 = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;
<span class="hljs-built_in">Object</span>.assign(target, source1, source2);
target <span class="hljs-comment">// &#123;a:1, b:2, c:3&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Object.assign()方法的第一个参数是目标对象，后面的参数都是源对象。</p>
</blockquote>
<p>注意，如果目标对象与源对象有同名属性，或多个源对象有同名属性，则后面的属性会覆盖前面的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-keyword">const</span> source1 = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> source2 = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;
<span class="hljs-built_in">Object</span>.assign(target, source1, source2);
target <span class="hljs-comment">// &#123;a:1, b:2, c:3&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果只有一个参数，Object.assign()会直接返回该参数。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;;
<span class="hljs-built_in">Object</span>.assign(obj) === obj <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-43">14.函数的rest参数与扩展运算符</h1>
<h2 data-id="heading-44">14.1.rest参数</h2>
<blockquote>
<p>用于获取函数的实参，代替arguments</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/661b5d972b5d43349866121d9ebe9ce3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-45">14.2.扩展运算符</h2>
<blockquote>
<p>将数组分割成逗号分隔的参数序列</p>
</blockquote>
<h1 data-id="heading-46">15.数组中增加的一些方法</h1>
<h2 data-id="heading-47">15.1.find,findindex,filter的比较</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bb418dbc16e4ecfb58fd06de52aca5a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-48">15.2.value,key,entries的比较</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5991f5f0bb7848c694d3cf70359afeb9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-49">16.函数参数的解构赋值</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/955bce7502be486a98ab34c8822803e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-50">17.箭头函数</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f134e15ca841109dcb5ae6087f4d31~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上面代码之中，只有一个，就是函数的，所以都输出同样的结果。因为所有的内层函数都是箭头函数，都没有自己的，它们的其实都是最外层函数的。</p>
<h1 data-id="heading-51">18.链判断运算符</h1>
<blockquote>
<p>编程实务中，如果读取对象内部的某个属性，往往需要判断一下该对象是否存在。比如，要读取，安全的写法是写成下面这样</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b607dcf8fd148858b7ed409a0f4f31c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a8d68512e6d460ab9325bb4b2a3ccf5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cb13d58ca7046ec920614684551e0ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-52">19.async 函数</h1>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//1.使用then方法调用</span>
​    <span class="hljs-comment">//2.使用await</span>
​    <span class="hljs-comment">//只能在async函数中使用，await之后只能是一个promise对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-53">19.2具体使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//request.js封装请求</span>
<span class="hljs-keyword">let</span> baseUrl=<span class="hljs-string">"http://192.168.24.36:3000/"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">http</span>(<span class="hljs-params">url</span>)</span>&#123;
  <span class="hljs-keyword">return</span> $.ajax(&#123;
​    url:baseUrl+url,
​    type:<span class="hljs-string">"get"</span>
  &#125;)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.html页面中发送请求</span>
<span class="hljs-keyword">let</span> url=<span class="hljs-string">"top/playList?cat=华语"</span>
​    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getdata</span>(<span class="hljs-params"></span>)</span>&#123;
​      <span class="hljs-keyword">let</span> cat=<span class="hljs-keyword">await</span> http(url)
​      <span class="hljs-keyword">let</span> id=cat.playlists[<span class="hljs-number">0</span>].id
​      <span class="hljs-keyword">let</span> detail=<span class="hljs-keyword">await</span> http(<span class="hljs-string">`playlist/detail?id=<span class="hljs-subst">$&#123;id&#125;</span>`</span>)
​      <span class="hljs-keyword">let</span> songId=detail.playlist.tracks[<span class="hljs-number">0</span>].id
​      <span class="hljs-keyword">let</span> songurl=<span class="hljs-keyword">await</span> http(<span class="hljs-string">`song/url?id=<span class="hljs-subst">$&#123;songId&#125;</span>`</span>)
​      <span class="hljs-built_in">console</span>.log(songurl)
​    &#125;

​    getdata()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-54">20总结</h1>
<blockquote>
<p>这是一篇根据对学习es6的总结，对学习es6的记录,总结供大家参考讨论</p>
</blockquote>
<h1 data-id="heading-55">21.参考文献</h1>
<ul>
<li>ECMAScript6 (原著:阮一峰)</li>
<li>深入理解ES6</li>
</ul></div>  
</div>
            