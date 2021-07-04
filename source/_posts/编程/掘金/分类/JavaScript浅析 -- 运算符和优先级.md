
---
title: 'JavaScript浅析 -- 运算符和优先级'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4402'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:23:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=4402'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先上几道题，如果都能做出来且理解了下面内容可以不看，如果做不出来可以文章中可以找到答案。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以下输出结果是啥？</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>+<span class="hljs-string">'3'</span>++<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">2</span>*<span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> (<span class="hljs-number">2</span>*<span class="hljs-number">3</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">2</span>+<span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> + <span class="hljs-literal">false</span>);
<span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>] + [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>]);
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>, <span class="hljs-number">6</span>, <span class="hljs-number">6</span>);
<span class="hljs-built_in">console</span>.log(+!![]);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span> - - <span class="hljs-string">' '</span>);
<span class="hljs-built_in">console</span>.log(!<span class="hljs-number">6</span> + !<span class="hljs-number">6</span>);
<span class="hljs-built_in">console</span>.log([] + []);
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>/<span class="hljs-number">0</span>, <span class="hljs-number">1</span>/<span class="hljs-number">0</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> + (<span class="hljs-string">'true'</span> - <span class="hljs-number">0</span>));

<span class="hljs-keyword">var</span> a=<span class="hljs-number">0</span>, b=<span class="hljs-number">0</span>;
<span class="hljs-built_in">console</span>.log(a+++b, a, b);

