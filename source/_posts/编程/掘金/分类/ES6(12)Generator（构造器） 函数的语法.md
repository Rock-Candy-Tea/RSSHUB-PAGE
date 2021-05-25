
---
title: 'ES6(12)Generator（构造器） 函数的语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5898'
author: 掘金
comments: false
date: Tue, 25 May 2021 02:36:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=5898'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">基本概念：异步编程解决方案</h2>
<p><code>Generator </code>函数是 <code>ES6 </code>提供的一种<code>异步编程解决方案</code>，语法行为与传统函数<code>完全不同</code>。</p>
<h3 data-id="heading-1">1、语法上：<code>Generator</code> 函数是一个<code>状态机</code>，封装了多个内部状态</h3>
<h4 data-id="heading-2">执行 Generator 函数会返回一个遍历器对象</h4>
<h4 data-id="heading-3">Generator 函数除了状态机，还是一个遍历器对象生成函数</h4>
<blockquote>
<p>执行 <code>Generator</code> 函数会<code>返回一个遍历器对象</code>，也就是说，<code>Generator</code> 函数<code>除了状态机</code>，还<code>是一个遍历器对象生成函数</code>。返回的遍历器对象，可以依次遍历 <code>Generator</code> 函数内部的每一个状态。</p>
</blockquote>
<h3 data-id="heading-4">2、形式上：<code>Generator</code> 函数是一个普通函数，但是有两个特征</h3>
<h4 data-id="heading-5">（1）function关键字与函数名之间有一个<code>星号</code>；</h4>
<h4 data-id="heading-6">（2）函数体内部使用<code>yield</code>表达式，定义不同的内部状态（<code>yield</code>在英语里的意思就是<code>“产出”</code>）</h4>
<h3 data-id="heading-7">3、调用 <code>Generator</code> 函数后：<code>必须调用</code>遍历器对象的<code>next方法</code>，使得指针移向下一个状态</h3>
<blockquote>
<p>该<code>函数并不执行</code>，返回的也<code>不是函数运行结果</code>，而<code>是一个指向内部状态的指针对象</code>，也就是上一章介绍的<code>遍历器对象</code>（Iterator Object）。</p>
</blockquote>
<h4 data-id="heading-8">（1）每次调用<code>next</code>方法，内部指针就从函数头部或上一次停下来的地方开始执行，直到遇到下一个<code>yield</code>表达式（或<code>return</code>语句）为止</h4>
<h4 data-id="heading-9">（2）Generator 函数是分段执行的，yield表达式是暂停执行的标记，而next方法可以恢复执行</h4>
<blockquote>
<p>下一步，必须调用遍历器对象的<code>next</code>方法，使得指针移向下一个状态。也就是说，每次调用<code>next</code>方法，内部指针就从函数头部或上一次停下来的地方开始执行，直到遇到下一个<code>yield</code>表达式（或<code>return</code>语句）为止。换言之，<code>Generator 函数是分段执行的</code>，<code>yield</code>表达式是<code>暂停执行的标记</code>，而<code>next方法可以恢复执行</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">aaa</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'hello'</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'world'</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'ending'</span>;
&#125;

<span class="hljs-keyword">var</span> hw=aaa();
<span class="hljs-built_in">console</span>.log(aaa);
<span class="hljs-comment">//[GeneratorFunction: aaa]</span>

<span class="hljs-built_in">console</span>.log(hw);
<span class="hljs-comment">//Object [Generator] &#123;&#125;</span>

<span class="hljs-built_in">console</span>.log(hw.next());
<span class="hljs-comment">// &#123; value: 'hello', done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(hw.next());
<span class="hljs-comment">// &#123; value: 'world', done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(hw.next());
<span class="hljs-comment">// &#123; value: 'ending', done: true &#125;</span>

<span class="hljs-built_in">console</span>.log(hw.next());
<span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上边的函数有三个状态：<code>hello</code>，<code>world </code>和 <code>return</code> 语句（结束执行）。</p>
<h4 data-id="heading-10">（3）<code>next</code>方法返回一个对象，它的<code>value</code>属性就是当前<code>yield</code>表达式的值，<code>done</code>属性的值表示遍历还没有结束</h4>
<h4 data-id="heading-11">（4）一直执行到<code>return语句</code>（如果<code>没有return语句</code>，就执行<code>到函数结束</code>）</h4>
<h4 data-id="heading-12">（5）<code>next</code>方法返回的对象的<code>value属性</code>，就是紧跟<code>在return语句后面</code>的表达式的值（如果<code>没有return</code>语句，则<code>value</code>属性的值<code>为undefined</code>）</h4>
<h4 data-id="heading-13">（6）<code>done</code>属性的值<code>为true</code>，表示遍历已经结束</h4>
<h3 data-id="heading-14">4、没有规定function关键字与函数名之间的星号，写在哪个位置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//都可以</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> * <span class="hljs-title">foo</span>(<span class="hljs-params">x, y</span>) </span>&#123; ··· &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">foo</span>(<span class="hljs-params">x, y</span>) </span>&#123; ··· &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params">x, y</span>) </span>&#123; ··· &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>*<span class="hljs-title">foo</span>(<span class="hljs-params">x, y</span>) </span>&#123; ··· &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">yield 表达式</h2>
<p>由于 <code>Generator </code>函数返回的遍历器对象，只有调用<code>next</code>方法才会遍历下一个内部状态，所以<code>其实提供了一种可以暂停执行的函数</code>。</p>
<h3 data-id="heading-16">yield表达式就是暂停标志</h3>
<h3 data-id="heading-17">遍历器对象的next方法的运行逻辑</h3>
<h4 data-id="heading-18">（1）遇到<code>yield</code>表达式，就<code>暂停执行后面的操作</code>，并将紧跟在<code>yield</code>后面的那个表达式的值，作为返回的对象的<code>value</code>属性值</h4>
<h4 data-id="heading-19">（2）下一次调用<code>next</code>方法时，再继续往下执行，直到<code>遇到下一个yield</code>表达式</h4>
<h4 data-id="heading-20">（3）如果<code>没有</code>再遇到<code>新的yield</code>表达式，就<code>一直运行到函数结束</code>，直到<code>return</code>语句为止，并将<code>return</code>语句后面的表达式的值，作为返回的对象的<code>value</code>属性值</h4>
<h4 data-id="heading-21">（4）如果该函数<code>没有return</code>语句，则返回的对象的<code>value属性值为undefined</code></h4>
<h4 data-id="heading-22">（5）<code>yield</code>表达式<code>后面的表达式</code>，只有当调用<code>next</code>方法、内部指针指向该语句时<code>才会执行</code>，因此等于为<code>JavaScript</code>提供了手动的<code>“惰性求值”</code>（Lazy Evaluation）的语法功能</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span>  <span class="hljs-number">123</span> + <span class="hljs-number">456</span>;
&#125;
<span class="hljs-comment">//yield后面的表达式123 + 456，不会立即求值，只会在next方法将指针移到这一句时，才会求值。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">yield表达式与return语句</h3>
<p>既有相似之处，也有区别。</p>
<h4 data-id="heading-24"><code>相似之处在于</code>：都能返回紧跟在语句后面的那个表达式的值</h4>
<h4 data-id="heading-25"><code>区别在于</code>：每次遇到<code>yield</code>，函数暂停执行，下一次再从该位置继续向后执行，而<code>return</code>语句不具备位置记忆的功能</h4>
<h4 data-id="heading-26">一个函数里面，只能执行<code>一次（或者说一个）return</code>语句，但是可以执行<code>多次（或者说多个）yield</code>表达式</h4>
<h3 data-id="heading-27">Generator 函数不用yield表达式,就变成了一个单纯的暂缓执行函数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了！'</span>)
&#125;

