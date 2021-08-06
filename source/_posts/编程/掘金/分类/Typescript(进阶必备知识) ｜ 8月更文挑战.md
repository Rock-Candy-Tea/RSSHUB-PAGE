
---
title: 'Typescript(进阶必备知识) ｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be13eb689ea44ee7a55453bff9ee7469~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:19:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be13eb689ea44ee7a55453bff9ee7469~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Typescript</h1>
<p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<div>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be13eb689ea44ee7a55453bff9ee7469~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" loading="lazy" referrerpolicy="no-referrer">
<h1 data-id="heading-1">基础知识</h1>
<h2 data-id="heading-2">基础类型: number string boolean array object</h2>
<p>1. enum: 枚举</p>
<p>2. type, interface</p>
<p>3. 联合类型 | (联合类型一次只能一种类型；而交叉类型每次都是多个类型的合并类型。)</p>
<p>4. 交叉类型 & (联合类型一次只能一种类型；而交叉类型每次都是多个类型的合并类型。)</p>
<p>5. typeof</p>
<p>Typeof 操作符可以用来获取一个变量声明或对象的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toArray</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">Array</span><<span class="hljs-title">number</span>> </span>&#123; 
    <span class="hljs-keyword">return</span> [x];
&#125;
<span class="hljs-keyword">type</span> Func = <span class="hljs-keyword">typeof</span> toArray; <span class="hljs-comment">// (x: number) => number[]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6. keyof</p>
<p>Keyof 操作符可以用来一个对象中的所有 key 值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person &#123; 
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; 
    age: <span class="hljs-built_in">number</span>;
&#125;
type1 K1 = Keyof Person; <span class="hljs-string">"name"</span> | <span class="hljs-string">"age"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7. in</p>
<p>In 用来遍历枚举类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Keys = <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>
<span class="hljs-keyword">type</span> Obj = &#123;
    [p <span class="hljs-keyword">in</span> Keys]: <span class="hljs-built_in">any</span>
&#125; <span class="hljs-comment">// &#123; a: any, b: any, c: any &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8. extends</p>
<p>有时候我们定义的泛型不想过于灵活或者说想继承某些类等，可以通过 extends 关键字添加泛型约束。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ILengthwise &#123;
    <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">ILengthwise</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);
    <span class="hljs-keyword">return</span> arg;
&#125;

