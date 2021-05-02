
---
title: 'Electron + Puppeteer + Robotjs 实现工作自动化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec2692c247f1476c809a4af2346ab209~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 02 May 2021 00:20:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec2692c247f1476c809a4af2346ab209~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当年在百度搜索团队的时候做的一个小工具，可以把一些日常工作自动化，确实解决了一些问题。正值五一，分享点有趣的东西。希望能给大家一些启发。</p>
<h2 data-id="heading-1">故事的开始</h2>
<p>就在不久之前，我入职了百度的搜索团队，参与 pc 搜索的一些业务。搜索业务这么多年，历史积累的技术债务蛮多的，其中影响效率的主要是开发过程的问题。比如，首页经常要切换登录态和非登录态来看效果，每次切换都要手动输入用户名密码，而且因为有的 http 的资源会涉及跨域而失败，需要单独请求下。比如，每次上线之前都要过几遍 checklist，繁琐也花时间，所以几乎没人会认真的一遍遍过 checklist，等等，一些问题。而且因为我们开发时也是直接代码推到服务器来看效果，所以经常登录跳板机和切换不同机器，需要记住一些机器名和密码，也很耗费时间。我在熟悉流程和架构之余就一直在想着怎么去解决这些痛点。有一次走查，UE 和 PM 说每次走查的登录都好麻烦哦。听到这，发现这是个共性问题，就觉得可以正式着手做了。</p>
<h2 data-id="heading-2">最初的目标</h2>
<p>最开始的目标就是一键登录和退出登录，一键跑 checklist，还有一键登录跳板机和一键切环境，涉及到浏览器的自动化，自然就想到了 puppeteer，一个用于前端自动化测试的库。而登录跳板机和切换登录的机器不在浏览器中，需要涉及到系统的自动化（鼠标和键盘事件等），最后选择了 robotjs。这俩库都是在node环境下才能跑的，而UE和PM的电脑不会装 node，加上功能多了以后有个图形界面会更好，就想到了 electron（提供node环境和图形界面）。</p>
<p>先简单介绍下这三门技术：</p>
<h4 data-id="heading-3">1. Puppeteer</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec2692c247f1476c809a4af2346ab209~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Puppeteer 是一个 Node 库，它提供了一些高级API来通过 DevTools 协议控制 Chromium 或 Chrome。</p>
<p>它能做的很多，比如：</p>
<ul>
<li>生成页面的截图和PDF；</li>
<li>抓取 SPA 并生成预渲染的内容（即“SSR”）；</li>
<li>从网站抓取内容；</li>
<li>自动表单提交，UI 测试，键盘输入等；</li>
<li>创建一个最新的自动化测试环境。 使用最新的 JavaScript 和浏览器功能，直接在最新版本的 Chrome 中运行测试；</li>
<li>捕获你网站的 Timeline Trace，来帮助诊断性能问题；</li>
</ul>
<p><strong>Most things that you can do manually in the browser can be done using Puppeteer!</strong></p>
<p>它提供了这些api</p>
<ul>
<li>Puppeteer：通过DevTools协议与浏览器通信，创建Browser实例。</li>
<li>Browser：浏览器实例，可以拥有多个BrowserContext。</li>
<li>BrowserContext：定义了一个浏览会话，可以拥有多个Page。</li>
<li>Page：至少有一个Frame：主框架。 可能存在由iframe或框架标签创建的其他帧。</li>
<li>Frame: 至少有一个执行上下文 - 默认执行上下文 - 执行框架的JavaScript。 Frame可能有与扩展相关联的其他执行上下文。</li>
<li>Worker: 具有单个执行上下文，便于与WebWorkers交互。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6979f6c9993b4a30842e783587a02d50~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">2. Robotjs</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08d6d6b326af48fa8540c30e76bd72b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Robotjs 是 nodejs 的第一个用于桌面自动化的库。他能自动化鼠标、键盘和读取屏幕，并且提供了 Mac, Windows, Linux 的跨平台支持。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd7ed723c3c04a2681c76026031b9846~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ec7971d1ae34c01895a8beb2f6d1571~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">3. Electron</h4>
<p>Electron 可以让你使用纯 JavaScript 调用丰富的原生(操作系统) APIs 来创造桌面应用。 你可以把它看作一个 Node. js 的变体，它专注于桌面应用而不是 Web 服务器端。</p>
<p>Electron进程分为主进程和渲染进程，Electron 运行 package.json 的 main 脚本的进程被称为主进程。 在主进程中运行的脚本通过创建web页面来展示用户界面。 一个 Electron 应用总是有且只有一个主进程， 每个 Electron 中的 web 页面运行在它的叫渲染进程的进程中。所以做 electron 应用会经常用到 ipc 来做进程通信，很多操作只能在主进程做。</p>
<p>之后界面的展示用任何组件方案都可以，本来想用 san（百度的前端框架），但是 san 没有 electron 的脚手架，考虑到效率，暂时选用了 electron-vue 来创建项目。</p>
<h2 data-id="heading-6">最初的用户</h2>
<p>最初的版本的走查工具，界面是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fb3537f883b4dbfbc1ed77b771d6bf3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入 url，点击登录，就是通过 puppeteer 来启动一个浏览器，并且自动跳转到登录页面，输入用户名密码，之后点击登录，跳转到输入的 url。这里只是 pc 的，移动端的话启动的时候设置下 ua 就好了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">browser = <span class="hljs-keyword">await</span> puppeteer.launch(&#123;
  <span class="hljs-attr">executablePath</span>: getConfig(<span class="hljs-string">'chromePath'</span>),
  <span class="hljs-attr">headless</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">defaultViewport</span>: &#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">args</span>: [
    <span class="hljs-string">'--allow-running-insecure-content'</span>, 
    <span class="hljs-string">'--disable-web-security'</span>,
    <span class="hljs-string">'--auto-open-devtools-for-tabs'</span>
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动浏览器的时候通过 <strong>headless</strong> 设置为 false，puppeteer 支持启动没有界面的浏览器，主要是用于自动化测试，但我们这里需要界面。</p>
<p>然后通过 <strong>executablePath</strong> 指定一个本地的 chrome 的启动路径，可以在设置里面修改（一般 chrome 的路径是固定的），这样使用本地的 chrome 来跑，不用连 chrome 一起打包进去。</p>
<p><strong>defaultViewport</strong> 设置为 width:0 和 height:0 是为了让内容自动适应窗口大小。</p>
<p><strong>--allow-running-insecure-content</strong> 和 <strong>--disable-web-security</strong> 可以禁止同源策略，这样 https 网站加载 http 的跨域资源也不会报错。</p>
<p><strong>--auto-open-devtools-for-tabs</strong> 可以打开新 tab 自动打开 dev tools（这个后续可以加到设置中去让用户自己设置）。</p>
<p>之后又顺手做了一个屏幕取色的功能，考虑到 ue 走查时可能会用到，实现是通过 ox-mouse 来监听系统鼠标事件，然后通过 robotjs 来获取鼠标所在位置的颜色，之后发送到 colorpicker 窗口做显示。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> mouseEvent <span class="hljs-keyword">from</span> <span class="hljs-string">'osx-mouse'</span>
<span class="hljs-keyword">import</span> robot <span class="hljs-keyword">from</span> <span class="hljs-string">'robotjs'</span>

 <span class="hljs-keyword">const</span> mouseTrack = mouseEvent()
 mouseTrack.on(<span class="hljs-string">'move'</span>, <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> color = <span class="hljs-string">'#'</span> + robot.getPixelColor(<span class="hljs-built_in">parseInt</span>(x), <span class="hljs-built_in">parseInt</span>(y))
    <span class="hljs-keyword">const</span> colorPickerWin = BrowserWindow.getAllWindows().filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.name === <span class="hljs-string">'colorPickerWin'</span>)[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">if</span> (colorPickerWin) &#123;
      colorPickerWin.webContents.send(<span class="hljs-string">'color'</span>, color)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最初的两个用户（PM 和 UE）都给了一致的肯定，这让我很开心。</p>
<h2 data-id="heading-7">扩展更多边界</h2>
<p>因为有了最初的一个场景的成功实践，后面也就更有热情去做了。最初的目标更多还是针对开发者，所以开发者版本独立做了一个工具。这方面可以应用的场景就多了。</p>
<p>最开始做的事自动登录跳板机和自动切环境的功能，真实的流程是打开终端，输入ssh链接跳板机的命令，然后输入密码并且手机认证，手机认证这部分暂时没有做自动化，也最好不要去做自动化，把之前的那些都做了自动化。最终效果是一点登录跳板机，就可以在如流手势认证登陆了。实现还是通过robotjs，先输入command + space打开spotlight，然后输入terminal.app，之后输入命令和密码。过程比较傻瓜式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">spolightOpen</span>(<span class="hljs-params">appName</span>) </span>&#123;
  robot.keyTap(<span class="hljs-string">'space'</span>, [<span class="hljs-string">'command'</span>])
  <span class="hljs-keyword">await</span> delayPromise(<span class="hljs-number">500</span>)
  robot.keyTap(<span class="hljs-string">'delete'</span>)
  robot.typeString(appName)
  <span class="hljs-keyword">await</span> delayPromise(<span class="hljs-number">2000</span>)
  robot.keyTap(<span class="hljs-string">'enter'</span>)
  <span class="hljs-keyword">await</span> delayPromise(<span class="hljs-number">1000</span>)
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sshLogin</span>(<span class="hljs-params">params</span>) </span>&#123;
  <span class="hljs-keyword">await</span> spolightOpen(<span class="hljs-string">'terminal.app'</span>)

  robot.typeString(<span class="hljs-string">'ssh xxx@baiduxxx.com'</span>)
  robot.keyTap(<span class="hljs-string">'enter'</span>)
  <span class="hljs-keyword">await</span> delayPromise(<span class="hljs-number">1000</span>)
  robot.typeString(<span class="hljs-string">'xxxxxx'</span>)
  robot.keyTap(<span class="hljs-string">'enter'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自动跑 checklist 是自动化测试的范畴，puppeteer 很拿手，只要把操作步骤写成脚本，然后在一些状态下做效果的验证就可以了。</p>
<p>做完这些功能后，又会想到自动创建 icafe（百度内部的项目管理平台）卡片（把 mrd（需求描述文档） 的内容拿过来自动粘贴，自动输入一些信息之后创建卡片，并且把关联 cr 的代码复制下来），自动创建提测单，自动创建上线单，自动发排期邮件，自动发周报等等。</p>
<p>很多平时手动的做的事情都可以自动来完成，包括浏览器里的和系统级别的。</p>
<p>慢慢想到这一个个的功能都是围绕代码库的，那是不是应该做一个代码库的管理，然后围绕代码库的开发周期来做工具链的集成。</p>
<h2 data-id="heading-8">开发工具基本成型</h2>
<p>这个阶段我对开发工具的定义是做代码库的管理，（比如首页分了好多模块，可以通过分类把一些模块归到一起管理），并且围绕代码库的开发流程提供一系列提效工具。可以通过插件来扩展工具链。</p>
<p>大概设计的界面是这样的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d77cdbf57d54802a6b16f5ccd4cf818~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个代码库都可以在创建时输入本地路径和 icode（百度内部的代码托管平台） 路径还有相关的开发和 pm 等信息，这样可以一键用 ide 打开本地代码库，在详情里可以看到相关的人员的信息，并且点击名字可以一键打开如流中对应人员的对话框（基于 robotjs）。</p>
<p>然后会扫描代码库下的 package.json 中的 npm scripts，可以在界面上执行，也可以选择在系统的 terminal 或者 ide 的 terminal 中执行。</p>
<p>选择开发流程会看到每个阶段的tab，每个tab下有这个阶段可能用到的工具，比如开发时的一键登录跳板机和切环境，排期阶段的自动发排期邮件，自动创建icafe卡片，自测阶段的自动登录退出，上线阶段的自动创建提测单等功能，实现方式一样，就是模拟用户的操作，通过浏览器自动化和系统的自动化来代替人来完成一些工作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cb62198b57040e1b2d075c4487c7a68~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为开发流程的入口藏得比较深却很常用，又单独提到了左侧。此外一些其他的工具也很常用，可以放到工具箱里面，比如可视化删除本地 node_modules，屏幕取色，屏幕尺子等等。</p>
<p>工具箱中工具有两种触发方式，一键触发和定时任务触发，比如每两周都自动列一下可用的会议室，然后准备好邮件，只需要确认下信息，然后点发送就可以自动订会议室，有的工具不需要定时功能。定时功能的实现是通过 node-schedule，它的api风格是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> schedule = <span class="hljs-built_in">require</span>(<span class="hljs-string">'node-schedule'</span>);

<span class="hljs-keyword">const</span>  scheduleCronstyle = <span class="hljs-function">()=></span>&#123;
  <span class="hljs-comment">//每分钟的第30秒定时执行一次:</span>
    schedule.scheduleJob(<span class="hljs-string">'30 * * * * *'</span>,<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'scheduleCronstyle:'</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
    &#125;); 
&#125;

scheduleCronstyle();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 * * * * * * 来指定时间间隔</p>
<pre><code class="copyable">*  *  *  *  *  *
┬ ┬ ┬ ┬ ┬ ┬
│ │ │ │ │  |
│ │ │ │ │ └ day of week (0 - 7) (0 or 7 is Sun)
│ │ │ │ └───── month (1 - 12)
│ │ │ └────────── day of month (1 - 31)
│ │ └─────────────── hour (0 - 23)
│ └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, OPTIONAL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个工具的思路是围绕代码库的开发流程的一些自动化工具，基于 puppeteer 和 robotjs，不同的场景下需要的工具不同，所以插件功能是很有必要的，如果插件足够丰富以后，我们可以在开发时选择适合自己场景的插件来安装，会自动添加一些阶段的工具。当然，这个还没有实现。</p>
<p>设置里面是设置各种账号信息，和一些功能的开启关闭等。</p>
<p>锁屏就是利用了系统的锁屏，中午出去吃饭前点一下就可以了。</p>
<p>开发到这里时，距离刚开始的想法已经过去半个月了，虽然还没有开发完成，但是这个工具的定义有了比较清晰的认知。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe35f8a54cbd4de29938bc564c77ee7d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">回顾</h2>
<h4 data-id="heading-10">雪中送炭和锦上添花</h4>
<p>把一个小工具做的比较大以后，会有些怀疑这个工具的必要性，但最终还是觉得它是有意义的。首先，他解决了我在pc场景下的痛点问题，自动登录退出、自动跑checklist、一键登录跳板机和切环境等，这是这个工具解决的比较痛点的问题，属于“雪中送炭”的功能。后面有些功能有更好，没有也不会影响很大，属于“锦上添花”的功能。</p>
<p>但提供插件机制之后，可以针对不同场景的痛点问题做更多的扩展，集成更多“雪中送炭”的功能。所以提供了代码库管理和划分开发流程还有提供插件机制会使得这个工具更有想象空间。</p>
<p>那天群里开玩笑说你可能需要这个工具的20个理由，其实没有达到，现在也就3、4个用这个工具的理由，但随着不断地完善，可能他会成为开发时很重要的一个辅助工具呢。</p>
<h4 data-id="heading-11">过程中的一些坑</h4>
<p>不得不说，electron 的坑是真的多，我简单列一下几个重要的。</p>
<ol>
<li>
<p>electron 提供的 node 环境中 node 版本和本地的 node 版本要分开，运行时如果报版本不兼容，你再怎么更新本地 node 版本也没用，要去更新 electron 版本，electon 版本和内置 node 版本的关系可以去官网查。因为包依赖的是 electron 版本，所以一些二进制包用 npm rebuild xxx 也是没用的，要用 electron-rebuild xxx。</p>
</li>
<li>
<p>electron 默认没有提供任何快捷键，所以打包后，你发现在输入框中 command + v 都不管用，这需要自己去设置。但不能触发别的应用的快捷键这一点对之前实现的系统自动化的功能有毁灭性的打击，因为实现系统自动化时时大量用到了别的应用的快捷键，但打包后发现不支持！绞尽脑汁思考后想出了一种方案，mac 应用内不支持触发别的系统的快捷键，父子进程都不行，那么两个独立的进程不久可以了，所以在本地起了一个单独的服务器，通过请求的参数来触发不同的自动化功能。但是多了一个应用外的本地服务器的依赖，还没想好应用应该如何去分发和管理。但至少是可行的。</p>
</li>
</ol>
<h2 data-id="heading-12">最后</h2>
<p>最初只是为了做个自动化的登录的工具，但做着做着发现可以做更多，很多场景下是需要一些自动化工具的。他能把我们工作中一些耗费时间却没有多大必要去手动做的事情给自动完成，释放我们的时间做一些更有意义的事情。插件机制让它变得更有想象空间，也许可以围绕这个工具形成生态。</p></div>  
</div>
            