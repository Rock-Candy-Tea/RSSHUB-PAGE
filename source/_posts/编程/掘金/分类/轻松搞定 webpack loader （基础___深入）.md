
---
title: '轻松搞定 webpack loader （基础___深入）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6184a02af0241ea9bbdfec5b00f4536~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 06:14:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6184a02af0241ea9bbdfec5b00f4536~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">序言</h2>
<p>在学习之前先抛出三个问题，我们根据这三个问题深入学习 loader 。</p>
<ol>
<li>什么是 loader ，它能干什么。</li>
<li>为什么需要 loader 。</li>
<li>如何使用 loader ，有哪些要掌握的核心。</li>
</ol>
<h2 data-id="heading-1">什么是 loader ？</h2>
<p><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6184a02af0241ea9bbdfec5b00f4536~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>这是 <strong>webpack</strong> 官网的宣传图，我们可以看到，左侧各种类型的文件，统一打包成右边被浏览器识别支持的文件，那么这个转换的过程是如何实现的呢，没错就是 webpack 的核心概念之一（ <strong>loader</strong>）实现的。</p>
<ol>
<li>loader 让 webpack <strong>能够处理其他类型的文件，并将它们转换为有效模块</strong>。</li>
<li>loader <strong>本质是一个函数，导出为函数的 JavaScript 模块</strong>。</li>
<li>简单说就是将各种类型的文件，转换成 JS 模块。</li>
</ol>
<h2 data-id="heading-2">为什么需要loader</h2>
<p>因为 webpack 只能理解 <strong>JavaScript</strong>和 <strong>JSON</strong>文件。所以需要一个模块来帮它处理其他类型的文件，loader 就是做这件事情的模块。</p>
<h3 data-id="heading-3">webpack常用的loader</h3>
<p>样式：style-loader、css-loader、less-loader、sass-loader 等<br>文件：raw-loader、file-loader 、url-loader 等<br>编译：babel-loader、coffee-loader 、ts-loader 等<br>校验测试：mocha-loader、jshint-loader 、eslint-loader 等<br>为什么有这么多种 loader 呢，是因为一种 loader 处理相应的文件，这样的<strong>职责单一的设计，可以高度复用和灵活组合</strong>。</p>
<h2 data-id="heading-4">loader怎么用</h2>
<p>首先 loader 是辅助 webpack 的模块 ，所以要配置 webpack.config 文件指定 loader 的执行区间和执行方式，我们以一个 sass-loader 的例子演示一下使用。</p>
<ol>
<li>首先匹配要处理的文件，通过 test，正则过滤出 scss 文件。</li>
<li>经过 sass-loader 转换 sass 文件为 css 文件， 并且包装一层 module.exports 成为一个 js module 。</li>
<li>通过 style-loader 将创建一个style 标签将上面转换完成的 css 文件嵌入 html 中。</li>
<li>最后 css-loader 处理其中的 <code>@import</code> 和 <code>url()</code>。因为 <strong>webpack 不认识，所以将其转化成 require 形式</strong>。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.scss$/</span>,
          use:[
              &#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">'style-loader'</span>&#125;,
              &#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">'css-loader'</span>,<span class="hljs-attr">options</span>:&#123;<span class="hljs-attr">sourceMap</span>:<span class="hljs-literal">true</span>,<span class="hljs-attr">modules</span>:<span class="hljs-literal">true</span>&#125;&#125;,
              &#123;<span class="hljs-attr">loader</span>:<span class="hljs-string">'sass-loader'</span>,<span class="hljs-attr">options</span>:&#123;<span class="hljs-attr">sourceMap</span>:<span class="hljs-literal">true</span>&#125;&#125;
          ],
          <span class="hljs-attr">exclude</span>:<span class="hljs-regexp">/node_modules/</span>,
          enforce: <span class="hljs-string">"post"</span>,
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">深入 loader</h2>
<p>我们已经知道了 loader 的概念和基本使用，所以接下来会探究一下 loader 的分类和执行流程。通过上例，我们发现还有一个 <code>enforce: "post"</code> 配置，这就是<strong>loader 分类的配置</strong>。<br>​<br></p>
<h3 data-id="heading-6">enforce ( loader 分类)</h3>
<h4 data-id="heading-7">类别与优先级</h4>
<ol>
<li>在 webpack 中 loader 可以被分为四类，分别是 ：<strong>普通</strong><code>normal</code> ，<strong>前置</strong><code>pre</code>，<strong>行内</strong><code>inline</code>，<strong>后置</strong> <code>post</code> 。</li>
<li>普通 <code>normal</code> ，前置<code>pre</code>，后置 <code>post</code> ，通过 enforce 可以进行分类设置，若无设置，则默认为 normal。</li>
<li>行内 <code>inline</code> 比较特殊，是在 import / require 的时候，直接写入代码中，用来过滤其他的 loader 。</li>
<li>四种loader调用先后顺序为：pre > normal > inline > post 。</li>
</ol>
<h4 data-id="heading-8">inline（行内 loader ）</h4>
<p>使用方法是在 <code>import / require</code> 的时候，将他的三种前缀语法写入代码中：</p>
<ol>
<li><code>!</code> : 忽略 normal-loader。</li>
<li><code>-!</code> : 忽略 pre-loader 和 normal-loader.</li>
<li><code>!!</code> : 忽略所有 loader （pre / normal / post）</li>
</ol>
<p>行内 loader 通过 <code>!</code> 控制资源中的 loader，同时支持在 loader 后面通过 <code>?</code> 传递参数。<br><strong>Tip：</strong><br>该分类是相对于 rules ，并非是某个 loader ，只要在当前这个 rules 范围内的所有 loader 都遵循此设定。<br><strong>实例</strong><br>假设我们有4个 loader ，分别为 pre-loader ，normal-loader ，post-loader ，inline-loader。<br>以上 loader 均为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">content</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"x-loader"</span>);
  <span class="hljs-keyword">return</span> content;
