
---
title: '使用puppeteer在node中绘图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996357038f9a46efb0ab6a7106990009~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 01:29:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996357038f9a46efb0ab6a7106990009~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>笔者在项目中需要用到 node 绘图并返回，查询了市面上的 node 的绘图库</p>

















<table><thead><tr><th>绘图库</th><th>不想用的理由</th></tr></thead><tbody><tr><td><a href="https://github.com/Automattic/node-canvas" target="_blank" rel="nofollow noopener noreferrer">canvas</a></td><td>这个库吧安装要求，太多了，Python 版本要求 2.7，还要安装 GTK，gyp 什么的，因为已经安装了 py3.0 了改来改去也太麻烦了~。</td></tr><tr><td><a href="https://github.com/aheckmann/gm" target="_blank" rel="nofollow noopener noreferrer">gm</a></td><td>因为没找到这个库的渐变怎么做的资料，其他看起来挺好用的</td></tr></tbody></table>
<p>找来找去我想到可以利用 <a href="https://github.com/GoogleChrome/puppeteer" target="_blank" rel="nofollow noopener noreferrer">puppeteer</a>进行绘图</p>
<h2 data-id="heading-1">介绍</h2>
<blockquote>
<p><a href="https://github.com/GoogleChrome/puppeteer" target="_blank" rel="nofollow noopener noreferrer">puppeteer</a> 是谷歌官方出品的一个通过 DevTools 协议控制 headless Chrome 的 Node 库。</p>
<p>可以通过 <a href="https://github.com/GoogleChrome/puppeteer" target="_blank" rel="nofollow noopener noreferrer">puppeteer</a> 的提供的 api 直接控制 Chrome 模拟大部分用户操作来进行 UI Test 或者作为爬虫访问页面来收集数据。</p>
</blockquote>
<blockquote>
<p>首先 Puppeteer 提供了很多的函数能在 Page DOM Environment 中执行代码，</p>
<p>其次 Puppeteer 提供了 ElementHandle 和 JsHandle 将 Page DOM Environment 中元素和对象封装成对应的 Node.js 对象，这样可以直接这些对象的封装函数进行操作 Page DOM</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/996357038f9a46efb0ab6a7106990009~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大白话就是一个跑在 node 内部的浏览器，可以在这个浏览器中进行一些 node 不能做的操作，比如：生成网页的 PDF， 网页性能测试，模拟表单提交，爬取网页数据等等，
当然还有这篇文章的主题用<a href="https://github.com/GoogleChrome/puppeteer" target="_blank" rel="nofollow noopener noreferrer">puppeteer</a>在 node 中绘图</p>
<h2 data-id="heading-2">gogogo</h2>
<pre><code class="copyable">npm i puppeteer
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.封装一下获取浏览器实例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> puppeteer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'puppeteer'</span>)
<span class="hljs-keyword">const</span> mainConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./mainConfig'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BrowserManage</span> </span>&#123;
browserDestructionTimeout <span class="hljs-comment">//清理浏览器实例</span>
browserInstance <span class="hljs-comment">//浏览器实例</span>
browserState = <span class="hljs-string">'closed'</span> <span class="hljs-comment">//浏览器状态</span>
<span class="hljs-comment">/**
 * 用于长时间未进行操作时关闭浏览器实例
 */</span>
<span class="hljs-function"><span class="hljs-title">scheduleBrowserForDestruction</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.browserDestructionTimeout)
<span class="hljs-built_in">this</span>.browserDestructionTimeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.browserInstance) &#123;
<span class="hljs-built_in">this</span>.browserState = <span class="hljs-string">'closed'</span>
<span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.browserInstance.close() <span class="hljs-comment">//关闭浏览器实例</span>
&#125;
&#125;, <span class="hljs-number">5000</span>)
&#125;
<span class="hljs-comment">/**
 * 用于长时间未进行操作时关闭浏览器实例
 */</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getBrowser</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-keyword">async</span> (resolve, reject) => &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.browserState === <span class="hljs-string">'closed'</span>) &#123;
