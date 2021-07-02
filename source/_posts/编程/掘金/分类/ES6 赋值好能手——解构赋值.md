
---
title: 'ES6 赋值好能手——解构赋值'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf394c7988f4b25bbd7d7280cbc8f1d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 07:47:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf394c7988f4b25bbd7d7280cbc8f1d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ES6 赋值好能手——解构赋值</h2>

<p><strong>博客说明</strong></p>
<blockquote>
<p>文章所涉及的资料来自互联网整理和个人总结，意在于个人学习和经验汇总，如有什么地方侵权，请联系本人删除，谢谢！</p>
</blockquote>
<h4 data-id="heading-1">简介</h4>
<p><code>ES6</code> 允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构（Destructuring）。</p>
<p>有了这个操作之后，赋值的操作会更加的简洁和实用，解构赋值其实属于<code>模式匹配</code>，只要等号两边的模式相同，左边的变量就会被赋予对应的值。</p>
<h4 data-id="heading-2">数组的解构</h4>
<p>可以从数组中提取值，按照对应位置，对变量进行赋值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 以前</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
<span class="hljs-keyword">let</span> c = <span class="hljs-number">3</span>;


<span class="hljs-comment">// ES6 允许写成下面这样。</span>
<span class="hljs-keyword">let</span> [a, b, c] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以进行嵌套，还有完全解构和非完全解构，即等号左边的模式，只匹配一部分的等号右边的数组。这种情况下，解构依然可以成功。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [aa, [[bb], cc]] = [<span class="hljs-number">1</span>, [[<span class="hljs-number">2</span>], <span class="hljs-number">3</span>]];
aa <span class="hljs-comment">// 1</span>
bb <span class="hljs-comment">// 2</span>
cc <span class="hljs-comment">// 3</span>

<span class="hljs-keyword">let</span> [ , , third] = [<span class="hljs-string">"aa"</span>, <span class="hljs-string">"bb"</span>, <span class="hljs-string">"cc"</span>];
third <span class="hljs-comment">// "cc"</span>

<span class="hljs-keyword">let</span> [x, , y] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
x <span class="hljs-comment">// 1</span>
y <span class="hljs-comment">// 3</span>

<span class="hljs-keyword">let</span> [head, ...tail] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
head <span class="hljs-comment">// 1</span>
tail <span class="hljs-comment">// [2, 3, 4]</span>

<span class="hljs-keyword">let</span> [x, y, ...z] = [<span class="hljs-string">'a'</span>];
x <span class="hljs-comment">// "a"</span>
y <span class="hljs-comment">// undefined</span>
z <span class="hljs-comment">// []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果解构不成功，变量的值就等于<code>undefined</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [foo] = [];
<span class="hljs-keyword">let</span> [bar, foo] = [<span class="hljs-number">1</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">报错情况</h5>
<p>如果等号的右边不是数组（不是可遍历的结构），那么将会报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [foo] = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> [foo] = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">let</span> [foo] = <span class="hljs-literal">NaN</span>;
<span class="hljs-keyword">let</span> [foo] = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">let</span> [foo] = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> [foo] = &#123;&#125;;
<span class="hljs-comment">// 都会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">Set也可以使用解构赋值</h5>
<p>对于 Set 结构具有 Iterator 接口，也可以使用数组的解构赋值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [x, y, z] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>]);
x <span class="hljs-comment">// "a"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">默认值</h5>
<p>解构赋值允许指定默认值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [foo = <span class="hljs-literal">true</span>] = [];
foo <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> [x, y = <span class="hljs-string">'b'</span>] = [<span class="hljs-string">'a'</span>]; <span class="hljs-comment">// x='a', y='b'</span>
<span class="hljs-keyword">let</span> [x, y = <span class="hljs-string">'b'</span>] = [<span class="hljs-string">'a'</span>, <span class="hljs-literal">undefined</span>]; <span class="hljs-comment">// x='a', y='b'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>null</code>的使用，在ES6 内部使用严格相等运算符（<code>===</code>），判断一个位置是否有值。所以，只有当一个数组成员严格等于<code>undefined</code>，默认值才会生效。因为<code>null</code>不严格等于<code>undefined</code>，所以给<code>null</code>设置默认值依然是<code>null</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [x = <span class="hljs-number">1</span>] = [<span class="hljs-literal">undefined</span>];
x <span class="hljs-comment">// 1</span>

