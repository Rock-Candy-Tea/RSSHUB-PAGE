
---
title: 'Vue 中的 defineComponent'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4421'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 18:09:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=4421'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：崔静</p>
</blockquote>
<p>defineComponent 本身的功能很简单，但是最主要的功能是为了 ts 下的类型推到。对于一个 ts 文件，如果我们直接写</p>
<pre><code class="copyable">export default &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候，对于编辑器而言，&#123;&#125; 只是一个 Object 的类型，无法有针对性的提示我们对于 vue 组件来说 &#123;&#125; 里应该有哪些属性。但是增加一层 defineComponet 的话，</p>
<pre><code class="copyable">export default defineComponent(&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时，&#123;&#125; 就变成了 defineComponent 的参数，那么对参数类型的提示，就可以实现对 &#123;&#125; 中属性的提示，外还可以进行对参数的一些类型推导等操作。</p>
<blockquote>
<p>但是上面的例子，如果你在 vscode 的用 .vue 文件中尝试的话，会发现不写 defineComponent 也一样有提示。这个其实是 Vetur 插件进行了处理。</p>
</blockquote>
<p>下面看 defineComponent 的实现，有4个重载，先看最简单的第一个，这里先不关心 DefineComponent 是什么，后面细看。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// overload 1: direct setup function</span>
<span class="hljs-comment">// (uses user defined props interface)</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComponent</span><<span class="hljs-title">Props</span>, <span class="hljs-title">RawBindings</span> = <span class="hljs-title">object</span>>(<span class="hljs-params">
  setup: (
    props: Readonly<Props>,
    ctx: SetupContext
  ) => RawBindings | RenderFunction
</span>): <span class="hljs-title">DefineComponent</span><<span class="hljs-title">Props</span>, <span class="hljs-title">RawBindings</span>>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>defineComponet 参数为 function， function 有两个参数 props 和 ctx，返回值类型为 RawBindings 或者 RenderFunction。defineComponet 的返回值类型为 <code>DefineComponent<Props, RawBindings></code>。这其中有两个泛型 Props 和 RawBindings。Props 会根据我们实际写的时候给 setup 第一个参数传入的类型而确定，RawBindings 则根据我们 setup 返回值来确定。一大段话比较绕，写一个类似的简单的例子来看:</p>
<ul>
<li>
<p>类似 props 用法的简易 demo 如下，我们给 a 传入不同类型的参数，define 返回值的类型也不同。这种叫 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Ffunctions.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/functions.html" ref="nofollow noopener noreferrer">Generic Functions</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">Props</span>>(<span class="hljs-params">a: Props</span>): <span class="hljs-title">Props</span>

<span class="hljs-title">const</span> <span class="hljs-title">arg1</span>:<span class="hljs-title">string</span> = '123'
<span class="hljs-title">const</span> <span class="hljs-title">result1</span> = <span class="hljs-title">define</span>(<span class="hljs-params">arg1</span>) // <span class="hljs-title">result1</span>：<span class="hljs-title">string</span>

<span class="hljs-title">const</span> <span class="hljs-title">arg2</span>:<span class="hljs-title">number</span> = 1
<span class="hljs-title">const</span> <span class="hljs-title">result2</span> = <span class="hljs-title">define</span>(<span class="hljs-params">arg2</span>) // <span class="hljs-title">result2</span>: <span class="hljs-title">number</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>类似 RawBindings 的简易 demo如下： setup 返回值类型不同，define 返回值的类型也不同</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">T</span>>(<span class="hljs-params">setup: ()=>T</span>): <span class="hljs-title">T</span>

