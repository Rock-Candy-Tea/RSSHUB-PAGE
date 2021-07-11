
---
title: 'TypeScript——迭代器和生成器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5265'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 00:24:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=5265'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<h2 data-id="heading-0">可迭代性</h2>
<p>当一个对象实现了Symbol.iterator属性时，我们认为它是可迭代的。 一些内置的类型如 Array，Map，Set，String，Int32Array，Uint32Array等都已经实现了各自的Symbol.iterator。 对象上的 Symbol.iterator函数负责返回供迭代的值。</p>
<h3 data-id="heading-1">for..of 语句</h3>
<p>for..of会遍历可迭代的对象，调用对象上的Symbol.iterator方法。 下面是在数组上使用 for..of的简单例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someArray = [<span class="hljs-number">1</span>, <span class="hljs-string">"string"</span>, <span class="hljs-literal">false</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> entry <span class="hljs-keyword">of</span> someArray) &#123;
    <span class="hljs-built_in">console</span>.log(entry); <span class="hljs-comment">// 1, "string", false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">for..of vs. for..in 语句</h4>
<p>for..of和for..in均可迭代一个列表；但是用于迭代的值却不同，for..in迭代的是对象的 键 的列表，而for..of则迭代对象的键对应的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> list = [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> list) &#123;
    <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// "0", "1", "2",</span>
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> list) &#123;
    <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// "4", "5", "6"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个区别是for..in可以操作任何对象；它提供了查看对象属性的一种方法。 但是 for..of关注于迭代对象的值。内置对象Map和Set已经实现了Symbol.iterator方法，让我们可以访问它们保存的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> pets = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"Cat"</span>, <span class="hljs-string">"Dog"</span>, <span class="hljs-string">"Hamster"</span>]);
pets[<span class="hljs-string">"species"</span>] = <span class="hljs-string">"mammals"</span>;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> pet <span class="hljs-keyword">in</span> pets) &#123;
    <span class="hljs-built_in">console</span>.log(pet); <span class="hljs-comment">// "species"</span>
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> pet <span class="hljs-keyword">of</span> pets) &#123;
    <span class="hljs-built_in">console</span>.log(pet); <span class="hljs-comment">// "Cat", "Dog", "Hamster"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">代码生成</h2>
<h3 data-id="heading-4">目标为 ES5 和 ES3</h3>
<p>当生成目标为ES5或ES3，迭代器只允许在Array类型上使用。 在非数组值上使用 for..of语句会得到一个错误，就算这些非数组值已经实现了Symbol.iterator属性。</p>
<p>编译器会生成一个简单的for循环做为for..of循环，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> num <span class="hljs-keyword">of</span> numbers) &#123;
    <span class="hljs-built_in">console</span>.log(num);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的代码为：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> _i = <span class="hljs-number">0</span>; _i < numbers.length; _i++) &#123;
    <span class="hljs-keyword">var</span> num = numbers[_i];
    <span class="hljs-built_in">console</span>.log(num);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">目标为 ECMAScript 2015 或更高</h3>
<p>当目标为兼容ECMAScipt 2015的引擎时，编译器会生成相应引擎的for..of内置迭代器实现方式。</p>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            