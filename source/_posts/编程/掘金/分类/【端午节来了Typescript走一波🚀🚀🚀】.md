
---
title: '【端午节来了Typescript走一波🚀🚀🚀】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41b9033a95ed4705b61f3177c3726986~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:19:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41b9033a95ed4705b61f3177c3726986~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>近几年来前端的发展趋势一度离不开ts静态类型，包括我自己在用了之后就在也没回头过，在开发的体验中确实能在静态编译的时候帮我们避免很多问题，可能对于纯前端开发人员来说学习ts有一定的成本，但是我认为如果最后得到的收益是大于我们付出的成本的那么未尝不可一试，好了话不多说进入正题</p>
<h2 data-id="heading-1">介绍</h2>
<p>我们可以在<code>typescript</code>官网提供的ts编写乐园进行案例编写，以下我们讲的案例都可以在上面自己试一试（毕竟好记性不如烂笔头，多试试总没坏处）
代码编写入口：<a href="https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgA5QPaoM7IN4BQyxyIcAthAFzZhSgDmBAvgQTAK4gJjAYjIGEMADkKEABQATOGDhV0WbAEpCLIA" target="_blank" rel="nofollow noopener noreferrer">www.typescriptlang.org/play?#code/…</a></p>
<h2 data-id="heading-2">基础类型</h2>
<p>首先介绍<code>typescript</code>提供的基础类型，其实基础类型和我们在<code>js</code>中日常使用的<code>typeof</code> 返回的类型很相似</p>
<p><code>number</code> <br>
<code>boolean</code><br>
<code>string</code><br>
<code>undefined</code> <br>
<code>null</code><br>
<code>any</code><br>
<code>never</code><br>
<code>void</code></p>
<p>大概是以上几种类型我们可以看到有几种在<code>js</code>中也很常见，没见到的也不要急接下来我们依次介绍他们的作用以及使用场景</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//我们创建了一个n并且给的是number的类型，那也就是说n只能赋值number的类型</span>
<span class="hljs-comment">//这样在定义之后就防止之后因为类型错因为如果赋值其他类型ts会自动产生警告提示</span>
<span class="hljs-keyword">let</span> n:<span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>
n = <span class="hljs-string">'12'</span> <span class="hljs-comment">//Error</span>
n = <span class="hljs-number">2</span> <span class="hljs-comment">//Ok</span>

<span class="hljs-keyword">let</span> flag:<span class="hljs-built_in">boolean</span> = <span class="hljs-literal">true</span>
flag = <span class="hljs-literal">false</span> <span class="hljs-comment">//Ok</span>
flag = <span class="hljs-number">1</span> <span class="hljs-comment">//Error</span>

<span class="hljs-keyword">let</span> s:<span class="hljs-built_in">string</span> = <span class="hljs-string">'零湖冲'</span>
s = <span class="hljs-string">'疯清扬'</span> <span class="hljs-comment">// Ok</span>
s = <span class="hljs-number">1</span> <span class="hljs-comment">//Error</span>

<span class="hljs-keyword">let</span> out:<span class="hljs-literal">undefined</span>; <span class="hljs-comment">//类型为undefined</span>

<span class="hljs-keyword">let</span> nu:<span class="hljs-literal">null</span> = <span class="hljs-literal">null</span> <span class="hljs-comment">//类型为null</span>

<span class="hljs-keyword">let</span> an:<span class="hljs-built_in">any</span> = <span class="hljs-literal">null</span> <span class="hljs-comment">//any表示可以设置任意类型，在工作中尽量还是避免使用</span>

<span class="hljs-comment">//never类型表示的是那些永不存在的值的类型</span>
<span class="hljs-comment">//例如，never类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型</span>
<span class="hljs-comment">//当它们被永不为真的类型保护所约束时</span>
<span class="hljs-keyword">let</span> nev:<span class="hljs-built_in">never</span> 

