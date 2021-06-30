
---
title: '_JavaScript编码能力_浅拷贝和深拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16165bb6b2f7415eb1718cd3d16e510f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 19:47:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16165bb6b2f7415eb1718cd3d16e510f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">赋值（Copy）</h1>
<p>赋值是将某一数值或对象赋给某个变量的过程，分为两种情况：</p>
<ul>
<li>基本数据类型：赋值，赋值之后两个变量互不影响。</li>
<li>引用数据类型：赋值（引用地址），两个变量具有相同的引用，指向同一个对象，互相之间有影响。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//基本数据类型</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'hello'</span>
<span class="hljs-keyword">let</span> name2 = name
<span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// hello</span>
<span class="hljs-built_in">console</span>.log(name2) <span class="hljs-comment">// hello</span>
name2 = <span class="hljs-string">'hello world'</span>
<span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// hello</span>
<span class="hljs-built_in">console</span>.log(name2) <span class="hljs-comment">// hello world 修改了 name2 的值，不影响 name 的值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内存中有一个变量<code>name</code>，值为<code>hello</code>。我们从变量<code>name</code>复制出一个变量<code>name2</code>，此时在内存中创建了一个块新的空间用于存储<code>hello</code>，虽然两者值是相同的，但是两者指向的内存空间完全不同，这两个变量参与任何操作都互不影响。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'小刘'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    <span class="hljs-attr">info</span>: &#123;
        <span class="hljs-attr">field</span>: [<span class="hljs-string">'JS'</span>, <span class="hljs-string">'CSS'</span>, <span class="hljs-string">'HTML'</span>]
    &#125;
&#125;
<span class="hljs-keyword">let</span> obj2 = obj
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123;name: "小刘", age: 18, info: &#123;field: ["JS", "CSS", "HTML"]&#125;&#125;</span>
<span class="hljs-built_in">console</span>.log(obj2) <span class="hljs-comment">// &#123;name: "小刘", age: 18, info: &#123;field: ["JS", "CSS", "HTML"]&#125;&#125;</span>
obj2.name = <span class="hljs-string">'小孙'</span>
obj2.info.field = [<span class="hljs-string">'JavaScript'</span>]
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123;name: "小孙", age: 18, info: &#123;field: ["JavaScript"]&#125;&#125;</span>
<span class="hljs-built_in">console</span>.log(obj2) <span class="hljs-comment">// &#123;name: "小孙", age: 18, info: &#123;field: ["JavaScript"]&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对引用类型进行赋值（引用地址）操作，两个变量指向同一个对象，改变变量 obj2 之后会影响变量 obj ，哪怕改变的只是对象 obj2 中的基本数据类型。</p>
<h1 data-id="heading-1">浅拷贝（Shallow Copy）</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16165bb6b2f7415eb1718cd3d16e510f~tplv-k3u1fbpfcp-zoom-1.image" alt="16ce894a1f1b5c32" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。</p>
<ul>
<li>如果属性是基本类型，拷贝的就是基本类型的值；</li>
<li>如果属性是引用类型，拷贝的就是内存地址 ；如果其中一个对象改变了这个地址，就会影响到另一个对象。</li>
</ul>
</blockquote>
<h2 data-id="heading-2">Object.assign() （ES6）</h2>
<p>用于将所有<strong>可枚举属性</strong>的值从一个或多个源对象分配到目标对象。它将返回目标对象。</p>
<p>如果目标对象中的属性具有相同的键，则属性将被源对象中的属性覆盖。后面的源对象的属性将类似地覆盖前面的源对象的属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> target = &#123;&#125;
<span class="hljs-keyword">let</span> source = &#123; <span class="hljs-attr">a</span>: &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125; &#125;
<span class="hljs-built_in">Object</span>.assign(target, source)
<span class="hljs-built_in">console</span>.log(target) <span class="hljs-comment">// 修改前 &#123;a: &#123;b: 2&#125;&#125; 修改后 &#123;a: &#123;b: 10&#125;&#125;</span>
<span class="hljs-comment">//如果我们修改了 b 的属性</span>
source.a.b = <span class="hljs-number">10</span>
<span class="hljs-built_in">console</span>.log(source) <span class="hljs-comment">// &#123;a: &#123;b: 10&#125;&#125;</span>
<span class="hljs-built_in">console</span>.log(target) <span class="hljs-comment">// &#123;a: &#123;b: 10&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于修改后三个<code>target</code>里面的属性 b 都改变了，证明<code>Objec.assign</code>是一个浅拷贝。</p>
<blockquote>
<p>注意：</p>
<ol>
<li>拷贝的都是自有属性，不会拷贝对象继承的属性；</li>
<li>拷贝的都是可枚举属性；</li>
<li>可以拷贝<code>symbol</code>类型的属性；</li>
<li>原始类型会被包装为对象。</li>
</ol>
</blockquote>
<h2 data-id="heading-3">扩展运算符</h2>
<p>实际上, 展开语法和 <code>Object.assign()</code> 行为一致, 执行的都是浅拷贝(只遍历一层)。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">1</span> &#125; &#125;
<span class="hljs-keyword">let</span> obj2 = &#123; ...obj &#125;

