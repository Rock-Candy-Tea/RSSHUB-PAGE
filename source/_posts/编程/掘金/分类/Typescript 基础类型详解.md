
---
title: 'Typescript 基础类型详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4858'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 04:49:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=4858'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Boolean</h2>
<p>布尔类型声明：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> isDone: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Number</h2>
<p>和在<code>JavaScript</code>中一样，<code>TypeScript</code>中的所有数字要么是浮点值，要么是<code>BigIntegers</code>。这些浮点数的类型是<code>number</code>，而<code>BigIntegers</code>的类型是<code>bigint</code>。除了十六进制和十进制，<code>TypeScript</code>还支持<code>ECMAScript 2015</code>引入的二进制和八进制。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> decimal: <span class="hljs-built_in">number</span> = <span class="hljs-number">6</span>;
<span class="hljs-keyword">let</span> hex: <span class="hljs-built_in">number</span> = <span class="hljs-number">0xf00d</span>;
<span class="hljs-keyword">let</span> binary: <span class="hljs-built_in">number</span> = <span class="hljs-number">0b1010</span>;
<span class="hljs-keyword">let</span> octal: <span class="hljs-built_in">number</span> = <span class="hljs-number">0o744</span>;
<span class="hljs-keyword">let</span> big: bigint = <span class="hljs-number">100n</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">String</h2>
<p>在<code>typescript</code>中使用<code>string</code>来定义一个字符串类型的变量，跟<code>javascript</code>一样变量可以使用单引号或者双引号扩起来：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> color: <span class="hljs-built_in">string</span> = <span class="hljs-string">"blue"</span>;
color = <span class="hljs-string">'red'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以使用模版字符串，模版字符串可以跨越多行并且可以有嵌套的表达式。字符串的值使用``反引号括起来，表达式使用<code>$&#123; expr &#125;</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> fullName: <span class="hljs-built_in">string</span> = <span class="hljs-string">`Bob Bobbington`</span>;
<span class="hljs-keyword">let</span> age: <span class="hljs-built_in">number</span> = <span class="hljs-number">37</span>;
<span class="hljs-keyword">let</span> sentence: <span class="hljs-built_in">string</span> =
  <span class="hljs-string">"Hello, my name is "</span> +
  fullName +
  <span class="hljs-string">".\n\n"</span> +
  <span class="hljs-string">"I'll be "</span> +
  (age + <span class="hljs-number">1</span>) +
  <span class="hljs-string">" years old next month."</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Array</h2>
<p>声明数组变量有两种方式，</p>
<p><strong>方式一：</strong> 元素类型 + []</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> list: <span class="hljs-built_in">number</span>[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方式二：</strong> 使用范型类型<code>Array<elemType></code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> list: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Tuple（元组）</h2>
<p>元组用来定义元素个数固定的数组，数组中元素可以有各自的类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Declare a tuple type</span>
<span class="hljs-keyword">let</span> x: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>];
<span class="hljs-comment">// Initialize it</span>
x = [<span class="hljs-string">"hello"</span>, <span class="hljs-number">10</span>]; <span class="hljs-comment">// OK</span>
<span class="hljs-comment">// Initialize it incorrectly</span>
x = [<span class="hljs-number">10</span>, <span class="hljs-string">"hello"</span>]; <span class="hljs-comment">// Error</span>
<span class="hljs-comment">// Type 'number' is not assignable to type 'string'.</span>
<span class="hljs-comment">// Type 'string' is not assignable to type 'number'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当访问一个已知索引的元素，获取到的值的类型是相对应位置的类型:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// OK</span>
<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">0</span>].substring(<span class="hljs-number">1</span>));

<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">1</span>].substring(<span class="hljs-number">1</span>));
<span class="hljs-comment">// Property 'substring' does not exist on type 'number'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过超出元组索引范围的下标访问元组中的值会报错:</p>
<pre><code class="hljs language-ts copyable" lang="ts">x[<span class="hljs-number">3</span>] = <span class="hljs-string">"world"</span>;
<span class="hljs-comment">// Tuple type '[string, number]' of length '2' has no element at index '3'.</span>

