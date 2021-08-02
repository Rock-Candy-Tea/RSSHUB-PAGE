
---
title: 'JavaScript 基础（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3654'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:52:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=3654'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">函数</h2>
<p>​函数就是功能，封装一些语句放在函数内部，函数就具有了某一特定的功能</p>
<blockquote>
<p>声明：<code>function 函数名() &#123;&#125;</code></p>
</blockquote>
<blockquote>
<p>调用：<code>函数名();</code></p>
</blockquote>
<h3 data-id="heading-1">函数基础</h3>
<h4 data-id="heading-2">1. 函数的声明和调用</h4>
<p>函数声明：定义函数</p>
<p>关键字：<code>function</code></p>
<p>语法：</p>
<blockquote>
<p><code>function 函数名(参数) &#123;   结构体 &#125;</code></p>
</blockquote>
<p>调用：</p>
<blockquote>
<p><code>函数名();</code></p>
</blockquote>
<p>注</p>
<ul>
<li>函数名必须遵循标示符定义规则</li>
<li>函数只能先声明，才能够调用</li>
<li>函数声明时，内部的语句不会执行</li>
<li>函数执行的位置与声明的位置无关，取决于调用的位置</li>
<li>函数调用语法：函数名(实参);</li>
<li>函数可以多次调用</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
fun();
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 函数的参数</h4>
<p>​函数可以帮我们封装一些代码，代码可以穿重复调用，函数留了一个接口，就是我们的参数，可以通过参数的变化让我们的函数发生不同的作用。</p>
<p>​参数就是变量：命名规则与变量一样</p>
<blockquote>
<p><code>形参</code>：函数定义时，小括号里的参数叫做形式参数</p>
<p><code>实参</code>：函数调用时，小括号的参数叫实际参数</p>
<p><code>传参</code>：函数执行时，把实际参数传递到形式参数的过程</p>
</blockquote>
<p>JavaScript 是一个动态类型数据语言，变量的类型会根据里面存放的内容而变化。实参的数据类型会影响形参的数据类型，导致函数输出结构发生变化。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(a + b);
&#125;
sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
sum(<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span>);
sum(<span class="hljs-number">5</span>); <span class="hljs-comment">// 5 + undefined</span>
<span class="hljs-comment">// 12 number</span>
<span class="hljs-comment">// 12 string</span>
<span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3. 函数返回值 <code>return</code></h4>
<p>函数可以使用 <code>return</code>语句接受参数进行操作，<code>return</code> 只是返回值，不会输出。</p>
<blockquote>
<p>在函数中执行到 <code>return</code>关键字，会立即停止执行，直接返回</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>); <span class="hljs-comment">//不执行</span>
&#125;
<span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>));
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4. 模块化编程案例</h4>
<p>案例1：判断1000以内得质数</p>
<p>​思路：判断一个数是不是质数 ===》 找这个数得约数个数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">YSGS</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">var</span> sum = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i <= a; i++) &#123;
    <span class="hljs-keyword">if</span> (a % i === <span class="hljs-number">0</span>) &#123;
      sum ++;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> sum;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isZS</span>(<span class="hljs-params">b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> YSGS(b) === <span class="hljs-number">2</span> ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i < <span class="hljs-number">1000</span>; i++) &#123;
  <span class="hljs-keyword">let</span> msg = isZS(i) === <span class="hljs-literal">true</span> ?  <span class="hljs-string">'是质数'</span> : <span class="hljs-string">'不是质数'</span>
  <span class="hljs-built_in">console</span>.log(i + msg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例2：1-1000中得完美数</p>
<p>​思路：判断一个数是不是完美数数 ===》 约束和等于本身</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">YSH</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < a; i++) &#123;
    <span class="hljs-keyword">if</span> (a % i === <span class="hljs-number">0</span>) &#123;
      sum += i;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> sum;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isWMS</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">return</span> YSH(a) === a ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">WMS</span>(<span class="hljs-params">total</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>; i < total; i++) &#123;
    <span class="hljs-keyword">if</span> (isWMS(i)) &#123;
      <span class="hljs-built_in">console</span>.log(i + <span class="hljs-string">'是完美数'</span>);
    &#125;
  &#125;
&#125;

WMS(<span class="hljs-number">10000</span>);
<span class="hljs-comment">// 6是完美数</span>
<span class="hljs-comment">// 28是完美数</span>
<span class="hljs-comment">// 496是完美数</span>
<span class="hljs-comment">/// 8128是完美数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">5. 函数表达式</h4>
<p>函数定义可以使用关键字 <code>function</code> 来声明，也可以使用变量定义函数，称之为匿名函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;;
<span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>));
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">6. 函数的数据类型</h4>
<ul>
<li>
<p>简单数据类型</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
<span class="hljs-keyword">var</span> b = a;
a = <span class="hljs-number">4</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-comment">// 4</span>
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>引用数据类型</p>
<blockquote>
<p>引用数据类型传递的是地址，之间相互影响，详情参考</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> fun1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
&#125;
<span class="hljs-keyword">var</span> fun2 = fun1
fun2.haha = <span class="hljs-number">10</span>;
<span class="hljs-built_in">console</span>.log(fun1.haha); 
<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">7. 函数声明的提升</h4>
<ul>
<li>
<p>变量声明得提升：先引用，后定义，只提升定义，不提升赋值</p>
</li>
<li>
<p>函数声明得提升：先调用，后声明，只提升函数命，不提升定义，函数名指向函数得地址，所以调用函数时，函数内部得语句也会执行</p>
</li>
</ul>
<p>根据这个特性，我们一般会先调用函数，在最后声明函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fun();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>);
&#125;
<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当函数和变量重名时</p>
<blockquote>
<p><code>如果变量有值，那么输出的就是变量的值。</code></p>
<p><code>如果变量没有值，那么输出的就是这个函数。</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">var</span> sum = <span class="hljs-number">5</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;
<span class="hljs-built_in">console</span>.log(sum);
 

