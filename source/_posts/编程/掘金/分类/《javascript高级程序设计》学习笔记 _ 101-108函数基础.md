
---
title: '《javascript高级程序设计》学习笔记 _ 10.1-10.8.函数基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4724'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 17:41:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4724'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>关注<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsimon9124%2Fmy_demos" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/simon9124/my_demos" ref="nofollow noopener noreferrer">前端小讴</a>，阅读更多原创技术文章</strong></p>
</blockquote>
<ul>
<li>函数是<strong>对象</strong>，每个函数都是 <code>Function</code> 类型的实例，都与其他引用类型一样具有<strong>属性</strong>和<strong>方法</strong></li>
<li>函数名是<strong>指向函数对象的指针</strong>，不会与某个函数绑定（一个函数可能会有多个名字）</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsimon9124%2Fmy_demos%2Fblob%2Fmaster%2Fjavascript%25E9%25AB%2598%25E7%25BA%25A7%25E7%25A8%258B%25E5%25BA%258F%25E8%25AE%25BE%25E8%25AE%25A1%25EF%25BC%2588%25E7%25AC%25AC%25E5%259B%259B%25E7%2589%2588%25EF%25BC%2589%2F%25E7%25AC%25AC10%25E7%25AB%25A0%2520%25E5%2587%25BD%25E6%2595%25B0%2F10.1-10.8.%25E5%2587%25BD%25E6%2595%25B0%25E5%259F%25BA%25E7%25A1%2580.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/simon9124/my_demos/blob/master/javascript%E9%AB%98%E7%BA%A7%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%EF%BC%88%E7%AC%AC%E5%9B%9B%E7%89%88%EF%BC%89/%E7%AC%AC10%E7%AB%A0%20%E5%87%BD%E6%95%B0/10.1-10.8.%E5%87%BD%E6%95%B0%E5%9F%BA%E7%A1%80.js" ref="nofollow noopener noreferrer">相关代码 →</a></p>
<h1 data-id="heading-0">4 种定义方式</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1.函数声明定义</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;

<span class="hljs-comment">// 2.函数表达式定义</span>
<span class="hljs-keyword">let</span> sum = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;

<span class="hljs-comment">// 4.箭头函数定义</span>
<span class="hljs-keyword">let</span> sum = <span class="hljs-function">(<span class="hljs-params">num1, num2</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;

<span class="hljs-comment">// 4.Function构造函数定义</span>
<span class="hljs-comment">/* 不推荐使用构造函数定义，因为会造成解析2次代码（1次解析常规js代码，1次解析传入构造函数中的字符串） */</span>
<span class="hljs-keyword">var</span> sum = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'num1'</span>, <span class="hljs-string">'num2'</span>, <span class="hljs-string">'return num1+num2'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">10.1 箭头函数</h1>
<ul>
<li>任何可以使用函数表达式的地方<strong>都可以</strong>使用箭头函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arrowSum = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="hljs-keyword">let</span> functionExpressionSum = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="hljs-built_in">console</span>.log(arrowSum(<span class="hljs-number">5</span>, <span class="hljs-number">8</span>)) <span class="hljs-comment">// 13</span>
<span class="hljs-built_in">console</span>.log(functionExpressionSum(<span class="hljs-number">5</span>, <span class="hljs-number">8</span>)) <span class="hljs-comment">// 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果只有<strong>1 个参数</strong>，可以<strong>不用括号</strong>（多个参数或无参数必须用括号）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> double = <span class="hljs-function">(<span class="hljs-params">x</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> x * <span class="hljs-number">3</span>
&#125;
<span class="hljs-built_in">console</span>.log(double(<span class="hljs-number">3</span>)) <span class="hljs-comment">// 9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以<strong>不用大括号</strong>，如果这样则箭头后面<strong>只能有 1 行代码（赋值操作或表达式）</strong>，且<strong>隐式返回这行代码的值（不能有<code>return</code>）</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> person = &#123;&#125;
<span class="hljs-keyword">let</span> setName = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> (obj.name = <span class="hljs-string">'Matt'</span>) <span class="hljs-comment">// 相当于 &#123; return obj.name = 'Matt' &#125;</span>
<span class="hljs-comment">// let setName = (obj) => &#123; return (obj.name = 'Matt') &#125; // 用大括号的写法</span>
setName(person)
<span class="hljs-built_in">console</span>.log(person.name) <span class="hljs-comment">// 'Matt'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>箭头函数<strong>不适用</strong>的场合：
<ul>
<li>不能使用<code>arguments</code>、<code>super</code>和<code>new.target</code></li>
<li>不能用作构造函数</li>
<li>没有<code>prototype</code>属性（）</li>
</ul>
</li>
</ul>
<h1 data-id="heading-2">10.2 函数名</h1>
<ul>
<li>函数名是<strong>指向函数的指针</strong>，一个函数可以有<strong>多个</strong>名称</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;
<span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>)) <span class="hljs-comment">// 20</span>