&#125;;

<span class="hljs-built_in">module</span>.exports.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"x-loader-pitch"</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>无前缀信息时</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"/Users/jiangyuereee/Desktop/loader/inline-loader.js!./txt.txt"</span>

post-loader-pitch
inline-loader-pitch
normal-loader-pitch
pre-loader-pitch
pre-loader-pitch
normal-loader-pitch
inline-loader-pitch
post-loader-pitch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以发现，执行顺序是按照我们上文提到的优先级顺序进行排列，并且触发方式类似于洋葱模型。</p>
<ol start="2">
<li>！前缀信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"!/Users/jiangyuereee/Desktop/loader/inline-loader.js!./txt.txt"</span>

post-loader-pitch
inline-loader-pitch
pre-loader-pitch
pre-loader-pitch
inline-loader-pitch
post-loader-pitch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到 normal-loader 并没有触发，所以过滤成功。</p>
<ol start="3">
<li>-!前缀信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"-!/Users/jiangyuereee/Desktop/loader/inline-loader.js!./txt.txt"</span>

post-loader-pitch
inline-loader-pitch
inline-loader-pitch
post-loader-pitch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到 normal-loader 和 pre-loader 并没有触发，所以过滤成功。</p>
<ol start="4">
<li>!!前缀信息</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"!!/Users/jiangyuereee/Desktop/loader/inline-loader.js!./txt.txt"</span>

