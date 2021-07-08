
---
title: '_译_TypeScript 4.4 Beta版本发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcca6b4725443bb8d19e86080901c06~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 23:28:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcca6b4725443bb8d19e86080901c06~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4-beta%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/" ref="nofollow noopener noreferrer">devblogs.microsoft.com/typescript/…</a></p>
</blockquote>
<p>TypeScript4.4版本的一些主要亮点：</p>
<ul>
<li>别名条件下的控制流分析</li>
<li>Symbol和模板字符串模式索引签名</li>
<li>Catch变量中默认为<code>unknown</code>类型（<code>--useUnknownInCatchVariables</code>)</li>
<li>严格的可选属性类型(<code>--exactOptionalPropertyTypes</code>)</li>
<li><code>tsc --help</code>的更新和提升</li>
<li>性能提升</li>
<li>对于JavaScript的拼写建议</li>
<li>内嵌提示</li>
<li>不兼容的变更</li>
</ul>
<h2 data-id="heading-0">别名条件下的控制流分析</h2>
<p>在JavaScript中，我们经常需要用不同的方式去探测一个变量，看看它是否有一个我们可以使用的更加具体的类型。TypeScript理解这些探测并且把它们称作类型保护（<em>type guards</em>）。当我们使用变量类型时，类型检查器不必让TypeScript相信它的类型，而是利用一种称为控制流分析（<em>control flow analysis</em>）的方法来推断每个语言构造中的类型。</p>
<p>例如，我们可以这么写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">arg: unknown</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> arg === <span class="hljs-string">"string"</span>) &#123;
        <span class="hljs-comment">// We know this is a string now.</span>
        <span class="hljs-built_in">console</span>.log(arg.toUpperCase());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，我们检查<code>arg</code>是否是一个<code>string</code>。TypeScript识别了<code>typeof arg===“string”</code>检查，它认为这是一个类型保护，并且能够确定arg应该是if块主体中的字符串。</p>
<p>然而，如果我们将条件移出到一个常量中呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">arg: unknown</span>) </span>&#123;
    <span class="hljs-keyword">const</span> argIsString = <span class="hljs-keyword">typeof</span> arg === <span class="hljs-string">"string"</span>;
    <span class="hljs-keyword">if</span> (argIsString) &#123;
        <span class="hljs-built_in">console</span>.log(arg.toUpperCase());
        <span class="hljs-comment">//              ~~~~~~~~~~~</span>
        <span class="hljs-comment">// Error! Property 'toUpperCase' does not exist on type 'unknown'.</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在之前版本的TypeScript中，这里会报错——即使<code>argIsString</code>被分配了一个类型守卫的值，TypeScript也会丢失掉这个信息。更不走运的是，我们可能想要在几个地方重用同样的检查。为了避免这种情况，用户通常必须重复自己的操作或使用类型断言。</p>
