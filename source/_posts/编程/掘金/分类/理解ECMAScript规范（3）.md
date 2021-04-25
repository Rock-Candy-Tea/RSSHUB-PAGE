
---
title: '理解ECMAScript规范（3）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8863'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 23:34:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=8863'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>翻译本文的目的是尝试给出 ECMAScript 规范中核心术语的译法，供同好品评。</p>
</blockquote>
<p>这一次我们深入 ECMAScript 语言及其语法的定义。如果你不太熟悉<a href="https://en.wikipedia.org/wiki/Context-free_grammar" title="文无关文法" target="_blank" rel="nofollow noopener noreferrer">上下文无关文法</a>，应该先补补课，至少先弄懂一些基本概念。因为规范中使用了上下文无关文法定义语言。</p>
<h2 data-id="heading-0">ECMAScript 文法</h2>
<p>ECMAScript 规范定义了 4 种文法。</p>
<ol>
<li><a href="https://tc39.es/ecma262/#sec-ecmascript-language-lexical-grammar" title="词法文法" target="_blank" rel="nofollow noopener noreferrer">词法文法</a>：描述怎么把<a href="https://en.wikipedia.org/wiki/Unicode#Architecture_and_terminology" title="Unicode码点" target="_blank" rel="nofollow noopener noreferrer">Unicode 码点</a>（code point）翻译为<strong>输入元素</strong>（标记、行终止符、注释、空白）序列。</li>
<li><a href="https://tc39.es/ecma262/#sec-syntactic-grammar" title="语法文法" target="_blank" rel="nofollow noopener noreferrer">语法文法</a>：定义标记（token）怎么构成语法正确的程序。</li>
<li><a href="https://tc39.es/ecma262/#sec-patterns" title="正则文法" target="_blank" rel="nofollow noopener noreferrer">正则文法</a>：描述怎么把 Unicode 码点翻译为正则表达式。</li>
<li><a href="https://tc39.es/ecma262/#sec-tonumber-applied-to-the-string-type" title="数值字符串文法" target="_blank" rel="nofollow noopener noreferrer">数值字符串文法</a>：描述怎么把 String 翻译成数字值。</li>
</ol>
<p>每种文法都用上下文无关文法来定义，都包含一组产生式。</p>
<p>不同的文法使用了不同的表示方式。语法文法表示为<code>LeftHandSideSymbol :</code>，词法文法和正则文法表示为<code>LeftHandSideSymbol ::</code>，而数值字符串文法表示为<code>LeftHandSideSymbol :::</code>。（以冒号的多少来区分。——译者注）</p>
<p>接下来我们详细分析一下词法文法和语法文法。</p>

