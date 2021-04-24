
---
title: '【FuckingJavaScript系列】数据类型，你真的掌握了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07787b046d41eb9df5164e77de9684~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 01:57:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07787b046d41eb9df5164e77de9684~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>工欲善其事，必先利其器。</p>
</blockquote>
<p>大家好，我是龙哈哈。一个 <code>Java</code>，<code>JavaScript</code> 两栖动物。<br>
本篇是<code>FuckingJavaScript</code>系列的第一篇，我们来一起回顾一下<code>数据类型</code>的相关知识。</p>
<blockquote>
<p>JavaScript 是一种 <code>弱类型</code> 或者叫 <code>动态</code> 语言，<code>函数式编程</code>和<code>面向对象编程</code>的混合产物。开发者不用提前声明变量的类型，在程序运行过程中，类型会被自动确定，同一个变量可以保存不同类型的数据。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> foo = <span class="hljs-number">42</span>;    <span class="hljs-comment">// foo is a Number now</span>
foo = <span class="hljs-string">"bar"</span>; <span class="hljs-comment">// foo is a String now</span>
foo = <span class="hljs-literal">true</span>;  <span class="hljs-comment">// foo is a Boolean now</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">数据类型</h1>
<p>最新的 <code>ECMAScript</code> 标准定义了 9 种数据类型，包括了<code>原始数据类型</code>，<code>复杂数据类型</code>。</p>
<h2 data-id="heading-2">原始数据类型</h2>
<ul>
<li><code>String</code></li>
<li><code>Boolean</code></li>
<li><code>Number</code></li>
<li><code>Undefined</code></li>
<li><code>Symbol</code></li>
<li><code>Bigint</code></li>
</ul>
<h3 data-id="heading-3">String</h3>
<p>字符串类型，用于表示文本数据。
JavaScript 字符串是不可更改的。这意味着字符串一旦被创建，就不能被修改。但是，可以基于对原始字符串的操作来创建新的字符串。</p>
<ul>
<li>字符串截取<code>String.substr()</code></li>
<li>字符串拼接<code>String.concat()</code></li>
</ul>
<h3 data-id="heading-4">Boolean</h3>
<p>布尔类型，只有两个值 <code>true</code> 和 <code>false</code>，用于表示逻辑真与假。</p>
<h3 data-id="heading-5">Number</h3>
<p>数字类型，有最大值(<code>Number.MAX_VALUE</code>)和最小值<code>(Number.MIN_VALUE</code>)限制，超出后会自动转换为特殊值 <code>Infinity</code>和<code>NaN(非数值，Not-a-Number)</code>。</p>
<h3 data-id="heading-6">Undefined</h3>
<p>只有一个值 <code>undefined</code>，JavaScript中，一个没有被赋值的变量会有个默认值 <code>undefined</code>。</p>
<h3 data-id="heading-7">Symbol</h3>
<p>符号类型，是<code>ES6</code>中新定义的原始数据类型，符号类型是<code>唯一</code>的并且<code>不可修改</code>，<code>不可枚举</code>。</p>
<ul>
<li>作为<code>Object</code>的<code>属性key</code>可以保证永远不会出现同名属性，防止属性污染</li>
<li>模拟<code>class</code>的<code>私有属性</code>，控制变量读写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> garen = <span class="hljs-built_in">Symbol</span>(); <span class="hljs-comment">// 盖伦标记</span>
<span class="hljs-keyword">const</span> jarvanIV = <span class="hljs-built_in">Symbol</span>(); <span class="hljs-comment">// 嘉文四世标记</span>
<span class="hljs-comment">// 德玛西亚类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">demacia</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>[garen] = <span class="hljs-string">'Garen'</span>;
    <span class="hljs-built_in">this</span>[jarvanIV] = <span class="hljs-string">'JarvanIV'</span>;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getGaren</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[garen];
  &#125;
  <span class="hljs-function"><span class="hljs-title">setGaren</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-built_in">this</span>[garen] = value;
  &#125;
  <span class="hljs-function"><span class="hljs-title">getJarvanIV</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[jarvanIV];
  &#125;
  <span class="hljs-function"><span class="hljs-title">setJarvanIV</span>(<span class="hljs-params">value</span>)</span>&#123;
    <span class="hljs-built_in">this</span>[jarvanIV] = value;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Bigint</h3>
