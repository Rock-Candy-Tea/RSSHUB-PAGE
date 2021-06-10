
---
title: '重学TypeScript，深入常见的TS的`Utility Types`'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7692'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 18:57:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=7692'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 10 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>2021-06-10 TypeScript Utility Types</p>
</blockquote>
<h1 data-id="heading-0">重学TypeScript，深入常见的TS的<code>Utility Types</code></h1>
<h2 data-id="heading-1">1. 了解<code>Utility Types</code> 的热身</h2>
<h3 data-id="heading-2">1.1 <code>keyof</code></h3>
<p>keyof的作用是，假设T是一个类型，那么keyof T产生的类型是T的属性名称字符串字面量类型构成的联合类型。怎么直观理解呢？看下面代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface exampleA &#123;
  <span class="hljs-attr">name</span>:string;
  id:number;
  create:string;
&#125;

type TypeA = keyof exampleA; <span class="hljs-comment">// 其实就相当于 type TypeA = 'name'|'id'|'create'</span>
<span class="hljs-keyword">let</span> b:TypeA = <span class="hljs-string">'name'</span>;
b = <span class="hljs-string">'id'</span>;
<span class="hljs-comment">// b = 'end'; // Type '"end"' is not assignable to type 'keyof exampleA'</span>
<span class="hljs-built_in">console</span>.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.2 <code>in</code>操作符</h3>
<p>in的作用就是遍历联合类型例如</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">type A = <span class="hljs-string">'a'</span>|<span class="hljs-string">'b'</span>|<span class="hljs-string">'c'</span>;
type Obj = &#123;
[p <span class="hljs-keyword">in</span> A]: string
&#125; <span class="hljs-comment">// &#123;a: any, b: any&#125;</span>

<span class="hljs-keyword">const</span> a:Obj = &#123;
  <span class="hljs-attr">a</span>:<span class="hljs-string">'test'</span>,
  <span class="hljs-attr">b</span>:<span class="hljs-string">'test'</span>,
  <span class="hljs-comment">// Property 'c' is missing in type '&#123; a: string; b: string; &#125;' but required in type 'Obj</span>
  <span class="hljs-comment">// c:'test'</span>
&#125;
<span class="hljs-built_in">console</span>.log( a )
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.3 <code>in keyof T</code> 和 <code>extends keyof T</code></h3>
<p>一个是精确匹配查询，一个是包含查询</p>
<h2 data-id="heading-5">2 常用的<code>Utility Types</code></h2>
<h3 data-id="heading-6">2.1 <code>Partial<T></code></h3>
<p>构造一个类型，其所有属性的类型都设置为可选。此实用程序将返回表示给定类型的所有子集的类型。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface A &#123;
  <span class="hljs-attr">name</span>:string;
  id:string
&#125;

<span class="hljs-keyword">let</span> a: Partial<A> = &#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">'tangjie'</span>
&#125;
<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Partial的实现方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">type Partial<T> = &#123;
[K <span class="hljs-keyword">in</span> keyof T]?: T[K];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>功能与之相反的是<code>Required<T></code></p>
<h3 data-id="heading-7">2.2 <code>Pick<Type, Keys></code></h3>
<p>通过从Type中选择属性键集(字符串、文字或字符串文本的联合)来构造类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface A &#123;
  <span class="hljs-attr">id</span>: string;
  name: string;
  age: number;
&#125;
type B = Pick<A, <span class="hljs-string">"name"</span> | <span class="hljs-string">"age"</span>>;

<span class="hljs-keyword">const</span> xiaoming: B = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"xiaoming"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">26</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Pick的实现方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">type Pick<T,K <span class="hljs-keyword">extends</span> keyof T> = &#123;
[P <span class="hljs-keyword">in</span> K]: T;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.3 <code>Omit<Type, Keys></code></h3>
<p>通过选择Type中的所有属性，然后移除键(字符串、文字或字符串文本的联合)来构造类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface A &#123;
  <span class="hljs-attr">id</span>: string;
  name: string;
  age: number;
&#125;

<span class="hljs-keyword">const</span> a:Omit<A,<span class="hljs-string">'id'</span>> = &#123;
<span class="hljs-attr">name</span>:<span class="hljs-string">'tangjie'</span>,
<span class="hljs-attr">age</span>:<span class="hljs-number">18</span>,
<span class="hljs-comment">// id:1 如果加了这个属性就报错</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.4 <code>Parameters<Type></code></h3>
<p>从函数类型类型的参数中使用的类型构造元组类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">declare <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params">arg: &#123; a: number; b: string &#125;</span>): <span class="hljs-title">void</span></span>;
type A = Parameters<<span class="hljs-function">() =></span> string>;<span class="hljs-comment">// 相当于A = []    </span>
type B = Parameters<<span class="hljs-function">(<span class="hljs-params">s: string</span>) =></span> <span class="hljs-keyword">void</span>>;<span class="hljs-comment">// 相当于 B = [s: string]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">3.总结</h2>
<p>ts最难的地方估计也就是对泛型的使用，通过上面的Ts原生支持的<code>Utility Type</code>的实现思路，能够帮我们掌握很多关于泛型使用的细节，更多<code>utility type</code>可以去这个<a href="https://github.com/piotrwitek/utility-types" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>，这个就是第三方的啦~</p></div>  
</div>
            