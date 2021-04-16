
---
title: 'Deno 1.9 发布：新增原生 HTTP_2 Web 服务器、优化 Rust 调用效率'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f09a085c51bbb32cea6ac40dbdf3e5e7a75.png'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 07:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f09a085c51bbb32cea6ac40dbdf3e5e7a75.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="color:#333333">Deno 1.9 已正式发布，此版本包含许多新功能、性能优化以及错误修复。</span></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9%23native-http%252F2-web-server" target="_blank">原生 HTTP/2 Web 服务器</a></strong>：Deno 新增了一个快速且功能完整的 HTTP 服务器</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9%23faster-calls-into-rust-with-serde_v8" target="_blank">使用 serde_v8 更快地调用 Rust</a></strong>：整体性能大约优化了 98%</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9%23blob-url-support-%2526-improvements-to-fetch" target="_blank">支持 Blob URL & 优化<code>fetch</code></a></strong>：<span style="color:#24292e">新的 Web 兼容性功能</span></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9%23import-completions-in-the-lsp" target="_blank">在 LSP 中支持自动补全 import</a></strong>：支持在本地、远程和注册补全场景中使用</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9%23allow-lists-for---allow-env-and---allow-run" target="_blank">具有交互的权限提示</a></strong>：<span style="color:#24292e">以交互的方式提示正在使用的权限，而不是事先声明它们</span></li> 
</ul> 
<p><span style="background-color:#ffffff"><span style="color:#333333">如果已经安装了 Deno，运行</span></span><code>deno upgrade</code><span style="background-color:#ffffff"><span style="color:#333333">命令即可升级到 1.9 版本。如果是首次安装，可以参考下面的方法：</span></span></p> 
<pre><code># Using Shell (macOS and Linux):
curl -fsSL https://deno.land/x/install/install.sh | sh

# Using PowerShell (Windows):
iwr https://deno.land/x/install/install.ps1 -useb | iex

# Using Homebrew (macOS):
brew install deno

# Using Scoop (Windows):
scoop install deno

# Using Chocolatey (Windows):
choco install deno</code></pre> 
<h1 style="text-align:left">新增原生 HTTP/2 Web 服务器</h1> 
<div style="text-align:start"> 
 <p style="text-align:justify">Deno 当前的 HTTP 服务器为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.land%2Fstd%2Fhttp" target="_blank">std/http</a><span style="color:#24292e">，</span>这是一个使用纯 TypeScript 开发，基于 TCP Socket 之上的实现。尽管它是一个脚本式的 HTTP 服务器，但在尾延迟 (Tail Latency) 上的表现却十分良好，唯一的缺点就是只支持 HTTP/1.1，并且难以升级成为 HTTP/2。</p> 
</div> 
<div style="text-align:start"> 
 <p style="text-align:justify"><span style="color:#333333">而开发团队也不想花费精力开发 HTTP 服务器，因此便聘用了 Hyper 团队替 Deno 构建了一个全新的 HTTP/2 服务器 API，与纯 TypeScript 实现的 HTTP 服务器 std/http 相比，他们测试发现新服务器提升了 48％ 的吞吐量。目前新 HTTP/2 服务器 API 仍处于测试阶段，开发者需要在 API 使用<code>--unstable</code>标签方可试用，Deno 开发团队表示他们会尽量让 API 进入稳定阶段。</span></p> 
 <p style="text-align:justify"><span style="color:#333333"><img alt src="https://oscimg.oschina.net/oscnet/up-f09a085c51bbb32cea6ac40dbdf3e5e7a75.png" referrerpolicy="no-referrer"></span></p> 
 <h1 style="text-align:start"><span style="color:#24292e">使用 serde_v8 优化 Rust 调用</span></h1> 
 <p><span style="background-color:#ffffff"><span style="color:#333333">Deno 1.9 中，调用 Rust 的性能也获得大幅度的改进。Deno 开发团队删除了 1500 多行核心代码，并且改进了</span></span> <span style="color:#24292e">baseline binding (AKA ops or opcalls)</span> 的开销，以及<span style="background-color:#ffffff"><span style="color:#333333">建立更干净的操作基础，对未来发展有一定帮助（插件、优化等）。</span></span></p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-da059cf5ecdbe924bd7bb5ba53add39b8cc.png" referrerpolicy="no-referrer"></p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-baa42e97243c3ff498ad50d40f9f2ebe548.png" referrerpolicy="no-referrer"></p> 
 <h1 style="text-align:start"><span style="color:#24292e">支持 Blob URL 和改进 <code>fetch</code></span></h1> 
 <p>Deno 在此版本引入了对<code>blob:</code>（也称为对象 URL）的支持。用于创建和撤消 Blob URL 的 API 与浏览器中的 API 相同：</p> 
 <pre><code>const blob = new Blob(["Hello World!"]);
const url = URL.createObjectURL(blob);
console.log(url); // blob:null/7b09af21-03d5-461e-90a3-af329667d0ac

const resp = await fetch(url);
console.log(await resp.text()); // Hello World!

URL.revokeObjectURL(url);
</code></pre> 
 <p><code>fetch</code><span style="color:#24292e">支持 Blob URL，以及</span><code>data</code><span style="color:#24292e"> URL：</span></p> 
 <pre><code>const resp = await fetch("data:text/plain;base64,SGVsbG8gV29ybGQh");
console.log(await resp.text()); // Hello World!</code></pre> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.9" target="_blank">详细内容查看发布公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            