
---
title: '来看看TypeScript 4.3.5 的一些新增属性吧～'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a559b75c4f2a46f8bd931641f9f76106~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:20:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a559b75c4f2a46f8bd931641f9f76106~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://www.typescriptlang.org/play?ts=4.3.5" target="_blank" rel="nofollow noopener noreferrer">4.3.5 playground地址</a></p>
<p><a href="https://www.typescriptlang.org/play?ts=4.2.3" target="_blank" rel="nofollow noopener noreferrer">4.2.3 playground地址</a></p>
<h2 data-id="heading-0">模版字符串的ts</h2>
<ol>
<li>typescript 帮我们推断出字符串</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Colors = <span class="hljs-string">"red"</span> | <span class="hljs-string">"green"</span>;
<span class="hljs-keyword">type</span> Size = <span class="hljs-string">"big"</span> | <span class="hljs-string">"small"</span>;
<span class="hljs-keyword">type</span> Result = <span class="hljs-string">`<span class="hljs-subst">$&#123;Colors | Size&#125;</span> fish`</span>; <span class="hljs-comment">// "red fish" | "green fish" | "big fish" | "small fish"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在函数中使用</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 模版字符串</span>
<span class="hljs-keyword">const</span> Demo = (s: <span class="hljs-built_in">string</span>): <span class="hljs-string">`hahaha <span class="hljs-subst">$&#123;<span class="hljs-built_in">string</span>&#125;</span>`</span> => &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`hahaha <span class="hljs-subst">$&#123;s&#125;</span>`</span>;
&#125;;

<span class="hljs-keyword">type</span> DemoType = <span class="hljs-keyword">typeof</span> Demo; <span class="hljs-comment">// type Demo = (s: string) => `hahaha $&#123;string&#125;`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">“#” 声明私有属性/方法</h2>
<p>在类中使用 “#” 使得属性/方法 在运行时成为真正的私有元素</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    age = <span class="hljs-number">58</span>
    <span class="hljs-keyword">private</span> length = <span class="hljs-string">"吐司"</span>
    #name = <span class="hljs-string">"吐司"</span>
    <span class="hljs-keyword">static</span> #staticName = <span class="hljs-string">"吐司"</span>

    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello world'</span>)
    &#125;

    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">sayYes</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'yes'</span>)
    &#125;

    #<span class="hljs-function"><span class="hljs-title">sayNo</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'No'</span>)
    &#125;

&#125;

<span class="hljs-comment">// 属性</span>
<span class="hljs-keyword">new</span> Foo().age
<span class="hljs-keyword">new</span> Foo().length    
<span class="hljs-comment">//        ~~~~~~</span>
<span class="hljs-comment">// Property 'length' is private and only accessible within class 'Foo'.</span>
<span class="hljs-keyword">new</span> Foo().staticName  
<span class="hljs-comment">//        ~~~~~~</span>
<span class="hljs-comment">// Property 'staticName' does not exist on type 'Foo'.</span>
<span class="hljs-keyword">new</span> Foo().name  
<span class="hljs-comment">//       ~~~~~~</span>
<span class="hljs-comment">// Property 'name' does not exist on type 'Foo'.</span>

<span class="hljs-comment">// 方法</span>
<span class="hljs-keyword">new</span> Foo().sayHello()
<span class="hljs-keyword">new</span> Foo().sayYes()  
<span class="hljs-comment">//        ~~~~~~</span>
<span class="hljs-comment">// Property 'sayYes' is private and only accessible within class 'Foo'.</span>
<span class="hljs-keyword">new</span> Foo().sayNo()   
<span class="hljs-comment">//        ~~~~~~</span>
<span class="hljs-comment">// Property 'sayNo' does not exist on type 'Foo'</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>继承的子类也不能访问</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FooChild</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">sayFatherAge</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.length)  
        <span class="hljs-comment">//               ~~~~~~</span>
        <span class="hljs-comment">// Property 'length' is private and only accessible within class 'Foo'.</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.staticName)  
        <span class="hljs-comment">//               ~~~~~~~~~</span>
        <span class="hljs-comment">// Property 'staticName' does not exist on type 'FooChild'.</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">抽象类 ConstructorParameters</h2>
