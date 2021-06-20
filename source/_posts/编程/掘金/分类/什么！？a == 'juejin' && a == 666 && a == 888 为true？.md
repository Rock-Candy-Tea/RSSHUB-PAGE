
---
title: "什么！？a == 'juejin' && a == 666 && a == 888 为true？"
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5720'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 18:17:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=5720'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>看到这个标题，很多人可能会感觉很新奇， <code>a == 'juejin' && a == 666 && a == 888</code> 为 true，这怎么可能呢？javascript 有时就是这么的神奇，上面表达式的实现是通过 js 隐式转换部分知识实现的，那让我们先来了解一下隐式转换，再去尝试实现上述表达式吧。</p>
<h2 data-id="heading-0">什么是隐式转换</h2>
<p>在 javascript 中，当运算符在运算时，如果两边数据类型不统一，CPU就无法进行运算，这时 javascript 会自动将运算符两边的数据做一个数据类型转换，转成一样的数据类型再计算。这种无需程序员手动转换，而由编译器自动转换的方式就称为隐式转换。</p>
<p>当引用类型和基础类型进行运算时，会将引用类型转换为基础类型。在 javascript 中，每个引用类型都有他们的内置方法，其中有两个内置方法 <code>valueOf()</code> 和 <code>toString()</code>:</p>
<ul>
<li>toString(): 返回对象的字符串表示。</li>
<li>valueOf(): 返回对象对应的字符串、数值或布尔值表示。通常与 toString()的返回值相同。</li>
</ul>
<p>他们能够将 Object 类型隐式转换为基础类型，从而进行运算和比较。</p>
<h2 data-id="heading-1">不同类型转换规则</h2>
<p>了解了隐式转换需要将不同类型转换为同一类型，那我们需要在了解一下不同类型转换的规则。</p>
<p>首先 js 目前有基本类型： number、string、boolean、undefined、null和symbol，引用类型为Object。</p>
<p>其中，js规定 <code>undefined == null</code>，且其他类型无法转换为 undefined 和 null。剩下的其他类型大多可以互相转化。</p>
<h3 data-id="heading-2">其他类型 -> number类型</h3>
<h4 data-id="heading-3">string -> number</h4>
<ul>
<li>如果 string 的内容为纯数字内容，则转换结果为数字</li>
<li>如果 string 的内容不是纯数字，则转换结果为NaN</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">'1272421'</span>)  <span class="hljs-comment">// 1272421</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">'ok111'</span>)    <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">boolean -> number</h4>
<ul>
<li>true -> 1</li>
<li>false -> 0</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">true</span>)   <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">false</span>)  <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">undefined -> number</h4>
<ul>
<li>undefined -> NaN</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">undefined</span>)   <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">null -> number</h4>
<ul>
<li>null -> 0</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">null</span>)   <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">Object -> number</h4>
<ul>
<li>先调用 valueOf() 方法，看能否得到一个基础类型，如能，使用 Number() 对此基础类型进行转换</li>
<li>如调用 valueOf() 没有得到基础类型，则调用 toString() 方法看能否得到一个基础类型，如能，使用 Number() 对此基础类型进行转换；如不能，报错</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 未实现自定义 valueOf() 和 toString() 的对象</span>
<span class="hljs-keyword">const</span> a = &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;
<span class="hljs-built_in">Number</span>(a)  <span class="hljs-comment">// NaN</span>
<span class="hljs-comment">// 自定义了 valueOf() 返回基础类型</span>
<span class="hljs-keyword">const</span> b = &#123;
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">6</span>
    &#125;
&#125;
<span class="hljs-built_in">Number</span>(b)  <span class="hljs-comment">// 6</span>
<span class="hljs-comment">// 自定义了 toString() 返回基础类型</span>
<span class="hljs-keyword">const</span> c = &#123;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">7</span>
    &#125;
