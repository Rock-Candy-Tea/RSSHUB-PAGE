
---
title: 'TypeScript——Symbols'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1463'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 00:06:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1463'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<h1 data-id="heading-0">Symbols</h1>
<h2 data-id="heading-1">介绍</h2>
<p>自ECMAScript 2015起，symbol成为了一种新的原生类型，就像number和string一样。</p>
<p>symbol类型的值是通过Symbol构造函数创建的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> sym1 = <span class="hljs-built_in">Symbol</span>();

<span class="hljs-keyword">let</span> sym2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"key"</span>); <span class="hljs-comment">// 可选的字符串key</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Symbols是不可改变且唯一的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> sym2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"key"</span>);
<span class="hljs-keyword">let</span> sym3 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"key"</span>);

sym2 === sym3; <span class="hljs-comment">// false, symbols是唯一的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像字符串一样，symbols也可以被用做对象属性的键。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> sym = <span class="hljs-built_in">Symbol</span>();

<span class="hljs-keyword">let</span> obj = &#123;
    [sym]: <span class="hljs-string">"value"</span>
&#125;;

<span class="hljs-built_in">console</span>.log(obj[sym]); <span class="hljs-comment">// "value"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Symbols也可以与计算出的属性名声明相结合来声明对象的属性和类成员。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getClassNameSymbol = <span class="hljs-built_in">Symbol</span>();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    [getClassNameSymbol]()&#123;
       <span class="hljs-keyword">return</span> <span class="hljs-string">"C"</span>;
    &#125;
&#125;

<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> C();
<span class="hljs-keyword">let</span> className = c[getClassNameSymbol](); <span class="hljs-comment">// "C"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">众所周知的Symbols</h2>
<p>除了用户定义的symbols，还有一些已经众所周知的内置symbols。 内置symbols用来表示语言内部的行为。</p>
<p>以下为这些symbols的列表：</p>
<ul>
<li>Symbol.hasInstance</li>
</ul>
<p>方法，会被instanceof运算符调用。构造器对象用来识别一个对象是否是其实例。</p>
<ul>
<li>Symbol.isConcatSpreadable</li>
</ul>
<p>布尔值，表示当在一个对象上调用Array.prototype.concat时，这个对象的数组元素是否可展开。</p>
<ul>
<li>Symbol.iterator</li>
</ul>
<p>方法，被for-of语句调用。返回对象的默认迭代器。</p>
<ul>
<li>Symbol.match</li>
</ul>
<p>方法，被String.prototype.match调用。正则表达式用来匹配字符串。</p>
<ul>
<li>Symbol.replace</li>
</ul>
<p>方法，被String.prototype.replace调用。正则表达式用来替换字符串中匹配的子串。</p>
<ul>
<li>Symbol.search</li>
</ul>
<p>方法，被String.prototype.search调用。正则表达式返回被匹配部分在字符串中的索引。</p>
<ul>
<li>Symbol.species</li>
</ul>
<p>函数值，为一个构造函数。用来创建派生对象。</p>
<ul>
<li>Symbol.split</li>
</ul>
<p>方法，被String.prototype.split调用。正则表达式来用分割字符串。</p>
<ul>
<li>Symbol.toPrimitive</li>
</ul>
<p>方法，被ToPrimitive抽象操作调用。把对象转换为相应的原始值。</p>
<ul>
<li>Symbol.toStringTag</li>
</ul>
<p>方法，被内置方法Object.prototype.toString调用。返回创建对象时默认的字符串描述。</p>
<ul>
<li>Symbol.unscopables</li>
</ul>
<p>对象，它自己拥有的属性会被with作用域排除在外。</p>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            