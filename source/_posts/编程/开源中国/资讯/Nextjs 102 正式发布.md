
---
title: 'Next.js 10.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8eeacfcb687e07a1951ae8bcb60dc592a21.png'
author: 开源中国
comments: false
date: Tue, 11 May 2021 07:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8eeacfcb687e07a1951ae8bcb60dc592a21.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff"><span style="color:#111111">Next.js 10.2 稳定版已发布，主要变化如下：</span></span></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23webpack-5" target="_blank">提升构建速度</a></strong>：使用缓存后的构建速度提升了大约 60%</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23webpack-5" target="_blank">提升刷新速度</a></strong>：刷新时间提升了大约 100ms 到 200ms</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23improved-startup-performance" target="_blank">提升启动速度</a></strong>：<code>next dev</code>的启动速度提升了大约 24%</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23accessibility-improvements" target="_blank">改进可访问性</a></strong>：屏幕阅读器改变路由</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23header-cookie-and-query-matching-for-rewrites-and-redirects" target="_blank">更灵活的重定向和重写</a></strong>：支持匹配任意 header, cookie 或 query string</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23automatic-webfont-optimization" target="_blank">自动 Webfont 优化</a></strong>：<span style="background-color:#ffffff"><span style="color:#111111">通过内联字体 CSS 来提升性能</span></span></li> 
</ul> 
<blockquote> 
 <p>Next.js 是一个用于生产环境的 React 框架，提供了生产环境所需的所有功能以及最佳开发体验：包括静态及服务器端融合渲染、支持 TypeScript、智能化打包、路由预取等功能，无需任何配置。</p> 
</blockquote> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8eeacfcb687e07a1951ae8bcb60dc592a21.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><strong><span style="color:#111111"><span style="background-color:#ffffff"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23webpack-5" target="_blank">Webpack 5</a></span></span></strong></h2> 
<p style="text-align:start"><span style="color:#111111"><span style="background-color:#ffffff">开发团队表示，在 Next.js 10.1 中，他们优化了“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-1%233x-faster-refresh" target="_blank">快读刷新</a>”功能并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-1%23improved-installation-time" target="_blank">减少了安装时间</a>，现在又通过 Webpack 5 实现了其他的性能改进。</span></span></p> 
<p>启用 Webpack 5 后，使用者可自动获得新功能和改进。例如：改进磁盘缓存、改进快速刷新、改进资源的长期缓存和改进 Tree Shaking。</p> 
<h2 style="text-align:start"><strong><span style="color:#111111"><span style="background-color:#ffffff"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23improved-startup-performance" target="_blank">改进的启动性能</a></span></span></strong></h2> 
<p style="text-align:start"><span style="color:#111111"><span style="background-color:#ffffff">Next.js 团队改进了 Next.js CLI 的初始化，使</span></span><code>next dev</code><span style="color:#111111"><span style="background-color:#ffffff">首次运行后的启动时间缩短了大约 </span></span><strong>24％</strong><strong>。</strong><span style="color:#111111"><span style="background-color:#ffffff">例如，</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvercel.com%2F" target="_blank">vercel.com</a> 的<code>next dev</code><span style="color:#111111"><span style="background-color:#ffffff">从 3.3 秒变为 2.5 秒。</span></span></p> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23header-cookie-and-query-matching-for-rewrites-and-redirects" target="_blank">更灵活的重定向和重写</a></h2> 
<p style="text-align:start"><span style="color:#111111">Next.js 的重写、重定向和 header 现在支持新的<code>has</code>属性，可用于匹配传入的 header、cookie 和查询字符串。举个例子，Verce l客户 Joyn 使用<code>has</code>来优化内容的可发现性和性能。例如，可以根据 User-Agent 重定向旧的浏览器。</span></p> 
<pre><code class="language-javascript">// next.config.js

module.exports = &#123;
  async redirects() &#123;
    return [
      &#123;
        source: '/:path*',
        has: [
          &#123;
            type: 'header',
            key: 'User-Agent',
            value:
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)'
          &#125;
        ],
        destination: '/old-browser',
        permanent: false
      &#125;
    ]
  &#125;
&#125;</code></pre> 
<p style="text-align:start"><span style="background-color:#ffffff"><span style="color:#111111">另一个示例是根据用户的位置重定向用户：</span></span></p> 
<pre><code class="language-javascript">// next.config.js

module.exports = &#123;
  async redirects() &#123;
    return [
      &#123;
        source: '/:path*',
        has: [
          &#123;
            type: 'header',
            key: 'x-vercel-ip-country',
            value: 'GB'
          &#125;
        ],
        destination: '/:path*/uk',
        permanent: true
      &#125;
    ]
  &#125;
&#125;</code></pre> 
<p style="text-align:start"><span style="color:#111111"><span style="background-color:#ffffff">如果用户已经登录，也可以进行重定向：</span></span></p> 
<pre><code class="language-javascript">// next.config.js

module.exports = &#123;
  async redirects() &#123;
    return [
      &#123;
        source: '/:path*',
        has: [
          &#123;
            type: 'header',
            key: 'x-authorized',
            value: '(?<authorized>yes|true)'
          &#125;
        ],
        destination: '/dashboard?authorized=:authorized',
        permanent: false
      &#125;
    ]
  &#125;
&#125;</code></pre> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2" target="_blank">详细更新说明查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            