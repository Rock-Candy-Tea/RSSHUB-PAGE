
---
title: 'D 语言 _ DLang 2.100.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8092'
author: 开源中国
comments: false
date: Tue, 17 May 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8092'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px; margin-right:0px; text-align:start">D 语言 / DLang 2.100.0 已正式发布。此版本包<span style="background-color:#ffffff; color:#663333">含 22 个主要更改和 179 个已修复的 Bugzilla 问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">主要变化</p> 
<ul> 
 <li style="text-align:left">改进<span style="background-color:#ffffff; color:#333333"><span> </span>C++ header gen</span></li> 
 <li style="text-align:left"><code>@mustuse</code>强制返回类型错误检查的新属性</li> 
 <li style="text-align:left">支持 contract 不变版本标识符</li> 
 <li>添加 <span><span>.tupleof<strong> </strong></span></span>静态数组的属性</li> 
 <li style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.100.0.html%23zlib" target="_blank">Zlib 更新到 1.2.12</a></li> 
 <li style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.100.0.html%23std_functional_bind" target="_blank">std.functional</a> 引入新函数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.100.0.html%23std_functional_bind" target="_blank"><span> </span>bind</a></li> 
 <li style="text-align:left">引入不可传递的 inout 返回，以及更多改进</li> 
</ul> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>使用 ImportC 在 C 源码中导入 D 代码模块</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从 D 2.099.0 开始，可通过<code>__import</code><span> </span>关键字直接将 D 代码模块导入 C 文件。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d">// dsayhello.d</span>
<span style="color:#d73a49">import</span> core.stdc.stdio : <span>puts</span>;

<span style="color:#d73a49">extern</span>(C) <span><span style="color:#d73a49">void</span> <span style="color:#6f42c1">helloImport</span><span>()</span> </span>&#123;
    <span>puts</span>(<span style="color:#032f62">"Hello __import!"</span>);
&#125;</code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d">// dhelloimport.c</span>
__import dsayhello;
__import core.stdc.stdio : <span>puts</span>;

<span><span style="color:#d73a49">int</span> <span style="color:#6f42c1">main</span><span>(<span style="color:#d73a49">int</span> argc, <span style="color:#d73a49">char</span>** argv)</span> </span>&#123;
    helloImport();
    <span>puts</span>(<span style="color:#032f62">"Cool, eh?"</span>);
    <span style="color:#d73a49">return</span> <span>0</span>;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用如下代码进行编译：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">dmd</span> <span style="color:#d73a49">dhelloimport</span><span style="color:#6f42c1">.c</span> <span style="color:#d73a49">dsayhello</span><span style="color:#6f42c1">.d</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此外还可导入已经通过 ImportC 编译过的 C 代码模块：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d">// csayhello.c</span>
__import core.stdc.stdio : <span>puts</span>;

<span><span style="color:#d73a49">void</span> <span style="color:#6f42c1">helloImport</span><span>()</span> </span>&#123;
    <span>puts</span>(<span style="color:#032f62">"Hello _import!"</span>);
&#125;</code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d">// chelloimport.c</span>
__import csayhello;
__import core.stdc.stdio : <span>puts</span>;

<span><span style="color:#d73a49">int</span> <span style="color:#6f42c1">main</span><span>(<span style="color:#d73a49">int</span> argc, <span style="color:#d73a49">char</span>** argv)</span> </span>&#123;
    helloImport();
    <span>puts</span>(<span style="color:#032f62">"Cool, eh?"</span>);
    <span style="color:#d73a49">return</span> <span>0</span>;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用如下代码进行编译：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">dmd</span> <span style="color:#d73a49">chelloimport</span><span style="color:#6f42c1">.c</span> <span style="color:#d73a49">csayhello</span><span style="color:#6f42c1">.c</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>引入抛出表达式 (throw expression)</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在 D 语言的生命周期中，<code>throw</code><span> </span>属于声明 (statement )，不能在表达式中使用，因为表达式必须有一个类型，而由于<span> </span><code>throw</code><span> </span>不返回值，所以没有合适的类型，这导致它不能使用以下语法。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>(string err) => <span style="color:#d73a49">throw</span> <span style="color:#d73a49">new</span> <span style="color:#d73a49">Exception</span>(err);</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">只能使用如下的方案：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>(<span>string</span> err) &#123; <span style="color:#d73a49">throw</span> <span style="color:#d73a49">new</span> Exception(err); &#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">不过从 D 2.099.0 开始，以下代码片段可通过编译：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">void</span> foo(int <span><span style="color:#d73a49">function</span>() <span style="color:#6f42c1">f</span>) </span>&#123;&#125;

<span style="color:#d73a49">void</span> main() &#123;
    foo(<span><span>()</span> =></span> <span style="color:#d73a49">throw</span> <span style="color:#d73a49">new</span> Exception());
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.100.0.html" target="_blank">详情查看 Changelog</a>。</p>
                                        </div>
                                      
</div>
            