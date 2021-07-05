
---
title: '关于fp-ts的使用体验以及简要介绍（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7103'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 21:50:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=7103'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>有谁能够在见识过函数式编程的优雅之后还不心动的呢？</p>
<p>对我来说，函数式编程是一个可望而不可及的梦想。它很美好，但是却有点超脱现实。如果说，全然开始使用 Haskell 等函数式编程语言是疯狂，那么从这个编程范式凝聚的智慧中学习一些有用的思想应用于日常的开发那就非常地 make sense。fp-ts 就给我了我们这样一个机会。虽然它使用起来远没有直接使用 Haskell 优雅和完美，但却也是在函数式编程和命令式编程之间取了一个比较好的折中。</p>
<p>fp-ts 中的很多概念，比如 typeclass、instance 等都是取自 Haskell，这对于没有使用过 Haskell 的人来说可能不是非常友好。因此本文将根据自己的使用感受和个人的理解介绍一下 fp-ts 提供的一些我有使用过的一些 modules，希望对 fp-ts 有兴趣的人有帮助。当然，由于本人的经验和能力有限，文中难免存在错误和疏漏。希望可以得到大家的指正，也欢迎交流和讨论。</p>
<h2 data-id="heading-0">预备知识</h2>
<p>在开始正式之前有一些准备知识需要了解。</p>
<h3 data-id="heading-1">type</h3>
<p>在学 C 语言的第一节上我们就会认识到很多的类型，比如<code>int</code>、<code>char</code>等。虽然 JavaScript 是弱类型的语言，我们也不需要在申明变量时指定变量的类型，但是 JavaScript 值同样都是有类型的。比如<code>"abc"</code>的类型是 string，而<code>1</code>的类型是 number。TypeScript 更是在这门语言的基础上增加了静态的类型系统。在 TypeScript 中，我们可以使用 type annotations 来描述变量或者参数的类型。同时，也赋予了我们通过 union type 等描述更复杂类型的能力。</p>
<p>同属于一种类型的值可以组成一个集合，这个集合包含了这种类型的所有可能值。因此我们可以用"is a member of"来描述值和类型之间的关系。比如<code>true</code> is a member of type <code>boolean</code>。</p>
<h3 data-id="heading-2">type constructor</h3>
<p>顾名思义，type constructor是用来创建类型的。大家所熟悉的<code>Array</code>就是一个 type constructor。<code>Array</code>本身不能直接作为某个值的类型使用，它必须接受另一个 type：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> x: <span class="hljs-built_in">Array</span> = []; <span class="hljs-comment">// 错误 Generic type 'Array<T>' requires 1 type argument</span>

<span class="hljs-keyword">const</span> y: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">string</span>> = []; <span class="hljs-comment">// 正确</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在 TypeScript 中，type constructor 是用 generic type 模拟的</p>
</blockquote>
<p><code>Array</code>虽然也是类型，但是它和 number、string 这些 type 之间却有着非常明显的区别。因此我们必须引入一个概念来区别这些类型。正如值具有类型，类型本身也具有类型，也就是类型的类型，被称为 kind。number 等可以作为值的类型使用的类型被称为 concrete type。它们的 kind 可以使用<code>*</code>表示。而 Array 的 kind 是<code>* -> *</code>，也就是说必须提供另一个 concrete type，才能得到一个可以作为值的类型使用的 concrete type。这样的类型被称为 higher-kinded type（以后缩写为 HKT）。当然，也存在需要接受更多类型的 HKT，比如 kind 为<code>* -> * -> *</code>的需要接受两个参数的 HKT。<code>* -> * -> *</code>这个表示也是在暗示着我们，当我们只提供一个类型时，我们将得到一个 kind 为<code>* -> *</code>的 HKT。只是，这一点无法使用 TypeScript 的 generic type 来模拟，因为 generic type 要求我们必须同时提供所需要的类型参数。</p>
<h3 data-id="heading-3">typeclass</h3>
<p>观察 Haskell 中函数 show 的定义<code>show :: Show a => a -> String</code>，<code>=></code> 之前的内容是用来表达对类型变量的限制的（constraints on type variables）。<code>Show a</code>的含义是<code>a</code>类型必须满足<code>Show</code> typeclass。我们可以把 typeclass 想象称为一个个社团，比如有<code>Eq</code>社、<code>Show</code>社，而各种 type 就是社员。某 type 如果想要成为某社团的一员，那它必须要满足这个社团的入社要求。例如，<code>Eq</code>社要求入社的 type 需要支持判等的操作，也就是必须实现一个<code>equals</code>函数，这个函数接受任意两个属于 type 的值<code>a</code>和<code>b</code>，输出一个布尔值。在 Haskell 中我们可以使用 instance declaration，并提供 typeclass 所定义的成员的实现，来为某 type 提供入团证明。而在 fp-ts 中，typeclass 是使用 interface 模拟的。</p>
<p>由此看来，typeclass 的功能类似于接口，用于描述某些类型具备某些行为特性或者支持某种操作。</p>
<h2 data-id="heading-4">Eq</h2>
<p>既然上文已经提到了<code>Eq</code>这个typeclass，我们就先来看<code>Eq</code>能为我们带来什么以及如何使用。<code>Eq</code>表示能够判等的类型。它在 fp-ts 中的定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Eq<A> &#123;
  <span class="hljs-keyword">readonly</span> equals: <span class="hljs-function">(<span class="hljs-params">x: A, y: A</span>) =></span> <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如我们有类型<code>Point</code>定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们认为<code>x</code>和<code>y</code>都相等的点是相等的，因此写出<code>equals</code>的实现如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> equals = <span class="hljs-function">(<span class="hljs-params">a: Point, b: Point</span>) =></span> a.x === b.x && a.y === b.y;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也就为<code>Point</code>类型定义了一个 <code>Eq</code> 的 instance：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> eqPoint: Eq<Point> = &#123;
  equals
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么<code>Eq</code>能为我们带来什么呢。来看 fp-ts 的 Array 模块提供的一个<code>elem</code>函数的定义：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> elem: <A><span class="hljs-function">(<span class="hljs-params">
  E: Eq<A>
</span>) =></span> &#123;
  (a: A): <span class="hljs-function">(<span class="hljs-params"><span class="hljs-keyword">as</span>: <span class="hljs-built_in">Array</span><A></span>) =></span> <span class="hljs-built_in">boolean</span>
  (a: A, <span class="hljs-attr">as</span>: <span class="hljs-built_in">Array</span><A>): <span class="hljs-built_in">boolean</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数要求一个<code>Eq<A></code>类型的参数，也就是说必须为类型<code>A</code>定义了<code>Eq</code>的 instance。而我们的<code>Point</code>就满足了这个条件。于是，我们就可以使用<code>elem</code>函数判断某个点是否在类型为<code>Array<Point></code>的数组中存在：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> points: <span class="hljs-built_in">Array</span><Point> = [
  &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span> &#125;,
  &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span> &#125;,
  &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">4</span> &#125;,
];

