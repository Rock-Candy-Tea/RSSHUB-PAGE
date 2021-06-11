
---
title: 'require() 方法详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfce144c10ce41e2a27c6db075dcc5ae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 01:32:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfce144c10ce41e2a27c6db075dcc5ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>在 NodeJS 中有一个方法是我们使用频率最高的，那就是 require 方法。NodeJs 遵循 CommonJS 规范，该规范的核心是通过 require来加载其他依赖的模块。</p>
<h2 data-id="heading-0">几个问题</h2>
<ol>
<li>module.exports 或者 exports 是全局变量吗？</li>
<li>模块的加载是同步还是异步？</li>
<li>循环引用会不会产生性能问题或者导致错误？</li>
</ol>
<h2 data-id="heading-1">什么是 CommonJS</h2>
<p>每一个文件就是一个模块，拥有自己独立的作用域，变量，以及方法等，对其他的模块都不可见。CommonJS 规范规定，每个模块内部，module  变量代表当前模块。这个变量是一个对象，它的 exports 属性（即<code>module.exports</code>）是对外的接口。</p>
<h2 data-id="heading-2">Node 模块的分类</h2>
<ol>
<li><strong>build-in modules</strong> —— Nodejs 中以 C++ 形式提供的模块。</li>
<li><strong>constant module</strong> —— Nodejs 中定义常量的模块。</li>
<li><strong>native module</strong> —— Nodejs 中以 javascript 形式提供的模块。</li>
<li><strong>第三方module</strong> —— 由第三方提供的模块。</li>
</ol>
<h2 data-id="heading-3">module 对象</h2>
<p>NodeJs 内部提供一个 Module 构建函数。所有模块都是 Module 的实例。</p>
<p>每个模块内部，都有一个 module 对象，代表当前模块。它有以下属性。</p>
<ul>
<li>
<p>module 对象的属性</p>
<ul>
<li><code>module.id</code> 模块的识别符，通常是带有绝对路径的模块文件名。</li>
<li><code>module.filename</code> 模块的文件名，带有绝对路径。</li>
<li><code>module.loaded</code> 返回一个布尔值，表示模块是否已经完成加载。</li>
<li><code>module.parent</code> 返回一个对象，表示调用该模块的模块（程序入口文件的module.parent为null）</li>
<li><code>module.children</code> 返回一个数组，表示该模块要用到的其他模块。</li>
<li><code>module.exports</code> 表示模块对外输出的值。</li>
</ul>
</li>
<li>
<p>module.exports 属性
<code>module.exports</code>属性表示当前模块对外输出的接口，其他文件加载该模块，实际上就是读取<code>module.exports</code>变量。<code>module.exports</code>属性表示当前模块对外输出的接口，其他文件加载该模块，实际上就是读取<code>module.exports</code>变量。</p>
</li>
<li>
<p>exports 变量</p>
</li>
</ul>
<p>我们有时候会这么写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// test.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(test);
&#125;
<span class="hljs-keyword">export</span>.test = test;