<h2 data-id="heading-1">词法文法</h2>
<p>规范将 ECMAScript 源文本定义为一个 Unicode 码点序列。这意味着变量名并不限于 ASCII 字符，也可以包含其他 Unicode 字符。规范并没有谈到实际的编码（如 UTF-8 或 UTF-16），而是假设源代码已经按照自己的编码转换成了 Unicode 码点序列。</p>
<p>无法提前对 ECMAScript 源码进行标记化（tokenize），这使得定义词法文法略显复杂。比如，如果不看它所处的更大的上下文，就无法确定/是除法操作符还是正则表达式的开始。</p>
<pre><code class="copyable">const x = 10 / 5;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>/</code>是<code>DivPunctuator</code>。</p>
<pre><code class="copyable">const r = /foo/;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>/</code>是<code>RegularExpressionLiteral</code>的开头。</p>
<p>模板也引入了类似的歧义：对<code>&#125;`</code>的解释取决于它出现的上下文:</p>
<pre><code class="copyable">const what1 = 'temp';
const what2 = 'late';
const t = `I am a $&#123; what1 + what2 &#125;`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>I am a $&#123;</code>是<code>TemplateHead</code>，而 <code>&#125;</code> 是 <code>TemplateTail</code> 。</p>
<pre><code class="copyable">if (0 == 1) &#123;
&#125;`not very useful`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>&#125;</code>是<code>RightBracePunctuator</code>，而<code>`</code>是<code>NoSubstitutionTemplate</code>的开头。</p>
<p>即便对<code>/</code>和<code>&#125;`</code>的解释取决于上下文（它们在代码语法结构中的位置），我们下面介绍的文法仍然是上下文无关的。</p>
<p>词汇文法使用一些目标符号（goal symbol）来区分哪些上下文允许哪些输入元素，不允许哪些输入元素。例如，目标符号<code>InputElementDiv</code>（注意，这里的<code>Div</code>是 Divide，即除法的意思。——译者注）会用在<code>/</code>是除法和<code>/=</code>是除法赋值的上下文中。<code>InputElementDiv</code>产生式列出了在此上下文中可能产生的标记：</p>
<pre><code class="copyable">InputElementDiv ::
  WhiteSpace
  LineTerminator
  Comment
  CommonToken
  DivPunctuator
  RightBracePunctuator
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个上下文中，遇到<code>/</code>产生输入元素<code>DivPunctuator</code>，而不会产生<code>RegularExpressionLiteral</code>。</p>
<p>相应地，对于<code>/</code>是正则表达式开头的上下文，目标符号是<code>InputElementRegExp</code>：</p>
<pre><code class="copyable">InputElementRegExp ::
  WhiteSpace
  LineTerminator
  Comment
  CommonToken
  RightBracePunctuator
  RegularExpressionLiteral
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个产生式可以产生<code>RegularExpressionLiteral</code>输入元素，但不可能产生<code>DivPunctuator</code>。</p>
<p>类似地，目标符号<code>InputElementRegExpOrTemplateTail</code>对应的上下文除了<code>RegularExpressionLiteral</code>，还允许出现<code>TemplateMiddle</code>和<code>TemplateTail</code>。最后一个<code>InputElementTemplateTail</code>目标符号的上下文只允许<code>TemplateMiddle</code>和<code>TemplateTail</code>，不允许出现<code>RegularExpressionLiteral</code>。</p>
<p>在实现中，语法文法分析器(“解析器”)可以调用词法文法分析器(“标记器”或“词法器”)，将目标符号作为参数传递，并请求适合该目标符号的下一个输入元素。</p>
<h2 data-id="heading-2">语法文法</h2>
<p>词法文法定义了如何从 Unicode 码点构建标记。语法文法建立在它的基础上，定义了标记如何组成语法正确的程序。</p>
<h3 data-id="heading-3">例子：允许遗留标识符</h3>
<p>给文法增加新关键字有可能造成破坏：如果原有代码已经使用该关键字作为标识符了怎么办？</p>
<p>例如，在<code>await</code>还不是关键字的时候，可能出现这样的代码：</p>
<pre><code class="copyable">function old() &#123;
  var await;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ECMAScript 文法谨慎地添加了 await 关键字，以便这段代码可以继续工作。在 async 函数里面，await 是一个关键字，所以不能这样写：</p>
<pre><code class="copyable">async function modern() &#123;
  var await; // 语法错误
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在非生成器中允许<code>yield</code>，而在生成器中不允许与此类似。</p>
<p>要理解怎么允许<code>await</code>作为标识符，需要理解 ECMAScript 特定的语法文法表示。</p>
<h3 data-id="heading-4">产生式与简写形式</h3>
<p>来看看<code>VariableStatement</code>的产生式是怎么定义的。乍一看，这个文法有点吓人：</p>
<pre><code class="copyable">VariableStatement[Yield, Await] :
 var VariableDeclarationList[+In, ?Yield, ?Await] ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的下标（<code>[Yield, Await]</code>）和前缀（<code>+In</code>里的<code>+</code>和<code>?Await</code>里的<code>?</code>）都什么意思呀？</p>