<p>字如其意，<code>ES11</code>新增加的数据类型类型，可以通过在整数末尾附加 <code>n</code> 创建，<code>BigInt</code>可以安全地存储和操作大整数，甚至可以超过数字的安全整数限制。</p>
<h2 data-id="heading-9">复杂数据类型</h2>
<ul>
<li><code>Null</code></li>
<li><code>Object</code></li>
<li><code>Function</code></li>
</ul>
<h3 data-id="heading-10">Null</h3>
<p>Null类型只有一个值 <code>null</code>，<code>typeof null</code> 值为 <code>object</code>。</p>
<h3 data-id="heading-11">Object</h3>
<p>对象类型，几乎所有可以通过 <code>new Keyword</code> 创建的，类型都是 <code>Object</code>，例如 <code>new Array()</code>、<code>new Date()</code>、<code>new Map()</code>、<code>new Set()</code>、<code>new WeekMap()</code>, <code>new WeekSet()</code> 等。</p>
<h3 data-id="heading-12">Function</h3>
<p><code>Function</code> 是一个特殊的 <code>Obejct</code>，<code>Function</code> 的原型对象 <code>prototype</code> 的原型 <code>__proto__</code> 指向 <code>Object</code>(有点绕口，关于原型对象和原型，在后续说到<code>原型编程</code>时会讲)</p>
<h3 data-id="heading-13">Array</h3>
<p>数组类型，常用于表示列表数据<br>
数组的方法可总结为三类</p>
<ul>
<li>会改变调用它们的对象自身的值，<code>pop</code>、<code>push</code>、<code>reverse</code>、<code>splice</code>等</li>
<li>不会改变调用它们的对象的值，只会返回一个新的数组，<code>concat</code>，<code>slice</code>，<code>join</code>等</li>
<li>遍历方法，遍历过程中，不要对原数组进行任何操作，否则遍历结果可能会受影响，<code>foEach</code>，<code>entries</code>，<code>every</code>，<code>some</code>，<code>filter</code>，<code>find</code>等</li>
</ul>
<p>不同方法的具体用法这里就不一一说明了。</p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array" target="_blank" rel="nofollow noopener noreferrer">参考资料【MDN】数组Array</a></p>
<h3 data-id="heading-14">Date</h3>
<p>日期类型，基于 <code>Unix Time</code>，即自 <code>1970年1月1日（UTC）</code> 起经过的 <code>毫秒数</code>。</p>
<h3 data-id="heading-15">Set，WeakSet，Map，WeakMap</h3>
<ul>
<li>Map：键值对，并且能够记住键的原始插入顺序。任何值都可以作为一个键或一个值</li>
<li>WeakMap：键必须是对象，而值可以是任意的，不可枚举，键名所指向的对象，都是弱引用，不计入垃圾回收机制</li>
<li>Set：任意值的集合，你可以按照插入的顺序迭代它的元素。 Set中的元素<strong>只会出现一次</strong>，即 Set 中的元素是唯一的。</li>
<li>WeakSet：对象值的集合，不可枚举，对象都是弱引用，不计入垃圾回收机制</li>
</ul>
<h2 data-id="heading-16">不同数据类型的储存</h2>
<p>JavaScript的 <code>堆栈</code>和 Java 有些许差别</p>
<ul>
<li>栈：原始类型的局部变量，对象的引用</li>
<li>堆：原始类型的全局变量，闭包场景中的变量, 对象类型数据</li>
</ul>
<p>解释：下图中 <code>闭包函数</code> 的 <code>原始类型</code>的 <code>变量b</code> 还存在于<code>[[Scopes]]</code>对象中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> f1 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">console</span>.log(b) &#125;
&#125;
<span class="hljs-built_in">console</span>.dir(f1())
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07787b046d41eb9df5164e77de9684~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-17">类型判断</h1>
<h2 data-id="heading-18">typeof</h2>
<p>检测一个变量的类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-string">'1'</span> <span class="hljs-comment">// string</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-number">1</span> <span class="hljs-comment">// number</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-number">1n</span> <span class="hljs-comment">// bigint</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-literal">false</span> <span class="hljs-comment">// boolean</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span> <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span> <span class="hljs-comment">// object</span>

