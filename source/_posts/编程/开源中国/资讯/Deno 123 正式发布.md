
---
title: 'Deno 1.23 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4052'
author: 开源中国
comments: false
date: Sat, 18 Jun 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4052'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Deno 1.23 已发布，值得关注的更新包括：</p> 
<h3>默认不进行类型检查</h3> 
<p>当要求执行一个程序时，Deno 总是运行一个类型检查。然而，评估和类型检查是完全不同的操作，涉及完全不同的编译器，每个编译器的执行速度也完全不同。评估代码使用 Google 的 V8，而类型检查使用微软的 TypeScript 编译器。类型检查的速度相当慢，而 V8 的启动和评估则非常快。</p> 
<p>如果你仍然想要回到以前的行为，请使用 <code>--check</code> 标志。</p> 
<h3>移除不稳定的 <code>Deno.sleepSync</code> API</h3> 
<p>在这个版本中，由于没有明确的必要性 <code>Deno.sleepSync</code> 被删除了，因为这个功能已经可以通过现有的 Web API 获得。此外这也是一个很可能会引起问题的功能。 <code>Deno.sleepSync</code> 完全阻塞了事件循环。</p> 
<h3>文件观察器观察动态导入</h3> 
<p>从 v1.23 开始，内置的文件观察器（你可以用 <code>--watch</code> 标志激活）也会观察动态导入的文件的变化。</p> 
<p>这个功能使得 Fresh Web 框架的开发者体验大大提升。</p> 
<h3>对 <code>deno fmt</code> 的更新</h3> 
<p><code>deno fmt</code> 现在默认格式化 .cjs、.cts、.mjs 和 .mts 文件。此外，类型中一些不必要的括号将被自动删除。</p> 
<h3>新的不稳定的 <code>Deno.getGid()</code> API</h3> 
<p>在 v1.23 版本中，Deno 增加了一个新的不稳定的 API： <code>Deno.getGid()</code>。使用这个 API，你可以检索到用户组的 ID。请注意，这个 API 在 Linux 和 macOS 上有效，但在 Windows 上会返回 <code>null</code>。</p> 
<h3><code>deno info</code> 支持 <code>-config</code> 和 <code>-no-config</code> 标志</h3> 
<p>这个版本增加了对 <code>--config</code> 和 <code>--no-config</code> 标志的支持。在以前的版本中， <code>deno info</code> 会自动查找 <code>deno.json</code> 文件，但没有办法手动指定配置文件或完全禁用它。</p> 
<h3>TypeScript 4.7</h3> 
<p>Deno v1.23 采用了最新的 TypeScript 稳定版本。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdenoland%2Fdeno%2Freleases" target="_blank">https://github.com/denoland/deno/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            