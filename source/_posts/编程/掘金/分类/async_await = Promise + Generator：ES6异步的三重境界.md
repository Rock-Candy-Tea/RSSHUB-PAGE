
---
title: 'async_await = Promise + Generator：ES6异步的三重境界'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1620'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 01:40:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=1620'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>异步是JavaScript中的重要内容，异步的主要作用是把耗时间的代码“放一边”，让其不阻塞同步代码，等到异步代码出结果了，再通过回调函数来处理其结果。但是在实际工作中使用异步的时候有一个重要的问题，即多个异步代码的顺序问题。</p>
<p>假如我们要做多个Ajax请求，第二个请求的参数是一个请求的结果，这就要求异步代码之间需要有序，保证第二个请求在第一个请求执行完之后再执行。其实细考虑起来这是个略显诡异的需求，也就是使异步代码“同步化”。不过ES6的许多新特性使得这一操作变得更为简化。我们可以用Promise，Generator，或async/await分别实现上述“同步化异步代码”的需求。三者对照，可以更好地将ES6中的异步理解。</p>
<p>话不多说，上需求。首先模拟一个取数据的异步操作，返回的数据类型是Promise（比较典型的用法），代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params">params</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-comment">// 模拟ajax</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">"result: "</span> + params);
    &#125;, <span class="hljs-number">500</span>);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的需求是，先用getData取到数据，再对取到的数据进行作一次getData，两次操作需要有序，不然第二次的参数就空了。------以上是实习面试腾讯时的一道题，当时初涉前端，连题都没搞懂😭。</p>
<p>后面将用三种方法实现这个需求，领略ES6异步三境界。</p>
<h2 data-id="heading-1">一重境界：用Promise使异步代码有序</h2>
<p>Promise是为异步而生的，用.then可以大大缓解以前“回调地狱”的情况。直接上代码，详情见注释。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">getData(<span class="hljs-string">"start"</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-comment">// 取到结果 result: start</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage1"</span>, res);
    getData(res).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      <span class="hljs-comment">// 取到结果 result: result: start</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage2"</span>, res);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"all Done!!"</span>);
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">stage1 result: start
stage2 result: result: start
all Done!!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所见，简单易懂，但是多次异步写起来还是有点难受，“回调地狱”的问题没有彻底解决。不过没关系，后面还有新办法。</p>
<h2 data-id="heading-2">二重境界：用async/await简化Promise</h2>
<p>其实async/await可以算是上述问题的最终形态，本来应该放在最后说的，但相比Generator而言，async/await更好简洁，也更常用，于是便放在第二重了，毕竟Generator理解起来确实有点费劲。</p>
<p>async/await两兄弟，一个一个来介绍。</p>
<p>async：放于某函数function关键字之前时，可以将该函数的返回包裹上一个成一个fulfilled状态的Promise对象。看代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;

