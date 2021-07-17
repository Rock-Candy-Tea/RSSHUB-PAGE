
---
title: '_译_TypeScript条件类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=895'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 02:06:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=895'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fartsy.github.io%2Fblog%2F2018%2F11%2F21%2Fconditional-types-in-typescript%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://artsy.github.io/blog/2018/11/21/conditional-types-in-typescript/" ref="nofollow noopener noreferrer">artsy.github.io/blog/2018/1…</a></p>
</blockquote>
<p>条件类型或许并不是每天都会用到，但是你可能一直都在间接的使用它们。因为它们非常适合“管道(plumbing)”或者是“框架”代码，用来处理<strong>API边界(API boundaries)<strong>和</strong>底层的一些东西(behind-the-scenes kinda stuff)</strong>。</p>
<h2 data-id="heading-0">从一个条件类型开始</h2>
<p>这里有一段<code>JavaScript</code>代码：</p>
<pre><code class="copyable">
function process(text) &#123;

  return text && text.replace(/f/g, "p")

&#125;

process("foo").toUpperCase()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这段代码中，很明显<code>.toUpperCase()</code>的调用是安全的。每次给<code>process</code>传入一个字符串，函数返回一个字符串。</p>
<p>但是需要注意的是，我们也可以给这个函数传入一些别的参数，比如<code>null</code>，这时候函数会返回<code>null</code>。而这时候对返回结果调用<code>toUpperCase()</code>将会报错。</p>
<p>当然我们可以给这个函数添加一些基础的类型，让<code>TypeScript</code>来检查我们是否在安全的使用这个函数：</p>
<pre><code class="copyable">
function process(text: string | null): string | null &#123;

  return text && text.replace(/f/g, "p")

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么做看起来是安全的。如果像之前那样使用会发生什么？</p>
<pre><code class="copyable">
//            ⌄ Type Error! :(

process("foo").toUpperCase()

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TypeScript</code>提示了类型错误，因为它认为<code>process("foo")</code>可能会返回<code>null</code>，即使我们很清楚的知道实际上运行结果返回的不是null。但是<code>TypeScript</code>并没有办法对运行时的状态进行预测。</p>
<p>有一种方法能够帮助<code>TypeScript</code>更好的理解这个函数，就是使用<strong>重载(overloading)</strong>，重载可以为一个函数提供多个类型签名，来让<code>TypeScript</code>根据给定的上下文来决定使用哪一个。</p>
<pre><code class="copyable">
function process(text: null): null;

function process(text: string): string;

function process(text: any): any &#123;

  ...

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样如果我们传入一个<code>string</code>，它就会返回一个<code>string</code>。如果我们传入一个<code>null</code>，它就会返回一个<code>null</code>。</p>
<p>现在这个函数可以像我们所希望的那样工作了：</p>
<pre><code class="copyable">
// All clear!

process("foo").toUpperCase()

//           ⌄ Type Error! :)

process(null).toUpperCase()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这里有另外一个用例没有生效：</p>
<pre><code class="copyable">
declare const maybeFoo: string | null


//      ⌄ Type Error! :(

