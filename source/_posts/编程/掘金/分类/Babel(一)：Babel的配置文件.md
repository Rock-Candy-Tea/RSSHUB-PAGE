
---
title: 'Babel(一)：Babel的配置文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5303'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:07:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=5303'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Babel 是什么？</h2>
<p>Babel 是一个工具链，可以用于把 ES6 + 语法编写的代码转换为向后兼容的 JavaScript 语法，以便可以运行在当前和旧版本的浏览器或者其他环境中。</p>
<h3 data-id="heading-1">Babel 可以做哪些事呢？</h3>
<ul>
<li>语法转换</li>
<li>源码转换</li>
<li>通过 Polyfill 方式在目标环境中添加缺失的特性，如 <code>core-js</code></li>
<li>......</li>
</ul>
<h2 data-id="heading-2">Babel 的配置文件</h2>
<h3 data-id="heading-3">配置文件类型</h3>
<p>Babel 有两种并行的配置文件格式，可以一起使用，也可以独立使用。</p>
<ul>
<li>项目范围的配置
<ul>
<li>babel.config.json 文件，具有不同的扩展名(<code>.js</code>, <code>.cjs</code>, <code>.mjs</code>)</li>
</ul>
</li>
<li>文件相关配置
<ul>
<li>.babelrc.json 文件,，具有不同的扩展名(<code>.babelrc</code>, <code>.js</code>, <code>.cjs</code>, <code>.mjs</code>)</li>
<li>package.json 带 'babel' 秘钥的文件</li>
</ul>
</li>
</ul>
<h4 data-id="heading-4">项目范围的配置</h4>
<p>Babel 有一个 <strong><code>根目录</code></strong> 的概念，默认是当前的工作目录。Babel 将在此根目录自动搜索 <code>babel.config.json</code>；或者用户可以使用显示的 <code>configFile</code> 值来覆盖默认的配置文件搜索行为。</p>
<p>因为项目范围的配置文件和配置文件的物理位置是分开的，所以对于必须广泛应用的配置来说，它们是理想的，甚至允许插件和预置轻松地应用于 <code>node_module</code> 或符号链接包中的文件，这在 Babel 6.x 中配置是相当难受的。</p>
<p>但是项目范围的配置缺点就是：它依赖于工作目录，如果工作目录不是 <code>monorepo</code> 根目录，那么使用它会更难受。</p>
<p>我们也可以将 <code>configFile</code> 设置为 false</p>
<h4 data-id="heading-5">文件相关配置</h4>
<p>Babel 通过从正在编译的 <code>filename</code> 开始搜索目录结构 <code>.babelrc.json</code> 来加载文件。它可以运行你为包的子部分单独创建独立的配置。</p>
<p>文件相关的配置也被合并到项目范围的配置值之上，这使得它们可能对待特定的覆盖有用，尽管这也可以通过 <code>overrides</code> 来完成。</p>
<p>使用文件相关配置时需要注意的一些细节：</p>
<ul>
<li>一旦 <code>package.json</code> 找到包含 <code>a</code> 的目录，搜索将停止，因此相对配置仅适用于单个包</li>
<li>正在编译的 <code>filename</code> 必须在 <code>babelrcRoots</code> 包内，否则将停止搜索</li>
<li><code>.babelrc.json</code> 文件仅适用于它们自己的包内文件</li>
<li><code>.babelrc.json</code> 除非自己选择使用 <code>babelrcRoots</code>，否则包中不是 <code>Babel root</code> 的文件将被忽略</li>
</ul>
<h4 data-id="heading-6">根据使用场景来选择什么配置文件</h4>
<ol>
<li>如果你采用的是 <code>monorepo</code> 模式或者需要编译 <code>node_modules</code>：
<blockquote>
<p>使用 <code>babel.config.json</code> 更加适合</p>
</blockquote>
</li>
<li>如果你的配置文件只适用项目的某个部分：
<blockquote>
<p>使用 <code>.babelrc.json</code> 更好</p>
</blockquote>
</li>
</ol>
<blockquote>
<p>注：但是我们还是建议使用 <code>babel.config.json</code> 的配置文件。</p>
</blockquote>

