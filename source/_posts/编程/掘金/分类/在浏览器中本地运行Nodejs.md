
---
title: '在浏览器中本地运行Node.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07401713bf7c4214b6d808b658b08722~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 02:29:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07401713bf7c4214b6d808b658b08722~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一切要从收到一封邮件开始</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07401713bf7c4214b6d808b658b08722~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>大早上，我收到一封邮件，StackBlitz说正在与Next.js和Google的团队合作开发一项新技术</p>
</blockquote>
<ul>
<li>几年前，<code>StackBlitz</code>意识到网络正朝着关键的拐点发展。WebAssembly和新功能API的出现使编写基于WebAssembly的操作系统似乎变得可能，该操作系统功能强大到可以完全在浏览器中运行Node.js。我们设想了一个比本地环境更快，更安全和一致的高级开发环境，以实现无缝的代码协作而无需设置本地环境</li>
</ul>
<h4 data-id="heading-1">技术名为:<code>WebContainers</code></h4>
<ul>
<li>WebContainers允许您创建完整的Node.js环境，这些环境可以在毫秒内启动，并且一键即可立即联机和链接共享。该环境具有VS Code强大的编辑经验，完整的终端，npm等功能。它还可以完全在您的浏览器中运行，从而带来一些关键的好处：</li>
<li>比本地环境快。与yarn / npm相比，构建速度最多可提高20％，而卷装安装速度则可快5倍以上。</li>
<li>浏览器中的Node.js调试。与Chrome DevTools的无缝集成可实现本机后端调试，无需安装或扩展。</li>
<li>默认为安全。所有代码执行都发生在浏览器的安全沙箱中，而不是在远程VM或本地二进制文件上。</li>
<li>同样，这些环境不在远程服务器上运行。而是，每个环境都完全包含在您的Web浏览器中。没错：Node.js运行时本身第一次在浏览器中本机运行。</li>
</ul>
<blockquote>
<p>从现在开始，WebContainers现在处于公开测试阶段。当前支持包括Next.js，GraphQL和Vanilla Node.js，我们正在与其他开源项目合作以扩展支持</p>
</blockquote>
<h4 data-id="heading-2">为什么会有<code>WebContainers</code></h4>
<h5 data-id="heading-3">安全</h5>
<ul>
<li>StackBlitz通过利用浏览器中数十年来的速度和安全性创新来解决这些问题。StackBlitz中的所有计算都会在浏览器安全沙箱中立即发生，并且无法爆发到您的本地计算机上。该模型还释放了一些关键的开发和调试优势（在几秒钟内便会提供更多优势）。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05babf3ab054349bc46cc9d338db80c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">释放浏览器的功能</h5>
<ul>
<li>使用Chrome DevTools无缝进行Node.js调试
<ul>
<li>事实证明，浏览器确实非常擅长调试Javascript。我知道，这令人震惊；）通过在浏览器中执行Node.js，与Chrome DevTools的集成即开即用。无需安装，无需扩展，仅在浏览器中进行本机后端调试即可</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d98f17290a9f440e9b85acae27c22639~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">运行服务器,在你的浏览器中</h5>
<ul>
<li>实际上。WebContainers包含一个虚拟的TCP网络堆栈，该网络堆栈已映射到浏览器的ServiceWorker API，使您可以即时创建实时Node.js服务器，即使您处于脱机状态也可以继续工作。因为它完全在浏览器安全沙箱中运行，所以服务器响应的延迟比本地主机（！）少，并且可以保护您的Web服务器免受本地主机抓取攻击</li>
<li>毫秒级启动时间</li>
<li>每个页面加载时都有一个全新的环境
<ul>
<li>再见rm -rf node_modules！WebContainer的内置npm客户端是如此之快，以至于它在每次页面加载时都运行全新的安装，从而确保您每次都能获得一个干净的环境。如果您的环境确实出现问题，则可以像处理其他任何Web应用程序一样恢复到干净的状态：单击“刷新”按钮</li>
</ul>
</li>
<li>借助StackBlitz，无论您是在火车上，在飞机上还是在雨中后座时，都可以在没有互联网连接的情况下继续工作</li>
</ul>
<blockquote>
<p>使用StackBlitz新颖的计算模型，100％的代码执行发生在浏览器安全沙箱中。与本地相比，这导致了更快，更少限制的开发环境，同时又提供了更高的安全性，这是非常罕见的组合。</p>
</blockquote>
<ul>
<li>实际上，默认的安全状况是如此稳固，以至于我们的嵌入式软件包管理器是第一个可公开获得的工具，可以解决五年多来未解决的Sam Saccone长期未解决的npm漏洞</li>
<li>同样，这些环境不在远程服务器上运行。而是，每个环境都完全包含在您的Web浏览器中。没错：Node.js运行时本身第一次在浏览器中本机运行</li>
</ul>
<h4 data-id="heading-6">写在最后</h4>
<ul>
<li><code>WebAssembly</code>强大到足以编写操作系统，但是这次<code>WebContainers</code>把这个技术使用方向放在了<code>Node.js</code>上，我觉得是有划时代意义的</li>
<li>在我看来，这个技术在未来最主要应用方向是，可以使世界范围内的软件在以前无法运行的地方运行，以后电脑上可能只需要安装一个谷歌浏览器</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6642d964b73d48b68baaa9235710f8dd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            