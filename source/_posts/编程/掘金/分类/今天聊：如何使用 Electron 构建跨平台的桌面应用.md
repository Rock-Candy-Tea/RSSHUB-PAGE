
---
title: '今天聊：如何使用 Electron 构建跨平台的桌面应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206cae8aa94f4d3e9aba2300de05249d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 15:04:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206cae8aa94f4d3e9aba2300de05249d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>关注前端早早聊，跟进第三十届|前端早早聊大会 BFF 专场（GraphQL、统一网关、API 接入管理、超大规模集群，协议转换、安全切面、高并发、可视化编排、统一稳定性建设...）8-14 全天直播，9 位讲师，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2Ftl30" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/tl30" ref="nofollow noopener noreferrer">点击报名看直播👉 )：</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/206cae8aa94f4d3e9aba2300de05249d~tplv-k3u1fbpfcp-watermark.image" alt="海报 (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线，
所有往期都有全程录播，<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2F2021" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/2021" ref="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">自我介绍</h2>
<p>欢迎大家来到今天的早早聊跨端跨栈专场，今天我分享的主题是《如何基于 Electron 开发跨终端的应用》。
先做一下自我介绍，我叫逯子洋，17 年加入政采云，目前主要负责政采云前端工程化平台敦煌以及政采云电子招投标客户端的建设。这边是我们团队的微信公众号，大家如果想对我们团队有更多的了解，可以关注一下我们的公众号。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edb92b7eccf3432ca69e5aef56ea8e2e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">端的延展<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29d385d672cf4a52bb840225fed92da3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></h2>
<p>首先我们分享的第一块叫<strong>端的延展</strong>。不知道大家对这张图熟不熟悉，前段时间的新闻大家应该都听到过，硅谷钢铁侠艾隆马斯克发布了第一款商业化的载人龙飞船，这张图片中就是龙飞船的控制台，知乎上有人对这张图的评价叫 Js 上天了。为什么说叫 Js 上天了呢？因为有传言说它是基于 Electron 开发的，不过这个消息并没有得到证实。但是可以证实的一点是航天飞船的触控界面 UI ，确实是基于 Chromium + JavaScript 这样的架构来实现的。这也从某种程度上说明了这种架构的一个可用性和稳定性的能力。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87d01666f15545f898660e5370a7d0ea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们一起来回顾一下前端在整个端领域的发展历程。在早期，前端工程师的定义可能是基于浏览器运行环境的 Web 开发，但是随着 09 年 Node.js 的出现，让前端工程师有了脱离浏览器运行环境的开发能力。我们拥有了可以面向服务端开发的能力，前端的能力延展到了服务端。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c012bcf2bcb4435ba560e14f28e0744c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>随着 HTML5 标准的制定，以及移动端设备技术的发展，前端工程师也可以更多的拥抱面向移动端场景的开发。也出现了像今天上午两位讲师所讲到的移动端领域 React Native 这样的跨平台技术方案。随着移动 APP 成为一个主流，基于这些智能化的设备以及芯片的计算能力，前端也普及到了物联网设备方向，前端可以拥有了面向 Iot 的开发能力，也诞生了像 Thing.js  这样的面向物联网设备开发的 Js 框架。</p>
<h2 data-id="heading-2">CLI -> GUI</h2>
<p>今天所要讲的主题是<strong>桌面端</strong>，随着 Electron 这样的跨终端 Js 框架的出现，整个前端工程师的能力也是延展到了桌面端。当我们拥有了这样的一个桌面端的开发能力之后，它能带给我们的价值是什么呢？首先看一下桌面端给我们带来哪些不一样的体验。
大家看到左边这张图，是早期电脑的 DOS 系统的运行的截图，右边则是 1983 年苹果电脑发布的第一款 Apple Lisa 个人电脑，它是全球第一款搭载图形用户界面（也就是我们所说的 GUI）的一台个人电脑，正是因为这款电脑的问世，让后期个人电脑大众化的普及得以实现。为什么它会带动个人电脑的普及化，是因为图形界面对于用户来说，在视觉上更容易接受，学习的成本也是大幅的下降。相信用过 MAC 系统的同学都会对苹果优秀的界面设计以及整体的交互体验，有比较深刻的感受。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ede8be03313495b9791eb0872cabcd4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，这样的桌面端 GUI 的技术，能给我的前端开发工作带来什么不一样呢？</p>
<p>左边这个流程相信大家不陌生，在我们开始新项目开发的时候，可能需要做哪些事情？首先第一步可能是需要去创建一个 Git 仓库，创建完成之后将仓库克隆到本地，然后通过团队内部的 CLI 工具的安装之后，去执行例如 <code>xxx-cli create</code> 这样的命令去创建一个项目。创建项目完成之后，如果想进行开发，我们需要去运行 <code>npm install</code> ，安装所需的依赖包，最终将整个项目提交到 Git 仓库上去。这是我们新项目的创建，基于 CLI 方式的一个操作流程。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98a6d1bf47e24195989ca75f4bc4778d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
如果说基于客户端的能力的，我们可以做哪些改变呢？我们可以看到，右边的图是我们团队前端工程化平台敦煌的系统截图。如果是创建一个新项目，只需要选择自己的创建方式，然后输入一些必要的创建参数，比如说选择你需要创建的 Git 仓库 Group、项目名称、脚手架类型，点击创建项目之后，它会自动帮你将左边的这一系列的流程全部执行完毕。就是说将左边 6 个步骤简化到了 2 个步骤，大大的简化了操作的链路。</p>
<h4 data-id="heading-3">GUI 赋予的价值</h4>
<p>GUI 赋予了我们哪些价值呢？首先它可以将分散的任务点进行一个串联整合，提供了一个更简化的操作链路，同时它还可以抹平不同同学使用时一些流程间的差异，以及流程所依赖的一些环境的差异，并且基于 GUI 的一个整合能力，我们还可以将其他能力进行一个横向的串通，并且通过 GUI 来设计插件化的机制，还可以创造一个可共建的生态。同时基于 GUI 的图形界面操作低学习成本，以及它对整个流程的托管，也是可以大大的降低团队同学的研发复杂度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85886e1d60f5438c895e0bd622e91935~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">业务场景应用</h4>
<p>下面是基于 Electron 开发的一些重点应用的落地场景。这是我所负责的政采云电子招投标客户端的业务。它主要的功能是帮助用户由传统的线下招投标，纸质的标书，转变为电子标书，我们提供这样的客户端可以帮助用户串联整个制作标书的流程。同时基于 Electron 所提供的 Node.js 的能力，用户本地标书文件的读写，以及本地文件的加解密操作，都可以在客户端里面完成。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa615713361d461baddfc5ca298ad919~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">基建场景应用</h4>
<p>这边是 Electron 在我们的工程化平台上的实践，这就是我们前面所提到的前端工程化平台-敦煌。它主要做的内容是对整个前端研发流程的托管，像我们刚才所提到的项目创建就是其中的一个环节。下面我们还会详细的介绍一些这方面的应用。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b8c1587c2bb45a8a76a7942f0d333b3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">开发模式</h2>
<p>上面我们大概介绍了一下 Electron 的一些价值。如果说我们想基于 Electron 开发一个跨平台的桌面端应用，应该如何来做？下面一起来看一下，第二部分**开发模式。**Electron 的开发模式跟我们平时的 Web 开发有哪些不一样的地方？
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8972948673e943538ee4f2b4487187d9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">Electron 架构</h4>
<p>首先这是 Electron 的一个整体的架构，它是由 Github 开发了一个开源框架，允许我们使用来 HTML + CSS + Javascript 来构建开发桌面应用，大大降低了桌面应用的开发的复杂度。整体架构的核心组成是由 Chromium + Node.js + Native APIs 组成的。其中 Chromium 提供了 UI 的能力，Node.js 让 Electron 有了底层操作的能力，Navtive APIs 则解决了跨平台的一些问题，比如说 Windows 系统、MAC OS 系统及 Linux 系统之前一些差异的屏蔽，并且它还提供了一个比较统一体验的原生能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb697420cbe149c8a8e33664eb84912f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">能力点</h4>
<p>我们来介绍一下它的一些核心的能力点。</p>
<ul>
<li>首先是 Chromium，我们可以把它理解为是一个拥有最新版浏览器特性的一个 Chrome 浏览器，它带给我们的好处就是在开发过程中无需考虑浏览器的兼容性，我们可以使用一些 ES6、ES7 最新的语法，可以放心的使用 Flex 布局，以及浏览器的最新特性，都可以尝试，不需要考虑兼容性的问题。</li>
<li>Node.js 则是提供了一个文件读写、本地命令调用、以及第三方扩展的能力，并且基于 Node.js 整个强大的生态，将近几十万的 Node.js 模块都可以在整个客户端内使用。</li>
<li>Native APIs 提供了一个统一的原生界面的能力，还包括一些系统通知、快捷键，还可以通过它来获取一些系统的硬件信息。还提供了桌面客户端的基础能力，像更新机制、崩溃报告这样的能力。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925889b5510e49d394eb4f0e01600057~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">其他桌面端选型对比</h4>
<p>Electron 提供这些能力点大大的降低了桌面端开发的成本，以及上手的门槛。当然开发桌面端的话，除了 Electron 外，还会有一些其他的选型，我们看一下它跟其他的选型相比较的话有哪些差异点。</p>
<ul>
<li>开发桌面端首先可以选择 Native 开发，但是，在开发不同的平台的时候，需要使用不同的语言，但它的优点是具有比较好的原生体验，以及比较好的运行性能，但是它的门槛相对来说还是比较高的。</li>
<li>QT 是一个基于 C++ 的跨平台桌面端开发框架，它所使用的语言是使用 C++，整体性能和体验上来说，跟Native 开发的话是可以相媲美的，但由于技术栈原因，开发门槛相对来说也是比较高的。</li>
<li>另外两个就是 Electron 和 NW.js。这两个都是使用 Javascript 作为一个开发语言。相较与 Native 和 QT 来说，它们对前端工程师来说是相当友好的，并且它们两个有着比较相似的一个架构，都是基于 Chromium + Node.js 实现，同时它们也都有一个跨平台的支持能力。但两个的差异点是：Electron 相对来说有一个更好的一个社区的生态和社区的活跃度，我们平时如果遇到了一些问题，在社区内可能会有比较多、比较完善的解决方案，同时它对 issue 的响应速度也是比较快的。</li>
</ul>
<p>所以基于上面的比较，开发桌面客户端，对前端工程师来说，Electron 是一个非常好的选择。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5268860216a04512852e3b9d8bcfadf7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">简单 Electron 应用的结构</h4>
<p>下面来看一下，如果想开发一个桌面客户端，应该怎么做呢？
这边是一个最简单的 Electron 桌面应用的结构，我们只需要有三个文件，首先我们通过 package.json 中的 <code>main</code> 字段，通过 <code>main</code> 字段来定义应用的一个启动入口。我们将入口文件定义为 <code>main.js</code> ，在 <code>mian.js</code> 里我们做了哪些事情呢？首先 app 代表着整个应用，监听 app 的状态，当整个应用达到一个 ready 的状态之后，通过 Electron 提供的 <code>BrowserWindow</code> ，去新创建一个浏览器窗口。创建浏览器窗口之后，去加载 <code>index.html</code> 文件，这样的话我们就完成了一个最基础版桌面端应用的实现。基于 Electron 开发桌面端应用，和平时的开发 web 端应用有哪些不一样的，我们需要了解的两个核心概念就是：<strong>主进程和渲染进程，以及两个进程间的通信如何实现</strong>。在刚才的示例中，其中 <code>main.js</code> 是运行在主进程中， <code>index.html</code> 则是运行在渲染进程之中。下面我们通过一个简单的 Demo，来看一下如何实现两个进程之间的通信，并且如何通过主进程来进行一些 Node.js 能力调用的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/874b028c26bf434fbec5a0dd612e7e94~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">进程间的通信</h4>
<p>我们想要实现这样的效果，页面上有一个按钮，当点击按钮之后，向主进程发送了一个 <code>say-hello</code> 的消息，当主进程接收到消息之后，它会在系统桌面上创建一个文件叫 <code>hello.txt</code>。并写入内容 <code>Hello Mac!。</code>具体的我们是怎么做的？</p>
<p>首先在渲染进程里面，我们应该在页面上会进行一个按钮操作事件，当事件触发之后，我们通过 Electron 提供的 <code>ipcRenderer</code>  API 向主进程发送一个叫 <code>say-hello</code> 这样的一个消息。当我们的主进程接收到这样一个消息之后，则可以在主进程中直接调用 Node.js 的 fs 模块，一个文件读写的模块。首先先创建一个文件，并且对这个文件写入我们所传输的内容。当文件写入成功之后，对渲染进程进行回复，通过调用 Electron 提供的 <code>Notification </code>模块，显示系统通知去告知用户，这是一个简单的 Demo 的实现，其核心的点就是需要关注主进程和渲染进程的概念，以及两个进程之间是如何通过 IPC 机制进行通信的，这边是一个简单的实现。还有一些更多的应用的场景，这块就不再对 API 进行过多的介绍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37742fb55e4e4f7a873984b2de36b3c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">工程化发展 CLI -> GUI</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a6b8bf816749ee83d29d78dcd5aa3d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们会根据一个实际的应用，来介绍一下 Electron 开发的实践。以我们的前端工程化平台敦煌为例，介绍一下我们是如何通过 Electron 将工程化能力由 CLI 式 变为 GUI 式的使用。
首先大家先看一个视频，这个视频就是我们在最开始所提到的项目创建的整个流程的运行的演示。大家可以看到我们整个流程完成了 Git 仓库的创建、项目模板的创建、项目模板到仓库的推送，并且对 Git 项目进行本地克隆，克隆完成之后，会进行依赖的安装，并且在客户端进行重新载入和管理这样一个流程。将之前分散的单点命令操作，通过 GUI 的方式进行一个串联。
这个流程只是工程化平台中的一块，我们在整个工程化平台中，实现了很多的单点命令到工作流的串联。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e360ae98ae0c4ba685ed28624d844cfe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">I2P（Install To Publish）</h4>
<p>这边是我们整个前端应用管理平台的系统架构，大概看一下。核心流程就是上面所写到的一个 I2P 的概念，就是 <code>install to publish</code> 。它完成了组件、模板和项目这三个级别，从创建到发布的全流程托管。</p>
<ul>
<li>创建阶段，主要提供了包括本地创建、Git 创建、统一的创建模板管理、创建的流程审批和创建完成的反馈。</li>
<li>开发阶段，提供了一个 Dev Server 的运行能力，对项目级的页面管理、依赖管理、分支管理，还有一键式的升级能力。同时还打通了 CI/CD 持续集成能力。</li>
<li>发布阶段，则提供了一个发布前的权限校验和合规检测、资源推送以及发布的审批机制。</li>
<li>数据分析，是我们整个流程中比较核心的一块，是对我们整个流程进行一些数据沉淀，并且将这些数据以可视化报表的形式进行成输出，基于这些数据将整个 I2P 的流程与其他的能力进行一个串联。</li>
</ul>
<p>在上面的整个 I2P 的流程中，我们沉淀出一些项目数据，包括流程数据，可能还有一些类似于组件管理的数据。以数据为连接点，可以将整个的研发流程与其他的一些技术建设能力进行一个串联打通，包括用户行为分析、页面级、项目级的性能分析报告，还有错误监控的机制，都可以接入到整个工程化平台上。
支撑我们整个工程化平台就是一些基础能力以及 Electron 所提供的桌面端能力。
基础能力，包括一些常规的 GIt 操作、NPM 操作、一些命令执行和一些本地的 logger 服务。Electron 提供了桌面端包括更新、窗口管理、通信，以及些原生能力。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673ed023e04e4587bfd3b011f05381be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">由点到线</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2b900b8f6544111b1a8450dde2e5397~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">单点命令 -> 任务流</h4>
<p>下面我们就具体来看一下如何实现由一个单点命令到任务流这样的一个串联。将单点命令的操作变为任务流的串联模式，我们要从以下 4 个切入点来实现。
• 首先我们要将常规的一些命令调用变为函数式的调用。
• 基于这些函数式的调用，进行一个任务流的编排和组装，根据实际的开发场景，去定制一个任务流。
• 第三块我们所需要的是整个任务流的任务进度反馈机制，如何将任务执行，通过 GUI 的能力，让用户可以直观感受到整个任务的执行链路和进度。
• 最后，在整个任务流中，很重要的一块就是对整个流程的数据收集。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7d21bcbbba498cbab739916f70fab7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16"></h4>
<h4 data-id="heading-17">流程的设计</h4>
<p>下面是我们刚才所演示的项目创建流程的架构设计。当我们在调用项目创建模块的时候，首先会通过 Server 接口，去创建 Git 项目。先对整个用户的权限做一层校验，校验通过之后，通过调用 Gitlab API，进行一个仓库的创建，之后，根据所选用的模板信息拉取统一维护的项目模板，根据用户所输的项目名称、项目描述等信息，来生成真正的项目文件，调用 Gitlab API 将整个项目文件推送到创建好的仓库。关于 Gitlab API 的使用这一块，在掘金上有进行过文章的分享，大家感兴趣的话可以去了解一下，这边就不再进行详细的阐述。在我们整个服务端完成了一系列的 Git 创建操作之后，会将创建成功的仓库 url，给到我们的桌面端，桌面端接收到这样创建成功的任务结果之后，开始执行一些本地操作的任务流程。将 Git 仓库克隆到本地的工作区内，同时完成整个项目的依赖安装。在依赖安装之后，我们会借助桌面端的通知能力，包括钉钉的接口去完成通知和反馈。
其中克隆、依赖的安装以及通知反馈是在我们桌面端的主进程内完成的。在我们整个任务流中，它有实时与渲染进程的消息反馈。我们会将整个任务的进度，包括命令执行的日志输出、命令执行结果，通过 IPC 的方式实时的与渲染进行通信，最终在界面上给到用户反馈。在整个流程中，也会对项目数据和流程数据进行存储。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a958b81a1fe0484d87ad7e408e4c9bda~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
实现这样的整个流程，在实践上有哪些是需要说的呢，下面我们来看一下具体的代码。</p>
<h4 data-id="heading-18"></h4>
<h4 data-id="heading-19">npm install 变为 npm.install()</h4>
<p>首先在进行命令调用的时候，要将 <code>npm install</code> 这样一个命令行的调用方式变成变为一个函数式的调用，会变为 <code>npm.install()</code>  这样一个调用方式。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9473a9fb39094039be0b619e001b55ed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">git init 变为 git.init()</h4>
<p>类似 Git 的命令，也会变成函数式调用
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a931c1e31f24c4d9bb038dca07bf72d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">将命令式执行 Promise 化</h4>
<p>下面我们看一下，具体场景，如何将命令式调用变成函数式调用。
首先是将命令执行 Promise 化。例如 <code>git init</code> 这样的操作，在执行整个命令的时候，我们更多关心的是整个命令执行的结果，可能不太会关心命令执行过程中的一些输出的内容。这样的话我们就可以通过 Node.js 中的 <code>spawn</code> ，启动子进程来执行命令。通过监听子进程输出来判断我们整个命令的执行状态，然后对整个命令进行 Promise 封装，我们就完成了 <code>git init</code> 这样一个命令行调用变为 <code>git.init()</code> 这样一个异步的函数调用。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ec0d3a1681e49f080552d3f6ae6e428~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">实时输出命令执行日志</h4>
<p>在另外一个场景，比如说 <code>npm install</code> ，依赖安装，或者说启动本地开发服务，整个命令的执行过程可能会比较长，我们更关注的是过程中实时的日志输出。我们怎么来做呢？
首先我们这边是先创建一个 <code>EventEmitter</code>  实例，作为我们的日志的分发管理，同样的我们也是通过 <code>spwan</code> 来启动一个子进程来执行命令，并且实时的监听子进程的输出，将输出的日志通过 <code>emitter</code> 实例将它分发出去。当我们在主进程中拿到这样的实时日志输出之后，可以通过主进程跟渲染进程间的 IPC 的通信，将日志实时的输出到渲染进程当中。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f44083397c4f0987ff376b7550caa9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将命令式调用变为函数式调用，有了这样的能力之后，就可以通过对这些函数的调用，进行任务流的编排。例如刚才我们所提到的项目创建，这可能是一个比较通用的流程，还有组件管理、模板管理和以及项目发布等。大家可以根据自己实际的业务需要，来去编排自己一个任务流。</p>
<h4 data-id="heading-23">模拟终端：反馈任务进度</h4>
<p>上面我们提到的是主进程中对整个命令执行方式的一些改变。那么在我们的渲染进程当中，我们要怎样去实现类似于刚才视频中的终端日志反馈呢？反馈的方式有很多，我们可以通过设计一些任务的步骤条，或者进度条这样的方式来给予整个任务进度的反馈。但是更好的方式是我们可以把任务的进度，包括整个任务输出日志进行一个及时的反馈。这边我们使用的是 xterm.js。它是一个基于 ts 所编写的一个前端终端组件，可以在浏览器内实现终端应用，VsCode 也是基于 xterm.js 来实现的终端的。要如何将主进程的日志来输出到渲染进程当中，就是我们上面所提到的，在拿到一个 EventEmitter 所广播的的输出之后，要通过主进程与渲染进程之间的通信，将数据推送到渲染进程，在渲染进程所需要做的一个处理，把接受到的命令输出，实时的渲染到 xterm 实现的终端组件上面来。</p>
<p>这样的话我们就完成了整个任务流的反馈机制。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00aa9b3bea9644bbb04e8463b7e45227~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是我们在工程化平台中一个任务流的实现，借助于 Electron 能力，我们就可以很方便的实现整个流程任务的编排，以及实现对应流程的界面交互，对整个流程进行简化。除了任务流的实现之外，我们更多需要关注的是整个过程中的数据收集，包括流程数据以及流程中创建的项目、组件数据沉淀，也包括流程当中一些异常数据，因为这些数据是将流程与其他的基础建设能力进行打通的基础，同时也能让我们对整个流程持续的优化，</p>
<h2 data-id="heading-24">更新</h2>
<p>在完成客户端的开发之后，需要考虑的则是后续的更新，一起来看一下，我们如何实现客户端的自动更新的功能。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/742905fd09fc4208bd0a2439a056b267~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
Electron 提供了一套比较完善的打包更新机制。</p>
<p>通过 Election-builder 把我们的应用构建之后，会输出一个 latest-mac.yml 文件，以及应用的 zip 包，将这两个文件放到更新服务器上，更新服务器的实现方案有很多，我们选用的是 CDN 来做为更新服务器。
我们如何去设计整个更新的流程，在渲染进程内，一般会提供手动检测更新的触发入口，或者通过轮询任务，来定时进行版本更新检测。
渲染进程发起版本检测求之后，会在渲染进程内调用  <code>autoUpdater</code> 模块，它是 <code>Electron</code> 内置的更新管理模块。
首先需要设置 feedUrl，就是最新的更新包在更新服务端地址。当收到一个渲染进程的版本检测请求之后，调用 <code>checkForUpdates</code> 方法，之后，它会触发下面一系列的一些事件，我们可以通过对整个更新事件的各个生命周期的监听，来完成整个更新流程的把控。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83f5042eba164618a1eb5c384d59ebed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25"></h4>
<p>通过 Electron 内置的一个更新机制要面临的问题是更新包体积比较大。因为我们通过 Electron 所构建的桌面端的应用，它将整个 Chromium 进行了集成，就会导致即使我们写了一个很小的 Hello world 这样一个应用，它的体积压缩后也会有 40MB 左右，常规的一个应用来说可能占用 100MB 左右。这样的问题就是有一些比较小的改动的时候，就需要全量的更新，对于用户的一个体验来说并不是很好，对于这些我们有哪些解决方案？首先我们是可以对整个更新的交互设计上做一个优化。我们需要提供的是对整个更新流程的一个进度反馈，另外一点就是我们可以通过 autoUpdater，实现后台的下载。当我们完成了整个更新包的下载之后，然后再通知用户对整个应用进行一个重启，然后更新整个应用，这样的话就才从交互层面上，一定程度的避免了增量更新对用户所体验上的一些影响。当然全量更新还会存在的一个问题，如果用户量比较大的话，就会比较浪费网络资源。</p>
<h4 data-id="heading-26"></h4>
<h4 data-id="heading-27">增量发布</h4>
<p>下面是我们的一些在增量发布上面的一些实践。首先对整个 Renderer 层的静态资源进行 CDN 托管。对于我们整个应用，不会将 Renderer 层的静态资源打包到最终的桌面端程序内，将资源远程托管，同时我们根据一些特定的业务场景，可以利用 service worker 能力，对整个资源做一个离线缓存，并且对静态资源做版本控制。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab2811fd7fe24a15a502ba361c700b15~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-28">更新流程</h4>
<p>Renderer 层的一个更新流程是这样的，当页面发请求的时候，首先会匹配本地有没有这样的一个资源的缓存，如果我们匹配到资源，就会返回匹配到的结果。如果说本地没有匹配到的话，就重新请求最新资源，同时将请求的资源进行缓存。如果说在整个请求的过程中出现了错误，需要有一个可使用的默认版本的资源，并且将错误进行上报。
这里我们所实现的一个是基于 UI 层的一个增量更新。实际的业务场景，需要根据不同资源的更新频率，来决定应该是进行更新的体验优化，还是使用 UI 层增量更新，或者安装包的增量更新。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dd480935bda491c80e59d6f47a3d7c1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-29">敦煌工程化平台技术架构图</h4>
<p>这边是整个应用管理平台的架构，在我们的整个工程实践中，除了实现了对整个项目、组件还有模板的 I2P 全流程托管之外，我们还提供了其他能力，例如团队入口的收敛，包括文档入口，输出入口，同时还将团队内部的一些工具进行一个整合，将一些分散在各个地方的一些工具，比如说文档站点生成工具、图床工具，iconfont 管理工具进行了一个整合，同时我们还对整个客户端的用户行为数据做了采集，通过数据分析来持续迭代。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2caf3fa6cf5e40f089fede7647753777~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-30">更多场景</h2>
<p>以上我们基于 Electron 的前端工程化平台的实践。当然 Electron 还会有一些其他的应用场景，我们一起来看一下。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84cfec20ceb44d789465eec79ebe755d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
首先 VS code，以及支付宝小程序的 IDE，也是基于 Electron 框架实现的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d44280d679a4242ae1aff3cf1633756~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
左边是一个接口管理的桌面端工具，为开发过程提供辅助的功能。另外一个 switchhosts，它是一个本地环境管理工具。大家可以看到基于 Electron 开发的桌面端的应用，在我们整个的研发流程中，从我们的本地环境管理、流程管理，开发辅助以及研发编辑阶段都有涉及。工程化管理平台是对整个研发生命周期流程上的串通，但是在实际的编码阶段，其实还是有一个脱离的环节，依然需要依赖 IDE 的能力。基于 Electron 在 IDE 方向的一些可能性，我们未来的一个方向也是，希望将整个 IDE 的本地编码环境与我们的整个研发流程进行一个串通，真正意义上的实现整个研发链路的串通以及效率升级。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a6d0f994e742c38902b48f387ea8fd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然还有更多的可能性，就是前面提到的 spaceX 这样更大的一个场景~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3848c789948849eab84b1ff040b4b855~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-31">推荐一本书</h2>
<p>下面是我个人所推荐的一本书《少有人走的路》，从书中可以收获的是如何以更成熟的心智去看待所遇到的问题。在成长过程中，限制我们的，更可能是认知以及思维局限性。以什么认知和心态去看待遇到的问题，就会决定会以什么样的反应和什么样的能力去回应这些问题。这本书会让我们更多的去探索，怎样以更成熟的心智去看待所遇到的问题。
希望通过这本书能让大家收获如何更好的面对技术以外的问题，更好的解决问题。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf632590500e4a648521136525df77da~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-32">招聘</h2>
<p>以上就是我今天的所有的分享，这边是我们团队公众号的二维码，大家可以去了解一下我们团队的一些输出，同时我们近期也是在招聘前端实习生、资深、高级前端工程师。如果有兴趣的话，可以向下面的邮箱 进行简历的投递，感谢大家~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c3bef98600741709460309ff2f128f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-33">QA</h2>
<blockquote>
<p>请问子洋：如何进行热更新呢？据我了解 Electron 打包出来的页面是放在包内的，如何进行在线更新？</p>
</blockquote>
<p>我理解问题应该是 UI 层界面的更新。其实刚才我有提到过，我们对页面的一些静态资源是做了一个 cdn 上的托管，在更新的时候，会有一个检测更新的机制，它可以通过轮询或者服务端推送来实现，当收到静态资源版本更新的通知，通过主进程对渲染进程进行一个忽略缓存的强制刷新，或者说可以通过在主进程有相应的交互，包括升级提醒和更新日志，让用户触发页面重载，去更新 UI 层面的静态资源。</p>
<blockquote>
<p>请问子洋：Electron 和 NW.js 的区别能请您对比一下吗？</p>
</blockquote>
<p>它们两个最大的区别是在于对 Node.js 和 Chromium 事件循环机制的整合的处理方式是不一样的。首先 NW.js 是通过修改源码的方式，让 Chromium 与 Node.js 的事件循环机制进行打通； Electron 实现的机制是通过启用一个新的安全线程，在 Node.js 和 Chromium 之间做事件转发，这样来实现两者的打通。这样的一个好处就是 Chromium 和 Node.js 的事件循环机制不会有这么强的耦合。另外的区别则是 NW.js 支持 xp 系统，Electron 是不支持的。相比较而言 Electron 有着更活跃的社区，以及更多的大型应用如 VS code、Atom 的实践案例，更多的区别可以参考 Electron 官方的一篇介绍：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Fdevelopment%2Felectron-vs-nwjs" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electronjs.org/docs/development/electron-vs-nwjs" ref="nofollow noopener noreferrer">www.electronjs.org/docs/develo…</a></p>
<blockquote>
<p>请问子洋：更新包的文件是放在私有文件服务器还是 Gitlab 或者 Github 上面？</p>
</blockquote>
<p>有比较多方式，我们的实现是通过 CDN 的托管，也可以通过 Github 或者私有文件服务器的搭建来实现。根据自己实际的业务场景和技术栈来选择。</p>
<hr>
<p>关注前端早早聊，跟进学习更多 BFF/GraphQL，请关注第三十届|前端早早聊大会 BFF 专场 - 玩转前后端接口（GraphQL、统一网关、API 接入、API 管理、协议转换、统一安全切面、高并发处理、可视化编排、统一稳定性建设...）8-14 全天直播，9 位讲师，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2Ftl30" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/tl30" ref="nofollow noopener noreferrer">报名上车看直播👉 )：</a></p></div>  
</div>
            