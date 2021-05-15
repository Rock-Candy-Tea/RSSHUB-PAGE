
---
title: '一.深入探讨JS数据类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1380'
author: 掘金
comments: false
date: Fri, 14 May 2021 08:52:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=1380'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">一.数据类型分类(7+1)</h3>
<blockquote>
<p><code>最新版本的JS标准中，数据类型分了8种，包括：</code></p>
<ul>
<li><code>7种基本数据类型:</code>Undefined、Null、Boolean、Number、String、Symbol（es6新增）和BigInt（es10新增）；</li>
<li><code>1种引用数据类型</code>:Object（Object本质上是由一组无序的名值对组成的）。里面包含 function、Array、Date等。JavaScript不支持任何创建自定义类型的机制，而所有值最终都将是上述 8 种数据类型之一。</li>
</ul>
</blockquote>
<h4 data-id="heading-1">1.1 基本数据类型细述</h4>
<p>基本数据类型也是简单数据类型，或者原始类型，值类型；基本类型的变量值和变量标识符标识符一起存放在栈区的，一般不可改变。占据空间小、大小固定，属于被频繁使用数据，所以放入栈中存储。</p>
<h5 data-id="heading-2">1.1.1 typeof操作符</h5>
<blockquote>
<p>typeof 可以判断所有的值类型数据,返回的都是字符串</p>
<ul>
<li>常见的值类型数据有：number，string，boolean，undefined，symbol，</li>
<li>可以判断常见的引用类型数据：object,array,null.返回的都是 object</li>
<li>判断函数 function 返回的是 function</li>
</ul>
</blockquote>
<h5 data-id="heading-3">1.1.2 undefined类型</h5>
<p>声明后变量的没有初始化就是<code>undefined</code>,是唯一值;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//特殊情况是即使是没有声明变量a</span>
<span class="hljs-keyword">typeof</span> a ;<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">1.1.3 null类型</h5>
<p>null值表示一个空对象指针，表现为检验<code>typeof null</code>会返回'Object';</p>
<blockquote>
<p>null的用法：</p>
<ul>
<li>在定义将来要保存的对象时建议用null初始化；</li>
<li>null是个假值；所以，<code>null == undefined ;</code>为true。</li>
<li>一律用<code>===</code>,只有判断是不是等于 null 或 undefined 才用<code>==</code>。</li>
<li><code>null==0 ;</code>//false</li>
<li><code>!null==true;</code>//true  常用于if判断</li>
</ul>
</blockquote>
<h5 data-id="heading-5">1.1.4 Boolean类型</h5>
<p>Boolean类型是JavaScript中使用最多的一种基本数据类型，只有两个值true和false（全为小写）。</p>
<blockquote>
<p>JavaScript中所有类型的值都有与这两个Boolean值等价的值，可以调用转型函数Boolean()将其他类型的值转化为Boolean值。</p>
</blockquote>
<p>不同类型值与布尔值的转换规则如下：</p>
<pre><code class="hljs language-js copyable" lang="js">[] == <span class="hljs-literal">false</span>; <span class="hljs-comment">//true</span>
![]==<span class="hljs-literal">false</span>   <span class="hljs-comment">//true表示把空数组转化为布尔值在进行取反然后和右边的比较</span>
数据转化为布尔值的规律：只有<span class="hljs-string">`0/NaN/null/undefined`</span>五个值是<span class="hljs-literal">false</span>，其余全为<span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">1.1.5 Number类型</h5>
<ul>
<li>Number可以同时表示整数和浮点数值，用浮点值（小数）进行计算会不精确，即0.1+0.2=0.30000000000000004；</li>
<li>NaN:是非数字，英文名字<code>not a number</code>;函数isNaN();这句话的意思是<code>是否是非数字?</code></li>
<li>NaN==NaN  //false;</li>
</ul>
<h6 data-id="heading-7">1.1.5.1 Number的数值转换函数Number()</h6>
<p>Number()可以用于任何数据类型：</p>
<blockquote>
<ul>
<li>
<ul>
<li>布尔转化0，1</li>
</ul>
</li>
<li>
<ul>
<li>数值不转换</li>
</ul>
</li>
<li>
<ul>
<li>null转为0</li>
</ul>
</li>
<li>
<ul>
<li>undefined转为NaN</li>
</ul>
</li>
<li>
<ul>
<li>字符串：正常数字返回，16进制转化10进制；  空串为0，其他NaN</li>
</ul>
</li>
<li>
<ul>
<li>对象：调用对象的 valueOf()方法，然后依照前面的规则转换返回的值。如果转换 的结果是 NaN，则调用对象的 toString()方法，然后再次依照前面的规则转换返回的字符 串值。</li>
</ul>
</li>
</ul>
</blockquote>
<h6 data-id="heading-8">1.1.5.2 Number的数值转换函数parseInt()</h6>
<blockquote>
<ul>
<li>
<ul>
<li>parseInt()专门用于把字符串转换为数值：</li>
</ul>
</li>
<li>
<ul>
<li>函数在转换字符串时，更多的是看其是否符合数值模式。它会忽略字符串前面的空格，直至找到第一个非空格字符。</li>
</ul>
</li>
<li>
<ul>
<li>如果第一个字符不是数字字符或者负号，parseInt()就会返回 NaN；也就是说，用 parseInt()转换空字符串会返回 NaN（Number()对空字符返回 0）。</li>
</ul>
</li>
<li>
<ul>
<li>如果第一个字符是数字字符，parseInt()会继续解析第二个字符，直到解析完所有后续字符或者遇到了一个非数字字符。</li>
</ul>
</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num1 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"1234blue"</span>); <span class="hljs-comment">// 1234</span>
<span class="hljs-keyword">var</span> num2 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">""</span>); <span class="hljs-comment">// NaN</span>
<span class="hljs-keyword">var</span> num3 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"0xA"</span>); <span class="hljs-comment">// 10（十六进制数）</span>
<span class="hljs-keyword">var</span> num4 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-number">22.5</span>); <span class="hljs-comment">// 22</span>
<span class="hljs-keyword">var</span> num5 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"070"</span>); <span class="hljs-comment">// 56（八进制数）</span>
<span class="hljs-keyword">var</span> num6 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"70"</span>); <span class="hljs-comment">// 70（十进制数）</span>
<span class="hljs-keyword">var</span> num7 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"0xf"</span>); <span class="hljs-comment">// 15（十六进制数）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>parseInt()可以引入第二个参数：转换时使用的基数。</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num1 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10"</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">//2 （按二进制解析）</span>
<span class="hljs-keyword">var</span> num2 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10"</span>, <span class="hljs-number">8</span>); <span class="hljs-comment">//8 （按八进制解析）</span>
<span class="hljs-keyword">var</span> num3 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10"</span>, <span class="hljs-number">10</span>); <span class="hljs-comment">//10 （按十进制解析）</span>
<span class="hljs-keyword">var</span> num4 = <span class="hljs-built_in">parseInt</span>(<span class="hljs-string">"10"</span>, <span class="hljs-number">16</span>); <span class="hljs-comment">//16 （按十六进制解析）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">1.1.5.3 Number的数值转换函数parseFloat()</h6>
<p>parseFloat() 与 parseInt()函数类似，parseFloat()也是从第一个字符（位置 0）开始解析每个字符。而且也是一直解析到字符串末尾，或者解析到遇见一个无效的浮点数字字符为止。</p>
<h5 data-id="heading-10">1.1.6 String类型</h5>
<p>字符串是不可变的，若果要修改的话，必须要销毁原始的字符串，字符串可以用双引号、单引号、反引号标示。</p>
<h5 data-id="heading-11">1.1.6.1 转化为字符串</h5>
<ul>
<li><code>1、toString():</code> 除了null和undefined值没有tostring()方法，其他值都有这个方法，该方法返回字符串的一个副本。</li>
<li><code>2.String():</code>如果不确定一个值是null或undefined，可以使用String()转型函数，始终会返回相应类型值的字符串.</li>
<li><code>3.使用+" ":</code> 即可以通过要转换的值 + 空字符串(" ")，也可以实现转换。</li>
</ul>
<h5 data-id="heading-12">1.1.6.2 模板字面量、字符串插值、模板字面量标签函数</h5>
<h6 data-id="heading-13">模板字面量</h6>
<blockquote>
<p>ES6新增的模板字面量使用反引号包裹，它的作用是保留换行字符，可以跨行定义字符串</p>
</blockquote>
<h6 data-id="heading-14">字符串插值</h6>
<blockquote>
<ul>
<li>模板字面量是一种特殊的JavaScript句法表达式，只不过求值之后得到的是字符串。即模板字面量在定义时立即求值并转化为字符串实例。任何插入的变量也会从他们最接近的作用域中取值。</li>
<li>字符串插值通过$&#123;&#125;使用一个JavaScript表达式实现</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> num = <span class="hljs-number">5</span>;
      <span class="hljs-keyword">let</span> square = <span class="hljs-string">"二次方"</span>;
      <span class="hljs-keyword">let</span> res1 = num + <span class="hljs-string">"的"</span> + square + <span class="hljs-string">"是"</span> + num * num;
      <span class="hljs-keyword">let</span> res2 = <span class="hljs-string">`<span class="hljs-subst">$&#123;num&#125;</span>的<span class="hljs-subst">$&#123;square&#125;</span>是<span class="hljs-subst">$&#123;num * num&#125;</span>`</span>;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"字符串拼接"</span>, res1); <span class="hljs-comment">//字符串拼接 5的二次方是25</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"模板字符串"</span>, res2); <span class="hljs-comment">//模板字符串 5的二次方是25</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">1.1.7 Symbol类型(ES6)</h5>