<p>这种表示法在“<a href="https://tc39.es/ecma262/#sec-grammar-notation" title="文法表示法" target="_blank" rel="nofollow noopener noreferrer">文法表示法</a>”中有解释。</p>
<p>下标是对一组产生式的简写形式，一次性表达了一组产生式左端（left-hand side）符号。这个产生式左端符号有两个参数，它们可以展开为四个“真正的”产生式左端符号：</p>
<ul>
<li><code>VariableStatement</code></li>
<li><code>VariableStatement_Yield</code></li>
<li><code>VariableStatement_Await</code></li>
<li><code>VariableStatement_Yield_Await</code></li>
</ul>
<p>注意，以上<code>VariableStatement</code>就表示<code>VariableStatement</code>，没有<code>_Await</code>也没有<code>_Yield</code>。不要把它跟<code><i>VariableStatement</i><sub>[Yield, Await]</sub></code>（简写形式）弄混了。</p>
<p>在产生式右端，可以看到简写<code>+In</code>，意思是“使用带<code>_In</code>的版本”，而<code>?Await</code>的意思是“当且仅当左端符号有<code>_Await</code>时使用带<code>_Await</code>的版本”（<code>?Yield</code>也是类似的）。</p>
<p>第三种简写形式<code>~Foo</code>，意思是“使用没有<code>_Foo</code>的版本”（这个产生式中没有出现）。</p>
<p>了解了这些，可以把上面的产生式展开成这样：</p>
<pre><code class="copyable"> VariableStatement :
   var VariableDeclarationList_In ;

 VariableStatement_Yield :
   var VariableDeclarationList_In_Yield ;

 VariableStatement_Await :
   var VariableDeclarationList_In_Await ;

 VariableStatement_Yield_Await :
   var VariableDeclarationList_In_Yield_Await ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，还有要搞清楚两件事。</p>
<ol>
<li>在哪里确定我们处在有<code>_Await</code>或没有<code>_Await</code>的情况下？</li>
<li>有它和没它有什么区别，或者说<code>Something_Await</code>的产生式和<code>Something</code>（没有<code>_Await</code>）的产生式是在哪里分叉的？</li>
</ol>
<h3 data-id="heading-5"><code>_Await</code>还是没有<code>_Await</code></h3>
<p>先解决第一个问题。因为很容易猜到可以根据函数体是否带<code>_Await</code>来区分异步函数和非异步函数。看异步函数声明的产生式，我们发现了<a href="https://tc39.es/ecma262/#prod-AsyncFunctionBody" title="这个" target="_blank" rel="nofollow noopener noreferrer">这个</a>：</p>
<pre><code class="copyable">AsyncFunctionBody :
  FunctionBody[~Yield, +Await] 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意<code>AsyncFunctionBody</code>没有参数，参数在右端被添加给了<code>FunctionBody</code>。展开这个产生式得到：</p>
<pre><code class="copyable">AsyncFunctionBody :
  FunctionBody_Await
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换句话说，异步函数有<code>FunctionBody_Await</code>（即一个<code>await</code>会被当成关键字的）函数体。</p>
<p>另一方面，如果是在非异步函数中，<a href="https://tc39.es/ecma262/#prod-FunctionDeclaration" title="相关产生式" target="_blank" rel="nofollow noopener noreferrer">相关产生式</a>为：</p>
<pre><code class="copyable">FunctionDeclaration[Yield, Await, Default] :
  function BindingIdentifier[?Yield, ?Await] ( FormalParameters[~Yield, ~Await]) &#123; FunctionBody[~Yield, ~Await] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（<code>FunctionDeclaration</code>还有一个产生式，但跟我们的代码示例不相关。）</p>
<p>为避免组合展开，我们忽略<code>Default</code>参数，因为这个特别的产生式中没用到。于是，这个产生式的展开形式为：</p>
<pre><code class="copyable">FunctionDeclaration :
  function BindingIdentifier ( FormalParameters ) &#123; FunctionBody &#125; 

FunctionDeclaration_Yield :
  function BindingIdentifier_Yield ( FormalParameters ) &#123; FunctionBody &#125; 

FunctionDeclaration_Await :
  function BindingIdentifier_Await ( FormalParameters ) &#123; FunctionBody &#125; 

FunctionDeclaration_Yield_Await :
  function BindingIdentifier_Yield_Await ( FormalParameters ) &#123; FunctionBody &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个产生式中，只有<code>FunctionBody</code>和<code>FormalParameters</code>（不带<code>_Yield</code>，也不带<code>_Await</code>），因为在未展开的产生式中它们都有参数<code>[~Yield, ~Await]</code>。</p>
