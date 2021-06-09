
---
title: 'String字符串编码知识点笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5302'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 20:25:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=5302'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">fromCharCode</h3>
<p>用指定UTF-16 码点创建字符串，我们来试验一下</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">65</span>);<span class="hljs-comment">// A</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是它的参数值的范围介于 0 到 65535之间，用16进制来表示就是 0xFFFF，大于这个值的话，最高位将被截断，我们来试验一下</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">0xF680</span>);<span class="hljs-comment">// \f680</span>
<span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-number">0x1F680</span>);<span class="hljs-comment">// \f680</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这两个输出都是一样的，如果我就是想用0x1F680怎么办呢？</p>
<h3 data-id="heading-1">formCodePoint</h3>
<p>ES提供了formCodePoint这个方法，它的参数值范围介于0到1048575，用16进制表示就是0xFFFFF，比fromCharCode多了一个F，来运行一下</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">String</span>.fromCodePoint(<span class="hljs-number">0x1F680</span>);<span class="hljs-comment">// 🚀</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">charCodeAt</h3>
<p>这个方法是取字符串上指定位置的UTF-16值的，我们来试验一下</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-string">'ABC'</span>.charCodeAt(<span class="hljs-number">0</span>);<span class="hljs-comment">// 65</span>
<span class="hljs-string">'ABC'</span>.charCodeAt(<span class="hljs-number">1</span>);<span class="hljs-comment">// 66</span>
<span class="hljs-string">'ABC'</span>.charCodeAt(<span class="hljs-number">2</span>);<span class="hljs-comment">// 67</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和fromCharCode对应，charCodeAt也只能取最大值0xFFFF的码点，如果要取超过0xFFFF对应的UTF-16码点需要用到codePointAt</p>
<h3 data-id="heading-3">codePointAt</h3>
<p>先看一下以下代码</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-string">'🚀'</span>.charCodeAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>);<span class="hljs-comment">// d83d</span>
<span class="hljs-string">'🚀'</span>.codePointAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>);<span class="hljs-comment">// 1f680</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>JavaScript 内部，字符以 UTF-16 的格式储存，每个字符固定为2个字节。对于Unicode 码点大于0xFFFF的字符，需要用4个字节来存储，JavaScript 会认为它们是两个字符。</p>
</blockquote>
<p>因此呢🚀的length会被识别为2，如果想获取'🚀A'中'A'的编码，需要用到'🚀A'.codePointAt(2)才可以</p>
<p>所以我们要避免这个问题，就不能用for循环来处理of活扩展运算符来处理</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'🚀A'</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> ch <span class="hljs-keyword">of</span> str) &#123;
  <span class="hljs-built_in">console</span>.log(ch.codePointAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>));
&#125;

<span class="hljs-keyword">let</span> arr = [...str];
arr.forEach(
  <span class="hljs-function"><span class="hljs-params">ch</span> =></span> <span class="hljs-built_in">console</span>.log(ch.codePointAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>))
);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            