<span class="hljs-keyword">var</span> generator = f();

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  generator.next()
&#125;, <span class="hljs-number">2000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">yield表达式只能用在 Generator 函数里面</h3>
<p>用在其他地方都会报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
&#125;)()
<span class="hljs-comment">// SyntaxError: Unexpected number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">yield表达式如果用在另一个表达式之中，必须放在圆括号里面</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">demo</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">//console.log('Hello' + yield); // SyntaxError</span>
<span class="hljs-comment">//console.log('Hello' + yield 123); // SyntaxError</span>
    
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello'</span> + (<span class="hljs-keyword">yield</span>)); <span class="hljs-comment">// OK</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello'</span> + (<span class="hljs-keyword">yield</span> <span class="hljs-number">123</span>)); <span class="hljs-comment">// OK</span>
&#125;

<span class="hljs-keyword">var</span> a=demo();
<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//&#123; value: undefined, done: false &#125;</span>
<span class="hljs-comment">//Helloundefined</span>

<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//&#123; value: 123, done: false &#125;</span>
<span class="hljs-comment">//Helloundefined</span>

<span class="hljs-built_in">console</span>.log(a.next());<span class="hljs-comment">//&#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">yield表达式用作函数参数或放在赋值表达式的右边，可以不加括号</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> foo=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
    <span class="hljs-built_in">console</span>.log(b);
&#125;
<span class="hljs-comment">//demo 有 三个yield 所以 需要四次next  done才等于true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">demo</span>(<span class="hljs-params"></span>) </span>&#123;
    foo(<span class="hljs-keyword">yield</span> <span class="hljs-string">'a'</span>, <span class="hljs-keyword">yield</span> <span class="hljs-string">'b'</span>); <span class="hljs-comment">// OK</span>
    <span class="hljs-keyword">let</span> input = <span class="hljs-keyword">yield</span>; <span class="hljs-comment">// OK</span>
    <span class="hljs-built_in">console</span>.log(input);
&#125;

<span class="hljs-keyword">var</span> a=demo();
<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//&#123; value: 'a', done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//&#123; value: 'b', done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//这一步foo才执行 </span>
<span class="hljs-comment">//undefined</span>
                        <span class="hljs-comment">// undefined</span>
                        <span class="hljs-comment">// &#123; value: undefined, done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">//undefined</span>
                        <span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">与 Iterator 接口的关系</h3>
<h4 data-id="heading-32">1、任意一个对象的<code>Symbol.iterator</code>方法，<code>等于</code>该对象的<code>遍历器生成函数</code>，调用该函数会<code>返回</code>该对象的<code>一个遍历器对象</code></h4>
<h4 data-id="heading-33">2、由于<code>Generator</code> 函数<code>就是遍历器生成函数</code>，因此可以把 <code>Generator </code>赋值给对象的<code>Symbol.iterator</code>属性，从而<code>使</code>得<code>该对象具有 Iterator 接口</code></h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> myIterable = &#123;&#125;;
myIterable[<span class="hljs-built_in">Symbol</span>.iterator] = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;;

[...myIterable] <span class="hljs-comment">// [1, 2, 3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">3、<code>Generator</code> 函数执行后，返回一个遍历器对象。该对象本身也具有<code>Symbol.iterator</code>属性，<code>Symbol.iterator</code>属性执行后<code>返回自身</code></h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;

<span class="hljs-keyword">var</span> g = gen();

g[<span class="hljs-built_in">Symbol</span>.iterator]() === g
<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">next 方法的参数</h3>
<h4 data-id="heading-36">1、<code>yield表达式本身没有返回值，或者说总是返回undefined</code>(这就是为什么被赋值yield的变量都是 undefined的原因)</h4>
<h4 data-id="heading-37">2、上一个yield下边（下一行，不是紧跟在yield的代码）的代码只有在下一个next后才会执行</h4>
<h4 data-id="heading-38">3、<code>next</code>方法可以带一个参数，该参数就会被当作<code>上一个yield</code>表达式的<code>返回值</code>（把上一次的yield和紧跟yield的语句更改为next 的参数）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; <span class="hljs-literal">true</span>; i++) &#123;
        <span class="hljs-keyword">var</span> reset = <span class="hljs-keyword">yield</span> i;
        <span class="hljs-built_in">console</span>.log(reset);
        <span class="hljs-keyword">if</span>(reset) &#123; i = -<span class="hljs-number">1</span>; &#125;
    &#125;