<span class="hljs-keyword">var</span> num;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">num</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;
<span class="hljs-built_in">console</span>.log(num);

<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">var</span> a = <span class="hljs-number">5</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;

<span class="hljs-comment">// 5</span>
<span class="hljs-comment">// [Function: num]</span>
<span class="hljs-comment">// [Function: a]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当关键字声明函数和函数表达式重名时，关键字声明会覆盖函数表达式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">foo();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>);
&#125;
<span class="hljs-keyword">var</span> foo = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;
<span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">函数进阶</h3>
<h4 data-id="heading-10">1. 递归函数</h4>
<p>定义</p>
<blockquote>
<p>在一个函数内部通过名字调用自身函数</p>
</blockquote>
<blockquote>
<p>一个函数可以调用自身，这中现场叫做 <code>递归</code></p>
</blockquote>
<p>应用</p>
<blockquote>
<p>递归函数常用来处理一些数学问题</p>
<p>例如：斐波那契数列：1 1 2 3 5 8 13 21 34</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用一个函数求斐波那契数列的任意项</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">feibo</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
    <span class="hljs-keyword">if</span> (n === <span class="hljs-number">1</span> || n === <span class="hljs-number">2</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
     &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-keyword">return</span> feibo(n-<span class="hljs-number">1</span>) + feibo(n-<span class="hljs-number">2</span>)
     &#125;
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(feibo(<span class="hljs-number">9</span>));
<span class="hljs-comment">// 34</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2. 变量的作用域</h4>
<p>函数内部中使用关键字 <code>var</code> 定义的变量（函数作用域），只能在函数内部使用，不能在函数外部取得。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
  <span class="hljs-built_in">console</span>.log(num);
  <span class="hljs-comment">// 1</span>
&#125;
<span class="hljs-built_in">console</span>.log(num);
<span class="hljs-comment">// num is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">3. 局部变量和全局变量</h4>
<p>局部变量：在作用域（定义域）内定义的变量就是这个作用域的局部变量，只能在作用域内被访问到。</p>
<p>全局变量：全局变量定义在全局，可以在任何地方访问到。</p>
<p>变量声明原理：全局变量，在全局定义后会永久存在，任何时候任何位置都能访问；局部变量定义在函数内部，函数定义的过程并没有去定义这个局部变量，只有在函数执行的时，才会立即定义这个局部变量，执行完之后，变量回立即销毁，在其他地方访问时，找不到这个变量，所以报错该变量未定义。</p>
<h4 data-id="heading-13">4. 作用域链</h4>
<blockquote>
<p>作用域链指的是变量在查找的规律：在不同的作用域内使用相同的标识符去命名变量。若当前作用域内有这个变量，则直接使用；若没有，则会一层一层的从本层向外层依次查找，使用查找到的第一个（就近原则）</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> num = <span class="hljs-number">2</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> num = <span class="hljs-number">3</span>;
    <span class="hljs-built_in">console</span>.log(num);
    <span class="hljs-comment">// 本层中有定义直接输出 3</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun3</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(num);
      <span class="hljs-comment">// 本层没有定义，从本层出发依次向外查找，得到上层的 3</span>
    &#125;
    fun3();
  &#125;
  fun2();
&#125;
fun1();
<span class="hljs-built_in">console</span>.log(num);
<span class="hljs-comment">// 输出全局的 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">5. 形参是局部变量</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(a);
  <span class="hljs-comment">// 1</span>
&#125;
fun(<span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-comment">// a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">6. 全局变量的作用</h4>
<ul>
<li>传递：全局变量可以在不同函数间通信（信号量）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jia</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(num++);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jian</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(num--);
&#125;
jia();  <span class="hljs-comment">// 2</span>
jia();  <span class="hljs-comment">// 3</span>
jian();  <span class="hljs-comment">// 2</span>
jian();  <span class="hljs-comment">// 1</span>
jia();  <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同意函数不同调用</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 全局变量，不会让变量重置或者清空</span>
<span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">plus</span>(<span class="hljs-params"></span>) </span>&#123;
  num += <span class="hljs-number">4</span>;
  <span class="hljs-built_in">console</span>.log(num++);
&#125;
plus();  <span class="hljs-comment">// 5</span>
plus();  <span class="hljs-comment">// 9</span>
plus();  <span class="hljs-comment">// 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">7. 函数作用域</h4>
<blockquote>
<p>函数作用域与变量类似，只能在函数声明的地方使用，外部的任何地方都访问不到</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  &#125;
  inner();
&#125;
outer();
<span class="hljs-comment">// 1</span>
inner();
<span class="hljs-comment">// inner is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">8. 闭包</h4>
<p>体会闭包</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(num);
  &#125;
  <span class="hljs-comment">// inner 没有括号表示只输出inner函数的定义，不会立即执行</span>
  <span class="hljs-keyword">return</span> inner;
&#125;
<span class="hljs-built_in">console</span>.log(outer());
<span class="hljs-comment">/*
ƒ inner() &#123;
  console.log(num);
&#125;
*/</span>
<span class="hljs-keyword">var</span> fun = outer();
<span class="hljs-comment">// fun相当于inner函数的定义（地址）</span>
fun();
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 本层没有num的定义，但是inner存在作用域链，所以输出1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>闭包</code> ：函数把自己的 <code>内部语句</code> 和自己声明所出的 <code>作用域</code> 封装成一个密闭的环境</p>
</blockquote>
<p>函数本身就是一个闭包。函数在定义的时候，能够记住他的外部环境和内部语句，每次执行都会参考定义时的密闭环境。</p>
<p>案例1</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params">y</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(x + y);
  &#125;
  <span class="hljs-keyword">return</span> inner;
&#125;
<span class="hljs-keyword">var</span> fun = outer(<span class="hljs-number">3</span>);
<span class="hljs-comment">/*
  此时fun = function inner(y) &#123;
    console.log(3 + y);
  &#125;
*/</span>
fun(<span class="hljs-number">5</span>); <span class="hljs-comment">// 8</span>
fun(<span class="hljs-number">8</span>); <span class="hljs-comment">// 11</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例2</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(x + y);
  &#125;
  <span class="hljs-keyword">return</span> inner;
&#125;
<span class="hljs-keyword">var</span> fun = outer(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">/*
  inner的外部环境为
  x = 2;
  y = 3;
  fun = function inner(y) &#123;
    此时x为传入的参数可以直接使用，
    x在该作用域不存在找到上层 y = 3;
    console.log(x + 3);
  &#125;
*/</span>
fun(<span class="hljs-number">5</span>); <span class="hljs-comment">// 8</span>
fun(<span class="hljs-number">7</span>); <span class="hljs-comment">// 10</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例3</p>
<blockquote>
<p>函数的闭包，记住了定义时所在的作用域，这个作用域中的变量不是一成不变的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> num++;
  &#125;
  <span class="hljs-keyword">return</span> inner;
&#125;
<span class="hljs-keyword">var</span> fun = outer();
<span class="hljs-comment">/*
  inner的外部环境为
  num = 1;
  fun = function inner() &#123;
    num在该作用域不存在找到上层 num = 1;
    return num++;
  &#125;
*/</span>
<span class="hljs-built_in">console</span>.log(fun());
<span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(fun());
<span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(fun());
<span class="hljs-comment">// 3</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例4</p>
<blockquote>
<p>每次调用一个函数，都会产生一个新得闭包，新的闭包，语句全新，外部环境也是新的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outer</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inner</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> num++;
  &#125;
  <span class="hljs-keyword">return</span> inner;
&#125;
<span class="hljs-keyword">var</span> fun1 = outer();
<span class="hljs-keyword">var</span> fun2 = outer();
<span class="hljs-comment">/*
  inner的外部环境为 num = 1;
  fun1 = function inner() &#123;
    num在该作用域不存在找到上层 num = 1;
    return num++;
  &#125;
  fun1 = function inner() &#123;
    num在该作用域不存在找到上层 num = 1;
    return num++;
  &#125;
*/</span>
<span class="hljs-built_in">console</span>.log(fun1());
<span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(fun1());
<span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(fun2());
<span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(fun2());
<span class="hljs-comment">// 2</span>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            