<p>ES6新规定的Symbol(符号)是原始值，且符号实例唯一、不可变的，它的用途是确保对象属性使用唯一标识符。</p>
<h6 data-id="heading-16">使用方法</h6>
<p>需要使用Symbol()函数初始化</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-built_in">console</span>.log(name1 == name2);  <span class="hljs-comment">//false</span>
 
<span class="hljs-comment">// 希望能够多次使用同一个symbol值</span>
 <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到未创建后新建</span>
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到已创建后返回</span>
 <span class="hljs-built_in">console</span>.log(name1 === name2); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<blockquote>
<p>Symbol的另一特点是隐藏性，Symbol 作为属性名，遍历对象的时候，该属性不会出现在for...in、for...of循环中，也不会被Object.keys()、Object.getOwnPropertyNames()、JSON.stringify()返回。</p>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> id = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"id"</span>);
 <span class="hljs-keyword">let</span> obj = &#123;
  [id]:<span class="hljs-string">'symbol'</span>
 &#125;;
 <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> option <span class="hljs-keyword">in</span> obj)&#123;
     <span class="hljs-built_in">console</span>.log(obj[option]); <span class="hljs-comment">//空</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<blockquote>
<p>但是也有能够访问的方法：Object.getOwnPropertySymbols.该方法会返回一个数组，成员是当前对象的所有用作属性名的Symbol值。</p>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> id = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"id"</span>);
 <span class="hljs-keyword">let</span> obj = &#123;
  [id]:<span class="hljs-string">'symbol'</span>
 &#125;;
