
---
title: '「万字进阶」深入浅出 Commonjs 和 Es Module'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13686e44fd8947d89d3e330565972f02~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 16:44:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13686e44fd8947d89d3e330565972f02~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一 前言</h2>
<p>今天我们来深度分析一下 <code>Commonjs</code> 和 <code>Es Module</code>，希望通过本文的学习，能够让大家彻底明白 <code>Commonjs</code> 和 <code>Es Module</code> 原理，能够一次性搞定面试中遇到的大部分有关 <code>Commonjs</code> 和 <code>Es Module</code> 的问题。</p>
<p>老规矩我们带上疑问开始今天的分析🤔🤔🤔：</p>
<ul>
<li>1 Commonjs 和 Es Module 有什么区别 ？</li>
<li>2 Commonjs 如何解决的循环引用问题 ？</li>
<li>3 既然有了 <code>exports</code>，为何又出了 <code>module.exports </code>? 既生瑜，何生亮 ？</li>
<li>4 <code>require</code> 模块查找机制 ？</li>
<li>5 Es Module 如何解决循环引用问题 ？</li>
<li>6 <code>exports = &#123;&#125;</code> 这种写法为何无效 ？</li>
<li>7 关于 <code>import()</code> 的动态引入 ？</li>
<li>8 Es Module 如何改变模块下的私有变量 ？</li>
<li>9 ...</li>
</ul>
<blockquote>
<p>ps:由于作者前一段时间在写《React进阶实践指南》小册，没有时间持续输出高质量文章，接下来我会回归创作高质量技术文章，送人玫瑰，手有余香，希望阅读的朋友能给作者点个赞👍，鼓励我持续创作。</p>
</blockquote>
<h2 data-id="heading-1">二 模块化</h2>
<p>早期 JavaScript 开发很容易存在<strong>全局污染</strong>和<strong>依赖管理</strong>混乱问题。这些问题在多人开发前端应用的情况下变得更加棘手。我这里例举一个很常见的场景：</p>
<pre><code class="hljs language-js copyable" lang="js"><body>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./home.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./list.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上在没有模块化的前提下，如果在 <code>html</code> 中这么写，那么就会暴露一系列问题。</p>
<ul>
<li><strong>全局污染</strong></li>
</ul>
<p>没有模块化，那么 <code>script</code> 内部的变量是可以相互污染的。比如有一种场景，如上 <code>./index.js</code> 文件和 <code>./list.js</code> 文件为小 A 开发的，<code>./home.js</code> 为小 B 开发的。</p>
<p>小 A 在 <code>index.js</code>中声明 name 属性是一个字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'我不是外星人'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后小 A 在 <code>list.js</code> 中，引用 name 属性，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13686e44fd8947d89d3e330565972f02~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打印却发现 name 竟然变成了一个函数。刚开始小 A 不知所措，后来发现在小 B 开发的 <code>home.js</code> 文件中这么写道：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">name</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且这个 name 方法被引用了多次，导致一系列的连锁反应。</p>
<p>上述例子就是没有使用模块化开发，造成的全局污染的问题，每个加载的 js 文件都共享变量。当然在实际的项目开发中，可以使用匿名函数自执行的方式，形成独立的块级作用域解决这个问题。</p>
<p>只需要在 home.js 中这么写道：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">name</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//...</span>
    &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c0d219caa62435c83979ce7b0378364~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样小 A 就能正常在 <code>list.js</code> 中获取 name 属性。但是这只是一个 <code>demo</code> ，我们不能保证在实际开发中情况会更加复杂。所以不使用模块开发会暴露出很多风险。</p>