<span class="hljs-comment">//某种程度上来说，void类型像是与any类型相反，它表示没有任何类型</span>
<span class="hljs-comment">//当一个函数没有返回值时，你通常会见到其返回值类型是void</span>
<span class="hljs-keyword">let</span> vo:<span class="hljs-built_in">void</span> = <span class="hljs-literal">undefined</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以看到如果赋值字符串会提示需要number类型这样在之后的流程中能避免我们因为类型赋值错误导致有些方法不能使用</p>
</blockquote>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41b9033a95ed4705b61f3177c3726986~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-3">Typescript定义类型的方式</h2>
<p><code>interface</code><br>
<code>type</code></p>
<h3 data-id="heading-4">Interface</h3>
<p>先介绍一下<code>interface</code>，之后在说说<code>type</code>和两者之间的区别，以下是官网对<code>interface</code>的定义，可能读起来有些晦涩不过不要紧我们看几个例子就明白了</p>
<blockquote>
<p>TypeScript的核心原则之一是对值所具有的结构进行类型检查。 它有时被称做“鸭式辨型法”或“结构性子类型化”。 在TypeScript里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//基础操作</span>
<span class="hljs-comment">//1.声明Props接口</span>
<span class="hljs-keyword">interface</span> Props &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>
&#125;
<span class="hljs-comment">//2.创建getName函数形参使用Props类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">data:Props</span>)</span>&#123;
    <span class="hljs-keyword">let</span> name = data.name