<p>在TypeScript 4.4中，情况不再如此，上述例子不会出错。当TypeScript看到我们正在测试一个常量值时，它将做一些额外的工作来查看它是否包含类型保护。如果该类型保护对常量、只读属性或未修改的参数进行操作，那么TypeScript可以适当地缩小该值的范围。</p>
<p>不同类型的类型保护条件被保留下来——不仅仅是<code>typeof</code>的检查。例如，对区别联合类型的检查就可以很优雅：</p>
<pre><code class="hljs language-js copyable" lang="js">type Shape =
    | &#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">radius</span>: number &#125;
    | &#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>, <span class="hljs-attr">sideLength</span>: number &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">shape: Shape</span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">const</span> isCircle = shape.kind === <span class="hljs-string">"circle"</span>;
    <span class="hljs-keyword">if</span> (isCircle) &#123;
        <span class="hljs-comment">// We know we have a circle here!</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * shape.radius ** <span class="hljs-number">2</span>;
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// We know we're left with a square here!</span>
        <span class="hljs-keyword">return</span> shape.sideLength ** <span class="hljs-number">2</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个例子，这里有一个函数用来检查它的两个输入是否有内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doSomeChecks</span>(<span class="hljs-params">
    inputA: string | <span class="hljs-literal">undefined</span>,
    inputB: string | <span class="hljs-literal">undefined</span>,
    shouldDoExtraWork: boolean,
</span>) </span>&#123;
    <span class="hljs-keyword">let</span> mustDoWork = inputA && inputB && shouldDoExtraWork;
    <span class="hljs-keyword">if</span> (mustDoWork) &#123;
        <span class="hljs-comment">// Can access 'string' properties on both 'inputA' and 'inputB'!</span>
        <span class="hljs-keyword">const</span> upperA = inputA.toUpperCase();
        <span class="hljs-keyword">const</span> upperB = inputB.toUpperCase();
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>mustDoWork</code>为<code>true</code>，TypeScript可以理解<code>inputA</code>和<code>inputB</code>都存在。这意味着我们不必编写像<code>inputA!</code>这样的非空断言来使TypeScript确信<code>inputA</code>不是<code>undefined</code>。</p>
<p>另一个优点就是这种分析是传递性的。如果我们给一个条件分配了一个常量，这个条件中有更多的常量，这些常量都是被分配了类型保护，那么TypeScript可以向后传递这些条件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x: string | number | boolean</span>) </span>&#123;
    <span class="hljs-keyword">const</span> isString = <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"string"</span>;
    <span class="hljs-keyword">const</span> isNumber = <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"number"</span>;
    <span class="hljs-keyword">const</span> isStringOrNumber = isString || isNumber;
    <span class="hljs-keyword">if</span> (isStringOrNumber) &#123;
        x;  <span class="hljs-comment">// Type of 'x' is 'string | number'.</span>
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        x;  <span class="hljs-comment">// Type of 'x' is 'boolean'.</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，在检查这些条件时，TypeScript不会任意深入，但它的分析对于大多数检查来说已经足够深入了。</p>
<p>这个特性可以让很多直观的JavaScript代码在TypeScript中“正常工作”，而不会妨碍用户。有关更多详细信息，请查看GitHub上的实现。</p>
<h2 data-id="heading-1">Symbol和模板字符串模式索引签名</h2>
<p>TypeScript允许我们使用索引签名（<em>index signatures</em>）描述每个属性都必须具有特定类型的对象。这允许我们将这些对象用作类似于字典的类型，我们可以使用字符串键以方括号对它们进行索引。</p>
<p>例如，我们可以编写一个带有索引签名的类型，该类型接受字<code>string</code>键并映射到<code>boolean</code>值上。如果我们尝试分配除<code>boolean</code>值以外的任何值，我们将得到一个错误。</p>
<pre><code class="hljs language-js copyable" lang="js">interface BooleanDictionary &#123;
    [key: string]: boolean;
&#125;

declare <span class="hljs-keyword">let</span> myDict: BooleanDictionary;

<span class="hljs-comment">// Valid to assign boolean values</span>
myDict[<span class="hljs-string">"foo"</span>] = <span class="hljs-literal">true</span>;
myDict[<span class="hljs-string">"bar"</span>] = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// Error, "oops" isn't a boolean</span>
myDict[<span class="hljs-string">"baz"</span>] = <span class="hljs-string">"oops"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然Map在这里可能是一种更好的数据结构（特别是<code>Map<string，boolean></code>），但是JavaScript对象通常使用起来更方便，或者正好是我们要处理的对象。</p>
<p>类似地，<code>Array<T></code>已经定义了一个<code>number</code>索引签名，允许我们插入/检索类型<code>T</code>的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// This is part of TypeScript's definition of the built-in Array type.</span>
interface <span class="hljs-built_in">Array</span><T> &#123;
    [index: number]: T;

    <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span><string>();

<span class="hljs-comment">// Valid</span>
arr[<span class="hljs-number">0</span>] = <span class="hljs-string">"hello!"</span>;

<span class="hljs-comment">// Error, expecting a 'string' value here</span>
arr[<span class="hljs-number">1</span>] = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>索引签名对于在外部表达大量代码时非常有用；然而，到目前为止，它们仅限于<code>string</code>和<code>number</code>键（而且<code>string</code>索引签名有一个故意的怪癖，它们可以接受<code>number</code>键，因为它们无论如何都会被强制为字符串）。这意味着TypeScript不允许用<code>symbol</code>键索引对象。TypeScript也不能为某些<code>string</code>键的子集进行索引签名建模，例如，仅仅以<code>data-</code>开头的属性索引签名。</p>
<p>TypeScript 4.4解决了这些限制，并允许对<code>symbol</code>和模板字符串模式进行索引签名。</p>
<p>例如，TypeScript现在允许我们声明一个可以在任意<code>symbol</code>上键入的类型。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Colors &#123;
    [sym: symbol]: number;
&#125;

