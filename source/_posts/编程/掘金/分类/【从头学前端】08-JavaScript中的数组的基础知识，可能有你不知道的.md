
---
title: '【从头学前端】08-JavaScript中的数组的基础知识，可能有你不知道的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18741ea3940040bfa6d485c4db0fd3e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 07:35:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18741ea3940040bfa6d485c4db0fd3e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>Hello 大家好，我是<a href="https://juejin.cn/user/3350967174838701/posts" target="_blank" title="https://juejin.cn/user/3350967174838701/posts">彼岸繁華🌸</a>，一个坚信努力可以改变命运的前端👨🏻‍💻，如果有幸写的文章可以得到你的青睐，万分有幸~</p>
</blockquote>
<blockquote>
<p>本系列文章在掘金首发，编写不易转载请获得允许</p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>本篇文章将来学习JavaScript中的数组。通过本篇文章的学习可以掌握什么知识呢？如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18741ea3940040bfa6d485c4db0fd3e1~tplv-k3u1fbpfcp-watermark.image" alt="导读.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一些概念</h2>
<h3 data-id="heading-2">什么是数组</h3>
<p>JavaScript中的<strong>数组（Array）</strong> 是一个有序是数据集合，可以通过数组索引（<code>index</code>）访问数组中的数据内容。数组中的每一项可以存储任何类型的数据，也就是说，一个数组中可以存储不同类型的数据。</p>
<p>注：JavaScript中的数组对象并不能称为真正意义上的数组，而是通过对象的<code>key</code>和<code>value</code>键值对来模拟的数组。</p>
<p>下面代码定义了JavaScript中的数组：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在JavaScript中，并没有明确数组这种类型，但是提供了 <code>Array</code>对象。换句话讲，JavaScript操作数组主要是通过<code>Array</code>对象提供的属性和方法来完成。</p>
<blockquote>
<p>说明：关于<code>Array</code>的知识，将在引用类型部分讲解。</p>
</blockquote>
<p>JavaScript中的数组是允许动态调整的，也就是说，可以动态地向数组增加新的数据，也可以动态地从该数组中删除某个具体的数据。当然，还包括很多更为复杂的操作。</p>
<p>再有就是，数组中存储的每一个数据内容所在的位置都是唯一的。这样，我们就可以通过数据所在的位置很方便地访问到该数据内容。</p>
<h3 data-id="heading-3">数组的长度</h3>
<p>JavaScript语言提供了<code>Array</code>对象，该对象提供了一个<code>length</code>属性，该属性可以用来表示数组的长度。所谓的数组长度，简单来说，就是数组可以存储多少数据内容。</p>
<blockquote>
<p>说明：关于对象和属性的知识，将在对象那篇文章中进行讲解</p>
</blockquote>
<p>示例代码如下：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]

