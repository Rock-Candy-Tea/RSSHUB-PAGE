
---
title: 'Vue v3.1.0 (Pluto) 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7319'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 09:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7319'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Freleases%2Ftag%2Fv3.1.0" target="_blank">Vue.js v3.1.0</a> (Pluto) 已发布，目前的最新版本为 3.1.1。</p> 
<p>新版本增加了多项新特性，优化了性能，以及修复 bug，同时还有一些破坏性的变化。</p> 
<h2>新特性</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fmigration%2Fmigration-build.html" target="_blank">Migration Build</a>：提供兼容 Vue 2 行为的 Vue 3 构建。Migration Build 旨在帮助将现有的 Vue 2 应用程序迁移到 Vue 3</li> 
 <li><strong>compiler-core：</strong>支持空白字符处理策略 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2Fdee3d6ab8b4da6653d15eb148c51d9878007f6b6" target="_blank">dee3d6a</a>)</li> 
 <li>当使用 runtime 编译器时，支持组件级别的<code>compilerOptions</code>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2Fce0bbe053abaf8ba18de8baf535e175048596ee5" target="_blank">ce0bbe0</a>)</li> 
 <li><strong>config：</strong>支持通过<code>app.config.compilerOptions</code>配置 runtime 编译器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F091e6d67bfcc215227d78be578c68ead542481ad" target="_blank">091e6d6</a>)</li> 
 <li>支持通过<code>is="vue:xxx"</code>将普通元素转换为组件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2Faf9e6999e1779f56b5cf827b97310d8e4e1fe5ec" target="_blank">af9e699</a>)</li> 
 <li><strong>devtools：</strong>改进对 KeepAlive 的支持(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F03ae3006e1e678ade4377cd10d206e8f7b4ad0cb" target="_blank">03ae300</a>)</li> 
 <li><strong>devtools：</strong>引入性能事件 (performance events) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2Ff7c54caeb1dac69a26b79c98409e9633a7fe4bd3" target="_blank">f7c54ca</a>)</li> 
 <li>引入 onServerPrefetch (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fissues%2F3070" target="_blank">#3070</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F349eb0f0ad78f9cb491278eb4c7f9fe0c2e78b79" target="_blank">349eb0f</a>)</li> 
</ul> 
<h2>性能优化</h2> 
<ul> 
 <li>只有当实际改变时才会触发<code>$attrs</code>的更新 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F5566d39d467ebdd4e4234bc97d62600ff01ea28e" target="_blank">5566d39</a>)</li> 
 <li><strong>compiler：</strong>解析闭合标签时跳过不必要的检查 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F048ac299f35709b25ae1bc1efa67d2abc53dbc3b" target="_blank">048ac29</a>)</li> 
 <li>当使用 global mixins 时，避免对 props/emits 的规范化进行 deopt 处理</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Freleases%2Ftag%2Fv3.1.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            