<span class="hljs-keyword">const</span> red = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"red"</span>);
<span class="hljs-keyword">const</span> green = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"green"</span>);
<span class="hljs-keyword">const</span> blue = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"blue"</span>);

<span class="hljs-keyword">let</span> colors: Colors = &#123;&#125;;

colors[red] = <span class="hljs-number">255</span>;          <span class="hljs-comment">// Assignment of a number is allowed</span>
<span class="hljs-keyword">let</span> redVal = colors[red];   <span class="hljs-comment">// 'redVal' has the type 'number'</span>

colors[blue] = <span class="hljs-string">"da ba dee"</span>; <span class="hljs-comment">// Error: Type 'string' is not assignable to type 'number'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似地，我们可以使用模板字符串模式类型编写索引签名。这样做的一个用途可能是从TypeScript的多余属性检查中免除以<code>data-</code>开头的属性。当我们将对象文本传递给具有预期类型的对象时，TypeScript将查找预期类型中未声明的多余属性。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Options &#123;
    width?: number;
    height?: number;
&#125;

<span class="hljs-keyword">let</span> a: Options = &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>,
    <span class="hljs-string">"data-blah"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// Error! 'data-blah' wasn't declared in 'Options'.</span>
&#125;;

interface OptionsWithDataProps <span class="hljs-keyword">extends</span> Options &#123;
    <span class="hljs-comment">// Permit any property starting with 'data-'.</span>
    [optName: <span class="hljs-string">`data-<span class="hljs-subst">$&#123;string&#125;</span>`</span>]: unknown;
&#125;

<span class="hljs-keyword">let</span> b: OptionsWithDataProps = &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>,
    <span class="hljs-string">"data-blah"</span>: <span class="hljs-literal">true</span>,       <span class="hljs-comment">// Works!</span>

    <span class="hljs-string">"unknown-property"</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// Error! 'unknown-property' wasn't declared in 'OptionsWithDataProps'.</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于索引签名的最后一点是，它们现在允许联合类型，只要它们是无限域基元类型的联合—特别是：</p>
<ul>
<li>string</li>
<li>number</li>
<li>symbol</li>
<li>模板字符串模式(e.g. <code>hello-$&#123;string&#125;</code>)</li>
</ul>
<p>其参数是这些类型的并集的索引签名将分解为多个不同的索引签名。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Data &#123;
    [optName: string | symbol]: any;
&#125;

<span class="hljs-comment">// Equivalent to</span>

interface Data &#123;
    [optName: string]: any;
    [optName: symbol]: any;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Catch变量中默认为<code>unknown</code>类型（<code>--useUnknownInCatchVariables</code>）</h2>
<p>在JavaScript中，任何类型的值都可以通过<code>throw</code>抛出，并在<code>catch</code>子句中捕获。因此，TypeScript历史上将<code>catch</code>子句变量类型化为<code>any</code>，并且不允许任何其他类型的注释：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// Who knows what this might throw...</span>
    executeSomeThirdPartyCode();
&#125;
<span class="hljs-keyword">catch</span> (err) &#123; <span class="hljs-comment">// err: any</span>
    <span class="hljs-built_in">console</span>.error(err.message); <span class="hljs-comment">// Allowed, because 'any'</span>
    err.thisWillProbablyFail(); <span class="hljs-comment">// Allowed, because 'any' :(</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦TypeScript添加了<code>unknown</code>类型，很明显地，对于那些希望获得最高程度的正确性和类型安全性的用户来说，在<code>catch</code>子句<code>unknown</code>比<code>any</code>变量都是一个更好的选择，因为它可以更好地缩小范围，并迫使我们针对任意值进行测试。最终，Typescript 4.0允许用户在每个<code>catch</code>子句变量上指定一个<code>unknown</code>（或<code>any</code>）的显式类型注释，这样我们就可以根据具体情况选择更严格的类型；然而，对于某些人来说，在每个<code>catch</code>子句上手动指定<code>unknown</code>是件麻烦事。</p>
<p>这就是为什么TypeScript 4.4引入了一个名为<code>--useUnknownInCatchVariables</code>的新标志。此标志将<code>catch</code>子句变量的默认类型从<code>any</code>更改为<code>unknown</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
    executeSomeThirdPartyCode();
&#125;
<span class="hljs-keyword">catch</span> (err) &#123; <span class="hljs-comment">// err: unknown</span>

    <span class="hljs-comment">// Error! Property 'message' does not exist on type 'unknown'.</span>
    <span class="hljs-built_in">console</span>.error(err.message);

    <span class="hljs-comment">// Works! We can narrow 'err' from 'unknown' to 'Error'.</span>
    <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Error</span>) &#123;
        <span class="hljs-built_in">console</span>.error(err.message);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此标志在<code>--strict</code>选项族下启用。这意味着，如果您使用<code>--strict</code>检查代码，此选项将<strong>自动启用</strong>。在TypeScript 4.4中可能会出现错误，例如</p>
