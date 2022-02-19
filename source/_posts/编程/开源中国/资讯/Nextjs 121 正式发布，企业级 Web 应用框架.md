
---
title: 'Next.js 12.1 正式发布，企业级 Web 应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8997'
author: 开源中国
comments: false
date: Sat, 19 Feb 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8997'
---

<div>   
<div class="content">
                                                                                            <p>Next.js 12.1 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1" target="_blank">发布</a>。</p> 
<p><strong>新特性概览</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23on-demand-incremental-static-regeneration-beta" target="_blank"><strong>按需使用的 ISR (Beta)</strong></a>：支持即时使用<code>getStaticProps</code><span>重新验证页面</span></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23improved-swc-support" target="_blank">扩展对 SWC 的支持</a></strong>：引入<code>styled-components</code>和 Relay 等功能</li> 
 <li><strong>引入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23zero-configuration-jest-plugin" target="_blank"><code>next/jest</code>插件</a></strong><span>：</span>使用 SWC 实现零配置支持 Jest</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23faster-minification-with-swc" target="_blank">通过 SWC (RC) 提供更快的压缩</a></strong>：比 Terser 快 7 倍的压缩速度</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23self-hosted-nextjs-improvements" target="_blank">优化自托管功能</a></strong>：减小 Docker 镜像体积约 80%</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-12-1%23react-18-server-components-and-ssr-streaming-alpha" target="_blank"><strong>React 18 & Server Components (Alpha)</strong></a><span>：</span>优化稳定性和支持情况</li> 
</ul> 
<p><strong>按需使用的 ISR (Beta)</strong></p> 
<p>ISR 是 Next.js 9.5 引入的功能，本次的更新提供了按需使用的特性，开发者可按需手动清除特定页面的 Next.js 缓存。</p> 
<pre><code class="language-javascript">// pages/api/revalidate.js

export default async function handler(req, res) &#123;
  // Check for secret to confirm this is a valid request
  if (req.query.secret !== process.env.MY_SECRET_TOKEN) &#123;
    return res.status(401).json(&#123; message: 'Invalid token' &#125;)
  &#125;

  try &#123;
    await res.unstable_revalidate('/path-to-revalidate')
    return res.json(&#123; revalidated: true &#125;)
  &#125; catch (err) &#123;
    // If there was an error, Next.js will continue
    // to show the last successfully generated page
    return res.status(500).send('Error revalidating')
  &#125;
&#125;</code></pre> 
<p><strong>零配置 Jest 插件</strong></p> 
<p>Next.js 现已支持自动配置 Jest，使用基于 Rust 的 Next.js 编译器来转换文件，包括：</p> 
<ul> 
 <li>自动模拟样式表（<code>.css</code>,<span> </span><code>.module.css</code>和<code>.scss</code>变体），以及图像导入</li> 
 <li>将<code>.env</code>加载到<code>process.env</code></li> 
 <li><span>忽略测试解析和转换的</span><code>node_modules</code></li> 
 <li><span>忽略测试解析的</span><code>.next</code></li> 
 <li>Loading<span> </span><code>next.config.js</code><span> </span>for flags that enable Next.js compiler transforms</li> 
</ul> 
<p><strong>优化自托管功能</strong></p> 
<p>Next.js 现在支持自动创建<code>standalone</code>文件夹，该文件夹仅复制生产部署所需的文件。这使得自托管 Next.js 应用程序的<strong>Docker 映像缩小了约 80% 。</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Freleases%2Ftag%2Fv12.1.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            