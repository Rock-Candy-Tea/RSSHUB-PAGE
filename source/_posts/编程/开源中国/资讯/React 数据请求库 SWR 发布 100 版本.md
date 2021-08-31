
---
title: 'React 数据请求库 SWR 发布 1.0.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f8afd723d2fa759afa202ba1fc58189119b.png'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 06:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f8afd723d2fa759afa202ba1fc58189119b.png'
---

<div>   
<div class="content">
                                                                                            <p>React 数据请求库 SWR 1.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswr.vercel.app%2Fblog%2Fswr-v1" target="_blank">已正式发布</a>。SWR 是用于数据请求的 React Hooks 库，其名字来自于<code>stale-while-revalidate</code>：一种由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc5861" target="_blank">HTTP RFC 5861</a> 推广的 HTTP 缓存失效策略。这种策略首先从缓存中返回数据（过期的），同时发送 fetch 请求（重新验证），最后得到最新数据。</p> 
<blockquote> 
 <p>使用 SWR，组件将会不断地、自动获得最新数据流。<br> UI 也会一直保持快速响应。</p> 
</blockquote> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f8afd723d2fa759afa202ba1fc58189119b.png" referrerpolicy="no-referrer"></p> 
<p>新特性：</p> 
<ul> 
 <li> <p>更轻量：1.0.0 版本相较上一版本 0.5.6 核心体积减小 41%，安装包体积减小 52%，优化 tree-shaking</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b9b724a269b1a2ffb8bb3f3cf7fdcd95260.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>支持预加载数据作为 fallback：对于服务端渲染 (SSR)、静态站点生成 (SSG) 等场景有更好的支持</p> </li> 
</ul> 
<p>1.0 增加了新的<code>fallback</code>选项，支持提供任何预抓取 (pre-fetched) 数据作为所有具有特定键值的 SWR hooks 的初始值：</p> 
<pre><code class="language-javascript"><SWRConfig value=&#123;&#123;
  fallback: &#123;
    '/api/user': &#123; name: 'Bob', ... &#125;,
    '/api/items': ...,
    ...
  &#125;
&#125;&#125;>
  <App/>
</SWRConfig></code></pre> 
<ul> 
 <li> <p>支持 immutable 模式：可定义数据为 immutable，不重复请求</p> </li> 
</ul> 
<pre><code class="language-javascript">import useSWRImmutable from 'swr/immutable'

// ...

useSWRImmutable(key, fetcher, options)</code></pre> 
<ul> 
 <li> <p>中间件 (middleware) 支持：多场景拓展（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswr.vercel.app%2Fdocs%2Fmiddleware" target="_blank">示例</a>）</p> </li> 
</ul> 
<pre><code class="language-javascript"><SWRConfig value=&#123;&#123; use: [...middleware] &#125;&#125;>

// ... or directly in `useSWR`:
useSWR(key, fetcher, &#123; use: [...middleware] &#125;)</code></pre> 
<ul> 
 <li> <p>自定义缓存提供层：持久化、离线、测试等场景（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fswr.vercel.app%2Fdocs%2Fadvanced%2Fcache" target="_blank">文档</a>）</p> </li> 
</ul> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswr.vercel.app%2Fblog%2Fswr-v1" target="_blank">Announcing SWR 1.0 – SWR</a>。</p>
                                        </div>
                                      
</div>
            