<pre><code class="hljs language-js copyable" lang="js">Property <span class="hljs-string">'message'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
Property <span class="hljs-string">'name'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
Property <span class="hljs-string">'stack'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们不想在<code>catch</code>子句中处理<code>unknown</code>变量，我们总是可以添加显式的<code>：any</code>注释，这样我们就可以选择不使用更严格的类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
    executeSomeThirdPartyCode();
&#125;
<span class="hljs-keyword">catch</span> (err: any) &#123;
    <span class="hljs-built_in">console</span>.error(err.message); <span class="hljs-comment">// Works again!</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">严格的可选属性类型 (--exactOptionalPropertyTypes)</h2>
<p>在JavaScript中，读取对象上缺少的属性会产生<code>undefined</code>的值。也可能实际存在一个属性，它的值是<code>undefined</code>。JavaScript中的许多代码倾向于以相同的方式处理这些情况，因此最初TypeScript只是解释每个可选属性，就好像用户在类型中编写了<code>undefined</code>一样。例如，</p>
<pre><code class="hljs language-js copyable" lang="js">interface Person &#123;
    <span class="hljs-attr">name</span>: string,
    age?: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于</p>
<pre><code class="hljs language-js copyable" lang="js">interface Person &#123;
    <span class="hljs-attr">name</span>: string,
    age?: number | <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这意味着用户可以显式地编写<code>undefined</code>来代替<code>age</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Daniel"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// This is okay by default.</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，默认情况下，TypeScript不区分值为<code>undefined</code>的现存属性和缺失属性。虽然这在大多数情况下都是有效的，但并非JavaScript中的所有代码都做出相同的假设。像<code>Object.assign</code>、<code>Object.keys</code>、对象解构（<code>&#123;…obj&#125;</code>）和<code>for–in</code>循环这样的函数和操作符，根据对象上的属性是否实际存在而表现不同。在我们的<code>Person</code>示例中，如果当age属性的存在是非常重要的情况下，则这可能会导致运行时错误。</p>