<span class="hljs-keyword">var</span> anotherSum = sum <span class="hljs-comment">// 使用不带括号的函数名是访问函数指针，而非调用函数</span>
<span class="hljs-built_in">console</span>.log(anotherSum(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>)) <span class="hljs-comment">// 20</span>

sum = <span class="hljs-literal">null</span> <span class="hljs-comment">// 切断sum与函数的关系</span>
<span class="hljs-built_in">console</span>.log(anotherSum(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>)) <span class="hljs-comment">// 20，anotherSum()仍可正常调用</span>
<span class="hljs-comment">// console.log(sum(10, 10)) // 会报错，sum is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES6 所有函数对象都暴露一个<strong>只读</strong>的<code>name</code>属性，默认保存<strong>函数标识符</strong>（字符串化的函数名）</li>
<li><strong>无函数名</strong>则标识成空字符串，使用<code>Function</code>构造函数创建则标识成<code>anonymous</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 函数声明</span>
<span class="hljs-keyword">let</span> bar = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 函数表达式</span>
<span class="hljs-keyword">let</span> baz = <span class="hljs-function">() =></span> &#123;&#125; <span class="hljs-comment">// 箭头函数</span>

<span class="hljs-built_in">console</span>.log(foo.name) <span class="hljs-comment">// 'foo'</span>
<span class="hljs-built_in">console</span>.log(bar.name) <span class="hljs-comment">// 'bar'</span>
<span class="hljs-built_in">console</span>.log(baz.name) <span class="hljs-comment">// 'baz'</span>
<span class="hljs-built_in">console</span>.log((<span class="hljs-function">() =></span> &#123;&#125;).name) <span class="hljs-comment">// 空字符串</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>().name) <span class="hljs-comment">// 'anonymous'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果函数是一个<strong>获取函数</strong>、<strong>设置函数</strong>或<strong>使用<code>bind()</code>实例化</strong>，标识符前会加上一个<strong>前缀</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(foo.bind(<span class="hljs-literal">null</span>).name) <span class="hljs-comment">// 'bound foo' ，标识符前加前缀</span>
<span class="hljs-keyword">let</span> dog = &#123;
  <span class="hljs-attr">years</span>: <span class="hljs-number">1</span>,
  <span class="hljs-keyword">get</span> <span class="hljs-title">age</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.years
  &#125;,
  <span class="hljs-keyword">set</span> <span class="hljs-title">age</span>(<span class="hljs-params">newAge</span>) &#123;
    <span class="hljs-built_in">this</span>.years = newAge
  &#125;,
&#125;
<span class="hljs-keyword">let</span> propertyDescriptor = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(dog, <span class="hljs-string">'age'</span>) <span class="hljs-comment">// 获取属性描述符</span>
<span class="hljs-built_in">console</span>.log(propertyDescriptor) <span class="hljs-comment">// &#123; get: [Function: get age], set: [Function: set age], enumerable: true, configurable: true &#125;</span>
<span class="hljs-built_in">console</span>.log(propertyDescriptor.get.name) <span class="hljs-comment">// 'get age'，标识符前加前缀</span>
<span class="hljs-built_in">console</span>.log(propertyDescriptor.set.name) <span class="hljs-comment">// 'set age'，标识符前加前缀</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">10.3 理解参数</h1>
<ul>
<li>JS 函数<strong>不关心</strong>传入的<strong>参数个数</strong>和<strong>数据类型</strong></li>
<li>可在<strong>非箭头函数</strong>内部访问<code>arguments</code><strong>类数组</strong>对象，取得每个参数（如<code>arguments[0]</code>）</li>
<li>JS 函数的命名参数在调用时<strong>不用必须匹配函数签名</strong>，不存在验证命名参数的机制</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params">name, message</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;name&#125;</span>, <span class="hljs-subst">$&#123;message&#125;</span>`</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi2</span>(<span class="hljs-params">name, message</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]&#125;</span>`</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi3</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 没有命名参数</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]&#125;</span>`</span>)
&#125;
sayHi(<span class="hljs-string">'Jake'</span>, <span class="hljs-string">'How are you'</span>) <span class="hljs-comment">// 'Hello Jake, How are you'</span>
sayHi2(<span class="hljs-string">'Jake'</span>, <span class="hljs-string">'How are you'</span>) <span class="hljs-comment">// 'Hello Jake, How are you'</span>
sayHi3(<span class="hljs-string">'Jake'</span>, <span class="hljs-string">'How are you'</span>) <span class="hljs-comment">// 'Hello Jake, How are you'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以通过<code>arguments.length</code>检查传入参数的个数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">howManyArgs</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length) <span class="hljs-comment">// 检查参数个数</span>
&#125;
howManyArgs(<span class="hljs-string">'string'</span>, <span class="hljs-number">45</span>) <span class="hljs-comment">// 2</span>
howManyArgs() <span class="hljs-comment">// 0</span>
howManyArgs(<span class="hljs-number">12</span>) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>arguments</code>对象可以跟命名参数一起使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doAdd</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-built_in">console</span>.log(num1 + <span class="hljs-number">10</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">2</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] + num2)
  &#125;
