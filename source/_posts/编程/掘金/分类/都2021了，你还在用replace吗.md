
---
title: '都2021了，你还在用replace吗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3552'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 03:16:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=3552'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言：你是否有这样的困扰：想用一个指定的字符串替换原字符串中的所有满足条件的部分，比如用“*”替换“aabbccda”中所有的字符‘a’，然后查遍String的所有方法，只找到replace方法，但是replace只能替换第一个符合的字符a，只能通过其他的一些方式进行全部替换。js中怎么没有全部替换的方法呢？那么，今天它来了--replaceAll。</p>
</blockquote>
<ul>
<li>String.prototype.replace的局限性</li>
</ul>
<p>正如前言所说，当我们想要将字符串“aabbccda”中的“a”替换为“*”时，想到的方法是replace，但是看一下replace方法的定义：</p>
<blockquote>
<p>replace() 方法返回一个由替换值（replacement）替换部分或所有的模式（pattern）匹配项后的新字符串。模式可以是一个字符串或者一个正则表达式，替换值可以是一个字符串或者一个每次匹配都要调用的回调函数。如果pattern是字符串，则仅替换第一个匹配项。</p>
</blockquote>
<p>所以，如果直接用replace方法替换，则只会替换第一个满足条件的值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'aabbccda'</span>.replace(<span class="hljs-string">'a'</span>, <span class="hljs-string">'*'</span>); <span class="hljs-comment">// "*abbccda"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么如何才能全部替换出现的“a”？以下提供两种常用的方法：<br>
（1）正则表达式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'aabbccda'</span>.replace(<span class="hljs-regexp">/a/g</span>, <span class="hljs-string">'*'</span>); <span class="hljs-comment">// "**bbccd*"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）字符串的split方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'aabbccda'</span>.split(<span class="hljs-string">'a'</span>).join(<span class="hljs-string">'*'</span>); <span class="hljs-comment">// "**bbccd*"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然上面两种方式可以达到全部替换的目的，那么有没有更直接的方法呢？</p>
<ul>
<li>String.prototype.replaceAll</li>
</ul>
<p>replaceAll方法目前处于stage4阶段，预计会在ES2021发布。它的使用方法很简单，和replace一样：</p>
<blockquote>
<p>replaceAll() 方法返回一个新字符串，新字符串所有满足 pattern 的部分都已被replacement 替换。pattern可以是一个字符串或一个 RegExp， replacement可以是一个字符串或一个在每次匹配被调用的函数。原始字符串保持不变。</p>
</blockquote>
<p>语法：</p>
<blockquote>
<p>const newStr = str.replaceAll(regexp|substr, newSubstr|function)</p>
</blockquote>
<p>那么，前面提到的问题就可以用replaceAll方法解决：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'aabbccda'</span>.replaceAll(<span class="hljs-string">'a'</span>, <span class="hljs-string">'*'</span>); <span class="hljs-comment">// "**bbccd*"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很简单，但是使用replaceAll方法时需要注意一点：</p>
<blockquote>
<p>特别注意📢：如果regexp|substr为一个非全局的正则表达式，则replaceAll抛出错误。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">'aabbccda'</span>.replaceAll(<span class="hljs-regexp">/a/</span>, <span class="hljs-string">'*'</span>); <span class="hljs-comment">// Uncaught TypeError: String.prototype.replaceAll called with a non-global RegExp argument</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么会报错呢？</p>
<blockquote>
<p>replaceAll方法是替换所有的，但是正则表达式是非全局的，所以编译器不知道要怎么处理了，所以会报错。</p>
</blockquote>
<ul>
<li>以上就是replaceAll的使用方法，你学会了吗？</li>
</ul></div>  
</div>
            