loggingIdentity(<span class="hljs-number">3</span>);
loggingIdentity(&#123;<span class="hljs-attr">length</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>9. Paritial</p>
<p>Partial 的作用就是将某个类型里的属性全部变为可选项 ?。</p>
<p>10. Reuqired</p>
<p>Required 的作用就是将某个类型里的属性全部变为必选项。</p>
<p>11. Readonly</p>
<p>Readonly 的作用是将某个类型所有属性变为只读属性，也就意味着这些属性不能被重新赋值。</p>
<p>12. Record </p>
<p>Record<K extends keyof any, T> 的作用是将 K 中所有的属性的值转化为 T 类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts">
<span class="hljs-keyword">interface</span> PageInfo &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">type</span> Page = <span class="hljs-string">"home"</span> | <span class="hljs-string">"about"</span> | <span class="hljs-string">"contact"</span>;
<span class="hljs-keyword">const</span> x: Record<Page, PageInfo> = &#123;
    <span class="hljs-attr">about</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">"about"</span> &#125;,
    <span class="hljs-attr">contact</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">"contact"</span> &#125;,
    <span class="hljs-attr">home</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">"home"</span> &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="13">
<li>1. Exclude</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> T0 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span>>; <span class="hljs-comment">// "b" | "c"</span>
<span class="hljs-keyword">type</span> T1 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>; <span class="hljs-comment">// "c"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="14">
<li>Extract</li>
</ol>
<p>Extract<T, U> 的作用是从 T 中提取出 U。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> T0 = Extract<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"f"</span>>; <span class="hljs-comment">// "a"</span>
<span class="hljs-keyword">type</span> T1 = Extract<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>; <span class="hljs-comment">// () => void</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">常见面试题</h1>
<h2 data-id="heading-4">1. 简答</h2>
<ul>
<li>
<p>你觉得使用ts的好处是什么？</p>
</li>
<li>
<p>你觉得 typescript 和 javascript 有什么区别</p>
</li>
<li>
<p>typescript 你都用过哪些类型</p>
</li>
<li>
<p>typescript 中 type 和 interface 的区别</p>
</li>
<li>
<p>什么是泛型, 泛型的具体使用?</p>
</li>
</ul>
<hr>
<ul>
<li>
<p>Typescript的好处</p>
<p>1.1 TypeScript是JavaScript的加强版，它给JavaScript添加了可选的静态类型和基于类的面向对象编程，它拓展了JavaScript的语法。所以ts的功能比js只多不少.</p>
<p>1.2 Typescript 是纯面向对象的编程语言，包含类和接口的概念.</p>
<p>1.3 TS 在开发时就能给出编译错误， 而 JS 错误则需要在运行时才能暴露。</p>
<p>1.4 作为强类型语言，你可以明确知道数据的类型。代码可读性极强，几乎每个人都能理解。</p>
<p>1.5 ts中有很多很方便的特性, 比如可选链.</p>
</li>
<li>
<p>Typescript 与 JavaScript 的区别</p>
<ul>
<li>Typescript 是 JavaScript 的超集，它是基于 JavaScript 之上的编程语言，</li>
<li>Typescript 解决了 JavaScript 语言本身类型系统不足的问题</li>
<li>Typescript 还支持 ECMAScript 新特性</li>
<li>Typescript 会自动转化 ECMAScript 新特性，它最低支持 ES3 版本的代码，兼容性很好</li>
<li>JavaScript 是一门弱类型、动态类型的语言，它更灵活、多变</li>
</ul>
</li>
<li>
<p>Typescript 的缺点：</p>
<ul>
<li>相较于 JavaScript，Typescript 语言本身多出了很多概念，增加了学习成本</li>
<li>项目开发初期，Typescript 还需要做一些类型声明等，增加了一些开发成本</li>
</ul>
</li>
<li>
<p>用过的 Typescript 类型</p>
<ul>
<li>
<p>原始类型</p>
</li>
<li>
<p>数组类型</p>
</li>
<li>
<p>对象类型</p>
</li>
<li>
<p>任意类型</p>
</li>
<li>
<p>枚举类型</p>
</li>
<li>
<p>函数类型</p>
</li>
</ul>
</li>
<li>
<p>Typescript 中 type 和 interface 的区别</p>
</li>
<li>
<p>相同点：</p>
<ul>
<li>
<p>他们都可以描述对象或者函数</p>
</li>
<li>
<p>允许扩展（extends）</p>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">
<span class="hljs-keyword">type</span> Animal = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">say</span>: <span class="hljs-built_in">Function</span>
&#125;

<span class="hljs-keyword">interface</span> Animal2 &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">say</span>: <span class="hljs-built_in">Function</span>
&#125;

<span class="hljs-comment">// type extends type</span>
<span class="hljs-keyword">type</span> Cat = Animal & &#123; <span class="hljs-attr">jump</span>: <span class="hljs-built_in">Function</span> &#125;
<span class="hljs-comment">// type extends interface</span>
<span class="hljs-keyword">type</span> Cat2 = Animal2 & &#123; <span class="hljs-attr">jump</span>: <span class="hljs-built_in">Function</span> &#125;
    
<span class="hljs-keyword">interface</span> Dog <span class="hljs-keyword">extends</span> Animal2 &#123;
    <span class="hljs-attr">run</span>: <span class="hljs-built_in">Function</span>
&#125;
<span class="hljs-comment">// interface extends type</span>
<span class="hljs-keyword">interface</span> Dog2 <span class="hljs-keyword">extends</span> Animal &#123;
    <span class="hljs-attr">run</span>: <span class="hljs-built_in">Function</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>不同点：</p>
<ul>
<li>type 可以声明基本类型别名，联合类型，元组等类型</li>
</ul>
</li>
<li>
<p>什么是泛型, 泛型的具体使用?</p>
<p>泛型是指在定义函数、接口或类的时候，不预先指定具体的类型，使用时再去指定类型的一种特性。</p>
<p>可以把泛型理解为代表类型的参数</p>
</li>
</ul>
</div></div>  
</div>
            