<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">5</span>].toString());
<span class="hljs-comment">// Object is possibly 'undefined'.</span>
<span class="hljs-comment">// Tuple type '[string, number]' of length '2' has no element at index '5'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Enum (枚举)</h2>
<p>枚举是 <code>TypeScript</code> 为数不多的不是 <code>JavaScript</code> 类型扩展的特性之一。<code>Typescript</code> 提供数字枚举和基于字符串的枚举。定义枚举使用<code>Enum</code>关键字。</p>
<h3 data-id="heading-6">Numeric enums （数字枚举）</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction &#123;
  Up = <span class="hljs-number">1</span>,
  Down,
  Left,
  Right,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义一个数字枚举类型<code>Direction</code>，第一个元素<code>UP</code>初始值为1，后续元素的值在此基础上自动递增，也就是说·<code>Down =2, Left=3, Right = 4</code>，如果不带初始值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction &#123;
  Up,
  Down,
  Left,
  Right,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时<code>UP</code>初始值为<code>0</code>，后续元素的值在此基础上自动递增。如果我们不关心成员的值，只要他们的值不相同就可以，那自动递增就非常有用了。</p>
<p>或者也可以给每个元素明确的赋值，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Color &#123;
  Red = <span class="hljs-number">1</span>,
  Green = <span class="hljs-number">2</span>,
  Blue = <span class="hljs-number">4</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个方便的特性是还可以通过值来获取到对应值的名称（反向映射后面还会提到）</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Color &#123;
  Red = <span class="hljs-number">1</span>,
  Green,
  Blue,
&#125;
<span class="hljs-keyword">let</span> colorName: <span class="hljs-built_in">string</span> = Color[<span class="hljs-number">2</span>];

<span class="hljs-comment">// Displays 'Green'</span>
<span class="hljs-built_in">console</span>.log(colorName);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用枚举很简单：访问枚举类型的属性，并使用枚举的名称声明类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> UserResponse &#123;
  No = <span class="hljs-number">0</span>,
  Yes = <span class="hljs-number">1</span>,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">respond</span>(<span class="hljs-params">recipient: <span class="hljs-built_in">string</span>, message: UserResponse</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

respond(<span class="hljs-string">"Princess Caroline"</span>, UserResponse.Yes);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有初始化器的枚举要么必须放在第一个，要么必须放在用数字常量或其他常量枚举成员初始化的数字枚举之后。换句话说，以下情况是不允许的:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> E &#123;
  A = getSomeValue(),
  B,
<span class="hljs-comment">// Enum member must have initializer.</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">String enums(字符串枚举)</h3>
<p>字符串枚举的概念与数字枚举类似，但是有一些运行时的差别。字符串枚举类型的成员必须使用字符串或者另一个字符串枚举成员进行常量初始化。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction &#123;
  Up = <span class="hljs-string">"UP"</span>,
  Down = <span class="hljs-string">"DOWN"</span>,
  Left = <span class="hljs-string">"LEFT"</span>,
  Right = <span class="hljs-string">"RIGHT"</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管字符串枚举类型没有自动增长的行为，但字符串枚举的好处是它们可以很好地序列化。换句话说，在调试数字枚举运行时的值时，数字枚举的属性值不能够明确的向我们传达其所代表的意思（尽管有反向映射来获取属性值对应的属性名称），但字符串枚举可以给出一个有意义并且可读性更高的值。这样就不用依赖于枚举成员的名称了。</p>
<h3 data-id="heading-8">Heterogeneous enums （异构枚举）</h3>
<p><code>Typescript</code>的枚举类型是支持混合字符串枚举和数字枚举的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> BooleanLikeHeterogeneousEnum &#123;
  No = <span class="hljs-number">0</span>,
  Yes = <span class="hljs-string">"YES"</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是一般不推荐这样的用法。</p>
