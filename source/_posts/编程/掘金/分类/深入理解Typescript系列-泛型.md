
---
title: '深入理解Typescript系列-泛型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6320'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 18:35:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=6320'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 15 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>在我们的日常开发中，时长会考虑到方法的复用性，毕竟对于相似的场景拷贝一份代码既增加了代码量还增加了额外的维护成本，要是重构的时候忘了，还会导致不可描述的bug。</p>
<h2 data-id="heading-1">初探泛型</h2>
<p>我们先来看这么一段代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span>(<span class="hljs-params">arg: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数会返回任何传入它的值。但是只能输入number类型。那我们把它改造一下，支持任意类型呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span>(<span class="hljs-params">arg: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候，返回值为any了，这明显会不合理。针对这个场景，我们的想法是返回值类型是根据输入值类型确定的，我们引入泛型，可以这么写</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们给identity添加了类型变量T。 T帮助我们捕获用户传入的类型（比如：number），之后我们就可以使用这个类型。 之后我们再次使用了 T当做返回值类型。现在我们可以知道参数类型与返回值类型是相同的了。 这允许我们跟踪函数里使用的类型的信息。</p>
<p>我们把这个版本的identity函数叫做泛型，因为它可以适用于多个类型。 不同于使用 any，它不会丢失信息，像第一个例子那像保持准确性，传入数值类型并返回数值类型。</p>
<h2 data-id="heading-2">泛型类型</h2>
<p>假设我们这时候需要对string类型的值做一些特殊判断，那该怎么做呢？TS是支持类型的动态推导的，可以可以这么写：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> arg === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-comment">// arg类型自动推导为arg</span>
        <span class="hljs-keyword">return</span> arg + <span class="hljs-string">'x'</span>;
    &#125;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">react中的泛型</h2>
<p>如果平常用TS写过react，应该已经接触过泛型了，可能不知道这叫泛型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> State &#123;

&#125;
<span class="hljs-keyword">interface</span> Props &#123;
    
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span><<span class="hljs-title">State</span>, <span class="hljs-title">Props</span>> </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于React的Component的开发者不清楚使用者会如何使用，所以在设计类的时候就支持了泛型。通过传入State和Props的类型，可以在类的实现过程中可以获取到状态的类型。</p>
<h2 data-id="heading-4">泛型约束</h2>
<p>有时我们可能希望限制每个类型变量接受的类型数量，这就是泛型约束的作用。</p>
<p>泛型约束的另一个常见的使用场景就是检查对象上的键是否存在。不过在看具体示例之前，我们得来了解一下 keyof 操作符。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
  location: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">type</span> K1 = keyof Person; <span class="hljs-comment">// "name" | "age" | "location"</span>
<span class="hljs-keyword">type</span> K2 = keyof Person[];  <span class="hljs-comment">// number | "length" | "push" | "concat" | ...</span>
<span class="hljs-keyword">type</span> K3 = keyof &#123; [x: <span class="hljs-built_in">string</span>]: Person &#125;;  <span class="hljs-comment">// string | number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">在泛型里使用类类型</h2>
<p>在TypeScript使用泛型创建工厂函数时，需要引用构造函数的类类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span><<span class="hljs-title">T</span>>(<span class="hljs-params">c: &#123;<span class="hljs-keyword">new</span>(): T; &#125;</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> c();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">小结</h2>
<p>泛型的本质是做运行时的replace all，通过动态的检查，可以动态进行类型推导校验，降低重复代码，提升整体代码的复用性。泛型是对类型进行编程，参数是类型，返回值是一个新的类型。我们甚至可以对泛型的参数进行约束，就类似于函数的类型约束。</p></div>  
</div>
            