&#125;

<span class="hljs-keyword">var</span> g = f();

<span class="hljs-built_in">console</span>.log(g.next());  <span class="hljs-comment">// &#123; value: 0, done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(g.next());  <span class="hljs-comment">//undefined</span>
                        <span class="hljs-comment">// &#123; value: 1, done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(g.next());  <span class="hljs-comment">//undefined</span>
                        <span class="hljs-comment">// &#123; value: 2, done: false &#125;</span>

<span class="hljs-built_in">console</span>.log(g.next(<span class="hljs-literal">true</span>));    <span class="hljs-comment">// true</span>
                              <span class="hljs-comment">//&#123; value: 0, done: false &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>next</code>方法没有参数，每次运行到<code>yield</code>表达式，变量<code>reset</code>的值总是<code>undefined</code>。</p>
<p>当<code>next</code>方法带一个参数<code>true</code>时，变量<code>reset</code>就被重置为这个参数（即<code>true</code>），因此i会等于<code>-1</code>，下一轮循环就会从<code>-1</code>开始递增变为<code>0</code>。</p>
<h4 data-id="heading-39">通过<code>next</code>方法的参数 在不同阶段入不同值</h4>
<h5 data-id="heading-40">1、<code>Generator </code>函数从暂停状态到恢复运行，它的上下文状态（<code>context</code>）是不变的</h5>
<h5 data-id="heading-41">2、通过<code>next</code>方法的参数，就有办法在 <code>Generator</code> 函数开始运行之后，<code>继续向函数体内部注入值</code></h5>
<p>也就是说，可以在<code>Generator</code>函数运行的<code>不同阶段</code>，从外部向内部<code>注入不同的值</code>，从而<code>调整函数行为</code>。</p>
<h5 data-id="heading-42">3、由于<code>next</code>方法的参数表示上一个yield表达式的返回值，所以在<code>第一次使用next方法时，传递参数是无效的</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-keyword">var</span> y = <span class="hljs-number">2</span> * (<span class="hljs-keyword">yield</span> (x + <span class="hljs-number">1</span>));
    <span class="hljs-keyword">var</span> z = <span class="hljs-keyword">yield</span> (y / <span class="hljs-number">3</span>);
    <span class="hljs-keyword">return</span> (x + y + z);
&#125;

<span class="hljs-keyword">var</span> a = foo(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">// Object&#123;value:6, done:false&#125;  只执行到了var y； y=undefined</span>
<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">// Object&#123;value:NaN, done:false&#125;    只执行到了var z；相当于 z=undefined/3=NaN</span>
<span class="hljs-built_in">console</span>.log(a.next());  <span class="hljs-comment">// Object&#123;value:NaN, done:true&#125;    相当于  5+NaN+undefined</span>

<span class="hljs-keyword">var</span> b = foo(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(b.next());            <span class="hljs-comment">// &#123; value:6, done:false &#125;      y=undefined</span>
<span class="hljs-built_in">console</span>.log(b.next(<span class="hljs-number">12</span>));    <span class="hljs-comment">// &#123; value:8, done:false &#125;      y 后面的yield表达式重新设置为12 y=2*12=24  z=undefined</span>
<span class="hljs-built_in">console</span>.log(b.next(<span class="hljs-number">13</span>));    <span class="hljs-comment">// &#123; value:42, done:true &#125;      z 后面的yield表达式重新设置为13  5+24+13=42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">for...of 循环不再需要调用next方法</h3>
<p><code>for...of</code>循环可以自动遍历 <code>Generator </code>函数运行时生成的<code>Iterator</code>对象，且此时不再需要调用<code>next</code>方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">5</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-number">6</span>;
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> foo()) &#123;
  <span class="hljs-built_in">console</span>.log(v);
&#125;
<span class="hljs-comment">// 1 2 3 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">使原生对象支持for...of，通过 Generator 函数为它加上遍历接口</h4>
<p>原生的<code> JavaScript</code> 对象没有遍历接口，无法使用<code>for...of</code>循环，通过 <code>Generator</code> 函数为它加上这个接口，就可以用了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">objectEntries</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">let</span> propKeys = <span class="hljs-built_in">Reflect</span>.ownKeys(obj);

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> propKey <span class="hljs-keyword">of</span> propKeys) &#123;
    <span class="hljs-keyword">yield</span> [propKey, obj[propKey]];
  &#125;
&#125;

<span class="hljs-keyword">let</span> jane = &#123; <span class="hljs-attr">first</span>: <span class="hljs-string">'Jane'</span>, <span class="hljs-attr">last</span>: <span class="hljs-string">'Doe'</span> &#125;;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> objectEntries(jane)) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>: <span class="hljs-subst">$&#123;value&#125;</span>`</span>);
&#125;
<span class="hljs-comment">// first: Jane</span>
<span class="hljs-comment">// last: Doe</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-45">将 <code>Generator </code>函数加到对象的<code>Symbol.iterator</code>属性上面。</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">objectEntries</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> propKeys = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>);

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> propKey <span class="hljs-keyword">of</span> propKeys) &#123;
    <span class="hljs-keyword">yield</span> [propKey, <span class="hljs-built_in">this</span>[propKey]];
  &#125;
&#125;

<span class="hljs-keyword">let</span> jane = &#123; <span class="hljs-attr">first</span>: <span class="hljs-string">'Jane'</span>, <span class="hljs-attr">last</span>: <span class="hljs-string">'Doe'</span> &#125;;

