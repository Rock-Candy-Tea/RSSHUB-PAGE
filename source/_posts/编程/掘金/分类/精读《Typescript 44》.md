
---
title: '精读《Typescript 4.4》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/194be1a1f09e4aa79811b1c0bb73ab42~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 17:55:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/194be1a1f09e4aa79811b1c0bb73ab42~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Typescript 4.4 正式发布了！距离 Typescript 4.5 发布还有三个月的时间，抓紧上车学习吧！</p>
<p>本周精读的文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/" ref="nofollow noopener noreferrer">announcing-typescript-4-4</a></p>
<h2 data-id="heading-0">概述</h2>
<h3 data-id="heading-1">更智能的自动类型收窄</h3>
<p>类型收窄功能非常方便，它可以让 Typescript 尽可能的像 Js 一样自动智能判定类型，从而避免类型定义的工作，让你的 Typescript 写得更像 Js。</p>
<p>其实这个功能早就有了，在我们 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fascoders%2Fweekly%2Fblob%2Fmaster%2F%25E5%2589%258D%25E6%25B2%25BF%25E6%258A%2580%25E6%259C%25AF%2F58.%25E7%25B2%25BE%25E8%25AF%25BB%25E3%2580%258ATypescript2.0%2520-%25202.9%25E3%2580%258B.md%23%25E8%2587%25AA%25E5%258A%25A8%25E7%25B1%25BB%25E5%259E%258B%25E6%258E%25A8%25E5%25AF%25BC" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ascoders/weekly/blob/master/%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF/58.%E7%B2%BE%E8%AF%BB%E3%80%8ATypescript2.0%20-%202.9%E3%80%8B.md#%E8%87%AA%E5%8A%A8%E7%B1%BB%E5%9E%8B%E6%8E%A8%E5%AF%BC" ref="nofollow noopener noreferrer">精读《Typescript2.0 - 2.9》</a> 就已经介绍过，当时用的名词是自动类型推导，这次用了更精确的自动类型收窄一词，因为只有类型收窄是安全的，比如：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">arg: unknown</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> arg === <span class="hljs-string">"string"</span>) &#123;
        <span class="hljs-comment">// We know 'arg' is a string now.</span>
        <span class="hljs-built_in">console</span>.log(arg.toUpperCase());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在 Typescript 4.4 之前的版本，如果我们将这个判定赋值给一个变量，再用到 <code>if</code> 分支里，就无法正常收窄类型了：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">arg: unknown</span>) </span>&#123;
    <span class="hljs-keyword">const</span> argIsString = <span class="hljs-keyword">typeof</span> arg === <span class="hljs-string">"string"</span>;
    <span class="hljs-keyword">if</span> (argIsString) &#123;
        <span class="hljs-built_in">console</span>.log(arg.toUpperCase());
        <span class="hljs-comment">//              ~~~~~~~~~~~</span>
        <span class="hljs-comment">// Error! Property 'toUpperCase' does not exist on type 'unknown'.</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个问题在 Typescript 4.4 得到了解决，实际上是把这种类型收窄判断逻辑加深了，即无论这个判断写在哪都可以生效。所以下面这种解构的用法判断也可以推断出类型收窄：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Shape =
    | &#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>, <span class="hljs-attr">radius</span>: <span class="hljs-built_in">number</span> &#125;
    | &#123; <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>, <span class="hljs-attr">sideLength</span>: <span class="hljs-built_in">number</span> &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">shape: Shape</span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-comment">// Extract out the 'kind' field first.</span>
    <span class="hljs-keyword">const</span> &#123; kind &#125; = shape;

    <span class="hljs-keyword">if</span> (kind === <span class="hljs-string">"circle"</span>) &#123;
        <span class="hljs-comment">// We know we have a circle here!</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * shape.radius ** <span class="hljs-number">2</span>;
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// We know we're left with a square here!</span>
        <span class="hljs-keyword">return</span> shape.sideLength ** <span class="hljs-number">2</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不仅是单一的判断，Typescript 4.4 还支持复合类型推导：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doSomeChecks</span>(<span class="hljs-params">
    inputA: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
    inputB: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
    shouldDoExtraWork: <span class="hljs-built_in">boolean</span>,
</span>) </span>&#123;
    <span class="hljs-keyword">const</span> mustDoWork = inputA && inputB && shouldDoExtraWork;
    <span class="hljs-keyword">if</span> (mustDoWork) &#123;
        <span class="hljs-comment">// We can access 'string' properties on both 'inputA' and 'inputB'!</span>
        <span class="hljs-keyword">const</span> upperA = inputA.toUpperCase();
        <span class="hljs-keyword">const</span> upperB = inputB.toUpperCase();
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mustDoWork</code> 为 <code>true</code> 的分支就意味着 <code>inputA</code>、<code>inputB</code> 均收窄为 <code>string</code> 类型。</p>
<p>这种深层的判定还体现在，一个具备类型判断的变量进行再计算，生成的变量还具有类型判断功能：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | <span class="hljs-built_in">boolean</span></span>) </span>&#123;
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
<p>可以看到，我们几乎可以像写 Js 一样写 Typescript，4.4 支持了大部分符合直觉的推导非常方便。但要注意的是，Typescript
毕竟不是运行时，无法做到更彻底的自动推断，但足以支持绝大部分场景。</p>
<h3 data-id="heading-2">下标支持 Symbol 与模版字符串类型判定</h3>
<p>原本我们定义一个用下标访问的对象是这样的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Values &#123;
  [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在也支持 Symbol 拉：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Colors &#123;
    [sym: symbol]: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> red = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"red"</span>);
