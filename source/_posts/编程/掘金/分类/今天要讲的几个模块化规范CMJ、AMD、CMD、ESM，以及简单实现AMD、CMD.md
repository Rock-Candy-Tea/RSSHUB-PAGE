
---
title: '今天要讲的几个模块化规范CMJ、AMD、CMD、ESM，以及简单实现AMD、CMD'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4419'
author: 掘金
comments: false
date: Mon, 31 May 2021 22:23:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4419'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">CMJ（CommonJS规范）</h2>
<p>谈到CMJ我们很容易想到node.js因为node所使用的模块化规范正是CMJ,侧面说明了CMJ是一个适用与服务器的模块化规范。
CMJ有几个主要方法分别为：module、exports、require、global。 在开发中我们用module.exports 来导出模块，用 require来加载模块。
我们来看个简单的用例：
math.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//在math.js中，我们定义了一个变量和一个函数并把它暴露出来</span>
<span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-built_in">module</span>.exports = &#123; <span class="hljs-comment">//在这向外暴露出函数与变量</span>
  <span class="hljs-attr">add</span>: add,
  <span class="hljs-attr">num</span>: num
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//我们在这里使用require方法引用math.js</span>
<span class="hljs-keyword">let</span> math = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./math'</span>);
<span class="hljs-comment">//这时我们可以调用到math中的add方法。</span>
math.add(<span class="hljs-number">4</span>, <span class="hljs-number">9</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里要注意的是引用自定义的模块时，参数包含路径，可省略.js,而引用核心模块时，不需要带路径。
因为CommonJS用同步的方式加载模块。在浏览器中我们用同步方式加载模块时用户将无法继续操作网页，所以前端需要一个能异步加载模块的模块化规范。</p>
<p>文件是一个模块，私有。内置两个变量 module require (exports = module.exports)</p>
<p>一个引入一个导出，就构成了通信的基本结构</p>
<h3 data-id="heading-1">需要注意的两个问题</h3>
<ol>
<li>缓存，require 会缓存一下，所以</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'morrain'</span>
<span class="hljs-keyword">var</span> age = <span class="hljs-number">18</span>
<span class="hljs-built_in">exports</span>.name = name
<span class="hljs-built_in">exports</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> age
&#125;
<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'a.js'</span>)
<span class="hljs-built_in">console</span>.log(a.name) <span class="hljs-comment">// 'morrain'</span>
a.name = <span class="hljs-string">'rename'</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-built_in">require</span>(<span class="hljs-string">'a.js'</span>)
<span class="hljs-built_in">console</span>.log(b.name) <span class="hljs-comment">// 'rename'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>引用拷贝还是值拷贝的问题(CMJ 是值拷贝)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'morrain'</span>
<span class="hljs-keyword">var</span> age = <span class="hljs-number">18</span>
<span class="hljs-built_in">exports</span>.name = name
<span class="hljs-built_in">exports</span>.age = age
<span class="hljs-built_in">exports</span>.setAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>)</span>&#123;
    age = a
&#125;
<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'a.js'</span>)
<span class="hljs-built_in">console</span>.log(a.age) <span class="hljs-comment">// 18</span>
a.setAge(<span class="hljs-number">19</span>)
<span class="hljs-built_in">console</span>.log(a.age) <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>运行时加载 / 编译时加载（多阶段，异步）ESM</li>
</ol>
<h2 data-id="heading-2">AMD</h2>
<p>AMD就是一个异步加载模块的模块化规范。AMD的实现就是require.js
AMD规范定义了一个函数define，通过define方法定义模块</p>
<pre><code class="hljs language-js copyable" lang="js">define(id?, dependencies?, factory);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>id：可选参数，用来定义模块的标识，如果没有提供该参数，模块标识就取脚本文件名（去掉扩展名）。</li>
<li>dependencies：可选参数，用来传入当前模块依赖的模块名称数组。</li>
<li>factory：工厂方法，模块初始化要执行的函数或对象，如果是函数，它只被执行一次。如果是对象，此对象应该为模块的输出值。定义模块例子：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">define(<span class="hljs-string">'a'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a load'</span>)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a run'</span>) &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在require.js 中还有require.config和require，我们以加载一个jquery库为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>.config(&#123;
    <span class="hljs-attr">paths</span> : &#123;
        <span class="hljs-string">"jquery"</span> : [<span class="hljs-string">"http://libs.baidu.com/jquery/2.0.3/jquery"</span>]   
    &#125;
