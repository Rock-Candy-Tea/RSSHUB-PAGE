
---
title: 'JavaScript 常用数据类型及使用方式 -1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3273'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:57:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=3273'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<h3 data-id="heading-1">吃饱饭才有力气写代码~</h3>
<p>今天写代码的时候发现连最常用的JavaScript的数据类型以及使用都不熟练，所以打算今天好好整理一下！其中这个 JavaScript 对象是个很重要的思想，明天再详细地写这部分！</p>
<h3 data-id="heading-2">一.基本数据类型</h3>
<h4 data-id="heading-3">1 基本类型-String</h4>
<h5 data-id="heading-4">1.1 定义</h5>
<p>字符串类型，是存储字符(比如："Bill Gates")的变量;
<br>
字符串可以是引号中的任意文本，使用单引号双引号都行！
<br>
在字符串中使用引号也行，只要它不与包围字符串的引号匹配上就行，想要表示引号就用转义字符 ' 和 " 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-string">"jue jin"</span>
<span class="hljs-keyword">var</span> y = <span class="hljs-string">"jue jin"</span>
<span class="hljs-keyword">var</span> z = <span class="hljs-string">"jue 'jin"</span>
<span class="hljs-keyword">var</span> u = <span class="hljs-string">'jue "jin'</span>
<span class="hljs-keyword">var</span> s1=<span class="hljs-string">'It\'s alright'</span>;  <span class="hljs-comment">//It's alright</span>
<span class="hljs-keyword">var</span> s2=<span class="hljs-string">"He is called \"Johnny\""</span>; <span class="hljs-comment">//He is called "Johnny"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">1.2 常用方法</h5>
<ul>
<li>使用位置（索引）可以<strong>访问</strong>字符串中任何的<strong>字符</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = x[<span class="hljs-number">5</span>] <span class="hljs-comment">//i</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用长度属性 length 来<strong>计算</strong>字符串的<strong>长度</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.write(x.length);<span class="hljs-comment">//7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用 indexOf() 来<strong>定位</strong>字符串中某一个指定的字符首次出现的<strong>位置</strong>，lastIndexOf() 方法在字符串末尾开始查找字符串出现的位置。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = s1.indexOf(<span class="hljs-string">"It"</span>);<span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用 match() 来<strong>查找</strong>字符串中特定的<strong>字符</strong>，并且如果找到的话，则返回这个字符</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.write(s1.match(<span class="hljs-string">"right"</span>));<span class="hljs-comment">//right</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用 replace() 把某些字符<strong>替换</strong>另一些<strong>字符</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = s1.replace(<span class="hljs-string">"'s"</span>,<span class="hljs-string">" is"</span>);<span class="hljs-comment">//It is alright</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用函数 toUpperCase() / toLowerCase()<strong>大小写</strong>转换</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> txt=<span class="hljs-string">"Hello World!"</span>;       <span class="hljs-comment">// String</span>
<span class="hljs-keyword">var</span> txt1=txt.toUpperCase();   <span class="hljs-comment">// txt1 文本会转换为大写</span>
<span class="hljs-keyword">var</span> txt2=txt.toLowerCase();   <span class="hljs-comment">// txt2 文本会转换为小写</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用 split() 函数 把字符<strong>串</strong>转换为<strong>数组</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> s = <span class="hljs-string">"h,e,l,l,o"</span>
<span class="hljs-keyword">var</span> n = s.split(<span class="hljs-string">","</span>)
<span class="hljs-built_in">console</span>.log(n[<span class="hljs-number">1</span>])<span class="hljs-comment">//e</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用 concat() <strong>连接</strong>两个或多个<strong>字符串</strong>，不改变原字符串，返回一个新的字符串</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> str1=<span class="hljs-string">"Hello "</span>;
<span class="hljs-keyword">var</span> str2=<span class="hljs-string">"world!"</span>;
<span class="hljs-keyword">var</span> str3=<span class="hljs-string">" Have a nice day!"</span>;
<span class="hljs-keyword">var</span> n = str1.concat(str2,str3);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用 substring()  提取字符串中介于两个指定下标之间的字符</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> str=<span class="hljs-string">"Hello world!"</span>;
<span class="hljs-built_in">document</span>.write(str.substring(<span class="hljs-number">3</span>,<span class="hljs-number">7</span>));<span class="hljs-comment">//lo w</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2 基本类型-Number</h4>
<h5 data-id="heading-7">2.1 定义</h5>
<p>JavaScript 只有一种数字类型，可以带小数点也可以不带。<br>
极大或者极小的数字可以用科学计数法表示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x1=<span class="hljs-number">34.00</span>;     
<span class="hljs-keyword">var</span> x2=<span class="hljs-number">34</span>;
<span class="hljs-keyword">var</span> y=<span class="hljs-number">123e5</span>;      <span class="hljs-comment">// 12300000</span>
<span class="hljs-keyword">var</span> z=<span class="hljs-number">123e-5</span>;     <span class="hljs-comment">// 0.00123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：<strong>表数有范围</strong><br>
JavaScript 不定义不同类型的数字，比如整数、短、长、浮点等等，所有的数字都是浮点型类型。用 64 位存储数值，其中 0 到 51 存储数字（片段），52 到 62 存储指数，63 位存储符号。</p>
<ul>
<li>整数</li>
</ul>
<p>不使用小数点或指数计数法，最多为15位</p>
<ul>
<li>小数</li>
</ul>
<p>最大位数是17位，但是浮点运算不一定准确</p>
<ul>
<li>无穷大</li>
</ul>
<p>当数字运算结果超过了JavaScript所能表示的数字上限（溢出）或者负数下限，结果为一个特殊的无穷大（infinity）值或者负无穷大（-infinity）。<br>
<strong>除以0</strong>也产生了无限:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">2</span>/<span class="hljs-number">0</span>;<span class="hljs-comment">//Infinity</span>
<span class="hljs-keyword">var</span> y = -<span class="hljs-number">2</span>/<span class="hljs-number">0</span>;<span class="hljs-comment">//-Infinity</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>八进制和十六进制</li>
</ul>
<p>默认情况下JavaScript数字为十进制数。<br>
如果前缀为 0，则 JavaScript 会把数值常量解释为八进制数;
<br>如果前缀为 0 和 "x"，则解释为十六进制数。
<br>
可以使用 toString() 方法 <strong>输出</strong>16进制、8进制、2进制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> myNumber=<span class="hljs-number">128</span>;
myNumber.toString(<span class="hljs-number">16</span>);   <span class="hljs-comment">// 返回 80</span>
myNumber.toString(<span class="hljs-number">8</span>);    <span class="hljs-comment">// 返回 200</span>
myNumber.toString(<span class="hljs-number">2</span>);    <span class="hljs-comment">// 返回 10000000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>NaN 非数字值</li>
</ul>
<p>NaN 属性是代表非数字值的特殊值，这个属性表示这个值不是数字。可以用全局函数 isNaN() 来判断一个值是否是 NaN 值。<br>
<strong>一个数字除以一个字符串结果不是一个数字</strong><br>
<strong>一个数字除以一个字符串数字结果是一个数字</strong><br>
<strong>除以0是无穷大，无穷大是一个数字</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">1000</span> / <span class="hljs-string">"Apple"</span>;
<span class="hljs-built_in">isNaN</span>(x); <span class="hljs-comment">// 返回 true</span>
<span class="hljs-keyword">var</span> y = <span class="hljs-number">100</span> / <span class="hljs-string">"1000"</span>;
<span class="hljs-built_in">isNaN</span>(y); <span class="hljs-comment">// 返回 false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数字可以是数字或者对象</li>
</ul>
<p>数字可以私有数据进行初始化，就像 x = 123;<br>
JavaScript 数字对象初始化数据， var y = new Number(123);</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">123</span>;
<span class="hljs-keyword">var</span> y = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">123</span>);
(x === y) <span class="hljs-comment">// 为 false，因为 x 是一个数字，y 是一个对象</span>
<span class="hljs-keyword">typeof</span>(x) <span class="hljs-comment">// 返回 Number</span>
<span class="hljs-keyword">typeof</span>(y) <span class="hljs-comment">// 返回 Object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">2.2 常用方法</h5>
<ul>
<li>Number.parseFloat()    将字符串转换成浮点数</li>
<li>Number.parseInt()      将字符串转换成整型数字</li>
<li>Number.isFinite()      判断传递的参数是否为有限数字</li>
<li>Number.isInteger()     判断传递的参数是否为整数。</li>
<li>Number.isNaN()         判断传递的参数是否为 isNaN()。</li>
<li>Number.isSafeInteger() 判断传递的参数是否为安全整数。</li>
<li>toExponential()        返回一个数字的指数形式的字符串，如：1.23e+2</li>
<li>toFixed()              返回指定小数位数的表示形式。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a=<span class="hljs-number">123</span>; b=a.toFixed(<span class="hljs-number">2</span>); <span class="hljs-comment">// b="123.00"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>toPrecision()          返回一个指定精度的数字。如下例子中，a=123 中，3会由于精度限制消失:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a=<span class="hljs-number">123</span>; b=a.toPrecision(<span class="hljs-number">2</span>); <span class="hljs-comment">// b="1.2e+2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">3 基本类型-Boolean</h4>
<p>布尔（逻辑）只能有两个值：true 或 false
这个就经常用在条件测试中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x=<span class="hljs-literal">true</span>;
<span class="hljs-keyword">var</span> y=<span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4 基本类型-Null</h4>
<p>可以通过将变量的值设置为 null 来清空变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> car=<span class="hljs-string">"Volvo"</span>;
<span class="hljs-built_in">document</span>.write(car);<span class="hljs-comment">//Volvo</span>
<span class="hljs-keyword">var</span> car=<span class="hljs-literal">null</span>;
<span class="hljs-built_in">document</span>.write(car);<span class="hljs-comment">//null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">5 基本类型-Undefined</h4>
<p><strong>Undefined 这个值表示变量不含有值。</strong>
<br>
<strong>注意</strong>：如果遇到控制台报undefined,就意味着你定义的那个变量没有拿到值，就可以有针对性的排查！</p>
<h4 data-id="heading-12">6 基本类型-Symbol</h4>
<p>Symbol 是 ES6 引入了一种新的原始数据类型，表示独一无二的值。</p>
<h3 data-id="heading-13">二.引用数据类型</h3>
<h4 data-id="heading-14">1 引用类型-Object</h4>
<h5 data-id="heading-15">1.1 定义</h5>
<p>对象由花括号分隔；在括号内部，属性由逗号分隔；属性以名称和值对的形式 (name : value) 来定义；<br>
对象属性有两种寻址方式:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person=&#123;<span class="hljs-attr">firstname</span>:<span class="hljs-string">"John"</span>, <span class="hljs-attr">lastname</span>:<span class="hljs-string">"Doe"</span>, <span class="hljs-attr">id</span>:<span class="hljs-number">5566</span>&#125;;
name=person.lastname;
name=person[<span class="hljs-string">"lastname"</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">2 引用类型-Array</h4>
<h5 data-id="heading-17">2.1 定义</h5>
<p>下面的代码创建名为 cars 的数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> cars=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
cars[<span class="hljs-number">0</span>]=<span class="hljs-string">"Saab"</span>;
cars[<span class="hljs-number">1</span>]=<span class="hljs-string">"Volvo"</span>;
cars[<span class="hljs-number">2</span>]=<span class="hljs-string">"BMW"</span>;

<span class="hljs-keyword">var</span> cars=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">"Saab"</span>,<span class="hljs-string">"Volvo"</span>,<span class="hljs-string">"BMW"</span>);

<span class="hljs-keyword">var</span> cars=[<span class="hljs-string">"Saab"</span>,<span class="hljs-string">"Volvo"</span>,<span class="hljs-string">"BMW"</span>];

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">3 引用类型-Function</h4>
<p>（这个也明天写~）</p></div>  
</div>
            