<h2 data-id="heading-7">配置函数API</h2>
<p>js配置文件可以导出一个函数，该函数将被传递给配置函数API：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-params">api</span> =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 api 对象公开了 Babel 本身从其索引模块公开的所有内容，以及配置文件特定的API，如下：</p>
<ul>
<li>
<p><strong>api.version</strong>:</p>
<ul>
<li>类型： string</li>
<li>作用： 加载配置文件的 Babel 版本号</li>
</ul>
</li>
<li>
<p><strong>api.cache</strong>：<br>
虽然使用js来配置 Babel 很好，但缺点是它让缓存更加的困难，因为每次编译文件的时候都会重新执行配置函数，这样就会导致 Babel 也需要重新执行配置中引用的任何插件和预置函数。所以 Babel 为了避免这种情况，它希望配置函数的用户可以告诉它如何在配置文件中管理缓存。</p>

































<table><thead><tr><th>方法</th><th>作用</th></tr></thead><tbody><tr><td>api.cache.forever()</td><td>永久缓存计算出的配置并且不在调用该函数</td></tr><tr><td>api.cache.never()</td><td>不要缓存这个配置，并且每次都重新执行该功能</td></tr><tr><td>api.cache.using(() => process.env.NODE_ENV)</td><td>根据 “NODE_ENV” 的值进行缓存。任何时候，using 回调返回一个与预期值不同的值，将在次调用整个配置函数，并将一个新的条目添加到缓存中</td></tr><tr><td>api.cache.invalidate(() => process.env.NODE_ENV)</td><td>根据 “NODE_ENV” 的值进行缓存。任何时候使用回调函数返回的值不是预期的值，将在次调用整个配置函数，缓存中的所有条目都将被结果给替换</td></tr><tr><td>api.cache(true)</td><td>和 api.cache.forever() 一样</td></tr><tr><td>api.cache(false)</td><td>和 api.cache.never() 一样</td></tr></tbody></table>
</li>
<li>
<p><strong>api.env(...)</strong>：<br>
由于 <code>NODE_ENV</code> 是一种相当常见的切换行为的方式，Babel 还专门为此设计了 API 函数。这个 API 函数被用作检查 Babel加载的 <code>envName</code> 的快速方法，如果没有设置其他的覆盖环境，它将考虑到 <code>NODE_ENV</code>。</p>
<p>它有几种形式的不同：</p>

























<table><thead><tr><th>方法</th><th>作用</th></tr></thead><tbody><tr><td>api.env()</td><td>返回当前 envName 的值</td></tr><tr><td>api.env("production")</td><td>如果 envName === 'production' 则返回他 true</td></tr><tr><td>api.env(["development", "test"])</td><td>如果 ["development", "test"].includes(envName) 为true，那么就返回true</td></tr><tr><td>api.env(envName => envName.startsWith("test-"))</td><td>如果 env 以 "test-" 开头，那么就返回 true</td></tr></tbody></table>
</li>
</ul>
<blockquote>
<p>注意：为了确保 Babel 知道这个构建依赖于特定的 <code>envName</code>，不应该和 <code>api.cache.forever()</code> 或 <code>api.cache.never()</code> 一起使用。</p>
</blockquote>
<ul>
<li>
<p><strong>api.caller(cb)</strong>:<br>
这个 API 用于访问传递给 Babel 的调用者数据。由于许多 Babel 实例可能以不同的 <code>caller</code> 值运行在同一进程中，所以这个 API 被设计为自动配置 <code>api.cache</code>，与 <code>api.env</code> 相同。</p>
<p>demo：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isBabelRegister</span>(<span class="hljs-params">caller</span>) </span>&#123;
    <span class="hljs-keyword">return</span> !!(caller && caller.name === <span class="hljs-string">'@babel/register'</span>);
&#125;;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-params">api</span> =></span> &#123;
    <span class="hljs-keyword">const</span> isRegister = api.caller(isBabelRegister);
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">//...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>caller</code> 可以用做回调函数的第一个参数。</p>
</li>
<li>
<p><strong>api.assertVersion(range)</strong>:<br>
虽然 <code>api.version()</code> 很有用，但是 有些时候只需要声明你的版本号就好了，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-params">api</span> =></span> &#123;
    api.assertVersion(<span class="hljs-string">'^7.2'</span>);
    <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这个是根据自己的理解在加上翻译软件得出来的结果，我自己也正在学习 Babel，要是有什么不对的地方，还请各位大佬指出来，谢谢啦~</p></div>  
</div>
            