<p>ConstructorParameters 帮我们获取抽象类的 constructor 参数</p>
<p>(<a href="https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-classes-and-members" target="_blank" rel="nofollow noopener noreferrer">抽象类文档直达</a>)</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CCC</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span>, beauty: <span class="hljs-built_in">boolean</span></span>)</span>&#123;
    &#125;

    <span class="hljs-keyword">abstract</span> getName(): <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">type</span> CCCType = ConstructorParameters<<span class="hljs-keyword">typeof</span> CCC> <span class="hljs-comment">// [name: string, age: number, beauty: boolean]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">第二个泛型</h2>
<p>4.2及之前版本如下代码不能正确识别 第二个泛型C</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 4.2 及以前, 写法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeUnique</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">String</span> | <span class="hljs-title">Number</span>>(<span class="hljs-params">collection: <span class="hljs-built_in">Set</span><T> | T[]</span>): <span class="hljs-title">Set</span><<span class="hljs-title">T</span>> | <span class="hljs-title">T</span>[]</span>;
<span class="hljs-comment">// 4.3</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeUnique</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">String</span> | <span class="hljs-title">Number</span>, <span class="hljs-title">C</span> <span class="hljs-title">extends</span> <span class="hljs-title">Set</span><<span class="hljs-title">T</span>> | <span class="hljs-title">T</span>[]>(<span class="hljs-params">collection: C</span>): <span class="hljs-title">C</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeUnique</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">String</span> | <span class="hljs-title">Number</span>, <span class="hljs-title">C</span> <span class="hljs-title">extends</span> <span class="hljs-title">Set</span><<span class="hljs-title">T</span>> | <span class="hljs-title">T</span>[]>(<span class="hljs-params">
  collection: C,