<h3 data-id="heading-9">计算成员和常量成员</h3>
<p>每个枚举成员都有一个与之关联的值，可以是常量，也可以是计算值。一个枚举成员在满足下列条件时被认为是常量：</p>
<ul>
<li>如果是枚举中的第一个成员并且没有初始化器，在这种情况下它被初始化为0.
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// E.X is constant:</span>
<span class="hljs-built_in">enum</span> E &#123;
  X,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>没有初始化器并且它前面的枚举成员是一个数值常量。在这种情况下当前枚举成员的值是前面一个枚举成员的值加1。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// All enum members in 'E1' and 'E2' are constant.</span>

<span class="hljs-built_in">enum</span> E1 &#123;
  X,
  Y,
  Z,
&#125;

<span class="hljs-built_in">enum</span> E2 &#123;
  A = <span class="hljs-number">1</span>,
  B,
  C,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>枚举成员使用常量枚举表达式进行初始化。常量枚举表达式是<code>TypeScript</code>表达式的子集，可以在编译时完全求值。一个表达式满足下列条件就是常量枚举表达式：</li>
</ul>
<ol>
<li>字面量枚举表达式(主要是字符串字面量或数字字面量)</li>
<li>对先前定义的常量枚举成员的引用(它可以源自不同的枚举)</li>
<li>带圆括号的常量枚举表达式</li>
<li>用于常量枚举表达式的<code>+、-、~</code>一元运算符之一</li>
<li><code>+, -, *, /, %, <<, >>, >>>, &, |, ^</code>二进制操作符，常量枚举表达式作为操作数</li>
</ol>
<p>如果将常量枚举表达式求值为NaN或Infinity将会得到一个编译时错误。</p>
<p>所有其它情况的枚举成员都被当作是需要计算得出的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> FileAccess &#123;
  <span class="hljs-comment">// constant members</span>
  None,
  Read = <span class="hljs-number">1</span> << <span class="hljs-number">1</span>,
  Write = <span class="hljs-number">1</span> << <span class="hljs-number">2</span>,
  ReadWrite = Read | Write,
  <span class="hljs-comment">// computed member</span>
  G = <span class="hljs-string">"123"</span>.length,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">联合枚举和枚举成员类型（Union enums and enum member types）</h3>
<p>还有一种特殊的常量枚举成员的子集：字面量枚举成员。字面量枚举成员是值没有初始值的常量枚举成员或者初始值被初始化为:</p>
<ul>
<li>任何字符串字面量（例如："foo","bar","baz"）</li>
<li>任何数字字面量（例如：1，100）</li>
<li>或者任何加了一元操作符<code>-</code>号的数字字面量（比如：-1，-100）</li>
</ul>
<p>当枚举中的所有成员都有字面量枚举值时，就会产生一些特殊的语义。</p>
<p><strong>第一，</strong>  枚举成员本身也会成为类型。比如我们可以定义对象的某些成员只能具有枚举成员的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> ShapeKind &#123;
  Circle,
  Square,
&#125;

<span class="hljs-keyword">interface</span> Circle &#123;
  <span class="hljs-attr">kind</span>: ShapeKind.Circle;
  radius: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">interface</span> Square &#123;
  <span class="hljs-attr">kind</span>: ShapeKind.Square;
  sideLength: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> c: Circle = &#123;
  <span class="hljs-attr">kind</span>: ShapeKind.Square,
<span class="hljs-comment">// Type 'ShapeKind.Square' is not assignable to type 'ShapeKind.Circle'.</span>
  <span class="hljs-attr">radius</span>: <span class="hljs-number">100</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第二，</strong> 枚举类型本身实际上变成了每个枚举成员的联合。使用联合枚举，类型系统就能够知道存在于枚举中的确切的值，利用这一点<code>Typescript</code>可以捕获到错误比较的<code>bug</code>，例如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> E &#123;
  Foo,
  Bar,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x: E</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (x !== E.Foo || x !== E.Bar) &#123;
  <span class="hljs-comment">// This condition will always return 'true' since the types 'E.Foo' and 'E.Bar' have no overlap.</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，我们首先比较了 <code>x</code> 是否不等于 <code>E.Foo</code>。 如果这个条件成立，判断就结束了。但是如果不成立那<code>x</code>就是<code>E.Foo</code>。所以后面再去比较<code>E.bar</code>就没有意义了。</p>