<span class="hljs-keyword">const</span> green = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"green"</span>);
<span class="hljs-keyword">const</span> blue = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"blue"</span>);

<span class="hljs-keyword">let</span> colors: Colors = &#123;&#125;;

colors[red] = <span class="hljs-number">255</span>;          <span class="hljs-comment">// Assignment of a number is allowed</span>
<span class="hljs-keyword">let</span> redVal = colors[red];   <span class="hljs-comment">// 'redVal' has the type 'number'</span>

colors[blue] = <span class="hljs-string">"da ba dee"</span>; <span class="hljs-comment">// Error: Type 'string' is not assignable to type 'number'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且对于特定的字符串模版也支持类型匹配，比如希望以 <code>data-</code> 开头的下标是一种独立类型，可以这么定义：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Options &#123;
    width?: <span class="hljs-built_in">number</span>;
    height?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> a: Options = &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>,
    <span class="hljs-string">"data-blah"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// Error! 'data-blah' wasn't declared in 'Options'.</span>
&#125;;

<span class="hljs-keyword">interface</span> OptionsWithDataProps <span class="hljs-keyword">extends</span> Options &#123;
    <span class="hljs-comment">// Permit any property starting with 'data-'.</span>
    [optName: <span class="hljs-string">`data-<span class="hljs-subst">$&#123;<span class="hljs-built_in">string</span>&#125;</span>`</span>]: unknown;
&#125;

<span class="hljs-keyword">let</span> b: OptionsWithDataProps = &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>,
    <span class="hljs-string">"data-blah"</span>: <span class="hljs-literal">true</span>,       <span class="hljs-comment">// Works!</span>

    <span class="hljs-string">"unknown-property"</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// Error! 'unknown-property' wasn't declared in 'OptionsWithDataProps'.</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个对于 HTML 的 <code>data-</code> 属性非常有帮助。</p>
<p>同时还支持联合类型定义，下面两种类型定义方式是等价的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Data &#123;
    [optName: <span class="hljs-built_in">string</span> | symbol]: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-comment">// Equivalent to</span>

