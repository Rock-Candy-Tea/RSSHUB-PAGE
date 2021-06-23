
---
title: 'uTools 开源了？赶紧上车！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffde44e815c0478494605d1192685b15~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 04:48:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffde44e815c0478494605d1192685b15~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>话不多说，先放上截图和仓库地址：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffde44e815c0478494605d1192685b15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码仓库：<a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">github</a></p>
<h2 data-id="heading-0">故事背景</h2>
<h3 data-id="heading-1">网络抓包</h3>
<p>之前公司内部因为开发需要，需要和后端进行接口联调，测试环境的时候，经常会涉及到一些状态改变要看交互样式的问题。比如测试需要测商品的待支付、支付中、支付完成等各种节点的交互样式是否符合预期，这种情况测试一般会去造数据或者让后端改数据库接口。
有的小伙伴可能会用<code>Charles</code>修改返回数据进行测试。但是<code>Charles</code>的抓包体验和配置体验感觉有点麻烦，不是很友好，所以我们自己做了个<code>抓包&mock</code>工具：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe19cfe19ff4fb099202c7a87addc7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>傻瓜式交互一次性解决：抓包、代理、请求转发、接口数据篡改mock、跨域访问 等能力，并得到了广泛使用和好评。</p>
<h3 data-id="heading-2">文件上传</h3>
<p>随着项目开发的继续，有些用户给我们反馈页面加载图片资源比较慢，我们看了一下很多图片资源都没有经过压缩处理，这个时候我们可以通过 <code>webpack</code> 写了一些 <code>loader</code> 来对图片资源进行压缩处理。这个时候我们的图片资源大部分是存放在项目目录下。而有的时候，我们是需要将图片存放于 <code>cdn</code> 上的，此时我们又需要一个图床工具，可以在线存储图片资源。于是乎，我们又整合了图片压缩和上传的功能，做了个图床工具：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/542fcabe595740e19665e8f07edb3e99~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">性能测评</h3>
<p>开发者开发页面的时候，需要对页面的性能进行评估，另一方面也可以把评估报告通知给测试同学，对其进行性能测试。之前大多采用的是 <code>chrome</code> 插件 <code>lighthouse</code> 来做。但是这个东西对未登录用户无法做到性能评估，因为用户未登录直接测评了登录页面，显然不符合预期，其次，每个电脑上都得安装插件，受限于设备的不同，可能会导致性能没有同一的变量（网络、网速、分辨率、CUP等）。所以我们基于 <code>pupeeteer-core</code>以及<code>electron</code> 做了一个免登的测评工具：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2ce2d6baad343e49a2b589f1fc9f63a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这些还远远不够，我们随着业务的增加，功能愈发的多了起来：我们的埋点检测工具、需求管理工具、前端多环境切换工具 等等等....一方面导致 <code>electron</code> 体积变得臃肿起来，另一方面随着发布频率增加，安装下载的成本也越来越大，很多用户就不愿意再接着安装，因为确实很麻烦。所以我们需要改变，让功能不依赖与容器。这就需要把我们的功能全部独立出去，做成<strong>插件化</strong>。所以我注意到了 <a href="https://u.tools/" target="_blank" rel="nofollow noopener noreferrer">utools</a></p>
<h2 data-id="heading-4">插件化之旅</h2>
<p>一开始想到做插件化，无非就是使用 <code>electron</code> 的 <code>webview</code> 能力，实现类似于原生内嵌<code>h5</code>那样的方式，<code>h5</code> 页面可以做独立发布，原生提供 <code>nativaAPI</code> 之间通过 <code>jsBridge</code> 来桥接调用原生的方法。这样实现并无问题，我们也尝试了做了一次。最终思路大概是：</p>
<h3 data-id="heading-5">electron webview 方式</h3>
<h4 data-id="heading-6">1. electron 中使用 webview</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">webview</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://xxx.xx.com/index.html"</span> <span class="hljs-attr">preload</span>=<span class="hljs-string">"preload.js"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2. 实现 <code>bridge</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// preload.js</span>
<span class="hljs-built_in">window</span>.rubickBridge = &#123;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello world'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3. 插件借助 <code>bridge</code> 调用 <code>electron</code> 的能力</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span>></span>这是一个插件<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">window</span>.rubickBridge.sayHello()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4. 通信</h4>
<p>因为 <code>proload.js</code> 是 <code>electron</code> 的 <code>renderer</code> 进程的，所以如果需要使用部分 <code>main</code> 进程的能力，则需要使用通信机制：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main process</span>
ipcMain.on(<span class="hljs-string">'msg-trigger'</span>, <span class="hljs-keyword">async</span> (event, arg) => &#123;
    <span class="hljs-keyword">const</span> <span class="hljs-built_in">window</span> = arg.winId ? BrowserWindow.fromId(arg.winId) : mainWindow
    <span class="hljs-keyword">const</span> operators = arg.type.split(<span class="hljs-string">'.'</span>);
    <span class="hljs-keyword">let</span> fn = Api;
    operators.forEach(<span class="hljs-function">(<span class="hljs-params">op</span>) =></span> &#123;
      fn = fn[op];
    &#125;);
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fn(arg, <span class="hljs-built_in">window</span>);
    event.sender.send(<span class="hljs-string">`msg-back-<span class="hljs-subst">$&#123;arg.type&#125;</span>`</span>, data);
&#125;);
  
<span class="hljs-comment">// renderer process</span>
ipcRenderer.send(<span class="hljs-string">'msg-trigger'</span>, &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'getPath'</span>,
  name,
&#125;);
ipcRenderer.on(<span class="hljs-string">`msg-back-getPath`</span>, <span class="hljs-function">(<span class="hljs-params">e, result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(result)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">为什么后来我们又放弃了这条路🤔 ？</h3>
<p>其实上面的思路大致是没啥问题的，我们也基于上面的思路成功把功能抽成了插件，按照插件的方式进行安装加载。直到我们注意到 <code>utools</code> 的强大，感觉 <code>utools</code> 的生态非常丰富，我们要是能集成 <code>utools</code> 的生成那该多好呀！所以我们秉持着干不过他就成为他的原则，我们尝试着成为他。但是 <code>utools</code> 本身并没有开源，所以没有办法去吸取一些优秀的代码实现，但是我们可以看他的官方文档。</p>
<p>我们发现其实 <code>utools</code> 大多数插件都是和 <code>container</code> 层分离的，也就是说 <code>utools</code> 只是一个插件的容器，为插件提供了一些 <code>api</code> 能力和方法。所以一旦我们实现了<code>utools</code>加载插件的能力，实现 <code>utools</code> 的所有 <code>API</code> 函数，是不是就约等于实现了 <code>utools</code> ! 我们就可以使用 <code>utools</code> 的插件？</p>
<h3 data-id="heading-11">utools 方式</h3>
<p>按照 utools 的 文档，首先我们需要实现一个插件，必须要有个 <code>plugin.json</code>，这玩意就是用来告诉 <code>utools</code> 插件的信息。我们也按照文档来写：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"pluginName"</span>: <span class="hljs-string">"helloWorld"</span>,
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"我的第一个uTools插件"</span>,
    <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.html"</span>,
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.1"</span>,
    <span class="hljs-attr">"logo"</span>: <span class="hljs-string">"logo.png"</span>,
    <span class="hljs-attr">"features"</span>: [
        &#123;
          <span class="hljs-attr">"code"</span>: <span class="hljs-string">"hello"</span>,
          <span class="hljs-attr">"explain"</span>: <span class="hljs-string">"hello world"</span>,
          <span class="hljs-attr">"cmds"</span>:[<span class="hljs-string">"hello"</span>, <span class="hljs-string">"你好"</span>]
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是将写好的插件用 <code>utools</code> 跑起来，按照 <code>utools</code>的交互是复制 <code>plugin.json</code> 到<code>utools</code>搜索框即可，我们也可以实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听 input change</span>
<span class="hljs-comment">// 读取剪切板内容</span>
<span class="hljs-keyword">const</span> fileUrl = clipboard.read(<span class="hljs-string">'public.file-url'</span>).replace(<span class="hljs-string">'file://'</span>, <span class="hljs-string">''</span>);
<span class="hljs-comment">// 复制文件</span>
<span class="hljs-keyword">if</span> (fileUrl && value === <span class="hljs-string">'plugin.json'</span>) &#123;
  <span class="hljs-comment">// 读取 plugin.json 配置</span>
  <span class="hljs-keyword">const</span> config = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(fileUrl, <span class="hljs-string">'utf-8'</span>));
  <span class="hljs-keyword">const</span> pluginConfig = &#123;
    ...config,
    <span class="hljs-comment">// index.html 文件位置，用于webview加载</span>
    <span class="hljs-attr">sourceFile</span>: path.join(fileUrl, <span class="hljs-string">`../<span class="hljs-subst">$&#123;config.main || <span class="hljs-string">'index.html'</span>&#125;</span>`</span>),
    <span class="hljs-attr">id</span>: uuidv4(),
    <span class="hljs-attr">type</span>: <span class="hljs-string">'dev'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'image://'</span> + path.join(fileUrl, <span class="hljs-string">`../<span class="hljs-subst">$&#123;config.logo&#125;</span>`</span>),
    <span class="hljs-attr">subType</span>: (<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (config.main) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'template'</span>;
    &#125;)()
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b40162dd4c774a3ca6db2aa63c3606eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就是进行命令搜索插件:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/236e9308fa324a3bac266ff7332cd1ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现这个功能其实也就是对之前存储的<code>pluginConfig</code>的里面的 <code>features</code> 进行遍历，找到相应的 <code>cmd</code> 后进行下拉框展示即可。</p>
<p>然后我们要去实现选择功能，用 <code>webview</code> 加载页面的能力：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">webview</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"webview"</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"path"</span> <span class="hljs-attr">:preload</span>=<span class="hljs-string">"preload"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">`File://<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.$route.query.sourceFile&#125;</span>`</span>,
      <span class="hljs-attr">preload</span>: <span class="hljs-string">`File://<span class="hljs-subst">$&#123;path.join(__static, <span class="hljs-string">'./preload.js'</span>)&#125;</span>`</span>,
      <span class="hljs-attr">webview</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">query</span>: <span class="hljs-built_in">this</span>.$route.query,
      <span class="hljs-attr">config</span>: &#123;&#125;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37cf1909b1374606bdd1fbae657433c7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此结束了？并没有！！！由于篇幅的原因，我们后续再说。本出写的插件demo已上传github: <a href="https://github.com/clouDr-f2e/rubick-plugin-demo" target="_blank" rel="nofollow noopener noreferrer">github.com/clouDr-f2e/…</a></p>
<h2 data-id="heading-12">Far from enough 这只是开始</h2>
<p>接下来我们就可以参考 <code>utools</code> 交互一口气实现其大部分功能：</p>
<h3 data-id="heading-13">加载utools生态插件</h3>
<p>斗图：<a href="https://github.com/vst93/doutu-uToolsPlugin" target="_blank" rel="nofollow noopener noreferrer">github.com/vst93/doutu…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cba1eb758180433294c93b59724adefd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">窗口分离</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4de3a72c7244db898b2106b96c48416~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">utools doc 模板</h3>
<p>uTools 的插件开发给予了开发者最大的自由度，你可以随心所欲的设计页面结构、样式、交互，对于特别擅长前端开发的同学，这没有什么问题，但对于非前端开发者，要做出漂亮的、高质量的前端 UI 是一件困难的事情。</p>
<p>所以 Rubick 也实现了模板能力：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1acf7f300d2490d99aa208080e00dad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">utools 自带的系统命令</h3>
<h4 data-id="heading-17">取色</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c3e00e5f08545bcb96613689649b337~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">截屏</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18023dab52e1420c9e87362cefddb2a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">最后</h2>
<p>目前 <code>rubick</code> 已经实现 <code>utools</code> 大多数核心能力，<strong>最重要的是可以使用 utools 所有生态 ！</strong> 更多能力可以前往 github 体验。如果感觉有用，可以帮忙反手一个 star ✨</p>
<p><a href="https://github.com/clouDr-f2e/rubick" target="_blank" rel="nofollow noopener noreferrer">Rubick github</a></p></div>  
</div>
            