<span class="hljs-built_in">console</span>.log(arr.length) <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码的结果所示，我们可以看到<code>arr</code>数组中存储了3个数据内容，而<code>arr</code>数组的<code>length</code>属性值也为3。说明索引数组的长度是等于存储数据的个数的。</p>
<h2 data-id="heading-4">创建数组</h2>
<p>JavaScript中创建数组的方式具有如下3种方式：</p>
<ul>
<li>
<p>字面量方式创建数组</p>
</li>
<li>
<p><code>Array()</code>函数创建数组</p>
</li>
<li>
<p>构造函数方式创建数组</p>
</li>
</ul>
<h3 data-id="heading-5">字面量方式创建数组</h3>
<p>使用字面量方式创建数组是JavaScript标准规范汇总定义数组的结构来创建数组。其语法结构如下：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">[元素<span class="hljs-number">1</span>, 元素<span class="hljs-number">2</span>, 元素<span class="hljs-number">3</span>, 元素N]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种使用方括号（<code>[]</code>）的形式被称为字面量方式或者直接量方式。这种方式创建数组比其他方式创建数组更为便捷，通常是创建数组的首选。</p>
<p>如果使用这种方式创建数组时，没有声明任何一个数组元素的话，则称为空数组。所谓空数组就是指数组中不包含任何数据内容。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是，虽然这种方式与之前的原始类型的变量声明很像，但由于JavaScript中只提供了Array对象，而没有为数组提供任何数据类型。所以，数组的数据类型为Object，如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> arr) <span class="hljs-comment">// object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上图的结果所示，我们会发现<code>typeof arr</code>最终的结果为<code>object</code>。这是因为在<code>JavaScript</code>中<code>Object</code>是所有对象的父级，在<code>JavaScript</code>中并没有提供<code>array</code>这一类型，而是提供了Array对象。</p>
<p>我们也可以通过<code>instanceof</code>运算符再次判断，如下示例代码：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-built_in">console</span>.log(arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>说明：关于<code>instanceof</code>运算符将会在后面学习</p>
</blockquote>
<h3 data-id="heading-6">Array()函数方式创建数组</h3>
<p>JavaScript提供了<code>Array()</code>函数可以用来创建数组，其语法结构如下所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">Array</span>(元素<span class="hljs-number">1</span>, 元素<span class="hljs-number">2</span>, 元素<span class="hljs-number">3</span>, 元素N)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下示例代码展示了通过<code>Array()</code>函数来创建数组：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>(<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>)
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [ '这是一个测试内容.', 100, true ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是，<code>Array()</code>函数这种方式创建数组，如果传递的参数只有一个并且是数字值时，则表示创建了一个该数字值长度的空数组。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 稀疏数组</span>
<span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>(<span class="hljs-number">10</span>)
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [ <10 empty items> ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面创建的这种数组称为<strong>稀疏数组</strong> 。</p>
<h3 data-id="heading-7">构造函数方式创建数组</h3>
<p>JavaScript中提供了<code>Array</code>对象，实际上数组是通过该对象提供的属性和方法来进行操作的，例如 <code>length</code>属性等。不仅如此，我们也可以通过创建对象的方式来创建数组，称为构造函数方式创建数组。其语法结构如下所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(元素<span class="hljs-number">1</span>, 元素<span class="hljs-number">2</span>, 元素<span class="hljs-number">3</span>, 元素N)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是，构造函数方式与<code>Array()</code>函数方式在语法结构上仅相差一个<code>new</code>，但意义上完全不一样。因为使用<code>new</code>关键字是表示在<code>JavaScript</code>语言中创建一个对象。所以，这种方式表示创建了一个数组对象。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>)
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [ '这是一个测试内容.', 100, true ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与<code>Array()</code>函数方式类似，如果构造函数中的参数只有一个并且是数字值的话，则表示创建了一个该数字值长度的空数组。</p>
<h2 data-id="heading-8">数组操作</h2>
<p>JavaScript中的数组的作用与变量类似，都是用来存储数据内容的。区别在于变量每次只能存储一个数据内容，更新后会覆盖之前存储的数据内容；而数组一次允许存储多个数据内容，并且数据的类型没有任何要求。</p>
<p>所以，除了创建数组之外，数组的操作还有如下几种：</p>
<ul>
<li>
<p>访问数组中的数据</p>
</li>
<li>
<p>修改数组中的数据</p>
</li>
<li>
<p>删除数组中的数据</p>
</li>
</ul>
<h3 data-id="heading-9">访问数组中的数据</h3>
<p>使用数组存储了数据内容之后，我们还需要通过该数组访问其中存储的具体数据内容。具体的访问方式，就是通过数组的索引值来访问数组中某个位置上所存储的数据内容。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-built_in">console</span>.log(arr[<span class="hljs-number">0</span>]) <span class="hljs-comment">// 这是一个测试内容.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">修改数组中的数据</h3>
<p>修改数组中的数据与访问数据中的数据类似，都是通过索引值找到数组中对应位置上的数据。区别在于访问只是将数据内容读取出来，而修改则要使用新的数据内容来覆盖旧的数据内容。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
arr[<span class="hljs-number">0</span>] = <span class="hljs-string">'这是另一个测试内容.'</span>

<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [ '这是另一个测试内容.', 100, true ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上图的结果所示，我们可以看到<code>arr</code>数组0这个位置的数据内容已经被更新。</p>
<h3 data-id="heading-11">删除数组中的数据</h3>
<p>删除数组中的数据就是通过数组中具体的索引值来删除该位置上存储的数据内容，删除操作需要使用<code>delete</code>运算符来完成。如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-keyword">delete</span> arr[<span class="hljs-number">0</span>] <span class="hljs-comment">// [ <1 empty item>, 100, true ]</span>

<span class="hljs-built_in">console</span>.log(arr)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'arr数组的长度为：'</span> + arr.length) <span class="hljs-comment">// arr数组的长度为：3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上图的结果所示，值得注意的是，当通过<code>delete</code>运算符删除数组中指定索引值的位置上的数据内容时，该数组的长度不变，只是将指定位置上的数据内容删除而已。</p>
<h2 data-id="heading-12">遍历数组</h2>
<p>由于数组中可以存储多个数据内容，有时我们需要将数组中每一个数据内容全部读取出来，这就需要通过遍历数组来完成。遍历数组的操作可以通过任意一种循环语句来实现，如下示例代码所示：</p>
<p><code>while</code>语句</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">while</span> (i < arr.length) &#123;
  <span class="hljs-built_in">console</span>.log(arr[i])
  i++
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>do...while</code>语句</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">do</span> &#123;
  <span class="hljs-built_in">console</span>.log(arr[i])
  i++
&#125;
<span class="hljs-keyword">while</span> (i < arr.length) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>for</code>语句</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
  <span class="hljs-built_in">console</span>.log(arr[i])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13"><code>for...in</code>语句</h3>
<p><code>for...in</code>语句通过一个变量来循环一个对象中的可枚举属性。语法结构如下：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> 变量 <span class="hljs-keyword">in</span> 可遍历的对象) &#123;
    语句块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>关于对象、可枚举属性将会在后面学习，这里只需要记住<code>for...in</code>语句，循环语句的变量的是每一项值</p>
</blockquote>
<p>如下示例代码所示：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'这是一个测试内容.'</span>, <span class="hljs-number">100</span>, <span class="hljs-literal">true</span>]
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> arr) &#123;
  <span class="hljs-built_in">console</span>.log(arr[i])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在ECMAScript新特性中又增加了许多对数组遍历的方法，例如<code>for...of</code>语句、<code>forEach</code>方法等。</p>