<h3 data-id="heading-11">运行时的枚举</h3>
<p>在运行时枚举就是真实的对象，例如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> E &#123;
  X,
  Y,
  Z,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">obj: &#123; X: <span class="hljs-built_in">number</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> obj.X;
&#125;

<span class="hljs-comment">// Works, since 'E' has a property named 'X' which is a number.</span>
f(E);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以直接将枚举当对象使用。</p>
<h3 data-id="heading-12">编译时的枚举</h3>
<p>使用<code>keyof typeof</code>关键字可以获取一个类型，该类型将枚举所有的键表示为字符串。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> LogLevel &#123;
  ERROR,
  WARN,
  INFO,
  DEBUG,
&#125;

<span class="hljs-comment">/**
 * This is equivalent to:
 * type LogLevelStrings = 'ERROR' | 'WARN' | 'INFO' | 'DEBUG';
 */</span>
<span class="hljs-keyword">type</span> LogLevelStrings = keyof <span class="hljs-keyword">typeof</span> LogLevel;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">printImportant</span>(<span class="hljs-params">key: LogLevelStrings, message: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> num = LogLevel[key];
  <span class="hljs-keyword">if</span> (num <= LogLevel.WARN) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Log level key is:"</span>, key);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Log level value is:"</span>, num);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Log level message is:"</span>, message);
  &#125;
&#125;
printImportant(<span class="hljs-string">"ERROR"</span>, <span class="hljs-string">"This is a message"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">反向映射 （Reverse mappings）</h3>
<p>数字枚举类型成员会有一个从值到名字的反向映射，在前面也已经提到过。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Enum &#123;
  A,
&#125;

<span class="hljs-keyword">let</span> a = Enum.A;
<span class="hljs-keyword">let</span> nameOfA = Enum[a]; <span class="hljs-comment">// "A"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Typescript</code>会将这段代码编译成下面的<code>js</code>代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> Enum;
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Enum</span>) </span>&#123;
    Enum[Enum[<span class="hljs-string">"A"</span>] = <span class="hljs-number">0</span>] = <span class="hljs-string">"A"</span>;
&#125;)(Enum || (Enum = &#123;&#125;));
<span class="hljs-keyword">let</span> a = Enum.A;
<span class="hljs-keyword">let</span> nameOfA = Enum[a]; <span class="hljs-comment">// "A"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后的结果是将枚举编译成为一个对象，这个对象既存储了<code>name->value</code>的映射，又存储了<code>value->name</code>的映射。</p>
<p>需要特别注意的一点，字符串枚举不具备这种反向映射能力。</p>
<h4 data-id="heading-14">const 枚举 （const enums）</h4>
<p>常量枚举使用<code>const</code>修饰符定义，并且只能使用常量枚举表达式。不同于一般的枚举类型，如何不存在反向映射的访问，常量枚举在编译阶段会被完全移除掉，只会在使用枚举成员的地方保留枚举成员的值，正是因为没有计算成员，所以能够在编译阶段做到这一点。看个例子就明白了：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> Direction &#123;
  Up,
  Down,
  Left,
  Right,
&#125;

<span class="hljs-keyword">let</span> directions = [
  Direction.Up,
  Direction.Down,
  Direction.Left,
  Direction.Right,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子只存在对枚举成员的访问没有反向访问的情况（比如 <code>Direction[0]</code>，如果没有使用常量枚举编译后的<code>js</code>代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Direction;
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Direction</span>) </span>&#123;
    Direction[Direction[<span class="hljs-string">"Up"</span>] = <span class="hljs-number">0</span>] = <span class="hljs-string">"Up"</span>;
    Direction[Direction[<span class="hljs-string">"Down"</span>] = <span class="hljs-number">1</span>] = <span class="hljs-string">"Down"</span>;
    Direction[Direction[<span class="hljs-string">"Left"</span>] = <span class="hljs-number">2</span>] = <span class="hljs-string">"Left"</span>;
    Direction[Direction[<span class="hljs-string">"Right"</span>] = <span class="hljs-number">3</span>] = <span class="hljs-string">"Right"</span>;
