
---
title: '如何正确判断JS的数据类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=316'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 01:40:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=316'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 25 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>Javascript是一门动态类型的语言，一个变量从声明到最后使用，可能经过了很多个函数，而数据类型也会发生改变，那么，对一个变量的数据类型判断就显得尤为重要。</p>
<h2 data-id="heading-1">typeof是否能正确判断类型？</h2>
<p>由于由于历史原因，在判断原始类型时，<code>typeof null</code>会等于<code>object</code>。而且对于对象（Object）、数组（Array）来说，都会转换成<code>object</code>。例子如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">typeof</span> <span class="hljs-number">1</span> <span class="hljs-comment">// 'number'</span>
    <span class="hljs-keyword">typeof</span> <span class="hljs-string">"1"</span> <span class="hljs-comment">// 'string'</span>
    <span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span> <span class="hljs-comment">// 'object'</span>
    <span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 'undefined'</span>
    
    <span class="hljs-keyword">typeof</span> [] <span class="hljs-comment">// 'object'</span>
    <span class="hljs-keyword">typeof</span> &#123;&#125; <span class="hljs-comment">// 'object'</span>
    <span class="hljs-keyword">typeof</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 'function'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们可以发现，typeof可以判断基本数据类型，但是难以判断除了函数以外的复杂数据类型。于是我们可以使用第二种方法，通常用来判断复杂数据类型，也可以用来判断基本数据类型。</p>
<p>对于返回值为<code>object</code>，有三种情况：</p>
<ul>
<li>值为null</li>
<li>值为object</li>
<li>值为array</li>
</ul>
<p>对于null，我们可以直接用===来进行判断，那么数组和对象呢？不急，我们接着说。</p>
<h2 data-id="heading-2">instanceof是否能正确判断类型？</h2>
<p><code>instanceof</code>是通过原型链来判断的，但是对于对象来说，<code>Array</code>也会被转换成<code>Object</code>，而且也不能区分基本类型<code>string</code>和<code>boolean</code>。可以左边放你要判断的内容，右边放类型来进行JS类型判断，只能用来判断复杂数据类型,因为instanceof 是用于检测构造函数（右边）的 prototype 属性是否出现在某个实例对象（左边）的原型链上。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Func</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
    <span class="hljs-keyword">const</span> func = <span class="hljs-keyword">new</span> Func()
    <span class="hljs-built_in">console</span>.log(func <span class="hljs-keyword">instanceof</span> Func) <span class="hljs-comment">// true</span>
    
    <span class="hljs-keyword">const</span> obj = &#123;&#125;
    <span class="hljs-keyword">const</span> arr = []
    obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> <span class="hljs-comment">// true</span>
    arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> <span class="hljs-comment">// true</span>
    arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> <span class="hljs-comment">// true</span>
    
    <span class="hljs-keyword">const</span> str = <span class="hljs-string">"abc"</span>
    <span class="hljs-keyword">const</span> str2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">"abc"</span>)
    str <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span> <span class="hljs-comment">// false</span>
    str2 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单独使用<code>instanceof</code>好像也是不行的，但是我们对于typeof已经得出结论，不能区分数组和对象，那么，我们结合下<code>instanceof</code>，来写一个完整的判断逻辑</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myTypeof</span>(<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">const</span> type = <span class="hljs-keyword">typeof</span> data
        <span class="hljs-keyword">if</span> (data === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'null'</span>
        &#125;
        <span class="hljs-keyword">if</span> (type !== <span class="hljs-string">'object'</span>) &#123;
            <span class="hljs-keyword">return</span> type
        &#125;
        <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'array'</span>
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'object'</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Object.prototype.toString.call()</h2>
<p>上面我们通过<code>typeof</code>和<code>instanceof</code>实现了一版类型判断，那么是否有其他渠道，使我们的代码更加简洁吗？答案就是使用<code>Object.prototype.toString.call()</code>。</p>
<p>每个对象都有一个<code>toString()</code>方法，当要将对象表示为文本值或以预期字符串的方式引用对象时，会自动调用该方法。默认情况下，从<code>Object</code>派生的每个对象都会继承<code>toString()</code>方法。如果此方法未在自定义对象中被覆盖，则<code>toString()</code>返回<code>[Object type]</code>，其中<code>type</code>是对象类型。所以就有以下例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// [object Date]</span>
    <span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">"1"</span>) <span class="hljs-comment">// [object String]</span>
    <span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>) <span class="hljs-comment">// [object Numer]</span>
    <span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// [object Undefined]</span>
    <span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">null</span>) <span class="hljs-comment">// [object Null]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以综合上述知识点，我们可以封装出以下通用类型判断方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myTypeof</span>(<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">var</span> toString = <span class="hljs-built_in">Object</span>.prototype.toString;
        <span class="hljs-keyword">var</span> dataType = data <span class="hljs-keyword">instanceof</span> Element ? <span class="hljs-string">"element"</span> : toString.call(data).replace(<span class="hljs-regexp">/\[object\s(.+)\]/</span>, <span class="hljs-string">"$1"</span>).toLowerCase()
        <span class="hljs-keyword">return</span> dataType
    &#125;;

    myTypeof(<span class="hljs-string">"a"</span>) <span class="hljs-comment">// string</span>
    myTypeof(<span class="hljs-number">1</span>) <span class="hljs-comment">// number</span>
    myTypeof(<span class="hljs-built_in">window</span>) <span class="hljs-comment">// window</span>
    myTypeof(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"h1"</span>)) <span class="hljs-comment">// element</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">constructor</h2>
