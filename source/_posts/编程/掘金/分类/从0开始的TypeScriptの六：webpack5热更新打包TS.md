
---
title: '从0开始的TypeScriptの六：webpack5热更新打包TS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032c709bff7d4599b6577535ec99ff94~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 03:56:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032c709bff7d4599b6577535ec99ff94~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">webpack5热更新打包</h1>
<p>热更新，是指 <strong>Hot Module Replacement</strong>，缩写为 <strong>HMR</strong>。</p>
<p><strong>模块热替换</strong>（<strong>HMR</strong> - Hot Module Replacement）是 webpack 提供的最有用的功能之一。它允许在运行时替换，添加，删除各种模块，而无需进行完全刷新重新加载整个页面</p>
<p>当然这次主要是为了打包我写的<code>typescript</code>，为了修改ts后能够时时更新出js文件。</p>
<h2 data-id="heading-1">配置准备</h2>
<p>在之前的文章 《<a href="https://juejin.cn/post/6992956547252879374" target="_blank" title="https://juejin.cn/post/6992956547252879374">从0开始的TypeScriptの五：webpack打包typescript</a>》里面，关于webpack如何打包ts文件已经讲过一次，需要安装的插件还是需要继续依赖</p>
<p>插件：</p>
<ul>
<li>typescript</li>
<li>webpack</li>
<li>webpack-cli</li>
<li>ts-loader</li>
</ul>
<p>本次热更新对应还需要多安装一个包，叫做<code>webpack-dev-server</code></p>
<blockquote>
<p>安装命令： yarn add webpack-dev-server</p>
</blockquote>
<p>我的这四个包的版本(这里可以注意一下，我的<code>webpack</code>版本已经是5了)：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.3.5"</span>,
<span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.48.0"</span>,
<span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^4.7.2"</span>,
<span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时需要在根目录下创建<code>webpack.config.js</code>文件，这个文件的配置在此系列<a href="https://juejin.cn/post/6992956547252879374" target="_blank" title="https://juejin.cn/post/6992956547252879374">上一篇文章</a>中已经有写过，不过现在需要多增加<code>devServer</code>和<code>plugins</code>配置。</p>
<p>之前的<code>webpack.config.js</code>文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);   
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>:<span class="hljs-string">'./TypeScript/tsc05.ts'</span>,   <span class="hljs-comment">// 打包对入口文件，期望打包对文件入口。 这里配置tsc05.ts的位置</span>
  <span class="hljs-attr">output</span>:&#123;
    <span class="hljs-attr">filename</span>:<span class="hljs-string">'tsc_out.js'</span>,   <span class="hljs-comment">// 输出文件名称</span>
    <span class="hljs-attr">path</span>:path.resolve(__dirname,<span class="hljs-string">'./TypeScript/'</span>)  <span class="hljs-comment">//获取输出路径</span>
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,   <span class="hljs-comment">// 整个mode 可以不要，模式是生产坏境就是压缩好对，这里配置开发坏境方便看生成对代码</span>
  <span class="hljs-attr">module</span>:&#123;
  <span class="hljs-attr">rules</span>: [&#123;
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.tsx?$/</span>,
      use: <span class="hljs-string">'ts-loader'</span>,
      <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
    &#125;]
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.ts'</span>]      <span class="hljs-comment">// 解析对文件格式</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<strong>module.exports</strong>内增加的配置代码如下：</p>
<blockquote>
<p>通过 <strong>webpack-dev-server</strong> 的这些配置，能够以多种方式改变其行为</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">devServer: &#123;
    <span class="hljs-attr">liveReload</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// liveReload替代hot进行热更新</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">9000</span>,   <span class="hljs-comment">// 端口号</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'tsc_out.js'</span>,   <span class="hljs-comment">// 输出文件名称</span>
&#125;,
<span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">//热更新插件</span>
    <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()  <span class="hljs-comment">// 在最开始需要引入 const webpack = require('webpack');</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里很有可能在后面运行时出现报错，原因是webpack未找到， 如果此前没有在<code>webpack.config.js</code>引入webpack，此时需要引入一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack.config.js</code>配置好了之后，在根目录的<code>package.json</code>文件中，添加<code>script</code>运行脚本 start</p>
<pre><code class="copyable">"scripts": &#123;
    "dev": "webpack --mode development",
    "start": "webpack serve --config webpack.config.js --mode development"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong> 这里千万要注意，start的运行命令要写作<code>webpack serve</code>而不是<code>webpack-dev-server</code></p>
</blockquote>
<p>因为使用<code>webpack-dev-server</code>是webpack5以前的方式了，如果使用，就会在<code>npm run start</code>运行时发生报错，错误信息为： <code>Error: Cannot find module 'webpack-cli/bin/config-yargs'</code></p>
<p>参考文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdev-server%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/dev-server/" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/032c709bff7d4599b6577535ec99ff94~tplv-k3u1fbpfcp-watermark.image" alt="webpack-dev-server过时.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行命令配置错误：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d297b450207247e9bde0d015db262131~tplv-k3u1fbpfcp-watermark.image" alt="webpack热更新错误.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行命令配置后运行成功：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feb4262217ca4ccd9f22d18b833ef056~tplv-k3u1fbpfcp-watermark.image" alt="热更新配置成功.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<hr>
<br>
<h2 data-id="heading-2">艰难的配置之路</h2>
<p>接下来就开始了更加艰辛的配置过程了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01bbeffb352f4ac1b0cca66c289a507f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然此时配置成功，并且npm run start命令成功运行起来后，发现又出现了一堆报错，主要都是<code>Module not found: Error: Can't resolve</code>错误。</p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a509e18cb231434593c9882d5dae28b2~tplv-k3u1fbpfcp-watermark.image" width="700" loading="lazy" referrerpolicy="no-referrer">
<p>然后我又开始疯狂找原因，进入错误的文件夹<code>webpack-dev-server\client</code>下面，找到<code>index.js</code>文件。 发现错误都出现在<code>require</code>导入中。</p>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535f328d95cd482e9247cd2d4bede2a2~tplv-k3u1fbpfcp-watermark.image" height="400" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p><strong>原因：</strong><code>require</code>导入是<code>CommonJS标准</code>，这是主要出现在node中的方式。 所以需要在<code>webpack.config.js</code>中配置<code>target</code></p>
</blockquote>
<blockquote>
<p>具体配置可查官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Ftarget%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/target/" ref="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></p>
</blockquote>
<blockquote>
<p>构建目标(Targets)</p>
</blockquote>
<blockquote>
<p>webpack 能够为多种环境或 target 构建编译。target 告知 webpack 为目标(target)指定一个环境。默认值为 "browserslist"，如果没有找到 browserslist 的配置，则默认为 "web"</p>
</blockquote>
<p>所以将<code>target</code>设置成为'node'即可， <code>webpack.config.js</code>配置文件中添加<code>target: 'node'</code></p>
<p>这下使用<code>npm run start</code>命令成功运行起来了，并且<strong>好像</strong>没有报错啦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/000acbdf068d48df8fff9f7f9693b095~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<hr>
<br>
<p>现在运行<code>npm run start</code>命令，出现了下面的运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60ef0020be434b36a93df7675be050c8~tplv-k3u1fbpfcp-watermark.image" alt="热更新错误3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>既然说 <code>Compiled successfully.</code>已经成功，那么在相应的TypeScript文件夹下应该有对应的<strong>tsc_out.js</strong>生成了。</p>
<p><strong>但是</strong>，我没找到生成的js文件，不应该呀。 然后赶紧排查原因：</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR;
  d0[热更新JS文件未生成] -.-> d1[排查原因] -.-> 是否生成到其他文件夹 -.-> 否
  d1 -.-> 是否运行脚本错误 -.-> 否
  d1 -.-> 查看是否devServer配置错误 -.-> 是
</code></pre>
<p>发现使用热更新命令运行虽然成功了，但是热更新是编译的文件是存放在<strong>内存</strong>当中的，所以肯定在相应配置的<code>output</code>输出位置找不到对应的打包文件了</p>
<p>如果想要在对应位置热更新后产生相应的输出文件，需要在<code>webpack.config.js</code>中配置<code>devServer</code>时多添加一句：<strong>writeToDisk: true</strong></p>
<p>这句命令可以将产生的文件写入硬盘。 写入位置为 <code>output.path</code> 配置的目录 （<code>writeToDisk</code>我其实找了好久，才在官方文档中找到的，泪目）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">devServer: &#123;
    <span class="hljs-attr">progress</span>: <span class="hljs-literal">false</span>,  <span class="hljs-comment">// 命令行中会显示打包的进度</span>
    <span class="hljs-attr">liveReload</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">9000</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'tsc_out.js'</span>,
    <span class="hljs-attr">writeToDisk</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 将产生的文件写入硬盘。 写入位置为 output.path 配置的目录</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，使用热更新<code>npm run start</code>命令运行后，就会产生对应的<strong>tsc_out.js</strong>文件了</p>
<p><strong>不过</strong> ，每次更新ts后，虽然相应的tsc_out.js文件会自动改变，但是每次更新保存后也会多出两个<strong>main.xxx.js</strong>文件</p>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a617f25ba5d4d40915ad60586fcd3c6~tplv-k3u1fbpfcp-watermark.image" height="400" loading="lazy" referrerpolicy="no-referrer">
<p>所以这种情况依旧要需靠配置避免。</p>
<p>可以给 <strong>devServer.writeToDisk</strong> 传入一个函数用来筛选哪些文件需要写入硬盘。 使用正则表达式来对写入硬盘的文件名次进行筛选</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">writeToDisk: <span class="hljs-function">(<span class="hljs-params">filename</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-regexp">/tsc_out.js/</span>.test(filename);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功效果：</p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feaeeef7d8e445a984e2472e54cab744~tplv-k3u1fbpfcp-watermark.image" height="400" loading="lazy" referrerpolicy="no-referrer">
<p>至此，通过<code>webpack</code>进行热更新后时时打包生成<code>typescript</code>的编译js文件就完成了</p>
<br>
<hr>
<br>
<h2 data-id="heading-3">总结</h2>
<p>这次的热更新打包过程真的是跌跌撞撞，一个萝卜一个坑。</p>
<p>本篇文章的重点其实并不在于如何打包<code>typescript</code>，反而是在于如何配置<code>webpack</code>的热更新<code>devServer</code></p>
<p>关于如何在<code>webpack5</code>中配置<code>typescript</code>，我发现在官方网站上也有说明：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Ftypescript%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/guides/typescript/" ref="nofollow noopener noreferrer">webpack.docschina.org/guides/type…</a></p>
<p>虽然遇到了许多麻烦和报错，不过最终还是完成了配置</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e08a7e3ed22450ca7fc8d0303781fb3~tplv-k3u1fbpfcp-watermark.image" align="middle" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            