<ul>
<li><strong>依赖管理</strong></li>
</ul>
<p>依赖管理也是一个难以处理的问题。还是如上的例子，正常情况下，执行 js 的先后顺序就是 script 标签排列的前后顺序。那么如何三个 js 之间有依赖关系，那么应该如何处理呢？</p>
<p>假设三个 js 中，都有一个公共方法 <code>fun1</code> ， <code>fun2</code> ， <code>fun3</code>。三者之间的依赖关系如下图所示。</p>
<ul>
<li>下层 js 能调用上层 js 的方法，但是上层 js 无法调用下层 js 的方法。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25612d7905104fd18b3c4c0ea835ebe9~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以就需要模块化来解决上述的问题，今天我们就重点讲解一下前端模块化的两个重要方案：<strong>Commonjs</strong> 和 <strong>Es Module</strong></p>
<h2 data-id="heading-2">三 Commonjs</h2>
<p><code>Commonjs</code> 的提出，弥补 Javascript 对于模块化，没有统一标准的缺陷。nodejs 借鉴了 <code>Commonjs</code> 的 Module ，实现了良好的模块化管理。</p>
<p>目前 <code>commonjs</code> 广泛应用于以下几个场景：</p>
<ul>
<li><code>Node</code> 是 CommonJS 在服务器端一个具有代表性的实现；</li>
<li><code>Browserify</code> 是 CommonJS 在浏览器中的一种实现；</li>
<li><code>webpack</code> 打包工具对 CommonJS 的支持和转换；也就是前端应用也可以在编译之前，尽情使用 CommonJS 进行开发。</li>
</ul>
<h3 data-id="heading-3">1 commonjs 使用与原理</h3>
<p>在使用  规范下，有几个显著的特点。</p>
<ul>
<li>在 <code>commonjs</code> 中每一个 js 文件都是一个单独的模块，我们可以称之为 module；</li>
<li>该模块中，包含 CommonJS 规范的核心变量: exports、module.exports、require；</li>
<li>exports 和 module.exports 可以负责对模块中的内容进行导出；</li>
<li>require 函数可以帮助我们导入其他模块（自定义模块、系统模块、第三方库模块）中的内容；</li>
</ul>
<h4 data-id="heading-4">commonjs 使用初体验</h4>
<p><strong>导出</strong>：我们先尝试这导出一个模块：</p>
<p><strong><code>hello.js</code>中</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> name = <span class="hljs-string">'《React进阶实践指南》'</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayName</span>  (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>导入</strong>：接下来简单的导入：</p>
<p><strong><code>home.js</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sayName = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./hello.js'</span>)
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>:sayName(),
        <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上就是 Commonjs 最简单的实现，那么暴露出两个问题：</p>
<ul>
<li>如何解决变量污染的问题。</li>
<li>module.exports，exports，require 三者是如何工作的？又有什么关系？</li>
</ul>
<h4 data-id="heading-5">commonjs 实现原理</h4>
<p>首先从上述得知每个模块文件上存在 <code>module</code>，<code>exports</code>，<code>require</code>三个变量，然而这三个变量是没有被定义的，但是我们可以在 Commonjs 规范下每一个 js 模块上直接使用它们。在 nodejs 中还存在 <code>__filename</code> 和 <code>__dirname</code> 变量。</p>
<p>如上每一个变量代表什么意思呢：</p>
<ul>
<li><code>module</code> 记录当前模块信息。</li>
<li><code>require</code> 引入模块的方法。</li>
<li><code>exports</code> 当前模块导出的属性</li>
</ul>
<p>在编译的过程中，实际 Commonjs 对 js 的代码块进行了首尾包装， 我们以上述的 home.js 为例子🌰，它被包装之后的样子如下：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">exports</span>,<span class="hljs-built_in">require</span>,<span class="hljs-built_in">module</span>,__filename,__dirname</span>)</span>&#123;
   <span class="hljs-keyword">const</span> sayName = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./hello.js'</span>)
    <span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>:sayName(),
            <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 Commonjs 规范下模块中，会形成一个包装函数，我们写的代码将作为包装函数的执行上下文，使用的 <code>require</code> ，<code>exports</code> ，<code>module</code> 本质上是通过形参的方式传递到包装函数中的。</li>
</ul>
<p>那么包装函数本质上是什么样子的呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapper</span> (<span class="hljs-params">script</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'(function (exports, require, module, __filename, __dirname) &#123;'</span> + 
        script +
     <span class="hljs-string">'\n&#125;)'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>包装函数执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> modulefunction = wrapper(<span class="hljs-string">`
  const sayName = require('./hello.js')
    module.exports = function say()&#123;
        return &#123;
            name:sayName(),
            author:'我不是外星人'
        &#125;
    &#125;
`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上模拟了一个包装函数功能， script 为我们在 js 模块中写的内容，最后返回的就是如上包装之后的函数。当然这个函数暂且是一个字符串。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> runInThisContext(modulefunction)(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">require</span>, <span class="hljs-built_in">module</span>, __filename, __dirname)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在模块加载的时候，会通过 runInThisContext (可以理解成 eval ) 执行 <code>modulefunction</code> ，传入<code>require</code> ，<code>exports</code> ，<code>module</code> 等参数。最终我们写的 nodejs 文件就这么执行了。</li>
</ul>
<p>到此为止，完成了整个模块执行的原理。接下来我们来分析以下 require 文件加载的流程。</p>
<h3 data-id="heading-6">2 require 文件加载流程</h3>
<p>上述说了 commonjs 规范大致的实现原理，接下来我们分析一下， <code>require</code> 如何进行文件的加载的。</p>
<p>我们还是以 nodejs 为参考，比如如下代码片段中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs =      <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)      <span class="hljs-comment">// ①核心模块</span>
<span class="hljs-keyword">const</span> sayName = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./hello.js'</span>)  <span class="hljs-comment">//② 文件模块</span>
<span class="hljs-keyword">const</span> crypto =  <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto-js'</span>)   <span class="hljs-comment">// ③第三方自定义模块</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码片段中：</p>
<ul>
<li>① 为 nodejs 底层的核心模块。</li>
<li>② 为我们编写的文件模块，比如上述 <code>sayName</code></li>
<li>③ 为我们通过 npm 下载的第三方自定义模块，比如 <code>crypto-js</code>。</li>
</ul>
<p>当 require 方法执行的时候，接收的唯一参数作为一个<strong>标识符</strong> ，Commonjs 下对不同的标识符，处理流程不同，但是<strong>目的相同，都是找到对应的模块</strong>。</p>
<h4 data-id="heading-7">require 加载标识符原则</h4>
<p>首先我们看一下 <code> nodejs</code> 中对标识符的处理原则。</p>
<ul>
<li>首先像 fs ，http ，path 等标识符，会被作为 nodejs 的<strong>核心模块</strong>。</li>
<li><code> ./</code> 和 <code>../</code> 作为相对路径的<strong>文件模块</strong>， <code>/</code> 作为绝对路径的<strong>文件模块</strong>。</li>
<li>非路径形式也非核心模块的模块，将作为<strong>自定义模块</strong>。</li>
</ul>
<p><strong>核心模块的处理：</strong></p>
<p>核心模块的优先级仅次于缓存加载，在 <code>Node</code> 源码编译中，已被编译成二进制代码，所以加载核心模块，加载过程中速度最快。</p>
<p><strong>路径形式的文件模块处理：</strong></p>
<p>已 <code>./</code> ，<code>../</code> 和 <code>/</code> 开始的标识符，会被当作文件模块处理。<code>require()</code> 方法会将路径转换成真实路径，并以真实路径作为索引，将编译后的结果缓存起来，第二次加载的时候会更快。至于<strong>怎么缓存</strong>的？我们稍后会讲到。</p>
<p><strong>自定义模块处理：</strong>
自定义模块，一般指的是非核心的模块，它可能是一个文件或者一个包，它的查找会遵循以下原则：</p>
<ul>
<li>在当前目录下的 <code>node_modules</code> 目录查找。</li>
<li>如果没有，在父级目录的 <code>node_modules</code> 查找，如果没有在父级目录的父级目录的 <code>node_modules</code> 中查找。</li>
<li>沿着路径向上递归，直到根目录下的 <code>node_modules</code> 目录。</li>
<li>在查找过程中，会找 <code>package.json</code> 下 main 属性指向的文件，如果没有  <code>package.json</code> ，在 node 环境下会以此查找 <code>index.js</code> ，<code>index.json</code> ，<code>index.node</code>。</li>
</ul>
<p>查找流程图如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfb7a91998774fc78a9813e3b0db8199~tplv-k3u1fbpfcp-watermark.image" alt="4.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3 require 模块引入与处理</h3>
<p>CommonJS 模块同步加载并执行模块文件，CommonJS 模块在执行阶段分析模块依赖，采用<strong>深度优先遍历</strong>（depth-first traversal），执行顺序是父 -> 子 -> 父；</p>
<p>为了搞清除 require 文件引入流程。我们接下来再举一个例子，这里注意一下细节：</p>
<ul>
<li><code>a.js文件</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getMes = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./b'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 a 文件'</span>)
<span class="hljs-built_in">exports</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> message = getMes()
    <span class="hljs-built_in">console</span>.log(message)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>b.js</code>文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> say = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>)
<span class="hljs-keyword">const</span>  object = &#123;
   <span class="hljs-attr">name</span>:<span class="hljs-string">'《React进阶实践指南》'</span>,
   <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 b 文件'</span>)
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> object
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>主文件<code>main.js</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>)
<span class="hljs-keyword">const</span> b = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./b'</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'node 入口文件'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来终端输入 <code>node main.js</code> 运行 <code>main.js</code>，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b728ce249df740ce8b0232a889283f22~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的运行结果可以得出以下结论：</p>
<ul>
<li><code>main.js</code> 和 <code>a.js</code> 模块都引用了 <code>b.js</code> 模块，但是 <code>b.js</code> 模块只执行了一次。</li>
<li><code>a.js</code> 模块 和 <code>b.js</code> 模块互相引用，但是没有造成循环引用的情况。</li>
<li>执行顺序是父 -> 子 -> 父；</li>
</ul>
<p><strong>那么 <code>Common.js</code> 规范是如何实现上述效果的呢？</strong></p>
<h4 data-id="heading-9">require 加载原理</h4>
<p>首先为了弄清楚上述两个问题。我们要明白两个感念，那就是 <code>module</code> 和 <code>Module</code>。</p>
<p><strong><code>module</code></strong> ：在 Node 中每一个 js 文件都是一个 module ，module 上保存了 exports 等信息之外，还有一个 <strong><code>loaded</code></strong> 表示该模块是否被加载。</p>
<ul>
<li>为 <code>false</code> 表示还没有加载；</li>
<li>为 <code>true</code> 表示已经加载</li>
</ul>
<p><strong><code>Module</code></strong> ：以 nodejs 为例，整个系统运行之后，会用 <code>Module</code> 缓存每一个模块加载的信息。</p>
<p>require 的源码大致长如下的样子：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// id 为路径标识符</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">require</span>(<span class="hljs-params">id</span>) </span>&#123;
   <span class="hljs-comment">/* 查找  Module 上有没有已经加载的 js  对象*/</span>
   <span class="hljs-keyword">const</span>  cachedModule = Module._cache[id]
   
   <span class="hljs-comment">/* 如果已经加载了那么直接取走缓存的 exports 对象  */</span>
  <span class="hljs-keyword">if</span>(cachedModule)&#123;
    <span class="hljs-keyword">return</span> cachedModule.exports
  &#125;
 
  <span class="hljs-comment">/* 创建当前模块的 module  */</span>
  <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = &#123; <span class="hljs-attr">exports</span>: &#123;&#125; ,<span class="hljs-attr">loaded</span>: <span class="hljs-literal">false</span> , ...&#125;

  <span class="hljs-comment">/* 将 module 缓存到  Module 的缓存属性中，路径标识符作为 id */</span>  
  Module._cache[id] = <span class="hljs-built_in">module</span>
  <span class="hljs-comment">/* 加载文件 */</span>
  runInThisContext(wrapper(<span class="hljs-string">'module.exports = "123"'</span>))(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">require</span>, <span class="hljs-built_in">module</span>, __filename, __dirname)
  <span class="hljs-comment">/* 加载完成 */</span>/
  <span class="hljs-built_in">module</span>.loaded = <span class="hljs-literal">true</span> 
  <span class="hljs-comment">/* 返回值 */</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面我们总结出一次 <code>require</code> 大致流程是这样的；</p>
<ul>
<li>
<p>require 会接收一个参数——文件标识符，然后分析定位文件，分析过程我们上述已经讲到了，加下来会从 Module 上查找有没有缓存，如果有缓存，那么直接返回缓存的内容。</p>
</li>
<li>
<p>如果没有缓存，会创建一个 module 对象，缓存到 Module 上，然后执行文件，加载完文件，将 loaded 属性设置为 true ，然后返回 module.exports 对象。借此完成模块加载流程。</p>
</li>
<li>
<p>模块导出就是 return 这个变量的其实跟 a = b 赋值一样， 基本类型导出的是值， 引用类型导出的是引用地址。</p>
</li>
<li>
<p>exports 和 module.exports 持有相同引用，因为最后导出的是 module.exports， 所以对 exports 进行赋值会导致 exports 操作的不再是 module.exports 的引用。</p>
</li>
</ul>
<h4 data-id="heading-10">require 避免重复加载</h4>
<p>从上面我们可以直接得出，require 如何避免重复加载的，首先加载之后的文件的 <code>module</code> 会被缓存到 <code>Module</code> 上，比如一个模块已经 require 引入了 a 模块，如果另外一个模块再次引用 a ，那么会直接读取缓存值 module ，所以无需再次执行模块。</p>
<p>对应 demo 片段中，首先 <code>main.js</code> 引用了 <code>a.js</code> ，<code>a.js</code> 中 require 了 <code>b.js</code> 此时 <code>b.js</code> 的 module 放入缓存 <code>Module</code> 中，接下来 <code>main.js</code> 再次引用  <code>b.js</code> ，那么直接走的缓存逻辑。所以 b.js 只会执行一次，也就是在 a.js 引入的时候。</p>
<h4 data-id="heading-11">require 避免循环引用</h4>
<p>那么接下来这个循环引用问题，也就很容易解决了。为了让大家更清晰明白，那么我们接下来一起分析整个流程。</p>
<ul>
<li>① 首先执行 <code>node main.js</code> ，那么开始执行第一行 <code>require(a.js)</code>；</li>
<li>② 那么首先判断 <code>a.js</code> 有没有缓存，因为没有缓存，先加入缓存，然后执行文件 a.js （<strong>需要注意 是先加入缓存， 后执行模块内容</strong>）;</li>
<li>③ a.js 中执行第一行，引用 b.js。</li>
<li>④ 那么判断 <code>b.js</code> 有没有缓存，因为没有缓存，所以加入缓存，然后执行 b.js 文件。</li>
<li>⑤ b.js 执行第一行，再一次循环引用 <code>require(a.js)</code> 此时的 a.js 已经加入缓存，直接读取值。接下来打印 <code>console.log('我是 b 文件')</code>，导出方法。</li>
<li>⑥ b.js 执行完毕，回到 a.js 文件，打印 <code>console.log('我是 a 文件')</code>，导出方法。</li>
<li>⑦ 最后回到 <code>main.js</code>，打印 <code>console.log('node 入口文件')</code> 完成这个流程。</li>
</ul>
<p>不过这里我们要注意问题：</p>
<ul>
<li>如上第 ⑤ 的时候，当执行 b.js 模块的时候，因为 a.js 还没有导出 <code>say</code> 方法，所以 b.js 同步上下文中，获取不到 say。</li>
</ul>
<p>我用一幅流程图描述上述过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a2084aa55764fa493a7b82dfe2f2d50~tplv-k3u1fbpfcp-watermark.image" alt="15.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了进一步验证上面所说的，我们改造一下 <code>b.js</code> 如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> say = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>)
<span class="hljs-keyword">const</span>  object = &#123;
   <span class="hljs-attr">name</span>:<span class="hljs-string">'《React进阶实践指南》'</span>,
   <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 b 文件'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'打印 a 模块'</span> , say)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'异步打印 a 模块'</span> , say)
