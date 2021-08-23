
---
title: '精读《Typescript infer 关键字》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d32be823646f4a43acead3477238067d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 18:10:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d32be823646f4a43acead3477238067d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Infer 关键字用于条件中的类型推导。</p>
<p>Typescript 官网也拿 <code>ReturnType</code> 这一经典例子说明它的作用：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> ReturnType<T> = T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>[]) => infer R ? R : <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>理解为：如果 <code>T</code> 继承了 <code>extends (...args: any[]) => any</code> 类型，则返回类型 <code>R</code>，否则返回 <code>any</code>。其中 <code>R</code> 是什么呢？<code>R</code> 被定义在 <code>extends (...args: any[]) => infer R</code> 中，即 R 是从传入参数类型中推导出来的。</p>
<h2 data-id="heading-0">精读</h2>
<p>我们可以从两个视角来理解 <code>infer</code>，分别是需求角度与设计角度。</p>
<h3 data-id="heading-1">需求角度理解 infer</h3>
<p>实现 <code>infer</code> 这个关键字一定是背后存在需求，这个需求是普通 Typescript 能力无法满足的。</p>
<p>设想这样一个场景：实现一个函数，接收一个数组，返回第一项。</p>
<p>我们无法用泛型来描述这种类型推导，因为泛型类型是一个整体，而我们想要返回的是入参其中某一项，我们并不能通过类似 <code>T[0]</code> 的写法拿到第一项类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xxx</span><<span class="hljs-title">T</span>>(<span class="hljs-params">...args: T[]</span>): <span class="hljs-title">T</span>[0]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>而实际上不支持这种写法也是合理的，因为这次是获取第一项类型，如果 <code>T</code> 是一个对象，我们想返回其中 <code>onChange</code> 这个 Key 的返回值类型，就不知道如何书写了。所以此时必须用一种新的语法实现，就是 <code>infer</code>。</p>
<h3 data-id="heading-2">设计角度理解 infer</h3>
<p>从类型推导功能来看，泛型功能非常强大，我们可以用泛型描述调用时才传入的类型，并提前将它描述在类型表达式中：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xxx</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): </span>&#123; result: T &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但我们发现 <code>T</code> 这个泛型太整体化了，我们还不具备从中 Pick 子类型的能力。也就是对于 <code>xxx<&#123;label: string&#125;></code> 这个场景，<code>T = &#123;label: string&#125;</code>，但我们无法将 <code>R</code> 定义为 <code>&#123;label: R&#125;</code> 这个位置，因为泛型是一个不可拆分的整体。</p>
<p>而且实际上为了类型安全，我们也不能允许用户描述任意的类型位置，<strong>万一传入的类型结构不是 <code>&#123;label: xxx&#125;</code> 而是一个回调 <code>() => void</code>，那子类型推导岂不是建立在了错误的环境中。</strong> 所以考虑到想要拿到 <code>&#123;label: infer R&#125;</code>，首先参数必须具备 <code>&#123;label: xxx&#125;</code> 的结构，所以正好可以将 <code>infer</code> 与条件判断 <code>T extends ? A : B</code> 结合起来用，即：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> GetLabelTypeFromObject<T> = T <span class="hljs-keyword">extends</span> ? &#123; <span class="hljs-attr">label</span>: infer R &#125; ? R : <span class="hljs-built_in">never</span>

