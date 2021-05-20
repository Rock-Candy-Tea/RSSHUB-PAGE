
---
title: '理解ECMAScript规范（4）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6488'
author: 掘金
comments: false
date: Wed, 19 May 2021 23:28:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=6488'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>翻译本文的目的是尝试给出 ECMAScript 规范中核心术语的译法，供同好品评。</p>
</blockquote>
<p>原文链接：<a href="https://v8.dev/blog/understanding-ecmascript-part-4" target="_blank" rel="nofollow noopener noreferrer">v8.dev/blog/unders…</a></p>
<h2 data-id="heading-0">环球同此凉热</h2>
<p>Mozilla 的<a href="https://github.com/jorendorff" title="Jason Orendorff" target="_blank" rel="nofollow noopener noreferrer">Jason Orendorff</a>写了一篇深入分析 JS 诡异语法的文章。虽然实现细节上有差异，但每个 JS 引擎在这些诡异的细节上都会面对同样的问题。</p>
<h2 data-id="heading-1">包含文法</h2>
<p>这篇文章将深入探讨包含文法（cover grammar）。包含文法是为那些乍一看模棱两可的语法构造规定文法的一种方式。</p>
<p>为简单起见，我们跳过下标<code>[In, Yield, Await]</code>，因为对本文不重要。可以参考<a href="https://lisongfeng.cn/2020/09/16/understanding-ecmascript-part-3.html" title="第三篇文章" target="_blank" rel="nofollow noopener noreferrer">第三篇文章</a>，了解它们的含义和用法。</p>
<h2 data-id="heading-2">有限前查</h2>
<p>通常，解析器在<strong>有限前查</strong>（finite lookhead，跟进固定个数的标记）基础上决定使用哪个产生式。</p>
<p>有时候，下一个标记可以毫无歧义地决定要使用的产生式。<a href="https://tc39.es/ecma262/#prod-UpdateExpression" title="例如" target="_blank" rel="nofollow noopener noreferrer">例如</a>：</p>
<pre><code class="copyable"><pre>
<i>UpdateExpression</i> :
  <i>LeftHandSideExpression</i>
  <i>LeftHandSideExpression</i> ++
  <i>LeftHandSideExpression</i> --
  ++ <i>UnaryExpression</i>
  -- <i>UnaryExpression</i>
</pre>

