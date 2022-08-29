
---
title: 'Deno 1.25 发布，新增 deno init 命令'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9761'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9761'
---

<div>   
<div class="content">
                                                                                            <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.25 已发布，值得关注的更新包括：</p> 
<h3><code>deno init</code> 子命令</h3> 
<p>用 Deno 启动一个新的项目一直很简单：你只需要一个文件就可以开始了。不需要任何配置文件、依赖清单或构建脚本。来自其他生态的用户通常不习惯这种简单性 —— 他们通常会寻找一个工具来搭建一个基本的项目结构。</p> 
<p>在这个版本中，Deno 增加了一个 <code>deno init</code> 子命令，用来构建一个基本的 Deno 项目。</p> 
<pre><code>$ deno init
✅ Project initialized
Run these commands to get started
  deno run main.ts
  deno test

$ deno run main.ts
Add 2 + 3 = 5

$ deno test
Check file:///dev/main_test.ts
running 1 test from main_test.ts
addTest ... ok (6ms)

ok | 1 passed | 0 failed (29ms)
</code></pre> 
<h3>实验性的 npm 支持</h3> 
<p>这个版本增加了对 npm 的实验性支持。需要强调的是，这项功能仍在开发中。Deno 在接下来的几个版本中改善兼容性层和用户体验。</p> 
<h3>新的实验性 HTTP 服务器 API</h3> 
<p>Deno 1.25 引入了一个新的实验性 HTTP 服务器，旨在提供一流的 HTTP 性能。我们的基准显示，与 Node.js 相比，每秒的 hello-world 请求性能提高了 4 倍，与我们现有的网络服务器相比，提高了 3 倍。新的服务器甚至比 Rust HTTP 服务器 Hyper 的单线程配置快 20%。</p> 
<h3>对启动时间的改进</h3> 
<p>当 Deno 启动时，它提前分析了依赖关系，以确保远程模块被缓存。这种依赖性分析对大文件来说可能相当不友好，因此在 Deno 1.25 中，它会在幕后缓存每个文件。你应该能够注意到启动时间有了相当大的改善。</p> 
<h3>更新到 <code>Deno.UnsafePointerView</code>API</h3> 
<p>向 <code>Deno.UnsafePointerView</code>添加了三个新的静态方法</p> 
<ul> 
 <li><code>Deno.UnsafePointerView#getCString</code></li> 
 <li><code>Deno.UnsafePointerView#getArrayBuffer</code></li> 
 <li><code>Deno.UnsafePointerView#copyInto</code></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p>
                                        </div>
                                      
</div>
            