obj.a = <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// 修改二层属性前 &#123;a: 2, b: &#123;c: 1&#125;&#125; 修改二层属性后 &#123;a: 2, b: &#123;c: 2&#125;&#125;</span>
<span class="hljs-built_in">console</span>.log(obj2) <span class="hljs-comment">// 修改二层属性前 &#123;a: 1, b: &#123;c: 1&#125;&#125; 修改二层属性后 &#123;a: 2, b: &#123;c: 2&#125;&#125;</span>

obj.b.c = <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123;a: 2, b: &#123;c: 2&#125;&#125;</span>
<span class="hljs-built_in">console</span>.log(obj2) <span class="hljs-comment">// &#123;a: 1, b: &#123;c: 2&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Array.prototype.slice()</h2>
<p>返回一个新的数组对象，这一对象是一个由 <code>begin</code> 和 <code>end</code> 决定的原数组的<strong>浅拷贝</strong>（包括 <code>begin</code>，不包括<code>end</code>）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a = [<span class="hljs-number">0</span>, <span class="hljs-string">"1"</span>, [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>]]
<span class="hljs-keyword">let</span> b = a.slice(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// ["1", [4, 3]]</span>

a[<span class="hljs-number">1</span>] = <span class="hljs-string">'99'</span>
a[<span class="hljs-number">2</span>][<span class="hljs-number">0</span>] = <span class="hljs-number">4</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// [0, "99", [4, 3]]</span>
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// ["1", [4, 3]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改变<code>a[1]</code>之后<code>b[0]</code>的值并没有发生变化，但是改变<code>a[2][0]</code>之后，相应的<code>b[1][0]</code>的值也发生变化。</p>
<p>说明<code>slice()</code>方法是浅拷贝。</p>
<h2 data-id="heading-5">Array.prototype.concat()</h2>
<p>用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;]
<span class="hljs-keyword">let</span> arr2 = [&#123; <span class="hljs-attr">b</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">1</span> &#125;]
<span class="hljs-keyword">let</span> arr3 = arr.concat(arr2)
arr2[<span class="hljs-number">0</span>].b = <span class="hljs-number">123</span>
<span class="hljs-built_in">console</span>.log(arr3) <span class="hljs-comment">// [&#123;a: 1&#125;,&#123;a: 1&#125;,&#123;a: 1&#125;,&#123; b: 123&#125;,&#123;b: 1&#125;,&#123;b: 1&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改变<code>arr2[0].b</code> 之后，<code>arr3</code>的值也发生了变化，这说明<code>concat</code>也是浅拷贝。</p>
<h2 data-id="heading-6">手写浅拷贝</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowClone</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">let</span> target = &#123;&#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> source) &#123;
        <span class="hljs-keyword">if</span> (source.hasOwnProperty(key)) &#123;
            target[key] = source[key]
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> target
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">深拷贝（Deep Copy）</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d01b893d1d264cf890a625892e8db897~tplv-k3u1fbpfcp-zoom-1.image" alt="16ce893a54f6c13d" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>将一个对象从内存中完整的拷贝一份出来，从堆内存中开辟一个新的区域存放新对象，且修改新对象不会影响原对象。</p>
</blockquote>
<h2 data-id="heading-8">JSON.parse(JSON.stringify())</h2>
<ul>
<li><code>JSON.stringify()</code> 方法将一个 JavaScript 对象或值转换为 JSON 字符串。</li>
<li><code>JSON.parse()</code> 方法用来解析 JSON 字符串，构造由字符串描述的 JavaScript 值或对象。</li>
</ul>
<p>通过<code>JSON.stringify()</code>把一个对象序列化成为一个 JSON 字符串，将对象的内容转换成字符串的形式保存，再用<code>JSON.parse()</code> 反序列化将 JSON 字符串变成一个新对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [
    <span class="hljs-number">1</span>, <span class="hljs-number">6</span>, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"小刘"</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
    &#125;
]

<span class="hljs-keyword">let</span> arr2 = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(arr))
arr2[<span class="hljs-number">2</span>].name = <span class="hljs-string">"小孙"</span>
<span class="hljs-built_in">console</span>.log(arr, arr2) <span class="hljs-comment">// [1,6,&#123;name: "小刘", age: 18&#125;] [1,6,&#123;name: "小孙", age: 18&#125;] </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> test = &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">str</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">boolean</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">unf</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">nul</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">nan</span>: <span class="hljs-literal">NaN</span>,
    <span class="hljs-attr">infi</span>: <span class="hljs-literal">Infinity</span>,
    <span class="hljs-attr">infi1</span>: -<span class="hljs-literal">Infinity</span>,
    <span class="hljs-attr">obj</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'我是一个对象'</span>,
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">arr</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>],
    <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是一个函数'</span>)
    &#125;,
    <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-number">0</span>),
    <span class="hljs-attr">reg</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'/我是一个正则/ig'</span>),
    <span class="hljs-attr">err</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'我是一个错误'</span>)
&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(test)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/425a904cb9c84a97bb4f3523c2f7eea3~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210628132715522" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//循环引用</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">b</span>: &#123;
        <span class="hljs-attr">c</span>: <span class="hljs-number">2</span>
    &#125;
&#125;
obj.a = obj.b
obj.b.c = obj.a

