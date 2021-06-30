
---
title: '解读 rollup Plugin （二）--你最不想看的各种钩子函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=415'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 07:59:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=415'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 18 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>Lynne，一个能哭爱笑永远少女心的前端开发工程师。身处互联网浪潮之中，热爱生活与技术。</p>
</blockquote>
<h2 data-id="heading-0">rollup plugin 的实现</h2>
<p>接上一篇<a href="https://juejin.cn/post/6978413009060233246" target="_blank">解读 rollup Plugin （一）</a></p>
<p>当然，也不可能就这么简单啦~毕竟还要考虑实际复杂应用场景的~~</p>
<h3 data-id="heading-1">插件驱动</h3>
<p>PluginDriver ---  插件驱动器，调用插件和提供插件环境上下文等</p>
<h4 data-id="heading-2">钩子函数的调用时机</h4>
<p>平常书写rollup插件的时候，最关注的就是钩子函数部分了，钩子函数的调用时机有三类:</p>
<ul>
<li>const chunks = rollup.rollup执行期间的构建钩子函数 - <a href="https://rollupjs.org/guide/en/#build-hooks" target="_blank" rel="nofollow noopener noreferrer">Build Hooks</a></li>
<li>chunks.generator(write)执行期间的输出钩子函数 - <a href="https://rollupjs.org/guide/en/#output-generation-hooks" target="_blank" rel="nofollow noopener noreferrer">Output Generation Hooks</a></li>
<li>监听文件变化并重新执行构建的rollup.watch执行期间的 watchChange 钩子函数</li>
</ul>
<h4 data-id="heading-3">构建钩子函数</h4>
<p>为了与构建过程交互，你的插件对象需要包含一些构建钩子函数。构建钩子是构建的各个阶段调用的函数。构建钩子函数可以影响构建执行方式、提供构建的信息或者在构建完成后修改构建。rollup 中有不同的构建钩子函数：</p>
<ul>
<li>async: 处理promise的异步钩子，也有同步版本</li>
<li>first: 如果多个插件实现了相同的钩子函数，那么会串式执行，从头到尾，但是，如果其中某个的返回值不是null也不是undefined的话，会直接终止掉后续插件。</li>
<li>sequential: 如果多个插件实现了相同的钩子函数，那么会串式执行，按照使用插件的顺序从头到尾执行，如果是异步的，会等待之前处理完毕，在执行下一个插件。</li>
<li>parallel: 同上，不过如果某个插件是异步的，其后的插件不会等待，而是并行执行。</li>
</ul>
<p>构建钩子函数在构建阶段执行，它们被 <code>[rollup.rollup(inputOptions)](https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/cli/run/build.ts#L34)</code> 触发。它们主要关注在 Rollup 处理输入文件之前定位、提供和转换输入文件。构建阶段的第一个钩子是 <code>options</code>，最后一个钩子总是 <code>buildEnd</code>，除非有一个构建错误，在这种情况下 <code>closeBundle</code> 将在这之后被调用。</p>
<p>此外，在观察模式下，<code>watchChange</code> 钩子可以在任何时候被触发，以通知新的运行将在当前运行产生其输出后被触发。另外，当 watcher 关闭时，closeWatcher 钩子函数将被触发。</p>
<h4 data-id="heading-4">输出钩子函数</h4>
<p>输出生成钩子函数可以提供关于生成的包的信息并在构建完成后立马执行。它们和构建钩子函数拥有一样的工作原理和相同的类型，但是不同的是它们分别被 ·<code>[bundle.generate(output)](https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/cli/run/build.ts#L44)</code> 或 <code>[bundle.write(outputOptions)](https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/cli/run/build.ts#L64)</code> 调用。只使用输出生成钩子的插件也可以通过输出选项传入，因为只对某些输出运行。</p>
<p>输出生成阶段的第一个钩子函数是 <a href="https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/src/Bundle.ts#L50" target="_blank" rel="nofollow noopener noreferrer">outputOptions</a>，如果输出通过 <a href="https://github.com/rollup/rollup/blob/master/cli/run/build.ts#L44" target="_blank" rel="nofollow noopener noreferrer">bundle.generate(...)</a> 成功生成则第一个钩子函数是 <a href="https://github.com/rollup/rollup/blob/master/src/Bundle.ts#L73" target="_blank" rel="nofollow noopener noreferrer">generateBundle</a>，如果输出通过 <code>[bundle.write(...)](https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/src/watch/watch.ts#L200)</code> 生成则最后一个钩子函数是 <code>[writeBundle](https://github.com/rollup/rollup/blob/master/src/rollup/rollup.ts#L176)</code>，另外如果输出生成阶段发生了错误的话，最后一个钩子函数则是 <a href="https://github.com/rollup/rollup/blob/master/src/Bundle.ts#L70" target="_blank" rel="nofollow noopener noreferrer">renderError</a>。</p>
<p>另外，<a href="https://github.com/rollup/rollup/blob/master/src/rollup/rollup.ts#L59" target="_blank" rel="nofollow noopener noreferrer">closeBundle</a> 可以作为最后一个钩子被调用，但用户有责任手动调用 <code>bundle.close()</code> 来触发它。CLI 将始终确保这种情况发生。</p>
<h3 data-id="heading-5">钩子函数加载实现</h3>
<p><code>[PluginDriver](https://github.com/rollup/rollup/blob/07b3a02069594147665daa95d3fa3e041a82b2d0/src/utils/PluginDriver.ts#L124)</code> 中有 9 个 hook 加载函数。主要是因为每种类别的 hook 都有同步和异步的版本。
​</p>
<p>接下来从分类来看函数钩子的应用场景：
​</p>
<h4 data-id="heading-6">1. hookFirst</h4>
<p>加载 <code>first</code> 类型的钩子函数，场景有 <code>resolveId</code>、<code>resolveAssetUrl</code> 等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hookFirst</span><<span class="hljs-title">H</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">PluginHooks</span>, <span class="hljs-title">R</span> = <span class="hljs-title">ReturnType</span><<span class="hljs-title">PluginHooks</span>[<span class="hljs-title">H</span>]>>(<span class="hljs-params">
  hookName: H,
  args: Args<PluginHooks[H]>,
  replaceContext?: ReplaceContext | <span class="hljs-literal">null</span>,
  skip?: number | <span class="hljs-literal">null</span>
</span>): <span class="hljs-title">EnsurePromise</span><<span class="hljs-title">R</span>> </span>&#123;
  <span class="hljs-comment">// 初始化 promise</span>
  <span class="hljs-keyword">let</span> promise: <span class="hljs-built_in">Promise</span><any> = <span class="hljs-built_in">Promise</span>.resolve();
  <span class="hljs-comment">// this.plugins 在实例化 Graph 的时候，进行了初始化</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.plugins.length; i++) &#123;
    <span class="hljs-keyword">if</span> (skip === i) <span class="hljs-keyword">continue</span>;
    <span class="hljs-comment">// 覆盖之前的 promise，换言之就是串行执行钩子函数</span>
    promise = promise.then(<span class="hljs-function">(<span class="hljs-params">result: any</span>) =></span> &#123;
      <span class="hljs-comment">// 返回非 null 或 undefined 的时候，停止运行，返回结果</span>
      <span class="hljs-keyword">if</span> (result != <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> result;
      <span class="hljs-comment">// 执行钩子函数</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.runHook(hookName, args <span class="hljs-keyword">as</span> any[], i, <span class="hljs-literal">false</span>, replaceContext);
    &#125;);
  &#125;
  <span class="hljs-comment">// 返回 hook 过的 promise</span>
  <span class="hljs-keyword">return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.hookFirstSync</h4>
<p>hookFirst 的同步版本，使用场景有 <code>resolveFileUrl</code>、<code>resolveImportMeta</code> 等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hookFirstSync</span><<span class="hljs-title">H</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">PluginHooks</span>, <span class="hljs-title">R</span> = <span class="hljs-title">ReturnType</span><<span class="hljs-title">PluginHooks</span>[<span class="hljs-title">H</span>]>>(<span class="hljs-params">
  hookName: H,
  args: Args<PluginHooks[H]>,
  replaceContext?: ReplaceContext
</span>): <span class="hljs-title">R</span> </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.plugins.length; i++) &#123;
    <span class="hljs-comment">// runHook 的同步版本</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.runHookSync(hookName, args, i, replaceContext);
    <span class="hljs-comment">// 返回非 null 或 undefined 的时候，停止运行，返回结果</span>
    <span class="hljs-keyword">if</span> (result != <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> result <span class="hljs-keyword">as</span> any;
  &#125;
  <span class="hljs-comment">// 否则返回 null</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">as</span> any;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3. <strong>hookParallel</strong></h4>
<p>并行执行 hook，不会等待当前 hook 完成。使用场景 <code>buildEnd</code>、<code>buildStart</code>、<code>moduleParsed</code> 等。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">hookParallel<H <span class="hljs-keyword">extends</span> AsyncPluginHooks & ParallelPluginHooks>(
  hookName: H,
  <span class="hljs-attr">args</span>: Parameters<PluginHooks[H]>,
  replaceContext?: ReplaceContext
): <span class="hljs-built_in">Promise</span><<span class="hljs-keyword">void</span>> &#123;
  <span class="hljs-keyword">const</span> promises: <span class="hljs-built_in">Promise</span><<span class="hljs-keyword">void</span>>[] = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.plugins) &#123;
    <span class="hljs-keyword">const</span> hookPromise = <span class="hljs-built_in">this</span>.runHook(hookName, args, plugin, <span class="hljs-literal">false</span>, replaceContext);
    <span class="hljs-keyword">if</span> (!hookPromise) <span class="hljs-keyword">continue</span>;
    promises.push(hookPromise);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(promises).then(<span class="hljs-function">() =></span> &#123;&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4.<strong>hookReduceArg0</strong></h4>
<p>对 arg 第一项进行 reduce 操作。使用场景: <code>options</code>、<code>renderChunk</code> 等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hookReduceArg0</span><<span class="hljs-title">H</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">PluginHooks</span>, <span class="hljs-title">V</span>, <span class="hljs-title">R</span> = <span class="hljs-title">ReturnType</span><<span class="hljs-title">PluginHooks</span>[<span class="hljs-title">H</span>]>>(<span class="hljs-params">
    hookName: H,
    [arg0, ...args]: any[], <span class="hljs-comment">// 取出传入的数组的第一个参数，将剩余的置于一个数组中</span>
    reduce: Reduce<V, R>,
    replaceContext?: ReplaceContext <span class="hljs-comment">// 替换当前 plugin 调用时候的上下文环境</span>
</span>) </span>&#123;
  <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(arg0); <span class="hljs-comment">// 默认返回 source.code</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.plugins.length; i++) &#123;
    <span class="hljs-comment">// 第一个 promise 的时候只会接收到上面传递的arg0</span>
    <span class="hljs-comment">// 之后每一次 promise 接受的都是上一个插件处理过后的 source.code 值</span>
    promise = promise.then(<span class="hljs-function"><span class="hljs-params">arg0</span> =></span> &#123;
      <span class="hljs-keyword">const</span> hookPromise = <span class="hljs-built_in">this</span>.runHook(hookName, [arg0, ...args], i, <span class="hljs-literal">false</span>, replaceContext);
      <span class="hljs-comment">// 如果没有返回 promise，那么直接返回 arg0</span>
      <span class="hljs-keyword">if</span> (!hookPromise) <span class="hljs-keyword">return</span> arg0;
      <span class="hljs-comment">// result 代表插件执行完成的返回值</span>
      <span class="hljs-keyword">return</span> hookPromise.then(<span class="hljs-function">(<span class="hljs-params">result: any</span>) =></span>
        reduce.call(<span class="hljs-built_in">this</span>.pluginContexts[i], arg0, result, <span class="hljs-built_in">this</span>.plugins[i])
      );
    &#125;);
  &#125;
  <span class="hljs-keyword">return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">5.<strong>hookReduceArg0Sync</strong></h4>
<p><code>hookReduceArg0</code> 同步版本，使用场景 <code>transform</code>、<code>generateBundle</code> 等</p>
<h4 data-id="heading-11">6. <strong>hookReduceValue</strong></h4>
<p>将返回值减少到类型T，分别处理减少的值。允许钩子作为值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">hookReduceValue<H <span class="hljs-keyword">extends</span> PluginValueHooks, T>(
hookName: H,
<span class="hljs-attr">initialValue</span>: T | <span class="hljs-built_in">Promise</span><T>,
args: Parameters<AddonHookFunction>,
reduce: <span class="hljs-function">(<span class="hljs-params">
reduction: T,
result: ResolveValue<ReturnType<AddonHookFunction>>,
plugin: Plugin
</span>) =></span> T,
replaceContext?: ReplaceContext
): <span class="hljs-built_in">Promise</span><T> &#123;
<span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">Promise</span>.resolve(initialValue);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.plugins) &#123;
promise = promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
<span class="hljs-keyword">const</span> hookPromise = <span class="hljs-built_in">this</span>.runHook(hookName, args, plugin, <span class="hljs-literal">true</span>, replaceContext);
<span class="hljs-keyword">if</span> (!hookPromise) <span class="hljs-keyword">return</span> value;
<span class="hljs-keyword">return</span> hookPromise.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span>
reduce.call(<span class="hljs-built_in">this</span>.pluginContexts.get(plugin), value, result, plugin)
);
&#125;);
&#125;
<span class="hljs-keyword">return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><strong>7. hookReduceValueSync</strong></h4>
<p>hookReduceValue的同步版本</p>
<h4 data-id="heading-13">8. <strong>hookSeq</strong></h4>
<p>加载 <code>sequential</code> 类型的钩子函数，和 hookFirst 的区别就是不能中断，使用场景有 <code>onwrite</code>、<code>generateBundle</code> 等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hookSeq</span><<span class="hljs-title">H</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">PluginHooks</span>>(<span class="hljs-params">
  hookName: H,
  args: Args<PluginHooks[H]>,
  replaceContext?: ReplaceContext,
  <span class="hljs-comment">// hookFirst 通过 skip 参数决定是否跳过某个钩子函数</span>
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">void</span>> </span>&#123;
  <span class="hljs-keyword">let</span> promise: <span class="hljs-built_in">Promise</span><<span class="hljs-keyword">void</span>> = <span class="hljs-built_in">Promise</span>.resolve();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.plugins.length; i++)
    promise = promise.then(<span class="hljs-function">() =></span>
      <span class="hljs-built_in">this</span>.runHook<<span class="hljs-keyword">void</span>>(hookName, args <span class="hljs-keyword">as</span> any[], i, <span class="hljs-literal">false</span>, replaceContext),
    );
  <span class="hljs-keyword">return</span> promise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">9.<strong>hookSeqSync</strong></h4>