&#125;)
<span class="hljs-comment">//这时做完上面的操作后我们就可以直接用jquery来引入模块，不用后面那一大串CDN地址了</span>
<span class="hljs-built_in">require</span>([<span class="hljs-string">"jquery"</span>],<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>)</span>&#123;
    $(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        alert(<span class="hljs-string">"load finished"</span>);  
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>依赖前置</strong>，换句话说，在解析和执行当前模块之前，模块作者必须指明当前模块所依赖的模块。</p>
<p>代码在一旦运行到此处，能立即知晓依赖。而无需遍历整个函数体找到它的依赖，因此性能有所提升，缺点就是开发者必须显式得指明依赖——这会使得开发工作量变大，比如：当你写到函数体内部几百上千行的时候，忽然发现需要增加一个依赖，你不得不回到函数顶端来将这个依赖添加进数组。</p>
<pre><code class="hljs language-js copyable" lang="js">define(<span class="hljs-string">'a'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a load'</span>)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a run'</span>) &#125;
  &#125;
&#125;)

define(<span class="hljs-string">'b'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b load'</span>)
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b run'</span>) &#125;
  &#125;
&#125;)

<span class="hljs-built_in">require</span>([<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'main run'</span>) 
  a.run()
  b.run()
&#125;)

<span class="hljs-comment">// a load</span>
<span class="hljs-comment">// b load</span>
<span class="hljs-comment">// main run</span>
<span class="hljs-comment">// a run</span>
<span class="hljs-comment">// b run</span>
<span class="hljs-comment">//从这个打印结果我们可以看出，ADM在require时就把所有模块都加载了并没有管你有没有用到他，这就是依赖前置。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">简单实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> def = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-comment">// AMD mini impl</span>
<span class="hljs-keyword">const</span> defaultOptions = &#123;
  <span class="hljs-attr">paths</span>: <span class="hljs-string">''</span>
&#125;

<span class="hljs-comment">// From CDN 加载CDN （System 加载库）</span>
<span class="hljs-keyword">const</span> __import = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resove, reject</span>) =></span> &#123;
    System.import(url).then(resove, reject)
  &#125;)
&#125;

<span class="hljs-comment">// normal script 读取路径</span>
<span class="hljs-keyword">const</span> __load = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> head = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'head'</span>)[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
    node.type = <span class="hljs-string">'text/javascript'</span>;
    node.src = url;
    node.async = <span class="hljs-literal">true</span>;
    node.onload = resolve;
    node.onerror = reject;
    head.appendChild(node)
  &#125;)
&#125;

<span class="hljs-comment">// 为啥没写 let const var</span>
<span class="hljs-comment">// 千万不要在实际使用这种比较 low 的方式 🔥</span>
rj = &#123;&#125;;

rj.config = <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> <span class="hljs-built_in">Object</span>.assign(defaultOptions, options);

<span class="hljs-comment">// 定义模块，触发的时机其实是在 require 的时候，所以 -> 收集</span>
define = <span class="hljs-function">(<span class="hljs-params">name, deps, factory</span>) =></span> &#123;
  <span class="hljs-comment">// todo 参数的判断，互换</span>
  def.set(name, &#123; name, deps, factory &#125;);
&#125;

<span class="hljs-comment">// dep -> a -> a.js -> 'http:xxxx/xx/xx/a.js';</span>
<span class="hljs-keyword">const</span> __getUrl = <span class="hljs-function">(<span class="hljs-params">dep</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> p = location.pathname;
  <span class="hljs-keyword">return</span> p.slice(<span class="hljs-number">0</span>, p.lastIndexOf(<span class="hljs-string">'/'</span>)) + <span class="hljs-string">'/'</span> + dep + <span class="hljs-string">'.js'</span>;
&#125;

<span class="hljs-comment">// 其实才是触发加载依赖的地方</span>
<span class="hljs-built_in">require</span> = <span class="hljs-function">(<span class="hljs-params">deps, factory</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">Promise</span>.all(deps.map(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> &#123;
      <span class="hljs-comment">// 走 CDN</span>
      <span class="hljs-keyword">if</span> (defaultOptions.paths[dep]) <span class="hljs-keyword">return</span> __import(defaultOptions.paths[dep]);

      <span class="hljs-keyword">return</span> __load(__getUrl(dep)).then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123; deps, factory &#125; = def.get(dep);
        <span class="hljs-keyword">if</span> (deps.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> factory(<span class="hljs-literal">null</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">require</span>(deps, factory)
      &#125;)
    &#125;)).then(resolve, reject)
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-params">instances</span> =></span> factory(...instances))
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">CMD</h3>
<p>代表技术实现 Seajs
CMD例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//function有三个参数：require参数用来引入别的模块，exports和module用来导出模块公共接口。</span>
define(<span class="hljs-string">'a'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a load'</span>)
  <span class="hljs-built_in">exports</span>.run = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a run'</span>) &#125;
&#125;)

define(<span class="hljs-string">'b'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b load'</span>)
  <span class="hljs-built_in">exports</span>.run = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b run'</span>) &#125;
&#125;)

define(<span class="hljs-string">'main'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'main run'</span>)
  <span class="hljs-keyword">var</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'a'</span>)
  a.run()
  <span class="hljs-keyword">var</span> b = <span class="hljs-built_in">require</span>(<span class="hljs-string">'b'</span>)
  b.run()
&#125;)

seajs.use(<span class="hljs-string">'main'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到我们的依赖是用require<strong>按需要来引入</strong>的。这就是<strong>依赖后置</strong>。而且我们需要调用seajs.use()方法来执行这个模块。</p>
<h3 data-id="heading-5">简单实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> modules = &#123;&#125;;
<span class="hljs-keyword">const</span> <span class="hljs-built_in">exports</span> = &#123;&#125;;
sj = &#123;&#125;;

<span class="hljs-keyword">const</span> toUrl = <span class="hljs-function">(<span class="hljs-params">dep</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> p = location.pathname;
  <span class="hljs-keyword">return</span> p.slice(<span class="hljs-number">0</span>, p.lastIndexOf(<span class="hljs-string">'/'</span>)) + <span class="hljs-string">'/'</span> + dep + <span class="hljs-string">'.js'</span>;
&#125;

<span class="hljs-keyword">const</span> getDepsFromFn = <span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> matches = [];
  <span class="hljs-comment">// require('a ')</span>
  <span class="hljs-comment">//1. (?:require\() -> require(  -> (?:) 非捕获性分组</span>
  <span class="hljs-comment">//2. (?:['"]) -> require('</span>
  <span class="hljs-comment">//3. ([^'"]+) -> a -> 避免回溯 -> 回溯 状态机</span>
  <span class="hljs-keyword">let</span> reg = <span class="hljs-regexp">/(?:require\()(?:['"])([^'"]+)/g</span>; <span class="hljs-comment">// todo</span>
  <span class="hljs-keyword">let</span> r = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">while</span>((r = reg.exec(fn.toString())) !== <span class="hljs-literal">null</span>) &#123;
    reg.lastIndex
    matches.push(r[<span class="hljs-number">1</span>])
  &#125;

  <span class="hljs-keyword">return</span> matches
&#125;

<span class="hljs-keyword">const</span> __load = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> head = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'head'</span>)[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
    node.type = <span class="hljs-string">'text/javascript'</span>;
    node.src = url;
    node.async = <span class="hljs-literal">true</span>;
    node.onload = resolve;
    node.onerror = reject;
    head.appendChild(node)
  &#125;)
&#125;

<span class="hljs-comment">// 依赖呢？</span>
<span class="hljs-comment">// 提取依赖： 1. 正则表达式 2. 状态机</span>
define = <span class="hljs-function">(<span class="hljs-params">id, factory</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> url = toUrl(id);
  <span class="hljs-keyword">const</span> deps = getDepsFromFn(factory);
  <span class="hljs-keyword">if</span> (!modules[id]) &#123;
    modules[id] = &#123; url, id, factory, deps &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> __exports = <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> <span class="hljs-built_in">exports</span>[id] || (<span class="hljs-built_in">exports</span>[id] = &#123;&#125;);
<span class="hljs-keyword">const</span> __module = <span class="hljs-built_in">this</span>;
<span class="hljs-comment">// 这里面才是加载模块的地方</span>
<span class="hljs-keyword">const</span> __require = <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> __load(toUrl(id)).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 加载之后</span>
    <span class="hljs-keyword">const</span> &#123; factory, deps &#125; = modules[id];
    <span class="hljs-keyword">if</span> (!deps || deps.length === <span class="hljs-number">0</span>) &#123;
      factory(__require, __exports(id), __module);
      <span class="hljs-keyword">return</span> __exports(id);
    &#125;

    <span class="hljs-keyword">return</span> sj.use(deps, factory);
  &#125;)
&#125;

sj.use = <span class="hljs-function">(<span class="hljs-params">mods, callback</span>) =></span> &#123;
  mods = <span class="hljs-built_in">Array</span>.isArray(mods) ? mods : [mods];
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">Promise</span>.all(mods.map(<span class="hljs-function"><span class="hljs-params">mod</span> =></span> &#123;
      <span class="hljs-keyword">return</span> __load(toUrl(mod)).then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> &#123; factory &#125; = modules[mod];
        <span class="hljs-keyword">return</span> factory(__require, __exports(mod), __module)
      &#125;)
    &#125;)).then(resolve, reject)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">instances</span> =></span> callback && callback(...instances))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">补充</h2>
<p>有时候遇到递归调用，总是觉得非常绕，这时候我们可以试着拆开来看待，把它假设成为一个最基础简单的单过程</p>
<p>假设 模块 A 依赖 模块 B , 模块 B 则 无需依赖</p>
<p>我们简化下模型</p>
<p>假设只加载模块 B</p>
<p>定义 B 模块</p>
<pre><code class="hljs language-js copyable" lang="js">define(<span class="hljs-string">'B'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B load'</span>)
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B run'</span>) &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 模块 B</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>([<span class="hljs-string">"B"</span>],<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">B</span>)</span>&#123;
    B.run()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span> = <span class="hljs-function">(<span class="hljs-params">deps, factory</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
       <span class="hljs-comment">// 循环调用依赖</span>
      <span class="hljs-built_in">Promise</span>.all(deps.map(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> &#123;
        <span class="hljs-comment">// 走 CDN</span>
        <span class="hljs-keyword">if</span> (defaultOptions.paths[dep]) <span class="hljs-keyword">return</span> __import(defaultOptions.paths[dep]);
        <span class="hljs-comment">// 本地引用</span>
        <span class="hljs-keyword">return</span> __load(__getUrl(dep)).then(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">const</span> &#123; deps, factory &#125; = def.get(dep); <span class="hljs-comment">// 获取 define 时存储的 B 模块</span>
          <span class="hljs-keyword">return</span> factory(<span class="hljs-literal">null</span>); <span class="hljs-comment">// 执行 B 模块， 返回 B 模块 return 结果</span>
        &#125;)
      &#125;)).then(resolve, reject) <span class="hljs-comment">// 将 ↑ 执行结果放回 resolve 的值为 Promise.all 执行完成后的 factory 范围值 数组</span>
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">instances</span> =></span> factory(...instances)) <span class="hljs-comment">// 返回结果 执行 require 的 回调函数 factory</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 A 模块存在引用 B 模块时</p>
<p>定义 A 模块</p>
<pre><code class="hljs language-js copyable" lang="js">define(<span class="hljs-string">'A'</span>, [<span class="hljs-string">'B'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">B</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'A load'</span>)
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">run</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; B.run() &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 模块 A 时则要去检测 A 模块需要依赖的模块，当假设每个模块都有自己的依赖时，这个过程就像是一个树状图，不断地调用 各自的 require，每个树节点都去加载自己节点分支模块，符合递归调用的条件。</p>
<p>递归调用需要一个执行条件，条件就是该模块是否需要依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> __load(__getUrl(dep)).then(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> &#123; deps, factory &#125; = def.get(dep); <span class="hljs-comment">// 取出 模块 检查 是否需要依赖</span>
    <span class="hljs-keyword">if</span> (deps.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> factory(<span class="hljs-literal">null</span>); <span class="hljs-comment">// 当依赖长度部位0时</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">require</span>(deps, factory) <span class="hljs-comment">// 否则 加载 自身依赖</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            