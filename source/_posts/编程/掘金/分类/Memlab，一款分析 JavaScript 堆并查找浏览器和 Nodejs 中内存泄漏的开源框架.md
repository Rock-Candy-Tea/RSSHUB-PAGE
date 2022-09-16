
---
title: 'Memlab，一款分析 JavaScript 堆并查找浏览器和 Node.js 中内存泄漏的开源框架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9fc42c3bc1414baefce2bd59e2359e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 03:59:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9fc42c3bc1414baefce2bd59e2359e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>Memlab</code> 是一款 <code>E2E</code> 测试和分析框架，用于发现 <code>JavaScript</code> 内存泄漏和优化机会。</p>
<p><code>Memlab</code> 是 <code>JavaScript</code> 的内存测试框架。它支持定义一个测试场景（使用 <code>Puppeteer API</code>），教 <code>Memlab</code> 如何与您的单页应用程序（<code>SPA</code>）交互，<code>Memlab</code> 可以自动处理其余的内存泄漏检查：</p>
<ul>
<li>与浏览器交互并获取 <code>JavaScript</code> 堆快照</li>
<li>分析堆快照并过滤掉内存泄漏</li>
<li>聚合和分组类似的内存泄漏</li>
<li>生成用于内存调试的保留器跟踪</li>
</ul>
<h2 data-id="heading-0">安装 Memlab</h2>
<pre><code class="hljs language-sh copyable" lang="sh">npm install -g memlab
memlab <span class="hljs-built_in">help</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">在 Demo App 中检测泄漏</h2>
<p>使用 <code>Memlab</code> 检测分离的 <code>DOM</code> 元素的教程。Demo 源码：</p>
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebookincubator%2Fmemlab%2Ftree%2Fmain%2Fpackages%2Fe2e%2Fstatic%2Fexample" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebookincubator/memlab/tree/main/packages/e2e/static/example" ref="nofollow noopener noreferrer">github.com/facebookinc…</a></small></li>
</ul>
<h3 data-id="heading-2">设置示例 Web App</h3>
<p>当您单击 <code>“Create detached DOMs”</code> 按钮时，Demo app 会泄漏分离的 <code>DOM</code> 元素。每次单击都会创建 <code>1024</code> 个分离的 <code>DOM</code> 元素，这些元素由 <code>window</code> 对象引用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9fc42c3bc1414baefce2bd59e2359e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @nolint</span>

<span class="hljs-keyword">import</span> <span class="hljs-title class_">Link</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'next/link'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">DetachedDom</span>(<span class="hljs-params"></span>) &#123;

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">addNewItem</span> = (<span class="hljs-params"></span>) => &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-variable language_">window</span>.<span class="hljs-property">leakedObjects</span>) &#123;
      <span class="hljs-variable language_">window</span>.<span class="hljs-property">leakedObjects</span> = [];
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1024</span>; i++) &#123;
      <span class="hljs-variable language_">window</span>.<span class="hljs-property">leakedObjects</span>.<span class="hljs-title function_">push</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'div'</span>));
    &#125;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'Detached DOMs are created. Please check Memory tab in devtools'</span>)
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"row"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/"</span>></span>Go back<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"row"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"btn"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;addNewItem&#125;</span>></span>
          Create detached DOMs
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源文件：<code>packages/e2e/static/example/pages/examples/detached-dom.jsx</code></p>
<h4 data-id="heading-3">1. 克隆仓库</h4>
<p>要在本地机器上运行 <code>demo</code>，请克隆 <code>memlab</code> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebookincubator%2Fmemlab" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebookincubator/memlab" ref="nofollow noopener noreferrer">github 存储库</a>：</p>
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebookincubator%2Fmemlab" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebookincubator/memlab" ref="nofollow noopener noreferrer">github.com/facebookinc…</a></small></li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">git <span class="hljs-built_in">clone</span> git@github.com:facebookincubator/memlab.git
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2. 运行示例 App</h4>
<p>从 Memlab 项目的根目录运行以下命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">cd</span> packages/e2e/static/example
npm install
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将启动一个示例 <code>Nextjs</code> app。让我们通过从浏览器访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000" ref="nofollow noopener noreferrer">http://localhost:3000</a> 来确保它正在运行：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd582957e3cb4de3993efad5e2eb420a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="0.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里测试的是 <code>Example 1</code>。</p>
<h3 data-id="heading-5">查找内存泄漏</h3>
<h4 data-id="heading-6">1.创建一个场景文件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @nolint</span>
<span class="hljs-comment">// memlab/packages/e2e/static/example/scenario/detached-dom.js</span>
<span class="hljs-comment">/**
 * 我们要运行的场景的初始 `url`。
 */</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">url</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"http://localhost:3000/examples/detached-dom"</span>;