get1(); <span class="hljs-comment">// 返回结果为Promise &#123;<fulfilled>: 1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>await：你async能包一个promise，我await就能解开一个promise😊。上面代码别删，接着用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> get1(); <span class="hljs-comment">// 结果为 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两兄弟最简单的功能是对立的，但二者结合起来却能轻松地完成“异步代码同步化”的问题。先上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// async/await 写法,</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asy_fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// get到数据之前，下行代码下面的其他代码都得等着（wait）</span>
  <span class="hljs-keyword">let</span> stage1 = <span class="hljs-keyword">await</span> getData(<span class="hljs-string">"start"</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage1"</span>, stage1);
  <span class="hljs-keyword">let</span> stage2 = <span class="hljs-keyword">await</span> getData(stage1);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage2"</span>, stage2);
  <span class="hljs-keyword">return</span> <span class="hljs-string">"all Done!!"</span>;
&#125;

<span class="hljs-keyword">let</span> res_asy = asy_fn();
<span class="hljs-comment">// 因为返回值是Promise，所以最后的结果要then一下再打出来</span>
res_asy.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面讲点细节：</p>
<ol>
<li>await只能在async function中起到上面的作用，而且await右边函数的返回值得是promise，setTimeout造成的异步await无效。</li>
<li>await暂停代码时，其左边的赋值也是未进行的，实际上是停在了await右边的函数里。</li>
<li>因为await产生的异步效应是和promise同级别的，也就是微任务级别。具体细节可见<a href="https://juejin.cn/post/6989252270516863006" target="_blank" title="https://juejin.cn/post/6989252270516863006">《反复横跳的await与Promise优先级》</a>。</li>
</ol>
<h2 data-id="heading-3">三重境界：用Generator和Promise解构async/await</h2>
<p>Generator（生成器or迭代器？）是个陌生的家伙，一般业务中用到的比较少（写出来同事看不懂咋办😂），但是他是async/await背后的原理。而且若是能灵活掌握这个知识点的话，可以造出很多东西。本文就把这个当作最后boss了，用这个来理解async/await。</p>
<p>先简述，Generator，通过function*这样的函数声明方式产生一个迭代器函数，执行一下迭代器就产生<strong>一个迭代器对象</strong>。这个函数里的yield和return是一个个节点，在迭代器上next一下就从一个节点执行到下一个节点。就是会停止，对了，这就是await会停在某行代码上的原理😏。</p>
<p>show me your code，示例如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gene</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-keyword">let</span> g = gene(); <span class="hljs-comment">// 生成一个迭代器对象</span>
<span class="hljs-built_in">console</span>.log(g.next());
<span class="hljs-comment">// &#123; value: 1, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(g.next());
<span class="hljs-comment">// &#123; value: 2, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(g.next());
<span class="hljs-comment">// &#123; value: 3, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>next()产生的结果是&#123;value, done&#125;，这个对象里的值value是yield<strong>右侧的值或函数返回值</strong>，done是布尔值，迭代器是否执行完，即<strong>后面是否有其他的yield或return语句</strong>。</p>
<p>感觉next方法差不多整明白了，其实并没有😏。next函数其实可以传参数，next函数的参数即为上一个yield表达式的返回值（有点绕）。示例如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gene</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> n1 = <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-built_in">console</span>.log(n1);
  <span class="hljs-keyword">let</span> n2 = <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>; 
  <span class="hljs-built_in">console</span>.log(n2);
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-keyword">let</span> g = gene();
<span class="hljs-built_in">console</span>.log(g.next());
<span class="hljs-built_in">console</span>.log(g.next(<span class="hljs-string">"res for yield 1"</span>));
<span class="hljs-comment">// yield 函数返回值是下一个next运行时的输入值，</span>
<span class="hljs-comment">// 每次.next都执行到yield及后面的部分为止，</span>
<span class="hljs-comment">// 前面的赋值和yield本身都不返回值</span>
<span class="hljs-built_in">console</span>.log(g.next(<span class="hljs-string">"res for yield 2"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有点难理解，毕竟在下面执行的next里的函数跑到上面去了。但我们把每个next当作独立函数的话会更好理解。在执行到第二个next时，执行的代码其实是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// console.log(g.next("res for yield 1"));</span>
<span class="hljs-comment">// 相当于</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">param</span>) </span>&#123;
  <span class="hljs-keyword">let</span> n1 = param;
  <span class="hljs-built_in">console</span>.log(n1);
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以块为单位来理解yeild返回值便会比较清晰。</p>
<p>科普完毕，圆规正转，如何用<strong>Generator实现“异步代码同步化”</strong>。上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> stage1 = <span class="hljs-keyword">yield</span> getData(<span class="hljs-string">"start"</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage1"</span>, stage1);
  <span class="hljs-keyword">let</span> stage2 = <span class="hljs-keyword">yield</span> getData(stage1);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage2"</span>, stage2);
  <span class="hljs-keyword">return</span> <span class="hljs-string">"all Done!!"</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">generator, v</span>) </span>&#123;
  <span class="hljs-keyword">let</span> &#123; value, done &#125; = generator.next(v);
  <span class="hljs-keyword">if</span> (!done) &#123;
    value.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      run(generator, res);
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(value);
  &#125;
&#125;

<span class="hljs-keyword">let</span> res = run(gen());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先实现一个gen迭代器，生成一个迭代器实例放在run里自动化地跑，毕竟一个一个地写next也太二了。</p>
<p>发现没有，现在的用生成器实现方式已经很接近async/await的实现方式了，不过async函数返回的是promise，run返回的是字符串。稍作改变就可以达到相同的效果。所以下面代码就是“如何用Generator和Promise模拟async/await？”，即标题<strong>async/await = Promise + Generator</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params">stage0</span>) </span>&#123;
  <span class="hljs-keyword">let</span> stage1 = <span class="hljs-keyword">yield</span> getData(<span class="hljs-string">"start"</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage1"</span>, stage1);
  <span class="hljs-keyword">let</span> stage2 = <span class="hljs-keyword">yield</span> getData(stage1);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"stage2"</span>, stage2);
  <span class="hljs-keyword">return</span> <span class="hljs-string">"all Done!!"</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">generator, v</span>) </span>&#123;
  <span class="hljs-keyword">let</span> &#123; value, done &#125; = generator.next(v);
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span> (<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123; <span class="hljs-comment">// 包个promise</span>
    <span class="hljs-keyword">if</span> (!done) &#123;
        value.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> run(generator, res).then(resolve);
        &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> resolve(value); <span class="hljs-comment">// gen函数return时的处理</span>
    &#125;
  &#125;);
&#125;

<span class="hljs-keyword">let</span> res = run(gen());
res.then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码可与二重境界中代码等价，这便是async/await背后的实现原理了。于是就有了这种说法。</p>
<blockquote>
<p>async/await是一个promise+generator+run函数的语法糖。</p>
</blockquote>
<h2 data-id="heading-4">后记</h2>
<p>ES6异步Generator使用较少，但这又是理解async/await的关键一步，填上这个空缺，认知才够完整。</p></div>  
</div>
            