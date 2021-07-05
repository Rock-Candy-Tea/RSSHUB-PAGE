
---
title: 'TypeScript 断言'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2641'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 08:47:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=2641'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 类型断言</h2>
<p>在使用 <code>TypeScript</code> 的过程中，你可能会遇到这种情况：你比 <code>TypeScript</code> 更加清楚某个值的类型。
比如你从异步请求中拿到一个类型为<code>any</code>的值，但你清楚的知道这个值就是<code>string</code>类型，这个时候你可以通过<strong>类型断言</strong>方式告诉编译器："嘿！相信我，我知道我在干什么！"。类型断言有点类似于其他语言的类型转换，但它没有运行时的影响，只是在编译阶段起作用。
类型断言有两种形式：</p>
<h3 data-id="heading-1">1.1 尖括号语法</h3>
<ul>
<li>形式：<code><类型>变量名</code></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> value: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> length: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>value).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 as 语法</h3>
<ul>
<li>形式：<code>变量名 as 类型</code></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> value: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> length: <span class="hljs-built_in">number</span> = (value <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2. 非空断言</h2>
<p>当你明确知道某个值不可能为 <code>undefined</code> 和 <code>null</code> 时，你可以用 在变量后面加上一个 <code>!</code>（非空断言符号）来告诉编译器："嘿！相信我，我确信这个值不为空！"。
非空断言具体的使用场景如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> str: <span class="hljs-built_in">string</span> = value; <span class="hljs-comment">// error value 可能为 undefined 和 null</span>
  <span class="hljs-keyword">const</span> str: <span class="hljs-built_in">string</span> = value!; <span class="hljs-comment">//ok</span>
  <span class="hljs-keyword">const</span> length: <span class="hljs-built_in">number</span> = value.length; <span class="hljs-comment">// error value 可能为 undefined 和 null</span>
  <span class="hljs-keyword">const</span> length: <span class="hljs-built_in">number</span> = value!.length; <span class="hljs-comment">//ok</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3. 确定赋值断言</h2>
<p><code>TypeScript</code> 的确定赋值断言，允许在实例属性和变量声明后面放置一个 <code>!</code> 号，从而告诉 <code>TypeScript</code> 该属性会被明确地赋值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> name!: <span class="hljs-built_in">string</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述表达式就是对编译器说："有一个名为 <code>name</code> 的属性，其类型为 <code>string | undefined</code>。它以值 <code>undefined</code> 开始。但每次获取或设置该属性时，我都希望将其视为类型 <code>string。</code>"</p>
<p>为了更好地理解它的作用，我们来看个具体的例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> count: <span class="hljs-built_in">number</span>;
initialize();

<span class="hljs-comment">// Variable 'count' is used before being assigned.(2454)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span> * count); <span class="hljs-comment">// Error</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initialize</span>(<span class="hljs-params"></span>) </span>&#123;
  count = <span class="hljs-number">10</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显该异常信息是说变量 <code>count</code> 在赋值前被使用了，要解决该问题，我们可以使用确定赋值断言：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> count!: <span class="hljs-built_in">number</span>;
initialize();
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span> * count); <span class="hljs-comment">// Ok</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initialize</span>(<span class="hljs-params"></span>) </span>&#123;
  count = <span class="hljs-number">10</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4.参考文章</h2>
<ul>
<li><a href="https://typescript.bootcss.com/basic-types.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript 中文手册</a></li>
<li><a href="https://juejin.cn/post/6872111128135073806#heading-28" target="_blank">一份不可多得的 TS 学习指南</a></li>
</ul></div>  
</div>
            