jane[<span class="hljs-built_in">Symbol</span>.iterator] = objectEntries;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> jane) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>: <span class="hljs-subst">$&#123;value&#125;</span>`</span>);
&#125;
<span class="hljs-comment">// first: Jane</span>
<span class="hljs-comment">// last: Doe</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-46">扩展运算符（<code>...</code>）、解构赋值和<code>Array.from</code>方法可以将 <code>Generator </code>函数返回的 <code>Iterator</code> 对象，作为参数</h5>
<p>扩展运算符（<code>...</code>）、解构赋值和<code>Array.from</code>方法内部调用的，都是遍历器接口（for of）。这意味着，它们都可以将 <code>Generator </code>函数返回的 <code>Iterator</code> 对象，作为参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">numbers</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>
  <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>
&#125;

<span class="hljs-comment">// 扩展运算符</span>
[...numbers()] <span class="hljs-comment">// [1, 2]</span>

<span class="hljs-comment">// Array.from 方法</span>
<span class="hljs-built_in">Array</span>.from(numbers()) <span class="hljs-comment">// [1, 2]</span>

<span class="hljs-comment">// 解构赋值</span>
<span class="hljs-keyword">let</span> [x, y] = numbers();
x <span class="hljs-comment">// 1</span>
y <span class="hljs-comment">// 2</span>

<span class="hljs-comment">// for...of 循环</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> n <span class="hljs-keyword">of</span> numbers()) &#123;
  <span class="hljs-built_in">console</span>.log(n)
&#125;
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">Generator.prototype.throw() 在函数体外抛出错误，然后在 <code>Generator</code> 函数体内捕获</h2>
<p><code>Generator</code> 函数返回的遍历器对象，都有一个<code>throw</code>方法，在函数体外抛出错误，然后在 <code>Generator</code> 函数体内捕获。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> g = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span>;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内部捕获'</span>, e);
  &#125;
&#125;;

<span class="hljs-keyword">var</span> i = g();
i.next();

<span class="hljs-keyword">try</span> &#123;
  i.throw(<span class="hljs-string">'a'</span>);
  i.throw(<span class="hljs-string">'b'</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'外部捕获'</span>, e);
&#125;
<span class="hljs-comment">// 内部捕获 a</span>
<span class="hljs-comment">// 外部捕获 b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，遍历器对象<code>i</code>连续抛出两个错误。第一个错误被 <code>Generator </code>函数体内的<code>catch</code>语句捕获。<code>i</code>第二次抛出错误，由于 <code>Generator </code>函数内部的<code>catch</code>语句已经执行过了，不会再捕捉到这个错误了，所以这个错误就被抛出了<code>Generator</code>函数体，被函数体外的<code>catch</code>语句捕获。</p>
<h3 data-id="heading-48">1、<code>throw</code>方法可以接受一个参数，该参数会被<code>catch</code>语句接收，建议抛出<code>Error</code>对象的实例</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> g = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span>;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.log(e);
  &#125;
&#125;;

<span class="hljs-keyword">var</span> i = g();
i.next();
i.throw(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出错了！'</span>));
<span class="hljs-comment">// Error: 出错了！(…)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-49">2、不要混淆遍历器对象的<code>throw</code>方法和全局的<code>throw</code>命令</h3>
<p>上面代码的错误，是用遍历器对象的<code>throw</code>方法抛出的，而不是用<code>throw</code>命令抛出的。全局的<code>throw</code>命令抛出的错误只能被函数体外的<code>catch</code>语句捕获。</p>
<p><code>throw</code>命令与<code>g.throw</code>方法是无关的，两者互不影响。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> g = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">yield</span>;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (e != <span class="hljs-string">'a'</span>) <span class="hljs-keyword">throw</span> e;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内部捕获'</span>, e);
    &#125;
  &#125;
&#125;;

<span class="hljs-keyword">var</span> i = g();
i.next();

<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'a'</span>);
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'b'</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'外部捕获'</span>, e);
&#125;
<span class="hljs-comment">// 外部捕获 [Error: a]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-50">3、Generator 函数<code>内部</code>没有部署try...catch代码块，那么<code>throw</code>方法抛出的错误，将被外部<code>try...catch</code>代码块捕获</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> g = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-keyword">yield</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内部捕获'</span>, e);
  &#125;
&#125;;

<span class="hljs-keyword">var</span> i = g();
i.next();

<span class="hljs-keyword">try</span> &#123;
  i.throw(<span class="hljs-string">'a'</span>);
  i.throw(<span class="hljs-string">'b'</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'外部捕获'</span>, e);
&#125;
<span class="hljs-comment">// 外部捕获 a</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">4、Generator 函数<code>内部和外部</code>，都没有部署try...catch代码块那么程序将报错，直接中断执行</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> gen = <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'world'</span>);
&#125;

<span class="hljs-keyword">var</span> g = gen();
g.next();
g.throw();
<span class="hljs-comment">// hello</span>
<span class="hljs-comment">// Uncaught undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-52">5、throw方法抛出的错误要被内部捕获，前提是必须至少执行过一次next方法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内部捕获'</span>);
  &#125;
&#125;

<span class="hljs-keyword">var</span> g = gen();
g.throw(<span class="hljs-number">1</span>);
<span class="hljs-comment">// Uncaught 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>g.throw(1)</code>执行时，<code>next</code>方法一次都没有执行过。这时，抛出的错误不会被内部捕获，而是直接在外部抛出，导致程序出错。这种行为其实很好理解，因为<code>第一次执行next方法，等同于启动执行 Generator 函数的内部代码</code>，否则<code>Generator</code>函数还没有开始执行，这时<code>throw</code>方法抛错只可能抛出在函数外部。</p>
<h3 data-id="heading-53">6、throw方法被捕获以后，会附带执行下一条yield表达式</h3>
<p>也就是说，会附带执行一次next方法</p>
<p>只要<code>Generator</code>函数内部部署了<code>try...catch</code>代码块，那么遍历器的<code>throw</code>方法抛出的错误，不影响下一次遍历。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> gen = <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>);
&#125;