&#125;

<span class="hljs-comment">/**
 * 指定 memlab 应如何执行您要测试该 action 是否导致内存泄漏的 action。
 *
 * <span class="hljs-doctag">@param</span> <span class="hljs-variable">page</span> - Puppeteer's page object:
 * https://pptr.dev/api/puppeteer.page/
 */</span>
<span class="hljs-keyword">async</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">action</span>(<span class="hljs-params">page</span>) &#123;
  <span class="hljs-keyword">const</span> elements = <span class="hljs-keyword">await</span> page.$x(
    <span class="hljs-string">"//button[contains(., 'Create detached DOMs')]"</span>
  );
  <span class="hljs-keyword">const</span> [button] = elements;
  <span class="hljs-keyword">if</span> (button) &#123;
    <span class="hljs-keyword">await</span> button.<span class="hljs-title function_">click</span>();
  &#125;
  <span class="hljs-comment">// 从 memlab 清理外部引用</span>
  <span class="hljs-keyword">await</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">all</span>(elements.<span class="hljs-title function_">map</span>(<span class="hljs-function"><span class="hljs-params">e</span> =></span> e.<span class="hljs-title function_">dispose</span>()));
&#125;

<span class="hljs-comment">/**
 * 指定 memlab 应如何执行将重置您在上面执行的 action 的 action。
 *
 * <span class="hljs-doctag">@param</span> <span class="hljs-variable">page</span> - Puppeteer's page object:
 * https://pptr.dev/api/puppeteer.page/
 */</span>
<span class="hljs-keyword">async</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">back</span>(<span class="hljs-params">page</span>) &#123;
  <span class="hljs-keyword">await</span> page.<span class="hljs-title function_">click</span>(<span class="hljs-string">'a[href="/"]'</span>);
