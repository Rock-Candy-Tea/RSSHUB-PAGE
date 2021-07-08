
---
title: '简要介绍fp-ts（四）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3406'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 09:23:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=3406'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Reader</h2>
<p>在 fp-ts 中，<code>Reader</code>的定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Reader<R, A> &#123;
  (r: R): A
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是一个类型为<code>r -> a</code>的函数，<code>r</code>可以看作为计算所需的环境，而<code>a</code>是计算的结果。它经常被用来做依赖注入。先来看一段代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> f = (b: <span class="hljs-built_in">boolean</span>): <span class="hljs-function"><span class="hljs-params">string</span> =></span> b ? <span class="hljs-string">'true'</span> : <span class="hljs-string">'false'</span>;

<span class="hljs-keyword">const</span> g = (n: <span class="hljs-built_in">number</span>): <span class="hljs-function"><span class="hljs-params">string</span> =></span> f(n > <span class="hljs-number">2</span>);

<span class="hljs-keyword">const</span> h = (s: <span class="hljs-built_in">string</span>): <span class="hljs-function"><span class="hljs-params">string</span> =></span> g(s.length + <span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.log(h(<span class="hljs-string">'abc'</span>)) <span class="hljs-comment">// 'true'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是三个普通的函数，没有什么特别之处。现在假设，我们想让<code>f</code>更加国际化，比如来自中国的用户访问的时候，<code>f</code>应当返回“是”和“否”。于是，我们为<code>f</code>增加了一个参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Dependencies &#123;
  <span class="hljs-attr">i18n</span>: &#123;
    <span class="hljs-attr">true</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">false</span>: <span class="hljs-built_in">string</span>,
  &#125;
&#125;


<span class="hljs-keyword">const</span> f = (b: <span class="hljs-built_in">boolean</span>, <span class="hljs-attr">deps</span>: Dependencies): <span class="hljs-function"><span class="hljs-params">string</span> =></span> b ? deps.i18n.true : deps.i18n.false;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，这就导致了<code>g</code>编译不通过，因为<code>g</code>在调用<code>f</code>的之后没有传入<code>deps</code>。于是，我们必须为<code>g</code>增加一个参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> g = (n: <span class="hljs-built_in">number</span>, <span class="hljs-attr">deps</span>: Dependencies): <span class="hljs-function"><span class="hljs-params">string</span> =></span> f(n > <span class="hljs-number">2</span>, deps);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，这会导致<code>h</code>的编译失败，然后我们需要为<code>h</code>也增加一个参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> h = (s: <span class="hljs-built_in">string</span>, <span class="hljs-attr">deps</span>: Dependencies): <span class="hljs-function"><span class="hljs-params">string</span> =></span> g(s.length + <span class="hljs-number">1</span>, deps)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，我们终于可以给<code>h</code>传入<code>deps</code>，得到想要的结果了：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">console</span>.log(h(<span class="hljs-string">"356"</span>, &#123; <span class="hljs-attr">i18n</span>: &#123; <span class="hljs-attr">true</span>: <span class="hljs-string">"是"</span>, <span class="hljs-attr">false</span>: <span class="hljs-string">"否"</span> &#125; &#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的结果不能让人满意，<code>g</code>和<code>h</code>并没有使用传入的<code>deps</code>，但是为了能够使用<code>f</code>，他们必须拿到<code>deps</code>。</p>
<p>那么有没有更好的解决方法呢？我们先来尝试一下如果将<code>Dependencies</code>这个参数移出成为独立的一个参数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> f =
  (b: <span class="hljs-built_in">boolean</span>): <span class="hljs-function">(<span class="hljs-params">(deps: Dependencies) => <span class="hljs-built_in">string</span></span>) =></span>
  <span class="hljs-function">(<span class="hljs-params">deps</span>) =></span>
    b ? deps.i18n.true : deps.i18n.false;

<span class="hljs-keyword">const</span> g =
  (n: <span class="hljs-built_in">number</span>): <span class="hljs-function">(<span class="hljs-params">(deps: Dependencies) => <span class="hljs-built_in">string</span></span>) =></span> f(n > <span class="hljs-number">2</span>);

<span class="hljs-keyword">const</span> h =
  (s: <span class="hljs-built_in">string</span>): <span class="hljs-function">(<span class="hljs-params">(deps: Dependencies) => <span class="hljs-built_in">string</span></span>) =></span> g(s.length + <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>(deps: Dependencies) => string</code>就是<code>Reader<Dependencies, string></code>，所以我们也可以这样写：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> f =
  (b: <span class="hljs-built_in">boolean</span>): Reader<Dependencies, <span class="hljs-built_in">string</span>> =>
  <span class="hljs-function">(<span class="hljs-params">deps</span>) =></span>
    b ? deps.i18n.true : deps.i18n.false;

<span class="hljs-keyword">const</span> g = (n: <span class="hljs-built_in">number</span>): Reader<Dependencies, <span class="hljs-built_in">string</span>> => f(n > <span class="hljs-number">2</span>);

<span class="hljs-keyword">const</span> h = (s: <span class="hljs-built_in">string</span>): Reader<Dependencies, <span class="hljs-built_in">string</span>> => g(s.length + <span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如我们不想 hard code 我们的长度下限（也就是，<code>n > 2</code>的<code>2</code>），而是将下限注入到<code>g</code>中。首先，我们为<code>Dependencies</code>增加一项：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Dependencies &#123;
  <span class="hljs-attr">i18n</span>: &#123;
    <span class="hljs-attr">true</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">false</span>: <span class="hljs-built_in">string</span>,
  &#125;;
  lowerBound: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，我们想要从<code>Dependencies</code>读到<code>lowerBound</code>，但是我们不想写出这样的代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> g = (n: <span class="hljs-built_in">number</span>): Reader<Dependencies, <span class="hljs-built_in">string</span>> => <span class="hljs-function">(<span class="hljs-params">deps</span>) =></span> f(n > deps.lowerBound)(deps);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这会让我们之前的努力都白费了。幸好<code>Reader</code>的<code>ask</code>方法可以帮助我们从<code>Dependencies</code>读<code>lowerBound</code>而不需要真的拿到<code>deps</code>：</p>
<pre><code class="copyable">const g = (n: number): Reader<Dependencies, string> => pipe(
  ask<Dependencies>(),
  chain(deps => f(n > deps.lowerBound))
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ask</code>的实现如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> ask: <R><span class="hljs-function">() =></span> Reader<R, R> = <span class="hljs-function">() =></span> identity
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来推导一下<code>g</code>的返回值类型是不是符合<code>Reader<Dependencies, string></code>。首先<code>ask（）</code>返回<code>Reader<Dependencies, Dependencies></code>。<code>chain</code>接受的参数类型是<code>Dependencies -> Reader<Dependencies, string></code>，返回类型确实是<code>Reader<Dependencies, string></code>。</p>
<p>关于<code>Reader</code>最有趣的一点是，它和<code>Either</code>一样 kind 为<code>* -> * -> *</code>，也就意味着我们不能为 <code>Reader</code> 而只能为<code>Reader r</code>创建一个 <code>Functor</code> 的 instance。对应的<code>map</code>函数类型是：</p>
<pre><code class="copyable">map :: (a -> b) -> Reader r a -> Reader r b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面提到了<code>Reader r a</code>也就是<code>r -> a</code>，那么上述的类型其实就等价于：</p>
<pre><code class="copyable">(a -> b) -> (r -> a) -> (r -> b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于<code>compose</code>函数的定义：</p>
<pre><code class="copyable">compose :: (b -> c) -> (a -> b) -> (a -> c)
compose g f = \x -> g(f(x))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就会发现原来<code>Reader r</code>或者说<code>(->) r</code>的<code>map</code>就是函数的 composition。</p>
<h2 data-id="heading-1">Writer</h2>
<p><code>fp-ts</code>中的<code>Writer</code>定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Writer<W, A> &#123;
  (): [A, W]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是一个返回 tuple 的函数。假如我们有这样一个函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isHeavy = <span class="hljs-function">(<span class="hljs-params">weight: <span class="hljs-built_in">number</span></span>) =></span> weight > <span class="hljs-number">80</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数只返回了一个布尔值，但是我们希望这个返回值能多告诉我们一些额外的信息，为此，我们对返回值进行修改：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isHeavy =
  (weight: <span class="hljs-built_in">number</span>): W.Writer<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">boolean</span>> =>
  <span class="hljs-function">() =></span>
    [weight > <span class="hljs-number">80</span>, <span class="hljs-string">"与80kg进行比较。"</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就知道了更多的上下文，而不是一个干巴巴的布尔值。但是这也会带来一个问题，假如我们还有一个函数如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getWeight =
  (user: User): W.Writer<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>> =>
  <span class="hljs-function">() =></span>
    [user.weight, <span class="hljs-string">"取体重。"</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getWeight</code>的返回值不能直接传给<code>isHeavy</code>，因为<code>isHeavy</code>需要的是一个普通的 <code>number</code>，而<code>getWeight</code>返回的是一个附带着上下文的值。不过，<code>chain</code>能够在遵从上下文的前提下进行计算，所以我们再次用到它。这不过和之前不同的是，fp-ts的<code>Writer</code>并没有直接提供<code>Monad</code>的instance，我们需要使用<code>getMonad</code>自己创建：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> W <span class="hljs-keyword">from</span> <span class="hljs-string">"fp-ts/Writer"</span>;

<span class="hljs-keyword">const</span> monad = W.getMonad(monoidString);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getMonad</code>需求一个<code>Monoid</code>的instance，这是因为<code>Writer</code>接受的第一个类型并不一定是<code>string</code>，也有可能是<code>Array string</code>等。唯一的限制是它们需要能够提供<code>Monoid</code>的instance。那么<code>Monoid</code>这个 typeclass 又意味着什么呢。大家可能对 <code>Monoid</code> 这个英文名可能不太熟悉，但是很可能听过它的中文译名幺半群。</p>
<blockquote>
<p>幺半群，是指在抽象代数此一数学分支中，幺半群是指一个带有可结合二元运算和单位元的代数结构（摘自百度百科。）</p>
</blockquote>
<p>简单来说，幺半群就是具有单位元的半群。在编程的语境下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Semigroup<A> &#123;
  <span class="hljs-keyword">readonly</span> concat: <span class="hljs-function">(<span class="hljs-params">x: A, y: A</span>) =></span> A
&#125;

<span class="hljs-keyword">interface</span> Monoid<A> <span class="hljs-keyword">extends</span> Semigroup<A> &#123;
  <span class="hljs-keyword">readonly</span> empty: A
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，我们需要为<code>A</code>定义一个符合结合律的二元运算<code>concat</code>。对于<code>string</code>类型来说，这意味着任取三个字符串<code>a</code>、<code>b</code>、<code>c</code>，都有<code>concat(concat(a, b), c) = concat(a, concat(b, c))</code>。操作符<code>+</code>满足我们的要求，写成函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> concat: <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">string</span>, b:<span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">string</span> = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a + b;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单位元意味着需要找到一个字符串<code>e</code>，使得任取一个字符串<code>a</code>都有<code>concat(e, a) = concat(a, e)</code>。<code>e</code>可以选择空字符串。所以三元组<code><string, +, ''></code>就构成了一个半幺群。其他半幺群的例子有<code><number, +, 0></code>、<code><boolean, &&, true></code>等。</p>
<p>在通过<code>getMonad</code>之后，我们就拿到了一个<code>Monad</code>的 instance。于是我们就可以使用<code>chain</code>做有带着上下文的运算了：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 使用 execute 获得累积的额外信息</span>
W.execute(chain(getWeight(&#123; <span class="hljs-attr">weight</span>: <span class="hljs-number">75</span> &#125;), isHeavy)) <span class="hljs-comment">// 取体重。与80kg进行比较。</span>

<span class="hljs-comment">// 使用 evaluate 取得计算结果</span>
W.evaluate(chain(getWeight(&#123; <span class="hljs-attr">weight</span>: <span class="hljs-number">81</span> &#125;), isHeavy)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">State</h2>
<p>在 fp-ts 中，<code>State</code>的定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> State<S, A> &#123;
  (s: S): [A, S]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为纯函数是无法访问外部的 state 的，因此在函数式编程中 state 需要以参数的形式传进来，然后函数不仅要返回根据 state 计算出来的结果，还需要返回新的 state。一个伪随机数生成器（pseudo random number generators，PRNG）的例子：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpaulgray.net%2Fthe-state-monad" target="_blank" rel="nofollow noopener noreferrer" title="https://paulgray.net/the-state-monad" ref="nofollow noopener noreferrer">the state monad</a>。</p></div>  
</div>
            