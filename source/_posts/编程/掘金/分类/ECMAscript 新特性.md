
---
title: 'ECMAscript 新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb12610543e24f3f938627d269f201d8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 01:33:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb12610543e24f3f938627d269f201d8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">ECMAscript 新特性</h1>
<h2 data-id="heading-1">一概述</h2>
<h3 data-id="heading-2">1.了解的意义</h3>
<ul>
<li>语言与平台之间的关系</li>
<li>系统化学习 ECMAscript 高级进阶的需要</li>
<li>现代化、高质量的代码的需要</li>
</ul>
<h3 data-id="heading-3">2.基本概念</h3>
<ul>
<li>简写为 ES , 也是一门脚本语言, 通常看作 javascript 的标准化规范</li>
<li>javascript 实际是 ECMAscript 的扩展语言, ECMAscript 只提供了最基本的语法, 并不能完成实际功能开发</li>
<li>javascript 实现了 ECMAscript 标准, 并做了扩展, 在浏览器能够操作 dom、bom , 在node 环境中读写文件</li>
<li>javascript 语言本身即 ECMAscript</li>
</ul>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb12610543e24f3f938627d269f201d8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd5a097de0a4054b9ce8a084e8f2168~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>2015年开始, ES 保持每年一个版本的迭代, ES 新特性陆续出现, 使 javascript 越来越高级、便捷.
ES2015 在 ES5 发布后经过六年才完全标准化, 包含了许多颠覆式的新功能, 需要我们深入学习.
从 ES2015 后, ES 不再使用 版本号命名, 而使用年份, 如 ES2016、 ES2017. 在 ES5 之后发布的 ES2015 也称为 ES6.</p>
<h3 data-id="heading-4">3.ES6</h3>
<p>ES2015, 也称 ES6, 新时代 ECMAscript 的代表版本: 相比较于 ES5.1 变化较大 ; 自此, 命名标准也发生了变化
很多开发者用 ES6 泛指 ES5.1 之后的所有新标准, 如 ES6 新规范 async/await 属于 ES2017 的新规范</p>
<p>文档地址: <a href="https://262.ecma-international.org/6.0/" target="_blank" rel="nofollow noopener noreferrer">262.ecma-international.org/6.0/</a></p>
<p><strong>主要变化:</strong></p>
<ul>
<li>解决原有语法的问题和不足, 如 let、 cont 提供的块级作用域</li>
<li>对原有语法进行增强, 使语言便捷、易用. 如解构、展开、参数默认值、模版字符串</li>
<li>全新的对象、全新的功能、全新的方法,如: Promise、Proxy、Object的方法等</li>
<li>全新的数据结构, 如 set、map、symbol等</li>
</ul>
<p><strong>运行环境</strong></p>
<ul>
<li>chrome 浏览器</li>
<li>nodeJs, -v 12.13.0,</li>
<li>nodemon 工具, 修改完成自动执行代码,</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 安装</span>
npm i nodemon
<span class="hljs-comment">// 使用:</span>
nodemon index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">二语法介绍</h2>
<h3 data-id="heading-6">1.变量声明</h3>
<h4 data-id="heading-7">let 与块级作用域</h4>
<p>作用域: 代码中某成员起作用的范围.
在 ES2015 之前, 只有函数作用域和函数作用域, ES2015 中新增了块级作用域, 块指的是用 &#123;&#125; 包裹起来的范围.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-keyword">var</span> foo = <span class="hljs-literal">true</span>;
&#125;
<span class="hljs-built_in">console</span>.log(foo) <span class="hljs-comment">// true</span>
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-keyword">let</span> foo = <span class="hljs-literal">true</span>;
&#125;
<span class="hljs-built_in">console</span>.log(foo) <span class="hljs-comment">// foo is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环嵌套案例中的问题:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">3</span>; i++)&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">3</span>; i++)&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"循环结束之后的i:"</span> , i)
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 循环结束之后的i: 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码,在内层循环完毕之后, 内部的变量 i 已经改变, 并且将外部的变量覆盖, 使用块级作用域:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">3</span>; i++)&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">3</span>; i++)&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"循环结束之后的i:"</span> , i)
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 循环结束之后的i: 0</span>
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 循环结束之后的i: 1</span>
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 循环结束之后的i: 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环注册事件时候, 访问计数器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> elements = [&#123;&#125;, &#123;&#125;, &#123;&#125;]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<elements.length; i++)&#123;
    elements[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;
&#125;
<span class="hljs-comment">// 闭包解决</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<elements.length; i++)&#123;
    elements[i].onclick = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(i)
        &#125;  
    &#125;)(i)
&#125;
<span class="hljs-comment">// 块级作用域解决</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<elements.length; i++)&#123;
    elements[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>关于 for 循环的两层作用域:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">3</span>; i++)&#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-string">'foo'</span>
    <span class="hljs-built_in">console</span>.log(i)
&#125;
<span class="hljs-comment">// foo</span>
<span class="hljs-comment">// foo</span>
<span class="hljs-comment">// foo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到内部定义的 i 变量并没有受到循环 i 变量的影响, 为了便于理解, 我们可以将代码进行拆解:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">if</span>(i<<span class="hljs-number">3</span>)&#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-string">'foo'</span>
    <span class="hljs-built_in">console</span>.log(i)
&#125;
i++
<span class="hljs-keyword">if</span>(i<<span class="hljs-number">3</span>)&#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-string">'foo'</span>
    <span class="hljs-built_in">console</span>.log(i)
&#125;
i++
<span class="hljs-keyword">if</span>(i<<span class="hljs-number">3</span>)&#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-string">'foo'</span>
    <span class="hljs-built_in">console</span>.log(i)
&#125;
i++
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>for 循环内部是两级嵌套的作用域, 循环体内部 与 循环内部是两个独立的作用域</strong>
<strong>let 声明不会变量提升</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(a);
<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
<span class="hljs-comment">// undefined</span>
<span class="hljs-comment">// Cannot access 'b' before initialization</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">const</h4>
<p>const : 声明一个只读的衡量,常量, 声明之后不可修改.
<strong>声明之后必须赋值</strong>
<strong>不可修改是指声明之后不可修改内存地址, 并不是不可以修改内部属性</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">12</span>
<span class="hljs-built_in">console</span>.log(a)
a = <span class="hljs-number">11</span>
<span class="hljs-comment">//Assignment to constant variable. </span>

<span class="hljs-keyword">const</span> obj = &#123;&#125;
<span class="hljs-built_in">console</span>.log(obj)
obj.a = <span class="hljs-number">12</span>
<span class="hljs-built_in">console</span>.log(obj)
<span class="hljs-comment">// &#123;&#125;</span>
<span class="hljs-comment">// &#123; a: 12 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>最佳实践:不用 var(避免先使用再声明等开发陋习), 主用 const (更明确开发成员是否会修改), 配合 let</strong></p>
<h3 data-id="heading-9">2.解构</h3>
<p>Destructuring, 从数组或者对象中获取指定元素的快捷方式.</p>
<h4 data-id="heading-10">数组解构</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>, <span class="hljs-number">700</span>, <span class="hljs-number">1000</span>]
<span class="hljs-comment">// 原始写法</span>
<span class="hljs-keyword">const</span> arr1 = arr[<span class="hljs-number">0</span>]
<span class="hljs-keyword">const</span> arr2 = arr[<span class="hljs-number">1</span>]
<span class="hljs-keyword">const</span> arr3 = arr[<span class="hljs-number">2</span>]
<span class="hljs-comment">// 新写法</span>
<span class="hljs-keyword">const</span> [arr1, arr2, arr3] = arr
<span class="hljs-built_in">console</span>.log(arr1, arr2, arr3)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过解构获取指定位置成员</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>, <span class="hljs-number">700</span>, <span class="hljs-number">1000</span>]
<span class="hljs-keyword">const</span> [ , , , arr4] = arr
<span class="hljs-built_in">console</span>.log(arr4) <span class="hljs-comment">// 700</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解构位置的变量名之前添加三个点提取当前位置开始的所有元素</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>, <span class="hljs-number">700</span>, <span class="hljs-number">1000</span>]
<span class="hljs-keyword">const</span> [arr1, , ...rest] = arr
<span class="hljs-built_in">console</span>.log(rest) <span class="hljs-comment">//  [ 300, 700, 1000 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解构位置的成员长度小于被解构数组的长度, 按照从前到后的顺序解构</strong>
<strong>解构位置的成员长度大于被解构数组的长度, 解构值为undefined, 类似访问数组不存在的下标</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>]
<span class="hljs-keyword">const</span> [foo] = arr;
<span class="hljs-built_in">console</span>.log(foo) <span class="hljs-comment">// 100</span>
<span class="hljs-keyword">const</span> [bar, bbr, bcr] = arr
<span class="hljs-built_in">console</span>.log(bar, bbr, bcr) <span class="hljs-comment">// 100, 200 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以给解构位置成员设置默认值</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>]
<span class="hljs-keyword">const</span> [bar, bbr, bcr = <span class="hljs-string">'默认'</span>] = arr
<span class="hljs-built_in">console</span>.log(bar, bbr, bcr) <span class="hljs-comment">// 100, 200 默认</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>应用场景</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path  = <span class="hljs-string">"/foo/bar/test"</span>
<span class="hljs-keyword">const</span> [ , rootDir] = path.split(<span class="hljs-string">'/'</span>)
<span class="hljs-built_in">console</span>.log(rootDir) <span class="hljs-comment">// foo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">对象解构</h4>
<p><strong>根据属性名匹配提取</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"a"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-string">"b"</span>
&#125;
<span class="hljs-keyword">const</span> &#123; name &#125;  = obj
<span class="hljs-built_in">console</span>.log(name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他特点与数组一致, 如未匹配到的成员为 undefined , 可以设置默认值.
<strong>需要注意的是, 由于解构的变量名是用来匹配解构对象的属性名的, 当该变量名在作用域中存在同名的成员时, 会出现冲突</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"a"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-string">"b"</span>
&#125;
<span class="hljs-keyword">const</span> name = <span class="hljs-string">"quanju"</span>
<span class="hljs-keyword">const</span> &#123; name &#125;  = obj
<span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// Identifier 'name' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过重命名的方式解决, 在解构位置的成员名后加冒号和新的成员名.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"a"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-string">"b"</span>
&#125;
<span class="hljs-keyword">const</span> name = <span class="hljs-string">"quanju"</span>
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">name</span>:objName &#125;  = obj
<span class="hljs-built_in">console</span>.log(objName) <span class="hljs-comment">// Identifier 'name' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>应用场景</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; log &#125; = <span class="hljs-built_in">console</span>
log(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.模版字符串</h3>
<h4 data-id="heading-13">模版字符串字面量</h4>
<p>在 ES2015 中还增强了定义字符串的方式, 传统定义字符串的方式是单引号或者双引号, ES2015可以通过反引号的方式定义字符串,</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"hello world , my name is javascript"</span>
<span class="hljs-keyword">const</span> strNew = <span class="hljs-string">`hello world , my name is \`javascript\``</span>

<span class="hljs-built_in">console</span>.log(str)
<span class="hljs-built_in">console</span>.log(strNew)

<span class="hljs-comment">// hello world , my name is javascript</span>
<span class="hljs-comment">// hello world , my name is `javascript`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传统字符串不支持换行, 需要用 \n 表示, 模版字符串支持多行字符串.
模版字符串支持插值表达式的方式嵌入所对应的数值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"tom"</span>
<span class="hljs-keyword">const</span> msg = <span class="hljs-string">`hey <span class="hljs-subst">$&#123;name&#125;</span>`</span>
<span class="hljs-built_in">console</span>.log(msg)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带标签的模版字符串, 可以接收到字符串的数据, 以数组的形式获取</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> str = <span class="hljs-built_in">console</span>.log<span class="hljs-string">`hello world`</span>
[ <span class="hljs-string">'hello world'</span> ]

<span class="hljs-keyword">const</span> name = <span class="hljs-string">"tom"</span>
<span class="hljs-keyword">const</span> gender = <span class="hljs-literal">true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TagFunc</span> (<span class="hljs-params">strings</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(strings)
&#125;
<span class="hljs-keyword">const</span> result = TagFunc<span class="hljs-string">`hey, <span class="hljs-subst">$&#123;name&#125;</span> is a <span class="hljs-subst">$&#123;gender&#125;</span> `</span>
<span class="hljs-comment">// [ 'hey, ', ' is a ', ' ' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带标签的模版字符串, 可以接收到变量的数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"tom"</span>
<span class="hljs-keyword">const</span> gender = <span class="hljs-literal">true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TagFunc2</span> (<span class="hljs-params">strings, name, gender</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(strings,name, gender)
&#125;
<span class="hljs-keyword">const</span> result2 = TagFunc2<span class="hljs-string">`hey, <span class="hljs-subst">$&#123;name&#125;</span> is a <span class="hljs-subst">$&#123;gender&#125;</span> `</span>
<span class="hljs-comment">// [ 'hey, ', ' is a ', ' ' ] tom true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带标签的模版字符串, 返回值就是字符串的结果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"tom"</span>
<span class="hljs-keyword">const</span> gender = <span class="hljs-literal">true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TagFunc3</span> (<span class="hljs-params">strings, name, gender</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">123</span>
&#125;
<span class="hljs-keyword">const</span> result3 = TagFunc3<span class="hljs-string">`hey, <span class="hljs-subst">$&#123;name&#125;</span> is a <span class="hljs-subst">$&#123;gender&#125;</span> `</span>
<span class="hljs-built_in">console</span>.log(result3)
<span class="hljs-comment">// 123 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带标签的模版字符串, 可以对字符串数据进行处理,返回需要的字符串数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> name = <span class="hljs-string">"tom"</span>
<span class="hljs-keyword">const</span> gender = <span class="hljs-literal">true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TagFunc4</span> (<span class="hljs-params">strings, name, gender</span>) </span>&#123;
    <span class="hljs-keyword">const</span> sex = gender ? <span class="hljs-string">"man"</span> : <span class="hljs-string">"women"</span>
    <span class="hljs-keyword">return</span> strings[<span class="hljs-number">0</span>] + name + strings[<span class="hljs-number">1</span>] + sex + strings[<span class="hljs-number">2</span>]
&#125;
<span class="hljs-keyword">const</span> result4 = TagFunc4<span class="hljs-string">`hey, <span class="hljs-subst">$&#123;name&#125;</span> is a <span class="hljs-subst">$&#123;gender&#125;</span> `</span>
<span class="hljs-built_in">console</span>.log(result4)
<span class="hljs-comment">// hey, tom is a man</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4,.字符串的扩展方法</h3>
<p>一组方法判断字符串中是否包含指定内容</p>
<ul>
<li>includes()</li>
<li>startsWith()</li>
<li>endsWidth()</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> msg = <span class="hljs-string">'Error: foo is not defined.'</span>
<span class="hljs-built_in">console</span>.log(msg.includes(<span class="hljs-string">'foo'</span>))
<span class="hljs-built_in">console</span>.log(msg.startsWith(<span class="hljs-string">'Error'</span>))
<span class="hljs-built_in">console</span>.log(msg.endsWith(<span class="hljs-string">'.'</span>))
<span class="hljs-comment">// true</span>
<span class="hljs-comment">// true</span>
<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5.函数参数</h3>
<p>ECMAscript2015 中为函数的形参列表扩展了新语法</p>
<h4 data-id="heading-16">参数默认值</h4>
<p>以前为函数参数定义默认值需要在函数体中实现
ECMAscript2015 可以在参数重直接设置默认值
一般带有默认值的参数需要在函数多个参数的最后</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">enable</span>)</span>&#123;
    enable = enable === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">true</span> : enable;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"> enable = <span class="hljs-literal">true</span> </span>)</span>&#123;
    enable = enable === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">true</span> : enable;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">剩余参数</h4>
<p>对于未知个数的参数, 以前通过 arguments 伪数组接收
ECMAscript2015 可以在通过 ... 操作符实现
由于接收的是所有的参数,所以该操作符只能出现在形参的最后一位,只能出现一次</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">...args</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(args)
&#125;
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>)
<span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6.展开数组</h3>
<p>... 操作符除了用于收取剩余参数(rest), 还可以展开数组(spread)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-string">'dear'</span>]
<span class="hljs-built_in">console</span>.log(
    arr[<span class="hljs-number">0</span>],
    arr[<span class="hljs-number">1</span>],
    arr[<span class="hljs-number">2</span>],
)
<span class="hljs-built_in">console</span>.log.apply(<span class="hljs-built_in">console</span>, arr)
<span class="hljs-built_in">console</span>.log(...arr)
<span class="hljs-comment">// foo bar dear</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">7.箭头函数</h3>
<p>简化了函数表达式的定义方式, 多了一些新特性
箭头左边是参数列表,多个参数可以用 () 定义,
箭头右边是函数体, 多条表达式语句需要使用 &#123;&#125; 包裹 用 return 返回</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span> (<span class="hljs-params"></span>) </span>&#123; &#125;
<span class="hljs-keyword">const</span> inf = <span class="hljs-function"><span class="hljs-params">n</span> =></span> n+<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数的方式定义函数, 使代码更加简短易读.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">11</span>, <span class="hljs-number">24</span>, <span class="hljs-number">9</span>]
arr.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">v</span>)</span>&#123;
    <span class="hljs-keyword">return</span> v><span class="hljs-number">6</span>
&#125;)
arr.filter(<span class="hljs-function"><span class="hljs-params">v</span> =></span> v><span class="hljs-number">6</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数最大的改变就是不会改变 this 指向</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>, 
    <span class="hljs-attr">sayHello</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(
            <span class="hljs-string">`hello, my name is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>
        )
    &#125;,
    <span class="hljs-attr">sayHello2</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(
            <span class="hljs-string">`hello, my name is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>
        )
    &#125;,
    <span class="hljs-attr">sayHiAsync1</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
        &#125;,<span class="hljs-number">1000</span>)
    &#125;,
    <span class="hljs-attr">sayHiAsync2</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(_this.name)
        &#125;,<span class="hljs-number">1000</span>)
    &#125;,
    <span class="hljs-attr">sayHiAsync3</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
        &#125;,<span class="hljs-number">1000</span>)
    &#125;,
&#125;
person.sayHello()
person.sayHello2()
<span class="hljs-comment">//  hello, my name is tom</span>
<span class="hljs-comment">//  hello, my name is undefined</span>

person.sayHiAsync1()
person.sayHiAsync2()
person.sayHiAsync3()
<span class="hljs-comment">//  undefined</span>
<span class="hljs-comment">// tom</span>
<span class="hljs-comment">// tom</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">8.对象字面量增强</h3>
<p>对象是我们最常用的数据结构, 在 ECMAscript2015 中升级了字面量的语法.
传统的对象字面量要求我们使用 属性名 冒号 属性值 一一对应的方式, 在新语法中, 变量名与添加到对象中的属性名一致的时候, 可以简写.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> foo = <span class="hljs-string">"foo"</span>
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">bar</span>: <span class="hljs-string">"bar"</span> , <span class="hljs-comment">// 传统</span>
    foo ,       <span class="hljs-comment">// 等价于 foo: foo</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象添加方法: 传统方式 属性名 冒号 function, 新语法, 省略 冒号、function</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-comment">// 传统方式</span>
    <span class="hljs-attr">methods1</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

    &#125;,
    <span class="hljs-comment">// 新语法</span>
    methods2 () &#123;
        <span class="hljs-comment">// 也是普通的function</span>
        <span class="hljs-comment">// this指向的是当前对象</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象可以使用表达式的返回值作为对象属性名. 在 ECMAscript2015 之后可以通过 [] 直接使用动态值, 称为 <strong>计算属性名</strong>
用 [] 包裹表达式, 将表达式的运行结果作为对象的属性名</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 传统方式</span>
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">"11"</span>,
    <span class="hljs-built_in">Math</span>.random(): <span class="hljs-number">123</span> <span class="hljs-comment">//  报错</span>
&#125;
obj[<span class="hljs-built_in">Math</span>.random()] = <span class="hljs-number">123</span>

<span class="hljs-comment">// 新语法</span>
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">"11"</span>,
    [<span class="hljs-built_in">Math</span>.random()]: <span class="hljs-number">123</span> ,<span class="hljs-comment">// 正确</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">9.对象扩展方法</h3>
<h4 data-id="heading-22">Object.assign</h4>
<p>将多个原对象中的属性, 复制到一个目标对象中, 如果存在相同的属性,原对象中的属性覆盖目标对象的属性
从原对象去 向目标对象放
支持传入任意个数的对象, 第一个参数为目标对象, 返回目标对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> source = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">34</span>
&#125;
<span class="hljs-keyword">const</span> target = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-number">55</span>
&#125;
<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Object</span>.assign(target, source)
<span class="hljs-built_in">console</span>.log(result)
<span class="hljs-built_in">console</span>.log(result === target)

<span class="hljs-comment">// &#123; a: 12, c: 55, b: 34 &#125;</span>
<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>应用场景:复制对象</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj1 = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"tom"</span>&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params">obj</span>)</span>&#123;
    obj.name = <span class="hljs-string">'lili'</span>
&#125;
fun1(obj1) <span class="hljs-comment">// &#123; name: 'lili' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中, 运行函数, 改变了原来对象上属性的值, 我们可以通过复制一个新对象的方式避免这种问题的发生</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj2 = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"tom"</span>&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun2</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">const</span> funobj = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, obj)
    funobj.name = <span class="hljs-string">'lili'</span>
&#125;
fun2(obj2) 
<span class="hljs-built_in">console</span>.log(obj2) <span class="hljs-comment">// &#123; name: 'tom' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">Object.is</h4>
<p>判断两个值是否相等, 在 ECMAscript2015 之前一般使用 相等(==)或 严格相等(===) 比较两个数据是否相等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log( <span class="hljs-number">0</span> == <span class="hljs-literal">false</span>)     <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">0</span> === <span class="hljs-literal">false</span>)    <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log( +<span class="hljs-number">0</span> === -<span class="hljs-number">0</span> )     <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-literal">NaN</span> === <span class="hljs-literal">NaN</span> )   <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.is(+<span class="hljs-number">0</span>, -<span class="hljs-number">0</span>)            <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">NaN</span>, <span class="hljs-literal">NaN</span>)          <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">10.代理对象 Proxy</h3>
<p>如果我们想要监视对象的某个属性的读写, 我们可以使用 ES5 提供的 Object.defineProperty() 为对象添加属性, 从而捕获对象的读写过程.
ECMAscript2015 中新增了 Proxy 为对象添加代理,可以轻松监视对象的读写过程.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
&#125;
<span class="hljs-keyword">const</span> personProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, property</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(target, property)
        <span class="hljs-keyword">return</span> property <span class="hljs-keyword">in</span> target ? target[property] : <span class="hljs-string">"default"</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, property, value</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(target, property, value)
        <span class="hljs-comment">// 拦截 做数据校验</span>
        <span class="hljs-keyword">if</span>(property === <span class="hljs-string">'age'</span>)&#123;
            <span class="hljs-keyword">if</span>( !<span class="hljs-built_in">Number</span>.isInteger(value) )&#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;value&#125;</span> is not int`</span>)
            &#125;
        &#125;
        target[property] = value
    &#125;
&#125;)
personProxy.name  <span class="hljs-comment">// &#123; name: 'tom', age: 20 &#125; name</span>
personProxy.sex  <span class="hljs-comment">//  &#123; name: 'tom', age: 20 &#125; sex</span>


personProxy.age = <span class="hljs-string">"sss"</span> 
<span class="hljs-comment">// &#123; name: 'tom', age: 20 &#125; age sss</span>
<span class="hljs-comment">//  sss is not int</span>
personProxy.age = <span class="hljs-number">18</span> 
<span class="hljs-comment">// &#123; name: 'tom', age: 20 &#125; age 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>与Object.defineProperty()区别</strong></p>
<ul>
<li>defineProperty只能监视属性的读写, Proxy 能够监视对象更多的操作(如delete等)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
&#125;
<span class="hljs-keyword">const</span> personProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target, property</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(target, property)
        <span class="hljs-keyword">delete</span> target[property]
    &#125;
&#125;)

<span class="hljs-keyword">delete</span> personProxy.age <span class="hljs-comment">//  name: 'tom', age: 18 &#125; age</span>
<span class="hljs-built_in">console</span>.log(person)    <span class="hljs-comment">// &#123; name: 'tom' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccd23c6c674a464a90b86f60d615ffa4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<ul>
<li>对数组的操作, defineProperty 监听数组需要重写数组方法.Proxy 可以直接监听数组变化</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> list = []
<span class="hljs-keyword">const</span> listProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(list, &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, property, value</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(target, property, value)
        target[property] = value
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
&#125;)
listProxy.push(<span class="hljs-number">100</span>)

<span class="hljs-comment">// [] 0 100</span>
<span class="hljs-comment">// [ 100 ] length 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Proxy 以非侵入的方式监管了对象的读写, 对于定义好的对象, 不需要对对象本身做任何操作, 就可以监视对象读写. defineProperty 要求我们以特定的方式单独定义对象中需要监视的属性.</li>
</ul>
<h3 data-id="heading-25">11.Reflect</h3>
<p>ECMAscript2015 提供的一个全新的内置对象, 是一个统一的对象操作 API,.
Reflect 属于静态类, 不能通过 New 构造实例对象, 只能调用其中的静态方法, 如 Reflect.get()
Reflect 封装了一系列对对象的底层操作, 一共封装了 13 个方法, 是 Proxy 处理对象方法的默认实现, 也就是当我们没有定义对像的处理方法, 内部的方法默认实现的逻辑为 Reflect 对象中的方法.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">14</span>
&#125;
<span class="hljs-keyword">const</span> ProxyObj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
    get (target, property)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target, property)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>意义:</strong>
<strong>提供了统一用于操作对象的 API, 愿先对于对象的操作, 我们可以使用 Object 上面的方法, 也可能使用 delete、in 等操作符, Reflect统一了对象的操作方式.</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">14</span>
&#125;
<span class="hljs-comment">// 判断属性是否存在</span>
<span class="hljs-string">'name'</span> <span class="hljs-keyword">in</span> obj
<span class="hljs-built_in">Reflect</span>.has(<span class="hljs-string">"name"</span>)
<span class="hljs-comment">// 删除属性</span>
<span class="hljs-keyword">delete</span> obj.name
<span class="hljs-built_in">Reflect</span>.deleteProperty(<span class="hljs-string">"name"</span>)
<span class="hljs-comment">// 获取对象的属性</span>
<span class="hljs-built_in">Object</span>.keys(obj)
<span class="hljs-built_in">Reflect</span>.ownKeys(<span class="hljs-string">"name"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">12.Promise</h3>
<p>全新的异步编程解决方案, 链式调用解决了回调函数嵌套过多的问题.详细请看 Javascript异步编程.</p>
<h3 data-id="heading-27">13.class 类</h3>
<h4 data-id="heading-28">基本使用</h4>
<p>在 ECMAscript2015 之前, javascript 通过定义函数以及函数的原型对象实现类型.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义函数作为构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 通过this访问当前的实例对象</span>
    <span class="hljs-built_in">this</span>.name = name; 
&#125;
<span class="hljs-comment">// 通过 prototype 共享成员方法</span>
Person.prototype.say()&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ECMAscript2015 之后, 通过 class 关键字独立定义类型.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-comment">// 构造函数</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-comment">//  直接定义实例方法</span>
    say () &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name ) 
    &#125;
&#125;
<span class="hljs-comment">// 使用new关键词创建实例</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'aa'</span>)
p.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">类中的方法</h4>
<p>类中的方法分为<strong>静态方法</strong>和<strong>实例方法</strong>两种.
实例方法是通过类构造的实例对象调用
静态方法可以直接通过类型本身调用. 以前我们实现静态方法直接在构造函数对象上挂载方法. ECMAscript2015 之后新增了 static 关键词定义静态方法.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-comment">// 构造函数</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-comment">//  直接定义实例方法</span>
    say () &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name ) 
    &#125;
    <span class="hljs-comment">// 静态方法</span>
    <span class="hljs-keyword">static</span> create (name) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Person(name)
    &#125;
&#125;
<span class="hljs-comment">// 使用new关键词创建实例</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'aa'</span>)
p.say()
<span class="hljs-keyword">const</span> p2 = Person.create(<span class="hljs-string">'aa'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是, 静态方法是直接挂载在类型上的, 所以静态方法内部的 this 不会指向实例, 而是指向当前类型.</strong></p>
<h4 data-id="heading-30">继承</h4>
<p>继承是面向对象一个非常重要的特性, 通过继承我们可以将对象之间相同的特性进行抽象, 在 ECMAscript2015 之前, 通过原型的方式实现, 在 ECMAscript2015中定义了 extends 关键词实现继承</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    say () &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name ) 
    &#125;
    <span class="hljs-keyword">static</span> create (name) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Person(name)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Students</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-title">constructor</span> (<span class="hljs-params">name, studentId</span>) &#123;
        <span class="hljs-built_in">super</span>(name) <span class="hljs-comment">//  始终指向父类, 相当于调用父类的构造函数</span>
        <span class="hljs-built_in">this</span>.studentId = studentId
    &#125; 
    <span class="hljs-function"><span class="hljs-title">hello</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">super</span>.say();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`my school id is <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.studentId&#125;</span>`</span>)
    &#125;
&#125;
<span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> Students(<span class="hljs-string">"bb"</span>)
s.hello()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">14.Set 数据结构</h3>
<p>ECMAscript2015 新增了 Set 的全新数据结构, 与数组类似, 不同的是 Set 的内部成员不允许重复.
Set 是一个类型, 通过构造的实例存放不重复的数据
可以通过实例的 add 方法添加数据,并返回对象本身, 可以链式调用.
通过 forEach 方法 或者 of 方法进行遍历
通过 size 属性 获取集合的长度
通过 has 方法判断集合中是否存在特定的值
通过 delete 方法删除指定值, 返回 true 或 false
通过 clear 方法清除所有数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
s.add(<span class="hljs-number">1</span>);
s.add(<span class="hljs-number">12</span>);
s.add(<span class="hljs-number">15</span>);
s.add(<span class="hljs-number">17</span>);
<span class="hljs-built_in">console</span>.log(s)
s.forEach(<span class="hljs-function"><span class="hljs-params">i</span> =></span> cosnole.log(i))
<span class="hljs-built_in">console</span>.log(s.size)
<span class="hljs-built_in">console</span>.log(s.has(<span class="hljs-number">11</span>))
<span class="hljs-built_in">console</span>.log(s.delete(<span class="hljs-number">15</span>))
s.clear()
<span class="hljs-built_in">console</span>.log(s)
<span class="hljs-comment">/**
Set &#123; 1, 12, 15, 17 &#125;
1
12
15
17
4
false
true
Set &#123;&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最常见的应用场景是数组去重.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">34</span>, <span class="hljs-number">1</span>, <span class="hljs-number">15</span>, <span class="hljs-number">6</span>, <span class="hljs-number">35</span>, <span class="hljs-number">5</span>, <span class="hljs-number">15</span>]
<span class="hljs-keyword">const</span> ss = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr)
<span class="hljs-built_in">console</span>.log(ss)
<span class="hljs-comment">// Set &#123; 1, 3, 34, 15, 6, 35, 5 &#125;</span>
<span class="hljs-keyword">const</span> resArr = <span class="hljs-built_in">Array</span>.from(ss)
<span class="hljs-built_in">console</span>.log(resArr)
<span class="hljs-comment">/* [
   1,  3,
  34, 15,
   6, 35,
   5
]
*/</span>
<span class="hljs-keyword">const</span> resArr2 = [...new <span class="hljs-built_in">Set</span>(arr)]
<span class="hljs-built_in">console</span>.log(resArr2)
<span class="hljs-comment">/* [
   1,  3,
  34, 15,
   6, 35,
   5
]
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">15.Map 数据解构</h3>
<p>Map 数据解构与对象类似,本质都是键值对集合.
一般对象结构中的键只能是字符串, 所以在存放复杂数据结构的时候会有问题.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;&#125;
obj[<span class="hljs-literal">true</span>] = <span class="hljs-string">"value"</span>
obj[<span class="hljs-number">1</span>] = <span class="hljs-string">"value"</span>
obj[&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>&#125;] = <span class="hljs-string">"value"</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(obj))
<span class="hljs-comment">// [ '1', 'true', '[object Object]' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码我们可以看到, 我们设置的布尔值、数字、对象类型的键盘都转换为了字符串. 也就是说如果我们给对象添加的键不是字符串, 就会被用 toString 转换为字符串.
ECMAscript2015 中的 Map 解决了这种问题, Map 可以说才是从严格意义上键值对的集合, 用来映射两个任意类型数据之间的关系.
通过 set 方法存数据
通过 get 方法获取数据
通过 has 方法判断是否存在
判断 claer 方法清空所有数据
通过 forEach 方法遍历数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>&#125;, <span class="hljs-literal">false</span>)
<span class="hljs-built_in">console</span>.log(m)
<span class="hljs-comment">// Map &#123; &#123; a: 1 &#125; => false &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">16.Symbol</h3>
<h4 data-id="heading-34">基本使用</h4>
<p>一种全新的原始数据类型, 在 ECMAscript2015 之前, 对象的属性名都是字符串, 字符串是可能重复的, 重复就会产生冲突.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/// a.js</span>
cache[<span class="hljs-string">"aa"</span>] = foo;

<span class="hljs-comment">// b.js</span>
cache[<span class="hljs-string">"aa"</span>] = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种情况在我们引用第三方库,扩展第三方模块对象进行开发的时候, 很容易发生, 一般我们通过约定的方式规避这样的问题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/// a.js</span>
cache[<span class="hljs-string">"a_aa"</span>] = foo;

<span class="hljs-comment">// b.js</span>
cache[<span class="hljs-string">"b_aa"</span>] = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ECMAscript2015 提供了一种全新的数据类型 Symbol 解决这样的问题.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sm = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-built_in">console</span>.log(sm)  <span class="hljs-comment">// Symbol()</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> sm) <span class="hljs-comment">// symbol</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种类型最大的特点就是独一无二,也就是说我们通过 Symbol 函数创建的值永远不会重复.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sm1 = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">const</span> sm2 = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-built_in">console</span>.log( sm1=== sm2) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>考虑到开发过程中的调试, Symbol 函数允许我们传递一个字符串作为参数表示对数据的描述</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sm3 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"sm3"</span>);
<span class="hljs-built_in">console</span>.log(sm3)  <span class="hljs-comment">// Symbol(sm3)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ECMAscript2015 之后开始, 对象可以使用 Symbol 类型的值作为属性名.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> objSm = &#123;
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"sm3"</span>)]: <span class="hljs-number">123</span>
&#125;
objSm[<span class="hljs-built_in">Symbol</span>()] = <span class="hljs-number">333</span>;
objSm[<span class="hljs-built_in">Symbol</span>()] = <span class="hljs-number">322</span>;
<span class="hljs-built_in">console</span>.log(objSm)
<span class="hljs-comment">// &#123; [Symbol(sm3)]: 123, [Symbol()]: 333, [Symbol()]: 322 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Symbol 除了能够解决对象名重复产生的问题, 还可以实现对象的私有成员.
以前我们通过约定来表示对象的私有成员, 如用下划线开头( _a ).</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// a.js </span>
<span class="hljs-keyword">const</span> name = <span class="hljs-built_in">Symbol</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    [name]: <span class="hljs-string">"aa"</span>,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;

    &#125;
&#125;
<span class="hljs-comment">/// b.js</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> Person()
p.say();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面代码所演示, 在对象内部我们可以使用创建属性时的 Symbol 拿到对应的属性成员, 在外部文件中 我们无法创建一个完全相同的Symbol, 所以实现了私有成员.
Symbol 目前最主要的作用就是为对象添加独一无二的属性标识.</p>
<h4 data-id="heading-35">注意事项</h4>
<p><strong>唯一性: 每次调用 Symbol 函数产生的结果都是唯一的, 不管我们传入的描述文本是否相同.</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>) === <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'foo'</span>) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们可以使用全局变量或者静态的 for 方法 实现在全局复用一个相同的值</strong>
for 方法接收一个字符串作为参数, 相同的字符串返回相同的 Symbol 值, <code>Symbol.for("foo") === Symbol.for("foo")</code>
for 提供了一个全局注册表, 提供了 字符串 和 Symbol 一一对应的关系.
for 传入非字符串的时候, 内部方法会自动转换为字符串 .<code>Symbol.for("true") === Symbol.for(true)</code>
<strong>Symbol 对象提供了内置的常量, 用来作为内部方法的标识, 这些标识符可以让自定义对象实现js中内置的接口</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;&#125;
<span class="hljs-built_in">console</span>.log(obj.toString())
<span class="hljs-built_in">console</span>.log(obj.toString())
<span class="hljs-comment">// [object Object]</span>

<span class="hljs-keyword">const</span> obj13 = &#123;
    [<span class="hljs-built_in">Symbol</span>.toStringTag]:<span class="hljs-string">'xxObject'</span>
&#125;
<span class="hljs-built_in">console</span>.log(obj13.toString())
<span class="hljs-comment">// [object xxObject]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Symbol 作为对象的属性名, 通过 forEach 或 Object.keys() 是无法拿到的. 使用 JSON.stringfy() 序列化对象也会忽略该属性.
只可以通过 getOwnPropertySymbols 获取所有 Symbol 类型的属性名.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> objSymbol = &#123;
    <span class="hljs-built_in">Symbol</span>():<span class="hljs-string">'Symbolonly'</span>,
    <span class="hljs-attr">aa</span>: <span class="hljs-number">15</span>
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(objSymbol) )<span class="hljs-comment">// [ 'aa' ]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(objSymbol)) <span class="hljs-comment">// &#123;"aa":15&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getOwnPropertySymbols(objSymbol)) <span class="hljs-comment">// [ Symbol() ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">17.for... of 循环</h3>
<h4 data-id="heading-37">基础语法</h4>
<p>ECMAscript 中遍历数据有很多种方法, for 循环适合遍历普通数组, for... in 循环适合遍历键值对, 还有一些函数式的遍历方法.
ECMAscript2015 引用了全新的遍历方式, 作为遍历所有数据结构的统一方式.
<strong>对数组的遍历</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> array = [<span class="hljs-number">133</span>, <span class="hljs-number">345</span>, <span class="hljs-number">233</span>, <span class="hljs-number">445</span>]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> array)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-comment">// 133, 345, 233, 445</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>for of 循环 可以使用 break 跳出循环.</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> array = [<span class="hljs-number">133</span>, <span class="hljs-number">345</span>, <span class="hljs-number">233</span>, <span class="hljs-number">445</span>]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> array)&#123;
    <span class="hljs-built_in">console</span>.log(item)
    <span class="hljs-keyword">if</span>(item > <span class="hljs-number">200</span>)&#123;
        <span class="hljs-keyword">break</span>
    &#125;
&#125;
<span class="hljs-comment">// 133, 345</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>for of 除了可以遍历数组对象, 还可以对伪数组进行遍历.</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> <span class="hljs-built_in">arguments</span>)&#123;
        <span class="hljs-built_in">console</span>.log(item)
    &#125;
&#125;
Fun(<span class="hljs-string">'1'</span>,<span class="hljs-string">"22"</span>,<span class="hljs-string">"333"</span>) <span class="hljs-comment">// 1 22 333 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Set 和 Map 对象也可以通过 for of 进行遍历</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"aa"</span>, <span class="hljs-string">"bb"</span>, <span class="hljs-string">"cc"</span>])
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> set)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是, Map 对象的遍历,我们得到的是对象的键和值组成的数组.</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
map.add(<span class="hljs-string">'name'</span>, <span class="hljs-string">"tom"</span>)
map.add(<span class="hljs-string">'age'</span>, <span class="hljs-string">"18"</span>)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> map)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-comment">// [ 'name', 'tom' ]</span>
<span class="hljs-comment">// [ 'age', '18' ]</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> map)&#123;
    <span class="hljs-built_in">console</span>.log(key, value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对象的遍历</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">"tom"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> obj)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;

<span class="hljs-comment">// objet is not iterable  不可迭代</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">18.迭代器</h3>
<h4 data-id="heading-39">可迭代接口</h4>
<p>for...of 作为一种统一的遍历数据的方式, 我们遍历普通的对象却发生了错误.这是什么原因呢?
在 ES 中, 能够表示有结构的数据越来越多, 如 Set、Map、Array, 为了为各种各样的数据结构提供统一的遍历方法, ES2015 提供了 Iterable 的接口.
接口可以理解为一种统一的规格标准.
Iterable 接口就是一种能够被 for...of 循环遍历访问的规格标准, 所以含有 Iterable 接口的对象就可以被 for...of 遍历.</p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5782a80599949ab9c8a31d544a29a26~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293272800f114149a7be707a0e7b3607~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>我们继续观察到 Symbol.iterator 是一个方法,  在 Symbol.iterator 内部有一个 next 方法.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]; 
<span class="hljs-keyword">const</span> iterator = arr[<span class="hljs-built_in">Symbol</span>.iterator]()
iterator.next();
<span class="hljs-comment">// &#123;value: 1, done: false&#125;</span>
iterator.next();
<span class="hljs-comment">// &#123;value: 2, done: false&#125;</span>
iterator.next();
<span class="hljs-comment">// &#123;value: 3, done: false&#125;</span>
iterator.next();
<span class="hljs-comment">// &#123;value: undefined, done: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d9abad19ba64fa2882490caca0e6820~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p><strong>总结</strong></p>
<p>所有能被 for...of 循环遍历的数据类型都需要实现 Iterable 的接口, Iterable 内部挂载了一个 iterator 方法, 返回一个带有 next 方法的对象, 调用 next 方法就可以实现对数据的遍历.
这就是 for...of 循环的工作原理.</p>
<h4 data-id="heading-40">实现</h4>
<p>for...of 循环通过调用被循环对象的 iterator 方法,得到一个迭代器从而得到所有数据.
了解 for...of 的工作原理之后, 我们就能够理解为什么 for...of  循环为什么能作为遍历所有数据的统一方法了.
我们可以在普通对象上挂载一个 iterator 方法, 使普通对象能够通过  for...of 循环遍历.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
    
    [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

        <span class="hljs-keyword">return</span> &#123;

            <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">value</span>: <span class="hljs-string">'123'</span>,
                    <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>
                &#125;

            &#125;

        &#125;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3a4238732648c48fb2842117cef8d3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p><strong>三个对象</strong></p>
<p><strong>Iterable: 可迭代接口, 规定内部必须有一个返回迭代器的 iterator 方法.</strong></p>
<p><strong>Iterator: 迭代器接口, 内部必须有一个用于迭代的 next 方法.</strong></p>
<p><strong>IterationResult: 迭代结果接口, value表示当前迭代数据, done 表示迭代是否结束</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> objIterator = &#123;
    <span class="hljs-attr">store</span>:[<span class="hljs-string">"foo"</span>, <span class="hljs-string">"bar"</span>, <span class="hljs-string">"aa"</span>],
    
    [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">let</span> result = &#123;
                    <span class="hljs-attr">value</span>: self.store[index],
                    <span class="hljs-attr">done</span>: index === self.store.length
                &#125;
                index++
                <span class="hljs-keyword">return</span> result
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span>  objIterator)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-comment">// foo</span>
<span class="hljs-comment">// bar</span>
<span class="hljs-comment">// aa </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-41">迭代器模式</h4>
<p>下面我们通过一个案例演示一下迭代器模式.
案例 协同工作完成一个任务清单</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// aa 生成任务列表</span>
<span class="hljs-keyword">const</span> todoList = &#123;
    <span class="hljs-attr">life</span> :[<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"睡觉"</span>, <span class="hljs-string">"打豆豆"</span>],
    <span class="hljs-attr">works</span>:[<span class="hljs-string">"语文"</span>, <span class="hljs-string">"数学"</span>. <span class="hljs-string">"英语"</span>],
&#125;


<span class="hljs-comment">// bb 处理任务列表数据</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> todoList.life)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> todoList.works)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面的代码所示, 当我们需要协同完成一个任务列表的开发任务, A 负责生成任务列表, B 负责处理数据. 按照上面的处理方式, 当 A 的数据发生变化时, B 的数据处理逻辑也需要发生变化.如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// aa 生成任务列表</span>
<span class="hljs-keyword">const</span> todoList = &#123;
    <span class="hljs-attr">life</span> :[<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"睡觉"</span>, <span class="hljs-string">"打豆豆"</span>],
    <span class="hljs-attr">learn</span>:[<span class="hljs-string">"语文"</span>, <span class="hljs-string">"数学"</span>. <span class="hljs-string">"英语"</span>],
    <span class="hljs-attr">workes</span>:[<span class="hljs-string">"写代码"</span>],

&#125;

<span class="hljs-comment">// bb 处理任务列表数据</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> todoList.life)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> todoList.learn)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> todoList.workes)&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像这样极度耦合的代码大大增强了维护的难度, 我们可以对外暴露一个遍历数据的接口, 使代码更加通用.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// aa 生成任务列表</span>
<span class="hljs-keyword">const</span> todoList = &#123;
    <span class="hljs-attr">life</span> :[<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"睡觉"</span>, <span class="hljs-string">"打豆豆"</span>],
    <span class="hljs-attr">learn</span>:[<span class="hljs-string">"语文"</span>, <span class="hljs-string">"数学"</span>. <span class="hljs-string">"英语"</span>],
    <span class="hljs-attr">workes</span>:[<span class="hljs-string">"写代码"</span>],
    each (callBack) &#123;
        <span class="hljs-keyword">let</span> alls = [].concat(<span class="hljs-built_in">this</span>.life, <span class="hljs-built_in">this</span>.learn, <span class="hljs-built_in">this</span>.workes)
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> alls)&#123;
            callBack(item)
        &#125;
    &#125;

&#125;

<span class="hljs-comment">// bb 处理任务列表数据</span>
todoList.each(<span class="hljs-function"><span class="hljs-params">todo</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(todo)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码所示, 通过对外暴露接口的方式, 减少了重复代码, 使代码维护更加方便了, 我们可以通过迭代器实现同样的功能.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// aa 生成任务列表</span>
<span class="hljs-keyword">const</span> todoList = &#123;
    <span class="hljs-attr">life</span> :[<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"睡觉"</span>, <span class="hljs-string">"打豆豆"</span>],
    <span class="hljs-attr">learn</span>:[<span class="hljs-string">"语文"</span>, <span class="hljs-string">"数学"</span>. <span class="hljs-string">"英语"</span>],
    <span class="hljs-attr">workes</span>:[<span class="hljs-string">"写代码"</span>],
    each (callBack) &#123;
        <span class="hljs-keyword">let</span> alls = [].concat(<span class="hljs-built_in">this</span>.life, <span class="hljs-built_in">this</span>.learn, <span class="hljs-built_in">this</span>.workes)
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> alls)&#123;
            callBack(item)
        &#125;
    &#125;,
    [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> alls = [].concat(<span class="hljs-built_in">this</span>.life, <span class="hljs-built_in">this</span>.learn, <span class="hljs-built_in">this</span>.workes)
        <span class="hljs-keyword">let</span> index  = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">let</span> result =  &#123;
                    <span class="hljs-attr">value</span>: alls[index],
                    <span class="hljs-attr">done</span>:  index >= alls.length,
                &#125;
                index++;
                <span class="hljs-keyword">return</span> result
            &#125;
            
        &#125;
    &#125;

&#125;

<span class="hljs-comment">// bb 处理任务列表数据</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> todo <span class="hljs-keyword">of</span> todoList)&#123;
    <span class="hljs-built_in">console</span>.log(todo)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>迭代器的核心就是, 对外提供统一遍历数据的接口, 让外部不需要关心数据内部的结构.</strong> 上面我们自己的 each 方法只能适用于当前数据结构, 而 ES2015 提供的迭代器是语言层面实现的迭代器模式, 通用于任何数据结构, 只要在内部实现 iterator 方法就可以了.</p>
<h3 data-id="heading-42">19.生成器</h3>
<h4 data-id="heading-43">基本语法</h4>
<p>为了避免回调函数嵌套产生的问题, ES2015 中新增了生成器函数.</p>
<ul>
<li>在普通的函数 function 关键字后加*</li>
<li>生成器函数运行之后返回一个 Generator 对象</li>
<li>Generator 对象上有一个 next 方法, 调用 next 方法, 函数开始执行.</li>
<li>与 yield 关键词配合使用, 可以是函数执行暂停.</li>
<li>yield 后面的值作为 next 的值.</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> * <span class="hljs-title">foo</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
    <span class="hljs-keyword">yield</span> <span class="hljs-number">100</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">222</span>)
    <span class="hljs-keyword">yield</span> <span class="hljs-number">200</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">333</span>)
    <span class="hljs-keyword">yield</span> <span class="hljs-number">300</span>
&#125;
<span class="hljs-keyword">const</span> generator = foo()
<span class="hljs-built_in">console</span>.log(generator.next())
<span class="hljs-comment">// 111</span>
<span class="hljs-comment">// &#123; value: 100, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(generator.next())
<span class="hljs-comment">// 222</span>
<span class="hljs-comment">// &#123; value: 200, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(generator.next())
<span class="hljs-comment">// 333</span>
<span class="hljs-comment">// &#123; value: 300, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(generator.next())
<span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">案例实现</h4>
<p>自增id 发号器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> * <span class="hljs-title">createId</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> id = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
        <span class="hljs-keyword">yield</span> id++;
    &#125;
&#125;
<span class="hljs-keyword">const</span> idMaker = createId();
<span class="hljs-built_in">console</span>.log(idMaker.next().value)
<span class="hljs-built_in">console</span>.log(idMaker.next().value)
<span class="hljs-built_in">console</span>.log(idMaker.next().value)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用生成器函数实现 iterator 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> todoList = &#123;
    <span class="hljs-attr">life</span> :[<span class="hljs-string">"吃饭"</span>, <span class="hljs-string">"睡觉"</span>, <span class="hljs-string">"打豆豆"</span>],
    <span class="hljs-attr">learn</span>:[<span class="hljs-string">"语文"</span>, <span class="hljs-string">"数学"</span>. <span class="hljs-string">"英语"</span>],
    <span class="hljs-attr">workes</span>:[<span class="hljs-string">"写代码"</span>],
    each (callBack) &#123;
        <span class="hljs-keyword">let</span> alls = [].concat(<span class="hljs-built_in">this</span>.life, <span class="hljs-built_in">this</span>.learn, <span class="hljs-built_in">this</span>.workes)
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> alls)&#123;
            callBack(item)
        &#125;
    &#125;,
    [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span> * (<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> alls = [].concat(<span class="hljs-built_in">this</span>.life, <span class="hljs-built_in">this</span>.learn, <span class="hljs-built_in">this</span>.workes)
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> alls)&#123;
            <span class="hljs-keyword">yield</span> item
        &#125;
    &#125;

&#125;

<span class="hljs-comment">// bb 处理任务列表数据</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> todo <span class="hljs-keyword">of</span> todoList)&#123;
    <span class="hljs-built_in">console</span>.log(todo)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成器函数最主要的功能是解决异步回调函数嵌套的问题, 详细请看上一篇 <a href="https://juejin.cn/post/01-1%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B.md">javascript 异步编程</a>.</p>
<h3 data-id="heading-45">20.ES2016概述</h3>
<h4 data-id="heading-46">数组-includs</h4>
<p>直接查找数组中是否包含某个值. 返回布尔值.
可以直接查找 NaN.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Array.prototype.includes</span>
<span class="hljs-keyword">const</span> arr = [<span class="hljs-string">"foo"</span>, <span class="hljs-number">12</span>, <span class="hljs-string">"bar"</span>, <span class="hljs-literal">NaN</span>]

<span class="hljs-built_in">console</span>.log(arrInclu.indexOf(<span class="hljs-string">'bar'</span>))  <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(arrInclu.includes(<span class="hljs-string">'bar'</span>)) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(arrInclu.indexOf(<span class="hljs-literal">NaN</span>))  <span class="hljs-comment">// -1</span>
<span class="hljs-built_in">console</span>.log(arrInclu.includes(<span class="hljs-literal">NaN</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-47">数组-指数运算 **</h4>
<p>与加减乘除一样, 称为语言本身的运算符.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Math</span>.power(<span class="hljs-number">2</span>,<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>,<span class="hljs-number">4</span>)) <span class="hljs-comment">// 16</span>

<span class="hljs-built_in">console</span>.log( <span class="hljs-number">2</span> ** <span class="hljs-number">4</span> )  <span class="hljs-comment">// 16</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">21.ES2017概述</h3>
<h4 data-id="heading-49">Object.values</h4>
<p>与 Object.keys 类似, Object.keys 以数组的形式返回对象的键, Object.values 以数组的形式返回对象的值.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"li"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>&#125;))
<span class="hljs-comment">// [ 'name', 'age' ]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.values(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"li"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>&#125;))
<span class="hljs-comment">// [ 'li', 12 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">Object.entries</h4>
<p>将对象转换为数组形式.</p>
<ul>
<li>用 for of 遍历</li>
<li>转换为 ma p对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.entries(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"li"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>&#125;))
<span class="hljs-comment">// [ [ 'name', 'li' ], [ 'age', 12 ] ]</span>

<span class="hljs-comment">// for of 遍历</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"li"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>&#125;))&#123;
    <span class="hljs-built_in">console</span>.log(key, value)
&#125;

<span class="hljs-comment">// name li</span>
<span class="hljs-comment">// age 12</span>

<span class="hljs-comment">// 转为 map</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(<span class="hljs-built_in">Object</span>.entries(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"li"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">12</span>&#125;)))

<span class="hljs-comment">// Map &#123; 'name' => 'li', 'age' => 12 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">Object.getOwnPropertyDescriptors</h4>
<p>可以获取对象 get set 方法的完整信息, 解决 Object.assign 方法难以复制对象这些属性的弊端.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> nameObj = &#123;
    <span class="hljs-attr">firstName</span>:<span class="hljs-string">"li"</span>,
    <span class="hljs-attr">lastname</span>:<span class="hljs-string">"lei"</span>,
    <span class="hljs-keyword">get</span> <span class="hljs-title">FullName</span>()&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">" "</span> + <span class="hljs-built_in">this</span>.lastname
    &#125;
&#125;

<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(nameObj)
<span class="hljs-built_in">console</span>.log(nameObj.FullName)
<span class="hljs-comment">// li lei</span>

<span class="hljs-keyword">const</span> nameSelf = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,nameObj)
nameSelf.firstName = <span class="hljs-string">"wang"</span>
<span class="hljs-built_in">console</span>.log(nameSelf.FullName)
<span class="hljs-comment">// li lei</span>

<span class="hljs-keyword">const</span> descriptors = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(nameObj)
<span class="hljs-built_in">console</span>.log(descriptors)
<span class="hljs-comment">/*
&#123;
  firstName: &#123; value: 'li', writable: true, enumerable: true, configurable: true &#125;,
  lastname: &#123;
    value: 'lei',
    writable: true,
    enumerable: true,
    configurable: true
  &#125;,
  FullName: &#123;
    get: [Function: get FullName],
    set: undefined,
    enumerable: true,
    configurable: true
  &#125;
&#125;
*/</span>
<span class="hljs-keyword">const</span> nameSelf2 = <span class="hljs-built_in">Object</span>.defineProperties(&#123;&#125;, descriptors)
nameSelf2.firstName = <span class="hljs-string">"wang"</span>
<span class="hljs-built_in">console</span>.log(nameSelf2.FullName)
<span class="hljs-comment">// wang lei</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">padStart、padEnd</h4>
<p>用给定的字符串填充目标字符串开始或结束位置, 直到达到指定长度为止.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> nameObj = &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">"li"</span>,
    <span class="hljs-attr">lastname</span>: <span class="hljs-string">"lei"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">17</span>,
    <span class="hljs-attr">score</span>: <span class="hljs-number">99</span>
&#125;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(nameObj))&#123;
    <span class="hljs-built_in">console</span>.log(key, value)
&#125;
<span class="hljs-comment">/*
firstName li
lastname lei
age 17
score 99
*/</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(nameObj))&#123;
    <span class="hljs-built_in">console</span>.log(
        <span class="hljs-string">`<span class="hljs-subst">$&#123;key.padEnd(<span class="hljs-number">16</span>,<span class="hljs-string">"-"</span>)&#125;</span> | <span class="hljs-subst">$&#123;value.padStart(<span class="hljs-number">5</span>,<span class="hljs-string">" "</span>)&#125;</span>`</span>
    )
&#125;
<span class="hljs-comment">/*
firstName------- |    li
lastname-------- |   lei
age------------- |    17
score----------- |    99
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">Async / Await</h4>
<p>Generator 语法糖, 彻底解决异步编程中回调函数嵌套过深的问题.详细看 javascript 异步编程.</p>
<hr>
<p>(ps: 笔记来源拉钩大前端高薪训练营)</p>
<p>笔记日期:2021.04.01</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            