&#125;,<span class="hljs-number">0</span>)

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> object
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed8226a606004fd5a2621ca4a40a9997~tplv-k3u1fbpfcp-watermark.image" alt="6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第一次打印 say 为空对象。</li>
<li>第二次打印 say 才看到 b.js 导出的方法。</li>
</ul>
<p>那么如何获取到 say 呢，有两种办法：</p>
<ul>
<li>一是用动态加载 a.js 的方法，马上就会讲到。</li>
<li>二个就是如上放在异步中加载。</li>
</ul>
<p>我们注意到 a.js 是用 <code>exports.say</code> 方式导出的，如果 a.js 用 module.exports 结果会有所不同。至于有什么不同，为什么？我接下来会讲到。</p>
<h3 data-id="heading-12">4 require 动态加载</h3>
<p>上述我们讲了 <code>require</code> 查找文件和加载流程。接下来介绍 <code>commonjs</code> 规范下的 require 的另外一个特性——<strong>动态加载</strong>。</p>
<p>require 可以在任意的上下文，动态加载模块。我对上述 a.js 修改。</p>
<p><code>a.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 a 文件'</span>)
<span class="hljs-built_in">exports</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> getMes = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./b'</span>)
    <span class="hljs-keyword">const</span> message = getMes()
    <span class="hljs-built_in">console</span>.log(message)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>main.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>)
