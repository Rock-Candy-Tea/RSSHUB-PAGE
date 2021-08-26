
---
title: 'typescript入门笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4926'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:39:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=4926'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">联合类型(Union Types)<br></h2>
<p>使用<code>|</code>分隔的每个类型.<br></p>
<p>注意事项：<strong>当联合类型不确定是哪个类型时，只能访问联合类型的所有属性的共有属性或方法。</strong><br>
当访问独有类型时，ts会发出报错。那么，怎么进行类型保护呢？<br><br></p>
<ol>
<li>使用类型断言.<br></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">interface A &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'g'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">21</span>
&#125;
interface B &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'j'</span>,
  <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params">arg: A | B</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(arg.name === <span class="hljs-string">'g'</span>) &#123; <span class="hljs-comment">// 利用共有属性，逻辑上判断</span>
    <span class="hljs-built_in">console</span>.log((arg <span class="hljs-keyword">as</span> A).age)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log((arg <span class="hljs-keyword">as</span> B).sex)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用<code>in</code>语法</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func2</span>(<span class="hljs-params">arg: A | B</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-string">'age'</span> <span class="hljs-keyword">in</span> arg) &#123;
    <span class="hljs-built_in">console</span>.log(arg.age)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(arg.sex)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用<code>typeof</code></li>
<li>使用 instanceof</li>
</ol>
<p>等可以明确判断其是哪个类型时，就可以去除ts报错</p>
<h2 data-id="heading-1">枚举类型</h2>
<p>使用<code>enum</code>关键字定义。</p>
<pre><code class="hljs language-js copyable" lang="js">    enum Name &#123;
        A,
        B
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>默认情况下，枚举的类型是从0开始的。可以手动赋值来修改。<strong>没赋值的后面元素依次增加</strong>。<br></li>
<li><strong>枚举类型可以反向取值：<code>Name.A <==> Name[0]</code><br></strong></li>
<li><strong>注意：若是没赋值的元素(其值由依次增加而来).与已赋值的元素相同，ts并不会知道。且后面的元素会覆盖前面的元素</strong></li>
</ul>
<h2 data-id="heading-2">泛型</h2>
<h3 data-id="heading-3">函数泛型</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span><<span class="hljs-title">T</span>> (<span class="hljs-params">arg: T</span>) </span>&#123;
        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">类泛型</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">cls</span><<span class="hljs-title">T</span>> </span>&#123;
        
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>泛型主要是指，在<strong>定义</strong>函数，类或接口时<strong>不指定</strong>具体类型，而在<strong>使用时再指定类型的一种特性</strong>。<br>
<strong>可以使用<code>extends</code>约束泛型</strong>！<br>
比如：约束指定的泛型类型包含<code>name</code>属性</p>
<pre><code class="hljs language-js copyable" lang="js">    interface HasName &#123; <span class="hljs-comment">// </span>
        <span class="hljs-attr">name</span>: string
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">HasName</span>> </span>&#123;
        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再比如：约束泛型类型时<code>number</code>或者<code>string</code></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">number</span> | <span class="hljs-title">string</span>> (<span class="hljs-params"></span>) </span>&#123;
        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>keyof</code>来约束泛型只能取某些<strong>值</strong></p>
<blockquote>
<p><strong>interface</strong> 和 <strong>元组</strong> 的相似之处？</p>
<p><strong>interface</strong> 和 <strong>类型别名</strong> 的区别之处？</p>
<p><strong>函数</strong>有哪几种表现形式？</p>
</blockquote></div>  
</div>
            