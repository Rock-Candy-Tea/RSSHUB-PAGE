
---
title: 'Labor，首个 web container 开源实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7039'
author: 掘金
comments: false
date: Tue, 25 May 2021 08:16:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=7039'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>halo，大家好，俺是 132，今天给大家带来的是一个很有意思的东西</p>
<p>起因是 stackblitz 团队在 Chrome I/O 上分享了一篇文章，可以将 node 跑到浏览器中</p>
<p><a href="https://blog.stackblitz.com/posts/introducing-webcontainers/" target="_blank" rel="nofollow noopener noreferrer">blog.stackblitz.com/posts/intro…</a></p>
<p>然后惊艳四座，国内外都在猜测内部的可能实现……因为他们也不开源，于是……</p>
<p>经过我好几天的研究，我特么终于搞懂了o(╥﹏╥)o</p>
<p><a href="https://github.com/yisar/labor" target="_blank" rel="nofollow noopener noreferrer">github.com/yisar/labor</a></p>
<p>先放 github 地址，欢迎大家提 pr，点 star，蟹蟹大家啦</p>
<p>然后接下来我简单阐述一下这个的底层原理</p>
<p><strong>基本实现原理</strong></p>
<pre><code class="hljs language-js copyable" lang="js">code => service worker(js runtime) => go wasm API
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一句话就是，在 server worker 中，借助 wasm 实现一个 js runtime</p>
<p>举例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = readFileSync(<span class="hljs-string">'a.js'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先可以肯定的是，这段 js 是在 service worker 中跑的，service worker 充当了 v8 的角色</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'global'</span>, <span class="hljs-string">`with(global)&#123;
    const a = readFileSync('a.js')
&#125;`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，我们执行会提示缺少 <code>readFileSync</code> API，剩下的工作，我们就是要使用 wasm 实现这个 API，然后注入到 global 上</p>
<p>wasm 充当了 deno 中的 rust 角色</p>
<pre><code class="hljs language-go copyable" lang="go">js.Global().Set(<span class="hljs-string">"readFileSync"</span>, js.FuncOf(<span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">(this js.Value, args []js.Value)</span> <span class="hljs-title">interface</span></span>&#123;&#125; &#123;
    readFile(args[<span class="hljs-number">0</span>].String())
    <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>
&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大功告成！基本原理就是这么简单的啦</p>
<p><strong>文件系统</strong></p>
<p>根据 stackblitz 的 demo 可以看到，他们是可以读文件系统的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = readFileSync(<span class="hljs-string">'./a.js'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上如果我们没有文件系统的话，访问 <code>./a.js</code> 是拿不到内容的，所以重点来了</p>
<p>我们要在首次加载的时候，把所有文件都存到内存里，也就是需要构建一个 dependency graph</p>
<p>如果你有写过打包工具的经验，肯定会对 dependency graph 比较熟悉了，我之前也有一次技术分享详细讲过</p>
<p>简化就是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
    [<span class="hljs-string">'./a.js'</span>, buffer], 
    [<span class="hljs-string">'./b.go'</span>, buffer]
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在我们初始化的时候，就是要生成一张这样的图，这是我们实现文件系统的关键</p>
<p><strong>http client</strong></p>
<p>除了文件系统，另一个重点就是 http</p>
<p>好消息是 go 的 <code>net/http</code> 包对 WASI 的支持程度还不错，但有很多东西还是没办法用</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">Download</span><span class="hljs-params">(url <span class="hljs-keyword">string</span>)</span> <span class="hljs-title">interface</span></span>&#123;&#125; &#123;
    res, _ := http.Get(url)
    buffer, _ := ioutil.ReadAll(res.Body)
    body := js.Global().Get(<span class="hljs-string">"Uint8Array"</span>).New(<span class="hljs-built_in">len</span>(b))
    js.CopyBytesToJS(body, b)
    <span class="hljs-keyword">return</span> body
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一直报错，气死我了，所以为了抹平，我们只能重新重新实现一个 http client 了</p>
<p>基本原理是借助 net 的其他包，polyfill 不支持的包</p>
<p>比如 <code>net/http</code> 的 http.Get() 方法不支持，我们就用 <code>net/http/httputil</code> 包模拟</p>
<p>这块内容比较多，等我有时间了</p>
<p><strong>web container 的场景</strong></p>
<ol>
<li>webIDE</li>
</ol>
<p>这次的 stackblitz demo 就是 webIDE，因为可以直接在浏览器中直接跑 js runtime，直接启一个 server，所以节省了通往 server 的链路</p>
<p>类比的场景比如组件化实施预览，lowcode 的预览，物料市场的预览等等</p>
<ol start="2">
<li>better worker</li>
</ol>
<p>实际上 web container 也可以理解为，借助 wasm 能力进行增强的 worker，你可以用它做很多以前 worker 里做不了的事情</p>
<p>比如我在公司里是负责小程序底层架构的，小程序的模拟器是需要启动一个 server 的，然后每次重新编译就得重启 server，现在有了 labor，我就可以全部在浏览器中完成工作，可以说非常完美了</p>
<ol start="3">
<li>双 worker 同构</li>
</ol>
<p><a href="https://workers.cloudflare.com/" target="_blank" rel="nofollow noopener noreferrer">workers.cloudflare.com</a></p>
<p>前阵子 cloudflare worker 的形态令人耳目一新，我当时觉得这个形态的 serverless 真的是太赞了</p>
<p>但是 cloudflare 是 server 端的 js runtime，它一直缺少一个本地调试的终端</p>
<p>labor 就可以做这件事情，我们在本地通过 labor 开发，线上通过 cloudflare 运行，两个 worker API 完全相同，最终做到同构</p>
<p>这可以说是 serverless 的最绝美形态了</p>
<ol start="4">
<li>ssr/esr</li>
</ol>
<p>esr 是最近比较火的，就是在 serverless 平台下做 ssr，和上面的双 worker 同构一样，想象一下开发环境走 labor 的 ssr 会多么爽</p>
<p><strong>web container 的优势</strong></p>
<ol>
<li>不再需要开发者关注 server</li>
</ol>
<p>尤其是对于 ssr 的场景，非常非常赞</p>
<ol start="2">
<li>调试更好</li>
</ol>
<p>Chrome devtools 是最好的调试工具</p>
<ol start="3">
<li>更省钱</li>
</ol>
<p>咳咳咳。。。</p>
<p><strong>web container 的限制</strong></p>
<p>因为 labor 是在浏览器中实现 js runtime，所以主要限制来自于浏览器</p>
<ol>
<li>http 不能启端口</li>
</ol>
<p>也就是 go 的 <code>ListenAndServe</code> 不能用</p>
<ol start="2">
<li>不能访问本地文件</li>
</ol>
<p><a href="https://web.dev/file-system-access/" target="_blank" rel="nofollow noopener noreferrer">web.dev/file-system…</a> 这个 API 看着不太靠谱</p>
<ol start="3">
<li>wasm 性能差</li>
</ol>
<p>实测，go 的 wasm 版本，平均比 native go 慢 30 倍，比 js 慢 10 倍</p>
<p>这主要是 go 的 GC 导致的，所以社区内有一些替代方案，比如 tinygo，可以扳回一局</p>
<p><strong>总结</strong></p>
<p>社区内很多人对 web container 评价比较不好，比如太花里胡哨，比如性能差限制多</p>
<p>但是我问，当年双线程前端框架也是花里胡哨来着？</p>
<p>但最终还是成就了小程序这么一个无敌的产品</p>
<p>web container 也是同理，最终肯定有绝美的产品落地的</p>
<p>不多说啦</p>
<p><a href="https://github.com/yisar/labor" target="_blank" rel="nofollow noopener noreferrer">github.com/yisar/labor</a></p>
<p>快点来点赞吧，以后有机会再来分享啊哈</p></div>  
</div>
            