a.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上在 a.js 模块的 say 函数中，用 require 动态加载 b.js 模块。然后执行在 main.js 中执行 a.js 模块的 say 方法。</li>
</ul>
<p>打印结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a7b73ebb16c46d98f8708d87d79134a~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>require 本质上就是一个函数，那么函数可以在任意上下文中执行，来自由地加载其他模块的属性方法。</p>
<h3 data-id="heading-13">5 exports 和 module.exports</h3>
<p>系统分析完 <code>require</code> ，接下来我们分析一下，<code>exports</code> 和 <code>module.exports</code>，首先看一下两个的用法。</p>
<h4 data-id="heading-14">exports 使用</h4>
<p><strong>第一种方式：exports</strong>
<code>a.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.name = <span class="hljs-string">`《React进阶实践指南》`</span>
<span class="hljs-built_in">exports</span>.author = <span class="hljs-string">`我不是外星人`</span>
<span class="hljs-built_in">exports</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">666</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>引用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>)
<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>打印结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7522749385e44689893d19b7cc4d999~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>exports 就是传入到当前模块内的一个对象，本质上就是 <code>module.exports</code>。</li>
</ul>
<p><strong>问题：为什么 exports=&#123;&#125; 直接赋值一个对象就不可以呢？</strong> 比如我们将如上 <code>a.js</code> 修改一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>=&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'《React进阶实践指南》'</span>,
    <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">666</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>打印结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/532dcd2a40e345c594b3baa7077c428a~tplv-k3u1fbpfcp-watermark.image" alt="9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>理想情况下是通过 <code> exports = &#123;&#125;</code> 直接赋值，不需要在  <code>exports.a = xxx</code>  每一个属性，但是如上我们看到了这种方式是无效的。为什么会这样？实际这个是 js 本身的特性决定的。</p>