<span class="hljs-comment">// result.js</span>
<span class="hljs-keyword">const</span> test = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./test"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样也可以拿到正确的结果，这是因为：exports 变量指向 module.exports。这等同在每个模块头部，有一行这样的命令。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> <span class="hljs-built_in">exports</span> = <span class="hljs-built_in">module</span>.exports;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：不能直接给  exports  变量赋值，这样会改变  exports 的指向，不再指向 module.exports。在其他模块使用 require 方法是拿不到赋给 exports 的值的，因为  <strong>require 方法获取的是其他模块的 module.exports 的值</strong>。</p>
<p>建议：尽可能的使用 <code>module.exports</code> 来导出结果。</p>
<h2 data-id="heading-4">模块的流程</h2>
<ul>
<li>创建模块</li>
<li>导出模块</li>
<li>加载模块</li>
<li>使用模块</li>
</ul>
<h2 data-id="heading-5">require 方法</h2>
<blockquote>
<p>require 是 node 用来加载并执行其它文件导出的模块的方法。</p>
<p>在 NodeJs 中，我们引入的任何一个模块都对应一个 Module 实例，包括入口文件。</p>
</blockquote>
<p>完整步骤：</p>
<ol>
<li>
<p>调用父模块的 require 方法（父模块是指调用模块的当前模块）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span> = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">require</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">return</span> mod.require(path);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>调用 Module 的 _load 方法</p>
</li>
<li>
<p>通过 <code>Module._resolveFilename</code> 获取模块的路径 fileName</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> filename = Module._resolveFilename(request, parent, isMain);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>根据 fileName 判断是否存在该模块的缓存</p>
<ul>
<li>如果存在缓存，则调用 <code>updateChildren</code> 方法在更新缓存内容，并返回缓存</li>
<li>如果不存在缓存，则继续执行</li>
</ul>
</li>
<li>
<p>当做原生模块，调用 <code>loadNativeModule</code> 方法进行加载</p>
<ul>
<li>如果加载成功，则返回该原生模块</li>
<li>否则，继续执行</li>
</ul>
</li>
<li>
<p>根据当前模块名（路径）和父模块对象生成一个 Module 实例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = cachedModule || <span class="hljs-keyword">new</span> Module(filename, parent);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>再判断该模块是否是入口文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (isMain) &#123;
    process.mainModule = <span class="hljs-built_in">module</span>;
    <span class="hljs-built_in">module</span>.id = <span class="hljs-string">'.'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>将该模块的实例存入到 Module 的缓存中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Module._cache[filename] = <span class="hljs-built_in">module</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfce144c10ce41e2a27c6db075dcc5ae~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>该模块的实例调用自身的 <code>load</code> 方法，根据 fileName 加载模块</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.load(filename);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取该模块文件的后缀名称</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> extension = findLongestRegisteredExtension(filename);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果后缀名称是ES Module格式的（.mjs），则判断Module是否支持.mjs文件的解析，如果不支持，则抛出异常。</p>
</li>
<li>
<p>根据后缀名称解析模块文件内容</p>
<pre><code class="copyable">Module._extensions[extension](this, filename);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>根据fileName读取文件内容</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">content = fs.readFileSync(filename, <span class="hljs-string">'utf8'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>编译并执行读取到的文件，调用 module 自身的 <code>_complile</code> 方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>._compile(content, filename);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_compile</code> 主要内容步骤：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> compiledWrapper = wrapSafe(filename, content, <span class="hljs-built_in">this</span>);
<span class="hljs-keyword">const</span> dirname = path.dirname(filename);
<span class="hljs-keyword">const</span> <span class="hljs-built_in">require</span> = makeRequireFunction(<span class="hljs-built_in">this</span>, redirects);
<span class="hljs-keyword">let</span> result;
<span class="hljs-keyword">const</span> <span class="hljs-built_in">exports</span> = <span class="hljs-built_in">this</span>.exports;
<span class="hljs-keyword">const</span> thisValue = <span class="hljs-built_in">exports</span>;
<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = <span class="hljs-built_in">this</span>;
result = compiledWrapper.call(thisValue, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">require</span>, <span class="hljs-built_in">module</span>, filename, dirname);
<span class="hljs-keyword">return</span> result;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>wrapSafe</code>方法的返回值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65995afe94de4699b3df0b81c87c6e17~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体获得上图结果的代码是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> wrapper = Module.wrap(content);
<span class="hljs-keyword">return</span> vm.runInThisContext(wrapper, &#123;
    filename,
    <span class="hljs-attr">lineOffset</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">displayErrors</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">importModuleDynamically</span>: <span class="hljs-keyword">async</span> (specifier) => &#123;
        <span class="hljs-keyword">const</span> loader = asyncESM.ESMLoader;
        <span class="hljs-keyword">return</span> loader.import(specifier, normalizeReferrerURL(filename));
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>修改该模块的加载状态为true</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.loaded = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>加载成功。</p>
</li>
</ol>
<h2 data-id="heading-6">总结</h2>
<p>通过上面的调试过程可得出以下结论：</p>
<ol>
<li>在NodeJs中，从入口文件开始，<strong>一切皆 Module</strong>。</li>
<li>模块的加载是同步的。</li>
<li>由于缓存机制的存在，模块的循环引用对性能的影响微乎其微，并且循环引用到的模块可能是不完整的，并且可能会导致错</li>
<li>require 查找模块的流程如下：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1d58c640b8c43cc810f1a235623ac2a~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>文件路径的解析流程图如下：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0332096c1e554ac29b8bed5f76bc322c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><del>本文完</del></p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好！我是〖编程三昧〗的作者 <strong>隐逸王</strong>，我的公众号是『编程三昧』，欢迎关注，希望大家多多指教！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            