<span class="hljs-title">const</span> <span class="hljs-title">arg1</span>:<span class="hljs-title">string</span> = '123'
<span class="hljs-title">const</span> <span class="hljs-title">resul1</span> = <span class="hljs-title">define</span>(<span class="hljs-params">() => &#123;
  <span class="hljs-keyword">return</span> arg1
&#125;</span>)

<span class="hljs-title">const</span> <span class="hljs-title">arg2</span>:<span class="hljs-title">number</span> = 1
<span class="hljs-title">const</span> <span class="hljs-title">result2</span> = <span class="hljs-title">define</span>(<span class="hljs-params">() => &#123;
  <span class="hljs-keyword">return</span> arg2
&#125;</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>由上面两个简易的 demo，可以理解重载1的意思，defineComponet 返回类型为<code>DefineComponent<Props, RawBindings></code>，其中 Props 为 setup 第一个参数类型；RawBindings 为 setup 返回值类型，如果我们返回值为函数的时候，取默认值 object。从中可以掌握一个 ts 推导的基本用法，对于下面的定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">T</span>>(<span class="hljs-params">a: T</span>): <span class="hljs-title">T</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以根据运行时传入的参数，来动态决定 T 的类型</strong>  这种方式也是运行时类型和 typescript 静态类型的唯一联系，很多我们想通过运行时传入参数类型，来决定其他相关类型的时候，就可以使用这种方式。</p>
<p>接着看 definComponent，它的重载2，3，4分别是为了处理 options 中 props 的不同类型。看最常见的 object 类型的 props 的声明</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComponent</span><
  // <span class="hljs-title">the</span> <span class="hljs-title">Readonly</span> <span class="hljs-title">constraint</span> <span class="hljs-title">allows</span> <span class="hljs-title">TS</span> <span class="hljs-title">to</span> <span class="hljs-title">treat</span> <span class="hljs-title">the</span> <span class="hljs-title">type</span> <span class="hljs-title">of</span> </span>&#123; required: <span class="hljs-literal">true</span> &#125;
  <span class="hljs-comment">// as constant instead of boolean.</span>
  PropsOptions <span class="hljs-keyword">extends</span> Readonly<ComponentPropsOptions>,
  RawBindings,
  D,
  C <span class="hljs-keyword">extends</span> ComputedOptions = &#123;&#125;,
  M <span class="hljs-keyword">extends</span> MethodOptions = &#123;&#125;,
  Mixin <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  Extends <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  E <span class="hljs-keyword">extends</span> EmitsOptions = Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>,
  EE <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> = <span class="hljs-built_in">string</span>
>(
  options: ComponentOptionsWithObjectProps<
    PropsOptions,
    RawBindings,
    D,
    C,
    M,
    Mixin,
    Extends,
    E,
    EE
  >
): DefineComponent<PropsOptions, RawBindings, D, C, M, Mixin, Extends, E, EE>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和上面重载1差不多的思想，核心思想也是根据运行时写的 options 中的内容推导出各种泛型。在 vue3 中 setup 的第一个参数是 props，这个 props 的类型需要和我们在 options 传入的一致。这个就是在<code>ComponentOptionsWithObjectProps</code>中实现的。代码如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ComponentOptionsWithObjectProps<
  PropsOptions = ComponentObjectPropsOptions,
  RawBindings = &#123;&#125;,
  D = &#123;&#125;,
  C <span class="hljs-keyword">extends</span> ComputedOptions = &#123;&#125;,
  M <span class="hljs-keyword">extends</span> MethodOptions = &#123;&#125;,
  Mixin <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  Extends <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  E <span class="hljs-keyword">extends</span> EmitsOptions = EmitsOptions,
  EE <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> = <span class="hljs-built_in">string</span>,
  Props = Readonly<ExtractPropTypes<PropsOptions>>,
  Defaults = ExtractDefaultPropTypes<PropsOptions>
> = ComponentOptionsBase<
  Props,
  RawBindings,
  D,
  C,
  M,
  Mixin,
  Extends,
  E,
  EE,
  Defaults
> & &#123;
  <span class="hljs-attr">props</span>: PropsOptions & ThisType<<span class="hljs-built_in">void</span>>
&#125; & ThisType<
    CreateComponentPublicInstance<
      Props,
      RawBindings,
      D,
      C,
      M,
      Mixin,
      Extends,
      E,
      Props,
      Defaults,
      <span class="hljs-literal">false</span>
    >
  >
    
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ComponentOptionsBase<
  Props,
  RawBindings,
  D,
  C <span class="hljs-keyword">extends</span> ComputedOptions,
  M <span class="hljs-keyword">extends</span> MethodOptions,
  Mixin <span class="hljs-keyword">extends</span> ComponentOptionsMixin,
  Extends <span class="hljs-keyword">extends</span> ComponentOptionsMixin,
  E <span class="hljs-keyword">extends</span> EmitsOptions,
  EE <span class="hljs-keyword">extends</span> string = string,
  Defaults = &#123;&#125;
>
  <span class="hljs-keyword">extends</span> LegacyOptions<Props, D, C, M, Mixin, Extends>,
    ComponentInternalOptions,
    ComponentCustomOptions &#123;
      setup?: <span class="hljs-function">(<span class="hljs-params">
        <span class="hljs-built_in">this</span>: <span class="hljs-built_in">void</span>,
        props: Props,
        ctx: SetupContext<E, Props>
      </span>) =></span> <span class="hljs-built_in">Promise</span><RawBindings> | RawBindings | RenderFunction | <span class="hljs-built_in">void</span>
    <span class="hljs-comment">//...</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很长一段，同样的先用一个简化版的 demo 来理解一下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> TypeA<T1, T2, T3> = &#123;
  <span class="hljs-attr">a</span>: T1,
  <span class="hljs-attr">b</span>: T2,
  <span class="hljs-attr">c</span>: T3
&#125;
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">T1</span>, <span class="hljs-title">T2</span>, <span class="hljs-title">T3</span>>(<span class="hljs-params">options: TypeA<T1, T2, T3></span>): <span class="hljs-title">T1</span>
<span class="hljs-title">const</span> <span class="hljs-title">result</span> = <span class="hljs-title">define</span>(<span class="hljs-params">&#123;
  a: <span class="hljs-string">'1'</span>,
  b: <span class="hljs-number">1</span>,
  c: &#123;&#125;
&#125;</span>) // <span class="hljs-title">result</span>: <span class="hljs-title">string</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>根据传入的 options 参数 ts 会推断出 T1,T2,T3的类型。得到 T1, T2, T3 之后，可以利用他们进行其他的推断。稍微改动一下上面的 demo，假设 c 是一个函数，里面的参数类型由 a 的类型来决定：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> TypeA<T1, T2, T3> = TypeB<T1, T2>
<span class="hljs-keyword">type</span> TypeB<T1, T2> = &#123;
  <span class="hljs-attr">a</span>: T1
  <span class="hljs-attr">b</span>: T2,
  <span class="hljs-attr">c</span>: <span class="hljs-function">(<span class="hljs-params">arg:T1</span>)=></span>&#123;&#125;
&#125;
<span class="hljs-keyword">const</span> result = define(&#123;
  <span class="hljs-attr">a</span>: <span class="hljs-string">'1'</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">c</span>: <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> &#123;  <span class="hljs-comment">// arg 这里就被会推导为一个 string 的类型</span>
    <span class="hljs-keyword">return</span> arg
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后来看 vue 中的代码，首先 <code>defineComponent</code> 可以推导出 PropsOptions。但是 props 如果是对象类型的话，写法如下</p>
<pre><code class="copyable">props: &#123;
   name: &#123;
     type: String,
     //... 其他的属性
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 setup 中的 props 参数，则需要从中提取出 type 这个类型。所以在 ComponentOptionsWithObjectProps 中</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ComponentOptionsWithObjectProps<
  PropsOptions = ComponentObjectPropsOptions,
  <span class="hljs-comment">//...</span>
  Props = Readonly<ExtractPropTypes<PropsOptions>>,
  <span class="hljs-comment">//...</span>
>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 ExtracPropTypes 对 PropsOptions 进行转化，然后得到 Props，再传入 ComponentOptionsBase，在这个里面，作为 setup 参数的类型</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ComponentOptionsBase<
  Props,
  //...
>
  <span class="hljs-keyword">extends</span> LegacyOptions<Props, D, C, M, Mixin, Extends>,
    ComponentInternalOptions,
    ComponentCustomOptions &#123;
  setup?: <span class="hljs-function">(<span class="hljs-params">
    <span class="hljs-built_in">this</span>: <span class="hljs-built_in">void</span>,
    props: Props,
    ctx: SetupContext<E, Props>
  </span>) =></span> <span class="hljs-built_in">Promise</span><RawBindings> | RawBindings | RenderFunction | <span class="hljs-built_in">void</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了对 props 的推导。</p>
<ul>
<li>
<p>this 的作用</p>
<p>在 setup 定义中第一个是 this:void 。我们在 setup 函数中写逻辑的时候，会发现如果使用了 <code>this.xxx</code> IDE 中会有错误提示</p>
<blockquote>
<p>Property 'xxx' does not exist on type 'void'</p>
</blockquote>
<p>这里通过设置 <code>this:void</code>来避免我们在 setup 中使用 this。</p>
<p>this 在 js 中是一个比较特殊的存在，它是根据运行上上下文决定的，所以 typescript 中有时候无法准确的推导出我们代码中使用的 this 是什么类型的，所以 this 就变成了 any，各种类型提示/推导啥的，也都无法使用了(注意：只有开启了 noImplicitThis 配置， ts 才会对 this 的类型进行推导)。为了解决这个问题，typescript 中 function 的可以明确的写一个 this 参数，例如官网的例子：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Card &#123;
  <span class="hljs-attr">suit</span>: <span class="hljs-built_in">string</span>;
  card: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Deck &#123;
  <span class="hljs-attr">suits</span>: <span class="hljs-built_in">string</span>[];
  cards: <span class="hljs-built_in">number</span>[];
  createCardPicker(<span class="hljs-built_in">this</span>: Deck): <span class="hljs-function">() =></span> Card;
&#125;

<span class="hljs-keyword">let</span> deck: Deck = &#123;
  <span class="hljs-attr">suits</span>: [<span class="hljs-string">"hearts"</span>, <span class="hljs-string">"spades"</span>, <span class="hljs-string">"clubs"</span>, <span class="hljs-string">"diamonds"</span>],
  <span class="hljs-attr">cards</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">52</span>),
  <span class="hljs-comment">// <span class="hljs-doctag">NOTE:</span> The function now explicitly specifies that its callee must be of type Deck</span>
  <span class="hljs-attr">createCardPicker</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">this</span>: Deck</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> pickedCard = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">52</span>);
      <span class="hljs-keyword">let</span> pickedSuit = <span class="hljs-built_in">Math</span>.floor(pickedCard / <span class="hljs-number">13</span>);

      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">suit</span>: <span class="hljs-built_in">this</span>.suits[pickedSuit], <span class="hljs-attr">card</span>: pickedCard % <span class="hljs-number">13</span> &#125;;
    &#125;;
  &#125;,
&#125;;

<span class="hljs-keyword">let</span> cardPicker = deck.createCardPicker();
<span class="hljs-keyword">let</span> pickedCard = cardPicker();

alert(<span class="hljs-string">"card: "</span> + pickedCard.card + <span class="hljs-string">" of "</span> + pickedCard.suit);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>明确的定义出在 createCardPicker 中的 this 是 Deck 的类型。这样在 <code>createCardPicker</code> 中 this 下可使用的属性/方法，就被限定为 Deck 中的。</p>
<p>另外和 this 有关的，还有一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Futility-types.html%23thistypetype" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/utility-types.html#thistypetype" ref="nofollow noopener noreferrer"><code>ThisType</code></a>。</p>
</li>
</ul>
<h3 data-id="heading-0">ExtractPropTypes 和 ExtractDefaultPropTypes</h3>
<p>上面提到了，我们写的 props</p>
<pre><code class="copyable">&#123;
  props: &#123;
    name1: &#123;
      type: String,
      require: true
    &#125;,
    name2: &#123;
      type: Number
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过 defineComponent 的推导之后，会被转换为 ts 的类型</p>
<pre><code class="copyable">ReadOnly<&#123;
  name1: string,
  name2?: number | undefined
&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个过程就是利用 ExtractPropTypes 实现的。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ExtractPropTypes<O> = O <span class="hljs-keyword">extends</span> <span class="hljs-built_in">object</span>
  ? &#123; [K <span class="hljs-keyword">in</span> RequiredKeys<O>]: InferPropType<O[K]> &#125; &
      &#123; [K <span class="hljs-keyword">in</span> OptionalKeys<O>]?: InferPropType<O[K]> &#125;
  : &#123; [K <span class="hljs-keyword">in</span> <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据类型中清晰的命名，很好理解：利用 <code>RrequiredKeys<O></code> 和 <code>OptionsKeys<O></code> 将 O 按照是否有 required 进行拆分(以前面props为例子)</p>
<pre><code class="copyable">&#123;
  name1
&#125; & &#123;
  name2？
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后每一组里，用 <code>InferPropType<O[K]></code> 推导出类型。</p>
<ul>
<li>
<p>InferPropType</p>
<p>在理解这个之前，先理解一些简单的推导。首先我们在代码中写</p>
<pre><code class="copyable">props = &#123;
  type: String
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的话，经过 ts 的推导，props.type 的类型是 StringConstructor。所以第一步需要从 StringConstructor/ NumberConstructor 等 xxConstrucror 中得到对应的类型 string/number 等。可以通过 infer 来实现</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> a = StringConstructor
<span class="hljs-keyword">type</span> ConstructorToType<T> = T <span class="hljs-keyword">extends</span>  &#123; (): infer V &#125; ? V : <span class="hljs-built_in">never</span>
<span class="hljs-keyword">type</span> c = ConstructorToType<a> <span class="hljs-comment">// type c = String</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们通过 <code>():infer V</code> 来获取到类型。之所以可以这样用，和 String/Number 等类型的实现有关。javascript 中可以写</p>
<pre><code class="copyable">const key = String('a')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，key 是一个 string 的类型。还可以看一下 StringConstructor 接口类型表示</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> StringConstructor &#123;
    <span class="hljs-keyword">new</span>(value?: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">String</span>;
    (value?: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">string</span>;
    <span class="hljs-keyword">readonly</span> prototype: <span class="hljs-built_in">String</span>;
    fromCharCode(...codes: <span class="hljs-built_in">number</span>[]): <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面有一个 <code>():string</code> ，所以通过 <code>extends &#123;(): infer V&#125;</code> 推断出来的  V 就是 string。</p>
<p>然后再进一步，将上面的 a 修改成 propsOptions 中的内容，然后把 ConstructorToType 中的 infer V 提到外面一层来判断</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> a = StringConstructor
<span class="hljs-keyword">type</span> ConstructorType<T> = &#123; (): T &#125;
<span class="hljs-keyword">type</span> b = a <span class="hljs-keyword">extends</span> &#123;
  <span class="hljs-attr">type</span>: ConstructorType<infer V>
  required?: <span class="hljs-built_in">boolean</span>
&#125; ? V : <span class="hljs-built_in">never</span> <span class="hljs-comment">// type b = String</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就简单实现了将 props 中的内容转化为 type 中的类型。</p>
<p>因为 props 的 type 支持很多中写法，vue3 中实际的代码实现要比较复杂</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> InferPropType<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-literal">null</span>
  ? <span class="hljs-built_in">any</span> <span class="hljs-comment">// null & true would fail to infer</span>
  : T <span class="hljs-keyword">extends</span> &#123; <span class="hljs-attr">type</span>: <span class="hljs-literal">null</span> | <span class="hljs-literal">true</span> &#125;
    ? <span class="hljs-built_in">any</span> 
    <span class="hljs-comment">// As TS issue https://github.com/Microsoft/TypeScript/issues/14829 // somehow `ObjectConstructor` when inferred from &#123; (): T &#125; becomes `any` // `BooleanConstructor` when inferred from PropConstructor(with PropMethod) becomes `Boolean`</span>
    <span class="hljs-comment">// 这里单独判断了 ObjectConstructor 和 BooleanConstructor</span>
    : T <span class="hljs-keyword">extends</span> ObjectConstructor | &#123; <span class="hljs-attr">type</span>: ObjectConstructor &#125;
      ? Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>
      : T <span class="hljs-keyword">extends</span> BooleanConstructor | &#123; <span class="hljs-attr">type</span>: BooleanConstructor &#125;
        ? <span class="hljs-built_in">boolean</span>
        : T <span class="hljs-keyword">extends</span> Prop<infer V, infer D> ? (unknown <span class="hljs-keyword">extends</span> V ? D : V) : T

<span class="hljs-comment">// 支持 PropOptions 和 PropType 两种形式</span>
<span class="hljs-keyword">type</span> Prop<T, D = T> = PropOptions<T, D> | PropType<T>
<span class="hljs-keyword">interface</span> PropOptions<T = any, D = T> &#123;
  <span class="hljs-keyword">type</span>?: PropType<T> | <span class="hljs-literal">true</span> | <span class="hljs-literal">null</span>
  required?: <span class="hljs-built_in">boolean</span>
  <span class="hljs-keyword">default</span>?: D | DefaultFactory<D> | <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span> | <span class="hljs-built_in">object</span>
  validator?(value: unknown): <span class="hljs-built_in">boolean</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> PropType<T> = PropConstructor<T> | PropConstructor<T>[]

<span class="hljs-keyword">type</span> PropConstructor<T = <span class="hljs-built_in">any</span>> =
  | &#123; <span class="hljs-keyword">new</span> (...args: <span class="hljs-built_in">any</span>[]): T & <span class="hljs-built_in">object</span> &#125; <span class="hljs-comment">// 可以匹配到其他的 Constructor</span>
  | &#123; (): T &#125;  <span class="hljs-comment">// 可以匹配到 StringConstructor/NumberConstructor 和 () => string 等</span>
  | PropMethod<T> <span class="hljs-comment">// 匹配到 type: (a: number, b: string) => string 等 Function 的形式</span>

<span class="hljs-comment">// 对于 Function 的形式，通过 PropMethod 构造成了一个和 stringConstructor 类型的类型</span>
<span class="hljs-comment">// PropMethod 作为 PropType 类型之一</span>
<span class="hljs-comment">// 我们写 type: Function as PropType<(a: string) => &#123;b: string&#125;> 的时候，就会被转化为</span>
<span class="hljs-comment">// type: (new (...args: any[]) => ((a: number, b: string) => &#123;</span>
<span class="hljs-comment">//    a: boolean;</span>
<span class="hljs-comment">// &#125;) & object) | (() => (a: number, b: string) => &#123;</span>
<span class="hljs-comment">//    a: boolean;</span>
<span class="hljs-comment">// &#125;) | &#123;</span>
<span class="hljs-comment">//     (): (a: number, b: string) => &#123;</span>
<span class="hljs-comment">//         a: boolean;</span>
<span class="hljs-comment">//     &#125;;</span>
<span class="hljs-comment">//     new (): any;</span>
<span class="hljs-comment">//     readonly prototype: any;</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-comment">// 然后在 InferPropType 中就可以推断出 （a:number,b:string）=> &#123;a: boolean&#125;</span>
<span class="hljs-keyword">type</span> PropMethod<T, TConstructor = <span class="hljs-built_in">any</span>> = 
  T <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span> <span class="hljs-comment">// if is function with args</span>
  ? &#123; 
      <span class="hljs-keyword">new</span> (): TConstructor; 
      (): T; 
      <span class="hljs-keyword">readonly</span> prototype: TConstructor 
    &#125; <span class="hljs-comment">// Create Function like constructor</span>
  : <span class="hljs-built_in">never</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>RequiredKeys</p>
<p>这个用来从 props 中分离出一定会有值的 key，源码如下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> RequiredKeys<T> = &#123;
  [K <span class="hljs-keyword">in</span> keyof T]: T[K] <span class="hljs-keyword">extends</span>
    | &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span> &#125;
    | &#123; <span class="hljs-attr">default</span>: <span class="hljs-built_in">any</span> &#125;
    <span class="hljs-comment">// don't mark Boolean props as undefined</span>
    | BooleanConstructor
    | &#123; <span class="hljs-attr">type</span>: BooleanConstructor &#125;
    ? K
    : <span class="hljs-built_in">never</span>
&#125;[keyof T]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了明确定义 reqruied 以外，还包含有 default 值，或者 boolean 类型。因为对于 boolean 来说如果我们不传入，就默认为 false；而有 default 值的 prop，一定不会是 undefined</p>
</li>
<li>
<p>OptionalKeys</p>
<p>有了 RequiredKeys, OptionsKeys 就很简单了：排除了 RequiredKeys 即可</p>
<pre><code class="copyable">type OptionalKeys<T> = Exclude<keyof T, RequiredKeys<T>>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>ExtractDefaultPropTypes 和 ExtractPropTypes 类似，就不写了。</p>
<p>推导 options 中的 method，computed, data 返回值， 都和上面推导 props 类似。</p>
<h3 data-id="heading-1">emits options</h3>
<p>vue3 的 options 中新增加了一个 emits 配置，可以显示的配置我们在组件中要派发的事件。配置在 emits 中的事件，在我们写 <code>$emit</code> 的时候，会作为函数的第一个参数进行提示。</p>
<p>对获取 emits 中配置值的方式和上面获取 props 中的类型是类似的。<code>$emit</code>的提示，则是通过 <code>ThisType</code> 来实现的(关于 ThisType 参考另外一篇文章介绍)。下面是简化的 demo</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">T</span>>(<span class="hljs-params">props:&#123;
  emits: T,
  method?: &#123;[key: <span class="hljs-built_in">string</span>]: (...arg: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span>&#125;
&#125; & ThisType<&#123;
  $emits: (arg: T) => <span class="hljs-built_in">void</span>
&#125;></span>):<span class="hljs-title">T</span>

<span class="hljs-title">const</span> <span class="hljs-title">result</span> = <span class="hljs-title">define</span>(<span class="hljs-params">&#123;
  emits: &#123;
    key: <span class="hljs-string">'123'</span>
  &#125;,
  method: &#123;
    fn() &#123;
      <span class="hljs-built_in">this</span>.$emits(/*这里会提示：arg: &#123;
          key: <span class="hljs-built_in">string</span>;
      &#125;*/)
    &#125;
  &#125;
&#125;</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上面会推导出 T 为 emits 中的类型。然后 <code>& ThisType</code> ，使得在 method 中就可以使用 <code>this.$emit</code>。再将 T 作为 $emit 的参数类型，就可以在写 <code>this.$emit</code>的时候进行提示了。</p>
<p>然后看 vue3 中的实现</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComponent</span><
  //... 省却其他的
  <span class="hljs-title">E</span> <span class="hljs-title">extends</span> <span class="hljs-title">EmitsOptions</span> = <span class="hljs-title">Record</span><<span class="hljs-title">string</span>, <span class="hljs-title">any</span>>,
  //...
>(<span class="hljs-params">
  options: ComponentOptionsWithObjectProps<
    <span class="hljs-comment">//...</span>
    E,
    <span class="hljs-comment">//...</span>
  >
</span>): <span class="hljs-title">DefineComponent</span><<span class="hljs-title">PropsOptions</span>, <span class="hljs-title">RawBindings</span>, <span class="hljs-title">D</span>, <span class="hljs-title">C</span>, <span class="hljs-title">M</span>, <span class="hljs-title">Mixin</span>, <span class="hljs-title">Extends</span>, <span class="hljs-title">E</span>, <span class="hljs-title">EE</span>>

<span class="hljs-title">export</span> <span class="hljs-title">type</span> <span class="hljs-title">ComponentOptionsWithObjectProps</span><
  //..
  <span class="hljs-title">E</span> <span class="hljs-title">extends</span> <span class="hljs-title">EmitsOptions</span> = <span class="hljs-title">EmitsOptions</span>,
  //...
> = <span class="hljs-title">ComponentOptionsBase</span>< // 定义一个 <span class="hljs-title">E</span> 的泛型
  //...
  <span class="hljs-title">E</span>,
  //...
> & </span>&#123;
  <span class="hljs-attr">props</span>: PropsOptions & ThisType<<span class="hljs-built_in">void</span>>
&#125; & ThisType<
    CreateComponentPublicInstance<  <span class="hljs-comment">// 利用 ThisType 实现 $emit 中的提示</span>
      <span class="hljs-comment">//...</span>
      E,
      <span class="hljs-comment">//...</span>
    >
  >
    
<span class="hljs-comment">// ComponentOptionsWithObjectProps 中 包含了 ComponentOptionsBase</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ComponentOptionsBase<
  //...
  E <span class="hljs-keyword">extends</span> EmitsOptions, // type EmitsOptions = Record<string, ((...args: any[]) => any) | null> | string[]
  EE <span class="hljs-keyword">extends</span> string = string,
  Defaults = &#123;&#125;
>
  <span class="hljs-keyword">extends</span> LegacyOptions<Props, D, C, M, Mixin, Extends>,
    ComponentInternalOptions,
    ComponentCustomOptions &#123;
      <span class="hljs-comment">//..</span>
      emits?: (E | EE[]) & ThisType<<span class="hljs-built_in">void</span>>  <span class="hljs-comment">// 推断出 E 的类型</span>
&#125;
      
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ComponentPublicInstance<
  <span class="hljs-comment">//...</span>
  E <span class="hljs-keyword">extends</span> EmitsOptions = &#123;&#125;,
  <span class="hljs-comment">//...</span>
> = &#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-attr">$emit</span>: EmitFn<E>  <span class="hljs-comment">// EmitFn 来提取出 E 中的 key</span>
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一边学习一边实践的时候踩到一个坑。踩坑过程：将 emits 的推导过程实现了一下</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ObjectEmitsOptions = Record<
  <span class="hljs-built_in">string</span>,
  (<span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span>[]</span>) =></span> <span class="hljs-built_in">any</span>) | <span class="hljs-literal">null</span>
>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> EmitsOptions = ObjectEmitsOptions | <span class="hljs-built_in">string</span>[];

<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span><<span class="hljs-title">E</span> <span class="hljs-title">extends</span> <span class="hljs-title">EmitsOptions</span> = <span class="hljs-title">Record</span><<span class="hljs-title">string</span>, <span class="hljs-title">any</span>>, <span class="hljs-title">EE</span> <span class="hljs-title">extends</span> <span class="hljs-title">string</span> = <span class="hljs-title">string</span>>(<span class="hljs-params">options: E| EE[]</span>): (<span class="hljs-params">E | EE[]</span>) & <span class="hljs-title">ThisType</span><<span class="hljs-title">void</span>>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>然后用下面的方式来验证结果</p>
<pre><code class="copyable">const emit = ['key1', 'key2']
const a = define(emit)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看 ts 提示的时候发现，a 的类型是 <code>const b: string[] & ThisType<void></code>，但是实际中 vue3 中写同样数组的话，提示是 <code>const a: (("key1" | "key2")[] & ThisType<void>) | (("key1" | "key2")[] & ThisType<void>)</code></p>
<p>纠结好久，最终发现写法的不同：用下面写法的话推导出来结果一致</p>
<pre><code class="copyable">define(['key1', 'key2'])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是用之前的写法，通过变量传入的时候，ts 在拿到 emit 时候，就已经将其类型推导成了 <code>string[]</code>，所以 define 函数中拿到的类型就变成了 <code>string[]</code>，而不是原始的 <code>['key1', 'key2']</code></p>
<p><strong>因此需要注意：在 vue3 中定义 emits 的时候，建议直接写在 emits 中写，不要提取为单独的变量再传给 emits</strong></p>
<p>真的要放在单独变量里的话，需要进行处理，使得 <code>'[key1', 'key2']</code> 的变量定义返回类型为 <code>['key1', 'key2']</code> 而非 <code>string[]</code>。可以使用下面两种方式：</p>
<ul>
<li>
<p>方式一</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> keys = [<span class="hljs-string">"key1"</span>, <span class="hljs-string">"key2"</span>] <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>; <span class="hljs-comment">// const keys: readonly ["key1", "key2"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式写起来比较简单。但是有一个弊端，keys 为转为 readonly 了，后期无法对 keys 进行修改。</p>
<p>参考文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.to%2Fshakyshane%2F2-ways-to-create-a-union-from-an-array-in-typescript-1kd6" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.to/shakyshane/2-ways-to-create-a-union-from-an-array-in-typescript-1kd6" ref="nofollow noopener noreferrer">2 ways to create a Union from an Array in Typescript</a></p>
</li>
<li>
<p>方式二</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> UnionToIntersection<T> = (T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span> ? <span class="hljs-function">(<span class="hljs-params">v: T</span>) =></span> <span class="hljs-built_in">void</span> : <span class="hljs-built_in">never</span>) <span class="hljs-keyword">extends</span> (v: infer V) => <span class="hljs-built_in">void</span> ? V : <span class="hljs-built_in">never</span>
<span class="hljs-keyword">type</span> LastOf<T> = UnionToIntersection<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span> ? <span class="hljs-function">() =></span> T : <span class="hljs-built_in">never</span>> <span class="hljs-keyword">extends</span> () => infer R ? R : <span class="hljs-built_in">never</span>
<span class="hljs-keyword">type</span> Push<T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span>[], V> = [ ...T, V]

<span class="hljs-keyword">type</span> UnionToTuple<T, L = LastOf<T>, N = [T] <span class="hljs-keyword">extends</span> [<span class="hljs-built_in">never</span>] ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>> = N <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span> ? [] : Push<UnionToTuple<Exclude<T, L>>, L>

<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tuple</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">string</span>>(<span class="hljs-params">arr: T[]</span>): <span class="hljs-title">UnionToTuple</span><<span class="hljs-title">T</span>>

<span class="hljs-title">const</span> <span class="hljs-title">c</span> = <span class="hljs-title">tuple</span>(<span class="hljs-params">[<span class="hljs-string">'key1'</span>, <span class="hljs-string">'key2'</span>]</span>) // <span class="hljs-title">const</span> <span class="hljs-title">c</span>: ["<span class="hljs-title">key1</span>", "<span class="hljs-title">key2</span>"]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过 <code>arr: T[]</code> 将 <code>['key1', 'key2']</code> 转为 union，然后通过递归的方式， <code>LastOf</code> 获取 union 中的最后一个，<code>Push</code>到数组中。</p>
</li>
</ul>
<h4 data-id="heading-2">mixins 和 extends</h4>
<p>vue3 中写在 mixins 或 extends 中的内容可以在 <code>this</code> 中进行提示。对于 mixins 和 extends 来说，与上面其他类型的推断有一个很大的区别：递归。所以在进行类型判断的时候，也需要进行递归处理。举个简单的例子，如下</p>
<pre><code class="copyable">const AComp = &#123;
  methods: &#123;
    someA()&#123;&#125;
  &#125;
&#125;
const BComp = &#123;
  mixins: [AComp],
  methods: &#123;
    someB() &#123;&#125;
  &#125;
&#125;
const CComp = &#123;
  mixins: [BComp],
  methods: &#123;
    someC() &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 CComp 中的 this 的提示，应该有方法 someB 和 someA。为了实现这个提示，在进行类型推断的时候，需要一个类似下面的 ThisType</p>
<pre><code class="copyable">ThisType<&#123;
  someA
&#125; & &#123;
  someB
&#125; & &#123;
  someC
&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以对于 mixins 的处理，就需要递归获取 component 中的 mixins 中的内容，然后将嵌套的类型转化为扁平化的，通过 & 来链接。看源码中实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 判断 T 中是否有 mixin</span>
<span class="hljs-comment">// 如果 T 含有 mixin 那么这里结果为 false，以为 &#123;mixin: any&#125; &#123;mixin?: any&#125; 是无法互相 extends 的</span>
<span class="hljs-keyword">type</span> IsDefaultMixinComponent<T> = T <span class="hljs-keyword">extends</span> ComponentOptionsMixin
  ? ComponentOptionsMixin <span class="hljs-keyword">extends</span> T ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>
  : <span class="hljs-literal">false</span>

<span class="hljs-comment">// </span>
<span class="hljs-keyword">type</span> IntersectionMixin<T> = IsDefaultMixinComponent<T> <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span>
  ? OptionTypesType<&#123;&#125;, &#123;&#125;, &#123;&#125;, &#123;&#125;, &#123;&#125;>  <span class="hljs-comment">// T 不包含 mixin，那么递归结束，返回 &#123;&#125;</span>
  : UnionToIntersection<ExtractMixin<T>> <span class="hljs-comment">// 获取 T 中 Mixin 的内容进行递归</span>

<span class="hljs-comment">// ExtractMixin(map type) is used to resolve circularly references</span>
<span class="hljs-keyword">type</span> ExtractMixin<T> = &#123;
  <span class="hljs-attr">Mixin</span>: MixinToOptionTypes<T>
&#125;[T <span class="hljs-keyword">extends</span> ComponentOptionsMixin ? <span class="hljs-string">'Mixin'</span> : <span class="hljs-built_in">never</span>]

<span class="hljs-comment">// 通过 infer 获取到 T 中 Mixin, 然后递归调用 IntersectionMixin<Mixin></span>
<span class="hljs-keyword">type</span> MixinToOptionTypes<T> = T <span class="hljs-keyword">extends</span> ComponentOptionsBase<
  infer P,
  infer B,
  infer D,
  infer C,
  infer M,
  infer Mixin,
  infer Extends,
  <span class="hljs-built_in">any</span>,
  <span class="hljs-built_in">any</span>,
  infer Defaults
>
  ? OptionTypesType<P & &#123;&#125;, B & &#123;&#125;, D & &#123;&#125;, C & &#123;&#125;, M & &#123;&#125;, Defaults & &#123;&#125;> &
      IntersectionMixin<Mixin> &
      IntersectionMixin<Extends>
  : <span class="hljs-built_in">never</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>extends 和 mixin 的过程相同。然后看 ThisType 中的处理</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">ThisType<
    CreateComponentPublicInstance<
      Props,
      RawBindings,
      D,
      C,
      M,
      Mixin,
      Extends,
      E,
      Props,
      Defaults,
      <span class="hljs-literal">false</span>
    >
  >
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> CreateComponentPublicInstance<
  P = &#123;&#125;,
  B = &#123;&#125;,
  D = &#123;&#125;,
  C <span class="hljs-keyword">extends</span> ComputedOptions = &#123;&#125;,
  M <span class="hljs-keyword">extends</span> MethodOptions = &#123;&#125;,
  Mixin <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  Extends <span class="hljs-keyword">extends</span> ComponentOptionsMixin = ComponentOptionsMixin,
  E <span class="hljs-keyword">extends</span> EmitsOptions = &#123;&#125;,
  PublicProps = P,
  Defaults = &#123;&#125;,
  MakeDefaultsOptional <span class="hljs-keyword">extends</span> <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// 将嵌套的结构转为扁平化的</span>
  PublicMixin = IntersectionMixin<Mixin> & IntersectionMixin<Extends>,
  <span class="hljs-comment">// 提取 props</span>
  PublicP = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'P'</span>> & EnsureNonVoid<P>,
  <span class="hljs-comment">// 提取 RawBindings，也就是 setup 返回的内容</span>
  PublicB = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'B'</span>> & EnsureNonVoid<B>,
  <span class="hljs-comment">// 提取 data 返回的内容</span>
  PublicD = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'D'</span>> & EnsureNonVoid<D>,
  PublicC <span class="hljs-keyword">extends</span> ComputedOptions = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'C'</span>> &
    EnsureNonVoid<C>,
  PublicM <span class="hljs-keyword">extends</span> MethodOptions = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'M'</span>> &
    EnsureNonVoid<M>,
  PublicDefaults = UnwrapMixinsType<PublicMixin, <span class="hljs-string">'Defaults'</span>> &
    EnsureNonVoid<Defaults>
> = ComponentPublicInstance< <span class="hljs-comment">// 上面结果传给 ComponentPublicInstance，生成 this context 中的内容</span>
  PublicP,
  PublicB,
  PublicD,
  PublicC,
  PublicM,
  E,
  PublicProps,
  PublicDefaults,
  MakeDefaultsOptional,
  ComponentOptionsBase<P, B, D, C, M, Mixin, Extends, E, <span class="hljs-built_in">string</span>, Defaults>
>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是整体大部分的 defineComponent 的实现，可以看出，他纯粹是为了类型推导而生的，同时，这里边用到了很多很多类型推导的技巧，还有一些这里没有涉及，感兴趣的同学可以去仔细看下 Vue 中的实现。</p></div>  
</div>
            