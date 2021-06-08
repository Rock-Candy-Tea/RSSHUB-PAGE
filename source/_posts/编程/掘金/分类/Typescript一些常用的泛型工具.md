
---
title: 'Typescript一些常用的泛型工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4522'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:46:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=4522'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文将简要介绍Typescript一些常用泛型工具的作用以及如何使用，简单总结了一下。</p>
<h2 data-id="heading-1">Typescript泛型工具</h2>
<ul>
<li>
<p><strong>Partial</strong></p>
<p>将传入的属性变为可选项</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IPeople &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    name: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">const</span> people: Partial<IPeople> = &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'Delete inactive users'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Record<K, T></strong></p>
<p>类型参数K提供了对象属性名联合类型，类型参数T提供了对象属性的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// 将x, y 作为Person的key</span>
<span class="hljs-keyword">type</span> Peoples = Record<<span class="hljs-string">"x"</span> | <span class="hljs-string">"y"</span>, Person>;

<span class="hljs-keyword">const</span> P: Peoples = &#123;
    <span class="hljs-attr">x</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>
    &#125;,
    <span class="hljs-attr">y</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'李四'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Readonly</strong></p>
<p>把传入的类型变为只读状态</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> p: Readonly<Person> = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>
&#125;

p.name = <span class="hljs-string">'李四'</span>; <span class="hljs-comment">// 无法分配到 "name" ，因为它是只读属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Required</strong></p>
<p>把传入的类型变为必填状态</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    name?: <span class="hljs-built_in">string</span>;
    age?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> p: Required<Person> = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Pick<T, S></strong></p>
<p>在 T 中，过滤掉非 S 的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IPerson &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> TP = Pick<IPerson, <span class="hljs-string">'name'</span>>;

<span class="hljs-keyword">const</span> p: TP = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>, <span class="hljs-comment">// 对象文字可以只指定已知属性，并且“age”不在类型“TP”中</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Omit<T, K></strong></p>
<p>在 T 中删除对应的 K</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IPerson &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> TP = Omit<IPerson, <span class="hljs-string">'age'</span>>;

<span class="hljs-keyword">const</span> p: TP = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Exclude<T, U></strong></p>
<p>该工具类型能够从类型T中剔除所有可以赋值给类型U的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T0 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span>>;
<span class="hljs-comment">// 相当于 type T0 = "b" | "c"</span>

<span class="hljs-keyword">type</span> T1 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>;
<span class="hljs-comment">// 相当于 type T1 = "c"</span>

<span class="hljs-keyword">type</span> T2 = Exclude<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>;
<span class="hljs-comment">// 相当于 type T2 = string | number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Extract<T, U></strong></p>
<p>“Extract<T, U>”工具类型与“Exclude<T, U>”工具类型是互补的，它能够从类型T中获取所有可以赋值给类型U的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T0 = Extract<<span class="hljs-string">'a'</span> | <span class="hljs-string">'b'</span> | <span class="hljs-string">'c'</span>, <span class="hljs-string">'a'</span> | <span class="hljs-string">'f'</span>>;
<span class="hljs-comment">// 相当于 type T0 = 'a';</span>

<span class="hljs-keyword">type</span> T1 = Extract<<span class="hljs-built_in">string</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>;
<span class="hljs-comment">// 相当于 type T1 = () => void;</span>

<span class="hljs-keyword">type</span> T2 = Extract<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>, <span class="hljs-built_in">boolean</span>>;
<span class="hljs-comment">// 因为没有交集，相当于 type T2 = never;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>ReturnType</strong></p>
<p>该工具类型能够获取函数类型T的返回值类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// string</span>
<span class="hljs-keyword">type</span> T0 = ReturnType<<span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>>;

<span class="hljs-comment">// &#123; a: string; b: number &#125;</span>
<span class="hljs-keyword">type</span> T1 = ReturnType<<span class="hljs-function">() =></span> &#123; <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>; b: <span class="hljs-built_in">number</span>&#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            