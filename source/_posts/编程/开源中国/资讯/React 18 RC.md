
---
title: 'React 18 RC'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7594'
author: 开源中国
comments: false
date: Fri, 11 Mar 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7594'
---

<div>   
<div class="content">
                                                                                            <p>React 18 首个 RC 版本已发布。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F9" target="_blank">按照计划</a>，正式版将于 2~4 周后推出。</p> 
<p>React 18 引入了<span style="background-color:#ffffff; color:#333333"><span> </span>“并发渲染 (concurrent rendering)” 机制，它支持 React 同时准备多个版本的 UI。这个机制主要在幕后进行，但它为 React 启发了非常多新的可能性，以提升应用程序的真实与感知性能。</span>此外，React 18 还针对现有应用程序提供了渐近的采用策略。</p> 
<p><strong>安装 React 18 RC</strong></p> 
<p>使用 npm</p> 
<pre><code>npm install react@rc react-dom@rc</code></pre> 
<p>或者使用 yarn</p> 
<pre><code>yarn add react@rc react-dom@rc</code></pre> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>客户端渲染 API 的更新</li> 
 <li>服务器端渲染 API 的更新</li> 
 <li>自动批处理 (Automatic Batching)</li> 
 <li>更新严格模式 (Strict Mode)</li> 
 <li>不再支持 IE 浏览器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F82" target="_blank">更新以删除</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F82" target="_blank"><span> </span>“setState on unmounted component” 警告</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F72" target="_blank">Suspense不再需要<code>fallback</code>prop 来捕捉</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F75" target="_blank">组件现在可以在未定义的状态下进行渲染</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact%2Fpull%2F23355" target="_blank">弃用 renderSubtreeIntoContainer</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F96" target="_blank">StrictMode 更新为默认情况下不会静默双重日志记录</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fblog%2F2022%2F03%2F08%2Freact-18-upgrade-guide.html" target="_blank">更多内容点此查看</a>。</p>
                                        </div>
                                      
</div>
            