<span class="hljs-keyword">var</span> arr, arr2;
arr2 = arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
arr[arr.length] = arr = <span class="hljs-number">4</span>;
<span class="hljs-built_in">console</span>.log(arr);
<span class="hljs-built_in">console</span>.log(arr2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看了这些题，曾经我以为运算符其实很简单，但实际上组合起来并不简单。虽然平时不建议写这样的代码，但可以借此机会我们再学习下运算符。</p>
<h3 data-id="heading-0">一、运算符</h3>
<p>JavaScript中的运算符，主要用于连接简单表达式，组成一个复杂的表达式。<strong>在运算过程中，会根据需要将操作数转换成特定的类型进行运算，最后输出指定的类型</strong>。我个人习惯将他分为6大类进行记忆：算术运算符，比较运算符，布尔运算符，赋值运算符，位运算符，其他运算符。</p>
<h5 data-id="heading-1">（一）算术运算符（10个）</h5>
<ul>
<li>加法运算符（Addition）：x + y</li>
<li>减法运算符（Subtraction）： x - y</li>
<li>乘法运算符（Multiplication）： x * y</li>
<li>除法运算符（Division）：x / y</li>
<li>余数运算符（Remainder）：x % y</li>
<li>自增运算符（Increment）：++x 或者 x++</li>
<li>自减运算符（Decrement）：--x 或者 x--</li>
<li>求负运算符（Negate）：-x</li>
<li>数值运算符（Convert to number）： +x</li>
<li>指数运算符 （Exponential operator） ： x**y ，如2**4=16</li>
</ul>
<p>说明：</p>
<ol>
<li>x++先参与运算然后x再做加一操作。如<code>console.log(2 - a++)</code>相当于<code>console.log(2-a); a = a+1;</code>++x先进行加一操作再参与运算。如<code>console.log(2 - ++a)</code>相当于<code>a=a+1;console.log(2-a)</code></li>
<li>取余的正负号取决于第一位数，如<code>-7%2为-1;7%-2为1</code>，所以为了得到负数的正确余值需要用绝对函数，如判断num是否为偶数时<code>Math.abs(num) % 2</code></li>
<li>+x一般用来做转数的操作，如+new Date()、+[] // 0、+&#123;&#125; // NaN、+true // 1，其实相当于Number(x)只是结果为正。</li>
<li>+号运算时才确定是相加还是连接，如果有一方是字符串则变成连接符，否则是转成数字相加。<strong>对于对象相加先调用valueOf()再调用toString()，但是valueOf()返回的一般是原对象，所以一般都会调用toString()。</strong> 特例，Date对象反着来，先toString()再valueOf()。如<code>'3' + 5 + 6 // 356</code>和<code>3 + 5 + '6' // '86'</code>。</li>
<li>0除以0会得到NaN；而非0数值除以0，会返回Infinity，若带负号则结果为-Infinity。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0</span> / <span class="hljs-number">0</span> <span class="hljs-comment">// NaN</span>
<span class="hljs-number">1</span> / <span class="hljs-number">0</span> <span class="hljs-comment">// Infinity</span>
<span class="hljs-number">1</span> / -<span class="hljs-number">0</span> <span class="hljs-comment">// -Infinity</span>
-<span class="hljs-number">1</span> / <span class="hljs-number">0</span> <span class="hljs-comment">// -Infinity</span>
-<span class="hljs-number">1</span> / -<span class="hljs-number">0</span> <span class="hljs-comment">// Infinity</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">（二）比较运算符（8个）</h5>
<ul>
<li>== ：相等</li>
<li>=== ：严格相等</li>
<li>!= ：不相等</li>
<li>!== ：严格不相等</li>
<li>< ：小于</li>
<li><= ：小于或等于</li>
<li>> ：大于</li>
<li>>= ：大于或等于</li>
</ul>
<p>说明：
===是严格等于，要求类型和数值都相等（其中NaN===NaN为false）；而==会进行隐式转换之后再比较值是否相等。具体的转换规则参考<a href="https://juejin.cn/post/6980209452381110279/" target="_blank">文章</a>。</p>
<h5 data-id="heading-3">（三）布尔运算符（4个）</h5>
<ul>
<li>! ：取反运算符</li>
<li>&& ：且运算符</li>
<li>|| ：或运算符</li>
<li><code>condition? true case : false case</code> ：三元条件运算符</li>
</ul>
<p>说明：</p>
<ol>
<li>!a会对a先做Boolean()转换操作，然后对转换的布尔值进行取反，如!0为!Boolean(0)结果为true。</li>
<li>且和或的运算均为短路运算，即<code>a && b</code>两个为true才为true，a为false则不再管b；<code>a || b</code>一个为true则为true，a为true则不再管b。</li>
<li><code>condition ? a : b</code>相当于<code>if(condition) &#123; a &#125; else &#123; b &#125;</code>。</li>
</ol>
<h5 data-id="heading-4">（四）位运算符（7个）</h5>
<ul>
<li>或运算（or）：符号为|，表示两个二进制位中有一个为1，则结果为1，否则为0。</li>
<li>与运算（and）：符号为&，表示两个二进制位都为1，则结果为1，否则为0。</li>
<li>否运算（not）：符号为～，表示将一个二进制位变成相反值。</li>
<li>异或运算（xor）：符号为ˆ，表示两个二进制位中有且仅有一个为1时，结果为1，否则为0。</li>
<li>左移运算（left shift）：符号为<<</li>
<li>右移运算（right shift）：符号为>></li>
<li>带符号位的右移运算（zero filled right shift）：符号为>>></li>
</ul>
<h5 data-id="heading-5">（五）赋值运算符（11个）</h5>
<ul>
<li>x += y // 等同于 x = x + y</li>
<li>x -= y // 等同于 x = x - y</li>
<li>x *= y // 等同于 x = x * y</li>
<li>x /= y // 等同于 x = x / y</li>
<li>x %= y // 等同于 x = x % y</li>
<li>x >>= y // 等同于 x = x >> y</li>
<li>x <<= y // 等同于 x = x << y</li>
<li>x >>>= y // 等同于 x = x >>> y</li>
<li>x &= y // 等同于 x = x & y</li>
<li>x |= y // 等同于 x = x | y</li>
<li>x ^= y // 等同于 x = x ^ y</li>
</ul>
<h5 data-id="heading-6">（六）其他运算符</h5>
<ul>
<li>小括号：有两种用法，如果把表达式放在圆括号之中，作用是求值；如果跟在函数的后面，作用是调用函数。</li>
<li>void：void运算符的作用是执行一个表达式，然后返回undefined。常见的a标签写上<code>javascript:void(0)</code>就是这个原理，会运行冒号后面的表达式但返回undefined就没执行。</li>
<li>逗号运算符：逗号运算符用于对两个表达式求值，并返回后一个表达式的值。</li>
<li>typeof运算符：返回操作数的类型，其中<code>typeof null</code>结果'object'，<code>typeof Function</code>结果是'function'。</li>
<li>instanceof运算符：<code>a instanceof b</code>判断a是否是b的实例，返回布尔值。</li>
</ul>
<h3 data-id="heading-7">二、运算符的优先级</h3>























<table><thead><tr><th>运算符的优先级顺序如下（上大于下，左大于右）</th></tr></thead><tbody><tr><td>++、--（右结合大于左结合）、-（转负数）、+（转数）、~（位反）、!（取反）</td></tr><tr><td>delete、typeof、void</td></tr><tr><td>*、/、%、+、-</td></tr><tr><td><=、>=、==、!=、===、!==</td></tr><tr><td>||、&&、?:、赋值、,</td></tr></tbody></table>
<p>说明：</p>
<ol>
<li><strong>优先级指的是同时出现的时候先计算高优先级部分，而不是说先当做这个</strong>。例如转数的加号优先级高于加法的加号，<code>1+'3'++new Date()</code>不是说把加号先当做转数符，如果是那么<code>1+'3'</code>结果是4但结果是'13'，很显然是作为加号使用。而是说先计算<code>+new Date()</code>得到时间戳<code>1531139346042</code>，再执行<code>1+'3'+1531139346042</code>。</li>
<li>++、--之类的操作数必须是可以放在赋值左边的数而不能是常数，比如<code>4++</code>会报错。还有下面的例子也要注意：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a=<span class="hljs-number">0</span>, b=<span class="hljs-number">0</span>;
a+++b; <span class="hljs-comment">// 0</span>
a; <span class="hljs-comment">// 1</span>
b; <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>右结合的优先级高于左结合和加号，上面会先找有没有右结合，找到<code>a++</code>先运算，所以运算顺序是<code>(a++)+b</code>。</p>
<ol start="3">
<li>typeof的优先级比加减乘除还高，所以一般习惯把操作数加上括号，如</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-number">2</span>*<span class="hljs-number">3</span>; <span class="hljs-comment">// NaN</span>
<span class="hljs-keyword">typeof</span> (<span class="hljs-number">2</span>*<span class="hljs-number">3</span>); <span class="hljs-comment">// 'number'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-number">2</span>+<span class="hljs-number">3</span>; <span class="hljs-comment">// 'number3'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>逻辑非优先级高于加减乘除，但逻辑或和逻辑与比加减乘除优先级低。<code>!2*0</code>相当于<code>(!2)*0</code>。</li>
<li>逻辑或||、逻辑与&&的短路运算要注意，且返回的是其中的一个表达式，而不是布尔值。<code>1 && "hi" || 0</code>的结果是<code>'hi'</code>。</li>
<li>赋值的优先级非常低。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">a = b == c <span class="hljs-comment">// 相当于a = (b==c)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面这个例子，先自己猜一下结果，再看正确答案。arr.length会报错吗？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr, arr2;
arr2 = arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
arr[arr.length] = arr = <span class="hljs-number">4</span>;
<span class="hljs-built_in">console</span>.log(arr);
<span class="hljs-built_in">console</span>.log(arr2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个，由于赋值的优先级非常低最后才执行，<code>arr[arr.length] = arr = 4</code>其实是先算的<code>arr[arr.length]</code>是指向<code>arr[3]</code>的一个地址（和<code>arr2[3]</code>指向的是同一个），接着4赋值给arr然后arr的值4赋值给这块地址指向的内存（也就是<code>arr2[3]</code>变成了4）。所以结果是arr为4，arr2为[1, 2, 3, 4]。
再来看个例子也是类似。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">n</span>: <span class="hljs-number">1</span>&#125;;
<span class="hljs-keyword">var</span> b = a;
a.x = a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">2</span>&#125;;
<span class="hljs-built_in">console</span>.log(a.x); <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(b.x); <span class="hljs-comment">// &#123;n: 2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完上面内容之后，再回到最开始的题目，你是否能够做出来，并理解其中的原因了呢？</p></div>  
</div>
            