<span class="hljs-built_in">this</span>.browserInstance = <span class="hljs-keyword">await</span> puppeteer.launch(mainConfig.config.puppeteer) <span class="hljs-comment">//开启浏览器实例</span>
<span class="hljs-built_in">this</span>.browserState = <span class="hljs-string">'open'</span>
resolve(<span class="hljs-built_in">this</span>.browserInstance)
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.browserState === <span class="hljs-string">'open'</span>) &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.browserInstance) &#123;
resolve(<span class="hljs-built_in">this</span>.browserInstance)
&#125;
&#125;
&#125;)
&#125;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">new</span> BrowserManage()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>mainConfig.config.puppeteer</code> 为</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
<span class="hljs-attr">args</span>: [<span class="hljs-string">'--no-sandbox'</span>, <span class="hljs-string">'--disable-setuid-sandbox'</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为只用绘制功能所以，不会进行网页的跳转所以这里没有配置沙箱,如果你涉及了页面的跳转强烈建议你配置沙箱</p>
<blockquote>
<p>参考</p>
<p><a href="https://developers.google.com/web/tools/puppeteer/troubleshooting" target="_blank" rel="nofollow noopener noreferrer">developers.google.com/web/tools/p…</a></p>
<p><a href="https://stackoverflow.com/questions/66998228/why-is-no-sandbox-a-unsafe-arg-in-puppeteer" target="_blank" rel="nofollow noopener noreferrer">stackoverflow.com/questions/6…</a></p>
</blockquote>
<h3 data-id="heading-4">2.定义 绘图函数</h3>
<p>这里以绘制文字为例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.toImgData = <span class="hljs-keyword">async</span> (options) => &#123;
<span class="hljs-keyword">let</span> fontConfig = &#123;
<span class="hljs-attr">baseLine</span>: <span class="hljs-number">5</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getColorX</span>(<span class="hljs-params">i, colors</span>) </span>&#123;
<span class="hljs-keyword">if</span> (colors <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) &#123;
<span class="hljs-keyword">return</span> (i / (colors.length - <span class="hljs-number">1</span>)).toFixed(<span class="hljs-number">2</span>)
&#125;
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
<span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>),
font = options.text || <span class="hljs-string">'阿巴阿巴'</span>,
fontSize = <span class="hljs-built_in">Number</span>(options.fontSize || <span class="hljs-number">32</span>),
fontFamily = options.fontFamily,
lineHeight = fontSize + fontSize / fontConfig.baseLine
canvas.width = fontSize * font.length
canvas.height = lineHeight
gradient = ctx.createLinearGradient(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.width, <span class="hljs-number">0</span>)
ctx.shadowColor = options.shadowColor || <span class="hljs-string">''</span>
ctx.shadowOffsetX = options.shadowOffsetX || <span class="hljs-number">2</span>
ctx.shadowOffsetY = options.shadowOffsetY || <span class="hljs-number">2</span>
<span class="hljs-keyword">if</span> (options.colors <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) &#123;
<span class="hljs-comment">//实现渐变颜色</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < options.colors.length; i++) &#123;
gradient.addColorStop(getColorX(i, options.colors), options.colors[i])
&#125;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options.colors == <span class="hljs-string">'string'</span>) &#123;
gradient.addColorStop(<span class="hljs-number">0</span>, options.colors)
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 默认颜色</span>
gradient.addColorStop(<span class="hljs-number">0</span>, <span class="hljs-string">'rgba(241,158,194,1)'</span>)
&#125;
ctx.font = fontSize + <span class="hljs-string">'px '</span> + fontFamily
<span class="hljs-keyword">if</span> (!options.mode || options.mode == <span class="hljs-string">'1'</span>) &#123;
<span class="hljs-comment">//mode ==1为实线</span>
ctx.fillStyle = gradient
ctx.fillText(font, <span class="hljs-number">0</span>, fontSize)
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (options.mode == <span class="hljs-string">'2'</span>) &#123;
<span class="hljs-comment">//mode ==2为字体镂空效果</span>
ctx.strokeStyle = gradient
ctx.strokeText(font, <span class="hljs-number">0</span>, fontSize)
&#125;
ctx.restore()
<span class="hljs-keyword">const</span> dataURI = canvas.toDataURL(<span class="hljs-string">'image/png'</span>)
<span class="hljs-keyword">const</span> base64 = dataURI.substr(<span class="hljs-number">22</span>) <span class="hljs-comment">// 22 =`data:image/png;base64,`.length</span>
resolve(base64)
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.获取并使用浏览器页面实例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> browser = <span class="hljs-keyword">await</span> browserManage.getBrowser()
<span class="hljs-keyword">const</span> page = (<span class="hljs-keyword">await</span> browser.pages())[<span class="hljs-number">0</span>]
<span class="hljs-keyword">await</span> page.setOfflineMode(<span class="hljs-literal">true</span>) <span class="hljs-comment">//因为我们不需要进行网络资源读取,这样可以节省我可怜服务器的带宽</span>
page.on(<span class="hljs-string">'console'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> <span class="hljs-built_in">console</span>.log(msg.type(), msg.text())) <span class="hljs-comment">//监听页面console事件</span>
<span class="hljs-keyword">const</span> base64 = <span class="hljs-keyword">await</span> page.evaluate(toImgData, passedOptions)
browserManage.scheduleBrowserForDestruction()
<span class="hljs-keyword">const</span> buffer = Buffer.from(base64, <span class="hljs-string">'base64'</span>)
<span class="hljs-keyword">return</span> buffer <span class="hljs-comment">//返回Base64 编码的图片</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里注意 <code>page.evaluate</code>函数</p>
<blockquote>
<p>page.evaluate(pageFunction[, ...args])</p>
<p>pageFunction <function|string> 要在页面实例上下文中执行的方法</p>
<p>...args <...Serializable|JSHandle> 要传给 pageFunction 的参数</p>
<p>返回: <Promise> pageFunction 执行的结果</p>
<p>这个函数就相当于在获取的页面实例中内部 eval 调用 js 函数</p>
</blockquote>
<p>所以<code>toImgData</code>中的<code>getColorX</code>写在了内部</p>
<p>当然也可以把<code>getColorX</code>函数抽离然后这样调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> page.evaluate(getColorX) <span class="hljs-comment">//就相当于把getColorX声明并定义</span>
<span class="hljs-keyword">const</span> base64 = <span class="hljs-keyword">await</span> page.evaluate(toImgData, passedOptions)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>效果如下</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31d090cfe45544e78c608ffefa0d9901~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">总结</h2>
<p>本文介绍了 node 使用 puppeteer 进行绘图。</p>
<p>要注意的地方是如果在 linux 中绘制中文会出现空白的情况
因为在 linux 中默认是没有安装中文字符的进行安装即可</p>
<blockquote>
<p>安装可以参考文章 <a href="https://www.huaweicloud.com/articles/f618dd03bebe00f7edc9ceb4214c5254.html" target="_blank" rel="nofollow noopener noreferrer">www.huaweicloud.com/articles/f6…</a></p>
</blockquote>
<p>并且在 linux 中直接 <code>npm i puppeteer</code>是启动不了的
需要自己安装 chromium
或者</p>
<pre><code class="copyable">sudo apt-get install gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> browser = <span class="hljs-keyword">await</span> puppeteer.launch(&#123;
        <span class="hljs-attr">executablePath</span>: <span class="hljs-string">"/usr/bin/chromium-browser"</span>, <span class="hljs-comment">//通过executablePath配置Chromium 的路径</span>
        ......
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错这个</p>
<pre><code class="copyable">  (node:28469) UnhandledPromiseRejectionWarning: Error: Failed to launch chrome!
[1025/150325.817887:ERROR:zygote_host_impl_linux.cc(89)]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是因为没配置沙箱，这样以无沙箱模式启动</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> browser = <span class="hljs-keyword">await</span> puppeteer.launch(&#123;
  <span class="hljs-attr">args</span>: [<span class="hljs-string">'--no-sandbox'</span>, <span class="hljs-string">'--disable-setuid-sandbox'</span>]&#125;
  ......
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议配置沙箱</p>
<blockquote>
<p>参考 <a href="https://github.com/puppeteer/puppeteer/issues/3443" target="_blank" rel="nofollow noopener noreferrer">github.com/puppeteer/p…</a></p>
</blockquote>
<p>例子 git 地址 <a href="https://github.com/lgldlk/puppeteer-draw-example/" target="_blank" rel="nofollow noopener noreferrer">github.com/lgldlk/pupp…</a></p>
<p>欢迎加入前端学习讨论群 qq 群号： <a href="https://jq.qq.com/?_wv=1027&k=OBRz4lMY" target="_blank" rel="nofollow noopener noreferrer">530496237</a></p></div>  
</div>
            