<span class="hljs-keyword">let</span> array = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj);
 <span class="hljs-built_in">console</span>.log(array); <span class="hljs-comment">//[Symbol(id)]</span>
 <span class="hljs-built_in">console</span>.log(obj[array[<span class="hljs-number">0</span>]]);  <span class="hljs-comment">//'symbol'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">1.1.8 BigInt类型(ES10)</h5>
<blockquote>
<p>BigInt是JavaScript中一种可以用来表示任意精度(arbitrary precision)整数的基本数据类型，使用BigInt可以安全的存储和操作任意大小的整数而不受Number类型的安全值范围的限制。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">方法一:生成一个<span class="hljs-built_in">BigInt</span>类型的值只需要在任意整数后加上n做后缀即可。
      例如：<span class="hljs-number">123</span> 用<span class="hljs-built_in">BigInt</span>类型表示<span class="hljs-number">123n</span>.
 方法二:通过全局函数<span class="hljs-built_in">BigInt</span>(number)来将<span class="hljs-built_in">Number</span>类型转化为<span class="hljs-built_in">BigInt</span>类型
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BigInt类型更详细的介绍请参考MDN文档---><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/BigInt" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<h4 data-id="heading-18">1.2 引用数据类型-Object类型</h4>
<blockquote>
<p>简介:<br>
1.Object类型是JavaScript中最庞大而复杂的引用数据类型，本文只做简单介绍，后续的文章会做Object的详细介绍。<br>
2.Object，即对象，是一组数据和功能的集合。对象可以通过执行new操作符后跟要创建的对象类型的名称来创建。而创建 Object 类型的实例并为其添加属性和（或）方法，就可以创建自定义对象。</p>
</blockquote>
<h5 data-id="heading-19">1.2.1 Object实例属性和方法：</h5>
<p>由于在 ECMAScript 中 Object 是所有对象的基础，因此所有对象都具有这些基本的属性和方法。Object 的每个实例都具有下列属性和方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title">constructor</span>：保存着用于创建当前对象的函数。对于前面的例子而言，构造函数（<span class="hljs-title">constructor</span>）就是 <span class="hljs-title">Object</span>(<span class="hljs-params"></span>)。


