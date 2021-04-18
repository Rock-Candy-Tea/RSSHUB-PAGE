
---
title: '基于 Vite + React 构建 Chrome Extension (MV3) 开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5293d87a6bd64433a13ce866f9becb3a~tplv-k3u1fbpfcp-watermark.image?imageView2/2/w/480/h/480/q/85/interlace/1'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 00:54:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5293d87a6bd64433a13ce866f9becb3a~tplv-k3u1fbpfcp-watermark.image?imageView2/2/w/480/h/480/q/85/interlace/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>此前一直想做一个 bilibili 的弹幕扩展，最近借着研究 Vite 的契机实操了一下，花了两天时间算是搭好了基于 Vite + React 的 Chrome Extension (MV3) 开发环境，核心功能如下：</p>
<ul>
<li>📦️ JS 打包成单文件</li>
<li>🎨 自动引入 CSS</li>
<li>🔨 打包 service worker</li>
<li>🚀 开发环境热更新</li>
</ul>
<p>这里重点介绍一下当前热更新的实现，其他功能相对而言简单很多，详情可参考 <a href="https://github.com/theprimone/violet" target="_blank" rel="nofollow noopener noreferrer">theprimone/violet</a></p>
<blockquote>
<p>一次偶然的机会在 B 站看了 《紫罗兰永恒花园》，给人印象深刻，刚好这次打算做个 bilibili 的弹幕扩展，索性就取了女主名字中的 <strong>violet</strong> 😃</p>
</blockquote>
<h2 data-id="heading-1">实操</h2>
<p>热更新大致的流程如下图所示：</p>
<p><img alt="hot-reload-graph" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5293d87a6bd64433a13ce866f9becb3a~tplv-k3u1fbpfcp-watermark.image?imageView2/2/w/480/h/480/q/85/interlace/1" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">启动</h3>
<p>通过 <code>npm run dev</code> 同时执行三个命令：</p>
<ul>
<li>tsc 编译 service worker 并监听变化</li>
<li>vite 编译 extension</li>
<li>websocket 服务监听打包后目录 /dist 的变化</li>
</ul>
<p>其中，由于 <a href="https://github.com/vitejs/vite/issues/1434" target="_blank" rel="nofollow noopener noreferrer"><code>vite build --watch</code> 还未发布</a>，暂时通过<a href="https://github.com/theprimone/violet/blob/master/scripts/build-ext-watch.js" target="_blank" rel="nofollow noopener noreferrer">自定义脚本</a>监听源码变化，待 vite 该功能发布后可移除。</p>
<h3 data-id="heading-3">热更新</h3>
<p>浏览器页面加载 content scripts 后会创建一个 websocket 链接，服务端收到请求后会开启对 <code>/dist</code> 目录的监听，websocket 服务监听到 <code>/dist</code>  的变化后主动发起通知。</p>
<p>content scripts 收到需要更新 Extension 的通知，通过 <code>chrome.runtime.sendMessage</code> 触发 service worker 中通过 <code>chrome.runtime.onMessage</code> 注册的事件，依次触发 <code>chrome.runtime.reload</code> 和 <code>chrome.tabs.reload</code> 更新 Extension 和当前页面。实现了所写即所得，无需任何手动介入 🚀</p>
<p>可能会有读者有个疑问，为什么不直接在 service worker 中监听 websocket 的通知呢？</p>
<p>此前一直也是这么想的，在 Manifest V3 下使用 service worker 提倡 <a href="https://developer.chrome.com/docs/extensions/mv3/migrating_to_service_workers/#events" target="_blank" rel="nofollow noopener noreferrer">Thinking with events</a>，通过 <code>chrome.runtime.onInstalled</code> 和 <code>chrome.runtime.onStartup</code> 创建 websocket 客户端会被意外的关闭，即便是使用定时器轮询也会在执行多次之后被关闭再启动。因此，当前找到的最佳方案是在 service worker 中监听 <code>chrome.runtime.onMessage</code> 事件。</p>
<p>这样就实现了当页面加载当前 Extension 时才会触发热更新的流程。</p>
<h2 data-id="heading-4">总结</h2>
<p>由于现在的 Chrome Extension 大多是低于 MV3 版本的，两天下来，踩了不少坑，对于此前没有接触过的浏览器扩展开发也有了一定程度的了解。现在只是针对 Chrome Extension 的场景，后续会在不断完善当前场景的情况下，完成对其他浏览器扩展的支持。最终应该可以封装一个浏览器扩展开发的工具。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            