
---
title: 'Next.js 12 正式发布，速度最高提升 5 倍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4520'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4520'
---

<div>   
<div class="content">
                                                                                            <p>Next.js 12 被官方誉为是有史以来更新幅度最大的版本，该版本带来的变化如下：</p> 
<h3>版本特性</h3> 
<ul> 
 <li>Rust 编译器：本地刷新速度提高了约 3 倍，构建速度提高了约 5 倍；</li> 
 <li>中间件（Beta）：在 Next.js 中使用代码而不是配置，实现了充分的灵活性；</li> 
 <li>支持 React 18：现在支持 Native Next.js 的 API，以及 React 18 中的 Suspense；</li> 
 <li>AVIF 支持：与 WebP 相比，可减少图片体积约 20%；</li> 
 <li>本地 ES 模块支持：与标准化的模块系统保持一致；</li> 
 <li>URL 导入（Alpha）：从任何 URL 导入包，不需要安装或单独的构建步骤；</li> 
 <li>React 服务器组件（Alpha）：包括 SSR Streaming；</li> 
</ul> 
<p>开发者可以通过运行 <code>npm i next@latest</code> 进行更新。</p> 
<h3><strong>重大变化</strong></h3> 
<ul> 
 <li>在将 webpack 5 设为 Next.js 11 中的默认版本后，现在正式在 Next.js 中移除了 webpack 4；</li> 
 <li>不再需要<code>next.config.js</code>中的 <code>target</code></li> 
 <li><code>next/image</code>现在使用<code>span</code>而不是 <code>div</code>作为 Wrapping 元素；</li> 
 <li>Node.js 的最低版本已经从<code>12.0.0</code>升级至<code>12.22.0</code>，这是第一个原生支持 ES 模块的 Node.js 版本；</li> 
</ul> 
<h3>其他改进</h3> 
<ul> 
 <li>将 <code>pages/_app.js</code> 或 <code>pages/_document.js</code> 添加到你的应用程序，现在会自动替换内置版本，而不需要重新启动 Next.js CLI；</li> 
 <li>ESLint 集成现在支持在 <code>Next lint</code> 中使用 <code>--file</code> 标志进行单文件检查；</li> 
 <li>Next.js 12 现在支持设置自定义 <code>tsconfig.json</code> 路径；</li> 
 <li><code>next.config.mjs</code> 现在支持将配置写成 ES 模块；</li> 
 <li>对静态页面的检查现在使用共享工作池运行；</li> 
 <li>快速刷新现在使用 WebSocket 连接而不是 EventSource 连接；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12" target="_blank">https://nextjs.org/blog/next-12</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            