&#125;
<span class="hljs-built_in">Number</span>(c)  <span class="hljs-comment">// 7</span>
<span class="hljs-comment">// 自定义了 valueOf() 和 toString() 都不返回基础类型</span>
<span class="hljs-keyword">const</span> d = &#123;
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;
&#125;
<span class="hljs-built_in">Number</span>(d)  <span class="hljs-comment">// Uncaught TypeError: Cannot convert object to primitive value</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">其他类型 -> string</h3>
<h4 data-id="heading-9">基础类型 -> string</h4>
<ul>
<li>基础类型转换为string，相当于直接在外面<code>""</code>变成字符串内容</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>(<span class="hljs-number">666</span>)   <span class="hljs-comment">// "666"</span>
<span class="hljs-built_in">String</span>(<span class="hljs-literal">true</span>)  <span class="hljs-comment">// "true"</span>
<span class="hljs-built_in">String</span>(<span class="hljs-literal">undefined</span>)  <span class="hljs-comment">// "undefined"</span>
<span class="hljs-built_in">String</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// "null"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Object -> string</h4>
<ul>
<li>先调用 toString() 方法，看能否得到一个基础类型，如能，使用 String() 对此基础类型进行转换</li>
<li>如调用 toString() 没有得到基础类型，则调用 valueOf() 方法看能否得到一个基础类型，如能，使用 String() 对此基础类型进行转换；如不能，报错</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 未实现自定义 valueOf() 和 toString() 的对象</span>
<span class="hljs-keyword">const</span> a = &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;
<span class="hljs-built_in">Number</span>(a)  <span class="hljs-comment">// "[object Object]"</span>
<span class="hljs-comment">// 自定义了 toString() 返回基础类型</span>
<span class="hljs-keyword">const</span> b = &#123;
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"ok"</span>
    &#125;
&#125;
<span class="hljs-built_in">String</span>(b)  <span class="hljs-comment">// "ok"</span>
<span class="hljs-comment">// 自定义了 valueOf() 返回基础类型</span>
<span class="hljs-keyword">const</span> c = &#123;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span>
    &#125;
&#125;
<span class="hljs-built_in">String</span>(c)  <span class="hljs-comment">// "hello"</span>
<span class="hljs-comment">// 自定义了 valueOf() 和 toString() 都不返回基础类型</span>
<span class="hljs-keyword">const</span> d = &#123;
    <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;
&#125;
<span class="hljs-built_in">String</span>(d)  <span class="hljs-comment">// Uncaught TypeError: Cannot convert object to primitive value</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">其他类型 -> boolean</h3>
<ul>
<li>undefined null 0 -0 +0 NaN '' 转换结果为 false</li>
<li>其他类型和值转换结果都为 true</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Boolean</span>(&#123;&#125;) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">== 比较规则</h2>
<h3 data-id="heading-13">基础类型的比较</h3>
<ul>
<li>undefined等于null</li>
<li>string 和 number 比较时，string 转 number</li>
<li>number 和 boolean 比较时，boolean 转 number</li>
<li>string 和 boolean 比较时，两者转 number</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>;    <span class="hljs-comment">//true</span>
<span class="hljs-string">'0'</span> == <span class="hljs-number">0</span>;        　　  <span class="hljs-comment">//true,字符串转数字</span>
<span class="hljs-number">0</span> == <span class="hljs-literal">false</span>;           <span class="hljs-comment">//true,布尔转数字</span>
<span class="hljs-string">'0'</span> == <span class="hljs-literal">false</span>;    　　　<span class="hljs-comment">//true,两者转数字</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">引用类型和基础类型比较</h3>
<p>引用类型和基础类型比较，上面提到过会通过 valueOf() 和 toString() 方法将引用类型转换为基础类型，然后进行比较。上面有提到过转换规则，引用类型转换为 number 类型优先使用 valueOf()，转换成 string 类型优先使用 toString()。</p>
<p>但是在使用 <code>==</code> 进行比较时有一点区别：</p>
<ul>
<li>和 boolean 类型比较，都转换为 true</li>
<li>和 number 或者 string 类型比较，都优先使用 valueOf() 看能否转换为基础类型，能的话将基础类型在转换成对应的 number 或者 string 类型比较；不能的话再使用 toString() 进行转换</li>
</ul>
<h2 data-id="heading-15">实现 a == 'juejin' && a == 666 && a == 888</h2>
<p>理解了上面的隐式转换规则，那我们就可以思考如何来实现了。</p>
<p>我们可以自定义 valueOf()，第一次比较时返回的值为 'juejin'，第二次为666，之后返回的值为888：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123;
 <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 记录当前是第几次比较</span>
 <span class="hljs-function"><span class="hljs-title">valueOf</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-built_in">this</span>.count++;
   <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.count === <span class="hljs-number">1</span>) &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-string">'juejin'</span>
   &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.count === <span class="hljs-number">2</span>) &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-number">666</span>
   &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-number">888</span>
   &#125;
 &#125;
&#125;

<span class="hljs-built_in">console</span>.log(a == <span class="hljs-string">'juejin'</span> && a == <span class="hljs-number">666</span> && a == <span class="hljs-number">888</span>)  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此就实现了标题中的表达式为 true。</p></div>  
</div>
            