<span class="hljs-title">hasOwnProperty</span>(<span class="hljs-params">propertyName</span>)：用于检查给定的属性在当前对象实例中（而不是在实例的原型中）是否存在。其中，作为参数的属性名（<span class="hljs-title">propertyName</span>）必须以字符串形式指定（例如：<span class="hljs-title">o</span>.<span class="hljs-title">hasOwnProperty</span>(<span class="hljs-params"><span class="hljs-string">"name"</span></span>)）。


<span class="hljs-title">isPrototypeOf</span>(<span class="hljs-params">object</span>)：用于检查传入的对象是否是传入对象的原型。


<span class="hljs-title">propertyIsEnumerable</span>(<span class="hljs-params">propertyName</span>)：用于检查给定的属性是否能够使用 <span class="hljs-title">for</span>-<span class="hljs-title">in</span> 语句来枚举。与<span class="hljs-title">hasOwnProperty</span>(<span class="hljs-params"></span>)方法一样，作为参数的属性名必须以字符串形式指定。


<span class="hljs-title">toLocaleString</span>(<span class="hljs-params"></span>)：返回对象的字符串表示，该字符串与执行环境的地区对应。


<span class="hljs-title">toString</span>(<span class="hljs-params"></span>)：返回对象的字符串表示。


<span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)：返回对象的字符串、数值或布尔值表示。通常与 <span class="hljs-title">toString</span>(<span class="hljs-params"></span>)方法的返回值相同。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">二.数据类型比较</h3>
<h4 data-id="heading-21">2.1基本数据类型</h4>
<ul>
<li>值是不可变的</li>
</ul>
<blockquote>
<ul>
<li>一.可变和不可变类型</li>
</ul>
<blockquote>
<p>可变类型:值发生改变时，内存地址不变，即id不变，证明在改变原值
不可变类型：值发生改变时，地址也发生改变，即id也变，证明是没有在改变原值，是产生了新的值</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">"aaaaaa"</span>;
name.toUpperCase();<span class="hljs-comment">//输出 AAAAAA</span>
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">// 输出 aaaaaa</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>存放在栈区</li>
</ul>
<blockquote>
<p>基本类型值指的是简单的数据段，按值访问，可操作保存在变量中的实际的值，其占据空间小、大小固定，属于被频繁使用的数据，所以放入栈（stack）中存储。</p>
</blockquote>
<ul>
<li>值的比较</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> m = <span class="hljs-literal">true</span>;
<span class="hljs-built_in">console</span>.log(n == m);<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(n === m);<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">2.2 引用数据类型</h4>
<ul>
<li>值是可变的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'jake'</span>,
        <span class="hljs-attr">age</span>:<span class="hljs-number">22</span>,
        <span class="hljs-attr">action</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"do something!"</span>)
        &#125;
      &#125;
