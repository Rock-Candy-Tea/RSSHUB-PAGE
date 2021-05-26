
---
title: '一文搞懂koa2核心原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc14ab4cc11a4a04b5f84a4ff2bae837~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 19:17:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc14ab4cc11a4a04b5f84a4ff2bae837~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">koa的基础结构</h2>
<p>首先，让我们认识一下koa框架的定位——koa是一个精简的node框架：</p>
<ul>
<li>它基于node原生req和res，封装自定义的request和response对象，并基于它们封装成一个统一的context对象。</li>
<li>它基于async/await（generator）的洋葱模型实现了中间件机制。</li>
</ul>
<p>koa框架的核心目录如下：</p>
<pre><code class="hljs language-js copyable" lang="js">── lib
   ├── application.js
   ├── context.js
   ├── request.js
   └── response.js

<span class="hljs-comment">// 每个文件的具体功能</span>
── lib
   ├── <span class="hljs-keyword">new</span> Koa()  || ctx.app
   ├── ctx
   ├── ctx.req  || ctx.request
   └── ctx.res  || ctx.response
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc14ab4cc11a4a04b5f84a4ff2bae837~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">koa源码基础骨架</h2>
<p><code>application.js</code>
application.js是koa的主入口，也是核心部分，主要干了以下几件事情：</p>
<ol>
<li>完成了koa实例初始化的工作，启动服务器</li>
<li>实现了洋葱模型的中间件机制</li>
<li>封装了高内聚的context对象</li>
<li>实现了异步函数的统一错误处理机制</li>
</ol>
<p><code>context.js</code>
context.js主要干了两件事情：</p>
<ol>
<li>完成了错误事件处理</li>
<li>代理了response对象和request对象的部分属性和方法</li>
</ol>
<p><code>request.js</code>
request对象基于node原生req封装了一系列便利属性和方法，供处理请求时调用。所以当你访问ctx.request.xxx的时候，实际上是在访问request对象上的setter和getter。</p>
<p><code>response.js</code>
response对象基于node原生res封装了一系列便利属性和方法，供处理请求时调用。所以当你访问ctx.response.xxx的时候，实际上是在访问response对象上的setter和getter。</p>
<p><strong>4个文件的代码结构如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c106a1ea444fbc8133f1aa2d8ca026~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ff83931150642e69d7fa60f3b71ee2d~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">koa工作流</h3>
<p><strong>Koa整个流程可以分成三步:</strong></p>
<ol>
<li>初始化阶段</li>
</ol>
<p>new初始化一个实例，包括创建中间件数组、创建context/request/response对象，再使用use(fn)添加中间件到middleware数组，最后使用listen 合成中间件fnMiddleware，按照洋葱模型依次执行中间件，返回一个callback函数给http.createServer，开启服务器，等待http请求。结构图如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/290d83a2818f481c9bb68913582a2a0e~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>请求阶段</li>
</ol>
<p>每次请求，createContext生成一个新的ctx，传给fnMiddleware，触发中间件的整个流程。
3. 响应阶段
整个中间件完成后，调用respond方法，对请求做最后的处理，返回响应给客户端。</p>
<h3 data-id="heading-3">koa中间件机制与实现</h3>
<p>koa中间件机制是采用koa-compose实现的，compose函数接收middleware数组作为参数，middleware中每个对象都是async函数，返回一个以context和next作为入参的函数，我们跟源码一样，称其为fnMiddleware在外部调用this.handleRequest的最后一行，运行了中间件：<code>fnMiddleware(ctx).then(handleResponse).catch(onerror);</code></p>
<p>以下是koa-compose库中的核心函数：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/097d569078ca4e93b34b9e396abf2abc~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们不禁会问：中间件中的next到底是什么呢？为什么执行next就进入到了下一个中间件了呢？中间件所构成的执行栈如下图所示，其中next就是一个含有dispatch方法的函数。在第1个中间件执行next时，相当于在执行dispatch(2)，就进入到了下一个中间件的处理流程。因为dispatch返回的都是Promise对象，因此在第n个中间件await next()时，就进入到了第n+1个中间件，而当第n+1个中间件执行完成后，可以返回第n个中间件。但是在某个中间件中，我们没有写next()，就不会再执行它后面所有的中间件。运行机制如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa709ad09bc94c0895c2b9a1ef355926~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们比较一下koa框架的中间件和mtop框架的中间件运行顺序会有何不同：
以下是mtop client源码中关于中间件的运行机制部分，使用了<code>_sequence</code>函数来包装整个请求过程（包括确定请求方法、请求类型、获取token、签名、中间件、发送请求等流程），<code>Mtop.prototype._sequence</code>方法中，如果传入数组中的元素仍然是数组时，则按顺序对其数组中的各项元素进行依次处理。如<code>that.middlewares</code>是中间件处理的数组，因此在请求过程中，也是对于每个中间件进行依次处理的，和koa的洋葱模型有些不同。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eac7edb49cc4d6f9f2990f75db96f78~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">koa-convert解析</h3>
<p>在koa2中引入了koa-convert库，在使用use函数时，会使用到convert方法（只展示核心的代码）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> convert = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-convert'</span>);

