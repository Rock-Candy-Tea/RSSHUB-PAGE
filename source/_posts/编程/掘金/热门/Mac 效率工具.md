
---
title: 'Mac 效率工具'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f59edff0c8b64b29816f37651e50b204~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 16:46:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f59edff0c8b64b29816f37651e50b204~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看： <a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战</a>」</p>
<h2 data-id="heading-0">前言</h2>
<p>使用 Mac 开发也有几个年头了，积累了一些效率工具和开发工具，今天整理了一下并分享给大家，工具几乎都是开源免费的，也期待大家有更多好的工具推荐给我，我补充上去。</p>
<h2 data-id="heading-1">包管理器</h2>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbrew.sh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://brew.sh/" ref="nofollow noopener noreferrer">Homebrew</a></h3>
<p>Homebrew 是一款 Mac OS 平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能。算是 Mac 系统的必备环境了。</p>
<p>有了它，比如你要下载下面提到的 node 环境，你根本不用考虑 node 去哪个地方下，只需要执行<code>brew install node</code>命令就好。</p>
<p>如果大家不习惯使用命令操作，还可以使用这款可视化的工具<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cakebrew.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cakebrew.com/" ref="nofollow noopener noreferrer">cakebrew</a>。</p>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">Npm</a></h3>
<p>Npm 其实是 Node.js 的包管理工具，安装 Node 后就会有 npm 环境了。有很多 npm 包是很好的工具，以我经常用的一个举例吧</p>
<h4 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fanywhere" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/anywhere" ref="nofollow noopener noreferrer">anywhere</a></h4>
<p>它可以随时随地将你的当前目录变成一个静态文件服务器的根目录，只需要你在当前目前下执行一个<code>anywhere</code>命令。</p>
<p>这样就实现了<strong>一个局域网</strong>下，文件互传的功能，我经常使用它来和同事之间传递文件，毕竟内网传递速度就是快。</p>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=https%3A%2F%2Frubygems.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rubygems.org/" ref="nofollow noopener noreferrer">Gem</a></h3>
<p>Gem 是 Ruby 模块的包管理器。如果你是 iOS 开发者，对这个一定不会陌生，因为 CocoaPods 本身就是一个 ruby 模块，我们可以通过 gem 来安装 CocoaPods，当然还可以通过 Homebrew 来安装。</p>
<h2 data-id="heading-6">日常工具</h2>
<h3 data-id="heading-7"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.snipaste.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.snipaste.com/" ref="nofollow noopener noreferrer">Snipaste</a></h3>
<p>最好用的截图工具，我要向大家强烈安利它，不仅有正常的截图、编辑等功能，还有一个其他软件都没有而且我经常用的功能 -- 贴图，可以直接将图片像便签一样贴在桌面上。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f59edff0c8b64b29816f37651e50b204~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.mweb.im%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.mweb.im/" ref="nofollow noopener noreferrer">MWeb</a></h3>
<p>专业的 Markdown 写作、记笔记、静态博客生成软件，用起来真的比较方便，其实还有会朋友推荐 Typora 这款软件，但是我不太喜欢那种预览区和编辑区在一起的方式，如果对 Typora 有兴趣的，也可以去看看。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b43cc8df710a47dbac19d807f844487f~tplv-k3u1fbpfcp-watermark.image" alt="MWeb.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzipzapmac.com%2FGo2Shell" target="_blank" rel="nofollow noopener noreferrer" title="https://zipzapmac.com/Go2Shell" ref="nofollow noopener noreferrer">Go2Shell</a></h3>
<p>Go2Shell 可以让 Finder 中打开一个指向当前目录的终端窗口。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7edeab2277894f31a2865e05d897bab0~tplv-k3u1fbpfcp-watermark.image" alt="Go2Shell.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.parallels.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.parallels.cn/" ref="nofollow noopener noreferrer">Parallel Desktop</a></h3>
<p>Mac 上的虚拟机软件，有的软件没有 Windows 版本，或多或少需要一个虚拟机安装其他系统。</p>
<p>我有的时候会通过这种方式从 Mac 电脑向 Mac 不支持写的硬盘中拷贝文件。</p>
<h3 data-id="heading-11"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fdownload%2Fdetails.aspx%3Fid%3D50042" target="_blank" rel="nofollow noopener noreferrer" title="https://www.microsoft.com/en-us/download/details.aspx?id=50042" ref="nofollow noopener noreferrer">Mircrosoft Remote Desktop</a></h3>
<p>微软官方免费远程桌面控制 Windows 的软件，我之所以用这款软件，是因为我上家公司服务器系统是 Windows Server 的，如果也有类似需求或者需要远程 Windows 系统的读者，可以看看这款软件。</p>
<h3 data-id="heading-12"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fremote-desktop-vnc%2Fid472995993%3Fmt%3D12" target="_blank" rel="nofollow noopener noreferrer" title="https://apps.apple.com/cn/app/remote-desktop-vnc/id472995993?mt=12" ref="nofollow noopener noreferrer">Remote Desktop - VNC</a></h3>
<p>远程连接 Mac 的工具。我只所以用这款软件，是因为我前不久需要连接 Mac Mini 做一些 iOS 自动化打包的事情，有类似需求的读者，可以看看这款软件。</p>
<h3 data-id="heading-13"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhovancik%2Fstretchly" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hovancik/stretchly" ref="nofollow noopener noreferrer">Stretchly</a></h3>
<p>这是一款休息时间提醒应用，非常适合我们程序员这类写 Bug 时聚精会神，忘记起来活动活动的职业。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fec1f0a8d354b83abc22d714046c830~tplv-k3u1fbpfcp-watermark.image" alt="stretchly.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.alfredapp.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.alfredapp.com/" ref="nofollow noopener noreferrer">Alfred</a></h3>
<p>这个我觉得根本无需介绍，神器，使用 macOS 的同学应该都知道。一句话来说就是，Alfred 是 macOS 上神级的效率应用，能够在实际操作中大幅提升工作效率。</p>
<h3 data-id="heading-15"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fu.tools%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://u.tools/" ref="nofollow noopener noreferrer">uTools</a></h3>
<p>生产力工具集</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24ea80df2d144135a159ac86814212cd~tplv-k3u1fbpfcp-watermark.image" alt="utools.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswh.app%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swh.app/zh/" ref="nofollow noopener noreferrer">SwitchHosts</a></h3>
<p>是一个管理、切换多个 hosts 方案的可视化工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16a188c21eef46f7bea8dec383efb864~tplv-k3u1fbpfcp-watermark.image" alt="SwitchHosts.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fezip.awehunt.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ezip.awehunt.com/" ref="nofollow noopener noreferrer">ezip</a></h3>
<p>Mac 文件解压缩工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36387be2f8854b118ecb9367503ef5c8~tplv-k3u1fbpfcp-watermark.image" alt="ezip.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMortennn%2FDozer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Mortennn/Dozer" ref="nofollow noopener noreferrer">Dozer</a></h3>
<p>一款免费的 Mac 菜单栏图标隐藏软件，开启软件后，在 Mac 菜单栏会出现两个小圆点，将两个小圆点拖拽至你需要隐藏的应用图标的右边，点击第二个小圆点，便能完成隐藏。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e44406918523499ea5098e900d707df7~tplv-k3u1fbpfcp-watermark.image" alt="Dozer.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">开发工具</h2>
<h3 data-id="heading-20"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sourcetreeapp.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sourcetreeapp.com/" ref="nofollow noopener noreferrer">Sourcetree</a></h3>
<p>Sourcetree 是我用过最好用的版本管理（Git）客户端软件。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/420d43074e6248a78fcbd6ea5d7aa48c~tplv-k3u1fbpfcp-watermark.image" alt="Sourcetree.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.charlesproxy.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.charlesproxy.com/" ref="nofollow noopener noreferrer">Charles</a></h3>
<p>非常优秀的抓包工具</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45aacad31c4a47b8a572f03c12701e4c~tplv-k3u1fbpfcp-watermark.image" alt="Charles.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fiterm2.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://iterm2.com/" ref="nofollow noopener noreferrer">iTerm2</a></h3>
<p><code>iTerm2</code> + <code>Oh My Zsh </code>可以实现命令自动补全、自定义主题等等功能，强烈推荐，相关安装教程有很多，可以自己去找找。</p>
<p>只上一张效果图，大家感受一下吧</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16e8938f87b94a4eab4bb1c3b1b890aa~tplv-k3u1fbpfcp-watermark.image" alt="iterm2.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.postman.com%2Fdownloads%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.postman.com/downloads/" ref="nofollow noopener noreferrer">Postman</a></h3>
<p>接口测试工具，如果不想安装软件，也可以安装谷歌浏览器扩展。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3672bc58ed9f409abfcce838def4e93e~tplv-k3u1fbpfcp-watermark.image" alt="Postman.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24"><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.hostbuf.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.hostbuf.com/" ref="nofollow noopener noreferrer">FinalShell</a></h3>
<p>FinalShell 是一体化的的服务器，网络管理软件，不仅是 ssh 客户端，还是功能强大的开发，运维工具，充分满足开发，运维需求。</p>
<p>国人开发的 SSH 客户端工具，亲验好用。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e774dbcd9d4440ff8ef3975a0075c08d~tplv-k3u1fbpfcp-watermark.image" alt="FinalShell.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">iOS 工具</h2>
<h3 data-id="heading-26"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fiosyaowei%2FJSONConverter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/iosyaowei/JSONConverter" ref="nofollow noopener noreferrer">JSONConverter</a></h3>
<p>JSONConverter 是 MAC 上 iOS/Flutter 开发的辅助工具，可以快速的格式化 JSON 数据并转换生成对应的模型类属性，目前支持 Objective-C、Swift、Flutter 以及目前流行的第三方库：SwiftyJSON、HandyJSON，ObjectMapper, 可以灵活选择构建 class/struct，并支持配置类名前缀等，省去手敲模型的麻烦，借此提高开发效率。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbdee37825dc4dfb894a0a52a90d1af7~tplv-k3u1fbpfcp-watermark.image" alt="JSONConvert.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftinymind%2FLSUnusedResources" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tinymind/LSUnusedResources" ref="nofollow noopener noreferrer">LSUnusedResources</a></h3>
<p>用于在 Xcode 项目中查找未使用的图像和资源。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1ec9fe33c7a44b9b93fc343e38df00c~tplv-k3u1fbpfcp-watermark.image" alt="LSUnusedResourcesExample.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FRobertGummesson%2FBuildTimeAnalyzer-for-Xcode" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/RobertGummesson/BuildTimeAnalyzer-for-Xcode" ref="nofollow noopener noreferrer">BuildTimeAnalyzer</a></h3>
<p>展示 Swift 编译构建时间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56f2b35dfd904d6c92e38d573988724a~tplv-k3u1fbpfcp-watermark.image" alt="BuildTimeAnalayer.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-29"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimageoptim.com%2Fmac" target="_blank" rel="nofollow noopener noreferrer" title="https://imageoptim.com/mac" ref="nofollow noopener noreferrer">ImageOptim</a></h3>
<p>图片压缩工具</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ed796b3e044cb8a7ad09c008a6f6a0~tplv-k3u1fbpfcp-watermark.image" alt="ImageOptim.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flookin.work%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lookin.work/" ref="nofollow noopener noreferrer">Lookin</a></h3>
<p>Lookin 可以查看与修改 iOS App 里的 UI 对象，类似于 Xcode 自带的 UI Inspector 工具，或另一款叫做 Reveal 的软件。但借助于“控制台”和“方法监听”功能，Lookin 还可以进行 UI 之外的调试。此外，虽然 Lookin 主体是一款 macOS 程序，它亦可嵌入你的 iOS App 而单独运行在 iPhone 或 iPad 上。最后，Lookin 完全免费。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1524932b540a4f08bc45ad81ad848ec5~tplv-k3u1fbpfcp-watermark.image" alt="Lookin.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhuanxsd%2FLinkMap" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/huanxsd/LinkMap" ref="nofollow noopener noreferrer">LinkMap</a></h3>
<p>这个工具是专为用来分析项目的 LinkMap 文件，得出每个类或者库所占用的空间大小（代码段 + 数据段），方便开发者快速定位需要优化的类或静态库。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c7cffe8b8724e0c92dfec1670a12efc~tplv-k3u1fbpfcp-watermark.image" alt="LinkMap.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-32"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnicklockwood%2FSwiftFormat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nicklockwood/SwiftFormat" ref="nofollow noopener noreferrer">SwiftFormat For Xcode</a></h3>
<p>SwiftFormat 是一个代码库和命令行工具，用于在 macOS 或 Linux 上重新格式化 Swift 代码。</p>
<h3 data-id="heading-33"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.hopperapp.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.hopperapp.com/" ref="nofollow noopener noreferrer">Hopper</a></h3>
<p>逆向工程工具，可让您反汇编、反编译和调试应用程序。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/905a97ada9464e15922e1516a4e5e6e9~tplv-k3u1fbpfcp-watermark.image" alt="Hopper.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-34"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpro.itools.cn%2Fpro_mac%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pro.itools.cn/pro_mac/" ref="nofollow noopener noreferrer">iTools</a></h3>
<p>这个只要是做 iOS 开发的应该都知道，我就不过多介绍了。</p>
<h3 data-id="heading-35"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdownloads%2F%3Fq%3DHardware%2520IO%2520Tools" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/downloads/?q=Hardware%20IO%20Tools" ref="nofollow noopener noreferrer">Network Link Conditioner</a></h3>
<p>这是一个来自苹果官方的工具，它可以模拟任何网络环境，如 3G，Edge 等等，也可以重新定义当前的网络环境，如网络延迟、带宽或丢包率。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94ee361dbe74343a06190fd525fe4b6~tplv-k3u1fbpfcp-watermark.image" alt="Network Link Conditioner.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-36"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxndrs%2FXSimulatorMngr" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xndrs/XSimulatorMngr" ref="nofollow noopener noreferrer">XSimulatorMngr</a></h3>
<p>XCode 模拟器管理器，用于管理 iOS 模拟器的开发者工具。</p>
<ul>
<li>已安装的模拟器列表。</li>
<li>每个模拟器已安装的开发者应用程序列表。</li>
<li>允许直接打开应用程序包或沙箱文件夹。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94692bb3b035436ca8cdf9b289e20c40~tplv-k3u1fbpfcp-watermark.image" alt="XSimulatorMngr.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-37"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKnuffApp%2FKnuff" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KnuffApp/Knuff" ref="nofollow noopener noreferrer">Knuff</a></h3>
<p>Apple 推送通知服务 (APN) 的调试应用程序</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e35f1921ec44bc2a774a7f95b24bb73~tplv-k3u1fbpfcp-watermark.image" alt="Knuff.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-38"><a href="https://link.juejin.cn/?target=http%3A%2F%2Finjectionforxcode.johnholdsworth.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://injectionforxcode.johnholdsworth.com/" ref="nofollow noopener noreferrer">InjectionIII</a></h3>
<p>允许您在 iOS <strong>模拟器</strong>中增量更新函数和类、结构或枚举的任何方法的实现，而无需重新构建或重新启动应用程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5b7733416c4159b70ca45eb156088c~tplv-k3u1fbpfcp-watermark.image" alt="InjectionIII.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-39"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.dokit.cn%2F%23%2Findex%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://www.dokit.cn/#/index/home" ref="nofollow noopener noreferrer">DoKit</a></h3>
<p>滴滴推出的 APP 效率工具</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0acf076ed1a14b5ab922dff9a151092f~tplv-k3u1fbpfcp-watermark.image" alt="DoKit.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-40"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshaojiankui%2FProfilesManager%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shaojiankui/ProfilesManager/releases" ref="nofollow noopener noreferrer">ProfilesManager</a></h3>
<p>mobileprovision 文件管理器工具</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/186ef612947746d3b4fce7a4e3f3cc5e~tplv-k3u1fbpfcp-watermark.image" alt="ProfilesManager.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-41">在线工具</h2>
<h3 data-id="heading-42"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.json.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.json.cn/" ref="nofollow noopener noreferrer">JSON</a></h3>
<p>JSON 解析，用来格式化 JSON</p>
<h3 data-id="heading-43"><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftinypng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tinypng.com/" ref="nofollow noopener noreferrer">tinypng</a></h3>
<p>在线压缩图片</p>
<h3 data-id="heading-44"><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftableconvert.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tableconvert.com/" ref="nofollow noopener noreferrer">tableconvert</a></h3>
<p>将表格转成 md，excel 等各种形式，我经常会用来写一些表格用来转成 md</p>
<h3 data-id="heading-45"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fminhaskamal.github.io%2FDownGit%2F%23%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://minhaskamal.github.io/DownGit/#/home" ref="nofollow noopener noreferrer">DownGit</a></h3>
<p>下载 Github 仓库中某一个指定文件或者文件夹</p>
<h3 data-id="heading-46"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswiftify.com%2Fconverter%2Fcode%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swiftify.com/converter/code/" ref="nofollow noopener noreferrer">swiftify</a></h3>
<p>快速将 Objective-C 代码转换为 Swift</p>
<hr>
<blockquote>
<p>有一个技术的圈子与一群同道众人非常重要，来我的技术公众号及博客，这里只聊技术干货。</p>
<ul>
<li>微信公众号：<strong>CoderStar</strong></li>
<li>博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoder-star.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coder-star.github.io/" ref="nofollow noopener noreferrer">CoderStar's Blog</a></li>
</ul>
</blockquote></div>  
</div>
            