<p>通过上述讲解都知道 exports ， module 和 require 作为形参的方式传入到 js 模块中。我们直接 <code> exports = &#123;&#125;</code>  修改 exports ，等于重新赋值了形参，那么会重新赋值一份，但是不会在引用原来的形参。举一个简单的例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrap</span> (<span class="hljs-params">myExports</span>)</span>&#123;
    myExports=&#123;
       <span class="hljs-attr">name</span>:<span class="hljs-string">'我不是外星人'</span>
   &#125;
&#125;

<span class="hljs-keyword">let</span> myExports = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'alien'</span>
&#125;
wrap(myExports)
<span class="hljs-built_in">console</span>.log(myExports)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>打印：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4d6d42ff5943faa4b4c5e034728906~tplv-k3u1fbpfcp-watermark.image" alt="10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们期望修改 myExports ，但是没有任何作用。</p>
<p>假设 <code>wrap</code> 就是 Commonjs 规范下的包装函数，我们的 js 代码就是包装函数内部的内容。当我们把  myExports 对象传进去，但是直接赋值 <code> myExports = &#123; name:'我不是外星人' &#125;</code> 没有任何作用，相等于内部重新声明一份 <code>myExports</code> 而和外界的 myExports 断绝了关系。所以解释了为什么不能 <code>exports=&#123;...&#125; </code> 直接赋值。</p>
<p>那么解决上述也容易，只需要函数中像 exports.name 这么写就可以了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrap</span> (<span class="hljs-params">myExports</span>)</span>&#123;
    myExports.name=<span class="hljs-string">'我不是外星人'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>打印：</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e423f263ad8d47c991744e88534a4066~tplv-k3u1fbpfcp-watermark.image" alt="11.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">module.exports 使用</h4>
<p>module.exports 本质上就是 exports ，我们用 module.exports 来实现如上的导出。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports =&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'《React进阶实践指南》'</span>,
    <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">666</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module.exports 也可以单独导出一个函数或者一个类。比如如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述 <code>require</code> 原理实现中，我们知道了 exports 和 module.exports 持有相同引用，因为最后导出的是 module.exports 。那么这就说明在一个文件中，我们最好选择 <code>exports</code> 和 <code>module.exports</code> 两者之一，如果两者同时存在，很可能会造成覆盖的情况发生。比如如下情况：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.name = <span class="hljs-string">'alien'</span> <span class="hljs-comment">// 此时 exports.name 是无效的</span>
<span class="hljs-built_in">module</span>.exports =&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'《React进阶实践指南》'</span>,
    <span class="hljs-attr">author</span>:<span class="hljs-string">'我不是外星人'</span>,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">666</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>上述情况下 exports.name 无效，会被 <code>module.exports</code> 覆盖。</li>
</ul>
<h4 data-id="heading-16">Q & A</h4>
<p>1 那么问题来了？ <strong>既然有了 <code>exports</code>，为何又出了 <code>module.exports </code>?</strong></p>
<p>答：如果我们不想在 commonjs 中导出对象，而是只导出一个<strong>类或者一个函数</strong>再或者其他属性的情况，那么 <code>module.exports</code> 就更方便了，如上我们知道 <code>exports</code> 会被初始化成一个对象，也就是我们只能在对象上绑定属性，但是我们可以通过 <code>module.exports</code> 自定义导出出对象外的其他类型元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-built_in">module</span>.exports = a <span class="hljs-comment">// 导出函数</span>