&#125;
doAdd(<span class="hljs-number">10</span>) <span class="hljs-comment">// 20，10+10</span>
doAdd(<span class="hljs-number">30</span>, <span class="hljs-number">20</span>) <span class="hljs-comment">// 50，30+20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>arguments</code>对象的值始终会与命名参数<strong>同步</strong>
<ul>
<li>在内存中中分开（非访问同一个地址），仅值同步</li>
<li>调用函数时未传的参数，不会因为<code>arguments</code>改变而改变（始终是 undefined）</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">args</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] = <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(num1, num2)
&#125;
args(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// 2 10</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">args2</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] = <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(num1, num2)
&#125;
args2(<span class="hljs-number">2</span>) <span class="hljs-comment">// 2 undefined，调用函数时只传入一个参数，修改arguments不会改变第二个命名参数，仍旧是undefined</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">args3</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  num1 = <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>], <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>])
&#125;
args3(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// 10 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>严格模式下，<code>arguments</code>会有一些变化：
<ul>
<li><code>arguments</code>对象的值与命名参数<strong>不再同步</strong>，修改<code>arguments</code>不再对命名参数产生影响</li>
<li>在函数中重写<code>arguments</code>对象会报错，代码也不会执行</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strictArgs</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
<span class="hljs-meta">  'use strict'</span>
  <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] = <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(num1, num2)
  <span class="hljs-comment">// arguments = [] // SyntaxError: Unexpected eval or arguments in strict mode，不能重写arguments</span>
&#125;
strictArgs(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// 2 3，arguments与命名参数不再同步</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>箭头函数</strong>不能访问<code>arguments</code>，只能访问命名参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> bar2 = <span class="hljs-function">(<span class="hljs-params">num1, num2</span>) =></span> &#123;
  <span class="hljs-comment">// console.log(arguments[0], arguments[1]) // Uncaught ReferenceError: arguments is not defined</span>
  <span class="hljs-built_in">console</span>.log(num1, num2)
&#125;
bar2(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// 2 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>JS 中的所有参数都是<strong>按值传递</strong>的，如果<strong>把对象作为参数传递，传递的值是这个对象的引用（仍是按值传递）</strong></li>
</ul>
<h1 data-id="heading-4">10.4 没有重载</h1>
<ul>
<li>JS 的函数<strong>没有签名</strong>，因此<strong>没有重载</strong>，后定义的同名函数会<strong>覆盖</strong>先定义的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addSomeNumber</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num + <span class="hljs-number">100</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addSomeNumber</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num + <span class="hljs-number">200</span>
&#125;
<span class="hljs-keyword">let</span> result = addSomeNumber(<span class="hljs-number">100</span>)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// 300</span>

<span class="hljs-comment">// 把函数名当成指针</span>
<span class="hljs-keyword">let</span> addSomeNumber2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num + <span class="hljs-number">100</span>
&#125;
addSomeNumber2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num + <span class="hljs-number">200</span>
&#125;
<span class="hljs-keyword">let</span> result2 = addSomeNumber2(<span class="hljs-number">100</span>)
<span class="hljs-built_in">console</span>.log(result2) <span class="hljs-comment">// 300</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">10.5 默认参数值</h1>
<ul>
<li>ES5 及以前，实现默认参数的常用方法是<strong>检测某个参数是否等于<code>undefined</code></strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing</span>(<span class="hljs-params">name</span>) </span>&#123;
  name = <span class="hljs-keyword">typeof</span> name !== <span class="hljs-string">'undefined'</span> ? name : <span class="hljs-string">'Henry'</span> <span class="hljs-comment">// 检测参数name是否为undefined，如果是则赋值</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> VIII`</span>
&#125;
<span class="hljs-built_in">console</span>.log(makeKing()) <span class="hljs-comment">// 'King Henry VIII'</span>
<span class="hljs-built_in">console</span>.log(makeKing(<span class="hljs-string">'James'</span>)) <span class="hljs-comment">// 'King James VIII'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES6 及以后支持<strong>显式定义默认参数</strong>，在<strong>函数定义中的参数后赋值</strong>即可</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing2</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> VIII`</span>
&#125;
<span class="hljs-built_in">console</span>.log(makeKing2()) <span class="hljs-comment">// 'King Henry VIII'</span>
<span class="hljs-built_in">console</span>.log(makeKing2(<span class="hljs-string">'James'</span>)) <span class="hljs-comment">// 'King James VIII'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用默认参数时，<code>arguments</code>对象<strong>不反映参数默认值，只反映传给函数的参数</strong>，修改命名参数不会影响<code>arguments</code>对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing3</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span></span>) </span>&#123;
  name = <span class="hljs-string">'Louis'</span> <span class="hljs-comment">// 修改命名参数</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]&#125;</span>`</span>
&#125;
<span class="hljs-built_in">console</span>.log(makeKing3()) <span class="hljs-comment">// 'King undefined'，传给函数的参数为undefined</span>
<span class="hljs-built_in">console</span>.log(makeKing3(<span class="hljs-string">'James'</span>)) <span class="hljs-comment">// 'King James'，传给函数的参数为'James'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以使用<strong>调用函数的返回值</strong>作为默认参数值，计算默认值的函数在<strong>未传相应参数</strong>时被调用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> romanNumerals = [<span class="hljs-string">'Ⅰ'</span>, <span class="hljs-string">'Ⅱ'</span>, <span class="hljs-string">'Ⅲ'</span>, <span class="hljs-string">'Ⅳ'</span>, <span class="hljs-string">'Ⅴ'</span>, <span class="hljs-string">'Ⅵ'</span>]
<span class="hljs-keyword">let</span> ordinality = <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNumerals</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> romanNumerals[ordinality++] <span class="hljs-comment">// 每次调用后递增</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing4</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span>, numerals = getNumerals()</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;
<span class="hljs-built_in">console</span>.log(makeKing4()) <span class="hljs-comment">// 'King Henry Ⅰ'，未传numerals参数，调用函数getNumerals()</span>
<span class="hljs-built_in">console</span>.log(makeKing4(<span class="hljs-string">'James'</span>, <span class="hljs-string">'Ⅸ'</span>)) <span class="hljs-comment">// 'King James Ⅸ'，已传numerals参数，不调用函数</span>
<span class="hljs-built_in">console</span>.log(makeKing4()) <span class="hljs-comment">// 'King Henry Ⅱ'，未传numerals参数，调用函数getNumerals()</span>
<span class="hljs-built_in">console</span>.log(makeKing4()) <span class="hljs-comment">// 'King Henry Ⅲ'，未传numerals参数，调用函数getNumerals()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>箭头函数</strong>同样可以使用默认参数，只有一个参数时不能省略括号</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> makeKing5 = <span class="hljs-function">(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span></span>) =></span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span>`</span>
<span class="hljs-built_in">console</span>.log(makeKing5()) <span class="hljs-comment">// 'King Henry'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">默认参数作用域与暂时性死区</h2>
<ul>
<li>给参数定义默认值，实际上相当于使用<code>let</code>关键字<strong>按顺序</strong>声明变量一样</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing6</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span>, numerals = <span class="hljs-string">'Ⅷ'</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;

<span class="hljs-comment">// 使用let按顺序声明变量</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing7</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> name = <span class="hljs-string">'Henry'</span>
  <span class="hljs-keyword">let</span> numerals = <span class="hljs-string">'Ⅷ'</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>后定义默认值</strong>的参数可以<strong>引用先定义的参数</strong>；反之会因为<strong>暂时性死区</strong>报错（<code>let</code>声明的变量<strong>不会在作用域中被提升</strong>）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing8</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span>, numerals = name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;
<span class="hljs-built_in">console</span>.log(makeKing8()) <span class="hljs-comment">// 'King Henry Henry'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing9</span>(<span class="hljs-params">name = numerals, numerals = <span class="hljs-string">'Ⅷ'</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;
<span class="hljs-comment">// console.log(makeKing9()) // ReferenceError: Cannot access 'numerals' before initialization</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>参数存在自己的作用域，<strong>不能</strong>引用函数体的作用域</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeKing10</span>(<span class="hljs-params">name = <span class="hljs-string">'Henry'</span>, numerals = defaultNumeral</span>) </span>&#123;
  <span class="hljs-keyword">let</span> defaultNumeral = <span class="hljs-string">'Ⅷ'</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`King <span class="hljs-subst">$&#123;name&#125;</span> <span class="hljs-subst">$&#123;numerals&#125;</span>`</span>
&#125;
<span class="hljs-comment">// console.log(makeKing10()) // ReferenceError: defaultNumeral is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">10.6 参数扩展与收集</h1>
<ul>
<li>ES6 新增<strong>扩展操作符<code>...</code></strong>，可以用于<strong>调用函数时传参</strong>和<strong>定义函数参数</strong></li>
</ul>
<h2 data-id="heading-8">10.6.1 扩展参数</h2>
<ul>
<li>可对<strong>可迭代对象</strong>应用扩展操作符并将其<strong>作为一个参数</strong>传入，会将可迭代对象<strong>拆分</strong>并传入迭代返回的<strong>每个值</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> values = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">arguments</span>.length; i++) &#123;
    sum += <span class="hljs-built_in">arguments</span>[i]
  &#125;
  <span class="hljs-keyword">return</span> sum
&#125;

<span class="hljs-built_in">console</span>.log(getSum(...values)) <span class="hljs-comment">// 10，1+2+3+4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可在扩展操作符<strong>前面</strong>、<strong>候面</strong>再传其他的值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(getSum(-<span class="hljs-number">1</span>, ...values)) <span class="hljs-comment">// 9，-1+1+2+3+4</span>
<span class="hljs-built_in">console</span>.log(getSum(...values, <span class="hljs-number">5</span>)) <span class="hljs-comment">// 15，1+2+3+4+5</span>
<span class="hljs-built_in">console</span>.log(getSum(-<span class="hljs-number">1</span>, ...values, <span class="hljs-number">5</span>)) <span class="hljs-comment">// 14，-1+1+2+3+4+5</span>
<span class="hljs-built_in">console</span>.log(getSum(...values, ...[<span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>])) <span class="hljs-comment">// 28，1+2+3+4+5+6+7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>arguments</code>对象仍按照调用函数时传入的参数接收每一个值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">countArgs</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length)
&#125;
countArgs(-<span class="hljs-number">1</span>, ...values) <span class="hljs-comment">// 5</span>
countArgs(...values, <span class="hljs-number">5</span>) <span class="hljs-comment">// 5</span>
countArgs(-<span class="hljs-number">1</span>, ...values, <span class="hljs-number">5</span>) <span class="hljs-comment">// 6</span>
countArgs(...values, ...[<span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>]) <span class="hljs-comment">// 7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用扩展操作符的同时，也可以使用默认参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProduct</span>(<span class="hljs-params">a, b, c = <span class="hljs-number">1</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> a * b * c
&#125;
<span class="hljs-built_in">console</span>.log(getProduct(...[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>])) <span class="hljs-comment">// 2，1*2*1</span>
<span class="hljs-built_in">console</span>.log(getProduct(...[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])) <span class="hljs-comment">// 6，1*2*3</span>
<span class="hljs-built_in">console</span>.log(getProduct(...[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>])) <span class="hljs-comment">// 6，1*2*3</span>

<span class="hljs-keyword">let</span> getSum2 = <span class="hljs-function">(<span class="hljs-params">a, b, c = <span class="hljs-number">0</span></span>) =></span> &#123;
  <span class="hljs-keyword">return</span> a + b + c
&#125;
<span class="hljs-built_in">console</span>.log(getSum2(...[<span class="hljs-number">0</span>, <span class="hljs-number">1</span>])) <span class="hljs-comment">// 1，0+1</span>
<span class="hljs-built_in">console</span>.log(getSum2(...[<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>])) <span class="hljs-comment">// 3，0+1+2</span>
<span class="hljs-built_in">console</span>.log(getSum2(...[<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])) <span class="hljs-comment">// 3，0+1+2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10.6.2 收集参数</h2>
<ul>
<li>可以使用扩展操作符把<strong>不同长度</strong>的独立参数组合为一个<strong>数组</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum3</span>(<span class="hljs-params">...values</span>) </span>&#123;
  <span class="hljs-keyword">return</span> values.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> pre + cur, <span class="hljs-number">0</span>)
&#125;
<span class="hljs-built_in">console</span>.log(getSum3(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)) <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>因为收集参数的结果可变，因此<strong>只能</strong>把它作为<strong>最后</strong>一个参数</li>
<li>收集参数的前面如果还有命名参数，则只收集<strong>其余</strong>参数；若<strong>没收集到</strong>则获得<strong>空数组</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProduct</span>(<span class="hljs-params">...values, lastValue</span>) </span>&#123;&#125; <span class="hljs-comment">// SyntaxError: Rest parameter must be last formal parameter</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ignoreFirst</span>(<span class="hljs-params">firstValue, ...values</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(values)
&#125;
ignoreFirst() <span class="hljs-comment">// []，没收集到</span>
ignoreFirst(<span class="hljs-number">1</span>) <span class="hljs-comment">// []，没收集到</span>
ignoreFirst(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// [2]，收集其余参数</span>
ignoreFirst(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// [2, 3]，收集其余参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>箭头函数<strong>支持</strong>收集参数的定义方式，可用其实现与使用<code>arguments</code>一样的逻辑</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> getSum4 = <span class="hljs-function">(<span class="hljs-params">...values</span>) =></span> values.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> pre + cur, <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(getSum4(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>)) <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>收集参数<strong>不影响</strong><code>arguments</code>对象，仍反映调用时传给函数的参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum5</span>(<span class="hljs-params">...values</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length) <span class="hljs-comment">// 4</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>) <span class="hljs-comment">// [Arguments] &#123; '0': 1, '1': 2, '2': 3, '3': 4 &#125;</span>
  <span class="hljs-built_in">console</span>.log(values) <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>
&#125;
getSum5(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">10.7 函数声明与函数表达式</h1>
<ul>
<li>js 引擎在代码开始执行之前，解析器通过<strong>函数声明提升（function declaration hoisting）<strong>的过程，将</strong>声明函数</strong>放到源代码树的顶部，使其<strong>在执行任何代码之前可用（可以访问）</strong>；而<strong>函数表达式</strong>则必须等到解析器执行到所在代码行才被解释执行。</li>
<li><strong>函数声明</strong>和<strong>函数表达式</strong>的唯一区别就是<strong>什么时候可以通过变量访问函数</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(sumDeclare(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>)) <span class="hljs-comment">// 函数声明会提前</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sumDeclare</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;

<span class="hljs-built_in">console</span>.log(sumExpression(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>)) <span class="hljs-comment">// 函数表达式不会提前，会报错，sumExpression is not a function</span>
<span class="hljs-keyword">let</span> sumExpression = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num1, num2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">10.8 函数作为值</h1>
<ul>
<li><strong>函数名</strong>在 ECMAScript 中是<strong>变量</strong>，函数即可作为另一个函数的<strong>参数</strong>，也可在一个函数中<strong>返回</strong>另一个函数</li>
<li>如果是<strong>访问函数指针</strong>而非调用函数，必须<strong>不带括号</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callSomeFunction</span>(<span class="hljs-params">someFunction, someArgument</span>) </span>&#123;
  <span class="hljs-keyword">return</span> someFunction(someArgument)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add10</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">return</span> num + <span class="hljs-number">10</span>
&#125;
<span class="hljs-keyword">let</span> result3 = callSomeFunction(add10, <span class="hljs-number">10</span>) <span class="hljs-comment">// 访问函数的指针而不是执行函数，add10不带括号</span>
<span class="hljs-built_in">console</span>.log(result3) <span class="hljs-comment">// 20</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getGreeting</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'Hello,'</span> + name <span class="hljs-comment">// Hello,Nicholas</span>
&#125;
<span class="hljs-keyword">let</span> result4 = callSomeFunction(getGreeting, <span class="hljs-string">'Nicholas'</span>) <span class="hljs-comment">// 访问函数的指针而不是执行函数，getGreeting不带括号</span>
<span class="hljs-built_in">console</span>.log(result4) <span class="hljs-comment">// 'Hello,Nicholas'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>根据数组对象的某个对象属性进行排序：定义一个根据属性名来<strong>创建比较函数的函数</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">arraySort</span>(<span class="hljs-params">key, sort</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (sort === <span class="hljs-string">'asc'</span> || sort === <span class="hljs-literal">undefined</span> || sort === <span class="hljs-string">''</span>) &#123;
      <span class="hljs-comment">// 正序：a[key] > b[key]</span>
      <span class="hljs-keyword">if</span> (a[key] > b[key]) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (a[key] < b[key]) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sort === <span class="hljs-string">'desc'</span>) &#123;
      <span class="hljs-comment">// 倒序：a[key] < b[key]</span>
      <span class="hljs-keyword">if</span> (a[key] < b[key]) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (a[key] > b[key]) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">var</span> userList = [
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Tony'</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">3</span> &#125;,
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Tom'</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">2</span> &#125;,
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">5</span> &#125;,
]
<span class="hljs-built_in">console</span>.log(userList.sort(arraySort(<span class="hljs-string">'id'</span>))) <span class="hljs-comment">// [&#123; name: 'Tom', id: 2 &#125;,&#123; name: 'Tony', id: 3 &#125;,&#123; name: 'Jack', id: 5 &#125;]，按 id 正序排列</span>
<span class="hljs-built_in">console</span>.log(userList.sort(arraySort(<span class="hljs-string">'id'</span>, <span class="hljs-string">'desc'</span>))) <span class="hljs-comment">// [&#123; name: 'Jack', id: 5 &#125;,&#123; name: 'Tony', id: 3 &#125;,&#123; name: 'Tom', id: 2 &#125;]，按 id 倒序排列</span>
<span class="hljs-built_in">console</span>.log(userList.sort(arraySort(<span class="hljs-string">'name'</span>))) <span class="hljs-comment">// [&#123; name: 'Jack', id: 5 &#125;,&#123; name: 'Tom', id: 2 &#125;,&#123; name: 'Tony', id: 3 &#125;]，按 name 正序排列</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">总结 & 问点</h1>
<ul>
<li>函数是什么？函数有哪几种定义方式？</li>
<li>箭头函数在什么情况下可以不用参数的括号？什么情况下可以不用函数体的大括号？</li>
<li>箭头函数为什么不能用作构造函数或定义原型方法？</li>
<li>函数名是什么？一个函数可以有多少函数名？如何获取函数标识符？</li>
<li>函数内部的 arguments 对象是什么？其使用有哪些特点和限制？</li>
<li>如何理解并证明 JS 的函数没有重载？</li>
<li>ES5 及之前、ES6 及之后，分别如何定义函数的默认参数？</li>
<li>arguments 对象与函数默认参数有什么关联？如何理解默认参数的作用域与暂时性死区？</li>
<li>扩展操作符有什么作用？定义参数时使用其对 arguments 有什么影响？</li>
<li>箭头函数如何实现与 arguments 一样的逻辑，获取每个参数？</li>
<li>函数声明与函数表达式有什么区别？</li>
<li>写一段代码，根据对象数组的某个对象属性进行排序，可根据参数决定排序属性及升/降序</li>
</ul></div>  
</div>
            