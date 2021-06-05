
---
title: 'JavaScript沙箱'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7552'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 01:20:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=7552'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>参考链接： <a href="https://mp.weixin.qq.com/s/qOw0-u8w2Kjl-aDrCmUXYQ" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/qOw0-u8w2…</a></p>
<h1 data-id="heading-0">在微前端架构中，JavaScript沙箱需要解决的问题</h1>
<ol>
<li>挂在window上的全局方法/变量（如setTimeout、滚动等全局事件监听等）在子应用切换时的清理和还原</li>
<li>Cookie、LocalStorage等的读写安全策略限制</li>
<li>各子应用独立路由的实现</li>
<li>多个微应用共存时相互独立的实现</li>
</ol>
<h1 data-id="heading-1">qiankun架构设计中，JavaScript沙箱的实现</h1>
<h2 data-id="heading-2">核心文件</h2>
<ul>
<li>关注两个入口文件proxySandbox.ts和snapshotSandbox.ts</li>
</ul>
<h2 data-id="heading-3">技术方案</h2>
<ul>
<li>他们分别基于proxy实现代理了window上的常用的常量和方法</li>
<li>不支持proxy时降级通过快照实现备份还原</li>
</ul>
<h2 data-id="heading-4">实现思路</h2>
<p>起初版本使用了快照沙箱的概念，模拟ES6的proxy API，通过代理劫持window，当子应用修改或使用window上的属性和方法时，把对应的操作记录下来，每次子应用挂载/卸载时生成快照，当再次从外部切回当前子应用时，再从记录的快照中恢复，而后来为了兼容多个子应用共存的情况，又基于Proxy实现了处理所有全局性的常量和方法接口，为每个子应用构造了独立的运行环境。</p>
<h1 data-id="heading-5">阿里云开发平台的Browser VM</h1>
<h2 data-id="heading-6">核心文件</h2>
<p>Context.js</p>
<h2 data-id="heading-7">实现思路</h2>
<ol>
<li>借鉴with的实现效果，在webpack编译打包阶段为每个子应用代码包裹一层代码（见其插件包breezr-plugin-os下相关文件），创建一个闭包，传入自己模拟的window、document、location、history等全局对象（见根目录下相关文件）</li>
<li>在模拟的Context中，new一个iframe对象，提供一个和宿主应用空的（about：blank）同域URL来作为这个iframe初始加载的URL（空的URL不会发生资源加载，但是会产生和这个iframe关联的history不能被操作的问题，这事路由的变换只支持hash模式），然后将其下的原生浏览器对象通过contentWindow取出来（因为iframe对象天然隔离，这里省去了自己Mock实现所有API的成本）</li>
<li>取出对应的iframe中原生的对象之后，继续对特定需要隔离的对象生成对应的Proxy，然后对一些特定的实现（比如window.document需要返回特定的沙箱document而不是当前浏览器的document等）</li>
<li>为了文档内容能够被加载在同一个DOM树，对于document，大部分的DOM操作的属性和方法仍然直接使用宿主浏览器的document的属性和方法处理等</li>
</ol>
<h1 data-id="heading-8">Figma</h1>
<h2 data-id="heading-9">历史实现方案</h2>
<ul>
<li>起初 Figma 同样是将插件代码放入 iframe 中执行并通过 postMessage 与主线程通信，但由于易用性以及 postMessage 序列化带来的性能等问题，Figma 选择还是将插件放入主线程去执行。</li>
</ul>
<h2 data-id="heading-10">实现方案</h2>
<ul>
<li>Figma 采用的方案是基于目前还在草案阶段 Realm API，并将 JavaScript 解释器的一种 C++ 实现 Duktape 编译到了 WebAssembly，然后将其嵌入到 Realm 上下文中，实现了其产品下的三方插件的独立运行。</li>
</ul>
<h1 data-id="heading-11">构思web worker实现js隔离</h1></div>  
</div>
            