<p>hookSeq 同步版本，不需要构造 promise，而是直接使用 <code>runHookSync</code> 执行钩子函数。使用场景有 <code>closeWatcher</code>、<code>watchChange</code> 等。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">hookSeqSync<H <span class="hljs-keyword">extends</span> SyncPluginHooks & SequentialPluginHooks>(
  hookName: H,
  <span class="hljs-attr">args</span>: Parameters<PluginHooks[H]>,
  replaceContext?: ReplaceContext
): <span class="hljs-keyword">void</span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.plugins) &#123;
    <span class="hljs-built_in">this</span>.runHookSync(hookName, args, plugin, replaceContext);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<p>通过观察上面几种钩子函数的调用方式，我们可以发现，其内部有一个调用钩子函数的方法: runHook(Sync)，该函数执行插件中提供的钩子函数。
​</p>
<h4 data-id="heading-15">runHook(Sync)</h4>
<p>​</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runHook</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  hookName: string,
  args: any[],
  pluginIndex: number,
  permitValues: boolean,
  hookContext?: ReplaceContext | <span class="hljs-literal">null</span>,
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-built_in">this</span>.previousHooks.add(hookName);
  <span class="hljs-comment">// 找到当前 plugin</span>
  <span class="hljs-keyword">const</span> plugin = <span class="hljs-built_in">this</span>.plugins[pluginIndex];
  <span class="hljs-comment">// 找到当前执行的在 plugin 中定义的 hooks 钩子函数</span>
  <span class="hljs-keyword">const</span> hook = (plugin <span class="hljs-keyword">as</span> any)[hookName];
  <span class="hljs-keyword">if</span> (!hook) <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> any;

  <span class="hljs-comment">// pluginContexts 在初始化 plugin 驱动器类的时候定义，是个数组，数组保存对应着每个插件的上下文环境</span>
  <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">this</span>.pluginContexts[pluginIndex];
  <span class="hljs-comment">// 用于区分对待不同钩子函数的插件上下文</span>
  <span class="hljs-keyword">if</span> (hookContext) &#123;
    context = hookContext(context, plugin);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
    .then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 许可值允许返回值，而不是一个函数钩子，使用 hookReduceValue 或 hookReduceValueSync 加载。</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> hook !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">if</span> (permitValues) <span class="hljs-keyword">return</span> hook;
        <span class="hljs-keyword">return</span> error(&#123;
          <span class="hljs-attr">code</span>: <span class="hljs-string">'INVALID_PLUGIN_HOOK'</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">`Error running plugin hook <span class="hljs-subst">$&#123;hookName&#125;</span> for <span class="hljs-subst">$&#123;plugin.name&#125;</span>, expected a function hook.`</span>,
        &#125;);
      &#125;
      <span class="hljs-comment">// 传入插件上下文和参数，返回插件执行结果</span>
      <span class="hljs-keyword">return</span> hook.apply(context, args);
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> throwPluginError(err, plugin.name, &#123; <span class="hljs-attr">hook</span>: hookName &#125;));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">插件上下文</h3>
<p>​</p>
<p>rollup给钩子函数注入了context，也就是上下文环境，用来方便对chunks和其他构建信息进行增删改查。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> context: PluginContext = &#123;
    <span class="hljs-function"><span class="hljs-title">addWatchFile</span>(<span class="hljs-params">id</span>)</span> &#123;&#125;,
    <span class="hljs-attr">cache</span>: cacheInstance,
    <span class="hljs-attr">emitAsset</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">emitChunk</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">emitFile</span>: fileEmitter.emitFile,
    error(err)
    <span class="hljs-attr">getAssetFileName</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">getChunkFileName</span>: getDeprecatedContextHandler(),
    <span class="hljs-attr">getFileName</span>: fileEmitter.getFileName,
    <span class="hljs-attr">getModuleIds</span>: <span class="hljs-function">() =></span> graph.modulesById.keys(),
    <span class="hljs-attr">getModuleInfo</span>: graph.getModuleInfo,
    <span class="hljs-attr">getWatchFiles</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">Object</span>.keys(graph.watchFiles),
    <span class="hljs-attr">isExternal</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">meta</span>: &#123;
        rollupVersion,
        <span class="hljs-attr">watchMode</span>: graph.watchMode
    &#125;,
    <span class="hljs-keyword">get</span> <span class="hljs-title">moduleIds</span>() &#123;
        <span class="hljs-keyword">const</span> moduleIds = graph.modulesById.keys();
        <span class="hljs-keyword">return</span> wrappedModuleIds();
    &#125;,
    <span class="hljs-attr">parse</span>: graph.contextParse,
    <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">source, importer, &#123; custom, skipSelf &#125; = BLANK</span>)</span> &#123;
        <span class="hljs-keyword">return</span> graph.moduleLoader.resolveId(source, importer, custom, skipSelf ? pidx : <span class="hljs-literal">null</span>);
    &#125;,
    <span class="hljs-attr">resolveId</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">setAssetSource</span>: fileEmitter.setAssetSource,
    <span class="hljs-function"><span class="hljs-title">warn</span>(<span class="hljs-params">warning</span>)</span> &#123;&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">插件的缓存</h2>
<p>插件还提供缓存的能力，实现的非常巧妙.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPluginCache</span>(<span class="hljs-params">cache: SerializablePluginCache</span>): <span class="hljs-title">PluginCache</span> </span>&#123;
<span class="hljs-comment">// 利用闭包将cache缓存</span>
<span class="hljs-keyword">return</span> &#123;
<span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">id: string</span>)</span> &#123;
<span class="hljs-keyword">const</span> item = cache[id];
<span class="hljs-keyword">if</span> (!item) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
item[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>; <span class="hljs-comment">// 如果访问了，那么重置访问过期次数，猜测：就是说明用户有意向主动去使用</span>
<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;,
<span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">id: string</span>)</span> &#123;
<span class="hljs-keyword">const</span> item = cache[id];
<span class="hljs-keyword">if</span> (!item) <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
item[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>; <span class="hljs-comment">// 如果访问了，那么重置访问过期次数</span>
<span class="hljs-keyword">return</span> item[<span class="hljs-number">1</span>];
&#125;,
<span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">id: string, value: any</span>)</span> &#123;
            <span class="hljs-comment">// 存储单位是数组，第一项用来标记访问次数</span>
cache[id] = [<span class="hljs-number">0</span>, value];
&#125;,
<span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">id: string</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">delete</span> cache[id];
&#125;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后创建缓存后，会添加在插件上下文中:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createPluginCache <span class="hljs-keyword">from</span> <span class="hljs-string">'createPluginCache'</span>;

<span class="hljs-keyword">const</span> cacheInstance = createPluginCache(pluginCache[cacheKey] || (pluginCache[cacheKey] = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)));

<span class="hljs-keyword">const</span> context = &#123;
<span class="hljs-comment">// ...</span>
    <span class="hljs-attr">cache</span>: cacheInstance,
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后我们就可以在插件中就可以使用cache进行插件环境下的缓存，进一步提升打包效率:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPlugin</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"test-plugin"</span>,
    <span class="hljs-function"><span class="hljs-title">buildStart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.cache.has(<span class="hljs-string">"prev"</span>)) &#123;
        <span class="hljs-built_in">this</span>.cache.set(<span class="hljs-string">"prev"</span>, <span class="hljs-string">"上一次插件执行的结果"</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 第二次执行rollup的时候会执行</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.cache.get(<span class="hljs-string">"prev"</span>));
      &#125;
    &#125;,
  &#125;;
&#125;
<span class="hljs-keyword">let</span> cache;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">build</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> chunks = <span class="hljs-keyword">await</span> rollup.rollup(&#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">"src/main.js"</span>,
    <span class="hljs-attr">plugins</span>: [testPlugin()],
    <span class="hljs-comment">// 需要传递上次的打包结果</span>
    cache,
  &#125;);
  cache = chunks.cache;
&#125;

build().then(<span class="hljs-function">() =></span> &#123;
  build();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<h2 data-id="heading-18">总结</h2>
<p>恭喜你，把 rollup 那么几种钩子函数都熬着看过来了，可能实际的插件开发中我们未必会用到这些知识，我们也未必能一一掌握，但有些东西你必须得先知道，才能进行下一步~~</p></div>  
</div>
            