process(maybeFoo)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%3F%23code%2FGYVwdgxgLglg9mABABwE5wgUwM7YBRSYAeUAXImCADZUCU5lNA3AFCiSwIrpa4HFlE2KKhhgA5vSEix41gHp5idtHhI0GHPkIlyw0RMQAfCtTp6Zhk4yqsVndTy39diAIZgAnlI%2BfEAbxZERBYAXxYWABNMCCo3VExECARhREJhCwNxY1MaFg1ebRwoWiA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/play?#code/GYVwdgxgLglg9mABABwE5wgUwM7YBRSYAeUAXImCADZUCU5lNA3AFCiSwIrpa4HFlE2KKhhgA5vSEix41gHp5idtHhI0GHPkIlyw0RMQAfCtTp6Zhk4yqsVndTy39diAIZgAnlI+fEAbxZERBYAXxYWABNMCCo3VExECARhREJhCwNxY1MaFg1ebRwoWiA" ref="nofollow noopener noreferrer">亲手试一试</a></p>
<p><code>TypeScript</code>不允许我们传入一个类型<code>string | null</code>的参数，因为它无法合并重载声明。这时候我们既可以选择新增一种重载类型，(╯°□°)╯︵ ┻━┻亦或者选择使用<strong>条件类型</strong>。</p>
<pre><code class="copyable">
function process<T extends string | null>(

  text: T

): T extends string ? string : null &#123;

  ...

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们引入一个类型变量<code>T</code>来做<code>text</code>参数的类型。然后我们可以使用<code>T</code>作为条件返回类型的一部分：<code>T extends string ? string : null</code>。你或许已经注意到了这看起来像是一个三元表达式。事实上，它确实做着相似的事情，但是是在类型系统进行编译时完成的。</p>
<p>这样做就兼顾到了我们所有的使用用例：</p>
<pre><code class="copyable">
typeof process("foo") // => string

typeof process(null) // => null

typeof process(maybeFoo) // => string | null

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是条件类型，一种三元表达式，它看起来总是长这样：</p>
<pre><code class="copyable">
A extends B ? C : D

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>A、B、C、D</code>可以是任何我们已知的类型表达式，重点是在左边，<code>A extends B</code>条件。</p>
<h2 data-id="heading-1">可分配性</h2>
<p><code>extends</code>关键字是条件类型的核心，<code>A extends B</code>就意味着<strong>任何满足类型为<code>A</code>的值都可以安全的分配(assign)给类型为<code>B</code>的变量</strong>。用类型系统的话讲叫：<strong>A能够分配给B（A is assignable to B）</strong>。从如下这段代码中理解一下<strong>可分配</strong>：</p>
<pre><code class="copyable">
declare const a: A

const b: B = a

// type check succeeds only if A is assignable to B

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TypeScript</code>使用的是一种被称为<strong>结构类型</strong>的方法来决定哪些类型可以相互分配。这种类型系统在大约十年前开始出现在主流语言中，如果你有<code>C#</code>或者<code>Java</code>经验可能会觉得这种类型系统有点反直觉。</p>
<p>你或许听说过和动态类型语言息息相关的<strong>鸭子类型（ducking type）</strong>，<code>ducking type</code>的短语出自一个谚语：</p>
<blockquote>
<p>If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.</p>
</blockquote>
<p>在鸭子类型中，我们通过事物的行为来判断一个事物，而不是通过看它是谁或者追溯它来自何处。可以把它理解为“任人唯贤”。结构类型就是将这种思想应用于静态编译时类型系统的产物。</p>
<p>所以<code>TypeScript</code>只关心一个类型能够做什么，而不关心它叫什么以及它在类型层次结构中处于什么位置。</p>
<p>来看一个简单的例子：</p>
<pre><code class="copyable">
class A &#123;&#125;

class B &#123;&#125;

const b: B = new A() // ✔ all good

const a: A = new B() // ✔ all good

new A() instanceof B // => false

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面代码中，<code>TypeScript</code>将两个完全不相关的类型视为相等的，因为它们具有相同的结构和能力。但是在运行时，这两个类并不是等价的。</p>
<p>这是<code>TypeScript</code>和<code>JavaScript</code>在语义上存在显著差别的一个典型例子。这看起来似乎是一个问题，其实是因为结构类型要比<code>Java风格</code>的<code>名义（nominal）</code>类型要更加的灵活多变，后者更加关注名称（names）和层次结构（hierarchy）。但是这两者并不是互相排斥的，在某些语言中，例如<code>Scala</code>和<code>Flow</code>，允许你混用它们来解决特定问题。</p>
<p>除此之外，可分配性和结构类型这两者在实际的代码中是非常直观的：</p>
<pre><code class="copyable">
interface Shape &#123;

  color: string

&#125;

class Circle &#123;

  color: string

  radius: number

&#125;


// ✔ All good! Circles have a color

const shape: Shape = new Circle()

// ✘ Type error! Not all shapes have a radius!

const circle: Circle = shape

