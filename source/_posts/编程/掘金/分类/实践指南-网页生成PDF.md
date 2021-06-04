
---
title: '实践指南-网页生成PDF'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db647c98b3b4f43bfa86c4566b875f3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 04:11:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db647c98b3b4f43bfa86c4566b875f3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>开发工作中，需要实现网页生成 PDF 的功能，生成的 PDF 需上传至服务端，将 PDF 地址作为参数请求外部接口，这个转换过程及转换后的 PDF 不需要在前端展示给用户。</p>
<h1 data-id="heading-1">二、技术选型</h1>
<p>该功能不需要在前端展示给用户，为节省客户端资源，选择在服务端实现网页生成 PDF 的功能。</p>
<h2 data-id="heading-2">1. Puppeteer</h2>
<p><a href="https://pptr.dev/" target="_blank" rel="nofollow noopener noreferrer">Puppeteer</a> 是一个 <code>Node</code> 库，它提供了高级 <code>API</code> 来通过 <code>DevTools</code> 协议控制 <code>Chrome</code> 或 <code>Chromium</code>。</p>
<p>在浏览器中手动执行的大多数操作都可以使用 <code>Puppeteer</code> 完成，比如：</p>
<ul>
<li>生成页面的屏幕截图和 PDF；</li>
<li>爬取 <code>SPA</code> 并生成预渲染的内容（即 <code>SSR</code>）；</li>
<li>自动进行表单提交，UI 测试，键盘输入等；</li>
<li>创建最新的自动化测试环境。使用最新的 <code>JavaScript</code> 和浏览器功能，直接在最新版本的 <code>Chrome</code> 中运行测试；</li>
<li>捕获时间线跟踪网站，以帮助诊断性能问题；</li>
<li>测试 <code>Chrome</code> 扩展程序。</li>
</ul>
<p>从上可见，<code>Puppeteer</code> 可以实现在<code>Node</code> 端生成页面的 PDF 功能。</p>
<h1 data-id="heading-3">三、实现步骤</h1>
<h2 data-id="heading-4">1. 安装</h2>
<p>进入项目，安装 <code>puppeteer</code> 到本地。</p>
<pre><code class="copyable">$ npm install -g cnpm --registry=https://registry.npm.taobao.org
$ cnpm i puppeteer --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需注意的是，安装 <code>puppeteer</code> 时，会下载与 <code>API</code> 一起使用的最新版本的 <code>Chromium</code> 浏览器，有以下方法可以修改默认设置，不下载浏览器：</p>
<ol>
<li>在<a href="https://github.com/puppeteer/puppeteer/blob/v8.0.0/docs/api.md#environment-variables" target="_blank" rel="nofollow noopener noreferrer">环境变量</a>中设置 <code>PUPPETEER_SKIP_CHROMIUM_DOWNLOAD</code>；</li>
<li>用 <code>puppeteer-core</code> 代替 <code>puppeteer</code>。</li>
</ol>
<p><code>puppeteer-core</code> 是 <code>puppeteer</code> 的轻量级版本，默认不下载浏览器，而是启动现有的浏览器或者连接远程浏览器，使用 <code>puppeteer-core</code> 需注意本地有可连接的浏览器，且安装的 <code>puppeteer-core</code> 版本与打算连接的浏览器兼容。连接本地浏览器方法如下：</p>
<pre><code class="copyable">const browser = await puppeteer.launch(&#123; 
  executablePath: '/path/to/Chrome' 
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本项目需要部署至服务端，没有可连接的浏览器，因此选择安装的是 <code>puppeteer</code>。</p>
<h2 data-id="heading-5">2. 启动浏览器</h2>
<pre><code class="copyable">const browser = await puppeteer.launch(&#123;
    headless: true,
    args: ['--no-sandbox', '--font-render-hinting=medium']
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>headless</code> 代表无头模式，在后端启动浏览器，前端不会有展示。</p>
<blockquote>
<p>小建议：本地调试时，建议设置 <code>headless: false</code>，可以启动完整版本的浏览器，直接在浏览器窗口查看内容。</p>
</blockquote>
<h2 data-id="heading-6">3. 打开新页面</h2>
<p>生成浏览器后，在浏览器中打开新页面。</p>
<pre><code class="copyable">const page = await browser.newPage()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">4. 跳转到指定页面</h2>
<p>跳转至要生成 PDF 的页面。</p>
<pre><code class="copyable">await page.goto(`$&#123;baseURL&#125;/article/$&#123;id&#125;`, &#123;
    timeout: 60000,
    waitUntil: 'networkidle2', // networkidle2 会一直等待，直到页面加载后不存在 2 个以上的资源请求，这种状态持续至少 500 ms
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>timeout</code> 是最长的加载时间，默认 30s，网页加载时间长的情况下，建议将 <code>timeout</code> 值改大，防止超时报错。</p>
<p><code>waitUntil</code> 表示页面加载到什么程度可以开始生成 PDF 或其他操作了，当网页需加载的图片资源较多时，建议设置为 <code>networkidle2</code>，有以下值可选：</p>
<ul>
<li>load：当 <code>load</code> 事件触发时；</li>
<li>domcontentloaded： 当 <code>DOMContentLoaded</code> 事件触发时；</li>
<li>networkidle0： 页面加载后不存在 0 个以上的资源请求，这种状态持续至少 500 ms；</li>
<li>networkidle2： 页面加载后不存在 2 个以上的资源请求，这种状态持续至少 500 ms。</li>
</ul>
<h2 data-id="heading-8">5. 指定路径，生成pdf</h2>
<p>上述指定的页面加载完成后，将该页面生成 PDF。</p>
<pre><code class="copyable">  const ext = '.pdf'
  const key = randomFilename(title, ext)
  const _path = path.resolve(config.uploadDir, key)
  await page.pdf(&#123; path: _path, format: 'a4' &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>path</code> 表示将 PDF 保存到的文件路径，如果未提供路径，PDF 将不会保存至磁盘。</p>
<blockquote>
<p>小建议：不管 PDF 是不是需要保存到本地，建议在调试的时候都设置一个path，方便查看生成的 PDF 的样式，检查是否有问题。</p>
</blockquote>
<p><code>format</code> 表示 PDF 的纸张格式，a4 尺寸为 8.27 英寸 x 11.7 英寸，是传统的打印尺寸。</p>
<blockquote>
<p>注意：目前仅支持headless: true 无头模式下生成 PDF</p>
</blockquote>
<h2 data-id="heading-9">6. 关闭浏览器</h2>
<p>所有操作完成后，关闭浏览器，节约性能。</p>
<pre><code class="copyable">  await browser.close()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">四、难点</h1>
<h2 data-id="heading-11">1. 图片懒加载</h2>
<p>由于需生成 PDF 的页面是文章类型的页面，包含大量图片，且图片引入了懒加载，导致生成的 PDF 会带有很多懒加载兜底图，效果如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db647c98b3b4f43bfa86c4566b875f3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方法是跳转到页面后，将页面滚动到底部，所有图片资源都会得到请求，<code>waitUntil</code> 设置为 <code>networkidle2</code>，图片就能加载成功了。</p>
<pre><code class="copyable">await autoScroll(page) // 因为文章图片引入了懒加载，所以需要把页面滑动到最底部，保证所有图片都加载出来

/**
 * 控制页面自动滚动
 * */
function autoScroll (page) &#123;
  return page.evaluate(() => &#123;
    return new Promise<void>(resolve => &#123;
      let totalHeight = 0
      const distance = 100
      // 每200毫秒让页面下滑100像素的距离
      const timer = setInterval(() => &#123;
        const scrollHeight = document.body.scrollHeight
        window.scrollBy(0, distance)
        totalHeight += distance
        if (totalHeight >= scrollHeight) &#123;
          clearInterval(timer)
          resolve()
        &#125;
      &#125;, 200)
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里用到了 <code>page.evaluate()</code> 方法，用来控制页面操作，比如使用内置的 <code>DOM</code> 选择器、使用 <code>window</code> 方法等等。</p>
<h2 data-id="heading-12">2. CSS 打印样式</h2>
<p>根据<a href="https://pptr.dev/#?product=Puppeteer&version=v8.0.0&show=api-pagepdfoptions" target="_blank" rel="nofollow noopener noreferrer">官网</a>说明，<code>page.pdf()</code> 生成 PDF 文件的样式是通过 <code>print css media</code> 指定的，因此可以通过 <code>css</code> 来修改生成的 PDF 的样式，以本文需求为例，生成的 PDF 需要隐藏头部、底部，以及其他和文章主体无关的部分，代码如下：</p>
<pre><code class="copyable">@media print &#123;
  .other_info,
  .authors,
  .textDetail_comment,
  .detail_recTitle,
  .detail_rec,
  .SuspensePanel &#123;
    display: none !important;
  &#125;

  .Footer,
  .HeaderSuctionTop &#123;
    display: none;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">3. 登录态</h2>
<p>由于存在一部分文章不对外部用户公开，需要鉴权用户身份，符合要求的用户才能看到文章内容，因此跳转到指定文章页后，需要在生成的浏览器窗口中注入登录态，符合条件的登录用户才能看到这部分文章的内容。</p>
<p>采用注入 <code>cookie</code> 的方式来获取登录态，使用 <code>page.evaluate()</code> 设置 <code>cookie</code>，代码如下：</p>
<pre><code class="copyable">
async function simulateLogin (page, cookies, domain) &#123;
  return await page.evaluate((sig, sess, domain) => &#123;
    let date = new Date()
    date = new Date(date.setDate(date.getDate() + 1))
    let expires = ''
    expires = `; expires=$&#123;date.toUTCString()&#125;`
    document.cookie = `koa:sess.sig=$&#123;sig&#125;$&#123;expires&#125;; domain=$&#123;domain&#125;; path=/`
    document.cookie = `koa:sess=$&#123;sess&#125;=$&#123;expires&#125;; domain=$&#123;domain&#125;; path=/` // =是这个cookie的value
    document.cookie = `is_login=true$&#123;expires&#125;; domain=$&#123;domain&#125;; path=/`
  &#125;, cookies['koa:sess.sig'], cookies['koa:sess'], domain)
&#125;


await simulateLogin(page, cookies, config.domain.split('//')[1])
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>小建议：<code>Puppeteer</code> 也有自带的 <code>api</code> 实现 <code>cookie</code> 注入，如 <code>page.setCookie(&#123;name: name, value: value&#125;)</code>，但是我用这个方式注入没能获取到登录态，没有找到具体原因，建议还是直接用我上面这个方法来注入 <code>cookie</code>，注意除 <code>name</code> 和 <code>value</code>外，<code>expires</code>、<code>domain</code>、<code>path</code> 也需要配置。</p>
</blockquote>
<h2 data-id="heading-14">4. Docker 部署 Puppeteer</h2>
<p>根据上文操作，本地已经可以成功将页面生成 PDF 了，本地体验没问题后，需要部署到服务端给到测试、上线。</p>
<p>没有修改 <code>Dockerfile</code> 时，部署后发现了如下错误：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e9657215003430da008e04d24f97c79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>官网有给 <a href="https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md#running-puppeteer-in-docker" target="_blank" rel="nofollow noopener noreferrer">Docker 配置说明</a>可以参考，最终实践可用的 <code>ubuntu</code> 系统的 <code>Dockerfile</code> 如下：</p>
<pre><code class="copyable"># ...省略...

# 安装 puppeteer 依赖
RUN apt-get update && \
    apt-get install -y libgbm-dev && \
    apt-get install gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev -y && \
    apt-get install -y fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf --no-install-recommends

# ...省略...

<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要重点关注 <strong>安装 puppeteer 依赖</strong> 部分即可。</p>
<blockquote>
<p>注意：在 v1.18.1 之前，Puppeteer 至少需要 Node v6.4.0。从 v1.18.1 到 v2.1.0 的版本都依赖于 Node 8.9.0+。从 v3.0.0 开始，Puppeteer 开始依赖于 Node 10.18.1+。配置 Dockerfile 时也需要注意服务端的 node 版本。</p>
</blockquote>
<h1 data-id="heading-15">五、总结</h1>
<p>本文讲述了实现在 <code>Node</code> 端将网页生成 PDF 文件的完整过程，总结为以下 3 点：</p>
<ol>
<li>技术选型，根据需求场景选择合适的手段实现功能；</li>
<li>阅读<a href="https://pptr.dev/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>，快速过一遍文档才能少遇到些坑；</li>
<li>破解难点，使用一个未使用的工具，会遇到没有解决过的难题，遇招拆招吧 ^ ^。</li>
</ol>
<p>参照 <a href="https://github.com/jiaozitang/puppeteerPdfDemo" target="_blank" rel="nofollow noopener noreferrer">Demo 源码</a> 可快速上手上述功能，希望本文能对你有所帮助，感谢阅读❤️</p>
<hr>
<p><strong>· 往期精彩 ·</strong></p>
<p><a href="https://jelly.jd.com/article/5e6f8438ee9d090158673fdf" target="_blank" rel="nofollow noopener noreferrer">【直播回顾·程序媛的成长蜕变】</a></p>
<p><a href="https://jelly.jd.com/article/5e734631affa8301490877f1" target="_blank" rel="nofollow noopener noreferrer">【大规格文件的上传优化】</a></p>
<p><a href="https://jelly.jd.com/article/5e1c27c6d2fcd20149f6f560" target="_blank" rel="nofollow noopener noreferrer">【JDR DESIGN 开发小结】</a></p></div>  
</div>
            