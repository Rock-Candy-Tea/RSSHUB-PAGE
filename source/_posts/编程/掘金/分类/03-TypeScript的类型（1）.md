
---
title: '03-TypeScript的类型（1）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3159'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 01:35:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=3159'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上一节说了类型声明的语法， 我们接着学习更多的变量类型</p>
<ul>
<li>
<p>字面类型， 举例</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> a: <span class="hljs-string">"male"</span> | <span class="hljs-string">"female"</span> <span class="hljs-comment">// a的类型只能是male或female， 即</span>
a = <span class="hljs-string">"male"</span> <span class="hljs-comment">// 正确</span>
a = <span class="hljs-string">"female"</span> <span class="hljs-comment">// 正确</span>
a = <span class="hljs-string">"hello"</span> <span class="hljs-comment">// 错误， a不能是除male或female之外的值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>any类型， 表示任意类型， 举例</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 显式声明变量为any类型（不建议）</span>
<span class="hljs-keyword">let</span> a: <span class="hljs-built_in">any</span>;
a = <span class="hljs-string">"hello"</span> <span class="hljs-comment">// 正确</span>
a = <span class="hljs-number">1</span> <span class="hljs-comment">// 正确</span>
a = <span class="hljs-literal">true</span> <span class="hljs-comment">// 正确</span>

<span class="hljs-comment">// 隐式声明变量为any类型（不建议）</span>
<span class="hljs-keyword">let</span> b;
b = <span class="hljs-number">1</span>
b = <span class="hljs-string">"hello"</span>
b = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明变量为any类型， 可以给变量赋任意类型的值。 可以理解为， 声明变量为any类型， 即关闭了编译器对变量类型的检验， 同JavaScript。 使用TS时， 不建议将变量声明为any类型。</p>
</li>
<li>
<p>unknown类型， 表示未知类型， 类型安全的any， 举例</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">any</span>
a = <span class="hljs-number">1</span>
a = <span class="hljs-string">"hello"</span>
a = <span class="hljs-literal">true</span>

<span class="hljs-keyword">let</span> b: unknown
b = <span class="hljs-number">1</span>
b = <span class="hljs-string">"hello"</span>
b = <span class="hljs-literal">true</span>

<span class="hljs-keyword">let</span> s: <span class="hljs-built_in">string</span>
s = a <span class="hljs-comment">// 正确</span>
s = b <span class="hljs-comment">// 错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unknown类型与any类型的区别</p>
<p>相同点： 声明为unknown类型的变量和声明为any类型的变量， 可以给变量赋任意类型的值</p>
<p>不同点： any类型的变量， 可以赋值给任意类型的变量</p>
<p>​           unknown类型的变量， 不可以赋值给其他类型的变量</p>
<p>变量s本来是string类型， 变量a赋给s后变成了boolean类型， any类型不仅祸祸自己， 还祸祸其他人。 所以非常不建议把变量声明为any类型。如有需求把unknown变量赋给其他类型变量， 可以这样做</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 第一种， if判断</span>
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">type</span> b === <span class="hljs-string">"string"</span>) &#123;
s = b
&#125;

<span class="hljs-comment">// 第二种， 类型断言, 两种用法</span>
s = b <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>
s = <<span class="hljs-built_in">string</span>>b
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>void类型， 表示返回值为空， 举例</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"返回值为空"</span>)
&#125;

<span class="hljs-comment">// 可以返回undefined</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>never类型， 表示永远不会有返回结果, 也不能返回undefined， 用的很少， 了解即可</p>
</li>
</ul></div>  
</div>
            