<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以从结构上来看，<code>A extends B</code>很像是<strong>A是B的超集</strong>。说的更明白点，就是<strong>类型A包含类型B的所有属性，并且可能还有更多</strong>。</p>
<p>有一个需要注意的点，就是<strong>字面（literal）类型</strong>。在<code>TypeScript</code>中你可以使用字面量本身作为类型。</p>
<pre><code class="copyable">
let fruit: "banana" = "banana"

// Type Error! "apple" is not assignable to "banana"

fruit = "apple"

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>"banana"</code>作为字符串并没有比其他的字符串多出来什么属性，但是<code>"banana"</code>作为一个类型，却要比<code>string</code>类型具体的多，它只允许赋值为<code>"banana"</code>。</p>
<p>所以也可以从另一个角度理解<code>A extends B</code>：<strong>那就是<code>A</code>是<code>B</code>的一个更具体的版本</strong>。这里的“具体”的含义可以理解为有更多的属性或者是更加的明确，也就是有更多的限制。与之前的提到的<code>A</code>是<code>B</code>的超集一个含义。</p>
<p>这就引出了<strong>顶层类型（Top）和底层类型（Bottom）</strong>，也就是不那么具体的类型和最具体的类型。</p>
<p>在类型理论中，顶层类型是所有其他的类型都可以分配的类型，如果我们对一个类型没有任何具体的信息，那么就可以把这个类型设置为顶层类型，顶层类型被视为所有可能类型的联合：</p>
<pre><code class="copyable">
type Top = string | number | &#123;foo: Bar&#125; | Baz[] | ... | ∞

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TypeScript</code>包含两个顶层类型：<code>any</code>和<code>unknown</code>。</p>
<ul>
<li>
<p>使用<code>any</code>就意味着：你无法确定值的类型，所以<code>TypeScript</code>会假定你使用的是正确的，并且不会有任何的告警</p>
</li>
<li>
<p>使用<code>unknown</code>就意味着：同样是无法确定值的类型，但是<code>TypeScript</code>会要求你在运行时检查值的类型</p>
</li>
</ul>
<p>底层（bottom）类型是其他类型不可分配的类型，也没有值可以赋值给这个类型的变量。可以将其视为空联合类型：</p>
<pre><code class="copyable">
type Bottom = ∅

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TypeScript</code>中有一个底层类型：<code>never</code>。这个类型很能见名知意，也就是<strong>啥也不是</strong>。</p>
<p>在使用条件类型时，了解顶层类型和底层类型很有用。<code>never</code>在使用条件类型细化联合类型的时候尤其有用。</p>
<h2 data-id="heading-2">基于“分发条件类型”来细化联合类型</h2>
<p>条件类型可以用来过滤掉联合类型的特定成员。用一个例子来说明，首先我们定义一个联合类型<code>Animal</code>：</p>
<pre><code class="copyable">
type Animal = Lion | Zebra | Tiger | Shark

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们需要一个函数来过滤出哪些是猫科动物，我们可以写一个工具类型<code>ExtractCat</code>来实现：</p>
<pre><code class="copyable">
type ExtractCat<A> = A extends &#123; meow(): void &#125; ? A : never

type Cat = ExtractCat<Animal>

// => Lion | Tiger

<span class="copy-code-btn">复制代码</span></code></pre>
<p>I know lions and tigers don't meow, but how cute would it be if they did ^_^</p>
<p>起初，这种方式让我觉得有点迷糊又神奇。接下来我们深入了解一下<code>TypeScript</code>在处理<code>ExtractCat<Animal></code>时做了什么：</p>
<p><strong>首先，它将<code>ExtractCat</code>递归的应用于<code>Animal</code>的所有成员：</strong></p>
<pre><code class="copyable">
type Cat =

  | ExtractCat<Lion>

  | ExtractCat<Zebra>

  | ExtractCat<Tiger>

  | ExtractCat<Shark>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>然后它判断这些条件类型</strong>：</p>
