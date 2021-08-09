
---
title: 'Ts高手篇：22个示例深入讲解Ts最晦涩难懂的高级类型工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ceedd42d490435688bf9c236a4f19ad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 08:51:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ceedd42d490435688bf9c236a4f19ad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Hello大家，我是愣锤。随着Typescript不可阻挡的趋势，相信小伙伴们或多或少的使用过Ts开发了。而Ts的使用除了基本的类型定义外，对于Ts的泛型、内置高级类型、自定义高级类型工具等会相对陌生。本文将会通过22个类型工具例子，深入讲解Ts类型工具原理和编程技巧。不扯闲篇，全程干货，内容非常多，想提升Ts功力的小伙伴请耐心读下去。相信小伙伴们在读完此文后，能够对这块有更深入的理解。下面，我们开始吧～</p>
<p>本文基本分为三部分：</p>
<ul>
<li>第一部分讲解一些基本的关键词的特性（比如索引查询、索引访问、映射、extends等），但是该部分更多的讲解小伙伴们不清晰的一些特性，而基本功能则不再赘述。更多的关键词及技巧将包含在后续的例子演示中再具体讲述；</li>
<li>第二部分讲解Ts内置的类型工具以及实现原理，比如Pick、Omit等；第三部分讲解自定义类型；</li>
<li>第三部分讲解自定义的工具类型，该部分也是最难的部分，将通过一些复杂的类型工具示例进行逐步剖析，对于其中的晦涩的地方以及涉及的知识点逐步讲解。此部分也会包含大量Ts类型工具的编程技巧，也希望通过此部分的讲解，小伙伴的Ts功底可以进一步提升！</li>
</ul>
<h2 data-id="heading-0">第一部分 前置内容</h2>
<ul>
<li><code>keyof</code> 索引查询</li>
</ul>
<p>对应任何类型<code>T</code>,<code>keyof T</code>的结果为该类型上所有共有属性key的联合：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Eg1 &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-keyword">readonly</span> age: <span class="hljs-built_in">number</span>,
&#125;
<span class="hljs-comment">// T1的类型实则是name | age</span>
<span class="hljs-keyword">type</span> T1 = keyof Eg1

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Eg2</span> </span>&#123;
  <span class="hljs-keyword">private</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">readonly</span> age: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">protected</span> home: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-comment">// T2实则被约束为 age</span>
<span class="hljs-comment">// 而name和home不是公有属性，所以不能被keyof获取到</span>
<span class="hljs-keyword">type</span> T2 = keyof Eg2
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>T[K]</code> 索引访问</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Eg1 &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-keyword">readonly</span> age: <span class="hljs-built_in">number</span>,
&#125;
<span class="hljs-comment">// string</span>
<span class="hljs-keyword">type</span> V1 = Eg1[<span class="hljs-string">'name'</span>]
<span class="hljs-comment">// string | number</span>
<span class="hljs-keyword">type</span> V2 = Eg1[<span class="hljs-string">'name'</span> | <span class="hljs-string">'age'</span>]
<span class="hljs-comment">// any</span>
<span class="hljs-keyword">type</span> V2 = Eg1[<span class="hljs-string">'name'</span> | <span class="hljs-string">'age2222'</span>]
<span class="hljs-comment">// string | number</span>
<span class="hljs-keyword">type</span> V3 = Eg1[keyof Eg1]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>T[keyof T]</code>的方式，可以获取到<code>T</code>所有<code>key</code>的类型组成的联合类型；
<code>T[keyof K]</code>的方式，获取到的是<code>T</code>中的<code>key</code>且同时存在于<code>K</code>时的类型组成的联合类型；
注意：如果<code>[]</code>中的key有不存在T中的，则是any；因为ts也不知道该key最终是什么类型，所以是any；且也会报错；</p>
<ul>
<li><code>&</code> 交叉类型注意点</li>
</ul>
<p>交叉类型取的多个类型的并集，但是如果相同<code>key</code>但是类型不同，则该<code>key</code>为<code>never</code>。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Eg1 &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
&#125;

<span class="hljs-keyword">interface</span> Eg2 &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">string</span>,
&#125;

<span class="hljs-comment">/**
 * T的类型为 &#123;name: string; age: number; age: never&#125;
 * 注意，age因为Eg1和Eg2中的类型不一致，所以交叉后age的类型是never
 */</span>
<span class="hljs-keyword">type</span> T = Eg1 & Eg2
<span class="hljs-comment">// 可通过如下示例验证</span>
<span class="hljs-keyword">const</span> val: T = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">color</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">age</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>()
  &#125;)(),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">extends关键词特性（重点）</h3>
<ul>
<li>用于接口，表示继承</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> T1 &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
&#125;

<span class="hljs-keyword">interface</span> T2 &#123;
  <span class="hljs-attr">sex</span>: <span class="hljs-built_in">number</span>,
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * T3 = &#123;name: string, sex: number, age: number&#125;
 */</span>
<span class="hljs-keyword">interface</span> T3 <span class="hljs-keyword">extends</span> T1, T2 &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，接口支持多重继承，语法为逗号隔开。如果是type实现继承，则可以使用交叉类型<code>type A = B & C & D</code>。</p>
<ul>
<li>表示条件类型，可用于条件判断</li>
</ul>
<p>表示条件判断，如果前面的条件满足，则返回问号后的第一个参数，否则第二个。类似于js的三元运算。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type A1 = 1
 */</span>
<span class="hljs-keyword">type</span> A1 = <span class="hljs-string">'x'</span> <span class="hljs-keyword">extends</span> <span class="hljs-string">'x'</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type A2 = 2
 */</span>
<span class="hljs-keyword">type</span> A2 = <span class="hljs-string">'x'</span> | <span class="hljs-string">'y'</span> <span class="hljs-keyword">extends</span> <span class="hljs-string">'x'</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type A3 = 1 | 2
 */</span>
<span class="hljs-keyword">type</span> P<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-string">'x'</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="hljs-keyword">type</span> A3 = P<<span class="hljs-string">'x'</span> | <span class="hljs-string">'y'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提问：为什么<code>A2</code>和<code>A3</code>的值不一样？</p>
<ul>
<li>如果用于简单的条件判断，则是直接判断前面的类型是否可分配给后面的类型</li>
<li>若<code>extends</code>前面的类型是泛型，且泛型传入的是联合类型时，则会依次判断该联合类型的所有子类型是否可分配给extends后面的类型（是一个分发的过程）。</li>
</ul>
<p><strong>总结，就是<code>extends</code>前面的参数为联合类型时则会分解（依次遍历所有的子类型进行条件判断）联合类型进行判断。然后将最终的结果组成新的联合类型。</strong></p>
<ul>
<li>阻止extends关键词对于联合类型的分发特性</li>
</ul>
<p>如果不想被分解（分发），做法也很简单，可以通过简单的元组类型包裹以下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> P<T> = [T] <span class="hljs-keyword">extends</span> [<span class="hljs-string">'x'</span>] ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="hljs-comment">/**
 * type A4 = 2;
 */</span>
