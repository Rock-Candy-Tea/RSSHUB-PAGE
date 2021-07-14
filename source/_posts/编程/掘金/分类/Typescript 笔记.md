
---
title: 'Typescript 笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4191'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:20:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4191'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>刚开始学<code>typescript</code>,有点懵,留个笔记记录下常用的类型方法,方便后续查找</p>
<h2 data-id="heading-0">接口</h2>
<p>首字母要大写,加?表示参数可选</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 声明array</span>
<span class="hljs-keyword">interface</span> Arr &#123;
    [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-built_in">Array</span><&#123;<span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>,age?: <span class="hljs-built_in">number</span>&#125;>

<span class="hljs-comment">// 声明一个任意类型的Object</span>
<span class="hljs-keyword">interface</span> Obj &#123;
    [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-comment">// 声明制定key值的Object</span>
<span class="hljs-keyword">interface</span> Obj &#123;
    <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继承使用<code>extends</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> A &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">interface</span> B <span class="hljs-keyword">extends</span> A &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-comment">// 此时 B的类型如下</span>
<span class="hljs-keyword">type</span> B = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">类</h2>
<ul>
<li>类在声明时,必须要有<code>constructor</code>进行初始化赋值</li>
<li>类里面的变量可用以下几个修饰符进行修饰,默认使用的是<code>public</code>
<ul>
<li>public 公有</li>
<li>private 私有-只能在声明它的类中使用</li>
<li>protected 允许继承的实例访问</li>
<li>readonly 只读</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span>
  <span class="hljs-keyword">private</span> age: <span class="hljs-built_in">number</span>
  <span class="hljs-keyword">protected</span> sex: <span class="hljs-string">'男'</span> | <span class="hljs-string">'女'</span>

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, age: <span class="hljs-built_in">number</span>, sex: <span class="hljs-string">'男'</span> | <span class="hljs-string">'女'</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.age = age
    <span class="hljs-built_in">this</span>.sex = sex
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-keyword">public</span> height: <span class="hljs-built_in">number</span>
  <span class="hljs-keyword">readonly</span> <span class="hljs-keyword">readonly</span>: <span class="hljs-built_in">string</span>
  
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">height: <span class="hljs-built_in">number</span>,name: <span class="hljs-built_in">string</span>,age: <span class="hljs-built_in">number</span>, sex: <span class="hljs-string">'男'</span> | <span class="hljs-string">'女'</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name, age, sex)
    <span class="hljs-built_in">this</span>.height = height
    <span class="hljs-built_in">this</span>.readonly = <span class="hljs-string">'我是只读的'</span>
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">changeSex</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.sex = <span class="hljs-string">'男'</span> <span class="hljs-comment">// 可以修改</span>
  &#125;
  <span class="hljs-comment">// 此处会报错</span>
  <span class="hljs-function"><span class="hljs-title">changeReadonly</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.readonly = <span class="hljs-string">'尝试修改'</span> <span class="hljs-comment">// 无法分配到 "readonly" ，因为它是只读属性</span>
  &#125;
&#125;

<span class="hljs-keyword">const</span> ZhangSan = <span class="hljs-keyword">new</span> B(<span class="hljs-number">160</span>, <span class="hljs-string">'张三'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'男'</span>)
<span class="hljs-comment">// 此处会报错</span>
ZhangSan.age <span class="hljs-comment">// 属性“age”为私有属性，只能在类“A”中访问</span>
<span class="hljs-comment">// 此处会报错</span>
ZhangSan.sex = <span class="hljs-string">'女'</span> <span class="hljs-comment">// 属性“sex”受保护，只能在类“A”及其子类中访问</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">函数</h2>
<p>函数的剩余参数，可以通过<code>...</code>来获取</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">firstName: <span class="hljs-built_in">string</span>, ...restOfName: <span class="hljs-built_in">string</span>[]</span>) </span>&#123;
  <span class="hljs-keyword">return</span> firstName + <span class="hljs-string">" "</span> + restOfName.join(<span class="hljs-string">" "</span>);
&#125;

<span class="hljs-keyword">let</span> employeeName = buildName(<span class="hljs-string">"Joseph"</span>, <span class="hljs-string">"Samuel"</span>, <span class="hljs-string">"Lucas"</span>, <span class="hljs-string">"MacKinzie"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">泛型</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;

<span class="hljs-comment">// 1 指定类型</span>
<span class="hljs-keyword">let</span> output = identity<<span class="hljs-built_in">string</span>>(<span class="hljs-string">"myString"</span>);  <span class="hljs-comment">// type of output will be 'string'</span>
<span class="hljs-comment">// 2 无需指定，自动判断</span>
<span class="hljs-keyword">let</span> output = identity(<span class="hljs-string">"myString"</span>);

<span class="hljs-comment">// 如果是数组时，按如下方式指定T[] 或者 Array<T></span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T[]</span>): <span class="hljs-title">T</span>[] </span>&#123;
    <span class="hljs-built_in">console</span>.log(arg.length);  <span class="hljs-comment">// Array has a .length, so no more error</span>
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义泛型T表明，<>为声明，我们定义了泛型函数后，可以用两种方法使用。</p>
<p>在类和接口中使用</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> GenericIdentityFn<T> &#123;
    (arg: T): T;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GenericNumber</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-attr">zeroValue</span>: T;
    add: <span class="hljs-function">(<span class="hljs-params">x: T, y: T</span>) =></span> T;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">枚举</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//数字枚举，若不设置=1，则会从0开始+1自增</span>
<span class="hljs-built_in">enum</span> Direction &#123;
    Up=<span class="hljs-number">1</span>,
    Down,
    Left,
    Right,
&#125;
<span class="hljs-comment">// 普通枚举</span>
<span class="hljs-built_in">enum</span> Response &#123;
    No = <span class="hljs-number">0</span>,
    Yes = <span class="hljs-number">1</span>,
&#125;

<span class="hljs-comment">// 使用的好处, 可以尽量消除魔法字符串</span>
Direction.Down
Response.No
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">辅助函数</h2>
<h3 data-id="heading-6">Partial</h3>
<p>将所有值变成可选</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Todo &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    description: <span class="hljs-built_in">string</span>;
&#125;

Partial<Todo>
&#123;
    title?: <span class="hljs-built_in">string</span>;
    description?: <span class="hljs-built_in">string</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Readonly</h3>
<p>将所有值变成只读</p>
<h3 data-id="heading-8">Record<K,T></h3>
<p>生成一个key为K的对象类型，将T类型赋予里面的key</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> PageInfo &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">type</span> Page = <span class="hljs-string">'home'</span> | <span class="hljs-string">'about'</span> | <span class="hljs-string">'contact'</span>;

Record<Page, PageInfo>
&#123;
    <span class="hljs-attr">home</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span> &#125;,
    <span class="hljs-attr">about</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span> &#125;,
    <span class="hljs-attr">contact</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span> &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Pick<T,K></h3>
<p>自定义选择属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Todo &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    description: <span class="hljs-built_in">string</span>;
    completed: <span class="hljs-built_in">boolean</span>;
&#125;

Pick<Todo, <span class="hljs-string">'title'</span> | <span class="hljs-string">'completed'</span>>;
&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    completed: <span class="hljs-built_in">boolean</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Omit<T,K></h3>
<p>自定义删除几个属性</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Todo &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    description: <span class="hljs-built_in">string</span>;
    completed: <span class="hljs-built_in">boolean</span>;
&#125;

Omit<Todo, <span class="hljs-string">'description'</span>>;
&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    completed: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Exclude<T,U></h3>
<p>通过排除来生成</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T0 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span>>;  <span class="hljs-comment">// "b" | "c"</span>
<span class="hljs-keyword">type</span> T1 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span>>;  <span class="hljs-comment">// "c"</span>
<span class="hljs-keyword">type</span> T2 = Exclude<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>;  <span class="hljs-comment">// string | number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">NonNullable</h3>
<p>排除类型中的null和undefined</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T0 = NonNullable<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>>;  <span class="hljs-comment">// string | number</span>
<span class="hljs-keyword">type</span> T1 = NonNullable<<span class="hljs-built_in">string</span>[] | <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span>>;  <span class="hljs-comment">// string[]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">Parameters</h3>
<p>构造函数返回类型为参数类型的数组</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params">arg: &#123; a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">string</span> &#125;</span>): <span class="hljs-title">void</span>
<span class="hljs-title">type</span> <span class="hljs-title">T0</span> = <span class="hljs-title">Parameters</span><(<span class="hljs-params"></span>) => <span class="hljs-title">string</span>></span>;  <span class="hljs-comment">// []</span>
<span class="hljs-keyword">type</span> T1 = Parameters<<span class="hljs-function">(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>>;  <span class="hljs-comment">// [string]</span>
<span class="hljs-keyword">type</span> T2 = Parameters<(<T><span class="hljs-function">(<span class="hljs-params">arg: T</span>) =></span> T)>;  <span class="hljs-comment">// [unknown]</span>
<span class="hljs-keyword">type</span> T4 = Parameters<<span class="hljs-keyword">typeof</span> f1>;  <span class="hljs-comment">// [&#123; a: number, b: string &#125;]</span>
<span class="hljs-keyword">type</span> T5 = Parameters<<span class="hljs-built_in">any</span>>;  <span class="hljs-comment">// unknown[]</span>
<span class="hljs-keyword">type</span> T6 = Parameters<<span class="hljs-built_in">never</span>>;  <span class="hljs-comment">// never</span>
<span class="hljs-keyword">type</span> T7 = Parameters<<span class="hljs-built_in">string</span>>;  <span class="hljs-comment">// Error</span>
<span class="hljs-keyword">type</span> T8 = Parameters<<span class="hljs-built_in">Function</span>>;  <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">ConstructorParameters</h3>
<p>提取所有参数类型，构成返回，是Parameters的进阶</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T0 = ConstructorParameters<ErrorConstructor>;  <span class="hljs-comment">// [(string | undefined)?]</span>
<span class="hljs-keyword">type</span> T1 = ConstructorParameters<FunctionConstructor>;  <span class="hljs-comment">// string[]</span>
<span class="hljs-keyword">type</span> T2 = ConstructorParameters<RegExpConstructor>;  <span class="hljs-comment">// [string, (string | undefined)?]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">ReturnType</h3>
<p>构造一个由函数的返回类型组成的类型T</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>): </span>&#123; a: <span class="hljs-built_in">number</span>, <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span> &#125;
<span class="hljs-keyword">type</span> T0 = ReturnType<<span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>>;  <span class="hljs-comment">// string</span>
<span class="hljs-keyword">type</span> T1 = ReturnType<<span class="hljs-function">(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>>;  <span class="hljs-comment">// void</span>
<span class="hljs-keyword">type</span> T2 = ReturnType<(<T><span class="hljs-function">() =></span> T)>;  <span class="hljs-comment">// &#123;&#125;</span>
<span class="hljs-keyword">type</span> T3 = ReturnType<(<T extends U, U extends number[]>() => T)>;  // number[]
type T4 = ReturnType<typeof f1>;  // &#123; a: number, b: string &#125;
type T5 = ReturnType<any>;  // any
type T6 = ReturnType<never>;  // any
type T7 = ReturnType<string>;  // Error
type T8 = ReturnType<Function>;  // Error
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">InstanceType</h3>
<p>构造一个和实例类型一样的接口</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    x = <span class="hljs-number">0</span>;
    y = <span class="hljs-number">0</span>;
&#125;

<span class="hljs-keyword">type</span> T0 = InstanceType<<span class="hljs-keyword">typeof</span> C>;  <span class="hljs-comment">// C &#123;x:number,y:number&#125;</span>
<span class="hljs-keyword">type</span> T1 = InstanceType<<span class="hljs-built_in">any</span>>;  <span class="hljs-comment">// any</span>
<span class="hljs-keyword">type</span> T2 = InstanceType<<span class="hljs-built_in">never</span>>;  <span class="hljs-comment">// any</span>
<span class="hljs-keyword">type</span> T3 = InstanceType<<span class="hljs-built_in">string</span>>;  <span class="hljs-comment">// Error</span>
<span class="hljs-keyword">type</span> T4 = InstanceType<<span class="hljs-built_in">Function</span>>;  <span class="hljs-comment">// Error</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Required</h3>
<p>将类型里的可选全部去掉，与Partial相反</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Props &#123;
    a?: <span class="hljs-built_in">number</span>;
    b?: <span class="hljs-built_in">string</span>;
&#125;;

<span class="hljs-keyword">const</span> obj: Props = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">5</span> &#125;; <span class="hljs-comment">// OK</span>

<span class="hljs-keyword">const</span> obj2: Required<Props> = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">5</span> &#125;; <span class="hljs-comment">// Error: property 'b' missing</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            