</span>): <span class="hljs-title">C</span> </span>&#123;
  <span class="hljs-keyword">if</span> (collection <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Set</span>) &#123;
    <span class="hljs-keyword">return</span> collection;
  &#125;

  collection.sort(<span class="hljs-function">(<span class="hljs-params">a,b</span>) =></span> <span class="hljs-built_in">Number</span>(a) < <span class="hljs-built_in">Number</span>(b) ? -<span class="hljs-number">1</span> : <span class="hljs-number">1</span>)
  <span class="hljs-comment">//         ~~~~~~</span>
  <span class="hljs-comment">// Property 'sort' does not exist on type 'C'</span>
  

  <span class="hljs-comment">// 数组的去重操作，可忽略其实现</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < collection.length; index++) &#123;
    <span class="hljs-keyword">const</span> element = collection[index];
    <span class="hljs-comment">//                         ~~~~~~</span>
    <span class="hljs-comment">// Element implicitly has an 'any' type because expression of type 'number' can't be used to index type 'Set<T> | T[]'.</span>
    
    <span class="hljs-keyword">for</span> (
      <span class="hljs-keyword">let</span> startIndex = index + <span class="hljs-number">1</span>;
      index < collection.length - startIndex;
      startIndex++
    ) &#123;
      <span class="hljs-keyword">const</span> nextElement = collection[startIndex];
      <span class="hljs-keyword">if</span> (element === nextElement) &#123;
        collection.splice(index + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125;


  <span class="hljs-keyword">return</span> collection;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">检查promise 的 truthy</h2>
<p>文档说如果直接调用Promise 判断真假，会报错
但是我在playground 尝试并没有发现</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">boolean</span>> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">string</span>> </span>&#123;
  <span class="hljs-keyword">if</span> (foo()) &#123;
    <span class="hljs-comment">//  ~~~~~</span>
    <span class="hljs-comment">// Error!</span>
    <span class="hljs-comment">// This condition will always return true since</span>
    <span class="hljs-comment">// this 'Promise<boolean>' appears to always be defined.</span>
    <span class="hljs-comment">// Did you forget to use 'await'?</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">"true"</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"false"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">static允许修改类本身索引签名</h2>
<p>索引签名允许我们对值设置比显式声明的类型更多的属性, 但是之前我们只能在类的实例端声明，代码如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
  age = <span class="hljs-number">29</span>;

  [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-keyword">let</span> instance = <span class="hljs-keyword">new</span> Foo();
instance[<span class="hljs-string">'otherthing'</span>] = <span class="hljs-string">'我是name'</span>

<span class="hljs-comment">// 如果尝试直接修改类本身，则会报错</span>
Foo[<span class="hljs-string">"something"</span>] = <span class="hljs-string">'我是长度'</span>
<span class="hljs-comment">// ~~~~~</span>
<span class="hljs-comment">// Element implicitly has an 'any' type because expression of type '"something"' can't be used to index type 'typeof Foo'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.3 使得我们该索引签名添加 static 关键字，从而允许直接修改类本身的属性, 但是这样不能修改实例的</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
  age = <span class="hljs-number">29</span>;

  <span class="hljs-keyword">static</span> [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-keyword">let</span> instance = <span class="hljs-keyword">new</span> Foo();
instance[<span class="hljs-string">'otherthing'</span>] = <span class="hljs-string">'我是name'</span>
<span class="hljs-comment">//        ~~~~~~~~~~</span>
<span class="hljs-comment">// Element implicitly has an 'any' type because expression of type '"otherthing"' can't be used to index type 'Foo'.</span>

Foo[<span class="hljs-string">"something"</span>] = <span class="hljs-string">'我是长度'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类的静态方面的索引签名和实例方面的索引签名应用的规则相同，也就是说，其他所有的静态属性都必须和索引签名类型相同</p>
<pre><code class="hljs language-ts copyable" lang="ts">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
  <span class="hljs-keyword">static</span> age = <span class="hljs-number">29</span>;
  <span class="hljs-comment">//     ~~~</span>
  <span class="hljs-comment">// Property 'age' of type 'number' is not assignable to string index type 'string | undefined'</span>

  <span class="hljs-keyword">static</span> [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>
&#125;

Foo[<span class="hljs-string">"something"</span>] = <span class="hljs-string">'我是长度'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">枚举类型不能与永远不相等的数字进行比较</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> AA &#123;
  A = <span class="hljs-number">0</span>,
  B = <span class="hljs-number">1</span>
&#125;

<span class="hljs-keyword">const</span> demo = <span class="hljs-function">(<span class="hljs-params">val: AA</span>) =></span> &#123;
  <span class="hljs-keyword">if</span>(val === <span class="hljs-number">3</span>)&#123;
    <span class="hljs-comment">// ~~~~~~~ 4.3版本这里会类型报错</span>
    <span class="hljs-comment">// This condition will always return 'false' since the types 'AA' and '3' have no overlap.</span>

    <span class="hljs-comment">// do something</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对此的变通方案</strong></p>
<ol>
<li>重写枚举，将枚举重新声明为不平凡(non-trivial )的值</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> AA &#123;
  A = +<span class="hljs-number">0</span>,
  B = <span class="hljs-number">1</span>
&#125;

<span class="hljs-keyword">const</span> demo = <span class="hljs-function">(<span class="hljs-params">val: AA</span>) =></span> &#123;
  <span class="hljs-keyword">if</span>(val === <span class="hljs-number">3</span>)&#123;
    <span class="hljs-comment">// do something</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用 as, 对值进行类型断言</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> AA &#123;
  A = <span class="hljs-number">0</span>,
  B = <span class="hljs-number">1</span>
&#125;

<span class="hljs-keyword">const</span> demo = <span class="hljs-function">(<span class="hljs-params">val: AA</span>) =></span> &#123;
  <span class="hljs-keyword">if</span>((val <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>) === <span class="hljs-number">3</span>)&#123;
    <span class="hljs-comment">// do something</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用联合类型 并 添加注释</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">enum</span> AA &#123;
  A = <span class="hljs-number">0</span>,
  B = <span class="hljs-number">1</span>
&#125;

<span class="hljs-comment">// Include 3 in the type, if we're really certain that 3 can come through.</span>
<span class="hljs-keyword">const</span> demo = <span class="hljs-function">(<span class="hljs-params">val: AA  | <span class="hljs-number">3</span></span>) =></span> &#123;
  <span class="hljs-keyword">if</span>((val <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>) === <span class="hljs-number">3</span>)&#123;
    <span class="hljs-comment">// do something</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">其他</h1>
<ol>
<li>搭配新版内部版本vscode, import 类型提示更智能 <a href="https://code.visualstudio.com/insiders/" target="_blank" rel="nofollow noopener noreferrer">vscode地址</a></li>
<li>支持@link tag <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a559b75c4f2a46f8bd931641f9f76106~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></li>
</ol></div>  
</div>
            