<p>函数名的处理方式就不一样了：如果产生式左端符号中包含<code>_Yield</code>和<code>_Await</code>，则右端的函数名也会带上相应参数。</p>
<p>总结：异步函数有<code>FunctionBody_Await</code>，而非异步函数有<code>FunctionBody</code>（不带<code>_Await</code>）。因为我们讨论的是非生成器函数，所以无论异步示例函数还是非异步示例函数，都不会带参数<code>_Yield</code>。</p>
<p>可能记住哪个是<code>FunctionBody</code>，哪个是<code>FunctionBody_Await</code>有点难。在有<code>FunctionBody_Await</code>的函数体中，<code>await</code>是标识符，还是关键字？</p>
<p>可以把<code>_Await</code>参数的意思理解为“<code>await</code>是一个关键字。”这样理解在将来也不会有问题。假设将来又添加了一个<code>blob</code>关键字，但只适用于“斑驳”（blobby）函数。非斑驳、非异步、非生成器的函数仍然有<code>FunctionBody</code>（不带<code>_Yield</code>、<code>_Await</code>或<code>_Blob</code>），跟现在完全一样。斑驳函数则会有<code>FunctionBody_Await_Blob</code>等。虽然仍然要在产生式中添加<code>Blob</code>下标，但已存在函数的<code>FunctionBody</code>的展开形式还跟以前一样。</p>
<h3 data-id="heading-6">不允许<code>await</code>用作标识符</h3>
<p>接下来，我们要搞清楚在<code>FunctionBody_Await</code>中，是怎么不允许<code>await</code>用作标识符的。</p>
<p>仔细看一看产生式，可以发现从<code>FunctionBody</code>到之前的<code>VariableStatement</code>产生式都带<code>_Await</code>参数。因此，在异步函数中，就有<code>VariableStatement_Await</code>，而在非异步函数中，则有<code>VariableStatement</code>。</p>
<p>再看仔细一点，注意一下参数。我们已经看到了这个<a href="https://tc39.es/ecma262/#prod-VariableStatement" title="`VariableStatement`" target="_blank" rel="nofollow noopener noreferrer">VariableStatement</a>的产生式：</p>
<pre><code class="copyable">VariableStatement[Yield, Await] :
  var VariableDeclarationList[+In, ?Yield, ?Await] ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有<a href="https://tc39.es/ecma262/#prod-VariableDeclarationList" title="`VariableDeclarationList`" target="_blank" rel="nofollow noopener noreferrer">VariableDeclarationList</a>的产生式也都照样带这些参数：</p>
<pre><code class="copyable">VariableDeclarationList[In, Yield, Await] :
  VariableDeclaration[?In, ?Yield, ?Await] 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(这里只展示与我们例子相关的<a href="https://tc39.es/ecma262/#prod-VariableDeclaration" title="产生式" target="_blank" rel="nofollow noopener noreferrer">产生式</a>。)</p>
<pre><code class="copyable">VariableDeclarationList[In, Yield, Await] :
  BindingIdentifier[?Yield, ?Await] Initializer [?In, ?Yield, ?Await]opt ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>opt</code>简写代表产生式右端符号是可选的，也就是实际上有两个产生式：一个带可选的符号（<code>Initializer</code>），另一个不带。</p>
<p>对我们简单的例子来说，<code>VariableStatement</code>包含关键字<code>var</code>，紧跟一个<code>BindingIdentifier</code>（没有初始化器<code>Initializer</code>），以分号结束。</p>
<p>为了允许或不允许<code>await</code>用作<code>BindingIdentifier</code>，我们希望最终看到这些：</p>
<pre><code class="copyable">BindingIdentifier_Await :
  Identifier 
  yield

BindingIdentifier :
  Identifier 
  yield
  await
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这表示在异步函数中不允许<code>await</code>作为标识符，在非异步函数允许它作为标识符。</p>
<p>实际上规范中并没有给出这样的定义，而我们找到的是这个产生式：</p>
<pre><code class="copyable">BindingIdentifier[Yield, Await] :
  Identifier 
  yield
  await
<span class="copy-code-btn">复制代码</span></code></pre>
<p>展开后得到：</p>
<pre><code class="copyable">BindingIdentifier_Await :
  Identifier 
  yield
  await