<span class="hljs-keyword">typeof</span> [] <span class="hljs-comment">// object</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() <span class="hljs-comment">// object</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// function</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Date</span> <span class="hljs-comment">// function</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Array</span> <span class="hljs-comment">// function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>typeof null</code> 的值为 <code>object</code></p>
<blockquote>
<p>这是个历史遗留的 <code>Bug</code>，娘胎里带出来的</p>
</blockquote>
<p>不同的对象在底层都表示为二进制，在<code>JavacSript</code>中<code>二进制前三位</code>都为<code>0</code>的话会被判断为是<code>Object</code>，<code>null</code> 的二进制表示全为<code>0</code>，自然前三位也是<code>0</code>，所以执行 <code>typeof</code> 时会返回 <code>object</code><br>
判断 <code>null</code> 类型，建议用 <code>xxx=== null</code><br>
对于复杂类型的数据来说，函数的类型为 <code>function</code>，对象的类型为 <code>object</code></p>
<h2 data-id="heading-19">instanceof</h2>
<p>返回true/false，用于检测构造函数的 prototype 是否出现在实例对象的 原型链 上，从而判断对象类型。</p>
<h3 data-id="heading-20">如何手动实现 instanceof</h3>
<p><code>instanceof</code> 可以正确的判断对象的类型，原理是通过判断对象的原型链中能不能找到对应的类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123;
  <span class="hljs-comment">// 原型</span>
  <span class="hljs-keyword">let</span> proto = left.__proto__;
  <span class="hljs-comment">// 一层一层找对应的原型对象</span>
  <span class="hljs-keyword">while</span>(proto) &#123;
    <span class="hljs-keyword">if</span> (proto === right.prototype) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    proto = proto.__proto__
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">Object.prototype.toString</h2>
<p>个人比较推荐的判断类型的方法是<code>Object.prototype.toString</code>，可以完整的判断数据的类型，需要搭配 <code>call</code> 或者 <code>apply</code> 使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">'1'</span>) <span class="hljs-comment">// [object String]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>) <span class="hljs-comment">// [object Number]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1n</span>) <span class="hljs-comment">// [object BigInt]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">false</span>) <span class="hljs-comment">// [object Boolean]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// [object Undefined]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">null</span>) <span class="hljs-comment">// [object Null]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(&#123;&#125;) <span class="hljs-comment">// [object Object]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call([]) <span class="hljs-comment">// [object Array]</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// [object Date]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回值<code>[object &#123;type&#125;]</code> 中的 <code>type</code> 就是变量的类型</p>
<h1 data-id="heading-22">类型转换</h1>
<ul>
<li>强制转换</li>
<li>隐式转换</li>
</ul>
<h2 data-id="heading-23">强制转换</h2>
<p>通过 String()，Number()，Boolean()等函数做类型转换</p>
<h2 data-id="heading-24">隐式转换</h2>
<p>类型转换中，编译器自动转换的方式，通常发生在通过运算符运算时</p>
<ul>
<li>算术运算符 <code>+</code>，<code>-</code>，<code>*</code>，<code>÷</code>，<code>%</code>等</li>
<li><code>==</code>，<code>!=</code></li>
<li>条件运算 <code>if( )</code>，<code>else if( )</code>等</li>
</ul>
<h3 data-id="heading-25">算术运算符</h3>
<ul>
<li>字符串 <code>+</code> 数字,数字会转成字符串</li>
<li>数字 <code>-</code> 字符串，字符串会转成数字。如果<code>字符串不是纯数字</code>就会转成<code>NaN</code>。字符串-数字也一样。字符串-字符串也要先转成数字</li>
<li><code>+</code>，<code>*</code>，<code>÷</code>，<code>%</code>，<code>></code>，<code><</code> 和 <code>-</code> 的转换也是一样</li>
</ul>
<h3 data-id="heading-26">==，!=</h3>
<p>先自动做<code>类型转换</code>，再<code>比较</code></p>
<ul>
<li>字符串和数字比时，会将字符串转为数字，再比较</li>
<li>字符串和布尔比时，都转为数字，再比较</li>
<li>数字和布尔比时，会将布尔转为数字，再比较</li>
</ul>
<h3 data-id="heading-27">条件运算</h3>
<p>将条件内<code>数据或表达式</code>转换为 <code>Boolean</code></p>
<h3 data-id="heading-28">转换例子</h3>
<h4 data-id="heading-29">转Number</h4>
<ul>
<li><code>true</code> 为 1，<code>false</code> 为 0</li>
<li><code>null</code> 为 0，<code>undefined</code> 为 <code>NaN</code>，<code>symbol</code> 报错</li>
<li>字符串看内容，如果是数字或者进制值就正常转，否则就 <code>NaN</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">true</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">false</span>) <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'1'</span>)) <span class="hljs-comment">// Uncaught TypeError: Cannot convert a Symbol value to a number at Number</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">'1'</span>)  <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">'1a'</span>) <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'1'</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'1.23 abc'</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">parseFloat</span>(<span class="hljs-string">'1.1'</span>) <span class="hljs-comment">// 1.2</span>
<span class="hljs-built_in">parseFloat</span>(<span class="hljs-string">'1.1 abc'</span>) <span class="hljs-comment">// 1.1</span>
+<span class="hljs-string">'1'</span>  <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">转String</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>(<span class="hljs-number">1</span>) <span class="hljs-comment">// '1'</span>
<span class="hljs-number">1.</span>toString() <span class="hljs-comment">// '1'</span>
<span class="hljs-number">1.234</span>.toFixed(<span class="hljs-string">'2'</span>) <span class="hljs-comment">// '1.23'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">转Boolean</h4>
<ul>
<li><code>undefined</code>、<code>null</code>、<code>false</code>、<code>0</code>、<code>-0</code>、<code>NaN</code>、<code>空字符串</code> 转为 <code>false</code></li>
<li>其他所有值都转为 <code>true</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(<span class="hljs-number">0</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(<span class="hljs-string">''</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(<span class="hljs-string">'0'</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">NaN</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(&#123; <span class="hljs-attr">a</span>: <span class="hljs-literal">null</span> &#125;) <span class="hljs-comment">// `true`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-32">相等性判断</h1>
<ul>
<li>非严格相等比较 (<code>==</code>)</li>
<li>严格相等比较 (<code>===</code>)</li>
<li><code>Object.is(args1，args2)</code></li>
</ul>
<h2 data-id="heading-33">区别</h2>
<ul>
<li><code>==</code>将执行类型转换后，比较值</li>
<li><code>===</code>直接进行相同的比较，而不进行类型转换 (如果类型不同, 总会返回 false )</li>
<li><code>Object.is</code> 与 <code>===</code> 处理类似，但是对<code>NaN</code>、<code>0</code>、<code>-0</code>进行特殊处理，<code>Object.is(NaN，NaN)</code>结果为<code>true</code>，<code>Object.is(0. -0)</code> 结果为 <code>false</code></li>
</ul>
<h1 data-id="heading-34">参考资料</h1>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Data_structures" target="_blank" rel="nofollow noopener noreferrer">【MDN】JavaScript 数据类型和数据结构</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Equality_comparisons_and_sameness" target="_blank" rel="nofollow noopener noreferrer">【MDN】JavaScript相等性判断</a></li>
</ul>
<h1 data-id="heading-35">最后</h1>
<blockquote>
<p>三人行，必有我师焉<br>
掘金不停，代码不止<br>
互相学习，共同进步</p>
</blockquote>
<p>文中如有错误，欢迎在评论区指正。<br>
如果这篇文章对你有所帮助，欢迎点赞、评论和关注。</p>
<h1 data-id="heading-36">系列文章</h1>
<ul>
<li><a href="https://juejin.cn/post/6954365339320713223" target="_blank">【FuckingJavaScript系列】数据类型，你真的掌握了吗？</a></li>
<li>【FuckingJavaScript系列】原型编程，你真的理解了吗？</li>
<li>【FuckingJavaScript系列】函数编程，你真的熟练了吗？</li>
<li>【FuckingJavaScript系列】异步编程，你真的学会了吗？</li>
<li>【FuckingJavaScript系列】事件循环，你真的明白了吗？</li>
</ul></div>  
</div>
            