person.age = <span class="hljs-number">23</span>;
<span class="hljs-built_in">console</span>.log(person.age)<span class="hljs-comment">// 23</span>

从上面的代码可看出引用数据 类型可以拥有一个或多个属性和方法，而且是可以动态修改的,是在原值上修改的。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同时存放在栈内存和堆内存</li>
</ul>
<blockquote>
<p>引用数据类型在<code>栈中存储了指针</code>，该指针指向<code>堆中该实体</code>的起始地址，当解释器寻找引用值时，会首先检索其在栈中的地址，取得地址后从堆中获得实体。</p>
</blockquote>
<ul>
<li>值的比较</li>
</ul>
<blockquote>
<p>当从一个变量向另一个变量赋引用类型的值时，同样也会将存储在变量中的对象的值复制一份到位新变量分配的空间中。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person1 = &#123;
<span class="hljs-attr">age</span>:<span class="hljs-number">20</span>
          &#125;
<span class="hljs-keyword">var</span> person2 = person1;
person2.age = <span class="hljs-number">23</span>;
<span class="hljs-built_in">console</span>.log(person1.age == person2.age)<span class="hljs-comment">// true</span>
<span class="hljs-comment">/*
引用数据类型存储`在堆中的对象`,`在栈中存储了指针`，而这个指针的指向正是堆中实体的起始位置。变量person1初始化时，person1指针指向该对象&#123;age：20&#125;的地址，将person1赋给person2后，person2又指向该对象&#123;age：20&#125;的地址，这两个变量指向了同一个对象。因此改变其中任何一个变量，都会相互影响。
此时，如果取消某一个变量对于原对象的引用，不会影响到另一个变量。
*/</span>
<span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">age</span>:<span class="hljs-number">22</span>&#125;
<span class="hljs-keyword">var</span> b = a;
a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(b);<span class="hljs-comment">//&#123;age:22&#125;</span>
<span class="hljs-comment">/*
上面代码中，a和b指向同一个对象，然后a的值变为1，这时不会对b产生影响，b还是指向原来的那个对象。
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">三.JS数据类型隐式转化(你只需要记住常见的几种)</h3>
<h4 data-id="heading-24">3.1转成String类型</h4>
<pre><code class="hljs language-js copyable" lang="js">字符串连接符(+)转成字符串
 <span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>;
 <span class="hljs-keyword">var</span> b = <span class="hljs-string">"20"</span>;
 <span class="hljs-keyword">var</span> c = a + b;
 <span class="hljs-built_in">console</span>.log(c,<span class="hljs-keyword">typeof</span> c);<span class="hljs-comment">//1020 String</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">3.2转成Number类型(数学运算中)</h4>
<ul>
<li>
<p>自增自减运算符 ++/--</p>
</li>
<li>
<p>减乘除求余算数运算符 +-*/%</p>
</li>
<li>
<p>关系运算符 > < >= <=  == != === !===</p>
<ul>
<li>当关系运算符一边有<code>字符串</code>时，会将其数据类型使用Number转换，再做比较；</li>
</ul>
</li>
<li>
<p>特殊情况，请记住以下结论(判断相等吗，只有数字才能判断相等吗):</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span> == <span class="hljs-literal">undefined</span>) <span class="hljs-comment">// true </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>) <span class="hljs-comment">// true </span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> == <span class="hljs-literal">null</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">NaN</span> == <span class="hljs-literal">NaN</span>) <span class="hljs-comment">// false NaN与任何数据比较都是NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">3.3转成Boolean型(逻辑判断中)</h4>
<blockquote>
<ul>
<li>数据在逻辑判断和逻辑运算之中会隐式转换为Boolean类型</li>
<li>逻辑非运算符！ 逻辑非运算中，会将数据先做Boolean转换，然后取反</li>
</ul>
</blockquote>
<ul>
<li>以下这几种数据经过Boolean转换，会转成:false:
<ul>
<li>+0、-0、NaN、undefined、null、""、document.all();</li>
</ul>
</li>
<li>复杂数据类型经过Boolean转换后都是true，如：[]、&#123;&#125;</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>( &#123;&#125; )&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'12131231'</span>)
&#125;    <span class="hljs-comment">//12131231</span>