BindingIdentifier :
  Identifier 
  yield
  await
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（这里省略了<code>BindingIdentifier_Yield</code>和<code>BindingIdentifier_Yield_Await</code>的产生式，因为我们的例子不需要。）</p>
<p>这么看<code>await</code>和<code>yield</code>任何时候都可以作为标识符。这是怎么回事啊？这篇文章难道白写了吗？</p>
<h3 data-id="heading-7">静态语义出马</h3>
<p>原来为了在异步函数中禁止将<code>await</code>用作标识符，还需要用到<strong>静态语义</strong>。</p>
<p>静态语义描述静态规则，也就是在程序运行前要校验的规则。</p>
<p>对我们的例子而言，<a href="https://tc39.es/ecma262/#sec-identifiers-static-semantics-early-errors" title="`BindingIdentifier`的静态语义" target="_blank" rel="nofollow noopener noreferrer">BindingIdentifier的静态语义</a>定义了以下语法导向的规则：</p>
<pre><code class="copyable">BindingIdentifier[Yield, Await] : await
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果这个产生式有<code>[Await]</code>参数就是一个语法错误（Syntax Error）。</li>
</ul>
<p>实际上，这就是禁止<code>BindingIdentifier_Await : await</code>产生式。</p>
<p>规范解释说，之所以存在这个产生式但又通过静态语义将它定义为语法错误，是因为与 ASI（Automatic Semicolon Insertion，自动插入分号）冲突。</p>
<p>我们知道，在无法根据语法产生式解析一行代码时，ASI 就会介入。ASI 尝试添加分号以满足语句和声明必须以分号结束的要求。（关于 ASI 的详细介绍，可以看下一篇文章。）</p>
<p>来看下面的代码（规范中的例子）：</p>
<pre><code class="copyable">async function too_few_semicolons() &#123;
  let
  await 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果文法不允许<code>await</code>作用标识符，ASI 就会介入并将上面的代码转换为下面这样文法正确的代码，这样<code>let</code>也会被当成标识符：</p>
<pre><code class="copyable">async function too_few_semicolons() &#123;
  let;
  await 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与 ASI 的这种冲突被认为太令人困惑，因此才用静态语义禁止<code>await</code>作为标识符。</p>
<h3 data-id="heading-8">不允许标识符的<code>StringValues</code></h3>
<p>还有另一条相关规则：</p>
<pre><code class="copyable">BindingIdentifier : Identifier 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果这个产生式有<code>[Await]</code>参数，且<code>Identifier</code>的<code>StringValue</code>是<code>"await"</code>，就是一个语法错误（Syntax Error）。</li>
</ul>
<p>乍一看不好理解。<a href="https://tc39.es/ecma262/#prod-Identifier" title="Identifier的定义" target="_blank" rel="nofollow noopener noreferrer">Identifier 的定义</a>如下：</p>
<pre><code class="copyable">Identifier : 
 IdentifierName  but not  ReservedWord 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>await</code>是个<code>ReservedWord</code>，因此<code>Identifier</code>怎么可能是<code>await</code>呢？</p>
<p>的确，<code>Identifier</code>不可能是<code>await</code>，但可以是<code>StringValue</code>为<code>"await"</code>（字符序列<code>await</code>的一种不同的表示方式）的其他值。</p>
<p><a href="https://tc39.es/ecma262/#sec-identifier-names-static-semantics-stringvalue" title="标识符名的静态语义" target="_blank" rel="nofollow noopener noreferrer">标识符名的静态语义</a> 定义了如何计算标识符的<code>StringValue</code>。比如，<code>a</code>的 Unicode 转义序列是<code>\u0061</code>，因此<code>\u0061wait</code>的<code>StringValue</code>是<code>"await"</code>。<code>\u0061wait</code>不会被词法语法识别为关键字，而会被识别为<code>Identifier</code>。静态语义禁止在异步函数中使用它作为变量名。</p>
<p>因此，这样可以：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">old</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> \u0061wait;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这样不行：</p>
<pre><code class="copyable">async function modern() &#123;
  var \u0061wait; // 语法错误
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">小结</h2>
<p>通过学习这篇文章，我们了解了词法文法、语法文法，以及用于定义语法文法的简写形式。作为例子，我们研究了<code>await</code>在异步函数中被禁止用作标识符，但在非异步函数中则允许。</p>
<p>下一篇文章将介绍词法文法其他有意思的部分，比如自动插入分号（ASI）和包含文法（cover grammar）。</p></div>  
</div>
            