&#125;)(Direction || (Direction = &#123;&#125;));
<span class="hljs-keyword">var</span> directions = [
    Direction.Up,
    Direction.Down,
    Direction.Left,
    Direction.Right,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>const</code> 定义常量枚举类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> <span class="hljs-built_in">enum</span> Direction &#123;
  Up,
  Down,
  Left,
  Right,
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后的<code>js</code>代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> directions = [
    <span class="hljs-number">0</span> <span class="hljs-comment">/* Up */</span>,
    <span class="hljs-number">1</span> <span class="hljs-comment">/* Down */</span>,
    <span class="hljs-number">2</span> <span class="hljs-comment">/* Left */</span>,
    <span class="hljs-number">3</span> <span class="hljs-comment">/* Right */</span>,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的好处是显而易见的，没有了反向映射的额外代码，最终的代码变少了。</p>
<h3 data-id="heading-15">外部枚举 （Ambient enums）</h3>
<p>外部枚举被用来描述已经存在的枚举类型的，也就说：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Note: Assume no other file has actually created a Foo var at runtime</span>
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">enum</span> Foo &#123; Bar &#125; 
<span class="hljs-keyword">var</span> s = <span class="hljs-string">'Bar'</span>;
<span class="hljs-keyword">var</span> b = Foo[s]; <span class="hljs-comment">// Fails</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假定没有在其他地方定义过<code>Foo</code>枚举类型，这段代码不会在编译时报错，但是会在运行时报错，因为没有定义<code>Foo</code>枚举类型。</p>
<p>外部枚举和非外部枚举的一个重要区别是，在非外部枚举中，如果前一个枚举成员是常量，那么没有初始化式的成员将被认为是常量。相反，没有初始化式的外部(并且非<code>const</code>)枚举成员总是被当作计计算枚举成员。</p>
<h2 data-id="heading-16">Unknown</h2>
<p>当定义不知道的变量类型的时候可以将变量的类型定义为<code>unknown</code>。<code>unknown</code>就是告诉编译器当前变量可能是任何类型的值，我们现在不知道变量的类型所以给它一个<code>unknow</code>的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> notSure: unknown = <span class="hljs-number">4</span>;
notSure = <span class="hljs-string">"maybe a string instead"</span>;

<span class="hljs-comment">// OK, definitely a boolean</span>
notSure = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个unknown类型的变量，可以通过<code>typeof</code>、比较检查或更高级的类型保护将其缩小到更具体的范围：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> maybe: unknown;
<span class="hljs-comment">// 'maybe' could be a string, object, boolean, undefined, or other types</span>
<span class="hljs-keyword">const</span> aNumber: <span class="hljs-built_in">number</span> = maybe;
<span class="hljs-comment">// Type 'unknown' is not assignable to type 'number'.</span>

<span class="hljs-keyword">if</span> (maybe === <span class="hljs-literal">true</span>) &#123;
  <span class="hljs-comment">// TypeScript knows that maybe is a boolean now</span>
  <span class="hljs-keyword">const</span> aBoolean: <span class="hljs-built_in">boolean</span> = maybe;
  <span class="hljs-comment">// So, it cannot be a string</span>
  <span class="hljs-keyword">const</span> aString: <span class="hljs-built_in">string</span> = maybe;
<span class="hljs-comment">// Type 'boolean' is not assignable to type 'string'.</span>
&#125;

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> maybe === <span class="hljs-string">"string"</span>) &#123;
  <span class="hljs-comment">// TypeScript knows that maybe is a string</span>
  <span class="hljs-keyword">const</span> aString: <span class="hljs-built_in">string</span> = maybe;
  <span class="hljs-comment">// So, it cannot be a boolean</span>
  <span class="hljs-keyword">const</span> aBoolean: <span class="hljs-built_in">boolean</span> = maybe;
<span class="hljs-comment">// Type 'string' is not assignable to type 'boolean'.</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">Any</h2>
<p>当你想绕过类型检查的时候可以使用<code>any</code>类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span>(<span class="hljs-params">key: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">any</span></span>;
<span class="hljs-comment">// OK, return value of 'getValue' is not checked</span>
<span class="hljs-keyword">const</span> str: <span class="hljs-built_in">string</span> = getValue(<span class="hljs-string">"myString"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与<code>unknown</code>的区别是，当定一个变量为<code>any</code>类型的时候，可以访问这个变量的任意属性，<code>ts</code>不会检查属性是否存在和属性的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> looselyTyped: <span class="hljs-built_in">any</span> = <span class="hljs-number">4</span>;
<span class="hljs-comment">// OK, ifItExists might exist at runtime</span>
looselyTyped.ifItExists();
<span class="hljs-comment">// OK, toFixed exists (but the compiler doesn't check)</span>
looselyTyped.toFixed();

<span class="hljs-keyword">let</span> strictlyTyped: unknown = <span class="hljs-number">4</span>;
strictlyTyped.toFixed();
<span class="hljs-comment">// Object is of type 'unknown'.</span>

<span class="hljs-keyword">let</span> looselyTyped: <span class="hljs-built_in">any</span> = &#123;&#125;;
<span class="hljs-keyword">let</span> d = looselyTyped.a.b.c.d;
<span class="hljs-comment">// let d: any</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然使用<code>any</code>有这些便利，但是是以牺牲类型安全为代价的，这样就违背了使用<code>Typescript</code>的初衷了，总之能避免使用<code>any</code>就尽量避免。</p>
<h2 data-id="heading-18">Void</h2>
<p><code>void</code>类型有点像是<code>any</code>的反面，表示没有任何类型。通常在定义一个没有返回值的函数时会使用到：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">warnUser</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"This is my warning message"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将一个变量声明为<code>void</code>用处不大，因为只能赋值为<code>null</code>（没有指定<code>--strictNullChecks</code>的情况下）或者<code>undefined</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> unusable: <span class="hljs-built_in">void</span> = <span class="hljs-literal">undefined</span>;
<span class="hljs-comment">// OK if `--strictNullChecks` is not given</span>
unusable = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">Null 和 Undefined</h2>
<p>在<code>Typescript</code>中，值<code>null</code>和<code>undefined</code>都有自己的类型，分别为<code>null</code> 和 <code>undefined</code>。如果当前变量声明为<code>null</code>或者<code>undefined</code>时，也只能分别赋值为<code>null</code>和<code>undefined</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Not much else we can assign to these variables!</span>
<span class="hljs-keyword">let</span> u: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">let</span> n: <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型<code>null</code>和<code>undefined</code>是其他类型的子类型，比如可以将<code>null</code> 或者 <code>undefined</code>赋值给<code>number</code>类型的变量。</p>
<p>但是如果使用<code>--strictNullChecks</code>，<code>null</code>和<code>undefined</code>就只能赋值给<code>unknown</code>、<code>any</code> 还有他们各自的类型<code>null</code>和<code>undefined</code>的变量（<code>undefined</code>还可以赋值给<code>void</code>类型的变量）。</p>
<h2 data-id="heading-20">Never</h2>
<p><code>never</code>表示永远不会出现的值的类型。 比如一个函数永远不会返回或者总是抛出错误那么就可以将这个函数的返回值类型定义为<code>never</code>类型。当变量被永不为真的类型守卫所约束时也会获得<code>never</code>类型。</p>
<p><code>never</code>类型是任何类型的子类型，可以赋值给任何类型。但是只有<code>never</code>可以赋值给<code>never</code>，<code>any</code>类型也不能赋值给<code>never</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Function returning never must not have a reachable end point</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">error</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(message);
&#125;

<span class="hljs-comment">// Inferred return type is never</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fail</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> error(<span class="hljs-string">"Something failed"</span>);
&#125;

<span class="hljs-comment">// Function returning never must not have a reachable end point</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">infiniteLoop</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>never</code> 的使用场景：</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Foo &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'foo'</span>
&#125;

<span class="hljs-keyword">interface</span> Bar &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>
&#125;

<span class="hljs-keyword">type</span> All = Foo | Bar

<span class="hljs-comment">// 在 switch 当中判断 type，TS 是可以收窄类型的 (discriminated union)：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleValue</span>(<span class="hljs-params">val: All</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (val.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'foo'</span>:
      <span class="hljs-comment">// 这里 val 被收窄为 Foo</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'bar'</span>:
      <span class="hljs-comment">// val 在这里是 Bar</span>
      <span class="hljs-keyword">break</span>
    <span class="hljs-attr">default</span>:
      <span class="hljs-comment">// val 在这里是 never</span>
      <span class="hljs-keyword">const</span> exhaustiveCheck: <span class="hljs-built_in">never</span> = val
      <span class="hljs-keyword">break</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>
如果增加一个新的类型，但是没有在<code>switch</code>中处理：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> All = Foo | Bar | Baz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>
最终<code>default</code> 里面的<code>val</code>就被收窄为<code>Baz</code>， 因为没有任何类型可以赋值给<code>never</code>（除了<code>never</code>自己）导致这里无法通过编译。通过这个办法可以确保 <code>handleValue</code> 总是穷尽 (<code>exhaust</code>) 了所有 <code>All</code> 的可能类型。</p>
<h2 data-id="heading-21">Object</h2>
<p><code>object</code>表示非原始类型，也就是除<code>number</code>，<code>string</code>，<code>boolean</code>，<code>symbol</code>，<code>null</code>或<code>undefined</code>之外的类型。</p>
<p>使用<code>object</code>类型就可以更好的表示像<code>Object.create</code>这样的<code>API</code>。例如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">o: <span class="hljs-built_in">object</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">void</span></span>;

<span class="hljs-comment">// OK</span>
create(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-number">0</span> &#125;);
create(<span class="hljs-literal">null</span>);
create(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// with `--strictNullChecks` flag enabled, undefined is not a subtype of null</span>
<span class="hljs-comment">// Argument of type 'undefined' is not assignable to parameter of type 'object | null'.</span>

create(<span class="hljs-number">42</span>);
<span class="hljs-comment">// Argument of type '42' is not assignable to parameter of type 'object | null'.</span>
create(<span class="hljs-string">"string"</span>);
<span class="hljs-comment">// Argument of type '"string"' is not assignable to parameter of type 'object | null'.</span>
create(<span class="hljs-literal">false</span>);
<span class="hljs-comment">// Argument of type 'false' is not assignable to parameter of type 'object | null'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>## Type assertions （类型断言）</p>
<p>有时候当我们明确的知道某个值的类型，然后想告诉编译器将这个值按照某种类型处理时就可以使用类型断言，类型断言只用于编译阶段的类型检查，不会对值做任何运行时的转换。</p>
<p>有两种方式可以做类型断言：</p>
<p><strong>使用as语法</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: unknown = <span class="hljs-string">"this is a string"</span>;

<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (someValue <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用尖括号语法</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: unknown = <span class="hljs-string">"this is a string"</span>;
<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>someValue).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两种方式是等效的，喜欢那种方式看个人喜好，需要注意的是在<code>JSX</code>中只能使用<code>as</code>语法</p>
<p>## 关于 <code>Number</code>,<code>String</code>,<code>Boolean</code>,<code>Symbol</code>, <code>Object</code></p>
<p>需要区分<code>Number</code>,<code>String</code>,<code>Boolean</code>,<code>Symbol</code>, <code>Object</code>和小写的<code>number</code>,<code>string</code>,<code>boolean</code>,<code>symbol</code>, <code>object</code>，只有小写形式可以作为类型。</p>
<h2 data-id="heading-22">参考资料</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fenums.html%23numeric-enums" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/enums.html#numeric-enums" ref="nofollow noopener noreferrer">Enums</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fbasic-types.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/basic-types.html" ref="nofollow noopener noreferrer">Basic Types</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F354601204" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/354601204" ref="nofollow noopener noreferrer">TypeScript中的never类型具体有什么用？</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F28818849%2Fhow-do-the-different-enum-variants-work-in-typescript" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/28818849/how-do-the-different-enum-variants-work-in-typescript" ref="nofollow noopener noreferrer">How do the different enum variants work in TypeScript?</a></li>
</ol></div>  
</div>
            