<span class="hljs-keyword">if</span>( <span class="hljs-literal">null</span> )&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'4444444444'</span>)
&#125;  <span class="hljs-comment">//压根不执行</span>

<span class="hljs-keyword">if</span>( [] )&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shuzu'</span>)
&#125;<span class="hljs-comment">//shuzu</span>

<span class="hljs-keyword">if</span>( !<span class="hljs-literal">null</span> )&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'4444444444'</span>)
&#125;<span class="hljs-comment">//444444444</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">3.4 复杂数据类型隐式转换</h4>
<blockquote>
<p>复杂数据类型隐式转换时会先调用自身的valueOf()和toString()两个函数，如果自身数据原型对象上没有相应的函数则会由原型链__proto__最终调用到Object.prototype对象对应的函数上，所有对象（除Null 和 undefined）都会继承这两个方法。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">转换规则如前面所述，使用valueOf()获取原始值，如果原始值不是基本类型，则使用toString方法转成字符串

<span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>] == <span class="hljs-string">'1,2'</span>) <span class="hljs-comment">// true 解析如下</span>

<span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>].valueOf()) <span class="hljs-comment">// [1,2]，获取原始值</span>
<span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>].toString()) <span class="hljs-comment">// '1,2'，转成字符串，与右边数据相等</span>

<span class="hljs-keyword">var</span> a = &#123;&#125;
<span class="hljs-built_in">console</span>.log(a == <span class="hljs-string">"[object Object]"</span>) <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 左边转换过程</span>
<span class="hljs-built_in">console</span>.log(a.valueOf()) <span class="hljs-comment">// &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125;.toString()) <span class="hljs-comment">// "[object Object]"，再进行比较</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">3.5逻辑非隐式转换与关系运算符隐式转换</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1111</span>)||<span class="hljs-literal">undefined</span>)&#123;

    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1111</span>);

&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">22222</span>)

&#125;<span class="hljs-comment">//1111   22222</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>逻辑非优先级高于关系符运算</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(![] == <span class="hljs-number">0</span>) <span class="hljs-comment">// true </span>
<span class="hljs-comment">/*
解析：空数组转换布尔型是true，取非后为false；false跟数字0比较，
布尔型被Number后为0，0 == 0
*/</span>

<span class="hljs-built_in">console</span>.log([] == ![]) <span class="hljs-comment">// true </span>
<span class="hljs-comment">/*
[].valueOf().toString()=>''; 
![] => false 
关系运算符将两边转成Number型进行比较，Number('') => 0; Number(false) => 0
*/</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; == !&#123;&#125;) <span class="hljs-comment">// false </span>
<span class="hljs-comment">/*
逻辑非优先级高，其实是&#123;&#125;和!&#123;&#125;，这个逻辑表达式的比较，按照复杂类型隐式转换规则，需通过valueOf和toString转换后进行比较

console.log(&#123;&#125;.valueOf()) // &#123;&#125;
console.log(&#123;&#125;.toString()) // "[object Object]"，再进行比较
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">3.6引用数据类型的转化处理</h4>
<blockquote>
<ul>
<li>引用数据类型，可称为对象类型，包括Object 、Array 、Function 、Date等；数据存在堆中，变量中存的是堆地址，我们只能操作存在栈内存的引用地址。</li>
<li>var声明的一般是栈内存</li>
<li>6种基本数据类型的存储方式是值类型，存在于栈中</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log([] == []) <span class="hljs-comment">// false 数组为引用类型，在堆中存放的是两份不同的数据，所以比较结果不相等</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; == &#123;&#125;) <span class="hljs-comment">// false，同理，&#123;&#125;为引用类型，结果不相等</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里特别感谢快狗打车前端团队提供的优秀的技术博文参考，他们有很多优秀的文章值得阅读，若果你想去看，请点击<a href="https://juejin.cn/post/6844903880015216653" target="_blank">--->传送门</a></p></div>  
</div>
            