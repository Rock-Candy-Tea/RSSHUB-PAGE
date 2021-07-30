
---
title: '【Typescript】知识梳理：泛型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6096'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 23:52:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=6096'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">泛型基础</h2>
<p>泛型（Generics）是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性。</p>
<p>不用泛型，用<code>any</code>类型来定义函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span>(<span class="hljs-params">arg: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>any</code>类型会导致这个函数可以接收任何类型的<code>arg</code>参数，这样就丢失了一些信息：传入的类型与返回的类型应该是相同的。 如果传入一个数字，只知道任何类型的值都有可能被返回。</p>
<p>因此，需要一种方法使返回值的类型与传入参数的类型是相同的。 这里使用了类型变量，它是一种特殊的变量，只用于表示类型而不是值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>identity添加了类型变量<code>T</code>。 <code>T</code>帮助捕获用户传入的类型（比如：<code>number</code>），并可以使用这个类型。 之后再次使用了<code>T</code>当做返回值类型。现在参数类型与返回值类型是相同的， 如此允许跟踪函数里使用的类型的信息。</p>
<p>定义了泛型函数后，可以用两种方法使用。 第一种是，传入所有的参数，包含类型参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> output = identity<<span class="hljs-built_in">string</span>>(<span class="hljs-string">"myString"</span>);  <span class="hljs-comment">// type of output will be 'string'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里明确的指定了<code>T</code>是<code>string</code>类型，并做为一个参数传给函数，使用了<code><></code>括起来而不是<code>()</code>。</p>
<p>第二种方法更普遍。利用了类型推论-- 即编译器会根据传入的参数自动地帮助我们确定T的类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> output = identity(<span class="hljs-string">"myString"</span>);  <span class="hljs-comment">// type of output will be 'string'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时没必要使用尖括号（<code><></code>）来明确地传入类型；编译器可以查看<code>myString</code>的值，然后把<code>T</code>设置为它的类型。 类型推论帮助保持代码精简和高可读性。</p>
<h2 data-id="heading-1">泛型类型</h2>
<p>泛型函数的类型与非泛型函数的类型没什么不同，只是有一个类型参数在最前面，像函数声明一样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-keyword">let</span> myIdentity: <T><span class="hljs-function">(<span class="hljs-params">arg: T</span>) =></span> T = identity;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以使用不同的泛型参数名，只要在数量上和使用方式上能对应上就可以。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-keyword">let</span> myIdentity: <U><span class="hljs-function">(<span class="hljs-params">arg: U</span>) =></span> U = identity;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以使用带有调用签名的对象字面量来定义泛型函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-keyword">let</span> myIdentity: &#123;<T>(arg: T): T&#125; = identity;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">多个类型参数</h2>
<p>定义泛型的时候，可以一次定义多个类型参数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swap</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">tuple: [T, U]</span>): [<span class="hljs-title">U</span>, <span class="hljs-title">T</span>] </span>&#123;
    <span class="hljs-keyword">return</span> [tuple[<span class="hljs-number">1</span>], tuple[<span class="hljs-number">0</span>]];
&#125;
​
<span class="hljs-comment">//定义了一个swap函数，用来交换输入的元组。</span>
swap([<span class="hljs-number">7</span>, <span class="hljs-string">'seven'</span>]); <span class="hljs-comment">// ['seven', 7]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">泛型约束</h2>
<p>在函数内部使用泛型变量的时候，由于事先不知道它是哪种类型，所以不能随意的操作它的属性或方法。</p>
<p>此时，我们可以对泛型进行约束，只允许这个函数传入那些包含 该属性的变量。这就是泛型约束。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Lengthwise &#123;
    <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Lengthwise</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例，也可以设为T类型的数组默认<code>.length</code>属性存在：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T[]</span>): <span class="hljs-title">T</span>[] </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);  <span class="hljs-comment">// Array has a .length, so no more error</span>
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: <span class="hljs-built_in">Array</span><T></span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);  <span class="hljs-comment">// Array has a .length, so no more error</span>
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多个类型参数之间也可以互相约束：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//例中，使用了两个类型参数，其中要求 T 继承 U，这样就保证了 U 上不会出现 T 中不存在的字段。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyFields</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">U</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">target: T, source: U</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id <span class="hljs-keyword">in</span> source) &#123;
        target[id] = (<T>source)[id];
    &#125;
    <span class="hljs-keyword">return</span> target;
&#125;
​
<span class="hljs-keyword">let</span> x = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">d</span>: <span class="hljs-number">4</span> &#125;;
​
copyFields(x, &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">d</span>: <span class="hljs-number">20</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">泛型接口</h2>
<p>依据上例里的对象字面量拿出来做为一个接口：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> GenericIdentityFn &#123;
    <T>(arg: T): T;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-keyword">let</span> myIdentity: GenericIdentityFn = identity;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例，可以把泛型参数当作整个接口的一个参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> GenericIdentityFn<T> &#123;
    (arg: T): T;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;
​
<span class="hljs-keyword">let</span> myIdentity: GenericIdentityFn<<span class="hljs-built_in">number</span>> = identity;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<strong>此时在使用泛型接口的时候，需要定义泛型的类型。</strong></p>
<h2 data-id="heading-5">泛型类</h2>
<p>与泛型接口类似，泛型也可以用于类的类型定义中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GenericNumber</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-attr">zeroValue</span>: T;
    add: <span class="hljs-function">(<span class="hljs-params">x: T, y: T</span>) =></span> T;
&#125;
​
<span class="hljs-keyword">let</span> myGenericNumber = <span class="hljs-keyword">new</span> GenericNumber<<span class="hljs-built_in">number</span>>();
myGenericNumber.zeroValue = <span class="hljs-number">0</span>;
myGenericNumber.add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x, y</span>) </span>&#123; <span class="hljs-keyword">return</span> x + y; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">泛型参数的默认类型</h2>
<p>在 TypeScript 2.3 以后，可以为泛型中的类型参数指定默认类型。当使用泛型时没有在代码中直接指定类型参数，从实际值参数中也无法推测出时，这个默认类型就会起作用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createArray</span><<span class="hljs-title">T</span> = <span class="hljs-title">string</span>>(<span class="hljs-params">length: <span class="hljs-built_in">number</span>, value: T</span>): <span class="hljs-title">Array</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">let</span> result: T[] = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
        result[i] = value;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">在泛型里使用类类型</h2>
<p>在TypeScript使用泛型创建工厂函数时，需要引用构造函数的类类型。比如，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span><<span class="hljs-title">T</span>>(<span class="hljs-params">c: &#123;<span class="hljs-keyword">new</span>(): T; &#125;</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> c();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下例，使用原型属性推断并约束构造函数与类实例的关系：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BeeKeeper</span> </span>&#123;
    <span class="hljs-attr">hasMask</span>: <span class="hljs-built_in">boolean</span>;
&#125;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ZooKeeper</span> </span>&#123;
    <span class="hljs-attr">nametag</span>: <span class="hljs-built_in">string</span>;
&#125;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">numLegs</span>: <span class="hljs-built_in">number</span>;
&#125;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bee</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">keeper</span>: BeeKeeper;
&#125;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lion</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">keeper</span>: ZooKeeper;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span><<span class="hljs-title">A</span> <span class="hljs-title">extends</span> <span class="hljs-title">Animal</span>>(<span class="hljs-params">c: <span class="hljs-keyword">new</span> () => A</span>): <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> c();
&#125;
​
createInstance(Lion).keeper.nametag;  <span class="hljs-comment">// typechecks!</span>
createInstance(Bee).keeper.hasMask;   <span class="hljs-comment">// typechecks!</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            