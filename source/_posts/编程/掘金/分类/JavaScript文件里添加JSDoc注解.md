
---
title: 'JavaScript文件里添加JSDoc注解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3570'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 01:56:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=3570'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">支持的JSDoc <a id="user-content-supported-jsdoc" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></h2>
<p>下面的列表列出了当前所支持的JSDoc注解，你可以用它们在JavaScript文件里添加类型信息。</p>
<p>注意，没有在下面列出的标记（例如<code>@async</code>）都是还不支持的。</p>
<ul>
<li><code>@type</code></li>
<li><code>@param</code> (or <code>@arg</code> or <code>@argument</code>)</li>
<li><code>@returns</code> (or <code>@return</code>)</li>
<li><code>@typedef</code></li>
<li><code>@callback</code></li>
<li><code>@template</code></li>
<li><code>@class</code> (or <code>@constructor</code>)</li>
<li><code>@this</code></li>
<li><code>@extends</code> (or <code>@augments</code>)</li>
<li><code>@enum</code></li>
</ul>
<p>它们代表的意义与usejsdoc.org上面给出的通常是一致的或者是它的超集。 下面的代码描述了它们的区别并给出了一些示例。</p>
<h3 data-id="heading-1"><code>@type</code></h3>
<p>可以使用<code>@type</code>标记并引用一个类型名称（原始类型，TypeScript里声明的类型，或在JSDoc里<code>@typedef</code>标记指定的） 可以使用任何TypeScript类型和大多数JSDoc类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;string&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> s;

<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Window&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> win;

<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;PromiseLike<string>&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> promisedString;

<span class="hljs-comment">// You can specify an HTML Element with DOM properties</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;HTMLElement&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> myElement = <span class="hljs-built_in">document</span>.querySelector(selector);
element.dataset.myData = <span class="hljs-string">''</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@type</code>可以指定联合类型—例如，<code>string</code>和<code>boolean</code>类型的联合。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;(string | boolean)&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> sb;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，括号是可选的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;string | boolean&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> sb;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有多种方式来指定数组类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;number[]&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> ns;
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Array.<number>&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> nds;
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Array<number>&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> nas;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以指定对象字面量类型。 例如，一个带有<code>a</code>（字符串）和<code>b</code>（数字）属性的对象，使用下面的语法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;&#123; a: string, b: number &#125;</span></span>&#125; */</span>
<span class="hljs-keyword">var</span> var9;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用字符串和数字索引签名来指定<code>map-like</code>和<code>array-like</code>的对象，使用标准的JSDoc语法或者TypeScript语法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * A map-like object that maps arbitrary `string` properties to `number`s.
 *
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;Object.<string, number>&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> stringToNumber;

<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Object.<number, object>&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> arrayLike;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个类型与TypeScript里的<code>&#123; [x: string]: number &#125;</code>和<code>&#123; [x: number]: any &#125;</code>是等同的。编译器能识别出这两种语法。</p>
<p>可以使用TypeScript或Closure语法指定函数类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;function(string, boolean): number&#125;</span> </span>Closure syntax */</span>
<span class="hljs-keyword">var</span> sbn;
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;(s: string, b: boolean) => number&#125;</span> </span>Typescript syntax */</span>
<span class="hljs-keyword">var</span> sbn2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者直接使用未指定的<code>Function</code>类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Function&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> fn7;
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;function&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> fn6;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Closure的其它类型也可以使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;*&#125;</span> </span>- can be 'any' type
 */</span>
<span class="hljs-keyword">var</span> star;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;?&#125;</span> </span>- unknown type (same as 'any')
 */</span>
