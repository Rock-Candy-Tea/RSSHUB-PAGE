
---
title: '15 个提高开发效率的 TypeScript 小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3221'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 18:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3221'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>TypeScript 相信大家都见的很多了，但总有些时候不知道类型怎么写才能不报错</p>
<p>有时候你满脑子疑惑“哈？这都能报错？我写的明明是对的啊，到底该怎么写？”</p>
<p>来看看下面的小技巧吧，总有一个能提高你的效率</p>
<h2 data-id="heading-0">提取元组或数组类型中每一项的类型</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> ArrayType1 = <span class="hljs-built_in">Array</span><&#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
&#125;>
<span class="hljs-keyword">type</span> ArrayType2 = (&#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
&#125; | &#123;
    <span class="hljs-attr">c</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">d</span>: <span class="hljs-built_in">string</span>
&#125;)[]
<span class="hljs-comment">// 通过索引访问来获取，我们都知道数组的索引是 number 类型的</span>
<span class="hljs-keyword">type</span> GetArrayOrTupleItemType1 = ArrayType1[<span class="hljs-built_in">number</span>]
<span class="hljs-comment">// 得到</span>
<span class="hljs-keyword">type</span> GetArrayOrTupleItemType1 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-comment">// 通过 infer 进行推导</span>
<span class="hljs-keyword">type</span> GetArrayOrTupleItemType2 = ArrayType2 <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span><infer U> ? U : <span class="hljs-built_in">never</span>
<span class="hljs-comment">// 得到</span>
<span class="hljs-keyword">type</span> GetArrayOrTupleItemType2 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
&#125; | &#123;
    <span class="hljs-attr">c</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">d</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>

<h2 data-id="heading-1">获取接口 interface （或对象类型）中的类型</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> A &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">c</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">d</span>: <span class="hljs-built_in">Array</span><&#123;
        <span class="hljs-attr">e</span>: symbol
    &#125;>
&#125;
<span class="hljs-keyword">type</span> B = A[<span class="hljs-string">'b'</span>]
<span class="hljs-keyword">type</span> C = A[<span class="hljs-string">'c'</span>]
<span class="hljs-comment">// 与上一小节的技巧配置使用</span>
<span class="hljs-keyword">type</span> E = A[<span class="hljs-string">'d'</span>][<span class="hljs-built_in">number</span>][<span class="hljs-string">'e'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">const 和 let 类型推导的区别</h2>
<p>这在 ts 中叫做 <a href="https://www.typescriptlang.org/docs/handbook/type-inference.html" target="_blank" rel="nofollow noopener noreferrer">类型推断</a></p>
<p>const 声明的常量的类型为字面量类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span> <span class="hljs-comment">// 则 a 的类型就为 1</span>
<span class="hljs-keyword">const</span> d = <span class="hljs-string">'2'</span> <span class="hljs-comment">// 则 a 的类型就是 '2'</span>
<span class="hljs-comment">// 这是因为常量是不可修改的，所以不会进行类型推断，但下面的情况不是这样</span>
<span class="hljs-comment">// b 的类型为 number，c 的类型为 string，这是由于右侧得到的类型即为 (number | string)[]</span>
<span class="hljs-keyword">const</span> [b, c] = [<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span>]
<span class="hljs-comment">// d.e 的 类型 为 number，d.f 的类型 为 string，因为常量对象的属性是可以进行操作的，类型推导也会发生在初始化成员（对象属性）的过程中</span>
<span class="hljs-keyword">const</span> d = &#123;
    <span class="hljs-attr">e</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">f</span>: <span class="hljs-string">'2'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let 声明的变量时，类型会被推导</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span> <span class="hljs-comment">// a 为 number 类型</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-string">'2'</span> <span class="hljs-comment">// b 为 string 类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">as const 进行断言</h2>
<p>上一小节中 let 声明的 a 和 b 如何得到它们初始值本身对应的字面量类型？</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-number">1</span> = <span class="hljs-number">1</span> <span class="hljs-comment">// 1 本身也可以作为类型使用</span>
<span class="hljs-comment">// 同样的也可以进行断言</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span> <span class="hljs-keyword">as</span> <span class="hljs-number">1</span>
<span class="hljs-comment">// 也可以用 as const 更加统一，明了</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span> <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-string">'2'</span> <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
<span class="hljs-keyword">let</span> c = &#123;
    <span class="hljs-attr">e</span>: <span class="hljs-number">1</span> <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
&#125;
<span class="hljs-keyword">let</span> d = [<span class="hljs-number">1</span> <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用于接收类型为字面量类型的情况，如</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> a = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>
&#125;
<span class="hljs-keyword">const</span> c = <span class="hljs-function">(<span class="hljs-params">params: &#123; b: <span class="hljs-number">1</span> &#125;</span>) =></span> &#123;&#125;

c(a) <span class="hljs-comment">// 报错：不能将类型“number”分配给类型“1”，在 b: 1 那一行最后加上 as const 即可解决</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">as unknown as xxx 代替 as any</h2>
<p>开发中经常会遇到类型定义的不太好，需要用 as 进行断言的情况，简单来看，可以直接用 as any 解决几乎所有的 ts 类型问题（如报错）</p>
<p>但不利于后续的维护，维护者可能并不知道被 as any 的目标应该是什么类型，正确的做法应该是用 as unknown as xxx 代替，这样能看到明确的类型，如</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 真实场景可能更为复杂</span>
;(<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> unknown <span class="hljs-keyword">as</span> &#123; <span class="hljs-attr">handler</span>: (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span> &#125;).handler = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多内容参考我的这篇文章<a href="https://juejin.cn/post/6961985123923263525" target="_blank">TypeScript进阶, 如何避免 any</a></p>
<h2 data-id="heading-5">非空断言符</h2>
<p>有时候定义了某个变量或对象属性会包含 undefined 或 null 类型，但使用时逻辑上一定不存在未定义的情况</p>
<p>那么就可以使用非空断言</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-literal">undefined</span> | &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
&#125; = <span class="hljs-literal">undefined</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>) </span>&#123;
  a = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-string">'1'</span>
  &#125;
&#125;
c()
<span class="hljs-built_in">console</span>.log(a.b) <span class="hljs-comment">// 提示：对象可能为“未定义”</span>
<span class="hljs-comment">// 在可能为 undefined 或 null 的变量或对象属性后增加 ! 非空断言操作符</span>
<span class="hljs-built_in">console</span>.log(a!.b)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">可选链操作符</h2>
<p>大部分情况下，可选链操作符 ?. 会被编译，如果它前面的变量或对象属性为空，则会直接返回 undefined，新版 Chrome 浏览器已经支持这一特性，可以直接使用</p>
<h2 data-id="heading-7">declare 关键字</h2>
<p>declare 用于声明那些当前模块下没有，但实际上可以被访问的变量常量或方法等</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> a: <span class="hljs-built_in">string</span>
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span>
<span class="hljs-title">declare</span> <span class="hljs-title">class</span> <span class="hljs-title">C</span> </span>&#123;&#125;
<span class="hljs-comment">// 这样使用常量 a 和函数 b 都不会报错</span>
<span class="hljs-comment">// 比如有个 jquery 对象是通过 script 形式引入的，那么在项目的 .d.ts 文件中这样写，可以让它在任何地方都能被访问</span>
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> $: JQueryStatic
<span class="hljs-comment">// 当然，declare module 'jquery' 也是可以的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">有限元素的数组（元组）类型声明以及某一项（或多项）可为 undefined 的情况</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> DateArray = [<span class="hljs-built_in">Date</span>, <span class="hljs-built_in">Date</span>]
<span class="hljs-comment">// 可为空</span>
<span class="hljs-keyword">type</span> DateArray1 = [<span class="hljs-built_in">Date</span> | <span class="hljs-literal">undefined</span>, <span class="hljs-built_in">Date</span>]
<span class="hljs-comment">// 或直接在可为空的元素后面加 ?</span>
<span class="hljs-keyword">type</span> DateArray2 = [<span class="hljs-built_in">Date</span>?, <span class="hljs-built_in">Date</span>?]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">函数类型中的参数关系限定</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/* 如果 a 为 1 的时候，b 必须 传 '1'，a 为 2，b 必须传 2 */</span>
<span class="hljs-comment">/*  这样写无法限定两者的关系 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">a: <span class="hljs-number">1</span> | <span class="hljs-number">2</span>, b: <span class="hljs-string">'1'</span> | <span class="hljs-string">'2'</span></span>) </span>&#123;
    <span class="hljs-comment">// xxx</span>
&#125;
<span class="hljs-comment">/* 可以利用重载 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">a: <span class="hljs-number">1</span>, b: <span class="hljs-string">'1'</span></span>): <span class="hljs-title">void</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">a: <span class="hljs-number">2</span>, b: <span class="hljs-string">'2'</span></span>): <span class="hljs-title">void</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">a: <span class="hljs-number">1</span> | <span class="hljs-number">2</span>, b: <span class="hljs-string">'1'</span> | <span class="hljs-string">'2'</span></span>): <span class="hljs-title">void</span> </span>&#123;&#125;
/* 也可以利用泛型 */
<span class="hljs-title">interface</span> <span class="hljs-title">BType</span> </span>&#123;
    1: '1'
    2: '2'
&#125;
/* 只有在泛型中使用 <span class="hljs-title">extends</span> 约束，并且 <span class="hljs-title">a</span> 和 <span class="hljs-title">b</span> 确实有某种关系，才能在 <span class="hljs-title">a</span> 为特定类型的时候，约束 <span class="hljs-title">b</span> 的类型 */
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span><<span class="hljs-title">AType</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">BType</span>>(<span class="hljs-params">a: Atype, b: BType[AType]</span>): <span class="hljs-title">void</span> </span>&#123;&#125;
/* 或 */
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span><<span class="hljs-title">AType</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">BType</span>>(<span class="hljs-params">a: Atype, b: AType <span class="hljs-keyword">extends</span> <span class="hljs-string">'1'</span> ? BType[<span class="hljs-string">'1'</span>] : BType[<span class="hljs-string">'2'</span>]</span>): <span class="hljs-title">void</span> </span>&#123;&#125;
/* 
 * 你也可以用上述两种方式来声明参数与返回值的对应关系，泛型与 <span class="hljs-title">extends</span> 的特性也可以用于类的构造器的声明
 * 注意，如果函数只有一个参数，你也可以这样写
 */
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params">&#123; a, b &#125;: &#123; a: <span class="hljs-number">1</span>; b: <span class="hljs-string">'1'</span> &#125; | &#123; a: <span class="hljs-number">2</span>; b: <span class="hljs-string">'2'</span> &#125;</span>): <span class="hljs-title">void</span> </span>&#123;&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">如何得到异步函数返回值的具体类型？</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><</span>&#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>
    <span class="hljs-attr">c</span>: <span class="hljs-string">'2'</span>
&#125;>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 也就是这个 c 的类型，不调用 a 的情况如何获取呢？</span>
    <span class="hljs-keyword">const</span> c = <span class="hljs-keyword">await</span> a()
&#125;
<span class="hljs-comment">// 先能获得 Promise 泛型中传入的的类型</span>
<span class="hljs-keyword">type</span> GetPromiseType<P <span class="hljs-keyword">extends</span> unknown> = P <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Promise</span><
  infer Params
>
  ? Params
  : P
<span class="hljs-comment">// 这样就能得到了（ReturnType 是自带的工具类型）</span>
<span class="hljs-keyword">type</span> GetAsyncFunctionReturnType = GetPromiseType<ReturnType<<span class="hljs-keyword">typeof</span> a>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">提示找不到具有类型为 "string" 的参数的索引签名</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> a = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-number">2</span>
&#125;
<span class="hljs-keyword">let</span> c: <span class="hljs-built_in">string</span> = <span class="hljs-string">'b'</span>
<span class="hljs-comment">// 元素隐式具有 "any" 类型，因为类型为 "string" 的表达式不能用于索引类型 "&#123; b: number; c: number; &#125;"。</span>
<span class="hljs-comment">// 在类型 "&#123; b: number; c: number; &#125;" 上找不到具有类型为 "string" 的参数的索引签名。</span>
<span class="hljs-keyword">const</span> d = a[c] <span class="hljs-comment">// 这一行报错</span>

<span class="hljs-comment">// 这样定义 a 就好了</span>
<span class="hljs-keyword">const</span> a: &#123; [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span> &#125; = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-number">2</span>
&#125;
<span class="hljs-comment">// 如果你的 a 已声明类型了</span>
<span class="hljs-keyword">interface</span> A &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">c</span>: <span class="hljs-built_in">number</span>
&#125;
<span class="hljs-keyword">const</span> a: A = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-number">2</span>
&#125;
<span class="hljs-comment">// 那加在后面也是可以的</span>
<span class="hljs-keyword">const</span> a: A & &#123; [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">number</span> &#125; = &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-number">2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">各种自带的实用工具类型</h2>
<p>参考我的这篇文章<a href="https://juejin.cn/post/6970083128345903135" target="_blank">TypeScript 的 Utility Types，你真的懂吗？</a></p>
<h2 data-id="heading-13">得到对象类型值类型的联合类型</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> A &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>
    <span class="hljs-attr">c</span>: <span class="hljs-string">'3'</span>
&#125;
<span class="hljs-comment">// 要得到 1 | 2 | '3'</span>
<span class="hljs-comment">// 则</span>
<span class="hljs-keyword">type</span> Values = A[keyof A]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">如何重新导出一个类型声明</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// a.ts 文件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> A &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
    <span class="hljs-attr">b</span>: <span class="hljs-string">'2'</span>
&#125;
<span class="hljs-comment">// index.ts 文件</span>
<span class="hljs-comment">// 方式一，重新执行类型别名</span>
<span class="hljs-keyword">import</span> &#123; A &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.ts'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> AType = A
<span class="hljs-comment">// 方式二</span>
<span class="hljs-keyword">export</span> &#123; A &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.ts'</span>
<span class="hljs-comment">// 注：配置了 --isolatedModules 需要这样写</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> &#123; A &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.ts'</span>
<span class="hljs-comment">// 方式三</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.ts'</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            