
---
title: 'TypeScript 的另一面：类型编程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c852f78788544b23831e907efaaf4d80~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 18:20:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c852f78788544b23831e907efaaf4d80~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：穹心</p>
<h2 data-id="heading-0">前言</h2>
<p>作为前端开发的趋势之一，TypeScript 正在为越来越多的开发者所喜爱，从大的方面来说，几乎九成的框架与工具库都以其写就（或者就是类似的类型方案，如 Flow）；而从小的方面来说，即使是写个配置文件（如 vite 的配置文件）或者小脚本（感谢 ts-node），TypeScript 也是一大助力。一样事物不可能做到每个人都喜欢，如 nodemon 的作者 Remy Sharp 就曾表示自己从来没有使用过 TS（见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fremy%2Fnodemon%2Fissues%2F1565%23issuecomment-490429334" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/remy/nodemon/issues/1565#issuecomment-490429334" ref="nofollow noopener noreferrer">#1565</a>），在以后也不会去学习 TS，这可能是因为语言习惯的问题。而通常阻碍新人上手 TypeScript 的还有另外一座大山：学习成本高。</p>
<p>在学习 TypeScript 的开始阶段，很多同学对它是又爱又恨的，离不开它的类型提示和工程能力，却又经常为类型错误困扰，最后不得不用个 any 了事，这样的情况多了，TypeScript 就慢慢写成了 AnyScript...</p>
<p>这个问题的罪魁祸首其实就是部分同学在开始学习 TypeScript 时，要么是被逼上梁山，在一片空白的情况下接手 TS 项目，要么是不知道如何学习，那么良心的官方文档不看，看了几篇相关文章就觉得自己会了，最后遇到问题还是一头雾水。</p>
<p>这篇文章就是为了解决这后者的问题，尝试专注于 TypeScript 的类型编程部分（TS 还有几个部分？请看下面的解释），从最基础的泛型开始，到索引、映射、条件等类型，再到 is、in、infer 等关键字，最后是压轴的工具类型。打开你的 IDE，跟着笔者一节节的敲完代码，帮助你的 TypeScript 水平迈上新的台阶。</p>
<blockquote>
<p>需要注意的是，本文并非 TypeScript 入门文章，并不适用于对 TypeScript 暂时没有任何经验的同学。如果你仍处于新手期，笔者在这里推荐 xcatliu 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fts.xcatliu.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ts.xcatliu.com/" ref="nofollow noopener noreferrer">TypeScript 入门教程</a> 以及 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/zh/" ref="nofollow noopener noreferrer">官方文档</a>，从我个人的经验来看，你可以在初期阅读入门教程，并在感到困惑时前往官方文档对应部分查阅。</p>
<p>在完成 TypeScript 的基础入门后，欢迎再次回到本篇文章。</p>
</blockquote>
<h3 data-id="heading-1">TypeScript = 类型编程 + ES 提案</h3>
<p>笔者通常将 TypeScript 划分成两个部分：</p>
<ul>
<li>
<p><strong>预实现的 ES 提案</strong>，如 装饰器、 可选链<code>?.</code> 、空值合并运算符<code>??</code>（和可选链一起在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-3-7%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-3-7/" ref="nofollow noopener noreferrer">TypeScript3.7</a> 中引入）、类的私有成员 <code>private</code> 等。除了部分极端不稳定的语法（说的就是你，装饰器）以外，大部分的 TS 实现实际上就是未来的 ES 语法。</p>
<blockquote>
<p>严谨的来说，现在的 ES 版本装饰器和 TS 版本装饰器已经是两个东西了，笔者先前在 <a href="https://juejin.im/post/6859314697204662279" target="_blank" title="https://juejin.im/post/6859314697204662279">走近 MidwayJS：初识 TS 装饰器与 IoC 机制</a> 这篇文章中介绍了一些关于 TS 装饰器的历史，有兴趣的同学不妨一读。</p>
</blockquote>
<p>对于这一部分来说，无论你先前是只有 JavaScript 这门语言的使用经验，还是有过 Java、C#的使用经历，都能非常快速地上手，毕竟主要还是语法糖为主嘛。当然，这也是实际开发中使用最多的部分，毕竟和另一部分：<strong>类型编程</strong>比起来，还是这一部分更接地气。</p>
</li>
<li>
<p><strong>类型编程</strong>，从一个简简单单的<code>interface</code>，到看起来挺高级的<code>T extends SomeType</code> ，再到各种不明觉厉的工具类型<code>Partial</code>、<code>Required</code>等，这些都属于类型编程的范畴。这一部分对代码实际的功能层面没有任何影响，即使你一行代码十个 any，遇到类型错误就 <code>@ts-ignore</code> （类似于<code>@eslint-ignore</code>，将会禁用掉下一行的类型检查），甚至直接开启 <code>--transpileOnly</code> （这一选项会禁用掉 TS 编译器的类型检查能力，仅编译代码，会获得更快的编译速度·），也不会影响你代码本身的逻辑。<br>
然而，这也就是类型编程一直不受到太多重视的原因：相比于语法，它会带来许多额外的代码量（类型定义代码甚至可能超过业务代码量）等问题。而且实际业务中并不会需要多么苛刻的类型定义，通常只会对接口数据、应用状态流等进行定义，通常是底层框架类库才会需要大量的类型编程代码。<br>
如果说，上一部分让你写的代码更甜，那么这一部分，最重要的作用是让你的代码变得更优雅健壮（是的，优雅和健壮并不冲突）。如果你所在的团队使用 Sentry 这一类监控平台，对于 JS 代码来说最常见的错误就是<code>Cannot read property 'xxx' of undefined</code>、<code>undefined is not a function</code>这种（见<a href="https://link.juejin.cn/?target=https%3A%2F%2Frollbar.com%2Fblog%2Ftop-10-javascript-errors%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollbar.com/blog/top-10-javascript-errors/" ref="nofollow noopener noreferrer">top-10-javascript-errors</a>），虽然即使是 TS 也不可能把这个错误直接完全抹消，但也能解决十之八九了。</p>
</li>
</ul>
<p>好了，做了这么多铺垫，是时候开始进入正题了，本文的章节分布如下，如果你已经有部分前置知识的基础（如泛型），可以直接跳过。</p>
<ul>
<li>
<p>类型编程的基础：泛型</p>
</li>
<li>
<p>类型守卫与 is、in 关键字</p>
</li>
<li>
<p>索引类型与映射类型</p>
</li>
<li>
<p>条件类型、分布式条件类型</p>
</li>
<li>
<p>infer 关键字</p>
</li>
<li>
<p>工具类型</p>
</li>
<li>
<p>TypeScript 4.x 新特性</p>
</li>
</ul>
<h2 data-id="heading-2">泛型</h2>
<p>之所以上来就放泛型，是因为在 TypeScript 的整个类型编程体系中，它是最基础的那部分，所有的进阶类型都基于它书写。就像编程时我们不能没有变量，类型编程中的变量就是泛型。</p>
<p>假设我们有这么一个函数：</p>
<pre><code class="copyable">function foo(args: unknown): unknown &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>如果它接收一个字符串，返回这个字符串的部分截取。</p>
</li>
<li>
<p>如果接收一个数字，返回这个数字的 n 倍。</p>
</li>
<li>
<p>如果接收一个对象，返回键值被更改过的对象（键名不变）。</p>
</li>
</ul>
<p><strong>上面这些场景有一个共同点，即函数的返回值与入参是同一类型.</strong></p>
<p>如果在这里要获得精确地类型定义，应该怎么做？</p>
<ul>
<li>
<p>把 <code>unknown</code> 替换为 <code>string | number | object</code> ？但这样代表的意思是这个函数接受任何值，其返回类型都可能是 string / number / object，虽然有了类型定义，但完全称不上是精确。</p>
</li>
</ul>
<p>别忘记我们需要的是 <strong>入参与返回值类型相同</strong> 的效果。这个时候<strong>泛型</strong>就该登场了，我们先用一个泛型收集参数的类型值，再将其作为返回值，就像这样：</p>
<pre><code class="copyable">function foo<T>(arg: T): T &#123;
  return arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在我们使用 <code>foo</code> 函数时，编辑器就能实时根据我们传入的参数确定此函数的返回值了。就像编程时，程序中变量的值会在其运行时才被确定，泛型的值（类型）也是在方法被调用、类被实例化等类似的执行过程实际发生时才会被确定的。</p>
