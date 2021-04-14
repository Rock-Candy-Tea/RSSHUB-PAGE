
---
title: '我国首个 JS 语言提案在 ECMA 进入 Stage 3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2954163190e94cd484ad5218f213790b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 22:14:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2954163190e94cd484ad5218f213790b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>近期，在 ECMA 标准化组织的 TC39 技术委员会上，阿里巴巴前端标准化小组与淘系技术提出的 JavaScript 标准提案《Error Cause》进入了 Stage 3，将开始在 JavaScript 引擎中开始实现，并在浏览器、Node.js 实验性实施，是中国首个推进到 EcmaScript 的语言，将成为官方标准的自主技术提案。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2954163190e94cd484ad5218f213790b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">ECMA/T39 是什么？</h1>
<p>ECMA 是一个负责信息技术和通信系统的国际标准组织，全称欧洲标准化信息和通信系统协会。其中 ECMA/TC39 是技术委员会第 39 号技术委员会，主要负责 JavaScript 相关标准的制定，包括：</p>
<p>ECMA-262，即 JavaScript 的标准 ECMAScript 定义；
ECMA-402，即 ECMAScript 的国际化标准 API（ECMAScript Intl API）定义；
ECMA-404，即 JSON 定义；
T39 的成员主要包括：谷歌、微软、苹果、阿里巴巴、360、华为、腾讯等；</p>
<h1 data-id="heading-1">Error Cause 提案简介</h1>
<p>提案链接：<a href="https://github.com/tc39/proposal-error-cause" target="_blank" rel="nofollow noopener noreferrer">github.com/tc39/propos…</a></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f9d0b881dec41c8b422e6a062c61561~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个提案为 Error Constructor 新增了一个可选的参数 options，其中可以设置 cause 并且接受任意 JavaScript 值（JavaScript 可以 throw 任意值，如 undefined 或者字符串），将这个值赋值到新创建的 error.cause 上。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaf15901649248dfa6dbdc4ef1d6643a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
错误原因的特性在许多其他语言中都有类似的设计，如 C# Exception Cause，Java Exception Cause，Python raise exception from cause。同样的，在庞大的 JavaScript 生态中也已经有非常广泛的使用，如 verror 每周有上千万的下载量，@netflix/nerror 每周有数十万的下载量。</p>
<p>因为 Error Cause 以前没有标准化的参数定义及官方实现，所以容易丢失 error 的属性或需要写比较多的代码自定义等，并且开发者工具也难以依赖于非语言特性的自定义方案。本提案将 cause 写入了语言定义，能有效记录错误原因的值，可让开发者工具、应用监控如 Alinode 都能基于 cause 属性值获取错误逻辑链条，从而提升前端开发效率，降低重复开发成本。</p>
<p>作为阿里巴巴在加入 Ecma 标准化组织 TC39 技术委员会后的第一个落地的提案，这只是淘系技术在技术标准化上非常小的一步。</p>
<h1 data-id="heading-2">未来</h1>
<p>我们之所以进行这些提案，也是因为随着云原生技术在前端工程方面的大规模应用，语言的观测性能力格外重要。语言的观测能力直接影响到语言运行时的性能与成本。我们维护的 Node.js 发行版 Alinode 会在云原生时代的继续追求成本和性能的平衡。未来，我们也会结合阿里巴巴在步向云原生的技术业务场景，继续增加投入诸如异步上下文等关于观测性的核心语言特性提案，寻找 JavaScript 中长期以来困扰开发者的异步编程上下文追踪难题的解决方案，帮助基于云原生的业务建设更加精准、高机器效率、高工程效率的观测能力。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3340a1eb2bee4b3f8390523ea2a74a8d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
众所周知，Serverless 能够有效的优化成本，而“弹性”则是这一过程必不可少的手段。为了更好的实现弹性，启动速度是很关键的一环。Alinode Cloud Serverless Worker 按照 Web API 标准提供 JavaScript 运行环境，具有亚毫米级启动，业务应用 100ms 内启动并响应的特点，未来还将可以通过 Snapshot 快速水平（甚至跨服务器）扩展。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32eeb791e6534732ad71d1dc979bf3e9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>淘系技术非常注重标准化的参与和建设，我们也会继续从内部的技术场景中挖掘编程语言的拓展场景，探索商业技术、开发者与编程语言之间的深层次编程模型。同时，我们在前端其它核心领域的标准化也有所布局，比如 W3C 相关提案也在逐步推进中：</p>
<ul>
<li>滚动回收容器 Sliver：<a href="https://github.com/w3c/chinese-ig/issues/239" target="_blank" rel="nofollow noopener noreferrer">github.com/w3c/chinese…</a></li>
</ul>
<p>解决 Web 标准下滚动视图的复用回收问题，客户端开发中有 RecyclerView/UITableView 来实现滚动回收的布局容器，提案的 Display Sliver 定义了容器的布局方式以及当子元素滚动出 viewport 后的回收特性。</p>
<ul>
<li>常用手势事件：<a href="https://github.com/w3c/chinese-ig/issues/240" target="_blank" rel="nofollow noopener noreferrer">github.com/w3c/chinese…</a></li>
</ul>
<p>解决 Web 标准下集成常用的手势能力，客户端开发中有各种原生自带的如 Pan、Long Press 、Drag 等在 touch 之上封装的常用的基础手势能力，这使开发者可以更方便地直接使用这些手势能力，去快速开发一些交互更复杂的页面。提案期望在事件层做进一步的扩展，开发者可以直接在节点上绑定监听相关的手势事件，并在行为触发时派发相关事件。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            