post-loader-pitch
post-loader-pitch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到只有 inline-loader 触发，所以过滤成功。</p>
<ol start="5">
<li>当出现相同的 loader 的情况下，调用的优先级为，从低到高，自右往左。（pitch情况下，则相反）</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62ea37b4f9964c30ba0b30bf79d2c91c~tplv-k3u1fbpfcp-zoom-1.image" alt="loader.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">Loader-pitch</h3>
<ol>
<li>loader 的调用过程：在从右往左调用 loader 方法之前都会从左往右调用一遍 loader上面的 pitch 方法。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fca68178e8384a6f94b01acc8189c27a~tplv-k3u1fbpfcp-zoom-1.image" alt="loader调用过程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>loader 的熔断机制</li>
</ol>
<p>一旦一个 pitch 返回了结果，那么直接熔断，不会执行后面的 pitch ，直接将现有结果传递给前一个 loader 。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0bfe5ea86ea484c9a4c45f785fb7a3e~tplv-k3u1fbpfcp-zoom-1.image" alt="loade熔断过程.png" loading="lazy" referrerpolicy="no-referrer"><br>我们看到上图中 loader2.pitch 返回了结果，直接把结果传递给 loader1，剩下的都不会触发了。<br>​<br></p>
<h2 data-id="heading-10">同步 / 异步 loader</h2>
<p><br><strong>在官方文档中有描述</strong>：<br>如果是单个处理结果，可在<strong>同步模式</strong>中直接返回，但是如果有多个结果，则要调用 <code>this.callpack()</code>。在<strong>异步模式</strong>中，必须调用 <code>this.async()</code>来告知 loader runner 等待异步结果，它会返回 <code>this.callback()</code>回调函数，随后 loader 必须返回 undefined ，并且调用该回调函数。<br>在 webpack 中，loader 会依赖于读取外部配置文件，进行网络请求等，<strong>如果同步操作，会造成进程堵塞。所以loader 会有同步 / 异步之分</strong>。<br>​</p>
<p><strong>在 loader 中，可以通过两种方式返回数据</strong>：</p>
<ol>
<li>return ：只能返回 content。</li>
<li>callback ：可以返回</li>
</ol>
<ul>
<li><code>err : Error | null</code>                  (错误信息）</li>
<li><code>content : string | Buffer</code>    （content信息）</li>
<li><code>sourceMap : SourceMap </code>         （sourceMap）</li>
<li><code>meta? : any </code>                           （奇怪的数据，AST等等）</li>
</ul>
<h4 data-id="heading-11">同步 loader</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-comment">// return handleData(content);</span>
  <span class="hljs-built_in">this</span>.callback(<span class="hljs-literal">null</span>, handleData(content), handleSourceMap(map), meta);
  <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 当调用 callback() 函数时，总是返回 undefined</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">异步 loader</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">content, map, meta</span>) </span>&#123;
  <span class="hljs-keyword">var</span> callback = <span class="hljs-built_in">this</span>.async();
  asycnHandleData(content, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, result</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> callback(err);
    callback(<span class="hljs-literal">null</span>, result, map, meta);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结： 要注意的是，异步要通过 <code>this.async</code> 来获取 callback。</p>
<h2 data-id="heading-13">loader的输出</h2>
<p><br>由loader的返回方法 callback 可知，当 loader 链路到了最后一个 loader 的时候，compiler 期待得到的结果是可以转换为<code>String</code> 的 <code>Buffer</code> 或者直接是个 <code>String</code> 。表示当前模板处理后的 <code>JS</code> 源码。根据返回参数得知，还可以传递一个 <code>sourceMap</code>。<br>除去正常的 loader 输出的 JS 源码,还可以根据 <code>this.emitFile</code> 进行额外输出文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">emitFile(
    name: string, 
    <span class="hljs-attr">content</span>: Buffer|string, 
    sourceMap?: &#123;...&#125;
)；

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">相关使用工具</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Floaders%2F" target="_blank" title="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Floaders%2F">webpack 官方中文文档</a>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftsejx.github.io%2Fwebpack-guidebook%2Fprinciple-analysis%2Fimplementation-principle%2Floader" target="_blank" title="https://link.juejin.cn/?target=https%3A%2F%2Ftsejx.github.io%2Fwebpack-guidebook%2Fprinciple-analysis%2Fimplementation-principle%2Floader">Loader 机制</a>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Floader-runner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/loader-runner" ref="nofollow noopener noreferrer">Loader-runner调试工具</a>。</li>
</ol>
<br></div>  
</div>
            