<span class="hljs-keyword">var</span> g = gen();
g.next() <span class="hljs-comment">// a</span>
g.throw() <span class="hljs-comment">// b</span>
g.next() <span class="hljs-comment">// c</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">7、Generator 函数体内抛出的错误，也可以被函数体外的catch捕获</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> x = <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
  <span class="hljs-keyword">var</span> y = x.toUpperCase();
  <span class="hljs-keyword">yield</span> y;
&#125;

<span class="hljs-keyword">var</span> it = foo();

it.next(); <span class="hljs-comment">// &#123; value:3, done:false &#125;</span>

<span class="hljs-keyword">try</span> &#123;
  it.next(<span class="hljs-number">42</span>);
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-built_in">console</span>.log(err);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个<code>next</code>方法向函数体内传入一个参数 <code>42</code>，数值是没有<code>toUpperCase</code>方法的，所以会抛出一个 <code>TypeError</code>错误，被函数体外的<code>catch</code>捕获。</p>
<h4 data-id="heading-55">一旦 Generator 执行过程中抛出错误，且没有被内部捕获，就不会再执行下去了</h4>
<p>一旦 <code>Generator </code>执行过程中抛出错误，且没有被内部捕获，就不会再执行下去了。</p>
<p>如果此后还调用<code>next</code>方法，将返回一个<code>value</code>属性等于<code>undefined</code>、<code>done</code>属性等于<code>true</code>的对象，即<code> JavaScript</code> 引擎认为这个 <code>Generator </code>已经运行结束了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'throwing an exception'</span>);
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'generator broke!'</span>);
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log</span>(<span class="hljs-params">generator</span>) </span>&#123;
  <span class="hljs-keyword">var</span> v;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'starting generator'</span>);
  <span class="hljs-keyword">try</span> &#123;
    v = generator.next();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次运行next方法'</span>, v);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'捕捉错误'</span>, v);
  &#125;
  <span class="hljs-keyword">try</span> &#123;
    v = generator.next();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次运行next方法'</span>, v);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'捕捉错误'</span>, v);
  &#125;
  <span class="hljs-keyword">try</span> &#123;
    v = generator.next();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三次运行next方法'</span>, v);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'捕捉错误'</span>, v);
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'caller done'</span>);
&#125;

log(g());
<span class="hljs-comment">// starting generator</span>
<span class="hljs-comment">// 第一次运行next方法 &#123; value: 1, done: false &#125;</span>
<span class="hljs-comment">// throwing an exception</span>
<span class="hljs-comment">// 捕捉错误 &#123; value: 1, done: false &#125;</span>
<span class="hljs-comment">// 第三次运行next方法 &#123; value: undefined, done: true &#125;</span>
<span class="hljs-comment">// caller done</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码一共<code>三次运行next</code>方法，<code>第二次</code>运行的时候会抛出错误，然后第三次运行的时候，<code>Generator</code> 函数就已经结束了，不再执行下去了。</p>
<h2 data-id="heading-56">Generator.prototype.return()返回给定的值，并且终结遍历 Generator函数</h2>
<p><code>Generator </code>函数返回的遍历器对象，还有一个<code>return</code>方法，可以<code>返回给定的值</code>，并且<code>终结遍历 Generator </code>函数。</p>
<h3 data-id="heading-57">1、如果<code>return</code>方法调用时，不提供参数，则返回值的<code>value</code>属性为<code>undefined</code></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-keyword">var</span> g = gen();

g.next()        <span class="hljs-comment">// &#123; value: 1, done: false &#125;</span>
g.return(<span class="hljs-string">'foo'</span>) <span class="hljs-comment">// &#123; value: "foo", done: true &#125;</span>
g.next()        <span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-58">2、调用return方法后，以后再调用next方法，value总是为undefined，done属性总是返回true</h3>
<p>上面代码中，遍历器对象<code>g</code>调用<code>return</code>方法后，返回值的<code>value</code>属性就是<code>return</code>方法的参数<code>foo</code>。并且，<code>Generator </code>函数的遍历就终止了，返回值的<code>done</code>属性为<code>true</code>，以后再调用<code>next</code>方法，<code>done</code>属性总是返回<code>true</code>。</p>
<h3 data-id="heading-59">3、如果 <code>Generator </code>函数内部有<code>try...finally</code>代码块，且正在执行<code>try</code>代码块，那么<code>return</code>方法会推迟到<code>finally</code>代码块执行完再执行</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">numbers</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">5</span>;
  &#125;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">6</span>;
&#125;
<span class="hljs-keyword">var</span> g = numbers();
g.next() <span class="hljs-comment">// &#123; value: 1, done: false &#125;</span>
g.next() <span class="hljs-comment">// &#123; value: 2, done: false &#125;</span>
g.return(<span class="hljs-number">7</span>) <span class="hljs-comment">// &#123; value: 4, done: false &#125;</span>
g.next() <span class="hljs-comment">// &#123; value: 5, done: false &#125;</span>
g.next() <span class="hljs-comment">// &#123; value: 7, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，调用<code>return</code>方法后，就开始执行<code>finally</code>代码块，然后等到<code>finally</code>代码块执行完，再执行<code>return</code>方法。</p>
<h2 data-id="heading-60">yield* 表达式，如果<code>yield</code>表达式后面跟的是一个遍历器对象，需要在<code>yield</code>表达式后面加上<code>星号</code>，表明它返回的是一个遍历器对象</h2>
<h3 data-id="heading-61">1、在 <code>Generator </code>函数内部，调用<code>另一个 Generator</code> 函数。需要在前者的函数体内部，自己手动完成遍历</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'a'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'b'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'x'</span>;
  <span class="hljs-comment">// 手动遍历 foo()</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> foo()) &#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'y'</span>;
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> bar())&#123;
  <span class="hljs-built_in">console</span>.log(v);
