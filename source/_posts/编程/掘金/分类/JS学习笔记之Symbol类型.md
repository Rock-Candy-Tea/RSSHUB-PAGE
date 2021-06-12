
---
title: 'JS学习笔记之Symbol类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4de3886e88534a28bb547b3683e2e2bd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 02:50:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4de3886e88534a28bb547b3683e2e2bd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、Symbol概述</h3>
<p><strong>ES5 的对象属性名都是字符串，这容易造成属性名的冲突</strong>。比如，你使用了一个他人提供的对象，但又想为这个对象添加新的方法，新方法的名字就有可能与现有方法产生冲突。如果有一种机制，<code>保证每个属性的名字都是独一无二的</code>就好了，这样就从根本上防止属性名的冲突。这就是 ES6 引入Symbol的原因。</p>
<p>ES6 引入了一种新的<code>原始数据类型Symbol</code>，表示独一无二的值。它是 JavaScript 语言的第七种数据类型，前六种是：undefined、null、布尔值（Boolean）、字符串（String）、数值（Number）、对象（Object）。</p>
<p>Symbol 值通过<code>Symbol函数</code>生成。这就是说，对象的属性名现在可以有两种类型，一种是原来就有的字符串，另一种就是新增的 Symbol 类型。凡是属性名属于 Symbol 类型，就<code>都是独一无二的，可以保证不会与其他属性名产生冲突。</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Sym = <span class="hljs-built_in">Symbol</span>();

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> Sym)
<span class="hljs-comment">// symbol</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>变量s</code>就是一个独一无二的值。typeof运算符的结果，<code>表明变量s是 Symbol 数据类型</code>，而不是字符串之类的其他类型。</p>
<blockquote>
<p>注意，Symbol函数前不能使用new命令，否则会报错。这是因为生成的 Symbol 是一个原始类型的值，不是对象。也就是说，由于 Symbol 值不是对象，所以不能添加属性。基本上，它是一种类似于字符串的数据类型。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Sym = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Symbol</span>();

<span class="hljs-built_in">console</span>.log(Sym)
<span class="hljs-comment">//Uncaught TypeError: Symbol is not a constructor</span>
<span class="hljs-comment">//at new Symbol (<anonymous>)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Symbol函数可以接受一个字符串作为参数，表示对 Symbol 实例的描述，注意这个字符串仅仅表示描述而已，有了描述，输出的时候就能够分清，到底是哪一个值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> s1 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>);
<span class="hljs-keyword">let</span> s2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'bar'</span>);

s1 <span class="hljs-comment">// Symbol(foo)</span>
s2 <span class="hljs-comment">// Symbol(bar)</span>

s1.toString() <span class="hljs-comment">// "Symbol(foo)"</span>
s2.toString() <span class="hljs-comment">// "Symbol(bar)"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>因此相同参数的Symbol函数的返回值是不相等的。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> s1 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>);
<span class="hljs-keyword">let</span> s2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>);

<span class="hljs-built_in">console</span>.log(s1 === s2)
<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Symbol 值不能与其他类型的值进行运算，会报错。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sym = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'My symbol'</span>);

<span class="hljs-string">"your symbol is "</span> + sym
<span class="hljs-comment">// TypeError: can't convert symbol to string</span>
<span class="hljs-string">`your symbol is <span class="hljs-subst">$&#123;sym&#125;</span>`</span>
<span class="hljs-comment">// TypeError: can't convert symbol to string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，Symbol 值可以显式转为字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sym = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'My symbol'</span>);

<span class="hljs-built_in">String</span>(sym) <span class="hljs-comment">// 'Symbol(My symbol)'</span>
sym.toString() <span class="hljs-comment">// 'Symbol(My symbol)'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，Symbol 值也可以转为布尔值，但是不能转为数值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sym = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-built_in">Boolean</span>(sym) <span class="hljs-comment">// true</span>
!sym  <span class="hljs-comment">// false</span>

<span class="hljs-keyword">if</span> (sym) &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-built_in">Number</span>(sym) <span class="hljs-comment">// TypeError</span>
sym + <span class="hljs-number">2</span> <span class="hljs-comment">// TypeError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">二、Symbol作为属性名</h3>
<p>由于每一个 Symbol 值都是不相等的，这意味着 <code>Symbol 值可以作为标识符，用于对象的属性名</code>，就能保证不会出现同名的属性。这对于一个对象由多个模块构成的情况非常有用，能防止某一个键被不小心改写或覆盖。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> mySymbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"mySymbol"</span>);
<span class="hljs-keyword">let</span> a = &#123;
<span class="hljs-attr">mySymbol</span>:<span class="hljs-string">"name"</span>
&#125;;
a[mySymbol] = <span class="hljs-string">'Hello!'</span>;

<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4de3886e88534a28bb547b3683e2e2bd~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-06-12_16-17-55.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意，Symbol 值作为对象属性名时，不能用点运算符。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mySymbol = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">const</span> a = &#123;&#125;;
a.mySymbol = <span class="hljs-string">'Hello!'</span>;
a[mySymbol] <span class="hljs-comment">// undefined</span>
a[<span class="hljs-string">'mySymbol'</span>] <span class="hljs-comment">// "Hello!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，因为点运算符后面总是字符串，所以不会读取mySymbol作为标识名所指代的那个值，导致a的属性名实际上是一个字符串，而不是一个 Symbol 值。</p>
<p>同理，在对象的内部，使用 Symbol 值定义属性时，<code>Symbol 值必须放在方括号之中</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> s = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">let</span> obj = &#123;
  [s]: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">arg</span>) </span>&#123; ... &#125;
&#125;;

obj[s](<span class="hljs-number">123</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，如果s不放在方括号中，该属性的键名就是字符串s，而不是s所代表的那个 Symbol 值。</p>
<p><strong>---来自网道项目</strong></p></div>  
</div>
            