<span class="hljs-keyword">let</span> test = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj)) <span class="hljs-comment">// Uncaught TypeError: Converting circular structure to JSON</span>

<span class="hljs-comment">//不可枚举属性被忽略</span>
<span class="hljs-keyword">let</span> test1 = <span class="hljs-built_in">JSON</span>.stringify(
    <span class="hljs-built_in">Object</span>.create(
        <span class="hljs-literal">null</span>,
        &#123;
            <span class="hljs-attr">x</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'x'</span>, <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span> &#125;,
            <span class="hljs-attr">y</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'y'</span>, <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span> &#125;
        &#125;
    )
)
<span class="hljs-built_in">console</span>.log(test1) <span class="hljs-comment">// &#123;"y":"y"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>JSON 会忽略<code>undefiend</code>，<code>symbol</code>，<code>function</code>。</p>
</li>
<li>
<p><code>date</code>对象<code>Mon Jun 28 2021 13:28:59 GMT+0800 (中国标准时间)</code>转变为字符串 "2021-06-28T05:28:49.680Z"。</p>
<p>Date 日期调用了 <code>toJSON()</code> 将其转换为了 string 字符串（同<code>Date.toISOString()</code>），因此会被当做字符串处理。</p>
</li>
<li>
<p><code>NaN</code>，<code>Infinity</code>，<code>-Infinity</code>会转变为 <code>null</code>。</p>
</li>
<li>
<p><code>RegExp</code>，<code>Error</code>会变成空对象 &#123;&#125;。</p>
</li>
<li>
<p>循环引用的情况下，会报<code>Uncaught TypeError: Converting circular structure to JSON</code>错误。</p>
</li>
<li>
<p>其他类型的对象，包括 Map/Set/WeakMap/WeakSet，仅会序列化可枚举的属性。</p>
</li>
</ol>
<p>由此可见，使用 JSON 可以实现<strong>数组</strong>或<strong>对象</strong>深拷贝，但是处理其它类型对象会有问题。</p>
<h2 data-id="heading-9">手写深拷贝（ConardLi大佬版）</h2>
<p>深拷贝，考虑我们要拷贝的对象不知道有多少曾深度，我们可以用递归来解决问题：</p>
<ul>
<li>如果是原始类型，无需继续拷贝，直接返回；</li>
<li>如果是引用类型，创建一个新的对象，遍历需要克隆的对象，将需要克隆的对象的属性执行<strong>深拷贝</strong>后依次添加到新对象上。</li>
</ul>
<p>如果有更深层次的对象可以继续递归直到属性为原始类型，这样我们就完成了一个最简单的深拷贝：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> source === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">let</span> target = &#123;&#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> source) &#123;
            <span class="hljs-keyword">if</span> (source.hasOwnProperty(key)) &#123;
                target[key] = clone(source[key])
            &#125;
            <span class="hljs-keyword">return</span> target
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> source
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90567c5043604c7bb8be97aa26e30652~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210628181940498" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">考虑数组</h3>
<p>我们可以看到，返回结果中数组的返回值是<code>arr:&#123; 0:0, 1:1, 2:2 &#125;</code>。这说明我们没有判断对象是数组的情况。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> source === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">let</span> target = <span class="hljs-built_in">Array</span>.isArray(source) ? [] : &#123;&#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> source) &#123;
            target[key] = clone(source[key])
        &#125;
        <span class="hljs-keyword">return</span> target
    &#125;
    <span class="hljs-keyword">return</span> source
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b23c7097c72f47749fb95940b1d73dab~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210628182603404" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">循环引用</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> target = &#123;
    <span class="hljs-attr">field1</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">field2</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">field3</span>: &#123;
        <span class="hljs-attr">child</span>: <span class="hljs-string">'child'</span>
    &#125;,
    <span class="hljs-attr">field4</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>]