<span class="hljs-built_in">module</span>.exports = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>] <span class="hljs-comment">// 导出数组</span>

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">//导出方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2 与 <code>exports</code> 相比，<code>module.exports</code> 有什么缺陷 ？</p>
<p>答：<code>module.exports</code> 当导出一些函数等非对象属性的时候，也有一些风险，就比如循环引用的情况下。对象会保留相同的内存地址，就算一些属性是后绑定的，也能间接通过异步形式访问到。但是如果 module.exports 为一个非对象其他属性类型，在循环引用的时候，就容易造成属性丢失的情况发生了。</p>
<h2 data-id="heading-17">四 Es Module</h2>
<p><code>Nodejs</code> 借鉴了 <code>Commonjs</code> 实现了模块化 ，从 <code>ES6</code> 开始， <code>JavaScript</code> 才真正意义上有自己的模块化规范，</p>
<p>Es Module 的产生有很多优势，比如:</p>
<ul>
<li>借助 <code>Es Module</code> 的静态导入导出的优势，实现了 <code>tree shaking</code>。</li>
<li><code>Es Module</code> 还可以 <code>import()</code> 懒加载方式实现代码分割。</li>
</ul>
<p>在 <code>Es Module</code> 中用 <code>export</code> 用来导出模块，<code>import</code> 用来导入模块。但是 <code>export</code> 配合 <code>import</code> 会有很多种组合情况，接下来我们逐一分析一下。</p>
<h3 data-id="heading-18">导出 export 和导入 import</h3>
<p>所有通过 export 导出的属性，在 import 中可以通过结构的方式，解构出来。</p>
<p><strong>export 正常导出，import 导入</strong></p>
<p>导出模块：<code>a.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name = <span class="hljs-string">'《React进阶实践指南》'</span> 
<span class="hljs-keyword">const</span> author = <span class="hljs-string">'我不是外星人'</span>
<span class="hljs-keyword">export</span> &#123; name, author &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello , world'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入模块：<code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// name , author , say 对应 a.js 中的  name , author , say</span>
<span class="hljs-keyword">import</span> &#123; name , author , say &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>export &#123; &#125;， 与变量名绑定，命名导出。</li>
<li>import &#123; &#125; from 'module'， 导入 <code>module</code> 的命名导出 ，module 为如上的 <code>./a.js</code></li>
<li>这种情况下 import &#123; &#125; 内部的变量名称，要与 export &#123; &#125; 完全匹配。</li>
</ul>
<p><strong>默认导出 export default</strong></p>
<p>导出模块：<code>a.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name = <span class="hljs-string">'《React进阶实践指南》'</span>
<span class="hljs-keyword">const</span> author = <span class="hljs-string">'我不是外星人'</span>
<span class="hljs-keyword">const</span> say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello , world'</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    name,
    author,
    say
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入模块：<code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> mes <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>
<span class="hljs-built_in">console</span>.log(mes) <span class="hljs-comment">//&#123; name: '《React进阶实践指南》',author:'我不是外星人', say:Function &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>export default anything</code> 导入 module 的默认导出。 <code>anything</code> 可以是函数，属性方法，或者对象。</li>
<li>对于引入默认导出的模块，<code>import anyName from 'module'</code>， anyName 可以是自定义名称。</li>
</ul>
<p><strong>混合导入｜导出</strong></p>
<p>ES6 module 可以使用 export default 和 export 导入多个属性。</p>
<p>导出模块：<code>a.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> name = <span class="hljs-string">'《React进阶实践指南》'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> author = <span class="hljs-string">'我不是外星人'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello , world'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入模块：<code>main.js</code> 中有几种导入方式：</p>
<p>第一种：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> theSay , &#123; name, author <span class="hljs-keyword">as</span>  bookAuthor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>
<span class="hljs-built_in">console</span>.log(
    theSay,     <span class="hljs-comment">// ƒ say() &#123;console.log('hello , world') &#125;</span>
    name,       <span class="hljs-comment">// "《React进阶实践指南》"</span>
    bookAuthor  <span class="hljs-comment">// "我不是外星人"</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> theSay, * <span class="hljs-keyword">as</span> mes <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>
<span class="hljs-built_in">console</span>.log(
    theSay, <span class="hljs-comment">// ƒ say() &#123; console.log('hello , world') &#125;</span>
    mes <span class="hljs-comment">// &#123; name:'《React进阶实践指南》' , author: "我不是外星人" ，default:  ƒ say() &#123; console.log('hello , world') &#125; &#125;</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>导出的属性被合并到 <code>mes</code> 属性上， <code>export</code> 被导入到对应的属性上，<code>export default</code> 导出内容被绑定到 <code>default</code> 属性上。 <code>theSay</code> 也可以作为被 <code>export default</code> 导出属性。</li>
</ul>
<p><strong>重属名导入</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; bookName <span class="hljs-keyword">as</span> name, say, bookAuthor <span class="hljs-keyword">as</span> author &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span>
<span class="hljs-built_in">console</span>.log( bookName , bookAuthor , say ) <span class="hljs-comment">//《React进阶实践指南》 我不是外星人</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>从 module 模块中引入 name ，并重命名为 bookName ，从 module 模块中引入 author ，并重命名为 bookAuthor。 然后在当前模块下，使用被重命名的名字。</li>
</ul>
<p><strong>重定向导出</strong></p>
<p>可以把当前模块作为一个中转站，一方面引入 module 内的属性，然后把属性再给导出去。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span> <span class="hljs-comment">// 第一种方式</span>
<span class="hljs-keyword">export</span> &#123; name, author, ..., say &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span> <span class="hljs-comment">// 第二种方式</span>
<span class="hljs-keyword">export</span> &#123; bookName <span class="hljs-keyword">as</span> name, bookAuthor <span class="hljs-keyword">as</span> author, ..., say &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span> <span class="hljs-comment">//第三种方式</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第一种方式：重定向导出 module 中的所有导出属性， 但是不包括 <code>module</code> 内的 <code>default</code> 属性。</li>
<li>第二种方式：从 module 中导入 name ，author ，say 再以相同的属性名，导出。</li>
<li>第三种方式：从 module 中导入 name ，重属名为 bookName 导出，从 module 中导入 author ，重属名为 bookAuthor 导出，正常导出 say 。</li>
</ul>
<p><strong>无需导入模块，只运行模块</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">'module'</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行 module 不导出值  多次调用 <code>module</code> 只运行一次。</li>
</ul>
<p><strong>动态导入</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">import</span>(<span class="hljs-string">'module'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>import('module') </code>，动态导入返回一个 <code>Promise</code>。为了支持这种方式，需要在 webpack 中做相应的配置处理。</li>
</ul>
<h3 data-id="heading-19">ES6 module 特性</h3>
<p>接下来我们重点分析一下 ES6 module 一些重要特性。</p>
<h4 data-id="heading-20">1 静态语法</h4>
<p>ES6 module 的引入和导出是静态的，<code>import</code> 会自动提升到代码的顶层 ，<code>import</code> , <code>export</code> 不能放在块级作用域或条件语句中。</p>
<p>🙅错误写法一：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">import</span> name <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>  
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> author = <span class="hljs-string">'我不是外星人'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>🙅错误写法二：</p>
<pre><code class="hljs language-js copyable" lang="js">isexport &&  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span>  name = <span class="hljs-string">'《React进阶实践指南》'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种静态语法，在编译过程中确定了导入和导出的关系，所以更方便去查找依赖，更方便去 <code>tree shaking</code> (摇树) ， 可以使用 lint 工具对模块依赖进行检查，可以对导入导出加上类型信息进行静态的类型检查。</p>
<p>import 的导入名不能为字符串或在判断语句，下面代码是错误的</p>
<p>🙅错误写法三：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">'defaultExport'</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span>

<span class="hljs-keyword">let</span> name = <span class="hljs-string">'Export'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'default'</span> + name <span class="hljs-keyword">from</span> <span class="hljs-string">'module'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">2 执行特性</h4>
<p>ES6 module 和 Common.js 一样，对于相同的 js 文件，会保存静态属性。</p>
<p>但是与 Common.js 不同的是 ，<code>CommonJS </code> 模块同步加载并执行模块文件，ES6 模块提前加载并执行模块文件，ES6 模块在预处理阶段分析模块依赖，在执行阶段执行模块，两个阶段都采用深度优先遍历，执行顺序是子 -> 父。</p>
<p>为了验证这一点，看一下如下 demo。</p>
<p><strong><code>main.js</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'main.js开始执行'</span>)
<span class="hljs-keyword">import</span> say <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>
<span class="hljs-keyword">import</span> say1 <span class="hljs-keyword">from</span> <span class="hljs-string">'./b'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'main.js执行完毕'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>a.js</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> b <span class="hljs-keyword">from</span> <span class="hljs-string">'./b'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a模块加载'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello , world'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>b.js</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b模块加载'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayhello</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello,world'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>main.js</code> 和 <code>a.js</code> 都引用了 <code>b.js</code> 模块，但是 b 模块也只加载了一次。</li>
<li>执行顺序是子 -> 父</li>
</ul>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97075c8d67824c42b4dc7bcb535cc903~tplv-k3u1fbpfcp-watermark.image" alt="12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">3 导出绑定</h4>
<p><strong>不能修改import导入的属性</strong></p>
<p><code>a.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> num = <span class="hljs-number">1</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addNumber = <span class="hljs-function">()=></span>&#123;
    num++
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>main.js</code>中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;  num , addNumber &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>
num = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果直接修改，那么会报错。如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535dba214af349c9900193e60ad0364d~tplv-k3u1fbpfcp-watermark.image" alt="14.jpg" loading="lazy" referrerpolicy="no-referrer">
<strong>属性绑定</strong></p>
<p>所以可以在 <code>main.js</code> 中这么修改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;  num , addNumber &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>

<span class="hljs-built_in">console</span>.log(num) <span class="hljs-comment">// num = 1</span>
addNumber()
<span class="hljs-built_in">console</span>.log(num) <span class="hljs-comment">// num = 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上属性 num 的导入是绑定的。</li>
</ul>
<p>接下来对 import 属性作出总结：</p>
<ul>
<li>使用 import 被导入的模块运行在严格模式下。</li>
<li>使用 import 被导入的变量是只读的，可以理解默认为 const 装饰，无法被赋值</li>
<li>使用 import 被导入的变量是与原变量绑定/引用的，可以理解为 import 导入的变量无论是否为基本类型都是引用传递。</li>
</ul>
<h3 data-id="heading-23">import() 动态引入</h3>
<p><code>import()</code> 返回一个 <code>Promise</code> 对象， 返回的 <code>Promise</code> 的 then 成功回调中，可以获取模块的加载成功信息。我们来简单看一下 <code>import()</code> 是如何使用的。</p>
<p><code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> result  = <span class="hljs-keyword">import</span>(<span class="hljs-string">'./b'</span>)
    result.then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
        <span class="hljs-built_in">console</span>.log(res)
    &#125;)
&#125;, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>b.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> name =<span class="hljs-string">'alien'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayhello</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello,world'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480e4d9ba47048b6a286e2d791f8378c~tplv-k3u1fbpfcp-watermark.image" alt="13.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从打印结果可以看出 <code>import()</code>的基本特性。</p>
<ul>
<li><code>import()</code> 可以动态使用，加载模块。</li>
<li><code>import()</code> 返回一个 <code>Promise</code> ，成功回调 then 中可以获取模块对应的信息。 <code>name</code> 对应 name 属性， <code>default</code> 代表 <code>export default</code> 。<code>__esModule</code> 为 es module 的标识。</li>
</ul>
<h4 data-id="heading-24">import() 可以做一些什么</h4>
<p><strong>动态加载</strong></p>
<ul>
<li>首先 <code>import()</code> 动态加载一些内容，可以放在条件语句或者函数执行上下文中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(isRequire)&#123;
    <span class="hljs-keyword">const</span> result  = <span class="hljs-keyword">import</span>(<span class="hljs-string">'./b'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>懒加载</strong></p>
<ul>
<li><code>import()</code> 可以实现懒加载，举个例子 vue 中的路由懒加载；</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">[
   &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'home'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'首页'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">()=></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./home'</span>) ,
   &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>React中动态加载</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> LazyComponent =  React.lazy(<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'./text'</span>))
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;   
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span> <<span class="hljs-attr">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"icon"</span>></span><span class="hljs-tag"><<span class="hljs-name">SyncOutlinespin</span>/></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span> &#125; >
               <span class="hljs-tag"><<span class="hljs-name">LazyComponent</span> /></span>
           <span class="hljs-tag"></<span class="hljs-name">React.Suspense</span>></span></span>
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>React.lazy</code> 和 <code>Suspense</code> 配合一起用，能够有动态加载组件的效果。<code>React.lazy</code> 接受一个函数，这个函数需要动态调用 <code>import()</code> 。</p>
<p><code>import()</code> 这种加载效果，可以很轻松的实现<strong>代码分割</strong>。避免一次性加载大量 js 文件，造成首次加载白屏时间过长的情况。</p>
<h3 data-id="heading-25">tree shaking 实现</h3>
<p>Tree Shaking 在 Webpack 中的实现，是用来尽可能的删除没有被使用过的代码，一些被 import 了但其实没有被使用的代码。比如以下场景：</p>
<p><code>a.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> num = <span class="hljs-number">1</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addNumber = <span class="hljs-function">()=></span>&#123;
    num++
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> delNumber = <span class="hljs-function">()=></span>&#123;
    num--
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>main.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;  addNumber &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>
addNumber()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如上 <code>a.js</code> 中暴露两个方法，<code>addNumber</code>和 <code>delNumber</code>，但是整个应用中，只用到了 <code>addNumber</code>，那么构建打包的时候，<code>delNumber</code>将作为没有引用的方法，不被打包进来。</li>
</ul>
<h2 data-id="heading-26">五 Commonjs 和 Es Module 总结</h2>
<p>接下来贯穿全文，讲一下 <code>Commonjs</code> 和 <code>Es Module</code> 的特性。</p>
<h3 data-id="heading-27">Commonjs 总结</h3>
<p><code>Commonjs</code> 的特性如下：</p>
<ul>
<li>CommonJS 模块由 JS 运行时实现。</li>
<li>CommonJs 是单个值导出，本质上导出的就是 exports 属性。</li>
<li>CommonJS 是可以动态加载的，对每一个加载都存在缓存，可以有效的解决循环引用问题。</li>
<li>CommonJS 模块同步加载并执行模块文件。</li>
</ul>
<h3 data-id="heading-28">es module 总结</h3>
<p><code>Es module</code> 的特性如下：</p>
<ul>
<li>ES6 Module 静态的，不能放在块级作用域内，代码发生在编译时。</li>
<li>ES6 Module 的值是动态绑定的，可以通过导出方法修改，可以直接访问修改结果。</li>
<li>ES6 Module 可以导出多个属性和方法，可以单个导入导出，混合导入导出。</li>
<li>ES6 模块提前加载并执行模块文件，</li>
<li>ES6 Module 导入模块在严格模式下。</li>
<li>ES6 Module 的特性可以很容易实现 Tree Shaking 和 Code Splitting。</li>
</ul>
<h2 data-id="heading-29">六 总结</h2>
<p>本文详细讲解了 Commonjs 和 Es Module ，希望阅读的同学能对前端模块化的实现有更深入的认识。吃透本文，能够轻松应付  Commonjs 和 Es Module 的面试知识点。</p>
<p>如果这篇文章对你有帮助，希望能给笔者 <strong>点赞+收藏</strong> 以此鼓励作者继续创作前端硬核文章。也可以关注作者公众号 <strong>前端Sharing</strong> 第一时间推送前端好文。</p>
<h3 data-id="heading-30">参考文献</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000017878394" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000017878394" ref="nofollow noopener noreferrer">深入 CommonJs 与 ES6 Module</a></li>
<li><a href="https://juejin.cn/post/6892786383249735687" target="_blank" title="https://juejin.cn/post/6892786383249735687">「Node.js系列」深入浅出Node模块化开发——CommonJS规范</a></li>
</ul>
<h3 data-id="heading-31">小册完结撒花，是终点亦是起点～</h3>
<p><strong>系统学习 React 的掘金小册——《React进阶实践指南》已经完结啦～</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/491a1a2e509b4d2c892f68e64864be36~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是终点亦是起点,  小册内容将持续更新，随着 React 版本升级持续维护，并有持续更新章节～</p>
<p>提前透露，<strong>小册接下来会补充：<code>React context</code> 原理部分，内容补充到第八章。</strong></p>
<p>奉上几个小册 7 折 优惠码  <strong>F3Z1VXtv</strong> ，先到先得哦～</p></div>  
</div>
            