<p>constructor 判断方法跟instanceof相似,但是constructor检测Object与instanceof不一样,constructor还可以处理基本数据类型的检测,不仅仅是对象类型。</p>
<p>注意:</p>
<p>1.null和undefined没有constructor;
2.判断数字时使用(),比如  (123).constructor,如果写成123.constructor会报错
3.constructor在类继承时会出错,因为Object被覆盖掉了,检测结果就不对了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
    A.prototype = <span class="hljs-keyword">new</span> B();
    <span class="hljs-built_in">console</span>.log(A.constructor === B)  <span class="hljs-comment">// false</span>

    <span class="hljs-keyword">var</span> C = <span class="hljs-keyword">new</span> A();
    <span class="hljs-built_in">console</span>.log(C.constructor === B)  <span class="hljs-comment">// true</span>
    <span class="hljs-built_in">console</span>.log(C.constructor === A)  <span class="hljs-comment">// false </span>

    C.constructor = A;
    <span class="hljs-built_in">console</span>.log(C.constructor === A);  <span class="hljs-comment">// true</span>
    <span class="hljs-built_in">console</span>.log(C.constructor === B);  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Array.isArray()</h2>
<p>Array.isArray() 用于确定传递的值是否是一个 Array。如果对象是 Array ，则返回true，否则为false。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-built_in">Array</span>.isArray([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// true</span>
    <span class="hljs-built_in">Array</span>.isArray(&#123;<span class="hljs-attr">foo</span>: <span class="hljs-number">123</span>&#125;); <span class="hljs-comment">// false</span>
    <span class="hljs-built_in">Array</span>.isArray(<span class="hljs-string">"foobar"</span>); <span class="hljs-comment">// false</span>
    <span class="hljs-built_in">Array</span>.isArray(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">正则判断</h2>
<p>我们可以把对象和数组转成一个字符串，这样就可以做格式判断，从而得到最终的类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myTypeof</span>(<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-keyword">const</span> str = <span class="hljs-built_in">JSON</span>.stringify(data)
        <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^&#123;.*&#125;$/</span>.test(data)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'object'</span>
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^\[.*\]$/</span>.test(data)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'array'</span>
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            