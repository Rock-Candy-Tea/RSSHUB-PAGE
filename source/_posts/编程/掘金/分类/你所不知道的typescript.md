
---
title: '你所不知道的typescript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7047'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 03:08:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=7047'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">基础</h2>
<h4 data-id="heading-1">1. 基础类型</h4>
<blockquote>
<ul>
<li>常用：boolean、number、string、array、enum、any、void</li>
<li>不常用：tuple、null、undefine、never</li>
</ul>
</blockquote>
<h6 data-id="heading-2">数组</h6>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> numberArr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-keyword">const</span> arr: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-comment">// 除此之外，还可以使用数组泛型</span>
<span class="hljs-keyword">const</span> _arr: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-keyword">const</span> stringArr: <span class="hljs-built_in">string</span>[] = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];
<span class="hljs-comment">// 如果这个数组里面既存数字又存字符串，如何写</span>
<span class="hljs-keyword">const</span> arr1: (<span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span>)[] = [<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span> ,<span class="hljs-number">3</span>];

<span class="hljs-comment">// 除了基本类型的数组，对象类型的数组怎么写</span>
<span class="hljs-keyword">const</span> objectArr: &#123;<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>&#125;[] = [&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'a'</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">16</span>&#125;]
<span class="hljs-comment">// 将上面的写法简化下，利用 type alias 类型别名</span>
<span class="hljs-keyword">type</span> User = &#123;<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>&#125;
<span class="hljs-keyword">const</span> objectArr1: User[] = [&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'a'</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">16</span>&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. interface 和 type</h4>
<p>参考：<a href="https://juejin.cn/post/6844903799459414029" target="_blank" title="https://juejin.cn/post/6844903799459414029">juejin.cn/post/684490…</a></p>
<ul>
<li>
<p><em>interface</em></p>
<ol>
<li>对象interface
<ol>
<li>设置需要存在的普通属性</li>
<li>设置可选属性</li>
<li>设置只读属性</li>
</ol>
</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    bool?: <span class="hljs-built_in">boolean</span>
    <span class="hljs-keyword">readonly</span> timestamp: <span class="hljs-built_in">number</span>
    <span class="hljs-keyword">readonly</span> arr: ReadonlyArray<<span class="hljs-built_in">number</span>> <span class="hljs-comment">// 此外还有 ReadonlyMap/ReadonlySet</span>
&#125;

<span class="hljs-keyword">let</span> p1: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'oliver'</span>,
    <span class="hljs-attr">bool</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// ✔️️ 可以设置可选属性 并非必要的 可写可不写</span>
    <span class="hljs-attr">timestamp</span>: + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(), <span class="hljs-comment">// ✔️ 设置只读属性</span>
    <span class="hljs-attr">arr</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>] <span class="hljs-comment">// ✔️ 设置只读数组</span>
&#125;

<span class="hljs-keyword">let</span> p: Person = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-string">'oliver'</span>, <span class="hljs-comment">// ❌ 多出来的属性</span>
    <span class="hljs-attr">name</span>: <span class="hljs-number">123</span> <span class="hljs-comment">// ❌ 类型错误</span>
&#125;

p1.timestamp = <span class="hljs-number">123</span> <span class="hljs-comment">// ❌ 只读属性不可修改</span>
p1.arr.pop() <span class="hljs-comment">// ❌ 只读属性不可修改</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>函数 Interface</li>
</ol>
<p>Interface 还可以用来规范函数的形状。Interface 里面需要列出参数列表返回值类型的函数定义。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Func &#123;
<span class="hljs-comment">// ✔️ 定于这个函数接收两个必选参数都是 number 类型，以及一个可选的字符串参数 desc，这个函数不返回任何值</span>
(x: number, <span class="hljs-attr">y</span>: number, desc?: string): <span class="hljs-keyword">void</span>
&#125;

<span class="hljs-keyword">const</span> sum: Func = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">x, y, desc = <span class="hljs-string">''</span></span>) </span>&#123;
    <span class="hljs-comment">// const sum: Func = function (x: number, y: number, desc: string): void &#123;</span>
    <span class="hljs-comment">// ts类型系统默认推论可以不必书写上述类型定义</span>
    <span class="hljs-built_in">console</span>.log(desc, x + y)
&#125;

sum(<span class="hljs-number">32</span>, <span class="hljs-number">22</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><em>type</em></p>
<pre><code class="hljs language-js copyable" lang="js">type User = &#123;
    <span class="hljs-attr">name</span>: string
    <span class="hljs-attr">age</span>: number
&#125;;

type SetUser = <span class="hljs-function">(<span class="hljs-params">name: string, age: number</span>) =></span> <span class="hljs-keyword">void</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">user: User</span>) </span>&#123;
    <span class="hljs-keyword">return</span> user.name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-4">相同点</h5>
<p><strong>1. 都允许拓展</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// interface extends interface</span>
<span class="hljs-keyword">interface</span> Name &#123; 
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; 
&#125;
<span class="hljs-keyword">interface</span> User <span class="hljs-keyword">extends</span> Name &#123; 
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-comment">// type extends type</span>
<span class="hljs-keyword">type</span> Name = &#123; 
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; 
&#125;
<span class="hljs-keyword">type</span> User = Name & &#123; <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>  &#125;;

<span class="hljs-comment">// interface extends type</span>
<span class="hljs-keyword">type</span> Name = &#123; 
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; 
&#125;
<span class="hljs-keyword">interface</span> User <span class="hljs-keyword">extends</span> Name &#123; 
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>; 
&#125;

<span class="hljs-keyword">type</span> <span class="hljs-keyword">extends</span> <span class="hljs-keyword">interface</span>
<span class="hljs-keyword">interface</span> Name &#123; 
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; 
&#125;
<span class="hljs-keyword">type</span> User = Name & &#123; 
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">不同点</h5>
<ol>
<li>type 可以声明基本类型别名</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> s = <span class="hljs-built_in">string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>type 语句中还可以使用 typeof 获取实例的 类型进行赋值</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>interface可以合并声明</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> User &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-keyword">interface</span> User &#123;
  <span class="hljs-attr">sex</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-comment">/*
User 接口为 &#123;
  name: string
  age: number
  sex: string 
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">3. enum枚举</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> d1 &#123;
    a,
    b,
    c,
&#125;
<span class="hljs-built_in">enum</span> d1 &#123;
    a,
    b = <span class="hljs-string">'two'</span>,
    c = <span class="hljs-string">'three'</span>,
&#125;

<span class="hljs-comment">// 赋值了非数字的，下一个一定要赋值，除非它是最后一个，例如下面这种情况会报错</span>
<span class="hljs-built_in">enum</span> d1 &#123;
    a,
    b = <span class="hljs-string">'two'</span>,
    c,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4. 泛型 T（Type）</h4>
<p>简单说就是：泛指的类型，不确定的类型，可以理解为一个占位符（使用T只是习惯，使用任何字母都行）</p>
<ul>
<li>K（Key）：表示对象中的键类型；</li>
<li>V（Value）：表示对象中的值类型；</li>
<li>E（Element）：表示元素类型。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span><<span class="hljs-title">T</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result: T[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

createArray<<span class="hljs-built_in">string</span>>(<span class="hljs-number">3</span>, <span class="hljs-string">'x'</span>); <span class="hljs-comment">// ['x', 'x', 'x']</span>

<span class="hljs-comment">// 第一个T相当于一个变量，调用函数时createArray<string>...相当于给T赋值string类型</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            