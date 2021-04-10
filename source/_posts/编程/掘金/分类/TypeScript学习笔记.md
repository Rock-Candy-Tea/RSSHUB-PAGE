
---
title: 'TypeScript学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4099'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 23:15:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4099'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">基本类型和对象类型</h2>
<p>基础类型：<code>number</code>, <code>string</code>, <code>null</code>, <code>undefined</code>, <code>symbol</code>, <code>boolean</code>, <code>void</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> num: <span class="hljs-built_in">number</span> = <span class="hljs-number">123</span>;
<span class="hljs-keyword">const</span> teacherName: <span class="hljs-built_in">string</span> = <span class="hljs-string">'Dell'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象类型：<code>&#123;&#125;</code>, <code>[]</code>, <code>Class</code>, <code>unction</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> teacher: &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
&#125; = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Dell'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;;

<span class="hljs-keyword">const</span> numbers: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;&#125;
<span class="hljs-keyword">const</span> dell: Person = <span class="hljs-keyword">new</span> Person();

<span class="hljs-keyword">const</span> getTotal: <span class="hljs-function">() =></span> <span class="hljs-built_in">number</span> = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">123</span>;
&#125;;

<span class="hljs-keyword">const</span> func1: <span class="hljs-function">(<span class="hljs-params">str: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">number</span> = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseInt</span>(str, <span class="hljs-number">10</span>);
&#125;;

<span class="hljs-keyword">const</span> func2 = (str: <span class="hljs-built_in">string</span>): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseInt</span>(str, <span class="hljs-number">10</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">类型注解和类型推断</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// type annotation 类型注解：我们来告诉TS变量是什么类型</span>
<span class="hljs-keyword">let</span> count1: <span class="hljs-built_in">number</span>;
count1 = <span class="hljs-number">123</span>;

<span class="hljs-comment">// type inference 类型推断：TS自动去尝试分析变量的类型</span>
<span class="hljs-keyword">let</span> count2 = <span class="hljs-number">123</span>;

<span class="hljs-comment">// 如果TS能够自动分析变量类型，我们就什么也不需要做了</span>
<span class="hljs-keyword">const</span> num1 = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> num2 = <span class="hljs-number">2</span>;
<span class="hljs-keyword">const</span> total = num1 + num2;

<span class="hljs-comment">// 如果TS无法分析变量类型的话，我们就需要使用类型注解</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTotal2</span>(<span class="hljs-params">num1: <span class="hljs-built_in">number</span>, num2: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2;
&#125;

<span class="hljs-keyword">const</span> total = getTotal2(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">和函数相关的类型</h2>
<p><code>void</code>、<code>never</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 函数定义和js中一样，主要有3种</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">const</span> hello1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">const</span> hello2 = <span class="hljs-function">() =></span> &#123;&#125;

<span class="hljs-comment">// 最后的number可以不写，可通过类型推断推断出来</span>
<span class="hljs-comment">// 但是为了安全起见，还是写上比较好。因为在做逻辑处理时可能代码写错。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">first: <span class="hljs-built_in">number</span>, second: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> first + second
&#125;

<span class="hljs-comment">// 常用函数类型还有void、never等</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello"</span>)
&#125;

<span class="hljs-comment">// never: 函数永远不可能执行完或者会抛出异常时使用</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">errorEmitter</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>() <span class="hljs-comment">// while(true) &#123;&#125;</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"123"</span>)
&#125;

<span class="hljs-comment">// 解构的类型注解</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">&#123; first, second &#125;: &#123; first: <span class="hljs-built_in">number</span>; second: <span class="hljs-built_in">number</span> &#125;</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> first + second
&#125;
<span class="hljs-keyword">const</span> total = add(&#123; <span class="hljs-attr">first</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">second</span>: <span class="hljs-number">2</span> &#125;)

<span class="hljs-comment">// 解构一个变量时要注意</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getNumber</span>(<span class="hljs-params">&#123; first &#125;: &#123; first: <span class="hljs-built_in">number</span> &#125;</span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> first
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">其他情况</h2>
<p><code>any</code>：任意类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 其他：Date类型等</span>
<span class="hljs-keyword">const</span> data = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()

<span class="hljs-comment">// 其他的case: 比如用JSON.parse等函数时无法进行类型推断，要使用类型注解</span>
<span class="hljs-keyword">interface</span> Person &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"string"</span>
&#125;
<span class="hljs-keyword">const</span> rawData = <span class="hljs-string">'&#123;"name":"Dell"&#125;'</span>
<span class="hljs-keyword">const</span> newData = <span class="hljs-built_in">JSON</span>.parse(rawData) <span class="hljs-comment">// 类型推断无法使用，newDate为any类型</span>
<span class="hljs-keyword">const</span> newData2: Person = <span class="hljs-built_in">JSON</span>.parse(rawData) <span class="hljs-comment">// newDate2为Person类型</span>

<span class="hljs-keyword">let</span> temp: <span class="hljs-built_in">number</span> | <span class="hljs-built_in">string</span> = <span class="hljs-number">123</span>
temp = <span class="hljs-string">"456"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">类型断言</h2>
<p>有时候你会遇到这样的情况，你会比 TypeScript 更了解某个值的详细信息。通常这会发生在你清楚地知道一个实体具有比它现有类型更确切的类型。 通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。类型断言好比其它语言里的类型转换，但是不进行特殊的数据检查和解构。 它没有运行时的影响，只是在编译阶段起作用。 TypeScript 会假设你已经进行了必须的检查。</p>
<p>类型断言有两种形式。 其一是“尖括号”语法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>someValue).length
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个为 as 语法：(当在 TypeScript 里使用 JSX 时，只有 as 语法断言是被允许的)</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue2: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>
<span class="hljs-keyword">let</span> strLength2: <span class="hljs-built_in">number</span> = (someValue <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">interface-接口</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">type-类型别名</h2>
<p>类型别名也是一种类型，用一个单词代表可能比较复杂的类型声明，用关键字type表示。</p>
<p>示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> S = <span class="hljs-built_in">string</span>
<span class="hljs-keyword">let</span> a: S = <span class="hljs-string">'a'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用<code>S</code>作为<code>string</code>的别名，使用方法和<code>string</code>一模一样。</p>
<p>别名不仅可以代表基本类型，它可以代表任意类型。示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> SA = <span class="hljs-built_in">string</span>[] <span class="hljs-comment">// 代表字符串数组</span>
<span class="hljs-keyword">type</span> Handler = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span> <span class="hljs-comment">// 代表函数</span>
<span class="hljs-keyword">type</span> I = &#123;
  <span class="hljs-comment">// 代表接口</span>
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">value</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> = <span class="hljs-string">'a'</span>
  <span class="hljs-attr">value</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>
&#125;
<span class="hljs-keyword">type</span> D = C <span class="hljs-comment">// 代表类</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">高级类型</h2>
<p>主要有：联合、交叉、泛型、字面量类型等。</p>
<h3 data-id="heading-8">联合类型</h3>
<h3 data-id="heading-9">交叉类型</h3>
<h3 data-id="heading-10">泛型</h3>
<p>参考文章：<a href="https://juejin.cn/post/6949315742978277390" target="_blank">juejin.cn/post/694931…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            