&#125;
target.target = target
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e343856ecb34f5fa347d79dcb3540af~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210628183602418" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行上面一段代码，我们发现栈内存溢出了。原因就是上面的对象存在循环引用的情况，即<strong>对象的属性间接或直接的引用了自身</strong>。</p>
<p>解决循环引用的问题，我们可以额外开辟一个存储空间，来存储当前对象和拷贝对象的对应关系，当需要拷贝当前对象时，先去存储空间中寻找，有没有拷贝过这个对象，如果有的话直接返回，如果没有的话继续拷贝，这样就巧妙化解了循环引用的问题。</p>
<p>这个存储空间，需要可以存储<code>key-value</code>形式的数据，且<code>key</code>可以是一个引用类型，我们可以选择<code>Map</code>这种数据结构：</p>
<ul>
<li>检查<code>map</code>中有无克隆过的对象。
<ul>
<li>有，直接返回。</li>
<li>没有，将当前对象作为<code>key</code>，克隆对象作为<code>value</code>进行存储。</li>
</ul>
</li>
<li>继续克隆。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> source === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">let</span> target = <span class="hljs-built_in">Array</span>.isArray(source) ? [] : &#123;&#125;
        <span class="hljs-keyword">if</span> (map.get(source)) &#123;
            <span class="hljs-keyword">return</span> map.get(source)
        &#125;
        map.set(source, target)
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> source) &#123;
            target[key] = clone(source[key], map)
        &#125;
        <span class="hljs-keyword">return</span> target
    &#125;
    <span class="hljs-keyword">return</span> source
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc58ce582774e60864ab35e491915c8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210628195335578" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>Map</code>可以用<code>WeakMap</code>来代替，这样的好处是，不需要手动清除<code>Map</code>的属性，等下一次垃圾回收机制执行时，这块内存就会被释放掉。</p>
<p>坏处是，<code>WeakMap</code>是 ES6 新增的集合类型，兼容性没<code>Map</code>好。</p>
</blockquote>
<h3 data-id="heading-12">性能优化</h3>
<p>在上面的代码中，我们遍历数组和对象都使用了<code>for in</code>这种方式，实际上<code>for in</code>在遍历时效率是非常低的，下面我们来对比下常用的三种循环<code>for</code>，<code>while</code>，<code>for in</code>的执行效率：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//先建立一个40000000级别的字符串数组</span>
<span class="hljs-keyword">const</span> array = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">40000000</span>).fill(<span class="hljs-string">'hello'</span>)
<span class="hljs-keyword">const</span> length = array.length
<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'while'</span>)
<span class="hljs-keyword">while</span> (i < length) &#123;
    <span class="hljs-keyword">const</span> element = array[i]
    sum += element
    i++
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'while'</span>) <span class="hljs-comment">// while: 3408.120849609375 ms</span>

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'for'</span>)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
    <span class="hljs-keyword">const</span> element = array[i]
    sum += element
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'for'</span>) <span class="hljs-comment">// for: 6242.840087890625 ms</span>

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'for in'</span>)
sum = <span class="hljs-number">0</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> array) &#123;
    <span class="hljs-keyword">const</span> element = array[key]
    sum += element
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'for in'</span>) <span class="hljs-comment">// for in: 29896.768310546875 ms</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此可见，<code>while</code>的效率要高于<code>for</code>和<code>for in</code>。我们将<code>for in</code>遍历改写为<code>while</code>遍历。</p>
<p>我们先使用<code>while</code>来实现一个通用的<code>foreach</code>遍历，<code>iteratee</code>是遍历的回调函数，它可以接收每次遍历的<code>value</code>和<code>index</code>两个参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">array, iteratee</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">const</span> length = array.length
    <span class="hljs-keyword">while</span> (++index < length) &#123;
        iteratee(array[index], index)
    &#125;
    <span class="hljs-keyword">return</span> array
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们对<code>clone</code>函数进行改写：</p>
<ul>
<li>当遍历数组时，直接使用<code>forEach</code>进行遍历；</li>
<li>当遍历对象时，使用<code>Object.keys</code>取出所有的<code>key</code>进行遍历；</li>
<li>然后在遍历时把<code>forEach</code>回调函数的<code>value</code>当做<code>key</code>使用。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()</span>) </span>&#123;
    <span class="hljs-comment">//是对象的情况下</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> source === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-comment">//判定是数组还是对象</span>
        <span class="hljs-keyword">const</span> isArray = <span class="hljs-built_in">Array</span>.isArray(source)
        <span class="hljs-keyword">let</span> target = isArray ? [] : &#123;&#125;

        <span class="hljs-comment">//map中有克隆过的对象直接返回</span>
        <span class="hljs-keyword">if</span> (map.get(source)) &#123;
            <span class="hljs-keyword">return</span> map.get(source)
        &#125;
        <span class="hljs-comment">//map中没有克隆过的对象进行存储</span>
        map.set(source, target)

        <span class="hljs-comment">//遍历数组时，使用forEach遍历；遍历对象时，使用 Object.keys (返回 key 组成的数组)取出所用的 key 进行遍历</span>
        <span class="hljs-keyword">const</span> keys = isArray ? <span class="hljs-literal">undefined</span> : <span class="hljs-built_in">Object</span>.keys(source)
        <span class="hljs-comment">// undefined || array -> array</span>
        <span class="hljs-comment">// array || object -> array</span>
        forEach(keys || source, <span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
            <span class="hljs-comment">//如果是数组</span>
            <span class="hljs-keyword">if</span> (keys) &#123;
                <span class="hljs-comment">//将回调函数的 value 当做 key 使用</span>
                key = value
            &#125;
            <span class="hljs-comment">//将对象储存在 target 中 ，多层对象递归</span>
            target[key] = clone(source[key], map)
        &#125;)
        <span class="hljs-comment">//返回对象</span>
        <span class="hljs-keyword">return</span> target

    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//返回原始类型</span>
        <span class="hljs-keyword">return</span> source
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">合理的判断引用类型</h3>
<p>上面，我们只考虑了<code>object</code>和<code>array</code>两种数据类型，实际上所用的引用类型还有很多。</p>
<p>我们还需要考虑<code>function</code>和<code>null</code>两种特殊的数据类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> type = <span class="hljs-keyword">typeof</span> source
    <span class="hljs-keyword">return</span> source !== <span class="hljs-literal">null</span> && (type === <span class="hljs-string">'object'</span> || type === <span class="hljs-string">'function'</span>)
&#125;

<span class="hljs-keyword">if</span>(!isObject(source))&#123;
    <span class="hljs-keyword">return</span> source
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">获取数据类型</h3>
<p>我们可以使用<code>toString()</code>来获取准确的引用类型：</p>
<blockquote>
<p>每一个引用类型都有<code>toString</code>方法，默认情况下，<code>toString()</code>方法被每个<code>Object</code>对象继承。如果此方法在自定义对象中未被覆盖，<code>toString()</code> 返回 <code>"[object type]"</code>，其中type是对象的类型。</p>
</blockquote>
<p>注意，上面提到了如果此方法在自定义对象中未被覆盖，<code>toString</code>才会达到预想的效果，事实上，大部分引用类型比如<code>Array、Date、RegExp</code>等都重写了<code>toString</code>方法。</p>
<p>我们可以直接调用<code>Object</code>原型上未被覆盖的<code>toString()</code>方法，使用<code>call</code>来改变<code>this</code>指向来达到我们想要的效果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getType</span>(<span class="hljs-params">source</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(source)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们抽离出一些常用的数据类型以便后面使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> mapTag = <span class="hljs-string">'[object Map]'</span>
<span class="hljs-keyword">const</span> setTag = <span class="hljs-string">'[object Set]'</span>
<span class="hljs-keyword">const</span> arrayTag = <span class="hljs-string">'[object Array]'</span>
<span class="hljs-keyword">const</span> objectTag = <span class="hljs-string">'[object Object]'</span>

<span class="hljs-keyword">const</span> boolTag = <span class="hljs-string">'[object Boolean]'</span>
<span class="hljs-keyword">const</span> dateTag = <span class="hljs-string">'[object Date]'</span>
<span class="hljs-keyword">const</span> errorTag = <span class="hljs-string">'[object Error]'</span>
<span class="hljs-keyword">const</span> numberTag = <span class="hljs-string">'[object Number]'</span>
<span class="hljs-keyword">const</span> regexpTag = <span class="hljs-string">'[object RegExp]'</span>
<span class="hljs-keyword">const</span> stringTag = <span class="hljs-string">'[object String]'</span>
<span class="hljs-keyword">const</span> symbolTag = <span class="hljs-string">'[object Symbol]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的集中类型中，我们简单将他们分为两类：</p>
<ul>
<li>可以继续遍历的类型。</li>
<li>不可以继续遍历的类型。</li>
</ul>
<p>我们分别为它们做不同的拷贝。</p>
<h3 data-id="heading-15">可继续遍历的类型</h3>
<p><code>object</code>，<code>array</code>，<code>Map</code>，<code>Set</code>这几种类型都属于可持续遍历的类型，需要进行递归。</p>
<p>我们首先要获得它们的初始化数据，例如上面的<code>[]</code>和<code>&#123;&#125;</code>，我们可以通过拿到<code>constructor</code>的方式来通用的获取。</p>
<p>这种方法有一个好处：因为我们还使用了原对象的构造方法，所以他可以保留对象原型上的数据，如果直接使用普通的<code>&#123;&#125;</code>，那么原型必然会丢失的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()</span>) </span>&#123;
    <span class="hljs-comment">//克隆原始类型</span>
    <span class="hljs-keyword">if</span> (!isObject(source)) &#123;
        <span class="hljs-keyword">return</span> source
    &#125;
    <span class="hljs-comment">//初始化</span>
    <span class="hljs-keyword">const</span> type = getType(source)
    <span class="hljs-keyword">let</span> target
    <span class="hljs-keyword">if</span> (deepTag.includes(type)) &#123;
        target = getInit(source, type)
    &#125;

    <span class="hljs-comment">//防止循环引用</span>
    <span class="hljs-keyword">if</span> (map.get(source)) &#123;
        <span class="hljs-keyword">return</span> map.get(source)
    &#125;
    map.set(source, target)

    <span class="hljs-comment">//克隆set</span>
    <span class="hljs-keyword">if</span> (type === setTag) &#123;
        source.forEach(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            target.add(clone(value, map))
        &#125;)
        <span class="hljs-keyword">return</span> target
    &#125;

    <span class="hljs-comment">//克隆map</span>
    <span class="hljs-keyword">if</span> (type === mapTag) &#123;
        source.forEach(<span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
            target.set(key, clone(value, map))
        &#125;)
        <span class="hljs-keyword">return</span> target
    &#125;

    <span class="hljs-comment">//克隆对象和数组</span>
    <span class="hljs-comment">//运算符优先级 === > ...? :... > = </span>
    <span class="hljs-keyword">const</span> keys = type === arrayTag ? <span class="hljs-literal">undefined</span> : <span class="hljs-built_in">Object</span>.keys(source)
    forEach(keys || source, <span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (keys) &#123;
            key = value
        &#125;
        target[key] = clone(target[key], map)
    &#125;)
    <span class="hljs-keyword">return</span> target
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">不可继续遍历的类型</h3>
<p>其他剩余的类型我们把它们统一归类成不可处理的数据类型，我们依次进行处理：</p>
<p><code>Boolean</code>、<code>Number</code>、<code>String</code>、<code>String</code>、<code>Date</code>、<code>Error</code>这几种类型我们都可以直接用构造函数和原始数据创建一个新对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneOtherType</span>(<span class="hljs-params">targe, type</span>) </span>&#123;
    <span class="hljs-keyword">const</span> Ctor = targe.constructor
    <span class="hljs-keyword">switch</span> (type) &#123;
        <span class="hljs-keyword">case</span> boolTag:
        <span class="hljs-keyword">case</span> numberTag:
        <span class="hljs-keyword">case</span> stringTag:
        <span class="hljs-keyword">case</span> errorTag:
        <span class="hljs-keyword">case</span> dateTag:
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Ctor(targe)
        <span class="hljs-keyword">case</span> regexpTag:
            <span class="hljs-keyword">return</span> cloneReg(targe)
        <span class="hljs-keyword">case</span> symbolTag:
            <span class="hljs-keyword">return</span> cloneSymbol(targe)
        <span class="hljs-keyword">case</span> funcTag:
            <span class="hljs-keyword">return</span> cloneFunction(targe)
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>克隆<code>Symbol</code>类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneSymbol</span>(<span class="hljs-params">targe</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">Symbol</span>.prototype.valueOf.call(targe))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>克隆<code>Regexp</code>类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneReg</span>(<span class="hljs-params">targe</span>) </span>&#123;
    <span class="hljs-keyword">const</span> reFlags = <span class="hljs-regexp">/\w*$/</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">new</span> targe.constructor(targe.source, reFlags.exec(targe))
    result.lastIndex = targe.lastIndex
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>克隆<code>function</code>类型：</p>
<p>实际上克隆函数是没有实际应用场景的，两个对象使用一个在内存中处于同一个地址的函数也是没有任何问题的，<code>lodash</code>对函数的处理是直接返回：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isFunc = <span class="hljs-keyword">typeof</span> value == <span class="hljs-string">'function'</span>
 <span class="hljs-keyword">if</span> (isFunc || !cloneableTags[tag]) &#123;
        <span class="hljs-keyword">return</span> object ? value : &#123;&#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面来分析一下函数类型怎么克隆：</p>
<ol>
<li>首先，我们可以通过<code>protptype</code>来区分箭头函数和普通函数，箭头函数是没有<code>prototype</code>的。</li>
<li>我们可以直接使用<code>eval</code>和函数字符串来重新生成一个箭头函数。
<ul>
<li>这种方法不适用于普通函数。</li>
</ul>
</li>
<li>我们可以用正则来处理普通函数。
<ul>
<li>分别使用正则取出函数体和函数参数，然后使用<code>new Function([arg1,[arg2,[...argN]]],functionBody)</code>构造函数重新构造一个新的函数。</li>
</ul>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneFunction</span>(<span class="hljs-params">func</span>) </span>&#123;
    <span class="hljs-keyword">const</span> bodyReg = <span class="hljs-regexp">/(?<=&#123;)(.|\n)+(?=&#125;)/m</span>
    <span class="hljs-keyword">const</span> paramReg = <span class="hljs-regexp">/(?<=\().+(?=\)\s+&#123;)/</span>

    <span class="hljs-keyword">const</span> funcString = func.toString()
    <span class="hljs-keyword">if</span> (func.prototype) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'普通函数'</span>)
        <span class="hljs-keyword">const</span> param = paramReg.exec(funcString)
        <span class="hljs-keyword">const</span> body = bodyReg.exec(funcString)
        <span class="hljs-keyword">if</span> (body) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'匹配到函数体：'</span>, body[<span class="hljs-number">0</span>])
            <span class="hljs-keyword">if</span> (param) &#123;
                <span class="hljs-keyword">const</span> paramArr = param[<span class="hljs-number">0</span>].split[<span class="hljs-string">','</span>]
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'匹配到参数：'</span>, paramArr)
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(...paramArr, body[<span class="hljs-number">0</span>])
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(body[<span class="hljs-number">0</span>])
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">eval</span>(funcString)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">综合</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//可继续遍历的数据类型</span>
<span class="hljs-keyword">const</span> mapTag = <span class="hljs-string">'[object Map]'</span>
<span class="hljs-keyword">const</span> setTag = <span class="hljs-string">'[object Set]'</span>
<span class="hljs-keyword">const</span> arrayTag = <span class="hljs-string">'[object Array]'</span>
<span class="hljs-keyword">const</span> objectTag = <span class="hljs-string">'[object Object]'</span>
<span class="hljs-keyword">const</span> argsTag = <span class="hljs-string">'[object Arguments]'</span>
<span class="hljs-comment">//不可继续遍历的数据类型</span>
<span class="hljs-keyword">const</span> boolTag = <span class="hljs-string">'[object Boolean]'</span>
<span class="hljs-keyword">const</span> dateTag = <span class="hljs-string">'[object Date]'</span>
<span class="hljs-keyword">const</span> numberTag = <span class="hljs-string">'[object Number]'</span>
<span class="hljs-keyword">const</span> stringTag = <span class="hljs-string">'[object String]'</span>
<span class="hljs-keyword">const</span> symbolTag = <span class="hljs-string">'[object Symbol]'</span>
<span class="hljs-keyword">const</span> errorTag = <span class="hljs-string">'[object Error]'</span>
<span class="hljs-keyword">const</span> regexpTag = <span class="hljs-string">'[object RegExp]'</span>
<span class="hljs-keyword">const</span> funcTag = <span class="hljs-string">'[object Function]'</span>

<span class="hljs-keyword">const</span> deepTag = [mapTag, setTag, arrayTag, objectTag, argsTag]

<span class="hljs-comment">//通用 while 循环</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">array, iteratee</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">const</span> length = array.length
    <span class="hljs-keyword">while</span> (++index < length) &#123;
        iteratee(array[index], index)
    &#125;
    <span class="hljs-keyword">return</span> array
&#125;
<span class="hljs-comment">//判断是否为引用类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> type = <span class="hljs-keyword">typeof</span> source
    <span class="hljs-keyword">return</span> source !== <span class="hljs-literal">null</span> && (type === <span class="hljs-string">'object'</span> || type === <span class="hljs-string">'function'</span>)
&#125;
<span class="hljs-comment">//获取实际类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getType</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(source)
&#125;
<span class="hljs-comment">//初始化被克隆的对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getInit</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> Ctor = source.constructor
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Ctor()
&#125;
<span class="hljs-comment">//克隆Symbol</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneSymbol</span>(<span class="hljs-params">targe</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">Symbol</span>.prototype.valueOf.call(targe))
&#125;
<span class="hljs-comment">//克隆正则</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneReg</span>(<span class="hljs-params">targe</span>) </span>&#123;
    <span class="hljs-comment">//意思是匹配字符串尾部字母</span>
    <span class="hljs-keyword">const</span> reFlags = <span class="hljs-regexp">/\w*$/</span>
    <span class="hljs-comment">//targe.constructor 就是 RegExp 构造函数</span>
    <span class="hljs-comment">//正则分为源码（source）和修饰符（flags），targe.source 获取源码，也就是//里面的数据，reFlags.exec(targe) 获取修饰符，也就是 //后面的gim</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">new</span> targe.constructor(targe.source, reFlags.exec(targe))
    <span class="hljs-comment">//克隆lastIndex，lastIndex 表示每次匹配时的开始位置。</span>
    result.lastIndex = targe.lastIndex
    <span class="hljs-keyword">return</span> result
&#125;
<span class="hljs-comment">//克隆函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneFunction</span>(<span class="hljs-params">func</span>) </span>&#123;
    <span class="hljs-comment">//后行断言 匹配 &#123; + (非\n\r的所有字符或\r) + 先行断言 匹配 &#125; ，也就是匹配函数体</span>
    <span class="hljs-comment">//后行断言 匹配 ( + 非\n\r的所有字符 + 先行断言 匹配 ) + 空格 + &#123; ，也就是匹配函数参数</span>
    <span class="hljs-keyword">const</span> bodyReg = <span class="hljs-regexp">/(?<=&#123;)(.|\n)+(?=&#125;)/m</span>
    <span class="hljs-keyword">const</span> paramReg = <span class="hljs-regexp">/(?<=\().+(?=\)\s*&#123;)/</span>
    <span class="hljs-keyword">const</span> funcString = func.toString()
    <span class="hljs-keyword">if</span> (func.prototype) &#123;
        <span class="hljs-keyword">const</span> param = paramReg.exec(funcString)
        <span class="hljs-keyword">const</span> body = bodyReg.exec(funcString)
        <span class="hljs-keyword">if</span> (body) &#123;
            <span class="hljs-keyword">if</span> (param) &#123;
                <span class="hljs-keyword">const</span> paramArr = param[<span class="hljs-number">0</span>].split(<span class="hljs-string">','</span>)
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(...paramArr, body[<span class="hljs-number">0</span>])
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(body[<span class="hljs-number">0</span>])
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">eval</span>(<span class="hljs-string">'('</span> + funcString + <span class="hljs-string">')'</span>)
    &#125;
&#125;
<span class="hljs-comment">//克隆不可遍历类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneOtherType</span>(<span class="hljs-params">targe, type</span>) </span>&#123;
    <span class="hljs-keyword">const</span> Ctor = targe.constructor
    <span class="hljs-keyword">switch</span> (type) &#123;
        <span class="hljs-keyword">case</span> boolTag:
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">Boolean</span>.prototype.valueOf.call(targe)) <span class="hljs-comment">//为了修正Boolean(false)判定为true</span>
        <span class="hljs-keyword">case</span> numberTag:
        <span class="hljs-keyword">case</span> stringTag:
        <span class="hljs-keyword">case</span> errorTag:
        <span class="hljs-keyword">case</span> dateTag:
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Ctor(targe)
        <span class="hljs-keyword">case</span> regexpTag:
            <span class="hljs-keyword">return</span> cloneReg(targe)
        <span class="hljs-keyword">case</span> symbolTag:
            <span class="hljs-keyword">return</span> cloneSymbol(targe)
        <span class="hljs-keyword">case</span> funcTag:
            <span class="hljs-keyword">return</span> cloneFunction(targe)
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">source, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()</span>) </span>&#123;

    <span class="hljs-comment">// 原始类型直接返回</span>
    <span class="hljs-keyword">if</span> (!isObject(source)) &#123;
        <span class="hljs-keyword">return</span> source
    &#125;

    <span class="hljs-comment">// 初始化</span>
    <span class="hljs-keyword">const</span> type = getType(source)
    <span class="hljs-keyword">let</span> target
    <span class="hljs-keyword">if</span> (deepTag.includes(type)) &#123;
        target = getInit(source, type)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> cloneOtherType(source, type)
    &#125;

    <span class="hljs-comment">// 防止循环引用</span>
    <span class="hljs-keyword">if</span> (map.get(source)) &#123;
        <span class="hljs-keyword">return</span> map.get(source)
    &#125;
    map.set(source, target)

    <span class="hljs-comment">// 克隆set</span>
    <span class="hljs-keyword">if</span> (type === setTag) &#123;
        source.forEach(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            target.add(clone(value, map))
        &#125;)
        <span class="hljs-keyword">return</span> target
    &#125;

    <span class="hljs-comment">// 克隆map</span>
    <span class="hljs-keyword">if</span> (type === mapTag) &#123;
        source.forEach(<span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
            target.set(key, clone(value, map))
        &#125;)
        <span class="hljs-keyword">return</span> target
    &#125;

    <span class="hljs-comment">// 克隆对象和数组</span>
    <span class="hljs-comment">// 优先级 === > ?: > =</span>
    <span class="hljs-keyword">const</span> keys = type === arrayTag ? <span class="hljs-literal">undefined</span> : <span class="hljs-built_in">Object</span>.keys(source)
    forEach(keys || source, <span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
        <span class="hljs-comment">//对象的情况下，value 当做 key 使用</span>
        <span class="hljs-keyword">if</span> (keys) &#123;
            key = value
        &#125;
        <span class="hljs-comment">//递归</span>
        target[key] = clone(source[key], map)
    &#125;)

    <span class="hljs-keyword">return</span> target
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
map.set(<span class="hljs-string">'key'</span>, <span class="hljs-string">'value'</span>)
map.set(<span class="hljs-string">'xiaoliu'</span>, <span class="hljs-string">'hello world'</span>)

<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
set.add(<span class="hljs-string">'xiaoliu'</span>)
set.add(<span class="hljs-string">'hello world'</span>)

<span class="hljs-keyword">const</span> source = &#123;
    <span class="hljs-attr">field1</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">field2</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">field3</span>: &#123;
        <span class="hljs-attr">child</span>: <span class="hljs-string">'child'</span>
    &#125;,
    <span class="hljs-attr">field4</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>],
    <span class="hljs-attr">empty</span>: <span class="hljs-literal">null</span>,
    map,
    set,
    <span class="hljs-attr">bool</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">false</span>),
    <span class="hljs-attr">num</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">2</span>),
    <span class="hljs-attr">str</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-number">2</span>),
    <span class="hljs-attr">symbol</span>: <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">Symbol</span>(<span class="hljs-number">1</span>)),
    <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
    <span class="hljs-attr">reg</span>: <span class="hljs-regexp">/\d+/</span>,
    error: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(),
    <span class="hljs-attr">func1</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello world'</span>)
    &#125;,
    <span class="hljs-attr">func2</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
        <span class="hljs-keyword">return</span> a + b
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fa0c559ffb7417596bdcb2c1f9dc0ce~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210630091816645" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-18">参考：</h1>
<p><a href="https://juejin.cn/post/6844903929705136141" target="_blank">如何写出一个惊艳面试官的深拷贝?</a></p>
<p><a href="https://juejin.cn/post/6844903493925371917" target="_blank">js 深拷贝 vs 浅拷贝</a></p>
<p><a href="https://juejin.cn/post/6844903745961066503#heading-1" target="_blank">【进阶4-1期】详细解析赋值、浅拷贝和深拷贝的区别</a></p>
<p><a href="https://juejin.cn/post/6844903968586334221#comment" target="_blank">浅拷贝和深拷贝（较为完整的探索）</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/assign" target="_blank" rel="nofollow noopener noreferrer">Object.assign()</a></p>
<p><a href="https://juejin.cn/post/6844903749270372365#heading-4" target="_blank">聊聊对象深拷贝和浅拷贝</a></p>
<p><a href="https://juejin.cn/post/6889327058158092302#heading-5" target="_blank">这一次彻底掌握深拷贝</a></p>
<p><a href="https://juejin.cn/post/6844903692756336653" target="_blank">深拷贝的终极探索（90%的人都不知道）</a></p>
<p><a href="https://juejin.cn/post/6844904021627502599" target="_blank">头条面试官：你知道如何实现高性能版本的深拷贝嘛？</a></p>
<p><a href="https://juejin.cn/post/6844903621021138957#heading-3" target="_blank">JavaScript深拷贝的一些坑</a></p>
<p><a href="https://juejin.cn/post/6844903592344698888#heading-1" target="_blank">低门槛彻底理解JavaScript中的深拷贝和浅拷贝</a></p>
<p><a href="https://juejin.cn/post/6844903592587952135#heading-4" target="_blank">深入深入再深入 js 深拷贝对象</a></p>
<p><a href="https://juejin.cn/post/6889327058158092302#heading-14" target="_blank">这一次彻底掌握深拷贝</a></p>
<p><a href="https://juejin.cn/post/6844903775384125448" target="_blank">如何 clone 一个正则？</a></p></div>  
</div>
            