<span class="hljs-keyword">let</span> [x = <span class="hljs-number">1</span>] = [<span class="hljs-literal">null</span>];
x <span class="hljs-comment">// null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">对象的解构赋值</h4>
<p>对象的解构与数组有一个重要的不同。数组的元素是按次序排列的，变量的取值由它的位置决定；而对象的属性没有次序，变量必须与属性同名，才能取到正确的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; bar, foo &#125; = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'aaa'</span>, <span class="hljs-attr">bar</span>: <span class="hljs-string">'bbb'</span> &#125;;
foo <span class="hljs-comment">// "aaa"</span>
bar <span class="hljs-comment">// "bbb"</span>

<span class="hljs-keyword">let</span> &#123; baz &#125; = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'aaa'</span>, <span class="hljs-attr">bar</span>: <span class="hljs-string">'bbb'</span> &#125;;
baz <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果解构失败，变量的值等于<code>undefined</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123;foo&#125; = &#123;<span class="hljs-attr">bar</span>: <span class="hljs-string">'baz'</span>&#125;;
foo <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">获取对象的方法</h5>
<p>对象的解构赋值，可以很方便地将现有对象的方法，赋值到某个变量。将<code>console.log</code>赋值到<code>log</code>变量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; log &#125; = <span class="hljs-built_in">console</span>;
log(<span class="hljs-string">'hello'</span>) <span class="hljs-comment">// hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">模式与变量</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">foo</span>: baz &#125; = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'aaa'</span>, <span class="hljs-attr">bar</span>: <span class="hljs-string">'bbb'</span> &#125;;
baz <span class="hljs-comment">// "aaa"</span>
foo <span class="hljs-comment">// error: foo is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析上面代码，<code>foo</code>是匹配的模式，<code>baz</code>才是变量。真正被赋值的是变量<code>baz</code>，而不是模式<code>foo</code>，所以在使用的时候用<code>baz</code>.</p>
<h5 data-id="heading-9">对象的解构赋值可继承</h5>
<p>注意，对象的解构赋值可以取到继承的属性。下面的代码中，对象<code>obj1</code>的原型对象是<code>obj2</code>。<code>foo</code>属性不是<code>obj1</code>自身的属性，而是继承自<code>obj2</code>的属性，解构赋值可以取到这个属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj1 = &#123;&#125;;
<span class="hljs-keyword">const</span> obj2 = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span> &#125;;
<span class="hljs-built_in">Object</span>.setPrototypeOf(obj1, obj2);

<span class="hljs-keyword">const</span> &#123; foo &#125; = obj1;
foo <span class="hljs-comment">// "bar"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">对象解构赋值需要注意的几点</h5>
<p>1、已经声明的变量使用解构赋值。</p>
<p>在直接使用<code>&#123;x&#125;</code>时，<code>&#123;x&#125;</code>会被理解成一个代码块，从而发生语法错误。将整个解构赋值语句，放在一个圆括号里面，就可以正确执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> x;
&#123;x&#125; = &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;;
<span class="hljs-comment">// SyntaxError: syntax error</span>