<span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">fn</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'middleware must be a function!'</span>);
        <span class="hljs-keyword">if</span> (isGeneratorFunction(fn)) &#123;
            deprecate(<span class="hljs-string">'Support for generators will be removed'</span>;
            fn = convert(fn);
        &#125;
        debug(<span class="hljs-string">'use %s'</span>, fn._name || fn.name || <span class="hljs-string">'-'</span>);
        <span class="hljs-built_in">this</span>.middleware.push(fn);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>koa2框架针对koa1版本作了兼容处理，中间件函数如果是generator函数的话，会使用koa-convert进行转换为“类async函数”。首先我们必须理解generator和async的区别：async函数会自动执行，而generator每次都要调用next函数才能执行，因此我们需要寻找到一个合适的方法，让next()函数能够一直持续下去即可，这时可以将generator中yield的value指定成为一个Promise对象。下面看看<code>koa-convert</code>中的核心代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> co = <span class="hljs-built_in">require</span>(<span class="hljs-string">'co'</span>)
<span class="hljs-keyword">const</span> compose = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-compose'</span>)

<span class="hljs-built_in">module</span>.exports = convert

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert</span> (<span class="hljs-params">mw</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> mw !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'middleware must be a function'</span>)
  &#125;
  <span class="hljs-keyword">if</span> (mw.constructor.name !== <span class="hljs-string">'GeneratorFunction'</span>) &#123;
    <span class="hljs-keyword">return</span> mw
  &#125;
  <span class="hljs-keyword">const</span> converted = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ctx, next</span>) </span>&#123;
    <span class="hljs-keyword">return</span> co.call(ctx, mw.call(ctx, createGenerator(next)))
  &#125;
  converted._name = mw._name || mw.name
  <span class="hljs-keyword">return</span> converted
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先针对传入的参数mw作校验，如果不是函数则抛异常，如果不是generator函数则直接返回，如果是generator函数则使用co函数进行处理。<a href="https://github.com/tj/co/blob/master/index.js" target="_blank" rel="nofollow noopener noreferrer">co</a>的核心代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">co</span>(<span class="hljs-params">gen</span>) </span>&#123;
  <span class="hljs-keyword">var</span> ctx = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">var</span> args = slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>);
  
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> gen === <span class="hljs-string">'function'</span>) gen = gen.apply(ctx, args);
    <span class="hljs-keyword">if</span> (!gen || <span class="hljs-keyword">typeof</span> gen.next !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">return</span> resolve(gen);

    onFulfilled();
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onFulfilled</span>(<span class="hljs-params">res</span>) </span>&#123;
      <span class="hljs-keyword">var</span> ret;
      <span class="hljs-keyword">try</span> &#123;
        ret = gen.next(res);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> reject(e);
      &#125;
      next(ret);
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onRejected</span>(<span class="hljs-params">err</span>) </span>&#123;
      <span class="hljs-keyword">var</span> ret;
      <span class="hljs-keyword">try</span> &#123;
        ret = gen.throw(err);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> reject(e);
      &#125;
      next(ret);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">ret</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (ret.done) <span class="hljs-keyword">return</span> resolve(ret.value);
      <span class="hljs-keyword">var</span> value = toPromise.call(ctx, ret.value);
      <span class="hljs-keyword">if</span> (value && isPromise(value)) <span class="hljs-keyword">return</span> value.then(onFulfilled, onRejected);
      <span class="hljs-keyword">return</span> onRejected(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'You may only yield a function, promise, generator, array, or object, '</span>
        + <span class="hljs-string">'but the following object was passed: "'</span> + <span class="hljs-built_in">String</span>(ret.value) + <span class="hljs-string">'"'</span>));
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可以看出，co中作了这样的处理：</p>
<ol>
<li>把一个generator封装在一个Promise对象中</li>
<li>这个Promise对象再次把它的gen.next()也封装出Promise对象，相当于这个子Promise对象完成的时候也重复调用gen.next()</li>
<li>当所有迭代完成时，对父Promise对象进行resolve。</li>
</ol>
<p>以上工作完成后，就形成了一个类async函数。</p>
<h3 data-id="heading-5">异步函数的统一错误处理机制</h3>
<p>在koa框架中，有两种错误的处理机制，分别为：</p>
<ol>
<li>中间件捕获</li>
<li>框架捕获</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad28714941643009c17ff5ed5ef3b91~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p>中间件捕获是针对中间件做了错误处理响应，如<code>fnMiddleware(ctx).then(handleResponse).catch(onerror)</code>，在中间件运行出错时，会出发onerror监听函数。框架捕获是在<code>context.js</code>中作了相应的处理<code>this.app.emit('error', err, this)</code>，这里的this.app是对application的引用，当context.js调用onerror时，实际上是触发application实例的error事件 ，因为Application类是继承自EventEmitter类的，因此具备了处理异步事件的能力，可以使用EventEmitter类中对于异步函数的错误处理方法。</p>
<p>koa为什么能实现异步函数的统一错误处理？因为async函数返回的是一个Promise对象，如果async函数内部抛出了异常，则会导致Promise对象变为reject状态，异常会被catch的回调函数(onerror)捕获到。如果await后面的Promise对象变为reject状态，reject的参数也可以被catch的回调函数(onerror)捕获到。</p>
<h3 data-id="heading-6">委托模式在koa中的应用</h3>
<p>delegates库由知名的 TJ 所写，可以帮我们方便快捷地使用设计模式当中的委托模式，即外层暴露的对象将请求委托给内部的其他对象进行处理。</p>
<p>delegates 基本用法就是将内部对象的变量或者函数绑定在暴露在外层的变量上，直接通过 delegates 方法进行如下委托，基本的委托方式包含：</p>
<ul>
<li>getter：外部对象可以直接访问内部对象的值</li>
<li>setter：外部对象可以直接修改内部对象的值</li>
<li>access：包含 getter 与 setter 的功能</li>
<li>method：外部对象可以直接调用内部对象的函数</li>
</ul>
<p>delegates 原理就是__defineGetter__和__defineSetter__。在application.createContext函数中，被创建的context对象会挂载基于request.js实现的request对象和基于response.js实现的response对象。下面2个delegate的作用是让context对象代理request和response的部分属性和方法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/997f433077e84830998b99193c03eb79~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" loading="lazy" referrerpolicy="no-referrer"></p>
<p>做了以上的处理之后，<code>context.request</code>的许多属性都被委托在<code>context上</code>了，<code>context.response</code>的许多方法都被委托在<code>context</code>上了，因此我们不仅可以使用<code>this.ctx.request.xx</code>、<code>this.ctx.response.xx</code>取到对应的属性，还可以通过<code>this.ctx.xx</code>取到<code>this.ctx.request</code>或<code>this.ctx.response</code>下挂载的<code>xx</code>方法。</p>
<p>我们在源码中可以看到，response.js和request.js使用的是get set代理，而context.js使用的是delegate代理，为什么呢？因为delegate方法比较单一，只代理属性；但是使用set和get方法还可以加入一些额外的逻辑处理。在context.js中，只需要代理属性即可，使用delegate方法完全可以实现此效果，而在response.js和request.js中是需要处理其他逻辑的，如以下对query作的格式化操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">get</span> <span class="hljs-title">query</span>() &#123;
        <span class="hljs-keyword">const</span> str = <span class="hljs-built_in">this</span>.querystring;
        <span class="hljs-keyword">const</span> c = <span class="hljs-built_in">this</span>._querycache = <span class="hljs-built_in">this</span>._querycache || &#123;&#125;;
        <span class="hljs-keyword">return</span> c[str] || (c[str] = qs.parse(str));
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            