<!--more-->
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们正在解析<code>UpdateExpression</code>且下一个标记是<code>++</code>或<code>--</code>，那我们马上就知道要使用哪个产生式。如果下一个标记不是它们两个，那也问题不大，可以从所在位置开始解析<code>LeftHandSideExpression</code>，解析完之后再决定下一步干什么。</p>
<p>如果<code>LeftHandSideExpression</code>后面的标记是<code>++</code>，则要使用的产生式是<code>UpdateExpression : LeftHandSideExpression ++</code>。后面是<code>--</code>的情形类似。如果<code>LeftHandSideExpression</code>后面的标记既不是<code>++</code>也不是<code>--</code>，则使用产生式<code>UpdateExpression : LeftHandSideExpression</code>。</p>
<h3 data-id="heading-3">箭头函数参数列表，还是带括号的表达式？</h3>
<p>区分箭头函数参数列表与带括号的表达式更复杂一些。如：</p>
<pre><code class="copyable">let x = (a,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个箭头函数的开头吗，如：</p>
<pre><code class="copyable">let x = (a, b) => &#123; return a + b &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是一个带括号的表达式，如：</p>
<pre><code class="copyable">let  x = (a, 3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>括号中的内容，不管是什么，但可能是任意长度。因此不能根据有限标记确定它是什么。</p>
<p>想象一下，假设我们有下列直观的产生式：</p>
<pre><code class="copyable"><pre>
<i>AssignmentExpression</i> :
  ...
  <i>ArrowFunction</i>
  <i>ParenthesizedExpression</i>

<i>ArrowFunction</i> :
  <i>ArrowParameterList</i> => <i>ConciseBody</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那就可以使用有限前查来选择产生式。如果解析到<code>AssignmentExpression</code>之后，下一个标记是<code>(</code>，那怎么确定接下来解析什么？可以解析<code>ArrowParameterList</code>，也可以解析<code>ParenthesizedExpression</code>，但肯定有可能猜错。</p>
<h3 data-id="heading-4">非常宽纵的新符号：<code>CPEAAPL</code></h3>
<p>规范通过增加一个符号来解决这个问题：<code>CoverParenthesizedExpressionAndArrowParameterList</code>，简写成<code>CPEAAL</code>。<code>CPEAAL</code>表示既可能是<code>ParenthesizedExpression</code>也可能是<code>ArrowParameterList</code>，但现在不知道选哪个。</p>
<p><a href="https://tc39.es/ecma262/#prod-CoverParenthesizedExpressionAndArrowParameterList" title="`CPEAAL`的产生式" target="_blank" rel="nofollow noopener noreferrer">CPEAAL的产生式</a>非常宽纵，允许任何可以出现在<code>ParenthesizedExpression</code>和<code>ArrowParameterList</code>中的构造：</p>
<pre><code class="copyable"><pre>
<i> CPEAAPL </i> :
  ( <i>Expression</i> )
  ( <i>Expression ,</i> )
  ( )
  ( <i>... BindingIdentifier</i> )
  ( <i>... BindingPattern</i> )
  ( <i>Expression</i> , <i>... BindingIdentifier</i> )
  ( <i>ArrowFunction</i> , <i>... BindingPattern</i> )
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如，下列表达式都是有效的<code>CPEAAPL</code>：</p>
<pre><code class="copyable">// 有效的ParenthesizedExpression和ArrowParameterList：
(a, b)
(a, b = 1)

// 有效的ParenthesizedExpression：
(1, 2, 3)
(function foo() &#123; &#125;)

// 有效的ArrowParameterList：
()
(a, b,)
(a, ...b)
(a = 1, ...b)

// 两个都无效，但仍然是CPEAAPL：
(1, ...b)
(1, )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>末尾的逗号和<code>...</code>只可能出现在<code>ArrowParameterList</code>中。有的构造（如<code>b = 1</code>）两种情况下都有可能出现，但是含义不同：出现在<code>ParenthesizedExpression</code>中是赋值，出现在<code>ArrowParameterList</code>中是带默认值的参数。数值及其他不是有效参数名的<code>PrimaryExpression</code>（或参数解构模式）只可能出现在<code>ParenthesizedExpression</code>中。但它们都可能出现在<code>CPEAAPL</code>中。</p>
<h3 data-id="heading-5">在产生式中使用<code>CPEAAPL</code></h3>
<p>现在我们可以在<code>AssignmentExpression</code>产生式中使用这个非常宽纵的<code>CPEAAPL</code>。（注意：<code>ConditionalExpression</code>通过一个长长的产生式链通往<code>PrimaryExpression</code>，这里没有展示中间经过的产生式。）</p>
<pre><code class="copyable"><pre>
<i>AssignmentExpression</i> :
  <i>ConditionalExpression</i>
  <i>ArrowFunction</i>
  ...

<i>ArrowFunction</i> :
  <i>ArrowParameters</i> => <i>ConciseBody</i>

<i>ArrowParameters</i> :
  <i>BindingIdentifier</i>
  <i>CPEAAPL</i>

<i>PrimaryExpression</i> :
  ...
  <i>CPEAAPL</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想象一下，我们再次碰到之前的情形：解析到<code>AssignmentExpression</code>之后，下一个标记是<code>(</code>。这一次我们可以解析<code>CPEAAPL</code>，到后面再看要使用哪个产生式。此时是解析<code>ArrowFunction</code>还是解析<code>ConditionalExpression</code>并不重要，无论解析哪一个，下一个要解析的符号都是<code>CPEAAPL</code>！</p>
<p>解析完<code>CPEAAPL</code>之后，就可以决定最开始的（包含这个<code>CPEAAPL</code>的）<code>AssignmentExpression</code>使用哪个产生式了。这是由<code>CPEAAPL</code>后面跟着的标记决定的。</p>
<p>如果这个标记是<code>=></code>，则使用下面的产生式：</p>
<pre><code class="copyable"><pre>
<i>AssignmentExpression</i> :
  <i>ArrowFunction</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果这个标记是其他什么，则使用这个产生式：</p>
<pre><code class="copyable"><pre>
<i>AssignmentExpression</i> :
  <i>ConditionalExpression</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如：</p>
<pre><code class="copyable">let x = (a, b) => &#123; return a + b; &#125;;
//      ^^^^^^
//     CPEAAPL
//             ^^
//             跟在CPEAAPL后面的标记

let x = (a, 3);
//      ^^^^^^
//     CPEAAPL
//            ^
//            跟在CPEAAPL后面的标记
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时可以保持<code>CPEAAPL</code>不变，继续解析程序其余部分。比如，如果这个<code>CPEAAPL</code>在<code>ArrowFunction</code>中，那现在还不需要看它是不是有效的箭头函数参数列表，可以在后面再检查。（实际的解析器可以选择此时立即做有效性检查，但从规范角度看这不是必需的。）</p>
<h3 data-id="heading-6">限制<code>CPEAAPL</code></h3>
<p>如前所示，<code>CPEAAPL</code>的产生式非常宽纵，允许根本不合法的构造（如<code>(1, ...a)</code>）。在按照文法解析完程序后，需要驳回其中不合法的构造。</p>
<p>规范为此增加了如下限制：</p>
<blockquote>
<p><a href="https://tc39.es/ecma262/#sec-grouping-operator-static-semantics-early-errors" title="静态语义：前期错误" target="_blank" rel="nofollow noopener noreferrer">静态语义：前期错误</a></p>
</blockquote>
<blockquote>
<p><code>PrimaryExpression : CPEAAPL</code></p>
<ul>
<li>如果 CPEAAPL 未包含<code>ParenthesizedExpression</code>就是一个语法错误。</li>
</ul>
</blockquote>
<blockquote>
<p><a href="https://tc39.es/ecma262/#sec-expression" title="补充语法" target="_blank" rel="nofollow noopener noreferrer">补充语法</a></p>
</blockquote>
<blockquote>
<p>在处理以下产生式的实例时</p>
</blockquote>
<blockquote>
<p><code>PrimaryExpression : CPEAAPL</code></p>
</blockquote>
<blockquote>
<p>对<code>CPEAAPL</code>的解释使用以下文法改进（refine）：</p>
</blockquote>
<blockquote>
<p><code>ParenthesizedExpression : ( Expression )</code></p>
</blockquote>
<p>这意味着：如果<code>CPEAAPL</code>在语法树中出现在<code>PrimaryExpression</code>中，那它实际上是<code>ParenthesizedExpression</code>，而这是它唯一有效的产生式。</p>
<p><code>Expression</code>永远不能为空，因此<code>( )</code>不是有效的<code>ParenthesizedExpression</code>。逗号分隔的列表，如<code>(1, 2, 3)</code>是通过<a href="https://tc39.es/ecma262/#sec-comma-operator" title="逗号操作符" target="_blank" rel="nofollow noopener noreferrer">逗号操作符</a>创建的：</p>
<pre><code class="copyable"><pre>
<i>Expression</i> :
  <i>AssignmentExpression</i>
  <i>Expression</i> , <i>AssignmentExpression</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似地，如果<code>CPEAAPL</code>出现在<code>ArrowParameters</code>中，则适用如下限制：</p>
<blockquote>
<p><a href="https://tc39.es/ecma262/#sec-arrow-function-definitions-static-semantics-early-errors" title="静态语义：前期错误" target="_blank" rel="nofollow noopener noreferrer">静态语义：前期错误</a></p>
</blockquote>
<blockquote>
<p><code>ArrowParameters : CPEAAPL</code></p>
<ul>
<li>如果 CPEAAPL 未包含<code>ArrowFormalParameters</code>就是一个语法错误。</li>
</ul>
</blockquote>
<blockquote>
<p><a href="https://tc39.es/ecma262/#sec-arrow-function-definitions" title="补充语法" target="_blank" rel="nofollow noopener noreferrer">补充语法</a></p>
</blockquote>
<blockquote>
<p>在处理以下产生式的实例时</p>
</blockquote>
<blockquote>
<p><code>ArrowParameters : CPEAAPL</code></p>
</blockquote>
<blockquote>
<p>对<code>CPEAAPL</code>的解释使用以下文法改进（refine）：</p>
</blockquote>
<blockquote>
<p><code>ArrowFormalParameters : ( UniqueFormalParameters )</code></p>
</blockquote>
<h3 data-id="heading-7">其他包含文法</h3>
<p>除了<code>CPEAAPL</code>，规范还对其他看起来不明确的构造使用了包含文法。</p>
<p>出现在箭头函数参数列表中的<code>ObjectAssignmentPattern</code>把<code>ObjectLiteral</code>用作包含文法。这意味着<code>ObjectLiteral</code>允许在实际的对象字面量中不能出现的构造。</p>
<pre><code class="copyable"><pre>
<i>ObjectLiteral</i> :
  ...
  &#123; <i>PropertyDefinitionList</i> &#125;

<i>PropertyDefinition</i> :
  ...
  <i>CoverInitializedName</i>

<i>CoverInitializedName</i> :
  <i>IdentifierReference Initializer</i>

<i>Initializer</i> :
  = <i>AssignmentExpression</i>
</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如：</p>
<pre><code class="copyable">let o = &#123; a = 1 &#125;; // 语法错误

// 箭头函数使用了带默认值的解构参数：
let f = (&#123; a = 1 &#125;) => &#123; return a; &#125;;
f(&#123;&#125;); // 返回1
f(&#123;a : 6&#125;); // 返回6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步箭头函数在使用有限前查时同样有歧义：</p>
<pre><code class="copyable">let x = async(a,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是调用<code>async</code>函数呢，还是一个异步箭头函数？</p>
<pre><code class="copyable">let x1 = async(a, b);
let x2 = async();
function async() &#123; &#125;

let x3 = async(a, b) => &#123;&#125;;
let x4 = async();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为此，文法定义了一个包含文法符号<code>CoverCallExpressionAndAsyncArrowHead</code>，其原理与<code>CPEAAPL</code>类似。</p>
<h2 data-id="heading-8">小结</h2>
<p>本文介绍了规范怎么定义包含文法，并且在基于有限前查无法识别当前语法构造时使用它们。</p>
<p>特别地，我们探讨了区分箭头函数参数与带括号的表达式，以及规范在碰到看不懂的构造时怎么宽纵地使用包含文法，并且又在后面用静态语义来限制它们。</p></div>  
</div>
            