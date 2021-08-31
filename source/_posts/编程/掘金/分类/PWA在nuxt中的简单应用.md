
---
title: 'PWA在nuxt中的简单应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/621210d10de4484aba635c77463e6251~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 19:20:35 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/621210d10de4484aba635c77463e6251~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>PWA（Progressive Web Apps，渐进式 Web 应用）</strong> 运用现代的 Web API 以及传统的渐进式增强策略来创建跨平台 Web 应用程序。这些应用无处不在、功能丰富，使其具有与原生应用相同的用户体验优势。</p>
<p>通常用户使用pwa应用的方式是将H5页面添加到手机主屏幕（桌面），什么叫添加到主屏幕？</p>
<p><strong>添加到主屏幕</strong>（Add to Home Screen，简称 A2HS）是现代智能手机浏览器中的一项功能，使开发人员可以轻松便捷地将自己喜欢的 Web 应用程序（或网站）的快捷方式添加到主屏幕中，以便用户随后可以通过单击访问它。</p>
<p>Mobile Chrome / Android Webview 从 31 版开始支持 A2HS，Opera for Android 从 32 版开始支持，Firefox for Android 从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FMozilla%2FFirefox%2FReleases%2F58" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/58" ref="nofollow noopener noreferrer">58 版</a> 开始支持。</p>
<p>如何使我们的应用程序支持 <strong>A2HS</strong> 呢？</p>
<ul>
<li>应用通过 HTTPS 提供服务——Web 正朝着更加安全的方向发展，包括 A2HS 在内的许多现代 Web 技术都将仅工作在安全的环境中。</li>
<li>从 HTML 头链接具有正确字段的 manifest 文件。</li>
<li>有合适的图标可显示在主屏幕上。</li>
<li>Chrome 浏览器还要求该应用程序注册一个 Service Worker（这样在离线状态下就也可以运行）。</li>
</ul>
<p>详细说明可以参考: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FProgressive_web_apps%2FAdd_to_home_screen" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Progressive_web_apps/Add_to_home_screen" ref="nofollow noopener noreferrer">PWA Docs</a></p>
<p>按照上面的方法，我们讲解下如何使我们的nuxt应用支持A2HS：</p>
<ul>
<li>首先，我们的应用应该部署在 <strong>https</strong> 服务上。（这点大部分网站都是https的）</li>
<li>在nuxt中创建 <strong>manifest</strong> 文件:</li>
</ul>
<p>因为我们要在app.html中加入</p>
<pre><code class="copyable"><link rel="manifest" href="/manifest.webmanifest">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照nuxt访问路径，我们应该把manifest这种静态文件加到nuxt的static文件夹里，所以我们在static文件夹中创建manifest.webmanifest文件，这个文件的内容是定义我们的PWA桌面应用的配置。</p>
<pre><code class="copyable">&#123;
  "background_color": "#ffffff", // 安装应用时或启动应用时的背景色
  "theme_color": "#ffffff", // UI的颜色，操作系统使用的
  "description": "test pwa", // 应用描述
  "display": "standalone", // 桌面应用的壳中h5显示方式，全屏、独立、最小UI或浏览器
  "icons": [
    &#123;
      "src": "icon/36-min.png",
      "sizes": "36x36",
      "type": "image/png"
    &#125;,
    &#123;
      "src": "icon/48-min.png",
      "sizes": "48x48",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/72-min.png",
      "sizes": "72x72",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/96-min.png",
      "sizes": "96x96",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/144-min.png",
      "sizes": "144x144",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/192-min.png",
      "sizes": "192x192",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/256-min.png",
      "sizes": "256x256",
      "type": "image/png"
    &#125;,&#123;
      "src": "icon/512-min.png",
      "sizes": "512x512",
      "type": "image/png"
    &#125;
  ], // icon图标，图标尽量多种尺寸，可以支持用户不同的设备
  "name": "test", // 网站应用的全名
  "short_name": "test", // 显示在桌面的短名
  "start_url": "/?from=pwa", // 桌面应用的入口页面链接,可以带上参数来区分pwa应用打开
  "related_applications": [&#123; 
    "platform": "play",
    "id": "xxx",
    "url": "xxx"
  &#125;] // 关联google应用
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接着在nuxt应用中注册一个 <strong>serviceworker</strong></li>
</ul>
<p>我们可以在static文件夹中简单创建一个sw.js，可以在里面定义两个事件监听</p>
<pre><code class="copyable">self.addEventListener('install', (e) => &#123;
    e.waitUntil(caches.open('test-store').then((cache) => cache.addAll([
        // 可以加入你想缓存的文件列表
        '/xxxx/xxxx'
    ]))
&#125;)

self.addEventListener('fetch', (e) => &#123;
    e.respondWith(
        caches.match(e.request).then((response) => response || fetch(e.request))
    )
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了sw.js后，我们需要在window.onload的时候注册一下</p>
<pre><code class="copyable">window.addEventListener('load',function()&#123;
  if ('serviceWorker' in window.navigator) &#123;
    window.navigator.serviceWorker
      .register('sw.js')
      .then(() => &#123; console.log('Service Worker Registered'); &#125;)
      .catch(() => &#123; console.log('Service Worker Registered Failed'); &#125;);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们在上面支持A2HS的浏览器中打开我们的H5时，比如在安卓手机的chrome浏览器，点击右上角菜单，就能看到安装应用这个选项，便可以安装PWA应用到手机桌面啦。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/621210d10de4484aba635c77463e6251~tplv-k3u1fbpfcp-watermark.image" alt="2901630325820_.pic.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但实际上我们要做打包后js和静态图片文件缓存的话，应该在构建的时候将缓存的文件的路径打入到serviceworker里，对此google提供了一个插件叫 <strong>workbox-webpack-plugin</strong> ，我们在nuxt.config.js的插件配置他：</p>
<pre><code class="copyable">build: &#123;
    extend(config, &#123; isDev, isClient &#125;) &#123;
        const worboxWebpackPlugin = require("workbox-webpack-plugin")
        if (isClient) &#123;
            config.plugins.push(
                new worboxWebpackPlugin.GenerateSW(&#123;
                  cleanupOutdatedCaches: true,
                  clientsClaim: true,
                  skipWaiting: true,
                  maximumFileSizeToCacheInBytes: 10 * 1024 * 1024,
                  swDest: path.join(__dirname, '/src/static/sw.js'),
                  manifestTransforms: [
                    async (manifestEntries) => &#123;
                      const manifest = manifestEntries.filter(entry => &#123;
                        return entry.url.indexOf('../server') === -1;
                      &#125;);
                      return &#123;manifest, warnings: []&#125;;
                    &#125;
                  ]
                &#125;)
            )
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为nuxt构建是包含服务端server的文件，所以我们需要剔除他们，实际缓存的是client端的文件。
swDest是重新定义sw.js生成的路径，同样和前面demo的sw.js一样放到static文件夹里。</p>
<p>插件具体配置参数和作用可以参考： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ftools%2Fworkbox%2Freference-docs%2Flatest%2Fmodule-workbox-build%23.generateSW" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/tools/workbox/reference-docs/latest/module-workbox-build#.generateSW" ref="nofollow noopener noreferrer">developers.google.com/web/tools/w…</a></p>
<p>这样我们nuxt构建后，就会在static文件夹里生成sw.js和workbox-&#123;hash&#125;.js。</p>
<p>PWA在nuxt中的简单应用就实现了。
实际上，我们是希望用户点击H5页面的某个按钮或者提示条来触发PWA应用的安装，而不是需要用户自主点击浏览器菜单中的安装应用，这怎么实现呢？
这需要我们监听并使用浏览器的 <strong>beforeinstallprompt</strong> 事件。</p>
<p>在nuxt中，我们是通过写一个vue组件来实现一个提示条或安装按钮的，所以我们会在组件的mounted里这样写道：</p>
<pre><code class="copyable">window.addEventListener('beforeinstallprompt', (e) => &#123;
    e.preventDefault(); // 防止 Chrome 67 及更早版本自动显示安装提示
    this.deferredPrompt = e; // 保存event，点击唤起安装需要用到
    this.show(); // 触发事件时展示该组件
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后给该组件绑定一个点击事件：</p>
<pre><code class="copyable">handleClick() &#123;
    if (this.deferredPrompt) &#123;
        this.deferredPrompt.prompt();
        this.deferredPrompt.userChoice.then((choiceResult) => &#123;
          if (choiceResult.outcome === 'accepted') &#123;
            console.log('User accepted the A2HS prompt');
          &#125; else &#123;
            console.log('User dismissed the A2HS prompt');
          &#125;
          this.deferredPrompt = null;
        &#125;);
    &#125;
    this.hide(); // 点击完后隐藏该组件
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成后，我们发现组件有很大概率没有展示，也就是说我们监听的这个beforeinstallprompt事件并不能成功触发，这是为什么呢？
因为，beforeinstallprompt事件触发的时机过早，可能会比组件mounted还要早，所以如果浏览器已经触发了beforeinstallprompt事件，而我们才在组件mounted中去监听，那这个监听就不会再触发了，所以我们需要改进一下。</p>
<p>正常情况下，beforeinstallprompt事件会在window.onload后触发，我们可以在 <strong>app.html</strong> 里的script中 <strong>window.onload</strong> 的时候加个监听：</p>
<pre><code class="copyable">window.addEventListener('beforeinstallprompt',(e) => &#123;
  console.log(e);
  e.preventDefault();
  window.deferredPrompt = e;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把这个event存储在全局变量里，再修改下组件mounted里的展示判断：</p>
<pre><code class="copyable">// 如果beforeinstallprompt这个事件在window.onload后 组件mounted前就触发，那window.deferredPrompt就会是pwa的事件
if (window.deferredPrompt) &#123;
  this.deferredPrompt = window.deferredPrompt;
  this.show();
&#125; else &#123;
  // 如果beforeinstallprompt这个事件在window.onload后 组件mounted时未触发，则重新建立监听
  window.addEventListener('beforeinstallprompt', (e) => &#123;
    console.log('bar', e);
    e.preventDefault();
    this.deferredPrompt = e;
    this.show();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-0">这样就大功告成啦！</h4></div>  
</div>
            