<span class="hljs-keyword">var</span> question;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">转换</h4>
<p>TypeScript借鉴了Closure里的转换语法。 在括号表达式前面使用<code>@type</code>标记，可以将一种类型转换成另一种类型</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;number | string&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> numberOrString = <span class="hljs-built_in">Math</span>.random() < <span class="hljs-number">0.5</span> ? <span class="hljs-string">"hello"</span> : <span class="hljs-number">100</span>;
<span class="hljs-keyword">var</span> typeAssertedNumber = <span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;number&#125;</span> </span>*/</span> (numberOrString)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">导入类型</h4>
<p>可以使用导入类型从其它文件中导入声明。 这个语法是TypeScript特有的，与JSDoc标准不同：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param </span>p &#123; import("./a").Pet &#125;
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walk</span>(<span class="hljs-params">p</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Walking <span class="hljs-subst">$&#123;p.name&#125;</span>...`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入类型也可以使用在类型别名声明中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@typedef <span class="hljs-type">&#123; import("./a").Pet &#125;</span> <span class="hljs-variable">Pet</span></span>
 */</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;Pet&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> myPet;
myPet.name;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入类型可以用在从模块中得到一个值的类型。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;typeof import("./a").x &#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> x = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./a"</span>).x;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><code>@param</code>和<code>@returns</code></h3>
<p><code>@param</code>语法和<code>@type</code>相同，但增加了一个参数名。 使用<code>[]</code>可以把参数声明为可选的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Parameters may be declared in a variety of syntactic forms</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span>  <span class="hljs-variable">p1</span></span> - A string param.
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string=&#125;</span> <span class="hljs-variable">p2</span></span> - An optional param (Closure syntax)
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>[p3] - Another optional param (JSDoc syntax).
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>[p4="test"] - An optional param with a default value
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string&#125;</span> </span>This is the result
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stringsStringStrings</span>(<span class="hljs-params">p1, p2, p3, p4</span>)</span>&#123;
  <span class="hljs-comment">// TODO</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数的返回值类型也是类似的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;PromiseLike<string>&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ps</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;&#123; a: string, b: number &#125;</span></span>&#125; - May use '<span class="hljs-doctag">@returns</span>' as well as '<span class="hljs-doctag">@return</span>'
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ab</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>@typedef</code>, <code>@callback</code>, 和 <code>@param</code></h3>
<p><code>@typedef</code>可以用来声明复杂类型。 和<code>@param</code>类似的语法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;Object&#125;</span> <span class="hljs-variable">SpecialType</span></span> - creates a new type named 'SpecialType'
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">prop1</span></span> - a string property of SpecialType
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">prop2</span></span> - a number property of SpecialType
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;number=&#125;</span> <span class="hljs-variable">prop3</span></span> - an optional number property of SpecialType
 * <span class="hljs-doctag">@prop <span class="hljs-type">&#123;number&#125;</span> </span>[prop4] - an optional number property of SpecialType
 * <span class="hljs-doctag">@prop <span class="hljs-type">&#123;number&#125;</span> </span>[prop5=42] - an optional number property of SpecialType with default
 */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;SpecialType&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> specialTypeObject;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在第一行上使用<code>object</code>或<code>Object</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;object&#125;</span> <span class="hljs-variable">SpecialType1</span></span> - creates a new type named 'SpecialType1'
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">prop1</span></span> - a string property of SpecialType1
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">prop2</span></span> - a number property of SpecialType1
 * <span class="hljs-doctag">@property <span class="hljs-type">&#123;number=&#125;</span> <span class="hljs-variable">prop3</span></span> - an optional number property of SpecialType1
 */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;SpecialType1&#125;</span> </span>*/</span>
<span class="hljs-keyword">var</span> specialTypeObject1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@param</code>允许使用相似的语法。 注意，嵌套的属性名必须使用参数名做为前缀：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> <span class="hljs-variable">options</span></span> - The shape is the same as SpecialType above
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>options.prop1
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> </span>options.prop2
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number=&#125;</span> </span>options.prop3
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> </span>[options.prop4]
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> </span>[options.prop5=42]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">special</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (options.prop4 || <span class="hljs-number">1001</span>) + options.prop5;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@callback</code>与<code>@typedef</code>相似，但它指定函数类型而不是对象类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@callback <span class="hljs-variable">Predicate</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">data</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> </span>[index]
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Predicate&#125;</span> </span>*/</span>
<span class="hljs-keyword">const</span> ok = <span class="hljs-function"><span class="hljs-params">s</span> =></span> !(s.length % <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，所有这些类型都可以使用TypeScript的语法<code>@typedef</code>在一行上声明：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;&#123; prop1: string, prop2: string, prop3?: number &#125;</span></span>&#125; SpecialType */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;(data: string, index?: number) => boolean&#125;</span> </span>Predicate */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><code>@template</code></h3>
<p>使用<code>@template</code>声明泛型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@template <span class="hljs-variable">T</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;T&#125;</span> <span class="hljs-variable">x</span></span> - A generic parameter that flows through to the return type
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;T&#125;</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">id</span>(<span class="hljs-params">x</span>)</span>&#123; <span class="hljs-keyword">return</span> x &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用逗号或多个标记来声明多个类型参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@template </span>T,U,V
 * <span class="hljs-doctag">@template </span>W,X
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以在参数名前指定类型约束。 只有列表的第一项类型参数会被约束：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@template <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">K</span></span> - K must be a string or string literal
 * <span class="hljs-doctag">@template <span class="hljs-type">&#123;&#123; serious(): string &#125;</span></span>&#125; Seriousalizable - must have a serious method
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;K&#125;</span> <span class="hljs-variable">key</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Seriousalizable&#125;</span> <span class="hljs-variable">object</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">seriousalize</span>(<span class="hljs-params">key, object</span>) </span>&#123;
  <span class="hljs-comment">// ????</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code>@constructor</code></h3>
<p>编译器通过<code>this</code>属性的赋值来推断构造函数，但你可以让检查更严格提示更友好，你可以添加一个<code>@constructor</code>标记：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@constructor</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">data</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.size = <span class="hljs-number">0</span>;
  <span class="hljs-built_in">this</span>.initialize(data); <span class="hljs-comment">// Should error, initializer expects a string</span>
&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 */</span>
C.prototype.initialize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.size = s.length
&#125;

<span class="hljs-keyword">var</span> c = <span class="hljs-keyword">new</span> C(<span class="hljs-number">0</span>);
<span class="hljs-keyword">var</span> result = C(<span class="hljs-number">1</span>); <span class="hljs-comment">// C should only be called with new</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>@constructor</code>，<code>this</code>将在构造函数<code>C</code>里被检查，因此你在<code>initialize</code>方法里得到一个提示，如果你传入一个数字你还将得到一个错误提示。如果你直接调用<code>C</code>而不是构造它，也会得到一个错误。</p>
<p>不幸的是，这意味着那些既能构造也能直接调用的构造函数不能使用<code>@constructor</code>。</p>
<h3 data-id="heading-8"><code>@this</code></h3>
<p>编译器通常可以通过上下文来推断出<code>this</code>的类型。但你可以使用<code>@this</code>来明确指定它的类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@this <span class="hljs-type">&#123;HTMLElement&#125;</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">e</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callbackForLater</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.clientHeight = <span class="hljs-built_in">parseInt</span>(e) <span class="hljs-comment">// should be fine!</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><code>@extends</code></h3>
<p>当JavaScript类继承了一个基类，无处指定类型参数的类型。而<code>@extends</code>标记提供了这样一种方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@template <span class="hljs-variable">T</span></span>
 * <span class="hljs-doctag">@extends <span class="hljs-type">&#123;Set<T>&#125;</span></span>
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SortableSet</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Set</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意<code>@extends</code>只作用于类。当前，无法实现构造函数继承类的情况。</p>
<h3 data-id="heading-10"><code>@enum</code></h3>
<p><code>@enum</code>标记允许你创建一个对象字面量，它的成员都有确定的类型。不同于JavaScript里大多数的对象字面量，它不允许添加额外成员。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@enum <span class="hljs-type">&#123;number&#125;</span> </span>*/</span>
<span class="hljs-keyword">const</span> JSDocState = &#123;
  <span class="hljs-attr">BeginningOfLine</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">SawAsterisk</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">SavingComments</span>: <span class="hljs-number">2</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意<code>@enum</code>与TypeScript的<code>@enum</code>大不相同，它更加简单。然而，不同于TypeScript的枚举，<code>@enum</code>可以是任何类型：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** <span class="hljs-doctag">@enum <span class="hljs-type">&#123;function(number): number&#125;</span> </span>*/</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">Math</span> = &#123;
  <span class="hljs-attr">add1</span>: <span class="hljs-function"><span class="hljs-params">n</span> =></span> n + <span class="hljs-number">1</span>,
  <span class="hljs-attr">id</span>: <span class="hljs-function"><span class="hljs-params">n</span> =></span> -n,
  <span class="hljs-attr">sub1</span>: <span class="hljs-function"><span class="hljs-params">n</span> =></span> n - <span class="hljs-number">1</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">更多示例</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> someObj = &#123;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">param1</span></span> - Docs on property assignments work
   */</span>
  <span class="hljs-attr">x</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">param1</span>)</span>&#123;&#125;
&#125;;

<span class="hljs-comment">/**
 * As do docs on variable assignments
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Window&#125;</span></span>
 */</span>
<span class="hljs-keyword">let</span> someFunc = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;

<span class="hljs-comment">/**
 * And class methods
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>greeting The greeting to use
 */</span>
Foo.prototype.sayHi = <span class="hljs-function">(<span class="hljs-params">greeting</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hi!"</span>);

<span class="hljs-comment">/**
 * And arrow functions expressions
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> <span class="hljs-variable">x</span></span> - A multiplier
 */</span>
<span class="hljs-keyword">let</span> myArrow = <span class="hljs-function"><span class="hljs-params">x</span> =></span> x * x;

<span class="hljs-comment">/**
 * Which means it works for stateless function components in JSX too
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;&#123;a: string, b: number&#125;</span></span>&#125; test - Some param
 */</span>
<span class="hljs-keyword">var</span> fc = <span class="hljs-function">(<span class="hljs-params">test</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;test.a.charAt(0)&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;

<span class="hljs-comment">/**
 * A parameter can be a class constructor, using Closure syntax.
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;&#123;new(...args: any[]): object&#125;</span></span>&#125; C - The class to register
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerClass</span>(<span class="hljs-params">C</span>) </span>&#123;&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;...string&#125;</span> <span class="hljs-variable">p1</span></span> - A 'rest' arg (array) of strings. (treated as 'any')
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn10</span>(<span class="hljs-params">p1</span>)</span>&#123;&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;...string&#125;</span> <span class="hljs-variable">p1</span></span> - A 'rest' arg (array) of strings. (treated as 'any')
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn9</span>(<span class="hljs-params">p1</span>) </span>&#123;
  <span class="hljs-keyword">return</span> p1.join();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">已知不支持的模式</h3>
<p>在值空间中将对象视为类型是不可以的，除非对象创建了类型，如构造函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">aNormalFunction</span>(<span class="hljs-params"></span>) </span>&#123;

&#125;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;aNormalFunction&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> wrong;
<span class="hljs-comment">/**
 * Use 'typeof' instead:
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;typeof aNormalFunction&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> right;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象字面量属性上的<code>=</code>后缀不能指定这个属性是可选的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;&#123; a: string, b: number= &#125;</span></span>&#125;
 */</span>
<span class="hljs-keyword">var</span> wrong;
<span class="hljs-comment">/**
 * Use postfix question on the property name instead:
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;&#123; a: string, b?: number &#125;</span></span>&#125;
 */</span>
<span class="hljs-keyword">var</span> right;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Nullable</code>类型只在启用了<code>strictNullChecks</code>检查时才启作用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;?number&#125;</span></span>
 * With strictNullChecks: true -- number | null
 * With strictNullChecks: off  -- number
 */</span>
<span class="hljs-keyword">var</span> nullable;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Non-nullable</code>类型没有意义，以其原类型对待：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;!number&#125;</span></span>
 * Just has type number
 */</span>
<span class="hljs-keyword">var</span> normal;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不同于JSDoc类型系统，TypeScript只允许将类型标记为包不包含<code>null</code>。 没有明确的<code>Non-nullable</code> -- 如果启用了<code>strictNullChecks</code>，那么<code>number</code>是非<code>null</code>的。 如果没有启用，那么<code>number</code>是可以为<code>null</code>的。</p></div>  
</div>
            