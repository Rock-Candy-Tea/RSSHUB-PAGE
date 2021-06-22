
---
title: 'Next.js 11 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-84db660b8fed5062cdb41a606dedb9534f6.png'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 07:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-84db660b8fed5062cdb41a606dedb9534f6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Next.js 11 已正式发布，新版本主要变化：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23conformance" target="_blank"><strong>一致性</strong></a>：提供精心打磨的解决方案以支持最佳用户体验的系统</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23improved-performance" target="_blank"><strong>提升性能</strong></a>：进一步优化以缩短冷启动时间，以便开发者更快地开始编码</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23script-optimization" target="_blank"><strong><code>next/script</code></strong></a>：自动优先加载第三方脚本以提升性能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23image-improvements" target="_blank"><strong><code>next/image</code></strong></a>：通过自动尺寸检测和对模糊占位符的支持，减少布局偏移并创建更流畅的视觉体验</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23webpack-5" target="_blank"><strong>Webpack 5</strong></a>：现在默认为所有 Next.js 应用程序启用 Webpack 5，为所有 Next.js 开发人员带来<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23webpack-5" target="_blank">这些好处</a></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23cra-migration" target="_blank">创建 React App 迁移（实验阶段）</a></strong>：自动转换 Create React App 以兼容 Next.js</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11%23nextjs-live-preview-release" target="_blank"><strong>Next.js Live（预览版）</strong></a>：与团队成员在浏览器中实时编码</li> 
</ul> 
<h3>提升性能</h3> 
<p>开发团队表示，从 Next.js 10 开始，他们一直致力于进一步优化 Next.js 的开发者体验。在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-1" target="_blank">10.1</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2" target="_blank">10.2</a> 中，他们将启动时间缩短了 24%<strong>，</strong>并通过 React Fast Refresh 将处理时间再减少了40%。</p> 
<p>现在，Next.js 11 包含对 Babel 的另一项优化，以进一步缩短启动时间。开发团队为 webpack 创建了一个全新的 Babel 加载器实现，优化了加载并添加了内存配置缓存层。因此，实际使用上对开发人员来说并没有变化<strong>，</strong>但最终却带来了更快的开发体验。</p> 
<h3>Webpack 5</h3> 
<p>在 Next.js 10.2 中，开发团队将 webpack 5 的推广范围扩大到所有在<code>next.config.js</code>文件中没有自定义 webpack 配置的应用程序。现在，他们将 webpack 5 作为所有 Next.js 应用程序的默认配置，预计将会提供多项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-10-2%23webpack-5" target="_blank">功能和改进</a>。</p> 
<p>开发团队表示会与社区密切合作，以确保顺利过渡到 webpack 5，现有的超过 3400 个 Next.js 集成测试在每个启用 webpack 5 的 PR 上运行。他们说道，如果开发者的应用程序有一个自定义的 webpack 配置，建议遵循 webpack 5 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fdocs%2Fmessages%2Fwebpack5" target="_blank">升级文档</a>。</p> 
<h3>Next.js Live（预览版）</h3> 
<p>Next.js Live 通过利用 ServiceWorker、WebAssembly 和 ES Module 等前沿技术，将整个开发过程放在了网络浏览器中。因此这也开启了一些可能性，比如通过一个 URL 来即时协作和分享，而不需要构建步骤。对于开发者来说，这意味着更快的反馈循环，更少的等待构建时间，以及在浏览器中进行实时结对编程和编辑。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-84db660b8fed5062cdb41a606dedb9534f6.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnextjs.org%2Fblog%2Fnext-11" target="_blank">详细内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            