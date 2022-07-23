
---
title: 'Deno 1.24 发布，JavaScript 运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7548'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7548'
---

<div>   
<div class="content">
                                                                                            <p>Deno 是一个简单、现代和安全的 JavaScript 和 TypeScript 的运行时，它使用 V8 并以 Rust 构建。</p> 
<p>Deno 1.24 已发布，值得关注的更新包括：</p> 
<h3>类型检查和发射的性能改进</h3> 
<p>以前，当指定 <code>--check</code> 标志时，Deno 内部使用 TypeScript 编译器将 TypeScript 代码转换为 JavaScript，否则就使用 swc。在这个版本中，所有的发射都是用 swc 完成的，这要快得多。</p> 
<p>此外，由于一些架构的重构：</p> 
<ul> 
 <li>发射不再发生在 <code>deno check</code> 中</li> 
 <li>用来存储发射的 JavaScript 的缓存更加强大</li> 
 <li>如果 Deno 在过去已经成功地对某些代码进行了类型检查，那么它将更聪明地不进行类型检查。</li> 
</ul> 
<p>总的来说，这些改进应该有相当大的性能改善，但会因代码库的不同而不同。</p> 
<h3><code>unhandledrejection</code> 事件</h3> 
<p>这个版本增加了对 <code>unhandledrejection</code> 事件的支持。</p> 
<h3><code>beforeunload</code> 事件</h3> 
<p>这个版本增加了对 <code>beforeunload</code> 事件的支持。当事件循环没有更多的工作要做并即将退出时，该事件被触发。安排更多的异步工作（如定时器或网络请求）将导致程序继续。</p> 
<h3><code>import.meta.resolve()</code> API</h3> 
<p>Deno 从 v1.0 开始支持 <code>import.meta</code>。两个可用的选项是 <code>import.meta.url</code> 和 <code>import.meta.main</code>，这个版本增加了对 <code>import.meta.resolve()</code> API 的支持，它可以让你解决相对于当前模块的指定器。</p> 
<h3>FFI API 的改进</h3> 
<p>这个版本在不稳定的 FFI API 中增加了新的功能和性能改进</p> 
<h3>对新的子进程 API 的更新</h3> 
<p>在 Deno v1.21 中，引入了一个新的不稳定的子进程 API。这个版本对这个 API 进行了重大更新。</p> 
<h3>LSP 改进</h3> 
<p>这个版本在编辑器中提供了更好的自动导入支持，不再像以前在某些情况下需要缓存依赖关系后重新启动 LSP。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p>
                                        </div>
                                      
</div>
            