<span class="hljs-keyword">type</span> Result = GetLabelTypeFromObject<&#123; <span class="hljs-attr">label</span>: <span class="hljs-built_in">string</span> &#125;>;
<span class="hljs-comment">// type Result = string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即如果 <code>T</code> 遵循 <code>&#123; label: any &#125;</code> 这样一个结构，那么我可以将这个结构中任何变量位置替换为 <code>infer xxx</code>，如果传入类型满足这个结构（TS 静态解析环节判断），则可以基于这个结构体继续推导，所以在推导过程中我们就可以使用 <code>infer xxx</code> 推断的变量类型。</p>
<p>回过头来看第一个需求，拿到第一个参数类型就可以用 <code>infer</code> 实现了：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> GetFirstParamType<T> = T <span class="hljs-keyword">extends</span> ? <span class="hljs-function">(<span class="hljs-params">...args: infer R</span>) =></span> <span class="hljs-built_in">any</span> ? R[<span class="hljs-number">0</span>] : <span class="hljs-built_in">never</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以理解为，如果此时 <code>T</code> 满足 <code>(...args: any) => any</code> 这个结构，同时我们用 <code>infer R</code> 表示 <code>R</code> 这个临时变量指代第一个 <code>any</code> 运行时类型，那么整个函数返回的类型就是 <code>R</code>。如果 <code>T</code> 都不满足 <code>(...args: any) => any</code> 这个结构，比如 <code>GetFirstParamType<number></code>，那这种推导根本无从谈起，直接返回 <code>never</code> 类型兜底，当然也可以自定义比如 <code>any</code> 之类的任何类型。</p>
<h2 data-id="heading-3">概述</h2>
<p>我们理解了 <code>infer</code> 含义后，再结合 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flearntypescript.dev%2F09%2Fl2-conditional-infer" target="_blank" rel="nofollow noopener noreferrer" title="https://learntypescript.dev/09/l2-conditional-infer" ref="nofollow noopener noreferrer">conditional infer</a> 这篇文章理解里面的例子，有助于加深记忆。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> ArrayElementType<T> = T <span class="hljs-keyword">extends</span> (infer E)[] ? E : T;
<span class="hljs-comment">// type of item1 is `number`</span>
<span class="hljs-keyword">type</span> item1 = ArrayElementType<<span class="hljs-built_in">number</span>[]>;
<span class="hljs-comment">// type of item1 is `&#123;name: string&#125;`</span>
<span class="hljs-keyword">type</span> item2 = ArrayElementType<&#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> &#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>ArrayElementType</code> 利用了条件推断与 <code>infer</code>，表示了这样一个逻辑：如果 <code>T</code> 类型是一个数组，且我们将数组的每一项定义为 <code>E</code> 类型，那么返回类型就为 <code>E</code>，否则为 <code>T</code> 整体类型本身。</p>
<p>所以对于 <code>item1</code> 是满足结构的，所以返回 <code>number</code>，而 <code>item2</code> 不满足结构，所以返回其类型本身。</p>
<p>特别补充一点，对于下面的例子返回什么呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> item3 = ArrayElementType<[<span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>]>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是 <code>number | string</code>，原因是我们用多个 <code>infer E</code>（<code>(infer E)[]</code> 相当于 <code>[infer E, infer E]...</code> 不就是多个变量指向同一个类型代词 <code>E</code> 嘛）同时接收到了 <code>number</code> 和 <code>string</code>，所以可以理解为 <code>E</code> 时而为 <code>number</code> 时而为 <code>string</code>，所以是或关系，这就是协变。</p>
<p>那如果是函数参数呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Bar<T> = T <span class="hljs-keyword">extends</span> &#123; <span class="hljs-attr">a</span>: <span class="hljs-function">(<span class="hljs-params">x: infer U</span>) =></span> <span class="hljs-built_in">void</span>; b: <span class="hljs-function">(<span class="hljs-params">x: infer U</span>) =></span> <span class="hljs-built_in">void</span> &#125;
  ? U : <span class="hljs-built_in">never</span>
<span class="hljs-keyword">type</span> T21 = Bar<&#123; <span class="hljs-attr">a</span>: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>; b: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span> &#125;>; <span class="hljs-comment">// string & number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现结果是 <code>string & number</code>，也就是逆变。但这个例子也是同一个 <code>U</code> 时而为 <code>string</code> 时而为 <code>number</code> 呀，为什么是且的关系，而不是或呢？</p>
<p>其实协变或逆变与 <code>infer</code> 参数位置有关。在 TypeScript 中，对象、类、数组和函数的返回值类型都是协变关系，而函数的参数类型是逆变关系，所以 <code>infer</code> 位置如果在函数参数上，就会遵循逆变原则。</p>
<blockquote>
<p>逆变与协变：</p>
<ul>
<li>协变(co-variant)：类型收敛。</li>
<li>逆变(contra-variant)：类型发散。</li>
</ul>
</blockquote>
<p>关于逆变与协变更深入的话题可以再开一篇文章了，这里就不细讲了，对于 <code>infer</code> 理解到这里就够啦。</p>
<h2 data-id="heading-4">总结</h2>
<p><code>infer</code> 关键字让我们拥有深入展开泛型的结构，并 Pick 出其中任何位置的类型，并作为临时变量用于最终返回类型的能力。</p>
<p>对于 Typescript 类型编程，最大的问题莫过于希望实现一个效果却不知道用什么语法，<code>infer</code> 作为一个强大的类型推导关键字，势必会在大部分复杂类型推导场景下派上用场，所以在遇到困难时，可以想想是不是能用 <code>infer</code> 解决问题。</p>
<blockquote>
<p>讨论地址是：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly%2Fissues%2F346" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly/issues/346" ref="nofollow noopener noreferrer">精读《Typescript infer 关键字》· Issue #346 · dt-fe/weekly</a></p>
</blockquote>
<p><strong>如果你想参与讨论，请 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly" ref="nofollow noopener noreferrer">点击这里</a>，每周都有新的主题，周末或周一发布。前端精读 - 帮你筛选靠谱的内容。</strong></p>
<blockquote>
<p>关注 <strong>前端精读微信公众号</strong></p>
</blockquote>
<img width="200" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d32be823646f4a43acead3477238067d~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>版权声明：自由转载-非商用-非衍生-保持署名（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-nd%2F3.0%2Fdeed.zh" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh" ref="nofollow noopener noreferrer">创意共享 3.0 许可证</a>）</p>
</blockquote></div>  
</div>
            