&#125;
<span class="hljs-comment">// x</span>
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// y</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">2、<code>ES6 </code>提供了<code>yield*</code>表达式，作为解决办法，用来在一个 <code>Generator </code>函数里面<code>执行另一个 Generator</code> 函数</h3>
<h4 data-id="heading-63">（1）<code>yield*</code>后面的 <code>Generator</code> 函数（没有<code>return</code>语句时），等同于在 <code>Generator</code> 函数内部，部署一个<code>for...of</code>循环</h4>
<h4 data-id="heading-64">（2）<code>yield*</code>后面的 <code>Generator </code>函数在有<code>return</code>语句时，则需要用<code>var value = yield* iterator</code>的形式获取<code>return</code>语句的值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'a'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'b'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'x'</span>;
  <span class="hljs-keyword">yield</span>* foo();
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'y'</span>;
&#125;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'x'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'a'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'b'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'y'</span>;
&#125;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'x'</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> foo()) &#123;
    <span class="hljs-keyword">yield</span> v;
  &#125;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'y'</span>;
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> bar())&#123;
  <span class="hljs-built_in">console</span>.log(v);
&#125;
<span class="hljs-comment">// "x"</span>
<span class="hljs-comment">// "a"</span>
<span class="hljs-comment">// "b"</span>
<span class="hljs-comment">// "y"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从语法角度看，如果<code>yield</code>表达式后面跟的是一个遍历器对象，需要在<code>yield</code>表达式后面加上<code>星号</code>，表明它返回的是一个遍历器对象。这被称为<code>yield*</code>表达式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'hello!'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">outer1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'open'</span>;
  <span class="hljs-keyword">yield</span> inner();
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'close'</span>;
&#125;

<span class="hljs-keyword">var</span> gen = outer1()
gen.next().value <span class="hljs-comment">// "open"</span>
gen.next().value <span class="hljs-comment">// 返回一个遍历器对象</span>
gen.next().value <span class="hljs-comment">// "close"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">outer2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'open'</span>
  <span class="hljs-keyword">yield</span>* inner()
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'close'</span>
&#125;

<span class="hljs-keyword">var</span> gen = outer2()
gen.next().value <span class="hljs-comment">// "open"</span>
gen.next().value <span class="hljs-comment">// "hello!"</span>
gen.next().value <span class="hljs-comment">// "close"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-65">yield*后面跟着一个数组(字符串)，由于数组（字符串）原生支持遍历器，因此就会遍历数组成员</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//yield命令后面如果不加星号，返回的是整个数组，加了星号就表示返回的是数组的遍历器对象。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">yield</span>* [<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>];
&#125;
<span class="hljs-keyword">var</span> n=gen();
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"a", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"b", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"c", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:undefined, done:true &#125;</span>

<span class="hljs-comment">//yield表达式返回整个字符串，yield*语句返回单个字符。因为字符串具有 Iterator 接口，所以被yield*遍历</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">yield</span>* <span class="hljs-string">'hello'</span>;
&#125;
<span class="hljs-keyword">var</span> n=gen();
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"h", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"e", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:"l", done:false &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:'l', done:true &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:'o', done:true &#125;</span>
<span class="hljs-built_in">console</span>.log(n.next()); <span class="hljs-comment">// &#123; value:undefined, done:true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">被代理的 Generator 函数有return语句,就可以向代理它的 <code>Generator </code>函数返回数据</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'foo'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">bar</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
    <span class="hljs-keyword">var</span> v = <span class="hljs-keyword">yield</span>* foo();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'v'</span> + v);
    <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>;
&#125;

<span class="hljs-keyword">var</span> it = bar();

<span class="hljs-built_in">console</span>.log(it.next());     <span class="hljs-comment">//&#123; value: 1, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(it.next());     <span class="hljs-comment">//&#123; value: 2, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(it.next());     <span class="hljs-comment">//&#123; value: 3, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(it.next());     <span class="hljs-comment">//vfoo</span>
                            <span class="hljs-comment">//&#123; value: 4, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(it.next());     <span class="hljs-comment">//&#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">genFuncWithReturn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'a'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'b'</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'The result'</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">logReturned</span>(<span class="hljs-params">genObj</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">yield</span>* genObj;
  <span class="hljs-built_in">console</span>.log(result);
&#125;

[...logReturned(genFuncWithReturn())]
<span class="hljs-comment">// The result</span>
<span class="hljs-comment">// 值为 [ 'a', 'b' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>存在<code>两次遍历</code>。第一次是扩展运算符遍历函数<code>logReturned</code>返回的遍历器对象，第二次是<code>yield*</code>语句遍历函数<code>genFuncWithReturn</code>返回的遍历器对象。这两次遍历的效果是叠加的，最终表现为扩展运算符遍历函数<code>genFuncWithReturn</code>返回的遍历器对象。所以，最后的数据表达式得到的值等于<code>[ 'a', 'b' ]</code>。但是，函数<code>genFuncWithReturn</code>的<code>return</code>语句的返回值<code>The result</code>，会返回给函数<code>logReturned</code>内部的<code>result</code>变量，因此会有终端输出。</p>
<h3 data-id="heading-67">yield*命令可以很方便地取出嵌套数组的所有成员</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">iterTree</span>(<span class="hljs-params">tree</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(tree)) &#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i < tree.length; i++) &#123;
      <span class="hljs-keyword">yield</span>* iterTree(tree[i]);
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">yield</span> tree;
  &#125;
&#125;

<span class="hljs-keyword">const</span> tree = [ <span class="hljs-string">'a'</span>, [<span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>], [<span class="hljs-string">'d'</span>, <span class="hljs-string">'e'</span>] ];

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> x <span class="hljs-keyword">of</span> iterTree(tree)) &#123;
  <span class="hljs-built_in">console</span>.log(x);
&#125;
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// c</span>
<span class="hljs-comment">// d</span>
<span class="hljs-comment">// e</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-68">作为对象属性的 Generator 函数</h2>
<p>如果一个对象的属性是 Generator 函数，可以简写成下面的形式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
  * <span class="hljs-function"><span class="hljs-title">myGeneratorMethod</span>(<span class="hljs-params"></span>)</span> &#123;
    ···
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的完整形式如下，与上面的写法是等价的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">myGeneratorMethod</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ···</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-69">Generator 函数的this</h2>
<h3 data-id="heading-70">1、Generator 函数的实例，也继承了 Generator 函数的prototype对象上的方法</h3>
<p>Generator 函数总是返回一个遍历器，ES6 规定这个遍历器是 Generator 函数的实例，也继承了 Generator 函数的prototype对象上的方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