<p>泛型使得代码段的类型定义<strong>易于重用</strong>（比如后续又多了一种接收 <code>boolean</code> 返回 <code>boolean</code> 的函数实现），并提升了灵活性与严谨性。</p>
<p>另外，你可能曾经见过 <code>Array<number></code> <code>Map<string, ValueType></code> 这样的使用方式，通常我们将上面例子中 <code>T</code> 这样的未赋值形式成为 <strong>类型参数变量</strong> 或者说 <strong>泛型类型</strong>，而将 <code>Array<number></code> 这样已经实例化完毕的称为 <code>实际类型参数</code> 或者是 <strong>参数化类型</strong>。</p>
<blockquote>
<p>通常泛型只会使用单个字母。如 T U K V S等。我的推荐做法是在项目达到一定复杂度后，使用带有具体意义的泛型变量声明，如 <code>BasicBusinessType</code> 这种形式。</p>
</blockquote>
<pre><code class="copyable">foo<string>("linbudu");
const [count, setCount] = useState<number>(1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子也可以不指定，因为 TS 会自动推导出泛型的实际类型，在部分 Lint 规则中，实际上也不推荐添加能够被自动推导出的类型值。</p>
<p>泛型在箭头函数下的书写：</p>
<pre><code class="copyable">const foo = <T>(arg: T) => arg;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果你在 TSX 文件中这么写，<code><T></code>可能会被识别为 JSX 标签，因此需要显式告知编译器：</p>
<pre><code class="copyable">const foo = <T extends SomeBasicType>(arg: T) => arg;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>除了用在函数中，泛型也可以在类中使用：</p>
<pre><code class="copyable">class Foo<T, U> &#123;
  constructor(public arg1: T, public arg2: U) &#123;&#125;

  public method(): T &#123;
    return this.arg1;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单独对于泛型的介绍就到这里（因为单纯的讲泛型实在没有什么好讲的），在接下来的进阶类型篇章中，我们会讲解更多泛型的使用。</p>
<h2 data-id="heading-3">类型守卫、is in关键字</h2>
<p>我们来从相对简单直观的知识点：类型守卫 开始，由浅入深的了解基于泛型的类型编程。</p>
<p>假设有这么一个字段，它可能字符串也可能是数字：</p>
<pre><code class="copyable">numOrStrProp: number | string;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在在使用时，你想将这个字段的联合类型缩小范围，比如精确到<code>string</code>，你可能会这么写：</p>
<pre><code class="copyable">export const isString = (arg: unknown): boolean => typeof arg === "string";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看这么写的效果：</p>
<pre><code class="copyable">function useIt(numOrStr: number | string) &#123;
  if (isString(numOrStr)) &#123;
    console.log(numOrStr.length);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c852f78788544b23831e907efaaf4d80~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看起来 <code>isString</code> 函数并没有起到缩小类型范围的作用，参数依然是联合类型。这个时候就该使用 <code>is</code> 关键字了：</p>
<pre><code class="copyable">export const isString = (arg: unknown): arg is string =>
  typeof arg === "string";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候再去使用，就会发现在 <code>isString(numOrStr)</code> 为 <code>true</code>后，<code>numOrStr</code>的类型就被缩小到了<code>string</code>。这只是以原始类型为成员的联合类型，我们完全可以扩展到各种场景上，先看一个简单的假值判断：</p>
<pre><code class="copyable">export type Falsy = false | "" | 0 | null | undefined;

export const isFalsy = (val: unknown): val is Falsy => !val;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这应该是我日常用的最多的类型别名之一了，类似的，还有 <code>isPrimitive</code> 、<code>isFunction</code>这样的类型守卫。</p>
<p>而使用 in 关键字，我们可以进一步收窄类型（<code>Type Narrowing</code>），思考下面这个例子，要如何将 " A | B " 的联合类型缩小到"A"？</p>
<pre><code class="copyable">class A &#123;
  public a() &#123;&#125;

  public useA() &#123;
    return "A";
  &#125;
&#125;

class B &#123;
  public b() &#123;&#125;

  public useB() &#123;
    return "B";
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先联想下 <code>for...in</code> 循环，它遍历对象的属性名，而 <code>in</code> 关键字也是一样，它能够判断一个属性是否为对象所拥有：</p>
<pre><code class="copyable">function useIt(arg: A | B): void &#123;
  'a' in arg ? arg.useA() : arg.useB();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果参数中存在<code>a</code>属性，由于A、B两个类型的交集并不包含a，所以这样能立刻收窄类型判断到 A 身上。</p>
<p>由于A、B两个类型的交集并不包含 a 这个属性，所以这里的 <code>in</code> 判断会精确地将类型对应收窄到三元表达式的前后。即 A 或者 B。</p>
<p>再看一个使用字面量类型作为类型守卫的例子：</p>
<pre><code class="copyable">interface IBoy &#123;
  name: "mike";
  gf: string;
&#125;

interface IGirl &#123;
  name: "sofia";
  bf: string;
&#125;

function getLover(child: IBoy | IGirl): string &#123;
  if (child.name === "mike") &#123;
    return child.gf;
  &#125; else &#123;
    return child.bf;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>关于字面量类型<code>literal types</code>，它是对类型的进一步限制，比如你的状态码只可能是 0/1/2，那么你就可以写成 <code>status: 0 | 1 | 2</code> 的形式，而不是用一个 <code>number</code> 来表达。</p>
<p>字面量类型包括 <strong>字符串字面量</strong>、<strong>数字字面量</strong>、<strong>布尔值字面量</strong>，以及4.1版本引入的模板字面量类型（这个我们会在后面展开讲解）。</p>
<ul>
<li>
<p>字符串字面量，常见如 <code>mode: "dev" | "prod"</code>。</p>
</li>
<li>
<p>布尔值字面量通常与其他字面量类型混用，如 <code>open: true | "none" | "chrome"</code>。</p>
</li>
</ul>
<p>这一类细碎的基础知识会被穿插在文中各个部分进行讲解，以此避免单独讲解时缺少特定场景让相关概念显得过于单调。</p>
</blockquote>
<h3 data-id="heading-4">基于字段区分接口</h3>
<p>我在日常经常看到有同学在问类似的问题：登录与未登录下的用户信息是完全不同的接口，或者是</p>
<p>之前有个小哥问过一个问题，我想很多用 TS 写接口的小伙伴可能都遇到过，即登录与未登录下的用户信息是完全不同的接口（或者是类似的，需要基于属性、字段来区分不同接口），其实也可以使用 <code>in</code>关键字 解决：</p>
<pre><code class="copyable">interface ILogInUserProps &#123;
  isLogin: boolean;
  name: string;
&#125;

interface IUnLoginUserProps &#123;
  isLogin: boolean;
  from: string;
&#125;

type UserProps = ILogInUserProps | IUnLoginUserProps;

function getUserInfo(user: ILogInUserProps | IUnLoginUserProps): string &#123;
  return 'name' in user ? user.name : user.from;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者通过字面量类型：</p>
<pre><code class="copyable">interface ICommonUserProps &#123;
  type: "common",
  accountLevel: string
&#125;

interface IVIPUserProps &#123;
  type: "vip";
  vipLevel: string;
&#125;

type UserProps = ICommonUserProps | IVIPUserProps;

function getUserInfo(user: ICommonUserProps | IVIPUserProps): string &#123;
  return user.type === "common" ? user.accountLevel : user.vipLevel;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的思路，还可以使用<code>instanceof</code>来进行实例的类型守卫，建议聪明的你动手尝试下。</p>
<h2 data-id="heading-5">索引类型与映射类型</h2>
<h3 data-id="heading-6">索引类型</h3>
<p>在阅读这一部分前，你需要做好思维转变的准备，需要真正认识到 <strong>类型编程实际也是编程</strong>，因为从这里开始，我们就将真正将泛型作为变量进行各种花式操作了。</p>
<p>就像你写业务代码的时候常常会遍历一个对象，而在类型编程中我们也会经常遍历一个接口。因此，你完全可以将一部分编程思路复用过来。首先实现一个简单的函数，它返回一个对象的某个键值：</p>
<pre><code class="copyable">// 假设key是obj键名
function pickSingleValue(obj, key) &#123;
  return obj[key];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要为其进行类型定义的话，有哪些需要定义的地方？</p>
<ul>
<li>
<p>参数<code>obj</code></p>
</li>
<li>
<p>参数<code>key</code></p>
</li>
<li>
<p>返回值</p>
</li>
</ul>
<p>这三样之间存在着一定关联：</p>
<ul>
<li>
<p><code>key</code>必然是 <code>obj</code> 中的键值名之一，且一定为 <code>string</code> 类型（通常我们只会使用字符串作为对象键名）</p>
</li>
<li>
<p>返回的值一定是 <strong>obj 中的键值</strong></p>
</li>
</ul>
<p>因此我们初步得到这样的结果：</p>
<pre><code class="copyable">function pickSingleValue<T>(obj: T, key: keyof T) &#123;
  return obj[key];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>keyof</code> 是 <strong>索引类型查询</strong> 的语法， 它会返回后面跟着的类型参数的键值组成的字面量联合类型，举个例子：</p>
<pre><code class="copyable">interface foo &#123;
  a: number;
  b: string;
&#125;

type A = keyof foo; // "a" | "b"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是就像 <code>Object.keys()</code> 一样？区别就在于它返回的是联合类型。</p>
<blockquote>
<p>联合类型 <code>Union Type</code> 通常使用 <code>|</code> 语法，代表多个可能的取值，实际上在最开始我们就已经使用过了。联合类型最主要的使用场景还是 条件类型 部分，这在后面会有一个完整的章节来进行讲解。</p>
</blockquote>
<p>还少了返回值，如果你此前没有接触过此类语法，应该会卡住，我们先联想下<code>for...in</code>语法，遍历对象时我们可能会这么写：</p>
<pre><code class="copyable">const fooObj = &#123; a: 1, b: "1" &#125;;

for (const key in fooObj) &#123;
  console.log(key);
  console.log(fooObj[key]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和上面的写法一样，我们拿到了 key，就能拿到对应的 value，那么 value 的类型就更简单了：</p>
<pre><code class="copyable">function pickSingleValue<T>(obj: T, key: keyof T): T[keyof T] &#123;
  return obj[key];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这一部分可能不好一步到位理解，解释下：</p>
<pre><code class="copyable">interface T &#123;
 a: number;
 b: string;
&#125;

type TKeys = keyof T; // "a" | "b"

type PropAType = T["a"]; // number
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你用键名可以取出对象上的键值，自然也就可以取出接口上的键值（也就是类型）啦~</p>
</blockquote>
<p>但这种写法很明显有可以改进的地方：<code>keyof</code>出现了两次，以及泛型 T 其实应该被限制为对象类型。对于第一点，就像我们平时编程会做的那样：用一个变量把多处出现的存起来，记得，<strong>在类型编程里，泛型就是变量</strong>。</p>
<pre><code class="copyable">function pickSingleValue<T extends object, U extends keyof T>(
  obj: T,
  key: U
): T[U] &#123;
  return obj[key];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里又出现了新东西 <code>extends</code>... 它是啥？你可以暂时把 <code>T extends object</code> 理解为<strong>T 被限制为对象类型</strong>，<code>U extends keyof T</code>理解为 泛型 U 必然是泛型 T 的键名组成的联合类型（以字面量类型的形式，比如T这个对象的键名包括a b c，那么U的取值只能是"a" "b" "c"之一，即 <code>"a" | "b" | "c"</code>）。具体细节我们会在 条件类型 一章讲到。</p>
</blockquote>
<p>假设现在不只要取出一个值了，我们要取出一系列值，即参数 2 将是一个数组，成员均为参数 1 的键名组成：</p>
<pre><code class="copyable">function pick<T extends object, U extends keyof T>(obj: T, keys: U[]): T[U][] &#123;
  return keys.map((key) => obj[key]);
&#125;

// pick(obj, ['a', 'b'])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有两个重要变化：</p>
<ul>
<li>
<p><code>keys: U[]</code> 我们知道 U 是 T 的键名组成的联合类型，那么要表示一个内部元素均是 T 键名的数组，就可以使用这种方式，具体的原理请参见下文的 <strong>分布式条件类型</strong> 章节。</p>
</li>
<li>
<p><code>T[U][]</code> 它的原理实际上和上面一条相同，首先是<code>T[U]</code>，代表参数1的键值（就像<code>Object[Key]</code>），我认为它是一个很好地例子，表现了 TS 类型编程的组合性，你不感觉这种写法就像搭积木一样吗？</p>
</li>
</ul>
<h4 data-id="heading-7">索引签名 Index Signature</h4>
<p>在JavaScript中，我们通常使用 <code>arr[1]</code> 的方式索引数组，使用 <code>obj[key]</code> 的方式索引对象。说白了，索引就是你获取一个对象成员的方式，而在类型编程中，索引签名用于快速建立一个内部字段类型相同的接口，如</p>
<pre><code class="copyable">interface Foo &#123;
  [keys: string]: string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么接口 Foo 实际上等价于一个键值全部为 string 类型，不限制成员的接口。</p>
<blockquote>
<p>等同于<code>Record<string, string></code>，见 工具类型。</p>
</blockquote>
<p>值得注意的是，由于 JS 可以同时通过数字与字符串访问对象属性，因此<code>keyof Foo</code>的结果会是<code>string | number</code>。</p>
<blockquote>
<pre><code class="copyable">const o: Foo = &#123;
 1: "芜湖！",
&#125;;

o[1] === o["1"]; // true
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>但是一旦某个接口的索引签名类型为<code>number</code>，那么使用它的对象就不能再通过字符串索引访问，如<code>o['1']</code>，将会抛出错误， <strong>元素隐式具有 "any" 类型，因为索引表达式的类型不为 "number"。</strong></p>
<h3 data-id="heading-8">映射类型 Mapped Types</h3>
<p>在开始映射类型前，首先想想 JavaScript 中数组的 map 方法，通过使用map，我们从一个数组按照既定的映射关系获得一个新的数组。在类型编程中，我们则会从一个类型定义（包括但不限于接口、类型别名）映射得到一个新的类型定义。通常会在旧有类型的基础上进行改造，如：</p>
<ul>
<li>
<p>修改原接口的键值类型</p>
</li>
<li>
<p>为原接口键值类型新增修饰符，如 <code>readonly</code> 与 可选<code>?</code></p>
</li>
</ul>
<p>从一个简单场景入手：</p>
<pre><code class="copyable">interface A &#123;
  a: boolean;
  b: string;
  c: number;
  d: () => void;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们有个需求，实现一个接口，它的字段与接口 A 完全相同，但是其中的类型全部为 <code>string</code>，你会怎么做？直接重新声明一个然后手写吗？这样就很离谱了，我们可是机智的程序员。</p>
<p>如果把接口换成对象再想想，假设要拷贝一个对象（假设没有嵌套，不考虑引用类型变量存放地址），常用的方式是首先 new 一个新的空对象，然后遍历原先对象的键值对来填充新对象。而接口其实也一样：</p>
<pre><code class="copyable">type StringifyA<T> = &#123;
  [K in keyof T]: string;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很熟悉？重要的就是这个<code>in</code>操作符，你完全可以把它理解为 <code>for...in</code>/<code>for...of</code> 这种遍历的思路，获取到键名之后，键值就简单了，所以我们可以很容易的拷贝一个新的类型别名出来。</p>
<pre><code class="copyable">type ClonedA<T> = &#123;
  [K in keyof T]: T[K];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>掌握这种思路，其实你已经接触到一些工具类型的底层实现了：</p>
<blockquote>
<p>你可以把工具类型理解为<strong>你平时放在 utils 文件夹下的公共函数，提供了对公用逻辑（在这里则是类型编程逻辑）的封装</strong>，比如上面的两个类型接口就是。关于更多工具类型，参考 工具类型 一章。</p>
</blockquote>
<p>先写个最常用的 <code>Partial</code>尝尝鲜，工具类型的详细介绍我们会在专门的章节展开：</p>
<pre><code class="copyable">// 将接口下的字段全部变为可选的
type Partial<T> = &#123;
  [K in keyof T]?: T[k];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>key?: value</code> 意为这一字段是可选的，在大部分情况下等同于 <code>key: value | undefined</code>。</p>
</blockquote>
<h2 data-id="heading-9">条件类型 Conditional Types</h2>
<p>在编程中遇到条件判断，我们常用 If 语句与三元表达式实现，我个人偏爱后者，即使是：</p>
<pre><code class="copyable">if (condition) &#123;
  execute()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种没有 else 的 If 语句，我也习惯写成：</p>
<pre><code class="copyable">condition ? execute() : void 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 条件类型 的语法，实际上就是三元表达式，看一个最简单的例子：</p>
<pre><code class="copyable">T extends U ? X : Y
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果你觉得这里的 extends 不太好理解，可以暂时简单理解为 U 中的属性在 T 中都有。</p>
</blockquote>
<p>为什么会有条件类型？可以看到 条件类型 通常是和 泛型 一同使用的，联想到泛型的使用场景以及值得延迟推断，我想你应该明白了些什么。对于类型无法即时确定的场景，使用 条件类型 来在运行时动态的确定最终的类型（运行时可能不太准确，或者可以理解为，你提供的函数被他人使用时，根据他人使用时传入的参数来动态确定需要被满足的类型约束）。</p>
<p>类比到编程语句中，其实就是根据条件判断来动态的赋予变量值：</p>
<pre><code class="copyable">let unknownVar: string;

unknownVar = condition ? "淘系前端" : "淘宝FED";

type LiteralType<T> = T extends string ? "foo" : "bar";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>条件类型理解起来其实也很直观，唯一需要有一定理解成本的就是 <strong>何时条件类型系统会收集到足够的信息来确定类型</strong>，也就是说，条件类型有时不会立刻完成判断，比如工具库提供的函数，需要用户在使用时传入参数才会完成 条件类型 的判断。</p>
<p>在了解这一点前，我们先来看看条件类型常用的一个场景：<strong>泛型约束</strong>，实际上就是我们上面 索引类型 的例子：</p>
<pre><code class="copyable">function pickSingleValue<T extends object, U extends keyof T>(
  obj: T,
  key: U
): T[U] &#123;
  return obj[key];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>T extends object</code> 与 <code>U extends keyof T</code> 都是泛型约束，分别<strong>将 T 约束为对象类型</strong> 和 <strong>将 U 约束为 T 键名的字面量联合类型</strong>（不记得了？提示：<code>1 | 2 | 3</code>）。我们通常使用泛型约束来 <strong>收窄类型约束</strong>，简单的说，泛型本身是来者不拒的，所有类型都能被 <strong>显式传入</strong>（如 <code>Array<number></code>） 或者 <strong>隐式推导</strong> （如 <code>foo(1)</code>），这样其实不是我们想要的，就像我们有时会检测函数的参数：</p>
<pre><code class="copyable">function checkArgFirst(arg)&#123;
  if(typeof arg !== "number")&#123;
    throw new Error("arg must be number type!")
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 TS 中，我们通过泛型约束，要求传入的泛型只能是固定的类型，如 <code>T extends &#123;&#125;</code> 约束泛型至对象类型，<code>T extends number | string</code>将泛型约束至数字与字符串类型。</p>
<p>以一个使用条件类型作为函数返回值类型的例子：</p>
<pre><code class="copyable">declare function strOrNum<T extends boolean>(
  x: T
): T extends true ? string : number;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，条件类型的推导就会被延迟，因为此时类型系统没有足够的信息来完成判断。</p>
<p>只有给出了所需信息（在这里是入参 x 的类型），才可以完成推导。</p>
<pre><code class="copyable">const strReturnType = strOrNum(true);
const numReturnType = strOrNum(false);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，就像三元表达式可以嵌套，条件类型也可以嵌套，如果你看过一些框架源码，也会发现其中存在着许多嵌套的条件类型，无他，条件类型可以将类型约束收拢到非常窄的范围内，提供精确的条件类型，如：</p>
<pre><code class="copyable">type TypeName<T> = T extends string
  ? "string"
  : T extends number
  ? "number"
  : T extends boolean
  ? "boolean"
  : T extends undefined
  ? "undefined"
  : T extends Function
  ? "function"
  : "object";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">分布式条件类型 Distributive Conditional Types</h3>
<p>分布式条件类型实际上不是一种特殊的条件类型，而是其特性之一（所以说条件类型的分布式特性更为准确）。我们直接先上概念： <strong>对于属于裸类型参数的检查类型，条件类型会在实例化时期自动分发到联合类型上</strong>。</p>
<blockquote>
<p>原文:</p>
<p>Conditional types in which the checked type is a <strong>naked type parameter</strong> are called distributive conditional types. Distributive conditional types are automatically <strong>distributed over union types</strong> during instantiation</p>
</blockquote>
<p>先提取几个关键词，然后我们再通过例子理清这个概念：</p>
<ul>
<li>
<p><strong>裸类型参数</strong>（类型参数即泛型，见文章开头的泛型章节介绍）</p>
</li>
<li>
<p><strong>实例化</strong></p>
</li>
<li>
<p><strong>分发到联合类型</strong></p>
<p>// 使用上面的TypeName类型别名</p>
<p>// "string" | "function"
type T1 = TypeName<string | (() => void)>;</p>
<p>// "string" | "object"
type T2 = TypeName<string | string[]>;</p>
<p>// "object"
type T3 = TypeName<string[] | number[]>;</p>
</li>
</ul>
<p>我们发现在上面的例子里，条件类型的推导结果都是联合类型（T3 实际上也是，只不过因为结果相同所以被合并了），并且其实就是类型参数被依次进行条件判断后，再使用<code>|</code>组合得来的结果。</p>
<p>是不是 get 到了一点什么？上面的例子中泛型都是裸露着的，如果被包裹着，其条件类型判断结果会有什么变化吗？我们再看另一个例子：</p>
<pre><code class="copyable">type Naked<T> = T extends boolean ? "Y" : "N";
type Wrapped<T> = [T] extends [boolean] ? "Y" : "N";

// "N" | "Y"
type Distributed = Naked<number | boolean>;

// "N"
type NotDistributed = Wrapped<number | boolean>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>其中，Distributed类型别名，其类型参数（<code>number | boolean</code>）会正确的分发，即<br>
先分发到 <code>Naked<number> | Naked<boolean></code>，再进行判断，所以结果是<code>"N" | "Y"</code>。</p>
</li>
<li>
<p>而 NotDistributed 类型别名，第一眼看上去感觉TS应该会自动按数组进行分发，结果应该也是 <code>"N" | "Y"</code> ？但实际上，它的类型参数（<code>number | boolean</code>）不会有分发流程，直接进行<code>[number | boolean] extends [boolean]</code>的判断，所以结果是<code>"N"</code>。</p>
</li>
</ul>
<p>现在我们可以来讲讲这几个概念了：</p>
<ul>
<li>
<p>裸类型参数，没有额外被<code>[]</code>包裹过的，就像被数组包裹后就不能再被称为裸类型参数。</p>
</li>
<li>
<p>实例化，其实就是条件类型的判断过程，就像我们前面说的，条件类型需要在收集到足够的推断信息之后才能进行这个过程。在这里两个例子的实例化过程实际上是不同的，具体会在下一点中介绍。</p>
</li>
<li>
<p>分发到联合类型：</p>
</li>
<li>
<p>对于 TypeName，它内部的类型参数 T 是没有被包裹过的，所以 <code>TypeName<string | (() => void)></code> 会被分发为 <code>TypeName<string> | TypeName<(() => void)></code>，然后再次进行判断，最后分发为<code>"string" | "function"</code>。</p>
</li>
<li>
<p>抽象下具体过程：</p>
<pre><code class="copyable">( A | B | C ) extends T ? X : Y
// 相当于
(A extends T ? X : Y) | (B extends T ? X : Y) | (B extends T ? X : Y)

// 使用[]包裹后，不会进行额外的分发逻辑。
[A | B | C] extends [T] ? X : Y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一句话概括：<strong>没有被 <code>[]</code> 额外包装的联合类型参数，在条件类型进行判定时会将联合类型分发，分别进行判断。</strong></p>
</li>
</ul>
<p>这两种行为没有好坏之分，区别只在于是否进行联合类型的分发，如果你需要走分布式条件类型，那么注意保持你的类型参数为裸类型参数。如果你想避免这种行为，那么使用 <code>[]</code> 包裹你的类型参数即可（注意在 <code>extends</code> 关键字的两侧都需要）。</p>
<h2 data-id="heading-11">infer 关键字</h2>
<p>在条件类型中，我们展示了如何通过条件判断来延迟确定类型，但仅仅使用条件类型也有一定不足：它无法从条件上得到类型信息。举例来说，<code>T extends Array<PrimitiveType> ? "foo" : "bar"</code>这一例子，我们不能从作为条件的 <code>Array<PrimitiveType></code> 中获取到 <code>PrimitiveType</code> 的实际类型。</p>
<p>而这样的场景又是十分常见的，如获取函数返回值的类型、拆箱Promise / 数组等，因此这一节我们来介绍下 <code>infer</code> 关键字。</p>
<p><code>infer</code>是 <code>inference</code> 的缩写，通常的使用方式是用于修饰作为类型参数的泛型，如： <code>infer R</code>，<code>R</code>表示 <strong>待推断的类型</strong>。通常 <code>infer</code>不会被直接使用，而是与条件类型一起，被放置在底层工具类型中。如果说条件类型提供了延迟推断的能力，那么加上 <code>infer</code> 就是提供了基于条件进行延迟推断的能力。</p>
<p>看一个简单的例子，用于获取函数返回值类型的工具类型<code>ReturnType</code>:</p>
<pre><code class="copyable">const foo = (): string => &#123;
  return "linbudu";
&#125;;

type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// string
type FooReturnType = ReturnType<typeof foo>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>(...args: any[]) => infer R</code> 是一个整体，这里函数的返回值类型的位置被 <code>infer R</code> 占据了。</p>
</li>
<li>
<p>当 <code>ReturnType</code> 被调用，类型参数 T 、R 被显式赋值（T为 <code>typeof foo</code>，<code>infer R</code>被整体赋值为<code>string</code>，即函数的返回值类型），如果 T 满足条件类型的约束，就返回 infer 完毕的R 的值，在这里 R 即为函数的返回值实际类型。</p>
</li>
<li>
<p>实际上为了严谨，应当约束泛型T为函数类型，即：</p>
<pre><code class="copyable">// 第一个 extends 约束可传入的泛型只能为函数类型
// 第二个 extends 作为条件判断
type ReturnType<T extends (...args: any[]) => any> = T extends (...args: any[]) => infer R ? R : never;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><code>infer</code>的使用思路可能不是那么好习惯，我们可以用前端开发中常见的一个例子类比，页面初始化时先显示占位交互，像 <code>Loading</code> / 骨架屏，在请求返回后再去渲染真实数据。<code>infer</code>也是这个思路，<strong>类型系统在获得足够的信息（通常来自于条件的延迟推断）后，就能将 infer 后跟随的类型参数推导出来</strong>，最后通常会返回这个推导结果。</p>
<p>类似的，借着这个思路我们还可以获得函数入参类型、类的构造函数入参类型、甚至 Promise 内部的类型等，这些工具类型我们会在后面讲到。</p>
<p>另外，对于 TS 中函数重载的情况，使用 infer （如上面的 <code>ReturnType</code>）不会为所有重载执行推导过程，只有最后一个重载（因为一般来说最后一个重载通常是最广泛的情况）会被使用。</p>
<h2 data-id="heading-12">工具类型 Tool Type</h2>
<p>这一章应该是本文“性价比”最高的一部分了，因为即使你在阅读完这部分后，还是不太懂这些工具类型是如何实现的，也不影响你把它用的恰到好处，就像 Lodash 不会要求你对每个使用的函数都熟知原理一样。</p>
<p>这一部分包括 <strong>TS 内置工具类型</strong> 与社区的 <strong>扩展工具类型</strong>，我个人推荐在完成学习后挑选一部分工具类型记录下来，比如你觉得比较有价值、现有或者未来业务可能会使用，或者仅仅是觉得很好玩的工具类型，并在自己的项目里新建一个<code>.d.ts</code>文件（或是 <code>/utils/tool-types.ts</code> 这样）存储它。</p>
<blockquote>
<p><strong>在继续阅读前，最好确保你掌握了上面的知识，它们是工具类型的基础。</strong></p>
</blockquote>
<h3 data-id="heading-13">内置工具类型</h3>
<p>在上面我们已经实现了内置工具类型中被使用最多的一个:</p>
<pre><code class="copyable">type Partial<T> = &#123;
  [K in keyof T]?: T[k];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它用于将一个接口中的字段全部变为可选，除了索引类型以及映射类型以外，它只使用了<code>?</code>可选修饰符，那么我现在直接掏出小抄：</p>
<ul>
<li>
<p>去除可选修饰符：<code>-?</code>，位置与 <code>?</code> 一致</p>
</li>
<li>
<p>只读修饰符：<code>readonly</code>，位置在键名，如 <code>readonly key: string</code></p>
</li>
<li>
<p>去除只读修饰符：<code>-readonly</code>，位置同<code>readonly</code>。</p>
</li>
</ul>
<p>恭喜，你得到了 <code>Required</code> 和 <code>Readonly</code>（去除 <code>readonly</code> 修饰符的工具类型不属于内置的，我们会在后面看到）:</p>
<pre><code class="copyable">type Required<T> = &#123;
  [K in keyof T]-?: T[K];
&#125;;

type Readonly<T> = &#123;
  readonly [K in keyof T]: T[K];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面我们实现了一个 pick 函数：</p>
<pre><code class="copyable">function pick<T extends object, U extends keyof T>(obj: T, keys: U[]): T[U][] &#123;
  return keys.map((key) => obj[key]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似的，假设我们现在需要从一个接口中挑选一些字段：</p>
<pre><code class="copyable">type Pick<T, K extends keyof T> = &#123;
  [P in K]: T[P];
&#125;;

// 期望用法
// 期望结果 A["a"]类型 | A["b"]类型
type Part = Pick<A, "a" | "b">;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是映射类型，只不过现在映射类型的映射源是传入给 <code>Pick</code> 的类型参数K。</p>
<p>既然有了<code>Pick</code>，那么自然要有<code>Omit</code>（一个是从对象中挑选部分，一个是排除部分），它和<code>Pick</code>的写法非常像，但有一个问题要解决：我们要怎么表示<code>T</code>中剔除了<code>K</code>后的剩余字段？</p>
<blockquote>
<p>Pick 选取传入的键值，Omit 移除传入的键值</p>
</blockquote>
<p>这里我们又要引入一个知识点：<code>never</code>类型，它表示永远不会出现的类型，通常被用来将<strong>收窄联合类型或是接口</strong>，或者作为条件类型判断的兜底。详细可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fsearch%3Ftype%3Dcontent%26q%3Dts%2520never" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/search?type=content&q=ts%20never" ref="nofollow noopener noreferrer">尤大的知乎回答</a>， 在这里我们不做展开介绍。</p>
<p>上面的场景其实可以简化为：</p>
<pre><code class="copyable">// "3" | "4" | "5"
type LeftFields = Exclude<"1" | "2" | "3" | "4" | "5", "1" | "2">;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Exclude，字面意思看起来是排除，那么第一个参数应该是要进行筛选的，第二个应该是筛选条件！先按着这个思路试试：</p>
<p><strong>这里实际上使用到了分布式条件类型的特性，假设 Exclude 接收 T U 两个类型参数，T 联合类型中的类型会依次与 U 类型进行判断，如果这个类型参数在 U 中，就剔除掉它（赋值为 never）</strong>。</p>
<blockquote>
<p>接地气的版本：<code>"1"</code>在 <code>"1" | "2"</code> 里面吗( <code>"1" extends "1"|"2" -> true</code> )？ 在的话，就剔除掉它（赋值为<code>never</code>），不在的话就保留。</p>
</blockquote>
<pre><code class="copyable">type Exclude<T, U> = T extends U ? never : T;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 Omit就很简单了，对原接口的成员，剔除掉传入的联合类型成员，应用 Pick 即可。</p>
<pre><code class="copyable">type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剧透下，<strong>几乎所有使用条件类型的场景，把判断后的赋值语句反一下，就会有新的场景</strong>，比如 <code>Exclude</code> 移除掉键名，那反一下就是保留键名：</p>
<pre><code class="copyable">type Extract<T, U> = T extends U ? T : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看个常用的工具类型 <code>Record<Keys, Type></code>，通常用于生成以联合类型为键名（<code>Keys</code>），键值类型为<code>Type</code>的新接口，比如：</p>
<pre><code class="copyable">type MyNav = "a" | "b" | "b";
interface INavWidgets &#123;
  widgets: string[];
  title?: string;
  keepAlive?: boolean;
&#125;
const router: Record<MyNav, INavWidgets> = &#123;
  a: &#123; widget: [""] &#125;,
  b: &#123; widget: [""] &#125;,
  c: &#123; widget: [""] &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实很简单，把 <code>Keys</code> 的每个键值拿出来，类型规定为 <code>Type</code> 即可</p>
<pre><code class="copyable">// K extends keyof any 约束K必须为联合类型
type Record<K extends keyof any, T> = &#123;
  [P in K]: T;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，Record也支持 <code>Record<string, unknown></code> 这样的使用方式， <code>string extends keyof any</code> 也是成立的，因为 <code>keyof</code> 的最终结果必然是 <code>string</code> 组成的联合类型（除了使用数字作为键名的情况...）。</p>
<p>在前面的 infer 一节中我们实现了用于获取函数返回值的<code>ReturnType</code>：</p>
<pre><code class="copyable">type ReturnType<T extends (...args: any) => any> = T extends (
  ...args: any
) => infer R
  ? R
  : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实把 infer 换个位置，比如放到入参处，它就变成了获取参数类型的<code>Parameters</code>:</p>
<pre><code class="copyable">type Parameters<T extends (...args: any) => any> = T extends (
  ...args: infer P
) => any
  ? P
  : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果再大胆一点，把普通函数换成类的构造函数，那么就得到了获取类构造函数入参类型的<code>ConstructorParameters</code>：</p>
<pre><code class="copyable">type ConstructorParameters<
  T extends new (...args: any) => any
> = T extends new (...args: infer P) => any ? P : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>加上<code>new</code>关键字来使其成为<strong>可实例化类型声明</strong>，即此处约束泛型为<strong>类</strong>。</p>
</blockquote>
<p>这个是获得类的构造函数入参类型，如果把待 infer 的类型放到其返回处，想想 new 一个类的返回值是什么？实例！所以我们得到了实例类型<code>InstanceType</code>：</p>
<pre><code class="copyable">type InstanceType<T extends new (...args: any) => any> = T extends new (
  ...args: any
) => infer R
  ? R
  : any;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这几个例子看下来，你应该已经 get 到了那么一丝天机，类型编程的确没有特别高深晦涩的语法，它考验的是你对其中基础部分如<strong>索引</strong>、<strong>映射</strong>、<strong>条件类型</strong>的掌握程度，以及举一反三的能力。下面我们要学习的社区工具类型，本质上还是各种基础类型的组合，只是从常见场景下出发，补充了官方没有覆盖到的部分。</p>
<h3 data-id="heading-14">社区工具类型</h3>
<blockquote>
<p>这一部分的工具类型大多来自于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpiotrwitek%2Futility-types" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/piotrwitek/utility-types" ref="nofollow noopener noreferrer">utility-types</a>，其作者同时还有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpiotrwitek%2Freact-redux-typescript-guide" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/piotrwitek/react-redux-typescript-guide" ref="nofollow noopener noreferrer">react-redux-typescript-guide</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpiotrwitek%2Ftypesafe-actions" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/piotrwitek/typesafe-actions" ref="nofollow noopener noreferrer">typesafe-actions</a> 这两个优秀作品。</p>
<p>同时，也推荐 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Ftype-fest" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/type-fest" ref="nofollow noopener noreferrer">type-fest</a> 这个库，和上面相比更加接地气一些。其作者的作品...，我保证你直接或间接的使用过（如果不信，一定要去看看，我刚看到的时候是真的震惊的不行）。</p>
</blockquote>
<p>我们由浅入深，先封装基础的类型别名和对应的类型守卫：</p>
<pre><code class="copyable">export type Primitive =
  | string
  | number
  | bigint
  | boolean
  | symbol
  | null
  | undefined;

export const isPrimitive = (val: unknown): val is Primitive => &#123;
  if (val === null || val === undefined) &#123;
    return true;
  &#125;

  const typeDef = typeof val;

  const primitiveNonNullishTypes = [
    "string",
    "number",
    "bigint",
    "boolean",
    "symbol",
  ];

  return primitiveNonNullishTypes.indexOf(typeDef) !== -1;
&#125;;

export type Nullish = null | undefined;

export type NonUndefined<A> = A extends undefined ? never : A;
// 实际上TS也内置了这个工具类型
type NonNullable<T> = T extends null | undefined ? never : T;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>Falsy</code>和 <code>isFalsy</code> 我们已经在上面体现过了。</p>
</blockquote>
<p>趁着对 infer 的记忆来热乎，我们再来看一个常用的场景，提取 Promise 的实际类型：</p>
<pre><code class="copyable">const foo = (): Promise<string> => &#123;
  return new Promise((resolve, reject) => &#123;
    resolve("linbudu");
  &#125;);
&#125;;

// Promise<string>
type FooReturnType = ReturnType<typeof foo>;

// string
type NakedFooReturnType = PromiseType<FooReturnType>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你已经熟练掌握了<code>infer</code>的使用，那么实际上是很好写的，只需要用一个<code>infer</code>参数作为 Promise 的泛型即可：</p>
<pre><code class="copyable">export type PromiseType<T extends Promise<any>> = T extends Promise<infer U>
  ? U
  : never;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>infer R</code> 来等待类型系统推导出<code>R</code>的具体类型。</p>
<h3 data-id="heading-15">递归的工具类型</h3>
<p>前面我们写了个<code>Partial</code> <code>Readonly</code> <code>Required</code>等几个对接口字段进行修饰的工具类型，但实际上都有局限性，如果接口中存在着嵌套呢？</p>
<pre><code class="copyable">type Partial<T> = &#123;
  [P in keyof T]?: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>理一下逻辑：</p>
<ul>
<li>
<p>如果不是对象类型，就只是加上<code>?</code>修饰符</p>
</li>
<li>
<p>如果是对象类型，那就<strong>遍历这个对象内部</strong></p>
</li>
<li>
<p>重复上述流程。</p>
</li>
</ul>
<p>是否是对象类型的判断我们见过很多次了, <code>T extends object</code>即可，那么如何遍历对象内部？实际上就是递归。</p>
<pre><code class="copyable">export type DeepPartial<T> = &#123;
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>utility-types</code>内部的实现实际比这个复杂，还考虑了数组的情况，这里为了便于理解做了简化，后面的工具类型也同样存在此类简化。</p>
</blockquote>
<p>那么<code>DeepReadobly</code>、 <code>DeepRequired</code>也就很简单了：</p>
<pre><code class="copyable">export type DeepMutable<T> = &#123;
  -readonly [P in keyof T]: T[P] extends object ? DeepMutable<T[P]> : T[P];
&#125;;

// 即DeepReadonly
export type DeepImmutable<T> = &#123;
  +readonly [P in keyof T]: T[P] extends object ? DeepImmutable<T[P]> : T[P];
&#125;;

export type DeepRequired<T> = &#123;
  [P in keyof T]-?: T[P] extends object | undefined ? DeepRequired<T[P]> : T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尤其注意下<code>DeepRequired</code>，它的条件类型判断的是 <code>T[P] extends object | undefined</code>，因为嵌套的对象类型可能是可选的（undefined），如果仅使用object，可能会导致错误的结果。</p>
<p>另外一种省心的方式是不进行条件类型的判断，直接全量递归所有属性~</p>
<h3 data-id="heading-16">返回键名的工具类型</h3>
<p>在有些场景下我们需要一个工具类型，它返回接口字段键名组成的联合类型，然后用这个联合类型进行进一步操作（比如给 Pick 或者 Omit 这种使用），一般键名会符合特定条件，比如：</p>
<ul>
<li>
<p>可选/必选/只读/非只读的字段</p>
</li>
<li>
<p>（非）对象/（非）函数/类型的字段</p>
</li>
</ul>
<p>来看个最简单的函数类型字段<code>FunctionTypeKeys</code>：</p>
<pre><code class="copyable">export type FunctTypeKeys<T extends object> = &#123;
  [K in keyof T]-?: T[K] extends Function ? K : never;
&#125;[keyof T];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>&#123;[K in keyof T]: ... &#125;[keyof T]</code>这个写法可能有点诡异，拆开来看：</p>
<pre><code class="copyable">interface IWithFuncKeys &#123;
  a: string;
  b: number;
  c: boolean;
  d: () => void;
&#125;

type WTFIsThis<T extends object> = &#123;
  [K in keyof T]-?: T[K] extends Function ? K : never;
&#125;;

type UseIt1 = WTFIsThis<IWithFuncKeys>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很容易推导出 <code>UseIt1</code> 实际上就是：</p>
<pre><code class="copyable">type UseIt1 = &#123;
  a: never;
  b: never;
  c: never;
  d: "d";
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>UseIt</code>会保留所有字段，满足条件的字段其键值为字面量类型（即键名），不满足的则为never。</p>
</blockquote>
<p>加上后面一部分：</p>
<pre><code class="copyable">// "d"
type UseIt2 = UseIt1[keyof UseIt1];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个过程类似排列组合：<code>never</code>类型的值不会出现在联合类型中</p>
<blockquote>
<pre><code class="copyable">// never类型会被自动去除掉 string | number
type WithNever = string | never | number;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>所以<code>&#123; [K in keyof T]: ... &#125;[keyof T]</code>这个写法实际上就是为了返回键名（准备的说，是<strong>键名组成的联合类型</strong>）。</p>
<p>那么非函数类型字段也很简单了，这里就不做展示了，下面来看可选字段<code>OptionalKeys</code>与必选字段<code>RequiredKeys</code>，先来看个小例子：</p>
<pre><code class="copyable">type WTFAMI1 = &#123;&#125; extends &#123; prop: number &#125; ? "Y" : "N";
type WTFAMI2 = &#123;&#125; extends &#123; prop?: number &#125; ? "Y" : "N";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果能绕过来，很容易就能得出来答案。如果一时没绕过去，也很简单，对于前面一个情况，<code>prop</code>是必须的，因此空对象 <code>&#123;&#125;</code> 并不能满足<code>extends &#123; prop: number &#125;</code>，而对于prop为可选的情况下则可以。</p>
<p>因此，我们使用这种思路来得到可选/必选的键名。</p>
<ul>
<li>
<p><code>&#123;&#125; extends Pick<T, K></code>，如果<code>K</code>是可选字段，那么就留下（OptionalKeys，如果是 RequiredKeys 就剔除）。</p>
</li>
<li>
<p>怎么剔除？当然是用<code>never</code>了。</p>
<p>export type RequiredKeys = &#123;
[K in keyof T]-?: &#123;&#125; extends Pick<T, K> ? never : K;
&#125;[keyof T];</p>
</li>
</ul>
<p>这里是剔除可选字段，那么 OptionalKeys 就是保留了：</p>
<pre><code class="copyable">export type OptionalKeys<T> = &#123;
  [K in keyof T]-?: &#123;&#125; extends Pick<T, K> ? K : never;
&#125;[keyof T];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只读字段<code>IMmutableKeys</code>与非只读字段<code>MutableKeys</code>的思路类似，即先获得：</p>
<pre><code class="copyable">interface MutableKeys &#123;
  readonlyKeys: never;
  notReadonlyKeys: "notReadonlyKeys";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再获得不为<code>never</code>的字段名即可。</p>
<p>这里还是要表达一下对作者的敬佩，属实巧妙啊，首先定义一个工具类型<code>IfEqual</code>，比较两个类型是否相同，甚至可以比较修饰前后的情况下，也就是这里只读与非只读的情况。</p>
<pre><code class="copyable">type Equal<X, Y, A = X, B = never> = (<T>() => T extends X ? 1 : 2) extends <
  T
>() => T extends Y ? 1 : 2
  ? A
  : B;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>不要被<code><T>() => T extends X ? 1 : 2</code>干扰，可以理解为就是用于比较的包装，这一层包装能够区分出来只读与非只读属性。即 <code>(<T>() => T extends X ? 1 : 2)</code> 这一部分，只有在类型参数 <code>X</code> 完全一致时，两个 <code>(<T>() => T extends X ? 1 : 2)</code> ` 才会是全等的，这个一致要求只读性、可选性等修饰也要一致。</p>
</li>
<li>
<p>实际使用时（以非只读的情况为例），我们为 X 传入接口，为 Y 传入去除了只读属性<code>-readonly</code>的接口，使得所有键都被进行一次与去除只读属性的键的比较。为 A 传入字段名，B 这里我们需要的就是 never，因此可以不填。</p>
</li>
</ul>
<p>实例：</p>
<pre><code class="copyable">export type MutableKeys<T extends object> = &#123;
  [P in keyof T]-?: Equal<
    &#123; [Q in P]: T[P] &#125;,
    &#123; -readonly [Q in P]: T[P] &#125;,
    P,
    never
  >;
&#125;[keyof T];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>几个容易绕弯子的点：</p>
<ul>
<li>
<p>泛型 Q 在这里不会实际使用，只是映射类型的字段占位。</p>
</li>
<li>
<p>X 、 Y 同样存在着 <strong>分布式条件类型</strong>， 来依次比对字段去除 readonly 前后。</p>
</li>
</ul>
<p>同样的有：</p>
<pre><code class="copyable">export type IMmutableKeys<T extends object> = &#123;
  [P in keyof T]-?: Equal<
    &#123; [Q in P]: T[P] &#125;,
    &#123; -readonly [Q in P]: T[P] &#125;,
    never,
    P
  >;
&#125;[keyof T];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>这里不是对<code>readonly</code>修饰符操作，而是调换条件类型的判断语句。</p>
</li>
</ul>
<h3 data-id="heading-17">基于值类型的 Pick 与 Omit</h3>
<p>前面我们实现的 Pick 与 Omit 是基于键名的，假设现在我们需要按照值类型来做选取剔除呢？</p>
<p>其实很简单，就是<code>T[K] extends ValueType</code>即可：</p>
<pre><code class="copyable">export type PickByValueType<T, ValueType> = Pick<
  T,
  &#123; [Key in keyof T]-?: T[Key] extends ValueType ? Key : never &#125;[keyof T]
>;

export type OmitByValueType<T, ValueType> = Pick<
  T,
  &#123; [Key in keyof T]-?: T[Key] extends ValueType ? never : Key &#125;[keyof T]
>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>条件类型承担了太多...</p>
</blockquote>
<h3 data-id="heading-18">工具类型一览</h3>
<p>总结下我们上面书写的工具类型：</p>
<ul>
<li>
<p>全量修饰接口：<code>Partial</code> <code>Readonly(Immutable)</code> <code>Mutable</code> <code>Required</code>，以及对应的递归版本。</p>
</li>
<li>
<p>裁剪接口：<code>Pick</code> <code>Omit</code> <code>PickByValueType</code> <code>OmitByValueType</code></p>
</li>
<li>
<p>基于 infer：<code>ReturnType</code> <code>ParamType</code> <code>PromiseType</code></p>
</li>
<li>
<p>获取指定条件字段：<code>FunctionKeys</code> <code>OptionalKeys</code> <code>RequiredKeys</code> ...</p>
</li>
</ul>
<p><strong>需要注意的是，有时候单个工具类型并不能满足你的要求，你可能需要多个工具类型协作</strong>，比如用 <code>FunctionKeys</code> + <code>Pick</code> 得到一个接口中类型为函数的字段。</p>
<p><strong>另外，实际上上面的部分工具类型是可以用重映射能力实现的更加简洁优雅的，这不尝试下？</strong></p>
<p>受限于篇幅（本文到这里已经1.3w字了），本来还想放上来的 type-fest 的工具类型就只能遗憾退场了，但我还是建议大家去读一读它的源码。相比于上面的 utility-types 更加接地气，实现思路也更加有趣。</p>
<h2 data-id="heading-19">TypeScript 4.x 中的部分新特性</h2>
<p>这一部分是相对于之前的版本新增的部分，主要包括了4.1 - 4.4（Beta）版本中引入的一部分与本文介绍内容有关的新特性，包括 模板字面量类型 与 重映射。</p>
<h3 data-id="heading-20">模板字面量类型</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-1%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/" ref="nofollow noopener noreferrer">TypeScript 4.1</a> 中引入了模板字面量类型，使得我们可以使用<code>$&#123;&#125;</code> 这一语法来构造字面量类型，如：</p>
<pre><code class="copyable">type World = 'world';

// "hello world"
type Greeting = `hello $&#123;World&#125;`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模板字面量类型同样支持分布式条件类型，如：</p>
<pre><code class="copyable">export type SizeRecord<Size extends string> = `$&#123;Size&#125;-Record`

// "Small-Record"
type SmallSizeRecord = SizeRecord<"Small">
// "Middle-Record"
type MiddleSizeRecord = SizeRecord<"Middle">
// "Huge-Record"
type HugeSizeRecord = SizeRecord<"Huge">


// "Small-Record" | "Middle-Record" | "Huge-Record"
type UnionSizeRecord = SizeRecord<"Small" | "Middle" | "Huge">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有个有趣的地方，模板插槽（<code>$&#123;&#125;</code>）中可以传入联合类型，并且同一模板中如果存在多个插槽，各个联合类型将会被分别排列组合。</p>
<pre><code class="copyable">// "Small-Record" | "Small-Report" | "Middle-Record" | "Middle-Report" | "Huge-Record" | "Huge-Report"
type SizeRecordOrReport = `$&#123;"Small" | "Middle" | "Huge"&#125;-$&#123;"Record" | "Report"&#125;`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随之而来的还有四个新的工具类型：</p>
<pre><code class="copyable">type Uppercase<S extends string> = intrinsic;

type Lowercase<S extends string> = intrinsic;

type Capitalize<S extends string> = intrinsic;

type Uncapitalize<S extends string> = intrinsic;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它们的作用就是字面意思，不做解释了。相关的PR见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fpull%2F40336" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/TypeScript/pull/40336" ref="nofollow noopener noreferrer">40336</a>，作者Anders Hejlsberg 是 C# 与 Delphi 的首席架构师，同时也是TS的作者之一。</p>
<p><code>intrinsic</code>代表了这些工具类型是由 TS 编译器内部实现的，其实也很好理解，我们无法通过类型编程来改变字面量的值，但我想按照这个趋势，TS类型编程以后会支持调用 Lodash 方法也说不定。</p>
<blockquote>
<p>TS 的实现代码：</p>
<pre><code class="copyable">function applyStringMapping(symbol: Symbol, str: string) &#123;
 switch (intrinsicTypeKinds.get(symbol.escapedName as string)) &#123;
     case IntrinsicTypeKind.Uppercase: return str.toUpperCase();
     case IntrinsicTypeKind.Lowercase: return str.toLowerCase();
     case IntrinsicTypeKind.Capitalize: return str.charAt(0).toUpperCase() + str.slice(1);
     case IntrinsicTypeKind.Uncapitalize: return str.charAt(0).toLowerCase() + str.slice(1);
 &#125;
 return str;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>你可能会想到，模板字面量如果想截取其中的一部分要怎么办？这里可没法调用 slice 方法。其实思路就在我们上面提到过的 infer，使用 infer 占位后，便能够提取出字面量的一部分，如：</p>
<pre><code class="copyable">type CutStr<Str extends string> = Str extends `$&#123;infer Part&#125;budu` ? Part : never

// "lin"
type Tmp = CutStr<"linbudu">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再进一步，<code>[1,2,3]</code>这样的字符串，如果我们提供 <code>[$&#123;infer Member1&#125;, $&#123;infer Member2&#125;, $&#123;infer Member&#125;]</code> 这样的插槽匹配，就可以实现神奇的提取字符串数组成员效果：</p>
<pre><code class="copyable">type ExtractMember<Str extends string> = Str extends `[$&#123;infer Member1&#125;, $&#123;infer Member2&#125;, $&#123;infer Member3&#125;]` ? [Member1, Member2, Member3] : unknown;

// ["1", "2", "3"]
type Tmp = ExtractMember<"[1, 2, 3]">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，这里的模板插槽被使用 <code>,</code> 分隔开了，如果多个带有 infer 的插槽紧挨在一起，那么前面的 infer 只会获得单个字符，最后一个 infer 会获得所有的剩余字符（如果有的话），比如我们把上面的例子改成这样：</p>
<pre><code class="copyable">type ExtractMember<Str extends string> = Str extends `[$&#123;infer Member1&#125;$&#123;infer Member2&#125;$&#123;infer Member3&#125;]` ? [Member1, Member2, Member3] : unknown;

// ["1", ",", " 2, 3"]
type Tmp = ExtractMember<"[1, 2, 3]">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一特性使得我们可以使用多个相邻的 infer + 插槽，对最后一个 infer获得的值进行递归操作，如：</p>
<pre><code class="copyable">type JoinArrayMember<T extends unknown[], D extends string> =
  T extends [] ? '' :
  T extends [any] ? `$&#123;T[0]&#125;` :
  T extends [any, ...infer U] ? `$&#123;T[0]&#125;$&#123;D&#125;$&#123;JoinArrayMember<U, D>&#125;` :
  string;

// ""
type Tmp1 = JoinArrayMember<[], '.'>;
// "1"
type Tmp3 = JoinArrayMember<[1], '.'>;
// "1.2.3.4"
type Tmp2 = JoinArrayMember<[1, 2, 3, 4], '.'>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理也很简单，每次将数组的第一个成员添加上<code>.</code>，在最后一个成员时不作操作，在最后一次匹配（<code>[]</code>）返回空字符串，即可。</p>
<p>又或者反过来？把 <code>1.2.3.4</code> 回归到数组形式？</p>
<pre><code class="copyable">type SplitArrayMember<S extends string, D extends string> =
  string extends S ? string[] :
  S extends '' ? [] :
  S extends `$&#123;infer T&#125;$&#123;D&#125;$&#123;infer U&#125;` ? [T, ...SplitArrayMember<U, D>] :
  [S];

type Tmp11 = SplitArrayMember<'foo', '.'>;  // ['foo']
type Tmp12 = SplitArrayMember<'foo.bar.baz', '.'>;  // ['foo', 'bar', 'baz']
type Tmp13 = SplitArrayMember<'foo.bar', ''>;  // ['f', 'o', 'o', '.', 'b', 'a', 'r']
type Tmp14 = SplitArrayMember<any, '.'>;  // stri
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，看到 <code>a.b.c</code> 这样的形式，你应该想到了 Lodash 的 get 方法，即通过 <code>get(&#123;&#125;,"a.b.c")</code> 的形式快速获得嵌套属性。但是这样要怎么提供类型声明？有了模板字面量类型后，只需要结合 infer + 条件类型即可。</p>
<pre><code class="copyable">type PropType<T, Path extends string> =
    string extends Path ? unknown :
    Path extends keyof T ? T[Path] :
    Path extends `$&#123;infer K&#125;.$&#123;infer R&#125;` ? K extends keyof T ? PropType<T[K], R> : unknown :
    unknown;

declare function getPropValue<T, P extends string>(obj: T, path: P): PropType<T, P>;
declare const s: string;

const obj = &#123; a: &#123; b: &#123;c: 42, d: 'hello' &#125;&#125;&#125;;
getPropValue(obj, 'a');  // &#123; b: &#123;c: number, d: string &#125; &#125;
getPropValue(obj, 'a.b');  // &#123;c: number, d: string &#125;
getPropValue(obj, 'a.b.d');  // string
getPropValue(obj, 'a.b.x');  // unknown
getPropValue(obj, s);  // unknown
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">重映射</h3>
<p>这一能力在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-1%2F%23key-remapping-mapped-types" target="_blank" rel="nofollow noopener noreferrer" title="https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/#key-remapping-mapped-types" ref="nofollow noopener noreferrer">TS 4.1</a> 中引入，提供了在映射类型中重定向映射源至新类型的能力，这里的新类型可以是工具类型的返回结果、字面量模板类型等，用于解决在使用映射类型时，我们想要过滤/新增拷贝的接口成员，通常会将原接口成员的键作为新的转换方法参数，如：</p>
<pre><code class="copyable">type Getters<T> = &#123;
    [K in keyof T as `get$&#123;Capitalize<string & K>&#125;`]: () => T[K]
&#125;;

interface Person &#123;
    name: string;
    age: number;
    location: string;
&#125;

type LazyPerson = Getters<Person>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换后的结果：</p>
<pre><code class="copyable">type LazyPerson = &#123;
    getName: () => string;
    getAge: () => number;
    getLocation: () => string;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里的 <code>string & k</code> 是因为重映射的转换方法（即 <code>as</code> 后面的部分）必须是可分配给 <code>string | number | symbol</code> 的，而 K 来自于 <code>keyof</code>，可能包含 <code>symbol</code> 类型，这样的话是不能交给模板字面量类型使用的。</p>
</blockquote>
<p>如果转换方法返回了never，那么这个成员就被除去了，所以我们可以使用这个方法来过滤掉成员。</p>
<pre><code class="copyable">type RemoveKindField<T> = &#123;
    [K in keyof T as Exclude<K, "kind">]: T[K]
&#125;;

interface Circle &#123;
    kind: "circle";
    radius: number;
&#125;

// type KindlessCircle = &#123;
//     radius: number;
// &#125;
type KindlessCircle = RemoveKindField<Circle>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，当与模板字面量一同使用时，由于其排列组合的特性，如果重映射的转换方法是一个由 模板字面量类型 组成的 联合类型，那么就会从排列组合得到多个成员。</p>
<pre><code class="copyable">type DoubleProp<T> = &#123; [P in keyof T & string as `$&#123;P&#125;1` | `$&#123;P&#125;2`]: T[P] &#125;
type Tmp = DoubleProp<&#123; a: string, b: number &#125;>;  // &#123; a1: string, a2: string, b1: number, b2: number &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">尾声</h2>
<p>这篇文章确实很长很长，因不建议一次性囫囵吞枣的读完，建议选取几段有一定长度的连续时间，给它掰开了揉碎了好好读懂。写文不易，尤其是写这么长的文章，但是如果能帮助你的 TypeScript 更上一层楼，就完全值得了。</p>
<p>如果在之前，你从未关注过类型编程方面，那么阅读完毕后可能需要一定时间来适应思路的转变。还是那句话，认识到 <strong>类型编程的本质也是编程</strong>。当然，你也可以渐进式的开始实践这一点，比如从今天开始，从现在手头里的项目开始，从泛型到类型守卫，从索引/映射类型到条件类型，从使用工具类型到封装工具类型，一步步变成 TypeScript 高高手。</p></div>  
</div>
            