<p>在TypeScript 4.4中，新的标志<code>--exactOptionalPropertyTypes</code>指定可选属性类型应完全按照写入的方式进行解释，这意味着<code>undefined</code>不会添加到类型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// With 'exactOptionalPropertyTypes' on:</span>
<span class="hljs-keyword">const</span> p: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Daniel"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// Error! undefined isn't a number</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个标志不是<code>--strict</code>家族的一部分，如果想要开启这个这个行为，就需要显式地打开它。它还需要启用<code>--strictNullChecks</code>。</p>
<h2 data-id="heading-4">tsc --help帮助更新和改进</h2>
<p>TypeScript的<code>--help</code>选项得到了更新，多亏了宋高的一部分工作，我们引入了一些变化来更新编译器选项的描述，并用一些颜色和其他视觉分隔重新设置--help菜单的样式。虽然我们仍在迭代一些样式，以便跨平台默认主题很好地工作，但你可以通过查看原始建议线程来了解它的外观。</p>
<h2 data-id="heading-5">性能提升</h2>
<h3 data-id="heading-6">更快的声明触发</h3>
<p>TypeScript现在对不同上下文中是否可以访问内部符号以及如何打印特定类型进行了缓存。这些更改可以提高TypeScript在具有相当复杂类型的代码中的总体性能，尤其是在发出<code>--declaration</code>标志下的<code>.d.ts</code>文件时。</p>
<blockquote>
<p>没翻译明白这块……</p>
</blockquote>
<h3 data-id="heading-7">更快的路径规范化</h3>
<p>TypeScript通常必须对文件路径执行几种类型的“规范化”，以使它们成为编译器可以在任何地方使用的一致格式。这包括用斜杠替换反斜杠，或者删除路径的中间<code>/./</code>和<code>/../</code>段。当TypeScript必须在数百万条路径上运行时，这些操作最终会有点慢。在TypeScript 4.4中，首先要对路径进行快速检查，以确定它们首先是否需要任何规范化。这些改进在更大的项目上共同减少了5-10%的加载时间，并且在我们内部测试过的大型项目上有显著的效果。</p>
<h3 data-id="heading-8">更快的路径映射</h3>
<p>TypeScript现在对它构造路径映射的方式（使用<code>tsconfig.json</code>中的<code>paths</code>选项）进行了缓存，对于具有几百个映射的项目是非常重要的。</p>
<h3 data-id="heading-9">使用<code>--strict</code>更快的增量构建</h3>
<p>实际上这是一个bug，如果是<code>--strict</code>开启的情况下，在<code>--incremental</code>编译下，TypeScript最终会重做类型检查工作。这导致许多构建的速度都很慢，就像增量构建被关闭了一样。TypeScript 4.4修复了这个问题，不过这个变化也被移植到了TypeScript4.3中。</p>
<h3 data-id="heading-10">对大输出进行更快的Source Map生成</h3>
<p>TypeScript 4.4添加了一个优化，用于在非常大的输出文件上生成源映射。在构建旧版本的TypeScript编译器时，这将减少大约8%的触发时间。</p>
<h3 data-id="heading-11">更快的<code>--force</code>构建</h3>
<p>在项目引用上使用<code>--build</code>模式时，TypeScript必须执行最新检查，以确定需要重新构建哪些文件。但是，在执行<code>--force</code>构建时，这些信息无关紧要，因为每个项目依赖项都将从头开始重建。在TypeScript 4.4中，<code>--force</code>构建避免那些不必要的步骤，并开始完整的生成。</p>
<h2 data-id="heading-12">JavaScript拼写建议</h2>
<p>TypeScript支持在visual studio和visual studio code等编辑器中进行JavaScript编辑。大多数时候，TypeScript试图在JavaScript文件中置身事外；然而，TypeScript通常有大量的信息来提供可信的建议，以及呈现建议的方法，并且不会太具侵入性。</p>
<p>这就是为什么TypeScript现在在普通JavaScript文件中发出拼写建议的原因，这些文件没有<code>//@ts check</code>，或者是在<code>checkJs</code>关闭了的项目中。这些都是TypeScript文件已经有的“Did you mean…？”建议，现在它们以某种形式出现在所有JavaScript文件中。</p>
<h2 data-id="heading-13">内嵌提示</h2>
<p>TypeScript正在试验对嵌入文本的编辑器支持，它可以帮助在代码中显示有用的信息，比如内联的参数名。你可以把它看作是一种友好的“内嵌文本”。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcca6b4725443bb8d19e86080901c06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">不兼容性更改</h2>
<h3 data-id="heading-15">TypeScript 4.4中lib.d.ts的更改</h3>
<p>与每个TypeScript版本一样，lib.d.ts的声明（尤其是为web上下文生成的声明）也发生了变化。您可以查阅我们已知的lib.dom.d.ts更改列表来了解受影响的内容。</p>
<h3 data-id="heading-16">在Catch变量中使用<code>unknown</code></h3>
<p>从技术上讲，使用<code>--strict</code>标志运行的用户可能会看到围绕<code>catch</code>变量的新错误是<code>unknown</code>的，特别是在现有代码假定只捕获了<code>Error</code>值的情况下。这通常会导致错误消息，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">Property <span class="hljs-string">'message'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
Property <span class="hljs-string">'name'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
Property <span class="hljs-string">'stack'</span> does not exist on type <span class="hljs-string">'unknown'</span>.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了避免这种情况，您可以特别添加运行时检查，以确保抛出的类型与预期的类型匹配。或者，您可以只使用类型断言，向<code>catch</code>变量添加显式的<code>：any</code>，或者关闭<code>--useUnknownInCatchVariables</code>。</p>
<h3 data-id="heading-17">抽象属性不允许初始值设定</h3>
<p>下面的代码现在会报错，因为抽象属性可能没有初始值设定项：</p>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    abstract prop = <span class="hljs-number">1</span>;
    <span class="hljs-comment">//       ~~~~</span>
    <span class="hljs-comment">// Property 'prop' cannot have an initializer because it is marked abstract.</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相反地，只能为属性指定类型：</p>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    abstract prop: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">下一步</h2>
<p>目前的目标是在8月中旬发布一个候选版本，并在2021年8月底发布一个稳定的版本。</p></div>  
</div>
            