<span class="hljs-comment">// 正确的写法</span>
<span class="hljs-keyword">let</span> x;
(&#123;x&#125; = &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、由于数组本质是特殊的对象，因此可以对数组进行对象属性的解构。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">let</span> &#123;<span class="hljs-number">0</span> : first, [arr.length - <span class="hljs-number">1</span>] : last&#125; = arr;
first <span class="hljs-comment">// 1</span>
last <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">字符串的解构赋值</h4>
<p>字符串也可以解构赋值。这是因为此时，字符串被转换成了一个类似数组的对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> [a, b, c, d, e] = <span class="hljs-string">'hello'</span>;
a <span class="hljs-comment">// "h"</span>
b <span class="hljs-comment">// "e"</span>
c <span class="hljs-comment">// "l"</span>
d <span class="hljs-comment">// "l"</span>
e <span class="hljs-comment">// "o"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似数组的对象都有一个<code>length</code>属性，因此还可以对这个属性解构赋值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">length</span> : len&#125; = <span class="hljs-string">'hello'</span>;
len <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">数值和布尔值的解构赋值</h4>
<p>解构赋值时，如果等号右边是数值和布尔值，则会先转为对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">toString</span>: s&#125; = <span class="hljs-number">123</span>;
s === <span class="hljs-built_in">Number</span>.prototype.toString <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">toString</span>: s&#125; = <span class="hljs-literal">true</span>;
s === <span class="hljs-built_in">Boolean</span>.prototype.toString <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，数值和布尔值的包装对象都有<code>toString</code>属性，因此变量<code>s</code>都能取到值。</p>
<h5 data-id="heading-13">解构赋值的规则</h5>
<p>解构赋值的规则是，只要等号右边的值不是对象或数组，就先将其转为对象。由于<code>undefined</code>和<code>null</code>无法转为对象，所以对它们进行解构赋值，都会报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">prop</span>: x &#125; = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// TypeError</span>
<span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">prop</span>: y &#125; = <span class="hljs-literal">null</span>; <span class="hljs-comment">// TypeError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">函数参数的解构赋值</h4>
<p>函数的参数也可以使用解构赋值。在函数<code>add</code>的参数是一个数组，但在传入参数的时候，数组参数就被解构成变量<code>x</code>和<code>y</code>，在函数内部就可以直接使用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">[x, y]</span>)</span>&#123;
  <span class="hljs-keyword">return</span> x + y;
&#125;

add([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">圆括号问题</h4>
<p>解构赋值虽然很方便，但是解析起来并不容易。对于编译器来说，一个式子到底是模式，还是表达式，没有办法从一开始就知道，必须解析到（或解析不到）等号才能知道。</p>
<p>由此带来的问题是，如果模式中出现圆括号怎么处理。ES6 的规则是，只要有可能导致解构的歧义，就不得使用圆括号。</p>
<h5 data-id="heading-16">不能使用圆括号的情况</h5>
<p>1、变量声明语句</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [(a)] = [<span class="hljs-number">1</span>];

<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">x</span>: (c)&#125; = &#123;&#125;;
<span class="hljs-keyword">let</span> (&#123;<span class="hljs-attr">x</span>: c&#125;) = &#123;&#125;;
<span class="hljs-keyword">let</span> &#123;(x: c)&#125; = &#123;&#125;;
<span class="hljs-keyword">let</span> &#123;(x): c&#125; = &#123;&#125;;

<span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">o</span>: (&#123; <span class="hljs-attr">p</span>: p &#125;) &#125; = &#123; <span class="hljs-attr">o</span>: &#123; <span class="hljs-attr">p</span>: <span class="hljs-number">2</span> &#125; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、函数参数</p>
<p>函数参数也属于变量声明，因此不能带有圆括号。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">[(z)]</span>) </span>&#123; <span class="hljs-keyword">return</span> z; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">[z,(x)]</span>) </span>&#123; <span class="hljs-keyword">return</span> x; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、赋值语句的模式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(&#123; <span class="hljs-attr">p</span>: a &#125;) = &#123; <span class="hljs-attr">p</span>: <span class="hljs-number">42</span> &#125;;
([a]) = [<span class="hljs-number">5</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">可以使用圆括号的情况</h5>
<p>可以使用圆括号的情况只有一种：赋值语句的非模式部分，可以使用圆括号。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[(b)] = [<span class="hljs-number">3</span>]; <span class="hljs-comment">// 正确</span>
(&#123; <span class="hljs-attr">p</span>: (d) &#125; = &#123;&#125;); <span class="hljs-comment">// 正确</span>
[(<span class="hljs-built_in">parseInt</span>.prop)] = [<span class="hljs-number">3</span>]; <span class="hljs-comment">// 正确</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">解构赋值用途</h4>
<p>变量的解构赋值在实际开发中用途十分之多</p>
<h5 data-id="heading-19">交换变量的值</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> y = <span class="hljs-number">2</span>;

[x, y] = [y, x];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码交换变量<code>x</code>和<code>y</code>的值，这样的写法不仅简洁，而且易读，语义非常清晰。</p>
<h5 data-id="heading-20">从函数返回多个值</h5>
<p>函数只能返回一个值，如果要返回多个值，只能将它们放在数组或对象里返回。有了解构赋值，取出这些值就非常方便。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 返回一个数组</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
&#125;
<span class="hljs-keyword">let</span> [a, b, c] = example();

<span class="hljs-comment">// 返回一个对象</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">aa</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">bb</span>: <span class="hljs-number">2</span>
  &#125;;
&#125;
<span class="hljs-keyword">let</span> &#123; aa, bb &#125; = example();
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">函数参数的定义</h5>
<p>解构赋值可以方便地将一组参数与变量名对应起来。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 参数是一组有次序的值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">[x, y, z]</span>) </span>&#123; ... &#125;
f([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);

<span class="hljs-comment">// 参数是一组无次序的值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">&#123;x, y, z&#125;</span>) </span>&#123; ... &#125;
f(&#123;<span class="hljs-attr">z</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">取 JSON 数据</h5>
<p>解构赋值对提取 JSON 对象中的数据，这在获取请求数据中使用很广。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> jsonData = &#123;
  <span class="hljs-attr">code</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">status</span>: <span class="hljs-string">"OK"</span>,
  <span class="hljs-attr">data</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]
&#125;;

<span class="hljs-keyword">let</span> &#123; code, status, <span class="hljs-attr">data</span>: number &#125; = jsonData;

<span class="hljs-built_in">console</span>.log(id, status, number);
<span class="hljs-comment">// 200, "OK", [1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">函数参数的默认值</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">jQuery.ajax = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">url, &#123;
  <span class="hljs-keyword">async</span> = <span class="hljs-literal">true</span>,
  beforeSend = <span class="hljs-keyword">function</span> () &#123;&#125;,
  cache = <span class="hljs-literal">true</span>,
  complete = <span class="hljs-keyword">function</span> () &#123;&#125;,
  crossDomain = <span class="hljs-literal">false</span>,
  <span class="hljs-built_in">global</span> = <span class="hljs-literal">true</span>,
  <span class="hljs-regexp">//</span> ... more config
&#125; = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// ... do stuff</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>指定参数的默认值，就避免了在函数体内部再写<code>var foo = config.foo || 'default foo';</code>这样的语句。</p>
<h5 data-id="heading-24">遍历 Map 结构</h5>
<p>任何部署了 Iterator 接口的对象，都可以用<code>for...of</code>循环遍历。Map 结构原生支持 Iterator 接口，配合变量的解构赋值，获取键名和键值就非常方便。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'first'</span>, <span class="hljs-string">'hello'</span>);
map.set(<span class="hljs-string">'second'</span>, <span class="hljs-string">'world'</span>);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> map) &#123;
  <span class="hljs-built_in">console</span>.log(key + <span class="hljs-string">" is "</span> + value);
&#125;
<span class="hljs-comment">// first is hello</span>
<span class="hljs-comment">// second is world</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果只想获取键名，或者只想获取键值，可以写成下面这样。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取键名</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key] <span class="hljs-keyword">of</span> map) &#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-comment">// 获取键值</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [,value] <span class="hljs-keyword">of</span> map) &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">输入模块的指定方法</h5>
<p>加载模块时，往往需要指定输入哪些方法。解构赋值使得输入语句非常清晰。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; SourceMapConsumer, SourceNode &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"source-map"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>感谢</strong></p>
<blockquote>
<p>万能的网络</p>
<p>菜鸟教程</p>
<p>阮一峰的es6语法教程</p>
<p>以及勤劳的自己，<a href="https://blog.guizimo.top/" target="_blank" rel="nofollow noopener noreferrer">个人博客</a>，<a href="https://tangleia.github.io/" target="_blank" rel="nofollow noopener noreferrer">GitHub</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf394c7988f4b25bbd7d7280cbc8f1d~tplv-k3u1fbpfcp-zoom-1.image" alt="微信公众号" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            