<span class="hljs-keyword">type</span> A4 = P<<span class="hljs-string">'x'</span> | <span class="hljs-string">'y'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Fconditional-types.html%23distributive-conditional-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#distributive-conditional-types" ref="nofollow noopener noreferrer">条件类型的分布式特性文档</a></p>
<h3 data-id="heading-2">类型兼容性</h3>
<blockquote>
<p>集合论中，如果一个集合的所有元素在集合B中都存在，则A是B的子集；</p>
<p>类型系统中，如果一个类型的属性更具体，则该类型是子类型。（因为属性更少则说明该类型约束的更宽泛，是父类型）</p>
</blockquote>
<p><strong>因此，我们可以得出基本的结论：子类型比父类型更加具体,父类型比子类型更宽泛。</strong> 下面我们也将基于类型的可复制性（可分配性）、协变、逆变、双向协变等进行进一步的讲解。</p>
<ul>
<li>可赋值性</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Animal &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> Dog <span class="hljs-keyword">extends</span> Animal &#123;
  <span class="hljs-keyword">break</span>(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">let</span> a: Animal;
<span class="hljs-keyword">let</span> b: Dog;

<span class="hljs-comment">// 可以赋值，子类型更佳具体，可以赋值给更佳宽泛的父类型</span>
a = b;
<span class="hljs-comment">// 反过来不行</span>
b = a;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可赋值性在联合类型中的特性</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> A = <span class="hljs-number">1</span> | <span class="hljs-number">2</span> | <span class="hljs-number">3</span>;
<span class="hljs-keyword">type</span> B = <span class="hljs-number">2</span> | <span class="hljs-number">3</span>;
<span class="hljs-keyword">let</span> a: A;
<span class="hljs-keyword">let</span> b: B;

<span class="hljs-comment">// 不可赋值</span>
b = a;
<span class="hljs-comment">// 可以赋值</span>
a = b;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是<code>A</code>的类型更多，<code>A</code>就是子类型呢？恰恰相反，<code>A</code>此处类型更多但是其表达的类型更宽泛，所以<code>A</code>是父类型，<code>B</code>是子类型。</p>
<p>因此<code>b = a</code>不成立（父类型不能赋值给子类型），而<code>a = b</code>成立（子类型可以赋值给父类型）。</p>
<ul>
<li>协变</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Animal &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> Dog <span class="hljs-keyword">extends</span> Animal &#123;
  <span class="hljs-keyword">break</span>(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">let</span> Eg1: Animal;
<span class="hljs-keyword">let</span> Eg2: Dog;
<span class="hljs-comment">// 兼容，可以赋值</span>
Eg1 = Eg2;

<span class="hljs-keyword">let</span> Eg3: <span class="hljs-built_in">Array</span><Animal>
<span class="hljs-keyword">let</span> Eg4: <span class="hljs-built_in">Array</span><Dog>
<span class="hljs-comment">// 兼容，可以赋值</span>
Eg3 = Eg4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>Eg3</code>和<code>Eg4</code>来看，在<code>Animal</code>和<code>Dog</code>在变成数组后，<code>Array<Dog></code>依旧可以赋值给<code>Array<Animal></code>，因此对于<code>type MakeArray = Array<any></code>来说就是协变的。</p>
<p>最后引用维基百科中的定义：</p>
<blockquote>
<p>协变与逆变(Covariance and contravariance )是在计算机科学中，描述具有父/子型别关系的多个型别通过型别构造器、构造出的多个复杂型别之间是否有父/子型别关系的用语。</p>
</blockquote>
<p>简单说就是，具有父子关系的多个类型，在通过某种构造关系构造成的新的类型，如果还具有父子关系则是协变的，而关系逆转了（子变父，父变子）就是逆变的。可能听起来有些抽象，下面我们将用更具体的例子进行演示说明：</p>
<ul>
<li>逆变</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Animal &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> Dog <span class="hljs-keyword">extends</span> Animal &#123;
  <span class="hljs-keyword">break</span>(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-keyword">type</span> AnimalFn = <span class="hljs-function">(<span class="hljs-params">arg: Animal</span>) =></span> <span class="hljs-built_in">void</span>
<span class="hljs-keyword">type</span> DogFn = <span class="hljs-function">(<span class="hljs-params">arg: Dog</span>) =></span> <span class="hljs-built_in">void</span>

<span class="hljs-keyword">let</span> Eg1: AnimalFn;
<span class="hljs-keyword">let</span> Eg2: DogFn;
<span class="hljs-comment">// 不再可以赋值了，</span>
<span class="hljs-comment">// AnimalFn = DogFn不可以赋值了, Animal = Dog是可以的</span>
Eg1 = Eg2;
<span class="hljs-comment">// 反过来可以</span>
Eg2 = Eg1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>理论上，<code>Animal = Dog</code>是类型安全的，那么<code>AnimalFn = DogFn</code>也应该类型安全才对，为什么Ts认为不安全呢？看下面的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> animal: AnimalFn = <span class="hljs-function">(<span class="hljs-params">arg: Animal</span>) =></span> &#123;&#125;
<span class="hljs-keyword">let</span> dog: DogFn = <span class="hljs-function">(<span class="hljs-params">arg: Dog</span>) =></span> &#123;
  arg.break();
&#125;

<span class="hljs-comment">// 假设类型安全可以赋值</span>
animal = dog;
<span class="hljs-comment">// 那么animal在调用时约束的参数，缺少dog所需的参数，此时会导致错误</span>
animal(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'cat'</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个例子看到，如果dog函数赋值给animal函数，那么animal函数在调用时，约束的是参数必须要为Animal类型（而不是Dog），但是animal实际为dog的调用，此时就会出现错误。</p>
<p>因此，<code>Animal</code>和<code>Dog</code>在进行<code>type Fn<T> = (arg: T) => void</code>构造器构造后，父子关系逆转了，此时成为“逆变”。</p>
<ul>
<li>双向协变</li>
</ul>
<p>Ts在函数参数的比较中实际上默认采取的策略是双向协变：只有当源函数参数能够赋值给目标函数或者反过来时才能赋值成功。</p>
<p>这是不稳定的，因为调用者可能传入了一个具有更精确类型信息的函数，但是调用这个传入的函数的时候却使用了不是那么精确的类型信息（典型的就是上述的逆变）。 但是实际上，这极少会发生错误，并且能够实现很多JavaScript里的常见模式：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// lib.dom.d.ts中EventListener的接口定义</span>
<span class="hljs-keyword">interface</span> EventListener &#123;
  (evt: Event): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-comment">// 简化后的Event</span>
<span class="hljs-keyword">interface</span> Event &#123;
  <span class="hljs-keyword">readonly</span> target: EventTarget | <span class="hljs-literal">null</span>;
  preventDefault(): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-comment">// 简化合并后的MouseEvent</span>
<span class="hljs-keyword">interface</span> MouseEvent <span class="hljs-keyword">extends</span> Event &#123;
  <span class="hljs-keyword">readonly</span> x: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">readonly</span> y: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-comment">// 简化后的Window接口</span>
<span class="hljs-keyword">interface</span> Window &#123;
  <span class="hljs-comment">// 简化后的addEventListener</span>
  addEventListener(<span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">listener</span>: EventListener)
&#125;

<span class="hljs-comment">// 日常使用</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">(<span class="hljs-params">e: Event</span>) =></span> &#123;&#125;);
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function">(<span class="hljs-params">e: MouseEvent</span>) =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>Window</code>的<code>listener</code>函数要求参数是<code>Event</code>，但是日常使用时更多时候传入的是<code>Event</code>子类型。但是这里可以正常使用，正是其默认行为是双向协变的原因。可以通过<code>tsconfig.js</code>中修改<code>strictFunctionType</code>属性来严格控制协变和逆变。</p>
<p><strong>敲重点！！！敲重点！！！敲重点！！！</strong></p>
<p><code>infer</code>关键词的功能暂时先不做太详细的说明了，主要是用于<code>extends</code>的条件类型中让Ts自己推到类型，具体的可以查阅官网。但是关于<code>infer</code>的一些容易让人忽略但是非常重要的特性，这里必须要提及一下：</p>
<ul>
<li><code>infer</code>推导的名称相同并且都处于逆变的位置，则推导的结果将会是交叉类型。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Bar<T> = T <span class="hljs-keyword">extends</span> &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-function">(<span class="hljs-params">x: infer U</span>) =></span> <span class="hljs-built_in">void</span>;
  b: <span class="hljs-function">(<span class="hljs-params">x: infer U</span>) =></span> <span class="hljs-built_in">void</span>;
&#125; ? U : <span class="hljs-built_in">never</span>;

<span class="hljs-comment">// type T1 = string</span>
<span class="hljs-keyword">type</span> T1 = Bar<&#123; <span class="hljs-attr">a</span>: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>; b: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span> &#125;>;

<span class="hljs-comment">// type T2 = never</span>
<span class="hljs-keyword">type</span> T2 = Bar<&#123; <span class="hljs-attr">a</span>: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>; b: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span> &#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>infer</code>推导的名称相同并且都处于协变的位置，则推导的结果将会是交叉类型。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Foo<T> = T <span class="hljs-keyword">extends</span> &#123;
  <span class="hljs-attr">a</span>: infer U;
  b: infer U;
&#125; ? U : <span class="hljs-built_in">never</span>;

<span class="hljs-comment">// type T1 = string</span>
<span class="hljs-keyword">type</span> T1 = Foo<&#123; <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>; b: <span class="hljs-built_in">string</span> &#125;>;

<span class="hljs-comment">// type T2 = string | number</span>
<span class="hljs-keyword">type</span> T2 = Foo<&#123; <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>; b: <span class="hljs-built_in">number</span> &#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ceedd42d490435688bf9c236a4f19ad~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_8357a6f0-aa88-4faf-b21e-f1baa6bc790e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">第二部分 Ts内置类型工具原理解析</h2>
<h3 data-id="heading-4">Partial实现原理解析</h3>
<p><code>Partial<T></code>将<code>T</code>的所有属性变成可选的。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现就是通过映射类型遍历T上所有的属性，
 * 然后将每个属性设置为可选属性
 */</span>
<span class="hljs-keyword">type</span> Partial<T> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]?: T[P];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>[P in keyof T]</code>通过映射类型，遍历<code>T</code>上的所有属性</li>
<li><code>?:</code>设置为属性为可选的</li>
<li><code>T[P]</code>设置类型为原来的类型</li>
</ul>
<p>扩展一下，将制定的<code>key</code>变成可选类型:</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 主要通过K extends keyof T约束K必须为keyof T的子类型
 * keyof T得到的是T的所有key组成的联合类型
 */</span>
<span class="hljs-keyword">type</span> PartialOptional<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
  [P <span class="hljs-keyword">in</span> K]?: T[P];
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 *     type Eg1 = &#123; key1?: string; key2?: number &#125;
 */</span>
<span class="hljs-keyword">type</span> Eg1 = PartialOptional<&#123;
  <span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">key2</span>: <span class="hljs-built_in">number</span>,
  <span class="hljs-attr">key3</span>: <span class="hljs-string">''</span>
&#125;, <span class="hljs-string">'key1'</span> | <span class="hljs-string">'key2'</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Readonly原理解析</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 主要实现是通过映射遍历所有key，
 * 然后给每个key增加一个readonly修饰符
 */</span>
<span class="hljs-keyword">type</span> Readonly<T> = &#123;
  <span class="hljs-keyword">readonly</span> [P <span class="hljs-keyword">in</span> keyof T]: T[P]
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = &#123;
 *   readonly key1: string;
 *   readonly key2: number;
 * &#125;
 */</span>
<span class="hljs-keyword">type</span> Eg = Readonly<&#123;
  <span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">key2</span>: <span class="hljs-built_in">number</span>,
&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Pick</h3>
<p>挑选一组属性并组成一个新的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Pick<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
    [P <span class="hljs-keyword">in</span> K]: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本和上述同样的知识点，就不再赘述了。</p>
<h3 data-id="heading-7">Record</h3>
<p>构造一个<code>type</code>，<code>key</code>为联合类型中的每个子类型，类型为<code>T</code>。文字不好理解，先看例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg1 = &#123;
 *   a: &#123; key1: string; &#125;;
 *   b: &#123; key1: string; &#125;;
 * &#125;
 * <span class="hljs-doctag">@desc </span>就是遍历第一个参数'a' | 'b'的每个子类型，然后将值设置为第二参数
 */</span>
<span class="hljs-keyword">type</span> Eg1 = Record<<span class="hljs-string">'a'</span> | <span class="hljs-string">'b'</span>, &#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Record具体实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现就是遍历K，将值设置为T
 */</span>
<span class="hljs-keyword">type</span> Record<K <span class="hljs-keyword">extends</span> keyof <span class="hljs-built_in">any</span>, T> = &#123;
  [P <span class="hljs-keyword">in</span> K]: T
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg2 = &#123;a: B, b: B&#125;
 */</span>
<span class="hljs-keyword">interface</span> A &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>,
&#125;
<span class="hljs-keyword">interface</span> B &#123;
  <span class="hljs-attr">key1</span>: <span class="hljs-built_in">number</span>,
  <span class="hljs-attr">key2</span>: <span class="hljs-built_in">string</span>,
&#125;
<span class="hljs-keyword">type</span> Eg2 = Record<keyof A, B>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>值得注意的是<code>keyof any</code>得到的是<code>string | number | symbol</code></li>
<li>原因在于类型key的类型只能为<code>string | number | symbol</code></li>
</ul>
<p><strong>扩展: 同态与非同态。划重点！！！ 划重点！！！ 划重点！！！</strong></p>
<ul>
<li><code>Partial</code>、<code>Readonly</code>和<code>Pick</code>都属于同态的，即其实现需要输入类型T来拷贝属性，因此属性修饰符（例如readonly、?:）都会被拷贝。可从下面例子验证：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = &#123;readonly a?: string&#125;
 */</span>
<span class="hljs-keyword">type</span> Eg = Pick<&#123;<span class="hljs-keyword">readonly</span> a?: <span class="hljs-built_in">string</span>&#125;, <span class="hljs-string">'a'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>Eg</code>的结果可以看到，Pick在拷贝属性时，连带拷贝了<code>readonly</code>和<code>?:</code>的修饰符。</p>
<ul>
<li><code>Record</code>是非同态的，不需要拷贝属性，因此不会拷贝属性修饰符</li>
</ul>
<p>可能到这里就有小伙伴疑惑了，为什么<code>Pick</code>拷贝了属性，而<code>Record</code>没有拷贝？我们来对比一下其实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Pick<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
    [P <span class="hljs-keyword">in</span> K]: T[P];
&#125;;

<span class="hljs-keyword">type</span> Record<K <span class="hljs-keyword">extends</span> keyof <span class="hljs-built_in">any</span>, T> = &#123;
  [P <span class="hljs-keyword">in</span> K]: T
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>Pick</code>的实现中，注意<code>P in K</code>（本质是<code>P in keyof T</code>），T为输入的类型，而<code>keyof T</code>则遍历了输入类型；而<code>Record</code>的实现中，并没有遍历所有输入的类型，K只是约束为<code>keyof any</code>的子类型即可。</p>
<p>最后再类比一下<code>Pick、Partial、readonly</code>这几个类型工具，无一例外，都是使用到了<code>keyof T</code>来辅助拷贝传入类型的属性。</p>
<h3 data-id="heading-8">Exclude原理解析</h3>
<p><code>Exclude<T, U></code>提取存在于<code>T</code>，但不存在于<code>U</code>的类型组成的联合类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 遍历T中的所有子类型，如果该子类型约束于U（存在于U、兼容于U），
 * 则返回never类型，否则返回该子类型
 */</span>
<span class="hljs-keyword">type</span> Exclude<T, U> = T <span class="hljs-keyword">extends</span> U ? <span class="hljs-built_in">never</span> : T;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = 'key1'
 */</span>
<span class="hljs-keyword">type</span> Eg = Exclude<<span class="hljs-string">'key1'</span> | <span class="hljs-string">'key2'</span>, <span class="hljs-string">'key2'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>敲重点！！！</p>
<ul>
<li><code>never</code>表示一个不存在的类型</li>
<li><code>never</code>与其他类型的联合后，是没有<code>never</code>的</li>
</ul>
<pre><code class="copyable">/**
 * @example
 * type Eg2 = string | number
 */
type Eg2 = string | number | never
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此上述<code>Eg</code>其实就等于<code>key1 | never</code>,也就是<code>type Eg = key1</code></p>
<h3 data-id="heading-9">Extract</h3>
<p><code>Extract<T, U></code>提取联合类型T和联合类型U的所有交集。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Extract<T, U> = T <span class="hljs-keyword">extends</span> U ? T : <span class="hljs-built_in">never</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 *  type Eg = 'key1'
 */</span>
<span class="hljs-keyword">type</span> Eg = Extract<<span class="hljs-string">'key1'</span> | <span class="hljs-string">'key2'</span>, <span class="hljs-string">'key1'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Omit原理解析</h3>
<p><code>Omit<T, K></code>从类型<code>T</code>中剔除<code>K</code>中的所有属性。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 利用Pick实现Omit
 */</span>
<span class="hljs-keyword">type</span> Omit = Pick<T, Exclude<keyof T, K>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>换种思路想一下，其实现可以是利用<code>Pick</code>提取我们需要的keys组成的类型</li>
<li>因此也就是 <code>Omit = Pick<T, 我们需要的属性联合></code></li>
<li>而我们需要的属性联合就是，从T的属性联合中排出存在于联合类型K中的</li>
<li>因此也就是<code>Exclude<keyof T, K></code>;</li>
</ul>
<p>如果不利用Pick实现呢?</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 利用映射类型Omit
 */</span>
<span class="hljs-keyword">type</span> Omit2<T, K <span class="hljs-keyword">extends</span> keyof <span class="hljs-built_in">any</span>> = &#123;
  [P <span class="hljs-keyword">in</span> Exclude<keyof T, K>]: T[P]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>其实现类似于Pick的原理实现</li>
<li>区别在于是遍历的我们需要的属性不一样</li>
<li>我们需要的属性和上面的例子一样，就是<code>Exclude<keyof T, K></code></li>
<li>因此，遍历就是<code>[P in Exclude<keyof T, K>]</code></li>
</ul>
<h3 data-id="heading-11">Parameters 和 ReturnType</h3>
<p><strong>Parameters 获取函数的参数类型，将每个参数类型放在一个元组中。</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>具体实现
 */</span>
<span class="hljs-keyword">type</span> Parameters<T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>> = T <span class="hljs-keyword">extends</span> (...args: infer P) => <span class="hljs-built_in">any</span> ? P : <span class="hljs-built_in">never</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = [arg1: string, arg2: number];
 */</span>
<span class="hljs-keyword">type</span> Eg = Parameters<<span class="hljs-function">(<span class="hljs-params">arg1: <span class="hljs-built_in">string</span>, arg2: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>Parameters</code>首先约束参数<code>T</code>必须是个函数类型，所以<code>(...args: any) => any></code>替换成<code>Function</code>也是可以的</li>
<li>具体实现就是，判断<code>T</code>是否是函数类型，如果是则使用<code>inter P</code>让ts自己推导出函数的参数类型，并将推导的结果存到类型<code>P</code>上，否则就返回<code>never</code>；</li>
</ul>
<p><strong>敲重点！！！敲重点！！！敲重点！！！</strong></p>
<ul>
<li><code>inter</code>关键词作用是让Ts自己推导类型，并将推导结果存储在其参数绑定的类型上。Eg:<code>inter P</code> 就是将结果存在类型P上，供使用。</li>
<li><code>inter</code>关键词只能在extends条件类型上使用，不能在其他地方使用。</li>
</ul>
<p><strong>再敲重点！！！再敲重点！！！再敲重点！！！</strong></p>
<ul>
<li>
<p><code>type Eg = [arg1: string, arg2: number]</code>这是一个元组，但是和我们常见的元组<code>type tuple = [string, number]</code>。官网未提到该部分文档说明，其实可以把这个作为类似命名元组，或者具名元组的意思去理解。实质上没有什么特殊的作用，比如无法通过这个具名去取值不行的。但是从语义化的角度，个人觉得多了语义化的表达罢了。</p>
</li>
<li>
<p>定义元祖的可选项，只能是最后的选项</p>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 普通方式
 */</span>
<span class="hljs-keyword">type</span> Tuple1 = [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>?];
<span class="hljs-keyword">const</span> a: Tuple1 = [<span class="hljs-string">'aa'</span>, <span class="hljs-number">11</span>];
<span class="hljs-keyword">const</span> a2: Tuple1 = [<span class="hljs-string">'aa'</span>];

<span class="hljs-comment">/**
 * 具名方式
 */</span>
<span class="hljs-keyword">type</span> Tuple2 = [name: <span class="hljs-built_in">string</span>, age?: <span class="hljs-built_in">number</span>];
<span class="hljs-keyword">const</span> b: Tuple2 = [<span class="hljs-string">'aa'</span>, <span class="hljs-number">11</span>];
<span class="hljs-keyword">const</span> b2: Tuple2 = [<span class="hljs-string">'aa'</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>扩展：<code>infer</code>实现一个推导数组所有元素的类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 约束参数T为数组类型，
 * 判断T是否为数组，如果是数组类型则推导数组元素的类型
 */</span>
<span class="hljs-keyword">type</span> FalttenArray<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span><<span class="hljs-built_in">any</span>>> = T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span><infer P> ? P : <span class="hljs-built_in">never</span>;

<span class="hljs-comment">/**
 * type Eg1 = number | string;
 */</span>
<span class="hljs-keyword">type</span> Eg1 = FalttenArray<[<span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>]>
<span class="hljs-comment">/**
 * type Eg2 = 1 | 'asd';
 */</span>
<span class="hljs-keyword">type</span> Eg2 = FalttenArray<[<span class="hljs-number">1</span>, <span class="hljs-string">'asd'</span>]>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ReturnType 获取函数的返回值类型。</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>ReturnType的实现其实和Parameters的基本一样
 * 无非是使用infer R的位置不一样。
 */</span>
<span class="hljs-keyword">type</span> ReturnType<T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>> = T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => infer R ? R : <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">ConstructorParameters</h3>
<p><code>ConstructorParameters</code>可以获取类的构造函数的参数类型，存在一个元组中。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现还是利用infer进行推导构造函数的参数类型
 */</span>
<span class="hljs-keyword">type</span> ConstructorParameters<T <span class="hljs-keyword">extends</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">new</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>> = T <span class="hljs-keyword">extends</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">new</span> (...args: infer P) => <span class="hljs-built_in">any</span> ? P : <span class="hljs-built_in">never</span>;


<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = string;
 */</span>
<span class="hljs-keyword">interface</span> ErrorConstructor &#123;
  <span class="hljs-keyword">new</span>(message?: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">Error</span>;
  (message?: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">Error</span>;
  <span class="hljs-keyword">readonly</span> prototype: <span class="hljs-built_in">Error</span>;
&#125;
<span class="hljs-keyword">type</span> Eg = ConstructorParameters<ErrorConstructor>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg2 = [name: string, sex?: number];
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>, sex?: <span class="hljs-built_in">number</span></span>)</span> &#123;&#125;
&#125;
<span class="hljs-keyword">type</span> Eg2 = ConstructorParameters<<span class="hljs-keyword">typeof</span> People>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先约束参数<code>T</code>为拥有构造函数的类。注意这里有个<code>abstract</code>修饰符，等下会说明。</li>
<li>实现时，判断<code>T</code>是满足约束的类时，利用<code>infer P</code>自动推导构造函数的参数类型，并最终返回该类型。</li>
</ul>
<p><strong>敲重点！！！敲重点！！！敲重点！！！</strong></p>
<p>那么疑问来了，为什么要对T要约束为<code>abstract</code>抽象类呢？看下面例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 定义一个普通类
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;&#125;
<span class="hljs-comment">/**
 * 定义一个抽象类
 */</span>
<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyAbstractClass</span> </span>&#123;&#125;

<span class="hljs-comment">// 可以赋值</span>
<span class="hljs-keyword">const</span> c1: <span class="hljs-keyword">typeof</span> MyClass = MyClass
<span class="hljs-comment">// 报错，无法将抽象构造函数类型分配给非抽象构造函数类型</span>
<span class="hljs-keyword">const</span> c2: <span class="hljs-keyword">typeof</span> MyClass = MyAbstractClass

<span class="hljs-comment">// 可以赋值</span>
<span class="hljs-keyword">const</span> c3: <span class="hljs-keyword">typeof</span> MyAbstractClass = MyClass
<span class="hljs-comment">// 可以赋值</span>
<span class="hljs-keyword">const</span> c4: <span class="hljs-keyword">typeof</span> MyAbstractClass = MyAbstractClass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此看出，如果将类型定义为抽象类（抽象构造函数），则既可以赋值为抽象类，也可以赋值为普通类；而反之则不行。</p>
<p><strong>再敲重点！！！再敲重点！！！再敲重点！！！</strong></p>
<p>这里继续提问，直接使用类作为类型，和使用<code>typeof 类</code>作为类型，有什么区别呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 定义一个类
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">number</span>;
  age: <span class="hljs-built_in">number</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// p1可以正常赋值</span>
<span class="hljs-keyword">const</span> p1: People = <span class="hljs-keyword">new</span> People();
<span class="hljs-comment">// 等号后面的People报错，类型“typeof People”缺少类型“People”中的以下属性: name, age</span>
<span class="hljs-keyword">const</span> p2: People = People;

<span class="hljs-comment">// p3报错，类型 "People" 中缺少属性 "prototype"，但类型 "typeof People" 中需要该属性</span>
<span class="hljs-keyword">const</span> p3: <span class="hljs-keyword">typeof</span> People = <span class="hljs-keyword">new</span> People();
<span class="hljs-comment">// p4可以正常赋值</span>
<span class="hljs-keyword">const</span> p4: <span class="hljs-keyword">typeof</span> People = People;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论是这样的：</p>
<ul>
<li>当把类直接作为类型时，该类型约束的是该类型必须是类的实例；即该类型获取的是该类上的实例属性和实例方法（也叫原型方法）；</li>
<li>当把typeof 类作为类型时，约束的满足该类的类型；即该类型获取的是该类上的静态属性和方法。</li>
<li></li>
</ul>
<p>最后，只需要对inter的使用换个位置，便可以获取构造函数返回值的类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> InstanceType<T <span class="hljs-keyword">extends</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">new</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>> = T <span class="hljs-keyword">extends</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">new</span> (...args: <span class="hljs-built_in">any</span>) => infer R ? R : <span class="hljs-built_in">any</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">Ts compiler内部实现的类型</h3>
<ul>
<li>Uppercase</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>构造一个将字符串转大写的类型
 * <span class="hljs-doctag">@example</span>
 * type Eg1 = 'ABCD';
 */</span>
<span class="hljs-keyword">type</span> Eg1 = Uppercase<<span class="hljs-string">'abcd'</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Lowercase</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>构造一个将字符串转小大写的类型
 * <span class="hljs-doctag">@example</span>
 * type Eg2 = 'abcd';
 */</span>
<span class="hljs-keyword">type</span> Eg2 = Lowercase<<span class="hljs-string">'ABCD'</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Capitalize</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>构造一个将字符串首字符转大写的类型
 * <span class="hljs-doctag">@example</span>
 * type Eg3 = 'abcd';
 */</span>
<span class="hljs-keyword">type</span> Eg3 = Capitalize<<span class="hljs-string">'Abcd'</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Uncapitalize</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>构造一个将字符串首字符转小写的类型
 * <span class="hljs-doctag">@example</span>
 * type Eg3 = 'ABCD';
 */</span>
<span class="hljs-keyword">type</span> Eg3 = Uncapitalize<<span class="hljs-string">'aBCD'</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些类型工具，在<code>lib.es5.d.ts</code>文件中是看不到具体定义的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Uppercase<S <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = intrinsic;
<span class="hljs-keyword">type</span> Lowercase<S <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = intrinsic;
<span class="hljs-keyword">type</span> Capitalize<S <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = intrinsic;
<span class="hljs-keyword">type</span> Uncapitalize<S <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = intrinsic;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29417b98f5bd4870bf65396992f913d8~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_1900dfc9-3c22-4af2-9523-6860bcf03e03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">第三部分 自定义Ts高级类型工具及类型编程技巧</h2>
<h3 data-id="heading-15">SymmetricDifference</h3>
<p><code>SymmetricDifference<T, U></code>获取没有同时存在于T和U内的类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现
 */</span>
<span class="hljs-keyword">type</span> SymmetricDifference<A, B> = SetDifference<A | B, A & B>;

<span class="hljs-comment">/**
 * SetDifference的实现和Exclude一样
 */</span>
<span class="hljs-keyword">type</span> SymmetricDifference<T, U> = Exclude<T | U, T & U>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = '1' | '4';
 */</span>
<span class="hljs-keyword">type</span> Eg = SymmetricDifference<<span class="hljs-string">'1'</span> | <span class="hljs-string">'2'</span> | <span class="hljs-string">'3'</span>, <span class="hljs-string">'2'</span> | <span class="hljs-string">'3'</span> | <span class="hljs-string">'4'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其核心实现利用了3点：分发式联合类型、交叉类型和Exclude。</p>
<ul>
<li>首先利用Exclude从获取存在于第一个参数但是不存在于第二个参数的类型</li>
<li><code>Exclude</code>第2个参数是<code>T & U</code>获取的是所有类型的交叉类型</li>
<li><code>Exclude</code>第一个参数则是<code>T | U</code>，这是利用在联合类型在extends中的分发特性，可以理解为<code>Exclude<T, T & U> | Exclude<U, T & U></code>;</li>
</ul>
<p>总结一下就是，提取存在于<code>T</code>但不存在于<code>T & U</code>的类型，然后再提取存在于<code>U</code>但不存在于<code>T & U</code>的，最后进行联合。</p>
<h3 data-id="heading-16">FunctionKeys</h3>
<p>获取<code>T</code>中所有类型为函数的<code>key</code>组成的联合类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>NonUndefined判断T是否为undefined
 */</span>
<span class="hljs-keyword">type</span> NonUndefined<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-literal">undefined</span> ? <span class="hljs-built_in">never</span> : T;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>核心实现
 */</span>
<span class="hljs-keyword">type</span> FunctionKeys<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>> = &#123;
  [K <span class="hljs-keyword">in</span> keyof T]: NonUndefined<T[K]> <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Function</span> ? K : <span class="hljs-built_in">never</span>;
&#125;[keyof T];

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = 'key2' | 'key3';
 */</span>
<span class="hljs-keyword">type</span> AType = &#123;
    <span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">key2</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>,
    <span class="hljs-attr">key3</span>: <span class="hljs-built_in">Function</span>,
&#125;;
<span class="hljs-keyword">type</span> Eg = FunctionKeys<AType>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先约束参数T类型为<code>object</code></li>
<li>通过映射类型<code>K in keyof T</code>遍历所有的key，先通过<code>NonUndefined<T[K]></code>过滤<code>T[K]</code>为<code>undefined | null</code>的类型，不符合的返回never</li>
<li>若<code>T[K]</code>为有效类型，则判断是否为<code>Function</code>类型，是的话返回<code>K</code>,否则<code>never</code>；此时可以得到的类型，例如：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 上述的Eg在此时应该是如下类型，伪代码：
 */</span>
<span class="hljs-keyword">type</span> TempType = &#123;
    <span class="hljs-attr">key1</span>: <span class="hljs-built_in">never</span>,
    <span class="hljs-attr">key2</span>: <span class="hljs-string">'key2'</span>,
    <span class="hljs-attr">key3</span>: <span class="hljs-string">'key3'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后经过<code>&#123;省略&#125;[keyof T]</code>索引访问，取到的为值类型的联合类型<code>never | key2 | key3</code>,计算后就是<code>key2 | key3</code>;</li>
</ul>
<p><strong>敲重点！！！敲重点！！！敲重点！！！</strong></p>
<ul>
<li><code>T[]</code>是索引访问操作，可以取到值的类型</li>
<li><code>T['a' | 'b']</code>若<code>[]</code>内参数是联合类型，则也是分发索引的特性，依次取到值的类型进行联合</li>
<li><code>T[keyof T]</code>则是获取<code>T</code>所有值的类型类型；</li>
<li><code>never</code>和其他类型进行联合时，<code>never</code>是不存在的。例如：<code>never | number | string</code>等同于<code>number | string</code></li>
</ul>
<p><strong>再敲重点！！！再敲重点！！！再敲重点！！！</strong></p>
<ul>
<li><code>null</code>和<code>undefined</code>可以赋值给其他类型（开始该类型的严格赋值检测除外）,所以上述实现中需要使用<code>NonUndefined</code>先行判断。</li>
<li><code>NonUndefined</code>中的实现，只判断了<code>T extends undefined</code>，其实也是因为两者可以互相兼容的。所以你换成<code>T extends null</code>或者<code>T extends null | undefined</code>都是可以的。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// A = 1</span>
<span class="hljs-keyword">type</span> A = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">extends</span> <span class="hljs-literal">null</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="hljs-comment">// B = 1</span>
<span class="hljs-keyword">type</span> B = <span class="hljs-literal">null</span> <span class="hljs-keyword">extends</span> <span class="hljs-literal">undefined</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，如果你想写一个获取非函数类型的key组成的联合类型，无非就是<code>K</code>和<code>never</code>的位置不一样罢了。同样，你也可以实现<code>StringKeys</code>、<code>NumberKeys</code>等等。但是记得可以抽象个工厂类型哈：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Primitive =
  | <span class="hljs-built_in">string</span>
  | <span class="hljs-built_in">number</span>
  | bigint
  | <span class="hljs-built_in">boolean</span>
  | symbol
  | <span class="hljs-literal">null</span>
  | <span class="hljs-literal">undefined</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>用于创建获取指定类型工具的类型工厂
 * <span class="hljs-doctag">@param </span>T 待提取的类型
 * <span class="hljs-doctag">@param </span>P 要创建的类型
 * <span class="hljs-doctag">@param </span>IsCheckNon 是否要进行null和undefined检查
 */</span>
<span class="hljs-keyword">type</span> KeysFactory<T, P <span class="hljs-keyword">extends</span> Primitive | <span class="hljs-built_in">Function</span> | <span class="hljs-built_in">object</span>, IsCheckNon <span class="hljs-keyword">extends</span> <span class="hljs-built_in">boolean</span>> = &#123;
  [K <span class="hljs-keyword">in</span> keyof T]: IsCheckNon <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span>
    ? (NonUndefined<T[K]> <span class="hljs-keyword">extends</span> P ? K : <span class="hljs-built_in">never</span>)
    : (T[K] <span class="hljs-keyword">extends</span> P ? K : <span class="hljs-built_in">never</span>);
&#125;[keyof T];

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * 例如上述KeysFactory就可以通过工厂类型进行创建了
 */</span>
<span class="hljs-keyword">type</span> FunctionKeys<T> = KeysFactory<T, <span class="hljs-built_in">Function</span>, <span class="hljs-literal">true</span>>;
<span class="hljs-keyword">type</span> StringKeys<T> = KeysFactory<T, <span class="hljs-built_in">string</span>, <span class="hljs-literal">true</span>>;
<span class="hljs-keyword">type</span> NumberKeys<T> = KeysFactory<T, <span class="hljs-built_in">string</span>, <span class="hljs-literal">true</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">MutableKeys</h3>
<p><code>MutableKeys<T></code>查找<code>T</code>所有可选类型的key组成的联合类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现
 */</span>
<span class="hljs-keyword">type</span> MutableKeys<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]-?: IfEquals<
    &#123; [Q <span class="hljs-keyword">in</span> P]: T[P] &#125;,
    &#123; -<span class="hljs-keyword">readonly</span> [Q <span class="hljs-keyword">in</span> P]: T[P] &#125;,
    P
  >;
&#125;[keyof T];

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@desc </span>一个辅助类型，判断X和Y是否类型相同，
 * <span class="hljs-doctag">@returns </span>是则返回A，否则返回B
 */</span>
<span class="hljs-keyword">type</span> IfEquals<X, Y, A = X, B = <span class="hljs-built_in">never</span>> = (<T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> X ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>) <span class="hljs-keyword">extends</span> (<T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> Y ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>)
  ? A
  : B;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>MutableKeys</code>还是有一定难度的，讲解<code>MutableKeys</code>的实现，我们要分下面几个步骤：</p>
<p><strong>第一步，先理解只读和非只读的一些特性</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 遍历类型T，原封不动的返回，有点类似于拷贝类型的意思
 */</span>
<span class="hljs-keyword">type</span> RType1<T> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]: T[P];
&#125;
<span class="hljs-comment">/**
 * 遍历类型T，将每个key变成非只读
 * 或者理解成去掉只读属性更好理解。
 */</span>
<span class="hljs-keyword">type</span> RType2<T> = &#123;
  -<span class="hljs-keyword">readonly</span>[P <span class="hljs-keyword">in</span> keyof T]: T[P];
&#125;

<span class="hljs-comment">// R0 = &#123; a: string; readonly b: number &#125;</span>
<span class="hljs-keyword">type</span> R0 = RType1<&#123;<span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">readonly</span> b: <span class="hljs-built_in">number</span>&#125;>

<span class="hljs-comment">// R1 = &#123; a: string &#125;</span>
<span class="hljs-keyword">type</span> R1 = RType1<&#123;<span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>&#125;>;
<span class="hljs-comment">// R2 = &#123; a: string &#125;</span>
<span class="hljs-keyword">type</span> R2 = RType2<&#123;<span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>&#125;>;

<span class="hljs-comment">// R3 = &#123; readonly a: string &#125;</span>
<span class="hljs-keyword">type</span> R3 = RType1<&#123;<span class="hljs-keyword">readonly</span> a: <span class="hljs-built_in">string</span>&#125;>;
<span class="hljs-comment">// R4 = &#123; a: string &#125;</span>
<span class="hljs-keyword">type</span> R4 = RType2<&#123;<span class="hljs-keyword">readonly</span> a: <span class="hljs-built_in">string</span>&#125;>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到：<code>RType1</code>和<code>RType2</code>的参数为<strong>非只读</strong>的属性时，<code>R1</code>和<code>R2</code>的结果是一样的；<code>RType1</code>和<code>RType2</code>的参数为<strong>只读</strong>的属性时，得到的结果R3是<strong>只读</strong>的，<code>R4</code>是<strong>非只读</strong>的。所以，这里要敲个重点了：</p>
<ul>
<li><code>[P in Keyof T]</code>是映射类型，而映射是同态的，同态即会拷贝原有的属性修饰符等。可以参考R0的例子。</li>
<li>映射类型上的<code>-readonly</code>表示为<strong>非只读</strong>，或者可以理解为去掉<strong>只读</strong>。对于<strong>只读</strong>属性加上<code>-readonly</code>变成了<strong>非只读</strong>，而对<strong>非只读</strong>属性加上<code>-readonly</code>后还是<strong>非只读</strong>。一种常见的使用方式，比如你想把属性变成都是非只读的，不能前面不加修饰符（虽然不写就表示非只读），但是要考虑到同态拷贝的问题。</li>
</ul>
<p><strong>第二步，解析IfEquals</strong></p>
<p><code>IfEquals</code>用于判断类型<code>X</code>和<code>Y</code>是否相同，相等则返回<code>A</code>，否则返回<code>B</code>。这个函数是比较难的，也别怕啦，下面讲完就妥妥的明白啦~</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> IfEquals<X, Y, A = X, B = <span class="hljs-built_in">never</span>> =
  (<T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> X ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>) <span class="hljs-keyword">extends</span>
  (<T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> Y ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>)
    ? A : B;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先<code>IfEquals<X, Y, A, B></code>的四个参数，<code>X和Y</code>是待比较的两个类型，如果相等则返回<code>A</code>，不相等返回<code>B</code>。</li>
<li><code>IfEquals</code>的基本骨架是<code>type IfEquals<> = (参数1) extends (参数2) ? A : B</code>这样的，就是判断如果参数1的类型能够分配给参数2的类型，则返回<code>A</code>，否则返回<code>B</code>;</li>
<li>参数1和参数2的基本结构是一样的，唯一区别在于X和Y不同。这里看下具体下面的例子：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// A = <T>() => T extends string ? 1 : 2;</span>
<span class="hljs-keyword">type</span> A = <T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="hljs-comment">// B = <T>() => T extends number ? 1 : 2;</span>
<span class="hljs-keyword">type</span> B = <T><span class="hljs-function">() =></span> T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">number</span> ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;

<span class="hljs-comment">// C = 2</span>
<span class="hljs-keyword">type</span> C = A <span class="hljs-keyword">extends</span> B ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很奇怪，为什么能推导出<code>A</code>和<code>B</code>类型是不一样的？告诉你答案：</p>
<ul>
<li>这是利用了Ts编译器的一个特点，就是Ts编译器会认为如果两个类型（比如这里的<code>X</code>和<code>Y</code>）仅被用于约束两个相同的泛型函数则是相同的。这理解起来有些不可思议，或者说在逻辑上这种逻辑并不对（因为可以举出反例），但是Ts开发团队保证了这一特性今后不会变。可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F52443276%2Fhow-to-exclude-getter-only-properties-from-type-in-typescript" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/52443276/how-to-exclude-getter-only-properties-from-type-in-typescript" ref="nofollow noopener noreferrer">这里</a>。</li>
<li>注意，这里也会判断的属性修饰符，例如<code>readonly</code>, <code>可选属性</code>等，看通过下面的例子验证：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * T2比T1多了readonly修饰符
 * T3比T1多了可选修饰符
 * 这里控制单一变量进行验证
 */</span>
<span class="hljs-keyword">type</span> T1 = &#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125;;
<span class="hljs-keyword">type</span> T2 = &#123;<span class="hljs-keyword">readonly</span> key1: <span class="hljs-built_in">string</span>&#125;;
<span class="hljs-keyword">type</span> T3 = &#123;key1?: <span class="hljs-built_in">string</span>&#125;;

<span class="hljs-comment">// A1 = false</span>
<span class="hljs-keyword">type</span> A1 = IfEquals<T1, T2, <span class="hljs-literal">true</span> , <span class="hljs-literal">false</span>>;
<span class="hljs-comment">// A2 = false</span>
<span class="hljs-keyword">type</span> A2 = IfEquals<T1, T3, <span class="hljs-literal">true</span> , <span class="hljs-literal">false</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>IfEquals</code>最后就是借助1和2来辅助判断（语法层面的），还有就是给<code>A</code>的默认值为<code>X</code>，<code>B</code>的默认值为<code>never</code>。</li>
</ul>
<p>最后，如果你是个爱（搞）钻（事）研（情）的小宝宝，你或许会对我发出灵魂拷问：判断类型是否相等（兼容）为什么不直接使用<code>type IfEquals<X, Y, A, B> = X extends Y ? A : B</code>呢？既简单有粗暴（PS：来自你的邪魅一笑~）。答案，我们看下下面的示例：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> IfEquals<X, Y, A, B> = X <span class="hljs-keyword">extends</span> Y ? A : B;

<span class="hljs-comment">/**
 * 还用上面的例子
 */</span>
<span class="hljs-keyword">type</span> T1 = &#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125;;
<span class="hljs-keyword">type</span> T2 = &#123;<span class="hljs-keyword">readonly</span> key1: <span class="hljs-built_in">string</span>&#125;;
<span class="hljs-keyword">type</span> T3 = &#123;key1?: <span class="hljs-built_in">string</span>&#125;;

<span class="hljs-comment">// A1 = true</span>
<span class="hljs-keyword">type</span> A1 = IfEquals<T1, T2, <span class="hljs-literal">true</span> , <span class="hljs-literal">false</span>>;
<span class="hljs-comment">// A2 = true</span>
<span class="hljs-keyword">type</span> A2 = IfEquals<T1, T3, <span class="hljs-literal">true</span> , <span class="hljs-literal">false</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案显而易见，对readonly等这些修饰符，真的无能无力了。夸爪Kill~~~</p>
<p><strong>第3步，解析<code>MutableKeys</code>实现逻辑</strong></p>
<ul>
<li><code>MutableKeys</code>首先约束T为object类型</li>
<li>通过映射类型<code>[P in keyof T]</code>进行遍历，key对应的值则是<code>IfEquals<类型1, 类型2, P></code>，如果类型1和类型2相等则返回对应的P（也就是key），否则返回never。</li>
</ul>
<p>而<code>P</code>其实就是一个只有一个当前key的联合类型，所以<code>[Q in P]: T[P]</code>也只是一个普通的映射类型。但是要注意的是参数1<code>&#123; [Q in P]: T[P] &#125;</code>是通过<code>&#123;&#125;</code>构造的一个类型，参数2<code>&#123; -readonly [Q in P]: T[P] &#125;</code>也是通过<code>&#123;&#125;</code>构造的一个类型,两者的唯一区别即使<code>-readonly</code>。</p>
<p>所以这里就有意思了，回想一下上面的第一步的例子，是不是就理解了：如果P是只读的，那么参数1和参数2的P最终都是只读的；如果<code>P</code>是非只读的，则参数1的<code>P</code>为非只读的，而参数2的<code>P</code>被<code>-readonly</code>去掉了非只读属性从而变成了只读属性。因此就完成了筛选：<code>P</code>为非只读时<code>IfEquals</code>返回的<code>P</code>，<code>P</code>为只读时<code>IfEquals</code>返回<code>never</code>。</p>
<ul>
<li>所以key为非只读时，类型为<code>key</code>，否则类型为<code>never</code>，最后通过<code>[keyof T]</code>得到了所有非只读key的联合类型。</li>
</ul>
<h3 data-id="heading-18">OptionalKeys</h3>
<p><code>OptionalKeys<T></code>提取T中所有可选类型的key组成的联合类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> OptionalKeys<T> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]: &#123;&#125; <span class="hljs-keyword">extends</span> Pick<T, P> ? P : <span class="hljs-built_in">never</span>
&#125;[keyof T];

<span class="hljs-keyword">type</span> Eg = OptionalKeys<&#123;key1?: <span class="hljs-built_in">string</span>, <span class="hljs-attr">key2</span>: <span class="hljs-built_in">number</span>&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>核心实现，用映射类型遍历所有key，通过<code>Pick<T, P></code>提取当前key和类型。注意，这里也是利用了同态拷贝会拷贝可选修饰符的特性。</li>
<li>利用<code>&#123;&#125; extends &#123;当前key: 类型&#125;</code>判断是否是可选类型。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Eg2 = false</span>
<span class="hljs-keyword">type</span> Eg2 = &#123;&#125; <span class="hljs-keyword">extends</span> &#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125; ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
<span class="hljs-comment">// Eg3 = true</span>
<span class="hljs-keyword">type</span> Eg3 = &#123;&#125; <span class="hljs-keyword">extends</span> &#123;key1?: <span class="hljs-built_in">string</span>&#125; ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用的就是<code>&#123;&#125;</code>和只包含可选参数类型<code>&#123;key?: string&#125;</code>是兼容的这一特性。把<code>extends</code>前面的<code>&#123;&#125;</code>替换成<code>object</code>也是可以的。</p>
<h3 data-id="heading-19">增强Pick</h3>
<ul>
<li>PickByValue提取指定值的类型</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 辅助函数，用于获取T中类型不能never的key组成的联合类型</span>
<span class="hljs-keyword">type</span> TypeKeys<T> = T[keyof T];

<span class="hljs-comment">/**
 * 核心实现
 */</span>
<span class="hljs-keyword">type</span> PickByValue<T, V> = Pick<T,
  TypeKeys<&#123;[P <span class="hljs-keyword">in</span> keyof T]: T[P] <span class="hljs-keyword">extends</span> V ? P : <span class="hljs-built_in">never</span>&#125;>
>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 *  type Eg = &#123;
 *    key1: number;
 *    key3: number;
 *  &#125;
 */</span>
<span class="hljs-keyword">type</span> Eg = PickByValue<&#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">key2</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">key3</span>: <span class="hljs-built_in">number</span>&#125;, <span class="hljs-built_in">number</span>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Ts的类型兼容特性，所以类似<code>string</code>是可以分配给<code>string | number</code>的，因此上述并不是精准的提取方式。如果实现精准的方式，则可以考虑下面个这个类型工具。</p>
<ul>
<li>PickByValueExact精准的提取指定值的类型</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心实现
 */</span>
<span class="hljs-keyword">type</span> PickByValueExact<T, V> = Pick<T,
  TypeKeys<&#123;[P <span class="hljs-keyword">in</span> keyof T]: [T[P]] <span class="hljs-keyword">extends</span> [V]
    ? ([V] <span class="hljs-keyword">extends</span> [T[P]] ? P : <span class="hljs-built_in">never</span>)
    : <span class="hljs-built_in">never</span>;
  &#125;>
>

<span class="hljs-comment">// type Eg1 = &#123; b: number &#125;;</span>
<span class="hljs-keyword">type</span> Eg1 = PickByValueExact<&#123;<span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>&#125;, <span class="hljs-built_in">number</span>>
<span class="hljs-comment">// type Eg2 = &#123; b: number; c: number | undefined &#125;</span>
<span class="hljs-keyword">type</span> Eg2 = PickByValueExact<&#123;<span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">c</span>: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>&#125;, <span class="hljs-built_in">number</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>PickByValueExact</code>的核心实现主要有三点：</p>
<p>一是利用<code>Pick</code>提取我们需要的<code>key</code>对应的类型</p>
<p>二是利用给泛型套一层元组规避<code>extends</code>的<strong>分发式联合类型</strong>的特性</p>
<p>三是利用两个类型互相兼容的方式判断是否相同。</p>
<p>具体可以看下下面例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Eq1<X, Y> = X <span class="hljs-keyword">extends</span> Y ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
<span class="hljs-keyword">type</span> Eq2<X, Y> = [X] <span class="hljs-keyword">extends</span> [Y] ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
<span class="hljs-keyword">type</span> Eq3<X, Y> = [X] <span class="hljs-keyword">extends</span> [Y]
  ? ([Y] <span class="hljs-keyword">extends</span> [X] ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>)
  : <span class="hljs-literal">false</span>;

<span class="hljs-comment">// boolean, 期望是false</span>
<span class="hljs-keyword">type</span> Eg1 = Eq1<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>>
<span class="hljs-comment">// false</span>
<span class="hljs-keyword">type</span> Eg2 = Eq2<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>>

<span class="hljs-comment">// true，期望是false</span>
<span class="hljs-keyword">type</span> Eg3 = Eq2<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>>
<span class="hljs-comment">// false</span>
<span class="hljs-keyword">type</span> Eg4 = Eq3<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>>

<span class="hljs-comment">// true，非strictNullChecks模式下的结果</span>
<span class="hljs-keyword">type</span> Eg5 = Eq3<<span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>, <span class="hljs-built_in">number</span>>
<span class="hljs-comment">// false，strictNullChecks模式下的结果</span>
<span class="hljs-keyword">type</span> Eg6 = Eq3<<span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>, <span class="hljs-built_in">number</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>从<code>Eg1</code>和<code>Eg2</code>对比可以看出，给<code>extends</code>参数套上元组可以避免分发的特性，从而得到期望的结果；</li>
<li>从<code>Eg3</code>和<code>Eg4</code>对比可以看出，通过判断两个类型互相是否兼容的方式，可以得到从属类型的正确相等判断。</li>
<li>从<code>Eg5</code>和<code>Eg6</code>对比可以看出，非<code>strictNullChecks</code>模式下，undefined和null可以赋值给其他类型的特性，导致<code>number | undefined, number</code>是兼容的，因为是非<code>strictNullChecks</code>模式，所以有这个结果也是符合预期。如果不需要此兼容结果，完全可以开启<code>strictNullChecks</code>模式。</li>
</ul>
<p>最后，同理想得到<code>OmitByValue</code>和<code>OmitByValueExact</code>基本一样的思路就不多说了，大家可以自己思考实现。</p>
<h3 data-id="heading-20">Intersection</h3>
<p><code>Intersection<T, U></code>从<code>T</code>中提取存在于<code>U</code>中的<code>key</code>和对应的类型。（注意，最终是从<code>T</code>中提取<code>key</code>和类型）</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * 核心思路利用Pick提取指定的key组成的类型
 */</span>
<span class="hljs-keyword">type</span> Intersection<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>, U <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>> = Pick<T,
  Extract<keyof T, keyof U> & Extract<keyof U, keyof T>
>

<span class="hljs-keyword">type</span> Eg = Intersection<&#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125;, &#123;<span class="hljs-attr">key1</span>:<span class="hljs-built_in">string</span>, <span class="hljs-attr">key2</span>: <span class="hljs-built_in">number</span>&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>约束<code>T</code>和<code>U</code>都是<code>object</code>，然后利用<code>Pick</code>提取指定的<code>key</code>组成的类型</li>
<li>通过<code>Extract<keyof T, keyof U></code>提取同时存在于T和U中的key，<code>Extract<keyof U, keyof T></code>也是同样的操作</li>
</ul>
<p>那么为什么要做<strong>2</strong>次<code>Extract</code>然后再交叉类型呢？原因还是在于处理类型的兼容推导问题，还记得<code>string</code>可分配给<code>string | number</code>的兼容吧。</p>
<p>扩展：</p>
<p>定义<code>Diff<T, U></code>，从<code>T</code>中排除存在于<code>U</code>中的key和类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Diff<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>, U <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>> = Pick<
  T,
  Exclude<keyof T, keyof U>
>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">Overwrite 和 Assign</h3>
<p><code>Overwrite<T, U></code>从<code>U</code>中的同名属性的类型覆盖<code>T</code>中的同名属性类型。(后者中的同名属性覆盖前者)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * Overwrite实现
 * 获取前者独有的key和类型，再取两者共有的key和该key在后者中的类型，最后合并。
 */</span>
<span class="hljs-keyword">type</span> Overwrite<
  T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>,
  U <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>,
  I = Diff<T, U> & Intersection<U, T>
> = Pick<I, keyof I>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg1 = &#123; key1: number; &#125;
 */</span>
<span class="hljs-keyword">type</span> Eg1 = Overwrite<&#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span>&#125;, &#123;<span class="hljs-attr">key1</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">other</span>: <span class="hljs-built_in">boolean</span>&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先约束<code>T</code>和<code>U</code>这两个参数都是<code>object</code></li>
<li>借助一个参数I的默认值作为实现过程，使用的时候不需要传递I参数（只是辅助实现的）</li>
<li>通过<code>Diff<T, U></code>获取到存在于<code>T</code>但是不存在于<code>U</code>中的key和其类型。（即获取<code>T</code>自己特有<code>key</code>和类型）。</li>
<li>通过<code>Intersection<U, T></code>获取<code>U</code>和<code>T</code>共有的<code>key</code>已经该key在<code>U</code>中的类型。即获取后者同名<code>key</code>已经类型。</li>
<li>最后通过交叉类型进行合并，从而曲线救国实现了覆盖操作。</li>
</ul>
<p>扩展：如何实现一个<code>Assign<T, U></code>（类似于<code>Object.assign()</code>）用于合并呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 实现</span>
<span class="hljs-keyword">type</span> Assign<
  T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>,
  U <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>,
  I = Diff<T, U> & Intersection<U, T> & Diff<U, T>
> = Pick<I, keyof I>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@example</span>
 * type Eg = &#123;
 *   name: string;
 *   age: string;
 *   other: string;
 * &#125;
 */</span>
<span class="hljs-keyword">type</span> Eg = Assign<
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>; age: <span class="hljs-built_in">number</span>; &#125;,
  &#123; <span class="hljs-attr">age</span>: <span class="hljs-built_in">string</span>; other: <span class="hljs-built_in">string</span>; &#125;
>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想一下，是不是就是先找到前者独有的key和类型，再找到两者共有的key以及该key在后者中的类型，最后找到后者独有的key和类型，最后依次的合并进去。</p>
<h3 data-id="heading-22">DeepRequired</h3>
<p><code>DeepRequired<T></code>将T的转换成必须属性。如果<code>T</code>为对象，则将递归对象将所有<code>key</code>转换成<code>required</code>，类型转换为<code>NonUndefined</code>；如果<code>T</code>为数组则递归遍历数组将每一项设置为<code>NonUndefined</code>。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * DeepRequired实现
 */</span>
<span class="hljs-keyword">type</span> DeepRequired<T> = T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>[]) => <span class="hljs-built_in">any</span>
  ? T
  : T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span><<span class="hljs-built_in">any</span>>
    ? _DeepRequiredArray<T[<span class="hljs-built_in">number</span>]>
    : T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>
      ? _DeepRequiredObject<T>
      : T;

<span class="hljs-comment">// 辅助工具，递归遍历数组将每一项转换成必选</span>
<span class="hljs-keyword">interface</span> _DeepRequiredArray<T> <span class="hljs-keyword">extends</span> Array<DeepRequired<NonUndefined<T>>> &#123;&#125;

<span class="hljs-comment">// 辅助工具，递归遍历对象将每一项转换成必选</span>
<span class="hljs-keyword">type</span> _DeepRequiredObject<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]-?: DeepRequired<NonUndefined<T[P]>>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>DeepRequired</code>利用<code>extends</code>判断如果是函数或<code>Primitive</code>的类型，就直接返回该类型。</li>
<li>如果是数组类型，则借助<code>_DeepRequiredArray</code>进行递归，并且传递的参数为数组所有子项类型组成的联合类型，如下：</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> A = [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>]
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description </span>对数组进行number索引访问，
 * 得到的是所有子项类型组成的联合类型
 * type B = string | number
 */</span>
<span class="hljs-keyword">type</span> B = A[<span class="hljs-built_in">number</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>_DeepRequiredObject</code>是个接口（定义成type也可以），其类型是<code>Array<T></code>；而此处的<code>T</code>则通过<code>DeepRequired<T></code>进行对每一项进行递归；在<code>T</code>被使用之前，先被<code>NonUndefined<T></code>处理一次，去掉无效类型。</p>
</li>
<li>
<p>如果是对象类型，则借助<code>_DeepRequiredObject</code>实现对象的递归遍历。<code>_DeepRequiredObject</code>只是一个普通的映射类型进行变量，然后对每个key添加<code>-?</code>修饰符转换成<code>required</code>类型。</p>
</li>
</ul>
<h3 data-id="heading-23">DeepReadonlyArray</h3>
<p><code>DeepReadonlyArray<T></code>将<code>T</code>的转换成只读的，如果<code>T</code>为<code>object</code>则将所有的key转换为只读的，如果<code>T</code>为数组则将数组转换成只读数组。整个过程是深度递归的。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * DeepReadonly实现
 */</span>
<span class="hljs-keyword">type</span> DeepReadonly<T> = T <span class="hljs-keyword">extends</span> (<span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span>[]</span>) =></span> <span class="hljs-built_in">any</span>) | Primitive
  ? T
  : T <span class="hljs-keyword">extends</span> _DeepReadonlyArray<infer U>
  ? _DeepReadonlyArray<U>
  : T <span class="hljs-keyword">extends</span> _DeepReadonlyObject<infer V>
  ? _DeepReadonlyObject<V>
  : T;

<span class="hljs-comment">/**
 * 工具类型，构造一个只读数组
 */</span>
<span class="hljs-keyword">interface</span> _DeepReadonlyArray<T> <span class="hljs-keyword">extends</span> ReadonlyArray<DeepReadonly<T>> &#123;&#125;

<span class="hljs-comment">/**
 * 工具类型，构造一个只读对象
 */</span>
<span class="hljs-keyword">type</span> _DeepReadonlyObject<T> = &#123;
  <span class="hljs-keyword">readonly</span> [P <span class="hljs-keyword">in</span> keyof T]: DeepReadonly<T[P]>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>基本实现原理和<code>DeepRequired</code>一样，但是注意<code>infer U</code>自动推导数组的类型，<code>infer V</code>推导对象的类型。</li>
</ul>
<h3 data-id="heading-24">UnionToIntersection</h3>
<p>将联合类型转变成交叉类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> UnionToIntersection<T> = (T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span>
  ? <span class="hljs-function">(<span class="hljs-params">arg: T</span>) =></span> <span class="hljs-built_in">void</span>
  : <span class="hljs-built_in">never</span>
) <span class="hljs-keyword">extends</span> (arg: infer U) => <span class="hljs-built_in">void</span> ? U : <span class="hljs-built_in">never</span>
<span class="hljs-keyword">type</span> Eg = UnionToIntersection<&#123; <span class="hljs-attr">key1</span>: <span class="hljs-built_in">string</span> &#125; | &#123; <span class="hljs-attr">key2</span>: <span class="hljs-built_in">number</span> &#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>T extends any ? (arg: T) => void : never</code>该表达式一定走true分支，用此方式构造一个逆变的联合类型<code>(arg: T1) => void | (arg: T2) => void | (arg: Tn) => void</code></li>
<li>再利用第二个<code>extends</code>配合<code>infer</code>推导得到U的类型，但是利用<code>infer</code>对<strong>协变类型的特性得到交叉类型</strong>。</li>
</ul>
<h2 data-id="heading-25">参考内容</h2>
<ul>
<li>Ts官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Futility-types.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/utility-types.html" ref="nofollow noopener noreferrer">www.typescriptlang.org/docs/handbo…</a></li>
<li>utility-types <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpiotrwitek%2Futility-types" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/piotrwitek/utility-types" ref="nofollow noopener noreferrer">github.com/piotrwitek/…</a></li>
</ul>
<p>转载请注明作者及出处！</p></div>  
</div>
            