&#125;

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123; action, back, url &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个文件在 <code>packages/e2e/static/example/scenario/detached-dom.js</code>。</p>
<h4 data-id="heading-7">2.运行 memlab</h4>
<p>这可能需要几分钟：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">cd</span> packages/e2e/static/example
npm run dev <span class="hljs-comment"># 注意启动 Demo</span>
memlab run --scenario scenarios/detached-dom.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f232824256b4113a0eb3ac394968b3e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">3.调试泄漏跟踪</h4>
<p>对于每个泄漏的对象组，memLab 打印一个具有代表性的泄漏跟踪。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8519f9d8f9b4e2daf2fb162231d9e04~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>让我们从上到下分解结果：</p>
<p>第 1 部分：浏览器交互面包屑显示了按照我们的场景文件中指定的方式执行的浏览器交互（导航）<code>memlab</code>。</p>
<ul>
<li><code>page-load[6.5MB](baseline)[s1]</code> - 初始页面加载时 JavaScript 堆大小为 <code>6.5MB</code>。<code>baseline</code> 堆快照将在磁盘上保存为 <code>s1.heapsnapshot</code>。</li>
<li><code>action-on-page[6.6MB](baseline)[s2]</code> - 单击 <code>“Create detached DOMs”</code> 按钮后，堆大小增加到 <code>6.6MB</code>。</li>
<li><code>revert[7MB](final)[s3]</code> - 在离开触发内存泄漏的页面后，该网页最终达到了 7MB。</li>
</ul>
<p>第 2 部分：泄漏跟踪的总体摘要</p>
<ul>
<li><code>1024 leaks</code> - 有 1024 个泄漏的对象。<code>example app</code> 的第 12 行在 for 循环中创建了 1024 个分离的 DOM 对象。</li>
<li><code>Retained size</code> - 泄漏对象集群的聚合保留大小为 143.3KB（内存泄漏根据保留跟踪的相似性分组在一起）。</li>
</ul>
<p>第 3 部分：每个泄漏簇的详细代表泄漏跟踪</p>
<blockquote>
<p><small>泄漏跟踪是从 GC 根（垃圾收集器遍历堆的堆图中的入口对象）到泄漏对象的对象引用链。跟踪显示泄漏的对象为何以及如何在内存中仍然保持活动状态。 打破引用链意味着泄漏的对象将不再可以从 GC 根访问，因此可以进行垃圾回收。</small></p><small>
</small><p><small>通过从原生 Window（即 GC 根）向下逐个跟踪泄漏跟踪，您将能够找到应该设置为 null 的引用（但这不是由于bug 引起的）。</small></p>
</blockquote>
<ul>
<li><code>map</code> - 这是正在访问的对象的 <code>V8 HiddenClass</code>（V8 在内部使用它来存储有关对象形状的元信息和对其原型的引用 - 在此处查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ffast-properties%23hiddenclasses-and-descriptorarrays" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/fast-properties#hiddenclasses-and-descriptorarrays" ref="nofollow noopener noreferrer">更多</a>信息）- 在大多数情况下，这是 V8 实现细节，可以忽略。
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ffast-properties%23hiddenclasses-and-descriptorarrays" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/fast-properties#hiddenclasses-and-descriptorarrays" ref="nofollow noopener noreferrer">v8.dev/blog/fast-p…</a></small></li>
</ul>
</li>
<li><code>prototype</code> - 这是 <code>Window</code> 类的实例。</li>
<li><code>leakedObjects</code> - 这表明 <code>leakedObjects</code> 是 <code>Window</code> 对象的一个属性，大小为 <code>148.5KB</code>，指向一个 <code>Array</code> 对象。</li>
<li><code>0</code> - 这表明分离的 <code>HTMLDIVElement</code>（即当前未连接到 <code>DOM</code> 树的 <code>DOM</code> 元素）被存储为<code>leakedObjects</code> 数组的第一个元素（由于显示所有 <code>1024</code> 条泄漏痕迹是压倒性的，<code>Memlab</code> 只打印一个具有代表性的泄漏痕迹。即属性 <code>0</code> 而不是属性 <code>0->1023</code>)</li>
</ul>
<p>简而言之，从 Window 对象到泄漏对象的泄漏跟踪路径为：</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-variable language_">window</span>](object) -> <span class="hljs-title function_">leakedObjects</span>(property) -> [<span class="hljs-title class_">Array</span>](object)
  -> <span class="hljs-number">0</span>(element) -> [<span class="hljs-title class_">Detached</span> <span class="hljs-title class_">HTMLDIVElement</span>](native)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与示例中的泄漏代码匹配：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">window</span>.<span class="hljs-property">leakedObjects</span> = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1024</span>; i++) &#123;
    <span class="hljs-variable language_">window</span>.<span class="hljs-property">leakedObjects</span>.<span class="hljs-title function_">push</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'div'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">更多</h2>
<ul>
<li>官网及 Demo
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Ffacebookincubator.github.io%2Fmemlab" target="_blank" rel="nofollow noopener noreferrer" title="https://facebookincubator.github.io/memlab" ref="nofollow noopener noreferrer">facebookincubator.github.io/memlab</a></small></li>
</ul>
</li>
<li>文档
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Ffacebookincubator.github.io%2Fmemlab%2Fdocs%2Fintro%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://facebookincubator.github.io/memlab/docs/intro/" ref="nofollow noopener noreferrer">facebookincubator.github.io/memlab/docs…</a></small></li>
</ul>
</li>
<li>Meta Engineering 博客文章
<ul>
<li><small><a href="https://link.juejin.cn/?target=https%3A%2F%2Fengineering.fb.com%2F2022%2F09%2F12%2Fopen-source%2Fmemlab%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://engineering.fb.com/2022/09/12/open-source/memlab/" ref="nofollow noopener noreferrer">engineering.fb.com/2022/09/12/…</a></small></li>
</ul>
</li>
</ul></div>  
</div>
            