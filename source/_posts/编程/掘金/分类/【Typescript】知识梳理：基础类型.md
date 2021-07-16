
---
title: '【Typescript】知识梳理：基础类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1950'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 21:43:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=1950'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">数据类型</h2>
<h3 data-id="heading-1">布尔型<code>boolean</code></h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> isDone: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">数值<code>number</code></h3>
<p>TypeScript里的所有数字都是浮点数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> decLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">6</span>;
<span class="hljs-keyword">let</span> hexLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0xf00d</span>;<span class="hljs-comment">//十六进制</span>
<span class="hljs-keyword">let</span> binaryLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0b1010</span>;<span class="hljs-comment">//二进制</span>
<span class="hljs-keyword">let</span> octalLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">0o744</span>;<span class="hljs-comment">//八进制</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">字符串<code>string</code></h3>
<p>使用双引号（ <code>"</code>）或单引号（<code>'</code>）表示字符串。</p>
<p>使用模版字符串，它可以定义多行文本和内嵌表达式。 这种字符串是被反引号包围（<code>'</code>），并且以$&#123; expr &#125;这种形式嵌入表达式。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> name: <span class="hljs-built_in">string</span> = <span class="hljs-string">`Gene`</span>;
<span class="hljs-keyword">let</span> sentence: <span class="hljs-built_in">string</span> = <span class="hljs-string">`Hello, my name is <span class="hljs-subst">$&#123; name &#125;</span>.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">空值<code>void</code></h3>
<p>用于标识方法返回值的类型，表示该方法没有返回值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
    alert(<span class="hljs-string">"Hello Runoob"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">任意值<code>any</code></h3>
<p>允许被赋值为任意类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> notSure: <span class="hljs-built_in">any</span> = <span class="hljs-number">4</span>;
notSure = <span class="hljs-string">"maybe a string instead"</span>;
notSure = <span class="hljs-literal">false</span>; <span class="hljs-comment">// okay, definitely a boolean</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">数组<code>array</code></h3>
<p>可以在元素类型后面接上 <code>[]</code>，表示由此类型元素组成的一个数组:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> list: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用数组泛型,，<code>Array<元素类型></code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> list: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">元组<code>tuple</code></h3>
<p>元组类型用来表示已知元素数量和类型的数组，各元素的类型不必相同，对应位置的类型需要相同。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> x: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>];
x = [<span class="hljs-string">'Runoob'</span>, <span class="hljs-number">1</span>];    <span class="hljs-comment">// 运行正常</span>
x = [<span class="hljs-number">1</span>, <span class="hljs-string">'Runoob'</span>];    <span class="hljs-comment">// 报错</span>
<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">0</span>]);    <span class="hljs-comment">// 输出 Runoob</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">枚举<code>enum</code></h3>
<p>枚举类型用于定义数值集合。常用于取值被限定在一定范围内的场景，比如一周只能有七天，颜色限定为红绿蓝等。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Days &#123;Sun, Mon, Tue, Wed, Thu, Fri, Sat&#125;;

<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-string">"Sun"</span>] === <span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-string">"Mon"</span>] === <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-string">"Tue"</span>] === <span class="hljs-number">2</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-string">"Sat"</span>] === <span class="hljs-number">6</span>); <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-number">0</span>] === <span class="hljs-string">"Sun"</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-number">1</span>] === <span class="hljs-string">"Mon"</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-number">2</span>] === <span class="hljs-string">"Tue"</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(Days[<span class="hljs-number">6</span>] === <span class="hljs-string">"Sat"</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><code>null</code>和<code>undefined</code></h3>
<p><code>null</code>表示对象值缺失，<code>undefined</code>用于初始化变量为一个未定义的值。</p>
<p><code>undefined</code> 和 <code>null</code> 是所有类型的子类型。</p>
<h3 data-id="heading-10"><code>never</code></h3>
<p><code>never </code>是其它类型（包括 <code>null </code>和 undefined）的子类型，代表从不会出现的值。这意味着声明为 <code>never </code>类型的变量只能被 never类型所赋值，在函数中它通常表现为抛出异常或无法执行到终止点（例如无限循环）。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 返回值为 never 的函数可以是抛出异常的情况</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">error</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(message);
&#125;
<span class="hljs-comment">// 返回值为 never 的函数可以是无法被执行到的终止点的情况</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loop</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><code>object</code></h3>
<p><code>object</code>表示非原始类型，也就是除<code>number</code>，<code>string</code>，<code>boolean</code>，<code>symbol</code>，<code>null</code>或<code>undefined</code>之外的类型。</p>
<p>使用<code>object</code>类型，就可以更好的表示像<code>Object.create</code>这样的API。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">o: <span class="hljs-built_in">object</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">void</span></span>;

create(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-number">0</span> &#125;); <span class="hljs-comment">// OK</span>
create(<span class="hljs-literal">null</span>); <span class="hljs-comment">// OK</span>

create(<span class="hljs-number">42</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-string">"string"</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-literal">false</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">类型推论</h2>
<p>在初始化变量和成员，设置默认参数值和决定函数返回值时，类型推论会帮助提供类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> myFavoriteNumber = <span class="hljs-string">'seven'</span>;
myFavoriteNumber = <span class="hljs-number">7</span>;
<span class="hljs-comment">// index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果定义的时候没有赋值，不管之后有没有赋值，都会被推断成 <code>any</code> 类型而完全不被类型检查。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> myFavoriteNumber;
myFavoriteNumber = <span class="hljs-string">'seven'</span>;<span class="hljs-comment">//true</span>
myFavoriteNumber = <span class="hljs-number">7</span>;<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">联合类型</h2>
<p>联合类型（Union Types）表示取值可以为多种类型中的一种。联合类型使用 <code>|</code> 分隔每个类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> myFavoriteNumber: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>;
myFavoriteNumber = <span class="hljs-string">'seven'</span>;<span class="hljs-comment">//true</span>
myFavoriteNumber = <span class="hljs-number">7</span>;<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 TypeScript 不确定一个联合类型的变量到底是哪个类型的时候，我们<strong>只能访问此联合类型的所有类型里共有的属性或方法</strong>。</p>
<h2 data-id="heading-14">类型断言</h2>
<p>类型断言可以用来指定一个值的类型，即允许变量从一种类型更改为另一种类型。</p>
<h3 data-id="heading-15">语法格式</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><类型>值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或:</p>
<pre><code class="hljs language-ts copyable" lang="ts">值 <span class="hljs-keyword">as</span> 类型
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 tsx 语法（React 的 jsx 语法的 ts 版）中必须使用后者，即 <code>值 as 类型</code>。</p>
<p>形如 <code><Foo></code> 的语法在 tsx 中表示的是一个 <code>ReactNode</code>，在 ts 中除了表示类型断言之外，也可能是表示一个泛型。</p>
<h3 data-id="heading-16">用途总结</h3>
<ul>
<li>联合类型可以被断言成其中一个类型（类型断言不是类型转换，断言成一个联合类型中不存在的类型是不允许的。类型断言只能够「欺骗」TypeScript 编译器，无法避免运行时的错误，反而滥用类型断言可能会导致运行时错误）</li>
<li>父类可以断言成子类（实际运用中使用 <code>instanceof</code> 更加合适）</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ApiError</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Error</span> </span>&#123;
    <span class="hljs-attr">code</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HttpError</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Error</span> </span>&#123;
    <span class="hljs-attr">statusCode</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">200</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isApiError</span>(<span class="hljs-params">error: <span class="hljs-built_in">Error</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> (error <span class="hljs-keyword">as</span> ApiError).code === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="hljs-comment">//上下两者等价实现</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isApiError</span>(<span class="hljs-params">error: <span class="hljs-built_in">Error</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (error <span class="hljs-keyword">instanceof</span> ApiError) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>任何类型可以断言成any（<strong>一方面不能滥用 <code>as any</code>，另一方面也不要完全否定它的作用，我们需要在类型的严格性和开发的便利性之间掌握平衡</strong>（这也是 TypeScript 的设计理念之一），才能发挥出 TypeScript 最大的价值。）</li>
<li>any 可以断言成任何类型</li>
</ul></div>  
</div>
            