<pre><code class="copyable">
type Cat = Lion | never | Tiger | never

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>接下来一些有趣的事情发生了，还记得没有值可以是<code>never</code>类型么？所以在联合类型中包含<code>never</code>是没有任何意义的，所以<code>TypeScript</code>抛弃了它</strong>：</p>
<pre><code class="copyable">
type Cat = Lion | Tiger

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>TypeScript</code>中，这种条件类型的用法被称为<strong>分发条件类型（distributive conditional type）。</strong></p>
<p>这种“分发”，也就是联合类型以递归方式展开，<strong>但是这是有限制的：只发生在<code>extends</code>关键字左侧是普通类型变量的时候。我们将在下一节看到这意味着什么以及如何突破这种限制。</strong></p>
<h2 data-id="heading-3">分发条件类型的一个真实使用场景</h2>
<p>前段时间我正在写一个Chrome插件，它有一个<code>background</code>脚本和一个<code>view</code>脚本，这两者运行在不同的执行上下文中。它们之间需要共享状态，唯一的途径就是通过可序列化消息传递机制。受<code>Redux</code>启发我定义了一个全局联合类型<code>Action</code>来作为可以在不同上下文中传递的消息的模型。</p>
<pre><code class="copyable">
type Action =

  | &#123;

      type: "INIT"

    &#125;

  | &#123;

      type: "SYNC"

    &#125;

  | &#123;

      type: "LOG_IN"

      emailAddress: string

    &#125;

  | &#123;

      type: "LOG_IN_SUCCESS"

      accessToken: string

    &#125;

// ...

<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个全局的<code>dispatch</code>函数，通过这个函数就可以在不同的上下文广播消息。</p>
<pre><code class="copyable">
declare function dispatch(action: Action): void

// ...

