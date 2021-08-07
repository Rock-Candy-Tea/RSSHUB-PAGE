
---
title: 'Tagged Template Literals _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1633'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 08:34:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=1633'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>之前的文章中提到，htm 使用了 JavaScript 的 tagged template literals 特性。Template literal 和 tagged template literals 是 ES2015 引入的两种新 literals。它们看上去非常相似，但是实际上却非常不同。我们使用的更多的是 template literals，是支持插值的、允许多行的 string literals。而相比之下，比较低调的 tagged template literals 却是函数调用。</p>
<p>我相信大多数都已经对 template literals 很熟悉了，因此接下来我们主要来聊聊 tagged template。tagged template 虽然出场不多，但是熟悉 CSS-in-JS 的同学应该对它不陌生。styled-components 作为影响力比较大的 CSS-in-JS 库使用的就是 tagged template 语法。以下是一个 tagged template 的例子：</p>
<pre><code class="hljs language-js copyable" lang="js">tagFunction<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;firstName&#125;</span> <span class="hljs-subst">$&#123;lastName&#125;</span>!`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它看上去就是在 template string 前面加了一个函数。这实际上就触发了一次函数调用。上面的代码可以看作为这样的一次调用：</p>
<pre><code class="hljs language-js copyable" lang="js">tagFunction([<span class="hljs-string">"Hello"</span>, <span class="hljs-string">" "</span>, <span class="hljs-string">"!"</span>], firstName, lastName);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>置于 template string 之前的被调用的函数被称为 tag function。这个函数接受的参数可以分成两部分：template strings 和 substitutions。我们来一个具体的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tagFunction</span>(<span class="hljs-params">tempObj, ...subs</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(tempObj, subs);
&#125;

<span class="hljs-keyword">const</span> name = <span class="hljs-string">"World"</span>;

tagFunction<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;name&#125;</span>!`</span>;
<span class="hljs-comment">// 输出： [ 'Hello ', '!' ] [ 'World' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然第一个参数看上去是一个普通的数组，但是它还有一个保存 raw 版本 template string 的 <code>raw</code> 属性。那么 raw 版本有什么不同之处呢？其实，它们在大多数情况下都是一样的，只在对于 escape 字符 <code>\</code> 的处理上有区别：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tagFunction</span>(<span class="hljs-params">tempObj, ...subs</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(tempObj);
  <span class="hljs-built_in">console</span>.log(tempObj.raw);
&#125;

tagFunction<span class="hljs-string">`Hello\$&#123;`</span>;
tagFunction<span class="hljs-string">`Hello\``</span>;
tagFunction<span class="hljs-string">`Hello\n`</span>;

<span class="hljs-comment">// 输出依次为</span>
<span class="hljs-comment">// [ 'Hello$&#123;' ]</span>
<span class="hljs-comment">// [ 'Hello\\$&#123;' ]</span>
<span class="hljs-comment">// [ 'Hello`' ]</span>
<span class="hljs-comment">// [ 'Hello\\`' ]</span>
<span class="hljs-comment">// [ 'Hello\n' ]</span>
<span class="hljs-comment">// [ 'Hello\\n' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 “cooked” 版本中，<code>\</code> 的作用有：</p>
<ol>
<li>防止了<code>$&#123;</code>被解析成 substitution 的开始</li>
<li>将 <code>`</code> 转义成为普通的字符</li>
<li>和 <code>\</code> 在 string literals 中一样，将 <code>n</code> 、 <code>x</code> 等字符转义成特殊字符</li>
</ol>
<p>而在 raw 版本中，<code>\</code> 同样具有前两个功能。但是很特别的是即使在这种发挥出转义作用的 <code>\</code> 在 raw 版本还是得到了保留。而其他情况下的 <code>\</code> 都被替换成了 <code>\\</code>。也就是说，所有的 <code>\</code> 都被转义成了普通的反斜杠。</p>
<p>tagged templates 非常适合用来写 DSL。之前提到的 styled-components 和 htm（lit-html）都可以看作是在 JavaScript 中实现的一种 DSL。那接下来我们也来尝试实现一个 DSL。</p>
<p>markdown 是一种轻量的标记语言，为人们提供使用纯文本格式编写文档的能力。因为其语法的简单易用，markdown 几乎成为了文字编辑软件的标配。比如，这篇文字就是使用 markdown 写成的。那我们就来试试在 JavaScript 中嵌入 markdown。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> markdownIt <span class="hljs-keyword">from</span> <span class="hljs-string">"markdown-it"</span>;

<span class="hljs-keyword">const</span> md = <span class="hljs-keyword">new</span> markdownIt();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mark</span>(<span class="hljs-params">template, ...substitutions</span>) </span>&#123;
  <span class="hljs-keyword">const</span> raw = template.raw;

  <span class="hljs-keyword">let</span> result = <span class="hljs-string">""</span>;

  substitutions.forEach(<span class="hljs-function">(<span class="hljs-params">substitution, idx</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> t = raw[idx];

    result += t;
    result += <span class="hljs-built_in">String</span>(substitution);
  &#125;);
  result += template[template.length - <span class="hljs-number">1</span>];
  <span class="hljs-keyword">const</span> html = md.render(result);

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">String</span>(html);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码，实现了一个简单的 tag function <code>mark</code>。 它的作用很简单就是将传入的 substitutions 转为字符串然后和 template strings 拼接称为完整的 markdown 字符串。然后，使用 markdown-it 将该字符串转成 html 字符串。来看它是如何使用的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"Gary"</span>;
<span class="hljs-keyword">const</span> html = mark<span class="hljs-string">`Hello *<span class="hljs-subst">$&#123;name&#125;</span>*`</span>; <span class="hljs-comment">// "<p>Hello <em>Gary</em></p>\n"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可能有人会产生质疑，这和下面的代码有什么区别吗：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> markdownIt <span class="hljs-keyword">from</span> <span class="hljs-string">"markdown-it"</span>;

<span class="hljs-keyword">const</span> md = <span class="hljs-keyword">new</span> markdownIt();

<span class="hljs-keyword">const</span> name = <span class="hljs-string">"Gary"</span>;
md.render(<span class="hljs-string">`Hello *<span class="hljs-subst">$&#123;name&#125;</span>*`</span>); <span class="hljs-comment">// "<p>Hello <em>Gary</em></p>\n"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于这个例子来说，两个版本的代码输出确实是一致的。但是它们在本质上还是有区别的。之前提到了，template literals 就是一种产生字符串的语法结构，作用和 string literals 类似。而 tagged templates 是触发了一次函数调用。也就是说，<code>md.render</code>接收的是一个字符串，而 <code>mark</code> 接收的是 template strings 和 substitutions。这也就意味着，<code>mark</code>有能力对传入的 substitutions 做各种转换和处理，而 <code>md.render</code> 是做不到这一点的。比如说，<code>mark</code>可以针对数组类型的 substitutions 做特殊的处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(substitution)) &#123;
  substitution = substitution.join(<span class="hljs-string">" "</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> names = [<span class="hljs-string">"Gary"</span>, <span class="hljs-string">"Tomas"</span>];

mark<span class="hljs-string">`Hello *<span class="hljs-subst">$&#123;names&#125;</span>*`</span>; <span class="hljs-comment">// "<p>Hello <em>Gary Tomas</em></p>\n"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 <code>md.render</code> 版本则返回 <code><p>Hello <em>Gary,Tomas</em></p>\n</code>。这是由于 <code>names</code> 在被拼接之前先被转成了字符串。tagged template 版本的 <code>mark</code> 还有另外一个优点。注意到我们在取 template strings 时取的是 raw 版本。这会导致以下的差异：</p>
<pre><code class="hljs language-js copyable" lang="js">mark<span class="hljs-string">`\# Hello *World*`</span>; <span class="hljs-comment">// "<p># Hello <em>World</em></p>\n"</span>

md.render(<span class="hljs-string">`\# Hello *World*`</span>); <span class="hljs-comment">// "<h1>Hello <em>World</em></h1>\n"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：<code>\</code> 在 markdown 中也有转义的作用。</p>
<p>在 <code>mark</code> 版本中，转义字符正确的起作用，防止了 <code>#</code> 被当成 Heading 的起始字符。而在 <code>md.render</code> 中，<code>\</code> 却没有起作用。这是因为 <code>\</code> 在 template literals 中也担任转义字符的作用。而对于 template literals， <code>\#</code> 就是 <code>#</code>。所以 <code>md.render</code> 拿到的字符串实际上就是<code># Hello *World*</code>。要让 <code>\</code> 正确的在 markdown 语法中起效，我们需要对 <code>\</code> 进行转义，也就是传入 <code>\\# Hello *World*</code>。这样，<code>md.render</code> 的返回值就和 <code>mark</code> 版本一样了。这就像必须使用 <code>new RegExp("\\\\")</code> 才能匹配包含 <code>\</code> 的字符串。</p></div>  
</div>
            