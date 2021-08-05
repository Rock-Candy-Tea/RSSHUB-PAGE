
---
title: '新一代打包工具esbuild'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482640e887a8458289c49f9f58f63656~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 00:30:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482640e887a8458289c49f9f58f63656~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第<code>3</code>天，活动详情查看：<strong><a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">了解esbuild</h2>
<h3 data-id="heading-1">esbuild是什么</h3>
<p>esbuild官方描述的作用就是：<code>一个JavaScript的打包和和压缩工具</code>。<br>
esbuild使用<strong>golang</strong>开发，在打包的速度上非常快，我们熟悉的<code>vite</code>工具在<strong>dev模式</strong>下就是使用esbuild进行打包。</p>
<h3 data-id="heading-2">esbuild的主要特征</h3>
<ul>
<li>在没有缓存的情况也能有极致的性能</li>
<li>支持ES6的Tree shaking</li>
<li>原生支持typescript和jsx打包</li>
<li>支持Source Map</li>
<li>代码压缩</li>
<li>支持定义插件</li>
</ul>
<h3 data-id="heading-3">打包速度比较</h3>
<p>esbuild最主要的一个特征就是<strong>有极致的性能</strong>，那么它到底有多快，参考esbuild官方提供的一张图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482640e887a8458289c49f9f58f63656~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到，esbuild的性能跟现在主流的打包工具相比，速度比他们快超过100倍。可见它在性能方面有多可怕。<br>
因为现在主流的打包工具底层上执行还是在js的执行环境中，cpu不能充分地得到使用，所以就会导致执行速度慢。</p>
<h2 data-id="heading-4">esbuild使用</h2>
<p>了解完esbuild概念，接下来了解一下如何使用esbuild的一些主要概念</p>
<h3 data-id="heading-5">API</h3>
<ul>
<li>
<p><code>transform</code><br>
<code>transform</code>就是转换的意思，调用这个API能将<code>ts</code>，<code>jsx</code>等文件转换为js文件。<br>
支持的文件有:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> type Loader = <span class="hljs-string">'js'</span> | <span class="hljs-string">'jsx'</span> | <span class="hljs-string">'ts'</span> | <span class="hljs-string">'tsx'</span> | <span class="hljs-string">'css'</span> | <span class="hljs-string">'json'</span> | <span class="hljs-string">'text'</span> | <span class="hljs-string">'base64'</span> | <span class="hljs-string">'file'</span> | <span class="hljs-string">'dataurl'</span> | <span class="hljs-string">'binary'</span> | <span class="hljs-string">'default'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用transform
首先我们创建一个测试的TS文件</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">    <span class="hljs-comment">// test.ts</span>
    <span class="hljs-keyword">const</span> str: <span class="hljs-built_in">string</span> = <span class="hljs-string">'Hello World'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>transform</code>转换为js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// cli</span>
    exbuild ./test.ts --loader=ts <span class="hljs-comment">// 输出 const str = 'Hello World';</span>
    
    <span class="hljs-comment">// js api调用</span>
    <span class="hljs-keyword">const</span> esbuild = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>);
    <span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
    <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
    <span class="hljs-keyword">const</span> filePath = path.resolve(__dirname, <span class="hljs-string">'test.ts'</span>);
    <span class="hljs-keyword">const</span> code = esbuild.transformSync(fs.readFilesync(filePath), &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'ts'</span>,
    &#125;)
    <span class="hljs-built_in">console</span>.log(code);
    <span class="hljs-comment">// 输出</span>
    <span class="hljs-comment">// &#123;</span>
    <span class="hljs-comment">//  code: 'const str = 'Hello World'',</span>
    <span class="hljs-comment">//  map: '',</span>
    <span class="hljs-comment">//  warnings: []</span>
    <span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>transform还可以在转换代码的同时进行<strong>压缩代码(minify)</strong>，<strong>制定代码的模块类型(format)</strong> 等等，部分的的配置如下:</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> TransformOptions &#123;
  <span class="hljs-comment">// 源代码的类型</span>
  loader?: Loader;
  <span class="hljs-comment">// 代码顶部注入代码</span>
  banner?: <span class="hljs-built_in">string</span>;
  <span class="hljs-comment">// 代码底部注入代码</span>
  footer?: <span class="hljs-built_in">string</span>;
  
  <span class="hljs-comment">// sourcemap相关配置</span>
  sourcemap?: <span class="hljs-built_in">boolean</span> | <span class="hljs-string">'inline'</span> | <span class="hljs-string">'external'</span> | <span class="hljs-string">'both'</span>;
  legalComments?: <span class="hljs-string">'none'</span> | <span class="hljs-string">'inline'</span> | <span class="hljs-string">'eof'</span> | <span class="hljs-string">'linked'</span> | <span class="hljs-string">'external'</span>;
  sourceRoot?: <span class="hljs-built_in">string</span>;
  sourcesContent?: <span class="hljs-built_in">boolean</span>;
  
  <span class="hljs-comment">// 代码压缩相关</span>
  minify?: <span class="hljs-built_in">boolean</span>;
  minifyWhitespace?: <span class="hljs-built_in">boolean</span>;
  minifyIdentifiers?: <span class="hljs-built_in">boolean</span>;
  minifySyntax?: <span class="hljs-built_in">boolean</span>;
  charset?: Charset;
  treeShaking?: TreeShaking;
  
  <span class="hljs-comment">// jsx相关</span>
  jsx?: <span class="hljs-string">'transform'</span> | <span class="hljs-string">'preserve'</span>;
  jsxFactory?: <span class="hljs-built_in">string</span>;
  jsxFragment?: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的描述可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2Fapi%2F%23footer" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/api/#footer" ref="nofollow noopener noreferrer">这里</a></p>
</li>
<li>
<p><code>build</code><br>
<code>build</code>整合了<code>transform</code>后的代码，可以将一个或者多个文件转换并保存为文件。<br>
使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// cli</span>
    esbuild test.ts --outfile=./dist/test.js <span class="hljs-comment">// &#123; errors: [], warnings: [] &#125;</span>
    
    <span class="hljs-comment">// js api调用</span>
    <span class="hljs-keyword">const</span> esbuild = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>);
    <span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

    <span class="hljs-keyword">const</span> result = esbuild.buildSync(&#123;
      <span class="hljs-attr">entryPoints</span>: [path.resolve(__dirname, <span class="hljs-string">'test.ts'</span>)],
      <span class="hljs-attr">outdir</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    &#125;);

    <span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// &#123; errors: [], warnings: [] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完后会生成转换后的代码文件到指定的目录，具体的配置参数可以点击<a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2Fapi%2F%23build-api" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/api/#build-api" ref="nofollow noopener noreferrer">这里</a></p>
</li>
</ul>
<h3 data-id="heading-6">esbuild插件（Plugins）</h3>
<p>与其他打包工具一样，esbuild也有<code>plugin</code>，plugin会在<code>build</code>的时候提供一些钩子函数，让你可以在打包的某一个阶段去执行自定义的操作。<br>
<code>plugin</code>提供了四个钩子，<strong>按顺序执行</strong>分别是:<code>onStart</code>，<code>onResolve</code>，<code>onLoad</code>，<code>onEnd</code><br>
现在我们就来写一个测试的插件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> esbuild = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-comment">// 测试插件</span>
<span class="hljs-keyword">const</span> testPlugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'testPlugin'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">&#123; onStart, onResolve, onLoad, onEnd &#125;</span>)</span> &#123;
    onStart(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onStart'</span>);
    &#125;);
    onResolve(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span> &#125;, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onResolve'</span>, msg);
    &#125;);
    onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span> &#125;, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onLoad'</span>, msg);
    &#125;);
    onEnd(<span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onEnd'</span>, msg);
    &#125;);
  &#125;,
&#125;;

esbuild.buildSync(&#123;
  <span class="hljs-attr">entryPoints</span>: [path.resolve(__dirname, <span class="hljs-string">'test.ts'</span>)],
  <span class="hljs-attr">outdir</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
  <span class="hljs-attr">bundle</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">plugins</span>: [testPlugin],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后返回</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3666939a0b34c77a0281a5b25eb8354~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">实战：利用esbuild打包ts项目</h2>
<p>讲完esbuild的大概用法，接下来做一个实战项目。项目中大概的步骤:</p>
<ul>
<li>1.将typescript项目打包成js文件</li>
<li>2.将打包后的文件放到HTML中运行这个HTML。</li>
</ul>
<p>首先来写一个插入节点的ts文件<code>test.ts</code></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// test.ts</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> app = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>);
  <span class="hljs-keyword">const</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
  div.innerHTML = <span class="hljs-string">'<div>Hello World</div>'</span>;
  app.appendChild(div);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建一个html文件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>test html<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"&#123;&#123;scripts&#125;&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来写打包逻辑</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// esbuild.js</span>
<span class="hljs-keyword">const</span> esbuild = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-comment">// html文件地址</span>
<span class="hljs-keyword">const</span> HTML_PATH = path.resolve(__dirname, <span class="hljs-string">'index.html'</span>);
<span class="hljs-comment">// 目标地址</span>
<span class="hljs-keyword">const</span> TARGET_PATH = path.resolve(__dirname, <span class="hljs-string">'dist'</span>);
<span class="hljs-comment">// 输出js的地址</span>
<span class="hljs-keyword">const</span> OUTPUT_PATH = <span class="hljs-string">'./test.js'</span>;
<span class="hljs-comment">/**
 * 自定义插件
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123; import('esbuild').Plugin &#125;</span></span>
 */</span>
<span class="hljs-keyword">const</span> testPlugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'testPlugin'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">&#123; onEnd &#125;</span>)</span> &#123;
    <span class="hljs-comment">// 打包结束后执行替换和复制html操作</span>
    onEnd(<span class="hljs-function">(<span class="hljs-params">&#123; errors &#125;</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(errors);
      <span class="hljs-keyword">if</span> (!errors.length) &#123;
        <span class="hljs-keyword">let</span> data = fs.readFileSync(HTML_PATH, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span> &#125;);
        data = data.replace(<span class="hljs-string">`&#123;scripts&#125;`</span>, OUTPUT_PATH);
        fs.writeFileSync(path.resolve(TARGET_PATH, <span class="hljs-string">'index.html'</span>), data, &#123;
          <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>,
        &#125;);
      &#125;
    &#125;);
  &#125;,
&#125;;

<span class="hljs-comment">// 打包主方法</span>
esbuild
  .build(&#123;
    <span class="hljs-attr">entryPoints</span>: [path.resolve(__dirname, <span class="hljs-string">'test.ts'</span>)],
    <span class="hljs-attr">outdir</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">bundle</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">plugins</span>: [testPlugin],
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (msg.length) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'compile error'</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'compile success'</span>);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行esbuild.js文件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5b52140ce6455781caef14c909c36b~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>文件已经生成成功，打开html文件看一下有没有执行js
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f63e80bfe2064b7caed91c76627ecc84~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码成功执行
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feccfdf0e8cf4885b3f1c8405e37eef7~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">小结</h2>
<p>本文主要介绍了<code>esbuild</code>打包工具。主要介绍了:</p>
<ul>
<li>esbuild的性能比现在主流的打包工具要快得多</li>
<li>esbuild的api和用法</li>
<li>esbuild如何定义插件</li>
<li>利用esbuild打包一个ts项目</li>
</ul>
<p>若文章中有不严谨或出错的地方请在评论区域指出~</p>
<h2 data-id="heading-9">参考</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/" ref="nofollow noopener noreferrer">esbuild</a></li>
</ol></div>  
</div>
            