&#125;
<span class="hljs-comment">//3.调用getName按照接口声明的类型传参</span>
getName(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'零湖冲'</span>&#125;)

<span class="hljs-comment">//继承类型并且可以新增类型参数</span>
<span class="hljs-keyword">interface</span> userInfo <span class="hljs-keyword">extends</span> Props&#123;
    <span class="hljs-attr">age</span>:<span class="hljs-built_in">number</span> <span class="hljs-comment">// 新增age类型</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUser</span>(<span class="hljs-params">data:userInfo</span>)</span>&#123;
    <span class="hljs-keyword">let</span> name = data.name
    <span class="hljs-keyword">let</span> age = data.age
&#125;

getUser(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'任盈盈'</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">100</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>以上是整个接口使用的过程<br>
具体说一下细节在函数内部使用<code>data.name</code>的时候如果在编辑器中当你输入完<code>data</code>会自动提示你当前可以使用的参数<br>
在调用<code>getName</code>传参数的时候如果你不传参数或者是传的类型不符合当前定义的类型都会有警告提示</p>
</blockquote>
<blockquote>
<p>ts中有一些可选的操作符号比如<code>!非空断言操作符</code>、<code>?可选参数操作符</code>、<code>?.运算符</code>、<code>??空值合并运算符</code>我们依次介绍</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//!非空断言操作符</span>
<span class="hljs-comment">//可以用于断言操作对象是非 null 和非 undefined 类型</span>
<span class="hljs-comment">//这个例子中因为声明的类型有undefined的可能</span>
<span class="hljs-comment">//所以正常调用cb方法会有警告但是加上!之后就代表告诉类型忽略undefined和null</span>

<span class="hljs-keyword">type</span> fun = <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>; <span class="hljs-comment">// type下面会介绍</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">cb: fun | <span class="hljs-literal">undefined</span></span>) </span>&#123;
    <span class="hljs-keyword">const</span> num1 = cb(); <span class="hljs-comment">// Error</span>
    <span class="hljs-keyword">const</span> num2 = cb!(); <span class="hljs-comment">//Ok</span>
&#125;

<span class="hljs-comment">//?可选参数操作符</span>
<span class="hljs-comment">//非常好理解正常我们定义一个name的接口参数如果不传会提示error</span>
<span class="hljs-comment">//但是加上?之后也就是说这个name是可以传或不传都不会有提示</span>

<span class="hljs-keyword">interface</span> Props &#123;
    name?: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">data: Props</span>) </span>&#123;
    <span class="hljs-keyword">let</span> name = data.name
&#125;
getName(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'疯清扬'</span>&#125;) <span class="hljs-comment">// Ok</span>
getName(&#123;&#125;) <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//?.运算符(在ECMAScript中已经实现此运算符)</span>
<span class="hljs-comment">//在编写过程中如果遇到null或者undefined的情况会自动停止返回false</span>
<span class="hljs-comment">//举个🌰假如data是我们从接口获取到的参数里面有value并且value里面有name</span>
<span class="hljs-comment">/**
&#123;
   value:&#123;
       name:'零湖冲'
   &#125;
&#125;
**/</span>
<span class="hljs-keyword">let</span> res = data

<span class="hljs-comment">//在我们想使用name的时候可能以前会这样写，写一堆繁琐的校验</span>
<span class="hljs-keyword">let</span> name = res && res.value && res.value.name <span class="hljs-comment">// Error</span>

<span class="hljs-comment">//现在可以这样子写，如果其中有那一步没有正常返回不会因为获取不到而导致异常问题</span>
<span class="hljs-keyword">let</span> name = res?.value?.name <span class="hljs-comment">// Ok</span>

<span class="hljs-comment">//??空值合并运算符</span>
<span class="hljs-comment">//当左侧操作数为 null 或 undefined 时，其返回右侧的操作数，否则返回左侧的操作数。</span>
<span class="hljs-comment">//这个我觉得主要可以解决js中0的逻辑或判断问题举个🌰</span>
<span class="hljs-comment">//可以看到除了0其他都和逻辑或很相似</span>

<span class="hljs-keyword">let</span> aa = <span class="hljs-number">0</span> ?? <span class="hljs-string">'林平之'</span> <span class="hljs-comment">// 返回0</span>
<span class="hljs-keyword">let</span> aa = <span class="hljs-number">0</span> || <span class="hljs-string">'岳灵珊'</span> <span class="hljs-comment">// 返回岳灵珊</span>

<span class="hljs-keyword">let</span> aa = <span class="hljs-literal">null</span> ?? <span class="hljs-string">'岳不群'</span> <span class="hljs-comment">// 返回岳不群</span>
<span class="hljs-keyword">let</span> aa = <span class="hljs-literal">undefined</span> ?? <span class="hljs-string">'宁中则'</span> <span class="hljs-comment">// 返回宁中则</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Type</h3>
<p>介绍一下对<code>type</code>的定义，给类型起一个新名字、可以作用于原始值（基本类型）、联合类型、元组、交叉类型、类型映射以及其它任何你需要手写的类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//给类型换一个新的名字&作用🌧于原始值</span>
<span class="hljs-keyword">type</span> num = <span class="hljs-built_in">number</span>
<span class="hljs-keyword">type</span> n1 = num
<span class="hljs-keyword">let</span> n:n1 = <span class="hljs-number">11</span> <span class="hljs-comment">//Ok</span>
<span class="hljs-keyword">let</span> n:n1 = <span class="hljs-string">'12'</span> <span class="hljs-comment">//Error</span>

<span class="hljs-keyword">type</span> str = <span class="hljs-built_in">string</span>

<span class="hljs-comment">//声明一个联合类型</span>

<span class="hljs-keyword">type</span> ns = str | num

<span class="hljs-keyword">let</span> ns1:ns = <span class="hljs-string">'任盈盈'</span> <span class="hljs-comment">// Ok</span>
<span class="hljs-keyword">let</span> ns2:ns = <span class="hljs-number">1</span> <span class="hljs-comment">// Ok </span>

<span class="hljs-comment">//元组类型，限定数组的个数以及数组类型</span>

<span class="hljs-keyword">type</span> res = [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">number</span>]

<span class="hljs-keyword">let</span> data:res = [<span class="hljs-string">'12'</span>,<span class="hljs-number">12</span>] <span class="hljs-comment">//Ok</span>
<span class="hljs-keyword">let</span> data:res = [<span class="hljs-string">'12'</span>,<span class="hljs-literal">false</span>] <span class="hljs-comment">//number</span>

<span class="hljs-comment">//交叉类型，类似interface的继承</span>

<span class="hljs-keyword">interface</span> user &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">type</span> userInfo = user & &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">let</span> user: userInfo = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'东方不败'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">1</span> &#125; <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//类型映射，这个很简单就是把A上面的类型都映射到B类型上举个🌰</span>

<span class="hljs-keyword">type</span> keysList = <span class="hljs-string">"name"</span> | <span class="hljs-string">"sex"</span>

<span class="hljs-keyword">type</span> copeKey = &#123;
    [key <span class="hljs-keyword">in</span> keysList]: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">let</span> res: copeKey = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"东方不败"</span>,<span class="hljs-attr">sex</span>: <span class="hljs-string">"女"</span>&#125; <span class="hljs-comment">//Ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>具体总结一下<code>interface</code>和<code>type</code>的区别，具体区别不止这些大家可以自己试一哈<br>
1.都可以用来描述对象或函数和其他基础类型<br>
2.<code>interface</code>可以实现继承，<code>type</code>不行，但是<code>type</code>可以使用交叉类型<br>
3.<code>type</code>可以使用<code>in</code>进行类型映射，<code>interface</code>不可以实现<br>
4.<code>interface</code>可以定义多次接口会合并，但是<code>type</code>不可以</p>
</blockquote>
<h2 data-id="heading-6">泛型</h2>
<blockquote>
<p>在像<code>C#</code>和<code>Java</code>这样的语言中，可以使用泛型来创建可重用的组件，一个组件可以支持多种类型的数据。 这样用户就可以以自己的数据类型来使用组件。      <code>---- 来自官网的介绍</code></p>
</blockquote>
<h3 data-id="heading-7">我们来看几个例子就明白了其实说白了就是为了描述类型的一种方式</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//泛型是使用<>这种符号声明里面传的是当前需要的类型举个🌰</span>

<span class="hljs-comment">//调用的时候我们传了类型，这也就说明泛型里用的类型我们可以在外面动态传入</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>>(<span class="hljs-params">arg: T</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;

identity<<span class="hljs-built_in">string</span>>(<span class="hljs-string">'任我行'</span>) <span class="hljs-comment">// Ok</span>
identity<<span class="hljs-built_in">number</span>>(<span class="hljs-number">12</span>) <span class="hljs-comment">// Ok</span>

<span class="hljs-comment">//我们可以传入多个类型（是不是很简单）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">identity</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>, <span class="hljs-title">S</span>>(<span class="hljs-params">arg: T, name: U, f: S</span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">return</span> arg;
&#125;

identity<<span class="hljs-built_in">number</span>, <span class="hljs-built_in">string</span>, <span class="hljs-built_in">boolean</span>>(<span class="hljs-number">123</span>, <span class="hljs-string">'张无忌'</span>, <span class="hljs-literal">false</span>) <span class="hljs-comment">//Ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">我们看看怎么定义复杂类型对象</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> arrList = <span class="hljs-built_in">Array</span><<span class="hljs-built_in">any</span>>
<span class="hljs-keyword">let</span> arr:arrList = [] <span class="hljs-comment">// Ok</span>

<span class="hljs-comment">//如果需要定义数组内部的内容Array<>是泛型的方式</span>
<span class="hljs-keyword">type</span> arrList = <span class="hljs-built_in">Array</span><<span class="hljs-built_in">string</span>>
<span class="hljs-keyword">let</span> arr:arrList = [<span class="hljs-string">'左冷禅'</span>] <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//还可以这样子定义数组内容</span>
<span class="hljs-keyword">type</span> arrList = <span class="hljs-built_in">string</span>[]
<span class="hljs-keyword">let</span> arr:arrList = [<span class="hljs-string">'左冷禅'</span>] <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//数组的内部类型如果是复杂的类型可以这样</span>
<span class="hljs-keyword">type</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> &#125;
<span class="hljs-keyword">type</span> arrList = obj[]
<span class="hljs-keyword">let</span> arr: arrList = [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'1'</span> &#125;] <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//或者这样使用泛型的方式</span>
<span class="hljs-keyword">type</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> &#125;
<span class="hljs-keyword">type</span> arrList = <span class="hljs-built_in">Array</span><obj>
<span class="hljs-keyword">let</span> arr: arrList = [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'1'</span> &#125;] <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//规定变量可以接收的值</span>
<span class="hljs-keyword">type</span> curr = <span class="hljs-string">'age'</span> | <span class="hljs-string">'name'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCurr</span>(<span class="hljs-params">val:curr</span>)</span>&#123;
    <span class="hljs-keyword">return</span> val
&#125;
getCurr(<span class="hljs-string">'age'</span>) <span class="hljs-comment">//Ok</span>
getCurr(<span class="hljs-string">'name'</span>) <span class="hljs-comment">//Ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Typescript中的高级类型工具</h2>
<p><code>ts</code>中有几个高级类型支持类型直接的扩展以及转化等操作我们依次介绍<br></p>
<p><code>keyof</code> <br>
<code>extends</code><br>
<code>Partial</code><br>
<code>Required</code><br>
<code>Pick</code><br>
<code>Record</code></p>
<h3 data-id="heading-10">keyof&extends</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//keyof是索引类型查询的语法类似Object.keys()，取的值为键举个🌰</span>
<span class="hljs-keyword">interface</span> users &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">type</span> formtUser = keyof users
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUser</span>(<span class="hljs-params">val: formtUser</span>) </span>&#123;
    <span class="hljs-keyword">return</span> val
&#125;
getUser(<span class="hljs-string">'name'</span>) <span class="hljs-comment">// Ok</span>
getUser(<span class="hljs-string">'age'</span>) <span class="hljs-comment">//Ok</span>

<span class="hljs-comment">//来看看具体实际用途我们使用ts实现一个根据key获取对象内容的函数</span>
<span class="hljs-comment">//这样写法有两个问题</span>
<span class="hljs-comment">//1.无法确认返回类型</span>
<span class="hljs-comment">//2.无法对K做约束</span>
<span class="hljs-keyword">const</span> data = &#123;
  <span class="hljs-attr">age</span>: <span class="hljs-number">101</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'令狐冲'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params">o: <span class="hljs-built_in">object</span>, name: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> o[name]
&#125;
getData(data,<span class="hljs-string">'name'</span>)

<span class="hljs-comment">//我们可以使用泛型的方法来规定输入的内容和返回的内容</span>
<span class="hljs-comment">//extends代表条件类型，可以理解为T继承的类型来自Object</span>
<span class="hljs-comment">//另一个K继承来自T的键（上面说过keyof 可以获取键）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">Object</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">o: T, name: K</span>):<span class="hljs-title">T</span>[<span class="hljs-title">K</span>] </span>&#123;
  <span class="hljs-keyword">return</span> o[name]
&#125;
getData(data1,<span class="hljs-string">'name'</span>)

<span class="hljs-comment">//单独介绍一下extends条件类型，类似于js中的三元运算符，举🌰</span>
T <span class="hljs-keyword">extends</span> U ? X : Y
<span class="hljs-keyword">type</span> flag<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span> ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>
<span class="hljs-keyword">type</span> f1 = flag<<span class="hljs-built_in">number</span>> <span class="hljs-comment">// false</span>
<span class="hljs-keyword">type</span> f2 = flag<<span class="hljs-literal">false</span>> <span class="hljs-comment">// false</span>
<span class="hljs-keyword">type</span> f3 = flag<<span class="hljs-literal">true</span>> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Partial&Required</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//Partial将现有的类型全部转化为可选类型</span>
<span class="hljs-comment">//日常中我们可以复用其他已经定义好的类型没必要重新声明一次，举🌰</span>

<span class="hljs-keyword">interface</span> school &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-keyword">type</span> formtSchool = Partial<school> <span class="hljs-comment">//在这里全部转化为可选类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSchool</span>(<span class="hljs-params">val: formtSchool</span>) </span>&#123;
&#125;
getSchool(&#123; <span class="hljs-attr">name</span>: <span class="hljs-number">1</span> &#125;) <span class="hljs-comment">//Ok</span>


<span class="hljs-comment">//Required和Partial类型相反，它是将所有可选类型变为必选</span>

<span class="hljs-keyword">type</span> recordSchool = Required<formtSchool>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSchool</span>(<span class="hljs-params">val: recordSchool</span>) </span>&#123;
&#125;
getSchool(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'风青杨'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">1</span> &#125;) <span class="hljs-comment">//Ok</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">Pick&Record</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//Pick可以继承部分想要的类型，举🌰</span>
<span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">sex</span>: <span class="hljs-built_in">string</span>
&#125;;
<span class="hljs-keyword">type</span> PickUser = Pick<User, <span class="hljs-string">'age'</span> | <span class="hljs-string">'sex'</span>>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUser</span>(<span class="hljs-params">val: PickUser</span>) </span>&#123;
&#125;
getUser(&#123; <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'女'</span> &#125;) <span class="hljs-comment">//Ok 我们只继承了age和sex</span>

<span class="hljs-comment">//Record是类型映射，简单的说就是把一个类型映射到另一个类型的key上，这样讲可能有些难懂我们来看个🌰</span>
<span class="hljs-keyword">type</span> types = <span class="hljs-string">'a'</span> | <span class="hljs-string">'b'</span>
<span class="hljs-keyword">type</span> data = &#123; <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span> &#125;
<span class="hljs-keyword">type</span> result = Record<types, data> 
<span class="hljs-comment">/*
result结果是这样
type result = &#123;
    a: data;
    b: data;
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">定义一个值的类型却不知道应该是什么类型应该咋整？</h2>
<blockquote>
<p>直接问问<code>ts</code>就好了，举个🌰</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//当我们想定义一个时间类型，但是却不知道应该为什么类型，那么创建一个值为时间的变量ts会告诉你</span>
<span class="hljs-keyword">type</span> times = <span class="hljs-built_in">Date</span>
<span class="hljs-keyword">let</span> time:times = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() <span class="hljs-comment">//Ok</span>
<span class="hljs-keyword">let</span> time:times = <span class="hljs-number">123</span> <span class="hljs-comment">//Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c90d10ad565342b4bb83c326a897875d~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-14">结束</h2>
<blockquote>
<p>本篇幅到这里就结束了，讲了很多但是还差很多最重要的还是工作中去实践才能感受到<code>ts</code>带来的好处</p>
</blockquote>
<h3 data-id="heading-15">最后端午节幸福安康😄</h3>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71f34393e06a4d18b273ad91cd086ed5~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            