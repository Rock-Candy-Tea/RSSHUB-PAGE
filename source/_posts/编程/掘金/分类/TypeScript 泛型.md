
---
title: 'TypeScript 泛型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd43a5a37a54a0f9fe490ee185f5ec3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 08:49:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd43a5a37a54a0f9fe490ee185f5ec3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 泛型是什么？</h2>
<ul>
<li>
<p>官方的定义是：</p>
<blockquote>
<p>**泛型（Generics）**是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性。</p>
</blockquote>
</li>
<li>
<p>通俗的解释是：泛型是类型系统中的<strong>参数</strong>，就像函数的参数一样，只不过函数的参数传递的是值，而泛型传递的是<strong>类型</strong>。他只出现在现在<strong>函数</strong>，<strong>接口</strong>，和<strong>类</strong>中，主要作用是为了类型的复用。</p>
</li>
</ul>
<ul>
<li>设计泛型的关键目的：是在成员之间提供有意义的约束，这些成员可以是：函数参数、函数返回值、类的实例成员和类的方法。</li>
</ul>
<p>可能这么讲会有一些抽象，接下来我们以泛型函数为例，举一个简单的例子：</p>
<ol>
<li>首先我们来定义一个通用的 <code>identity</code> 函数，该函数接收一个<code>number</code>类型的参数，并直接返回这个值：</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span>(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;
identity(<span class="hljs-number">1</span>); <span class="hljs-comment">// ok</span>

identity(<span class="hljs-string">"hello"</span>); <span class="hljs-comment">// error</span>
<span class="hljs-comment">// 编译器报错： Argument of type 'string' is not assignable to parameter of type 'number'.ts(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>现在，<code>identity</code> 函数能且只能传入 <code>number</code> 类型的参数，如果我想传入 <code>string</code> 类型的 <code>TypeScript</code> 编译器会报错，那么该怎么办呢？或许你会想到 <code>any</code> 类型。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span>(<span class="hljs-params">value: <span class="hljs-built_in">any</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;
identity(<span class="hljs-number">1</span>); <span class="hljs-comment">// ok</span>
identity(<span class="hljs-string">"hello"</span>); <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>好吧，传入 <code>any</code> 确实可以生效，但我们失去了定义应该返回哪种类型的能力，并且在这个过程中也丧失了 <code>TypeScript</code> 的类型保护作用。我们的目标是让 <code>identity</code> 函数可以适用于任何特定的类型，为了实现这个目标，我们可以使用 <strong>泛型函数</strong> 来解决这个问题：</li>
</ol>
<h2 data-id="heading-1">2. 泛型函数</h2>
<p>定义泛型函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;
identity<<span class="hljs-built_in">number</span>>(<span class="hljs-number">1</span>); <span class="hljs-comment">// ok</span>
identity<<span class="hljs-built_in">string</span>>(<span class="hljs-string">"hello"</span>); <span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于刚接触 <code>TypeScript</code> 泛型的读者来说，首次看到 <code><T></code> 语法会感到陌生。但这没什么可担心的，就像传递参数一样，通过参数变量 <code>T</code>，把用户想要传入的类型，链式传递到后面函数的类型定义中去。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd43a5a37a54a0f9fe490ee185f5ec3~tplv-k3u1fbpfcp-zoom-1.image" alt="泛型传递" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源：<a href="https://juejin.cn/post/6844904184894980104" target="_blank">掘金阿宝哥</a>）</p>
<p>参考上面的图片，通过 <code><T></code> 声明 <strong>类型变量 <code>T</code></strong>，然后在后面的函数参数类型声明、和函数返回值类型声明中使用：<code>(value: T): T</code>。</p>
<p>理论上，<code>< ></code>类可以声明任意字符作为类型变量，但在定义泛型时通常用<code>T</code>作为类型变量名称，其中 <code>T</code> 代表 <code>Type</code>。当然，除了 <code>T</code> 之外，以下是常见泛型变量代表的意思：</p>
<ul>
<li>K（Key）：表示对象中的键类型。</li>
<li>V（Value）：表示对象中的值类型。</li>
<li>E（Element）：表示元素类型。</li>
<li>U（T 后面的字符）：表示第二个类型参数（以此类推）。</li>
</ul>
<p>很多时候并不是只能定义一个类型变量，我们可以引入更多的类型变量。比如我们引入一个新的类型变量 <code>U</code>，用于扩展我们定义的 <code>identity</code> 函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">value: T, message: U</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(message);
  <span class="hljs-keyword">return</span> value;
&#125;

<span class="hljs-built_in">console</span>.log(identity<<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">string</span>>(<span class="hljs-number">100</span>, <span class="hljs-string">"Hello Generics"</span>));
<span class="hljs-comment">// Hello Generics</span>
<span class="hljs-comment">// 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a44e54466504b35bf0506493340304e~tplv-k3u1fbpfcp-zoom-1.image" alt="泛型传递" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源：<a href="https://juejin.cn/post/6844904184894980104" target="_blank">掘金阿宝哥</a>）</p>
<p>除了为类型变量显式设定值之外，一种更常见的做法是使编译器自动选择这些类型，从而使代码更简洁。我们可以完全省略尖括号，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">value: T, message: U</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(message);
  <span class="hljs-keyword">return</span> value;
&#125;

<span class="hljs-built_in">console</span>.log(identity(<span class="hljs-number">100</span>, <span class="hljs-string">"Hello Generics"</span>));
<span class="hljs-comment">// Hello Generics</span>
<span class="hljs-comment">// 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. 泛型接口</h2>
<p>定义泛型接口：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> GenericInterface<T> &#123;
  <span class="hljs-attr">data</span>: T;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口泛型的使用方式和函数类似，我们可以通过<code><T></code>来声明参数变量<code>T</code>，并将其用在后面接口属性的类型定义上。</p>
<p>泛型接口常用于定义那些，需要用户自定义类型的对象上，最常见的就是 网络请求的响应对象了，以<code>Axios</code>为例：
假设我们通过 <code>axios.get</code> 发起网络请求，我们可以通过<code>axios.get<DataType></code>传入<code>data</code>的类型，最后拿响应 <code>res</code> 时，我们就可以明确的知道<code>data</code>的数据类型 ：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> DataType &#123;
  <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>;
  message: <span class="hljs-built_in">string</span>;
&#125;
axios.get<DataType>(<span class="hljs-string">"https://www.xxx.com"</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res.data.message);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>axios</code>实例，以及响应<code>res</code>的泛型接口如下定义：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> AxiosInstance &#123;
  <span class="hljs-comment">// ...</span>
  get<T = <span class="hljs-built_in">any</span>, R = AxiosResponse<T>>(
    url: <span class="hljs-built_in">string</span>,
    config?: AxiosRequestConfig
  ): <span class="hljs-built_in">Promise</span><R>;
&#125;

<span class="hljs-keyword">interface</span> AxiosResponse<T = any> &#123;
  <span class="hljs-attr">data</span>: T;
  status: <span class="hljs-built_in">number</span>;
  statusText: <span class="hljs-built_in">string</span>;
  headers: <span class="hljs-built_in">any</span>;
  config: AxiosRequestConfig;
  request?: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中响应的 <code>data</code> 是 <code>axios</code> 不知道的，所以 <code>axios</code> 通过泛型的方式，将类型<code>T</code>传递给后面的<code>data</code>属性。</p>
<h2 data-id="heading-3">4. 泛型类</h2>
<p>在类中使用泛型也很简单，我们只需要在类名后面，使用 <code><T, ...></code> 的语法定义任意多个类型变量。</p>
<p>定义泛型类：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> GenericInterface<U> &#123;
  <span class="hljs-attr">value</span>: U;
  getValue: <span class="hljs-function">() =></span> U;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GenericClass</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">GenericInterface</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-attr">value</span>: T;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value: T</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.value = value;
  &#125;

  getValue(): T &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value;
  &#125;
&#125;

<span class="hljs-keyword">const</span> myNumberClass = <span class="hljs-keyword">new</span> GenericClass<<span class="hljs-built_in">number</span>>(<span class="hljs-number">10</span>);
<span class="hljs-built_in">console</span>.log(myNumberClass.getValue()); <span class="hljs-comment">// 10</span>

<span class="hljs-keyword">const</span> myStringClass = <span class="hljs-keyword">new</span> GenericClass<<span class="hljs-built_in">string</span>>(<span class="hljs-string">"Hello Generics!"</span>);
<span class="hljs-built_in">console</span>.log(myStringClass.getValue()); <span class="hljs-comment">// Hello Generics!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们以实例化 <code>myNumberClass</code> 为例，来分析一下其调用过程：</p>
<ol>
<li>在实例化 <code>GenericClass</code> 对象时，我们传入 <code>number</code> 类型和构造函数参数值 68；</li>
<li>之后在 <code>GenericClass</code> 类中，类型变量 <code>T</code> 的值变成 <code>number</code> 类型；</li>
<li><code>GenericClass</code> 类实现了 <code>GenericInterface<T></code>，而此时 <code>T</code> 表示 <code>number</code> 类型，因此等价于该类实现了 <code>GenericInterface<number></code> 接口；</li>
<li>而对于 <code>GenericInterface<U></code> 接口来说，类型变量 <code>U</code> 也变成了 <code>number</code>。这里我有意使用不同的变量名，以表明类型值沿链向上传播，且与变量名无关。</li>
</ol>
<h2 data-id="heading-4">5. 泛型约束</h2>
<p>有时候我们希望限制泛型变量接受的类型（比如我只希望接受拥有<code>.length</code>属性的类型），我们就需要<strong>泛型约束</strong>。下面我们来举几个例子，介绍一下如何使用泛型约束。</p>
<h3 data-id="heading-5">5.1 确保属性存在</h3>
<p>有时候，我们希望类型变量对应的类型上存在某些属性。这时，除非我们显式地将特定属性定义为类型变量，否则编译器不会知道它们的存在。
一个很好的例子是在处理字符串或数组时，我们会假设 <code>length</code> 属性是可用的。让我们再次使用 <code>identity</code> 函数并尝试输出参数的长度：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(arg.length); <span class="hljs-comment">// error: T doesn't have .length</span>
  <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，编译器将不会知道 <code>T</code> 确实含有 <code>length</code> 属性，尤其是在可以将任何类型赋给类型变量 <code>T</code> 的情况下。我们需要做的就是让类型变量 <code>extends</code> 一个含有我们所需属性的接口，比如这样：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Length &#123;
  <span class="hljs-attr">length</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Length</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(arg.length); <span class="hljs-comment">// ok: 可以获取length属性</span>
  <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>T extends Length</code> 用于告诉编译器，我们支持已经实现 <code>Length</code> 接口的任何类型。</p>
<p>之后，当我们使用不含有 <code>length</code> 属性的对象作为参数调用 <code>identity</code> 函数时，<code>TypeScript</code> 会提示相关的错误信息：</p>
<pre><code class="hljs language-ts copyable" lang="ts">identity(<span class="hljs-number">10</span>); <span class="hljs-comment">// Error</span>
<span class="hljs-comment">// Argument of type '68' is not assignable to parameter of type 'Length'.(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.2 检查对象上的键是否存在</h3>
<p>泛型约束的另一个常见的使用场景就是检查对象上的键是否存在。不过在看具体示例之前，我们得来了解一下 <code>keyof</code> 操作符，该操作符可以用于<strong>获取某种类型的所有键</strong>，其返回类型是<strong>联合类型</strong>。我们来举个 <code>keyof</code> 的使用示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Person &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  age: <span class="hljs-built_in">number</span>;
  location: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">type</span> K1 = keyof Person; <span class="hljs-comment">// "name" | "age" | "location"</span>
<span class="hljs-keyword">type</span> K2 = keyof Person[]; <span class="hljs-comment">// number | "length" | "push" | "concat" | ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>keyof</code> 操作符，我们就可以获取指定类型的所有键，之后我们就可以结合前面介绍的 <code>extends</code> 约束，即限制输入的属性名包含在 <code>keyof</code> 返回的联合类型中。具体的使用方式如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProperty</span><<span class="hljs-title">T</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">obj: T, key: K</span>): <span class="hljs-title">T</span>[<span class="hljs-title">K</span>] </span>&#123;
  <span class="hljs-keyword">return</span> obj[key];
&#125;

<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>,
&#125;;

getProperty(obj, <span class="hljs-string">"name"</span>); <span class="hljs-comment">// ok</span>
getProperty(obj, <span class="hljs-string">"age"</span>); <span class="hljs-comment">// error 属性名 age 不存在 obj 上</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上的 <code>getProperty</code> 函数中，我们通过<code> K extends keyof T</code> 确保参数 <code>key</code> 一定是对象中含有的键，这样就不会发生运行时错误。这是一个类型安全的解决方案，与简单调用 <code>let value = obj[key];</code> 不同。</p>
<p>在以上示例中，对于 <code>getProperty(obj, "age")</code> 这个表达式，<code>TypeScript</code> 编译器会提示以下错误信息：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 编译器报错：Argument of type '"age"' is not assignable to parameter of type '"name"'.ts(2345)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显通过使用泛型约束，在编译阶段我们就可以提前发现错误，大大提高了程序的健壮性和稳定性。</p>
<h2 data-id="heading-7">6. 泛型参数默认类型</h2>
<p>我们都知道 <code>JavaScript</code> 的函数参数可以设置初始值（<code>defalut value</code>），类似地，我们也可以为泛型参数设置默认类型。当使用泛型时没有在代码中直接指定类型参数，从实际值参数中也无法推断出类型时，这个默认类型就会起作用。
泛型参数默认类型与普通函数默认值类似，对应的语法很简单，即 <code><T=Default Type></code>，对应的使用示例如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> MyObject<T = string> &#123;
  <span class="hljs-attr">id</span>: T;
&#125;

<span class="hljs-keyword">const</span> numObject: MyObject = &#123; <span class="hljs-attr">id</span>: <span class="hljs-string">"abc"</span> &#125;;
<span class="hljs-keyword">const</span> strObject: MyObject<<span class="hljs-built_in">number</span>> = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">123</span> &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>泛型参数的默认类型遵循以下规则：</p>
<ul>
<li>有默认类型的类型参数被认为是<strong>可选的</strong>。</li>
<li>必选的类型参数不能在可选的类型参数后。</li>
<li>如果类型参数有约束，类型参数的默认类型必须满足这个约束。</li>
<li>当指定类型实参时，你只需要指定必选类型参数的类型实参。 未指定的类型参数会被解析为它们的默认类型。</li>
<li>如果指定了默认类型，且类型推断无法选择一个候选类型，那么将使用默认类型作为推断结果。</li>
<li>一个被现有类或接口合并的类或者接口的声明可以为现有类型参数引入默认类型。</li>
<li>一个被现有类或接口合并的类或者接口的声明可以引入新的类型参数，只要它指定了默认类型。</li>
</ul>
<h2 data-id="heading-8">7. 泛型条件类型</h2>
<p>通过<strong>泛型条件类型</strong>，我们可以根据某些条件得到不同的类型，这里所说的条件是类型兼容性约束。尽管以上代码中使用了 <code>extends</code> 关键字，也不一定要强制满足继承关系，而是检查是否满足结构兼容性。</p>
<p>条件类型会以一个条件表达式进行类型关系检测，从而在两种类型中选择其一：
<code>T extends U ? X : Y</code>
以上表达式的意思是：若 <code>T</code> 能够赋值给 <code>U</code>（<code>T</code> 属于与 <code>U</code>的子类），那么类型是 <code>X</code>，否则为 <code>Y</code>。在条件类型表达式中，我们通常还会结合 <code>infer</code> 关键字，实现类型抽取：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> MyObject<T = any> &#123;
  <span class="hljs-attr">key</span>: T;
&#125;

<span class="hljs-keyword">type</span> StrObject = MyObject<<span class="hljs-built_in">string</span>>;
<span class="hljs-keyword">type</span> NumObject = MyObject<<span class="hljs-built_in">number</span>>;

<span class="hljs-keyword">type</span> ObjectMember<T> = T <span class="hljs-keyword">extends</span> MyObject<infer V> ? V : <span class="hljs-built_in">never</span>;
<span class="hljs-keyword">type</span> StrObjectMember = ObjectMember<StrObject>; <span class="hljs-comment">// string</span>
<span class="hljs-keyword">type</span> NumObjectMember = ObjectMember<NumObject>; <span class="hljs-comment">// number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面示例中，当类型 <code>T</code> 满足 <code>T extends MyObject</code> 约束时，我们会使用 <code>infer</code> 关键字声明了一个类型变量 <code>V</code>，并返回该类型，否则返回 <code>never</code> 类型。</p>
<h2 data-id="heading-9">8. 参考文章</h2>
<ul>
<li><a href="https://typescript.bootcss.com/basic-types.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript 中文手册</a></li>
<li><a href="https://juejin.cn/post/6872111128135073806#heading-28" target="_blank">一份不可多得的 TS 学习指南</a></li>
</ul></div>  
</div>
            