
---
title: '(译)你应该知道的ES2020中的10个JavaScript新功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924e2bd8c6574547aa8e1ae4c901b48d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 23:57:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924e2bd8c6574547aa8e1ae4c901b48d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>嘿，新的ES2020功能已经存在了一段时间，但并不是所有人都知道，所以这里有一些很酷的功能可以尝试一下！</p>
<h1 data-id="heading-0">1. BigInt</h1>
<p><code>BigInt</code>，JavaScript中最令人期待的功能之一，终于来了。实际上，它允许开发人员在其JS代码中使用更大的整数表示形式进行数据处理和数据处理。</p>
<p>目前，您可以在JavaScript中存储为整数的最大数量为<code>pow(2, 53) - 1</code>。但是 <code>BigInt</code> 实际上允许您执行更多操作。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924e2bd8c6574547aa8e1ae4c901b48d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是，如上所示，您需要在数字的末尾附加 <code>n</code>。 <code>n</code> 表示这是一个 <code>BigInt</code>，JavaScript引擎（对于v8引擎）应区别对待。</p>
<p>此改进不向后兼容，因为传统的数字系统是IEEE754(它不能支持此大小的数字)。</p>
<h1 data-id="heading-1">2. 动态导入</h1>
<p>JavaScript中的动态导入使您可以选择将JS文件作为模块自然地动态导入应用程序中。就像您当前使用 <code>Webpack</code> 和 <code>Babel</code> 进行操作时一样。</p>
<p>此功能将帮助您发送按需请求的代码（通常称为代码拆分），而不会增加 <code>webpack</code> 或其他模块捆绑器的开销。如果愿意，还可以有条件地在 <code>if-else</code> 块中加载代码。好消息是您实际上导入了一个模块，因此它永远不会污染全局名称空间。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/562a8c67d73447599230e02f31a97b2b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">3. 空值合并</h1>
<p>空值合并增加了真正检查 <code>空值</code> 而不是 <code>假值</code> 的能力。您可能会问，<code>空值</code> 和 <code>假值</code> 之间有什么区别？</p>
<p>在JavaScript中，许多值都是 <code>false</code>，例如 <code>""</code>，<code>0</code>，<code>undefined</code>，<code>null</code>，<code>false</code>，<code>NaN</code> 等。</p>
<p>但是，您可能要检查无数个变量是否为空的次数，也就是说，该变量是 <code>undefined</code> 还是 <code>null</code>，就像变量可以有一个空字符串甚至是一个假值一样。</p>
<p>在这种情况下，您将使用新的空值合并运算符 <code>??</code></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed515614c3354c73bbc2b43760242793~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>您可以清楚地看到 <code>||</code> 运算符如何始终返回真实值，而 <code>null</code> 运算符如何返回非null值。</p>
<h1 data-id="heading-3">4. 可选链接</h1>
<p>可选链接语法使您可以访问深度嵌套的对象属性，而不必担心该属性是否存在。如果存在，那就太好了！否则，将返回 <code>undefined</code>。这适用于对象属性，也适用于函数调用和数组。超级方便！像这个例子：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/602799dbd5e4479dae6564ba7b817914~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">5. Promise.allSettled</h1>
<p><code>Promise.allSettled</code> 方法接受一个Promises数组，并且仅在所有这些Promises都已结算时才解决(已解决或被拒绝)。</p>
<p>之前它是不可用的，即使像 <code>race</code> 和 <code>all</code> 一样的逻辑可用。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc55b8cd28054e15b8eed1b8b09fc86a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">6. String的matchAll</h1>
<p><code>matchAll</code> 是添加到 <code>String</code> 原型的新方法，与正则表达式相关。这将返回一个迭代器，该迭代器一个接一个地返回所有匹配的组。看一下这个例子：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e44deab6fa94424ae179ad3832fff8b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">7. 全局this</h1>
<p>如果您编写了一些可以在Node上，浏览器环境以及Web工作者内部运行的跨平台JS代码，那么将很难掌握全局对象。</p>
<p>这是因为它是浏览器的窗口，是Node的全局窗口，是web worker本身。如果有更多的运行时，则全局对象也将有所不同。</p>
<p>因此，您将不得不拥有自己的实现，以检测运行时，然后使用正确的全局变量。因此，ES2020带来了 <code>globalThis</code>，它始终引用全局对象，无论您在何处执行代码：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1d2331ea468457eb0771560f3f2e990~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">8. 导出模块的命名空间</h1>
<p>在JavaScript模块中，已经可以使用以下语法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> utils <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是到目前为止，还没有对应的导出语法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> * <span class="hljs-keyword">as</span> utils <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.mjs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它等效于：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> utils <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils.mjs'</span>
<span class="hljs-keyword">export</span> &#123; utils &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">9. 更好的定义for-in顺序</h1>
<p>ECMA规范未指定 <code>for (x in y)</code> 应按哪个顺序运行，即使以前浏览器自己实现了一致的顺序，但ES2020中已对其进行了正式标准化。</p>
<h1 data-id="heading-9">10. import.meta</h1>
<p><code>import.meta</code> 对象是由ECMAScript实现创建的，它带有一个 <code>null</code> 原型。</p>
<p>想象一个模块，<code>module.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"module"</span> src=<span class="hljs-string">"module.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>您可以使用 <code>import.meta</code> 对象访问有关模块的 <code>meta</code> 信息：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">import</span>.meta); <span class="hljs-comment">// &#123; url: "file:///home/user/module.js" &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它返回一个带有url属性的对象，该属性指示模块的基本URL。这将是从中获取脚本的URL（对于外部脚本）或包含文档的文档基础URL（对于内联脚本）。</p>
<p><em>我的公众号：<a href="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dcf733091574de1b3aa3b6e854ececb~tplv-k3u1fbpfcp-watermark.image" target="_blank" rel="nofollow noopener noreferrer">道道里的前端栈</a>，分享前端知识，嚼碎的感觉真奇妙~</em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            