g.prototype.hello = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'hi!'</span>;
&#125;;

<span class="hljs-keyword">let</span> obj = g();

obj <span class="hljs-keyword">instanceof</span> g <span class="hljs-comment">// true</span>
obj.hello() <span class="hljs-comment">// 'hi!'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-71">2、Generator 函数也不能当构造函数</h3>
<p>如果把g当作普通的构造函数，并不会生效，因为g返回的总是遍历器对象，而不是this对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.a = <span class="hljs-number">11</span>;
&#125;

<span class="hljs-keyword">let</span> obj = g();
obj.next();
obj.a <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">3、Generator 函数也不能跟new命令一起用，会报错</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">this</span>.x = <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">this</span>.y = <span class="hljs-number">3</span>;
&#125;

<span class="hljs-keyword">new</span> F()
<span class="hljs-comment">// TypeError: F is not a constructor</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">4、让 Generator 函数返回一个正常的对象实例，既可以用next方法，又可以获得正常的this</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">this</span>.b = <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-built_in">this</span>.c = <span class="hljs-number">3</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> gen.call(gen.prototype);
&#125;

<span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> F();

f.next();  <span class="hljs-comment">// Object &#123;value: 2, done: false&#125;</span>
f.next();  <span class="hljs-comment">// Object &#123;value: 3, done: false&#125;</span>
f.next();  <span class="hljs-comment">// Object &#123;value: undefined, done: true&#125;</span>

f.a <span class="hljs-comment">// 1</span>
f.b <span class="hljs-comment">// 2</span>
f.c <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-74">Generator 与状态机</h2>
<p>Generator 是实现状态机的最佳结构。</p>
<p>下面的clock函数就是一个状态机</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//es5</span>
<span class="hljs-keyword">var</span> ticking = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> clock = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (ticking)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Tick!'</span>);
  <span class="hljs-keyword">else</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Tock!'</span>);
  ticking = !ticking;
&#125;

<span class="hljs-comment">//es6</span>
<span class="hljs-comment">//因为while一直成立 所以 一直循环产生Tick 、 Tock</span>
<span class="hljs-keyword">var</span> clock = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Tick!'</span>);
        <span class="hljs-keyword">yield</span>;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Tock!'</span>);
        <span class="hljs-keyword">yield</span>;
    &#125;
&#125;();
<span class="hljs-built_in">console</span>.log(clock.next());
<span class="hljs-built_in">console</span>.log(clock.next());
<span class="hljs-built_in">console</span>.log(clock.next());
<span class="hljs-built_in">console</span>.log(clock.next());
<span class="hljs-comment">// Tick!</span>
<span class="hljs-comment">//     &#123; value: undefined, done: false &#125;</span>
<span class="hljs-comment">// Tock!</span>
<span class="hljs-comment">//     &#123; value: undefined, done: false &#125;</span>
<span class="hljs-comment">// Tick!</span>
<span class="hljs-comment">//     &#123; value: undefined, done: false &#125;</span>
<span class="hljs-comment">// Tock!</span>
<span class="hljs-comment">//     &#123; value: undefined, done: false &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-75">应用</h2>
<h3 data-id="heading-76">（1）异步操作的同步化表达</h3>
<p><code>Generator </code>函数的<code>暂停执行的效果</code>，意味着可以把异步操作写在<code>yield</code>表达式里面，等到调用<code>next</code>方法时再往后执行。这实际上等同于不需要写回调函数了，因为<code>异步操作的后续操作可以放在yield表达式下面</code>，反正要等到调用<code>next</code>方法时再执行。所以，<code>Generator</code> 函数的一个重要实际意义就是<code>用来处理异步操作</code>，改写回调函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">loadUI</span>(<span class="hljs-params"></span>) </span>&#123;
  showLoadingScreen();
  <span class="hljs-keyword">yield</span> loadUIDataAsynchronously();
  hideLoadingScreen();
&#125;
<span class="hljs-keyword">var</span> loader = loadUI();<span class="hljs-comment">//调用`loadUI`函数时其实没有任何操作</span>
<span class="hljs-comment">// 加载UI</span>
loader.next()<span class="hljs-comment">//第一次next</span>

<span class="hljs-comment">// 卸载UI</span>
loader.next()<span class="hljs-comment">//第二次next</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次调用<code>loadUI</code>函数时，该函数不会执行，仅返回一个遍历器。</p>
<p>下一次对该遍历器调用<code>next</code>方法，则会显示<code>Loading</code>界面（<code>showLoadingScreen</code>），并且异步加载数据（<code>loadUIDataAsynchronously</code>）。</p>
<p>等到数据加载完成，再一次使用next方法，则会隐藏Loading界面。</p>
<h4 data-id="heading-77">Generator 函数部署 Ajax 操作</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">yield</span> request(<span class="hljs-string">"http://some.url"</span>);
  <span class="hljs-keyword">var</span> resp = <span class="hljs-built_in">JSON</span>.parse(result);
    <span class="hljs-built_in">console</span>.log(resp.value);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">url</span>) </span>&#123;
  makeAjaxCall(url, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>)</span>&#123;
    it.next(response);   <span class="hljs-comment">//next必须加上参数 要不然main函数中 的 result是undefined</span>
  &#125;);
&#125;

<span class="hljs-keyword">var</span> it = main();
it.next();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-78">通过 Generator 函数逐行读取文本文件</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">numbers</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> file = <span class="hljs-keyword">new</span> FileReader(<span class="hljs-string">"numbers.txt"</span>);
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">while</span>(!file.eof) &#123;
      <span class="hljs-keyword">yield</span> <span class="hljs-built_in">parseInt</span>(file.readLine(), <span class="hljs-number">10</span>);
    &#125;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    file.close();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-79">（2）控制流管理</h3>