dispatch(&#123;

  type: "INIT"

&#125;)

// ...

dispatch(&#123;

  type: "LOG_IN",

  emailAddress: "david.sheldrick@artsy.net"

&#125;)

// ...

dispatch(&#123;

  type: "LOG_IN_SUCCESS",

  accessToken: "038fh239h923908h"

&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%3F%23code%2FC4TwDgpgBAggxsAlgewHZQLwFgBQUoA%2BUA3rvuVKJAFxQBEAkgHIMAqdZ5Avp0aXhUrgItOgGUAmkwDCHAfh4C%2BnClRH0AMgHkA4gH1mcwVAgBbAIaIANjAAmtgE4QAzs9rPgDxKgDmKqIr4yvLkaqLa%2Bsx6YgCq0tIAomJiRoLmcHAuzqzIANYQqO6e3n4hiri2EHBW5k5QAGYArqgIKOi2iM5g5sBwABYAFOlIaLTwI6gAlLQAbsiItrgVnd29g-z4YfTMbHJck0s4HV09-QMbQjSaugZMdAA0nGaWNvZOrqK25jMLAHTOfQgVkciDguQAArVgM4QL9UBBgHsDjhlic1udOFs6BFbtE4olkg9OOlMq4cvlCvQAAwAZgAHPU%2BgAmGkATj6rJZrKpdL6SKAA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/play?#code/C4TwDgpgBAggxsAlgewHZQLwFgBQUoA+UA3rvuVKJAFxQBEAkgHIMAqdZ5Avp0aXhUrgItOgGUAmkwDCHAfh4C+nClRH0AMgHkA4gH1mcwVAgBbAIaIANjAAmtgE4QAzs9rPgDxKgDmKqIr4yvLkaqLa+sx6YgCq0tIAomJiRoLmcHAuzqzIANYQqO6e3n4hiri2EHBW5k5QAGYArqgIKOi2iM5g5sBwABYAFOlIaLTwI6gAlLQAbsiItrgVnd29g-z4YfTMbHJck0s4HV09-QMbQjSaugZMdAA0nGaWNvZOrqK25jMLAHTOfQgVkciDguQAArVgM4QL9UBBgHsDjhlic1udOFs6BFbtE4olkg9OOlMq4cvlCvQAAwAZgAHPU+gAmGkATj6rJZrKpdL6SKAA" ref="nofollow noopener noreferrer">亲手试一试</a></p>
<p>这个API是类型安全的，并且与我的IDE的自动补全功能配合的也很好，我完全可以到这里就结束了，然后去做别的事情。</p>
<p>但是总有个想法在我的脑海里挥之不去，我相信大多数开发者可能都会有这种想法。</p>
<blockquote>
<p> 此处省略作者脑海中的思想斗争，感兴趣的可以看原文</p>
</blockquote>
<p>我希望可以像这样调用<code>dispatch</code>函数：</p>
<pre><code class="copyable">
// first argument is the 'type'

// second is any extra parameters

dispatch("LOG_IN_SUCCESS", &#123;

  accessToken: "038fh239h923908h"

&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>派生第一个参数的类型很简单：</p>
<pre><code class="copyable">
type ActionType = Action["type"]

// => "INIT" | "SYNC" | "LOG_IN" | "LOG_IN_SUCCESS"

<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是第二个参数的类型是由第一个参数决定的，我们可以使用一个类型变量来对依赖进行建模：</p>
<pre><code class="copyable">
declare function dispatch<T extends ActionType>(

  type: T,

  args: ExtractActionParameters<Action, T>

): void

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这里的<code>ExtractActionParameters</code>是什么东西呢？</p>
<p>显然是一个条件类型！如下所示是第一次尝试实现<code>ExtractActionParameters</code>：</p>
<pre><code class="copyable">
type ExtractActionParameters<A, T> = A extends &#123; type: T &#125; ? A : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这很像之前的<code>ExtractCat</code>那个例子，在那个例子里我们通过搜索是否具有<code>meow()</code>来过滤<code>Animals联合类型</code>。在这里我们通过<code>type</code>属性来过滤<code>Action联合类型</code>。我们来看一下实际效果：</p>
<pre><code class="copyable">
type Test = ExtractActionParameters<Action, "LOG_IN">

// => &#123; type: "LOG_IN", emailAddress: string &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里已经差不多了，但是目前提取的结果还保留着<code>type</code>，这就导致在调用<code>dispatch</code>还是需要再写一次<code>type</code>，这和我们的初衷并不一致。</p>
<p>我们可以通过组合使用条件类型和<code>keyof</code>操作符来实现一个<strong>映射类型（mapped type）</strong>，达到排除<code>type</code>属性的目的。</p>
<p>映射类型允许你在一个键的联合类型上通过映射来创建一个新的类型。</p>
<ul>
<li>首先，可以使用<code>keyof</code>操作符获取一个已经存在的类型的所有键作为一个联合类型返回</li>
<li>然后，可以使用条件类型来筛选这个键的联合类型返回一个筛选后的类型</li>
</ul>
<p>接下来通过一个具体的例子演示一下如何实现：</p>
<pre><code class="copyable">
type ExcludeTypeKey<K> = K extends "type" ? never : K

type Test = ExcludeTypeKey<"emailAddress" | "type" | "foo">

// => "emailAddress" | "foo"


type ExcludeTypeField<A> = &#123;[K in ExcludeTypeKey<A>]: A[K]&#125;

type Test = ExcludeTypeField<&#123; type: "LOG_IN"; emailAddress: string &#125;>

// => &#123; emailAddress: string &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们就可以使用<code>ExcludeTypeField</code>来重新定义<code>ExtractActionParameters</code>：</p>
<pre><code class="copyable">
type ExtractActionParameters<A, T> = A extends &#123; type: T &#125;

  ? ExcludeTypeField<A>

  : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，这个新版本的<code>dispatch</code>函数是类型安全的了：</p>
<pre><code class="copyable">
// All clear! :)

dispatch("LOG_IN_SUCCESS", &#123;

  accessToken: "038fh239h923908h"

&#125;)

dispatch("LOG_IN_SUCCESS", &#123;

  // Type Error! :)

  badKey: "038fh239h923908h"

&#125;)

// Type Error! :)

dispatch("BAD_TYPE", &#123;

  accessToken: "038fh239h923908h"

&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%3F%23code%2FC4TwDgpgBAggxsAlgewHZQLwFgBQUoA%2BUA3rvuVKJAFxQBEAkgHIMAqdZ5Avp0aXhUrgItOgGUAmkwDCHAfh4C%2BnClRH0AMgHkA4gH1mcwVAgBbAIaIANjAAmtgE4QAzs9rPgDxKgDmKqIr4yvLkaqLa%2Bsx6YgCq0tIAomJiRoLmcHAuzqzIANYQqO6e3n4hirhqsAgoqKzCmFVIaADadGp0ALq4uLYQcFbmTlAAZgCuqNVoULaIzmDmwHAAFgA8rCYAHsAFts6NNXWQAHwAFP5hUKwANP6DPm5QCVsO6cDwTagACoPmphDbDmcK3eNSulyOuAAlLQAG7IRC2bo4SpPfqjXqHCAAaQgIBWWKODSxm22qF29HaUAA-FBUBAYRAHFBaFikSiNmiMcIAGKICBWWzAwkYEhQZrE7yPDlWdEQTE4vH5EDIYawI4dWgwcUdAJs%2BpPTyvEFob4vP4AoEwMGsYWwEk7PbEIQ0S66kI01EyrmQXn8wUwCEhWh0hkOTi4AD0EdgVisUH6EEGAEJmZCerN5oslic6BEDExonFEsk6GD%2BBR0plXDl8oV6AAGADMAA5hksAEyNgCcSy7na79ebSzkXDTOHTcwWyxzeaisXiSRSZf8Ucu%2BocDmQDhT1DHFAARuZbArRE3Wx3u73%2B4Ph7hR0jV5jHhutzuxzNJ1mcwAhGAAET0VgJE%2BBJSxIW4MiyGsClPFs237K9uxvEdISAA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/play?#code/C4TwDgpgBAggxsAlgewHZQLwFgBQUoA+UA3rvuVKJAFxQBEAkgHIMAqdZ5Avp0aXhUrgItOgGUAmkwDCHAfh4C+nClRH0AMgHkA4gH1mcwVAgBbAIaIANjAAmtgE4QAzs9rPgDxKgDmKqIr4yvLkaqLa+sx6YgCq0tIAomJiRoLmcHAuzqzIANYQqO6e3n4hirhqsAgoqKzCmFVIaADadGp0ALq4uLYQcFbmTlAAZgCuqNVoULaIzmDmwHAAFgA8rCYAHsAFts6NNXWQAHwAFP5hUKwANP6DPm5QCVsO6cDwTagACoPmphDbDmcK3eNSulyOuAAlLQAG7IRC2bo4SpPfqjXqHCAAaQgIBWWKODSxm22qF29HaUAA-FBUBAYRAHFBaFikSiNmiMcIAGKICBWWzAwkYEhQZrE7yPDlWdEQTE4vH5EDIYawI4dWgwcUdAJs+pPTyvEFob4vP4AoEwMGsYWwEk7PbEIQ0S66kI01EyrmQXn8wUwCEhWh0hkOTi4AD0EdgVisUH6EEGAEJmZCerN5oslic6BEDExonFEsk6GD+BR0plXDl8oV6AAGADMAA5hksAEyNgCcSy7na79ebSzkXDTOHTcwWyxzeaisXiSRSZf8Ucu+ocDmQDhT1DHFAARuZbArRE3Wx3u73+4Ph7hR0jV5jHhutzuxzNJ1mcwAhGAAET0VgJE+BJSxIW4MiyGsClPFs237K9uxvEdISAA" ref="nofollow noopener noreferrer">亲手试一试</a></p>
<p>还剩一个严重的问题需要处理，那就是如果一个<code>action</code>没有参数需要传递，但我还是需要写一个空对象作为<code>dispatch</code>函数的第二个参数。</p>
<pre><code class="copyable">
dispatch("INIT", &#123;&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一种可耻的浪费行为，告诉拜登今天晚上别等我打麻将了，我要修复这个问题，立刻！马上！！🤪</p>
<p>可能我们会立即想到的一个做法是把第二个参数设置为可选的，但这会导致一个新的问题就是有参数的<code>action</code>如果不传递参数也会被允许，这就不满足类型安全了。</p>
<p>更好的做法是定义一个<code>dispatch</code>函数的重载：</p>
<pre><code class="copyable">
// And let's say that any actions that don't require

// extra parameters are 'simple' actions.

declare function dispatch(type: SimpleActionType): void

// this signature is just like before

declare function dispatch<T extends ActionType>(

  type: T,

  args: ExtractActionParameters<Action, T>

): void


type SimpleActionType = ExtractSimpleAction<Action>['type']

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们应该如何定义条件类型<code>ExtractSimpleAction</code>呢？我们知道如果把一个<code>action</code>类型的<code>type</code>字段去掉，返回的是一个空对象的话，那么这个<code>action</code>就是一个<code>SimpleActionType</code>。按照这个思路我们似乎可以这么实现：</p>
<pre><code class="copyable">
type ExtractSimpleAction<A> = ExcludeTypeField<A> extends &#123;&#125; ? A : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样是达不到我们期望的效果的。因为<code>ExcludeTypeField<A> extends &#123;&#125;</code>总是会返回<code>true</code>。这是因为<code>ExcludeTypeField<A></code>的返回值不存在无法分配给<code>&#123;&#125;</code>的情况。</p>
<p>既然这样，我们就交换两个参数的位置：</p>
<pre><code class="copyable">
type ExtractSimpleAction<A> = &#123;&#125; extends ExcludeTypeField<A> ? A : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在看起来如果<code>ExcludeTypeField<A></code>是空对象，那么就会走<code>true</code>分支，否则就会走<code>false</code>分支。</p>
<p>你以为这就解决了？并没有。这个条件类型是不起作用的。也许有的读者还记得之前说过这段话：</p>
<blockquote>
<p> 这种“分发”，也就是联合类型以递归方式展开，只发生在<code>extends</code>关键字左侧是普通类型变量的时候</p>
</blockquote>
<p>类型变量常常被定义在泛型参数列表中，被<code><</code>和<code>></code>包裹。例如：</p>
<pre><code class="copyable">
type Blah<These, Are, Type, Variables> = ...


function blah<And, So, Are, These>() &#123;

  ...

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你希望联合类型递归展开应用条件类型，那么这个联合类型需要：</p>
<ul>
<li>
<p>绑定在一个类型变量上</p>
</li>
<li>
<p>这个类型变量需要出现在<code>extends</code>关键字的左侧</p>
</li>
</ul>
<p>如下所示是可以展开应用条件类型的例子：</p>
<pre><code class="copyable">
type Blah<Var> = Var extends Whatever ? A : B

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些就不可以：</p>
<pre><code class="copyable">
type Blah<Var> = Foo<Var> extends Whatever ? A : B

type Blah<Var> = Whatever extends Var ? A : B

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我发现这个限制的时候，我认为我发现了一个分发条件类型在底层工作方式上的一个根本缺陷。我觉得这可能是对算法复杂度做的某种让步。我觉得可能是我的用例太高级了以至于<code>TypeScript</code>显得有些无能为力。</p>
<p>但事实证明我错了，这只是一个实用的语言设计来避免额外的语法，要解决也很简单：</p>
<pre><code class="copyable">
type ExtractSimpleAction<A> = A extends any

  ? &#123;&#125; extends ExcludeTypeField<A>

    ? A

    : never

  : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们只是把我们的逻辑包裹在了一个额外的条件判断中，这个外层的条件类型会永远执行<code>true</code>。</p>
<p>最终，我们可以删除无用的多余代码了：</p>
<pre><code class="copyable">
dispatch("INIT")

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><code>TypeScript</code>提供了一些我们可以在本节使用的内置类型：</p>
<pre><code class="copyable">
// Exclude from U those types that are assignable to T

type Exclude<U, T> = U extends T ? never : U

// Extract from U those types that are assignable to T

type Extract<U, T> = U extends T ? U : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前我们是这样实现<code>ExcludeTypeField</code>的：</p>
<pre><code class="copyable">
type ExcludeTypeField<A> = &#123; [K in ExcludeTypeKey<keyof A>]: A[K] &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以这样做：</p>
<pre><code class="copyable">
type ExcludeTypeField<A> = &#123; [K in Exclude<keyof A, "type">]: A[K] &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前我们这样实现<code>ExtractActionParameters</code>：</p>
<pre><code class="copyable">
type ExtractActionParameters<A, T> = A extends &#123; type: T &#125;

  ? ExcludeTypeField<A>

  : never

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们可以这样实现：</p>
<pre><code class="copyable">
type ExtractActionParameters<A, T> = ExcludeTypeField<Extract<A, &#123; type: T &#125;>>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">做个题休息一下</h2>
<p>目前，如下所示的代码仍然可以工作：</p>
<pre><code class="copyable">
dispatch("INIT", &#123;&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用你目前学到的东西，让没有参数的<code>action</code>传递了第二个参数的时候报错。</p>
<h2 data-id="heading-5">使用<code>infer</code>解构类型</h2>
<p>条件类型还有另外一个关键字：<code>infer</code>。它可以在 extends 关键字右侧的类型表达式中的任何位置使用。使用它可以为出现在该位置的任何类型命名。例如：</p>
<pre><code class="copyable">
type Unpack<A> = A extends Array<infer E> ? E : A


type Test = Unpack<Apple[]>

// => Apple

type Test = Unpack<Apple>

// => Apple

<span class="copy-code-btn">复制代码</span></code></pre>
<p>它可以优雅的处理歧义：</p>
<pre><code class="copyable">
type Stairs = Unpack<Apple[] | Pear[]>

// => Apple | Pear

<span class="copy-code-btn">复制代码</span></code></pre>
<p>你甚至可以多次使用<code>infer</code>：</p>
<pre><code class="copyable">
type Flip<T> = T extends [infer A, infer B] ? [B, A] : never

type Stairs = Flip<[Pear, Apple]>

// => [Apple, Pear]



type Union<T> = T extends [infer A, infer A] ? A : never

type Stairs = Union<[Apple, Pear]>

// => Apple | Pear

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">其他的内置条件类型</h2>
<p>我们已经看到了 Exclude 和 Extract，并且 TypeScript 提供了其他一些开箱即用的条件类型。</p>
<pre><code class="copyable">
// Exclude null and undefined from T

type NonNullable<T> =

  T extends null | undefined ? never : T




// Obtain the parameters of a function type in a tuple

type Parameters<T> =

  T extends (...args: infer P) => any ? P : never




// Obtain the parameters of a constructor function type in a tuple

type ConstructorParameters<T> =

  T extends new (...args: infer P) => any ? P : never




// Obtain the return type of a function type

type ReturnType<T> =

  T extends (...args: any[]) => infer R ? R : any




// Obtain the return type of a constructor function type

type InstanceType<T> =

  T extends new (...args: any[]) => infer R ? R : any

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">扩展阅读</h2>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-2-8.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-8.html" ref="nofollow noopener noreferrer">TypeScript 2.8 release notes</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript%2Fpull%2F21316" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/TypeScript/pull/21316" ref="nofollow noopener noreferrer">Microsoft/Typescript#21316</a> Conditional types pull request</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript%2Fpull%2F21496" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/TypeScript/pull/21496" ref="nofollow noopener noreferrer">Microsoft/Typescript#21496</a> <code>infer</code>pull request</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript%2Fblob%2Fa2205ad53d8f65a129a552b752d1e06fee3d41fc%2Flib%2Flib.es5.d.ts%23L1446" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/TypeScript/blob/a2205ad53d8f65a129a552b752d1e06fee3d41fc/lib/lib.es5.d.ts#L1446" ref="nofollow noopener noreferrer">lib.es5.d.ts#L1446</a> built-in conditional type definitions</p>
</li>
</ul></div>  
</div>
            