</blockquote>
<h2 data-id="heading-14">总结</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b75b11d31a2e48018d3e23c18d43ac38~tplv-k3u1fbpfcp-watermark.image" alt="总结.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>预告</strong>：下一篇文章我们将来学习JavaScript中的函数</p>
<h2 data-id="heading-15">精彩文章</h2>
<p><a href="https://juejin.cn/post/6994404257281605645" target="_blank" title="https://juejin.cn/post/6994404257281605645">【从头学前端】07-掌握JavaScript中的循环语句</a></p>
<p><a href="https://juejin.cn/post/6994011908563009567/" target="_blank" title="https://juejin.cn/post/6994011908563009567/">【从头学前端】06-这次我学会了JavaScript中的条件语句</a></p>
<p><a href="https://juejin.cn/post/6993711769281626119" target="_blank" title="https://juejin.cn/post/6993711769281626119">【从头学前端】05-详解JavaScript中的35种运算符</a></p>
<p><a href="https://juejin.cn/post/6992560962737799204" target="_blank" title="https://juejin.cn/post/6992560962737799204">【从头学前端】04-搞懂JavaScript中的基本数据类型</a></p>
<p><a href="https://juejin.cn/post/6992208659551879176" target="_blank" title="https://juejin.cn/post/6992208659551879176">【从头学前端】03-这次我就搞懂了JavaScript中的变量</a></p></div>  
</div>
            