<p>如果有一个多步操作非常耗时。</p>
<h4 data-id="heading-80">回调函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">step1(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value1</span>) </span>&#123;
  step2(value1, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value2</span>) </span>&#123;
    step3(value2, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value3</span>) </span>&#123;
      step4(value3, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value4</span>) </span>&#123;
        <span class="hljs-comment">// Do something with value4</span>
      &#125;);
    &#125;);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-81">Promise</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.resolve(step1)
  .then(step2)
  .then(step3)
  .then(step4)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value4</span>) </span>&#123;
    <span class="hljs-comment">// Do something with value4</span>
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// Handle any error from step1 through step4</span>
  &#125;)
  .done();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-82">Generator 函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">longRunningTask</span>(<span class="hljs-params">value1</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">var</span> value2 = <span class="hljs-keyword">yield</span> step1(value1);
    <span class="hljs-keyword">var</span> value3 = <span class="hljs-keyword">yield</span> step2(value2);
    <span class="hljs-keyword">var</span> value4 = <span class="hljs-keyword">yield</span> step3(value3);
    <span class="hljs-keyword">var</span> value5 = <span class="hljs-keyword">yield</span> step4(value4);
    <span class="hljs-comment">// Do something with value4</span>
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-comment">// Handle any error from step1 through step4</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，使用一个函数，按次序自动执行所有步骤。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">scheduler(longRunningTask(initialValue));

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduler</span>(<span class="hljs-params">task</span>) </span>&#123;
  <span class="hljs-keyword">var</span> taskObj = task.next(task.value);
  <span class="hljs-comment">// 如果Generator函数未结束，就继续调用</span>
  <span class="hljs-keyword">if</span> (!taskObj.done) &#123;
    task.value = taskObj.value
    scheduler(task);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这种做法，只适合同步操作，即所有的task都必须是同步的，不能有异步操作。因为这里的代码一得到返回值，就继续往下执行，没有判断异步操作何时完成。</p>
<h4 data-id="heading-83">利用for...of循环会自动依次执行yield命令的特性，提供一种更一般的控制流管理的方法</h4>
<p>(<code>只能用于所有步骤都是同步操作</code>)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//数组steps封装了一个任务的多个步骤</span>
<span class="hljs-keyword">let</span> steps = [step1Func, step2Func, step3Func];

<span class="hljs-comment">//Generator 函数iterateSteps则是依次为这些步骤加上yield命令</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">iterateSteps</span>(<span class="hljs-params">steps</span>)</span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i< steps.length; i++)&#123;
    <span class="hljs-keyword">var</span> step = steps[i];
    <span class="hljs-keyword">yield</span> step();
  &#125;
&#125;

<span class="hljs-comment">//用for...of循环一次性依次执行所有任务的所有步骤</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> step <span class="hljs-keyword">of</span> iterateJobs(jobs))&#123;
  <span class="hljs-built_in">console</span>.log(step.id);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-84"><code>for...of</code>的本质是一个<code>while</code>循环，所以上面的代码实质上执行的是下面的逻辑</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> it = iterateJobs(jobs);
<span class="hljs-keyword">var</span> res = it.next();

<span class="hljs-keyword">while</span> (!res.done)&#123;
  <span class="hljs-keyword">var</span> result = res.value;
  <span class="hljs-comment">// ...</span>
  res = it.next();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-85">（3）利用 <code>Generator </code>函数，可以在<code>任意对象</code>上部署<code>Iterator</code>接口</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">iterEntries</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">let</span> keys = <span class="hljs-built_in">Object</span>.keys(obj);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i < keys.length; i++) &#123;
    <span class="hljs-keyword">let</span> key = keys[i];
    <span class="hljs-keyword">yield</span> [key, obj[key]];
  &#125;
&#125;

<span class="hljs-keyword">let</span> myObj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">bar</span>: <span class="hljs-number">7</span> &#125;;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> iterEntries(myObj)) &#123;
  <span class="hljs-built_in">console</span>.log(key, value);
&#125;

<span class="hljs-comment">// foo 3</span>
<span class="hljs-comment">// bar 7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对数组部署 Iterator 接口</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">makeSimpleGenerator</span>(<span class="hljs-params">array</span>)</span>&#123;
  <span class="hljs-keyword">var</span> nextIndex = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">while</span>(nextIndex < array.length)&#123;
    <span class="hljs-keyword">yield</span> array[nextIndex++];
  &#125;
&#125;

<span class="hljs-keyword">var</span> gen = makeSimpleGenerator([<span class="hljs-string">'yo'</span>, <span class="hljs-string">'ya'</span>]);

gen.next().value <span class="hljs-comment">// 'yo'</span>
gen.next().value <span class="hljs-comment">// 'ya'</span>
gen.next().done  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-86">（4）作为数据结构</h3>
<h4 data-id="heading-87"><code>Generator</code> 可以看作是<code>数据结构</code>，更确切地说，可以看作是一个<code>数组结构</code></h4>
<p>因为 <code>Generator</code> 函数可以<code>返回一系列的值</code>，这意味着它可以对任意表达式，提供类似数组的接口。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">doStuff</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'hello.txt'</span>);
  <span class="hljs-keyword">yield</span> fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'world.txt'</span>);
  <span class="hljs-keyword">yield</span> fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'and-such.txt'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码就是依次返回三个函数，但是由于使用了 Generator 函数，导致可以像处理数组那样，处理这三个返回的函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (task <span class="hljs-keyword">of</span> doStuff()) &#123;
  <span class="hljs-comment">// task是一个函数，可以像回调函数那样使用它</span>
&#125;

<span class="hljs-comment">//相当于  ES5 </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doStuff</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> [
    fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'hello.txt'</span>),
    fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'world.txt'</span>),
    fs.readFile.bind(<span class="hljs-literal">null</span>, <span class="hljs-string">'and-such.txt'</span>)
  ];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            