elem(eqPoint)(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span> &#125;)(points) <span class="hljs-comment">// true</span>
elem(eqPoint)(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span> &#125;)(points) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fp-ts 已经为一些类型，比如number、string等提供了<code>Eq</code>的 instance。我们在创建自己的instance时，也可以选择利用这些已有的instance：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Eq <span class="hljs-keyword">as</span> eqNumber &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"fp-ts/number"</span>;
<span class="hljs-keyword">import</span> &#123; Eq, struct &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"fp-ts/Eq"</span>;

<span class="hljs-keyword">const</span> eqPoint: Eq<Point> = struct(&#123;
  <span class="hljs-attr">x</span>: eqNumber,
  <span class="hljs-attr">y</span>: eqNumber
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Ord</h2>
<p>Ord 表示支持比较操作的类型，于是在 Eq 的基础上又增加了新的要求：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Ordering = -<span class="hljs-number">1</span> | <span class="hljs-number">0</span> | <span class="hljs-number">1</span>

<span class="hljs-keyword">interface</span> Ord<A> <span class="hljs-keyword">extends</span> Eq<A> &#123;
  <span class="hljs-keyword">readonly</span> compare: <span class="hljs-function">(<span class="hljs-params">first: A, second: A</span>) =></span> Ordering
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说要先创建 Ord 的 instance，我们必须先创建 Eq 的 instance。 而比较的能力又为我们带来了什么呢？fp-ts/Array 提供了一个用于排序的函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> sort: <B><span class="hljs-function">(<span class="hljs-params">O: Ord<B></span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">A</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">B</span>></span>(as: A[]) => A[]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>假如我们有类型定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们希望按照年龄大小对用户进行排序。为了使用 sort，我们需要为 User 类型提供一个 Ord 的 instance：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> equals = <span class="hljs-function">(<span class="hljs-params">a: User, b: User</span>) =></span> a.age === b.age
<span class="hljs-keyword">const</span> compare = <span class="hljs-function">(<span class="hljs-params">a: User, b: User</span>) =></span> equals(a, b) ? <span class="hljs-number">0</span> : a.age > b.age ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>

<span class="hljs-keyword">const</span> ordUser: Ord<User> = &#123;
  <span class="hljs-attr">equals</span>: equals,
  <span class="hljs-attr">compare</span>: compare 
&#125;

<span class="hljs-keyword">const</span> users = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Tomas"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">25</span>
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Ammy"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">21</span>
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Kat"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">23</span>
  &#125;
]

sort(ordUser)(users) <span class="hljs-comment">// [&#123;"name":"Ammy","age":21&#125;,&#123;"name":"Kat","age":23&#125;,&#123;"name":"Tomas","age":25&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，fp-ts 也为 number 类型提供了 Ord 的 instance。我们也可以利用已有的 instance 来简化为 User 创建 instance 的过程：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> ordUser = contramap<<span class="hljs-built_in">number</span>, User>(<span class="hljs-function"><span class="hljs-params">u</span> =></span> u.age)(eqNumber)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这两个例子，我们了解了 typeclass 以及 instance 的作用和使用。接下来的文章，我们正式开始了解一些 fp-ts 提供的类型。</p></div>  
</div>
            