<span class="hljs-keyword">interface</span> Data &#123;
    [optName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
    [optName: symbol]: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">更严格的错误捕获类型</h3>
<p>在 <code>unknown</code> 类型出来之前，Typescript 以 <code>any</code> 作为抛出错误的默认类型，毕竟谁也不知道抛出错误的类型是什么：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// Who knows what this might throw...</span>
    executeSomeThirdPartyCode();
&#125;
<span class="hljs-keyword">catch</span> (err) &#123; <span class="hljs-comment">// err: any</span>
    <span class="hljs-built_in">console</span>.error(err.message); <span class="hljs-comment">// Allowed, because 'any'</span>
    err.thisWillProbablyFail(); <span class="hljs-comment">// Allowed, because 'any' :(</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Who knows what this might throw... 这句话很有意思，一个函数任何地方都可能出现运行时错误，这根本不是静态分析可以解决的，所以不可能自动推断错误类型，所以只能用 <code>any</code>。</p>
<p>在 Typescript 4.4 的 <code>--useUnknownInCatchVariables</code> 或 <code>--strict</code> 模式下都将以 <code>unknown</code> 作为捕获到错误的默认类型。</p>
<p>相比不存在的类型 <code>never</code>，<code>unknown</code> 仅仅是不知道是什么类型而已，所以不能像 <code>any</code> 一样当作任何类型使用，但我们可以将其随意推断为任意类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">try</span> &#123;
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
<p>如果觉得这样做麻烦，也可以重新申明类型为 <code>any</code>：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">try</span> &#123;
    executeSomeThirdPartyCode();
&#125;
<span class="hljs-keyword">catch</span> (err: <span class="hljs-built_in">any</span>) &#123;
    <span class="hljs-built_in">console</span>.error(err.message); <span class="hljs-comment">// Works again!</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这样做其实并不合适，因为即便是考虑了运行时因素，理论上还是可能发生意外错误，所以对错误过于自信的类型推断是不太合适的，最好保持其 <code>unknown</code> 类型，对所有可能的边界情况做处理。</p>
<h3 data-id="heading-4">明确的可选属性</h3>
<p>对象的可选属性在类型描述时有个含糊不清的地方，比如：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    age?: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 Typescript 对其的类型定义的是：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    age?: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要这么定义呢？因为很多情况下，没有这个 key，与这个 key 的值为 <code>undefined</code> 的表现是等价的。但比如 <code>Object.keys</code> 场景下这两种表现却又不等价，所以理论上对于 <code>age?: number</code> 的确切表述是：要么没有 <code>age</code>，要么有 <code>age</code> 且类型为 <code>number</code>，也就是说下面的写法应该是错误的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// With 'exactOptionalPropertyTypes' on:</span>
<span class="hljs-keyword">const</span> p: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Daniel"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// Error! undefined isn't a number</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Typescript 4.4 中同时开启 <code>--exactOptionalPropertyTypes</code> 与 <code>--strictNullChecks</code> 即可生效。</p>
<p>仔细想想这是合理的，既然定义的类型不是 <code>undefined</code>，就算对象是可选类型，也不能认为赋值 <code>undefined</code> 是合理的，因为 <code>age?: number</code> 的心理预期是，要么没有这个 key，要么有但是类型为 <code>number</code>，所以当 <code>Object.keys</code> 发现 <code>age</code> 这个 key 时，值就应该是 <code>number</code>。</p>
<h3 data-id="heading-5">支持 Static Block</h3>
<p>Typescript 4.4 支持了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-class-static-block%23ecmascript-class-static-initialization-blocks" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-class-static-block#ecmascript-class-static-initialization-blocks" ref="nofollow noopener noreferrer">class static blocks</a>，并且在代码块作用域内可以访问私有变量。</p>
<p>还有一些性能提升与体验优化杂项就不一一列举了，感兴趣可以直接看原文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-4%2F%23perf-improvements" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/#perf-improvements" ref="nofollow noopener noreferrer">perf-improvements</a>。</p>
<h2 data-id="heading-6">总结</h2>
<p>从 Typescript 4.4 特性可以看出，Typescript 正在往 “更具备原生 JS 亲和性” 方向作出努力，这无疑会使 Typescript 变得越来越好用。</p>
<p>对更多新特性感兴趣，可以 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fissues%2F45418" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/TypeScript/issues/45418" ref="nofollow noopener noreferrer">查看 Typescript 4.5 版本发布计划</a>。</p>
<blockquote>
<p>讨论地址是：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly%2Fissues%2F348" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly/issues/348" ref="nofollow noopener noreferrer">精读《Typescript 4.4》· Issue #348 · dt-fe/weekly</a></p>
</blockquote>
<p><strong>如果你想参与讨论，请 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly" ref="nofollow noopener noreferrer">点击这里</a>，每周都有新的主题，周末或周一发布。前端精读 - 帮你筛选靠谱的内容。</strong></p>
<blockquote>
<p>关注 <strong>前端精读微信公众号</strong></p>
</blockquote>
<img width="200" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/194be1a1f09e4aa79811b1c0bb73ab42~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>版权声明：自由转载-非商用-非衍生-保持署名（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-nd%2F3.0%2Fdeed.zh" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh" ref="nofollow noopener noreferrer">创意共享 3.0 许可证</a>）</p>
</blockquote></div>  
</div>
            