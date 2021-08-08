
---
title: 'DOM扩展 —— HTML5 的 CSS 类扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7952'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 07:54:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=7952'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>自 <code>HTML4</code> 被广泛采用以来，<code>Web</code> 开发中一个主要的变化是 <code>class</code> 属性用得越来越多，其用处是为元素添加样式以及语义信息。为了适应开发者和他们对 <code>class</code> 属性的认可，<code>HTML5</code> 增加了一些特性以方便使用 <code>CSS</code> 类。</p>
</blockquote>
<h2 data-id="heading-0">1. getElementsByClassName()</h2>
<p><code>getElementsByClassName()</code> 是 <code>HTML5</code> 新增的最受欢迎的一个方法，暴露在 <code>document</code> 对象和所有 <code>HTML</code> 元素上。这个方法脱胎于基于原有 <code>DOM</code> 特性实现该功能的 <code>JavaScript</code> 库，提供了性能高好的原生实现。</p>
<p><code>getElementsByClassName()</code> 方法接收一个参数，即包含一个或多个类名的字符串，返回类名中包含相应类的元素的 <code>NodeList</code>。如果提供了多个类名，则顺序无关紧要。下面是几个示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 取得所有类名中包含"username"和"current"元素</span>
<span class="hljs-comment">// 这两个类名的顺序无关紧要</span>
<span class="hljs-keyword">let</span> allCurrentUsernames = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">"username current"</span>);
<span class="hljs-comment">// 取得 ID 为"myDiv"的元素子树中所有包含"selected"类的元素</span>
<span class="hljs-keyword">let</span> selected = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myDiv"</span>).getElementsByClassName(<span class="hljs-string">"selected"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要给包含特定类（而不是特定 <code>ID</code> 或标签）的元素添加事件处理程序，使用这个方法会很方便。不过要记住，因为返回值是 <code>NodeList</code>，所以使用这个方法会遇到跟使用 <code>getElementsByTagName()</code> 和其他返回 <code>NodeList</code> 对象的 <code>DOM</code> 方法同样的问题。</p>
<h2 data-id="heading-1">2. classList 属性</h2>
<p>要操作类名，可以通过 <code>className</code> 属性实现添加、删除和替换。但 <code>className</code> 是一个字符串，所以每次操作之后都需要重新设置这个值才能生效，即使只改动了部分字符串也一样。以下面的 <code>HTML</code> 代码为例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bd user disabled"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 <code><div></code> 元素有 <code>3</code> 个类名。要想删除其中一个，就得先把 <code>className</code> 拆开，删除不想要的那个，再把包含剩余类的字符串设置回去。比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 要删除"user"类</span>
<span class="hljs-keyword">let</span> targetClass = <span class="hljs-string">"user"</span>;
<span class="hljs-comment">// 把类名拆成数组</span>
<span class="hljs-keyword">let</span> classNames = div.className.split(<span class="hljs-regexp">/\s+/</span>);
<span class="hljs-comment">// 找到要删除类名的索引</span>
<span class="hljs-keyword">let</span> idx = classNames.indexOf(targetClass);
<span class="hljs-comment">// 如果有则删除</span>
<span class="hljs-keyword">if</span> (idx > -<span class="hljs-number">1</span>) &#123;
 classNames.splice(i,<span class="hljs-number">1</span>);
&#125;
<span class="hljs-comment">// 重新设置类名</span>
div.className = classNames.join(<span class="hljs-string">" "</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>HTML5</code> 通过给所有元素增加 <code>classList</code> 属性为这些操作提供了更简单也更安全的实现方式。<code>classList</code> 是一个新的集合类型 <code>DOMTokenList</code> 的实例。与其他 DOM 集合类型一样，<code>DOMTokenList</code> 也有 <code>length</code> 属性表示自己包含多少项，也可以通过 <code>item()</code> 或中括号取得个别的元素。此外，<code>DOMTokenList</code> 还增加了以下方法。</p>
<ul>
<li><code>add(value)</code>，向类名列表中添加指定的字符串值 <code>value</code>。如果这个值已经存在，则什么也不做。</li>
<li><code>contains(value)</code>，返回布尔值，表示给定的 <code>value</code> 是否存在。</li>
<li><code>remove(value)</code>，从类名列表中删除指定的字符串值 <code>value</code>。</li>
<li><code>toggle(value)</code>，如果类名列表中已经存在指定的 <code>value</code>，则删除；如果不存在，则添加。</li>
<li><code>replace(old, new)</code>，如果类名列表中已经存在指定的 <code>old</code>，则替换成 <code>new</code>；如果不存在，则什么也不做。</li>
</ul>
<p>这样以来，前面的例子中那么多行代码就可以简化成下面的一行：</p>
<pre><code class="hljs language-js copyable" lang="js">div.classList.remove(<span class="hljs-string">"user"</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行代码可以在不影响其他类名的情况下完成删除。其他方法同样极大地简化了操作类名的复杂性，如下面的例子所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除"disabled"类</span>
div.classList.remove(<span class="hljs-string">"disabled"</span>);
<span class="hljs-comment">// 添加"current"类</span>
div.classList.add(<span class="hljs-string">"current"</span>);
<span class="hljs-comment">// 切换"user"类</span>
div.classList.toggle(<span class="hljs-string">"user"</span>);
<span class="hljs-comment">// 检测类名</span>
<span class="hljs-keyword">if</span> (div.classList.contains(<span class="hljs-string">"bd"</span>) && !div.classList.contains(<span class="hljs-string">"disabled"</span>))&#123;
 <span class="hljs-comment">// 执行操作</span>
)
<span class="hljs-comment">// 迭代类名</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">of</span> <span class="hljs-title">div</span>.<span class="hljs-title">classList</span>)</span>&#123;
 doStuff(<span class="hljs-class"><span class="hljs-keyword">class</span>)</span>;
&#125;
<span class="hljs-comment">// 将类值 "foo" 替换成 "bar"</span>
div.classList.replace(<span class="hljs-string">"foo"</span>, <span class="hljs-string">"bar"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加了 <code>classList</code> 属性之后，除非是完全删除或完全重写元素的 <code>class</code> 属性，否则 <code>className</code>属性就用不到了。</p>
<h2 data-id="heading-2">引用</h2>
<ul>
<li>[1] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F35175321%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/35175321/" ref="nofollow noopener noreferrer">JavaScript高级程序设计（第4版）</a></li>
<li>[2] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org" ref="nofollow noopener noreferrer">MDN Web Docs</a></li>
</ul></div>  
</div>
            