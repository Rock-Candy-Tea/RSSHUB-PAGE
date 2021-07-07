
---
title: 'TypeScript——接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1909'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 23:13:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=1909'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<h2 data-id="heading-0">介绍</h2>
<p>TypeScript的核心原则之一是对值所具有的结构进行类型检查。它有时被称做“鸭式辨型法”或“结构性子类型化”。在TypeScript里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。</p>
<h2 data-id="heading-1">接口初探</h2>
<p>下面通过一个简单示例来观察接口是如何工作的：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> LabelledValue &#123;
  <span class="hljs-attr">label</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printLabel</span>(<span class="hljs-params">labelledObj: LabelledValue</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(labelledObj.label);
&#125;

<span class="hljs-keyword">let</span> myObj = &#123;<span class="hljs-attr">size</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">"Size 10 Object"</span>&#125;;
printLabel(myObj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LabelledValue接口就好比一个名字，它代表了有一个 label属性且类型为string的对象。 需要注意的是，我们在这里并不能像在其它语言里一样，说传给 printLabel的对象实现了这个接口。我们只会去关注值的外形。 只要传入的对象满足上面提到的必要条件，那么它就是被允许的。</p>
<h2 data-id="heading-2">可选属性</h2>
<p>接口里的属性不全都是必需的。可选属性在应用“option bags”模式时很常用，即给函数传入的参数对象中只有部分属性赋值了。</p>
<p>下面是应用了“option bags”的例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SquareConfig &#123;
  color?: <span class="hljs-built_in">string</span>;
  width?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSquare</span>(<span class="hljs-params">config: SquareConfig</span>): </span>&#123;color: <span class="hljs-built_in">string</span>; area: <span class="hljs-built_in">number</span>&#125; &#123;
  <span class="hljs-keyword">let</span> newSquare = &#123;<span class="hljs-attr">color</span>: <span class="hljs-string">"white"</span>, <span class="hljs-attr">area</span>: <span class="hljs-number">100</span>&#125;;
  <span class="hljs-keyword">if</span> (config.color) &#123;
    newSquare.color = config.color;
  &#125;
  <span class="hljs-keyword">if</span> (config.width) &#123;
    newSquare.area = config.width * config.width;
  &#125;
  <span class="hljs-keyword">return</span> newSquare;
&#125;

<span class="hljs-keyword">let</span> mySquare = createSquare(&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">"black"</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带有可选属性的接口与普通的接口定义差不多，只是在可选属性名字定义的后面加一个?符号。</p>
<p>可选属性的好处之一是可以对可能存在的属性进行预定义，好处之二是可以捕获引用了不存在的属性时的错误。 比如，我们故意将 createSquare里的color属性名拼错，就会得到一个错误提示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SquareConfig &#123;
  color?: <span class="hljs-built_in">string</span>;
  width?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSquare</span>(<span class="hljs-params">config: SquareConfig</span>): </span>&#123; color: <span class="hljs-built_in">string</span>; area: <span class="hljs-built_in">number</span> &#125; &#123;
  <span class="hljs-keyword">let</span> newSquare = &#123;<span class="hljs-attr">color</span>: <span class="hljs-string">"white"</span>, <span class="hljs-attr">area</span>: <span class="hljs-number">100</span>&#125;;
  <span class="hljs-keyword">if</span> (config.clor) &#123;
    <span class="hljs-comment">// Error: Property 'clor' does not exist on type 'SquareConfig'</span>
    newSquare.color = config.clor;
  &#125;
  <span class="hljs-keyword">if</span> (config.width) &#123;
    newSquare.area = config.width * config.width;
  &#125;
  <span class="hljs-keyword">return</span> newSquare;
&#125;

<span class="hljs-keyword">let</span> mySquare = createSquare(&#123;<span class="hljs-attr">color</span>: <span class="hljs-string">"black"</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">只读属性</h2>
<p>一些对象属性只能在对象刚刚创建的时候修改其值。 你可以在属性名前用 readonly来指定只读属性:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123;
    <span class="hljs-keyword">readonly</span> x: <span class="hljs-built_in">number</span>;
    <span class="hljs-keyword">readonly</span> y: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript具有<code>ReadonlyArray<T></code>类型，它与<code>Array<T></code>相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">let</span> ro: ReadonlyArray<<span class="hljs-built_in">number</span>> = a;
ro[<span class="hljs-number">0</span>] = <span class="hljs-number">12</span>; <span class="hljs-comment">// error!</span>
ro.push(<span class="hljs-number">5</span>); <span class="hljs-comment">// error!</span>
ro.length = <span class="hljs-number">100</span>; <span class="hljs-comment">// error!</span>
a = ro; <span class="hljs-comment">// error!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的最后一行，可以看到就算把整个ReadonlyArray赋值到一个普通数组也是不可以的。 但是你可以用类型断言重写：</p>
<pre><code class="hljs language-ts copyable" lang="ts">a = ro <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>[];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">readonly vs const</h2>
<p>最简单判断该用readonly还是const的方法是看要把它做为变量使用还是做为一个属性。 做为变量使用的话用 const，若做为属性则使用readonly。</p>
<h2 data-id="heading-5">额外的属性检查</h2>
<p>我们在第一个例子里使用了接口，TypeScript让我们传入&#123; size: number; label: string; &#125;到仅期望得到&#123; label: string; &#125;的函数里。我们已经学过了可选属性，并且知道他们在“option bags”模式里很有用。</p>
<p>然而，天真地将这两者结合的话并不会像预想的那样。比如，拿 createSquare例子来说：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SquareConfig &#123;
    color?: <span class="hljs-built_in">string</span>;
    width?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSquare</span>(<span class="hljs-params">config: SquareConfig</span>): </span>&#123; color: <span class="hljs-built_in">string</span>; area: <span class="hljs-built_in">number</span> &#125; &#123;
    <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">let</span> mySquare = createSquare(&#123; <span class="hljs-attr">colour</span>: <span class="hljs-string">"red"</span>, <span class="hljs-attr">width</span>: <span class="hljs-number">100</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意传入createSquare的参数拼写为colour而不是color，这段代码在TypeScript中会抛错。对象字面量会被特殊对待而且会经过 额外属性检查，当将它们赋值给变量或作为参数传递的时候。 如果一个对象字面量存在任何“目标类型”不包含的属性时，你会得到一个错误。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// error: 'colour' not expected in type 'SquareConfig'</span>
<span class="hljs-keyword">let</span> mySquare = createSquare(&#123; <span class="hljs-attr">colour</span>: <span class="hljs-string">"red"</span>, <span class="hljs-attr">width</span>: <span class="hljs-number">100</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最佳的方式是能够添加一个字符串索引签名，前提是你能够确定这个对象可能具有某些做为特殊用途使用的额外属性。 如果 SquareConfig带有上面定义的类型的color和width属性，并且还会带有任意数量的其它属性，那么我们可以这样定义它：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SquareConfig &#123;
    color?: <span class="hljs-built_in">string</span>;
    width?: <span class="hljs-built_in">number</span>;
    [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种跳过这些检查的方式，这可能会让你感到惊讶，它就是将这个对象赋值给一个另一个变量： 因为 squareOptions不会经过额外属性检查，所以编译器不会报错。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> squareOptions = &#123; <span class="hljs-attr">colour</span>: <span class="hljs-string">"red"</span>, <span class="hljs-attr">width</span>: <span class="hljs-number">100</span> &#125;;
<span class="hljs-keyword">let</span> mySquare = createSquare(squareOptions);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要留意，在像上面一样的简单代码里，你可能不应该去绕开这些检查。对于包含方法和内部状态的复杂对象字面量来讲，你可能需要使用这些技巧，但是大部额外属性检查错误是真正的bug。就是说你遇到了额外类型检查出的错误，比如“option bags”，你应该去审查一下你的类型声明。在这里，如果支持传入 color或colour属性到createSquare，你应该修改SquareConfig定义来体现出这一点。</p>
<h2 data-id="heading-6">函数类型</h2>
<p>接口能够描述JavaScript中对象拥有的各种各样的外形。除了描述带有属性的普通对象外，接口也可以描述函数类型。</p>
<p>为了使用接口表示函数类型，我们需要给接口定义一个调用签名。它就像是一个只有参数列表和返回值类型的函数定义。参数列表里的每个参数都需要名字和类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> SearchFunc &#123;
  (source: <span class="hljs-built_in">string</span>, <span class="hljs-attr">subString</span>: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样定义后，我们可以像使用其它接口一样使用这个函数类型的接口。 下例展示了如何创建一个函数类型的变量，并将一个同类型的函数赋值给这个变量。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> mySearch: SearchFunc;
mySearch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source: <span class="hljs-built_in">string</span>, subString: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = source.search(subString);
  <span class="hljs-keyword">return</span> result > -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数的参数会逐个进行检查，要求对应位置上的参数类型是兼容的。如果你不想指定类型，TypeScript的类型系统会推断出参数类型，因为函数直接赋值给了 SearchFunc类型变量。 函数的返回值类型是通过其返回值推断出来的（此例是 false和true）。 如果让这个函数返回数字或字符串，类型检查器会警告我们函数的返回值类型与 SearchFunc接口中的定义不匹配。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> mySearch: SearchFunc;
mySearch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">src, sub</span>) </span>&#123;
    <span class="hljs-keyword">let</span> result = src.search(sub);
    <span class="hljs-keyword">return</span> result > -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">可索引的类型</h2>
<p>与使用接口描述函数类型差不多，我们也可以描述那些能够“通过索引得到”的类型，比如a[10]或ageMap["daniel"]。 可索引类型具有一个 索引签名，它描述了对象索引的类型，还有相应的索引返回值类型。 让我们看一个例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> StringArray &#123;
  [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">let</span> myArray: StringArray;
myArray = [<span class="hljs-string">"Bob"</span>, <span class="hljs-string">"Fred"</span>];

<span class="hljs-keyword">let</span> myStr: <span class="hljs-built_in">string</span> = myArray[<span class="hljs-number">0</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子里，我们定义了StringArray接口，它具有索引签名。 这个索引签名表示了当用 number去索引StringArray时会得到string类型的返回值。</p>
<p>TypeScript支持两种索引签名：字符串和数字。 可以同时使用两种类型的索引，但是数字索引的返回值必须是字符串索引返回值类型的子类型。 这是因为当使用 number来索引时，JavaScript会将它转换成string然后再去索引对象。 也就是说用 100（一个number）去索引等同于使用"100"（一个string）去索引，因此两者需要保持一致。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
    <span class="hljs-attr">breed</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-comment">// 错误：使用数值型的字符串索引，有时会得到完全不同的Animal!</span>
<span class="hljs-keyword">interface</span> NotOkay &#123;
    [x: <span class="hljs-built_in">number</span>]: Animal;
    [x: <span class="hljs-built_in">string</span>]: Dog;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串索引签名能够很好的描述dictionary模式，并且它们也会确保所有属性与其返回值类型相匹配。 因为字符串索引声明了 obj.property和obj["property"]两种形式都可以。 下面的例子里， name的类型与字符串索引类型不匹配，所以类型检查器给出一个错误提示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> NumberDictionary &#123;
  [index: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span>;
  length: <span class="hljs-built_in">number</span>;    <span class="hljs-comment">// 可以，length是number类型</span>
  name: <span class="hljs-built_in">string</span>       <span class="hljs-comment">// 错误，`name`的类型与索引类型返回值的类型不匹配</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，你可以将索引签名设置为只读，这样就防止了给索引赋值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ReadonlyStringArray &#123;
  <span class="hljs-keyword">readonly</span> [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">let</span> myArray: ReadonlyStringArray = [<span class="hljs-string">"Alice"</span>, <span class="hljs-string">"Bob"</span>];
myArray[<span class="hljs-number">2</span>] = <span class="hljs-string">"Mallory"</span>; <span class="hljs-comment">// error!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">类类型</h2>
<h3 data-id="heading-9">实现接口</h3>
<p>与C#或Java里接口的基本作用一样，TypeScript也能够用它来明确的强制一个类去符合某种契约。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ClockInterface &#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以在接口中描述一个方法，在类里实现它，如同下面的setTime方法一样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ClockInterface &#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
    setTime(d: <span class="hljs-built_in">Date</span>);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
    <span class="hljs-function"><span class="hljs-title">setTime</span>(<span class="hljs-params">d: <span class="hljs-built_in">Date</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.currentTime = d;
    &#125;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口描述了类的公共部分，而不是公共和私有两部分。它不会帮你检查类是否具有某些私有成员。</p>
<h3 data-id="heading-10">类静态部分与实例部分的区别</h3>
<p>当你操作类和接口的时候，你要知道类是具有两个类型的：静态部分的类型和实例的类型。 你会注意到，当你用构造器签名去定义一个接口并试图定义一个类去实现这个接口时会得到一个错误：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ClockConstructor &#123;
    <span class="hljs-keyword">new</span> (hour: <span class="hljs-built_in">number</span>, <span class="hljs-attr">minute</span>: <span class="hljs-built_in">number</span>);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockConstructor</span> </span>&#123;
    <span class="hljs-attr">currentTime</span>: <span class="hljs-built_in">Date</span>;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里因为当一个类实现了一个接口时，只对其实例部分进行类型检查。constructor存在于类的静态部分，所以不在检查的范围内。</p>
<p>因此，我们应该直接操作类的静态部分。 看下面的例子，我们定义了两个接口， ClockConstructor为构造函数所用和ClockInterface为实例方法所用。 为了方便我们定义一个构造函数 createClock，它用传入的类型创建实例。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ClockConstructor &#123;
    <span class="hljs-keyword">new</span> (hour: <span class="hljs-built_in">number</span>, <span class="hljs-attr">minute</span>: <span class="hljs-built_in">number</span>): ClockInterface;
&#125;
<span class="hljs-keyword">interface</span> ClockInterface &#123;
    tick();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createClock</span>(<span class="hljs-params">ctor: ClockConstructor, hour: <span class="hljs-built_in">number</span>, minute: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ctor(hour, minute);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DigitalClock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">tick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"beep beep"</span>);
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AnalogClock</span> <span class="hljs-title">implements</span> <span class="hljs-title">ClockInterface</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">h: <span class="hljs-built_in">number</span>, m: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">tick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"tick tock"</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> digital = createClock(DigitalClock, <span class="hljs-number">12</span>, <span class="hljs-number">17</span>);
<span class="hljs-keyword">let</span> analog = createClock(AnalogClock, <span class="hljs-number">7</span>, <span class="hljs-number">32</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为createClock的第一个参数是ClockConstructor类型，在createClock(AnalogClock, 7, 32)里，会检查AnalogClock是否符合构造函数签名。</p>
<h2 data-id="heading-11">继承接口</h2>
<p>和类一样，接口也可以相互继承。 这让我们能够从一个接口里复制成员到另一个接口里，可以更灵活地将接口分割到可重用的模块里。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Shape &#123;
    <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> Square <span class="hljs-keyword">extends</span> Shape &#123;
    <span class="hljs-attr">sideLength</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> square = <Square>&#123;&#125;;
square.color = <span class="hljs-string">"blue"</span>;
square.sideLength = <span class="hljs-number">10</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个接口可以继承多个接口，创建出多个接口的合成接口。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Shape &#123;
    <span class="hljs-attr">color</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> PenStroke &#123;
    <span class="hljs-attr">penWidth</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Square <span class="hljs-keyword">extends</span> Shape, PenStroke &#123;
    <span class="hljs-attr">sideLength</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> square = <Square>&#123;&#125;;
square.color = <span class="hljs-string">"blue"</span>;
square.sideLength = <span class="hljs-number">10</span>;
square.penWidth = <span class="hljs-number">5.0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">混合类型</h2>
<p>先前我们提过，接口能够描述JavaScript里丰富的类型。因为JavaScript其动态灵活的特点，有时你会希望一个对象可以同时具有上面提到的多种类型。</p>
<p>一个例子就是，一个对象可以同时做为函数和对象使用，并带有额外的属性。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Counter &#123;
    (start: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">string</span>;
    interval: <span class="hljs-built_in">number</span>;
    reset(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCounter</span>(<span class="hljs-params"></span>): <span class="hljs-title">Counter</span> </span>&#123;
    <span class="hljs-keyword">let</span> counter = <Counter><span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">start: <span class="hljs-built_in">number</span></span>) </span>&#123; &#125;;
    counter.interval = <span class="hljs-number">123</span>;
    counter.reset = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; &#125;;
    <span class="hljs-keyword">return</span> counter;
&#125;

<span class="hljs-keyword">let</span> c = getCounter();
c(<span class="hljs-number">10</span>);
c.reset();
c.interval = <span class="hljs-number">5.0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用JavaScript第三方库的时候，你可能需要像上面那样去完整地定义类型。</p>
<h2 data-id="heading-13">接口继承类</h2>
<p>当接口继承了一个类类型时，它会继承类的成员但不包括其实现。 就好像接口声明了所有类中存在的成员，但并没有提供具体实现一样。 接口同样会继承到类的private和protected成员。 这意味着当你创建了一个接口继承了一个拥有私有或受保护的成员的类时，这个接口类型只能被这个类或其子类所实现（implement）。</p>
<p>当你有一个庞大的继承结构时这很有用，但要指出的是你的代码只在子类拥有特定属性时起作用。 这个子类除了继承至基类外与基类没有任何关系。 例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Control</span> </span>&#123;
    <span class="hljs-keyword">private</span> state: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-keyword">interface</span> SelectableControl <span class="hljs-keyword">extends</span> Control &#123;
    select(): <span class="hljs-built_in">void</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Button</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Control</span> <span class="hljs-title">implements</span> <span class="hljs-title">SelectableControl</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">select</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TextBox</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Control</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">select</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;

<span class="hljs-comment">// 错误：“Image”类型缺少“state”属性。</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Image</span> <span class="hljs-title">implements</span> <span class="hljs-title">SelectableControl</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">select</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Location</span> </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子里，SelectableControl包含了Control的所有成员，包括私有成员state。 因为 state是私有成员，所以只能够是Control的子类们才能实现SelectableControl接口。 因为只有 Control的子类才能够拥有一个声明于Control的私有成员state，这对私有成员的兼容性是必需的。</p>
<p>在Control类内部，是允许通过SelectableControl的实例来访问私有成员state的。 实际上， SelectableControl接口和拥有select方法的Control类是一样的。 Button和TextBox类是SelectableControl的子类（因为它们都继承自Control并有select方法），但Image和Location类并不是这样的。</p>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            