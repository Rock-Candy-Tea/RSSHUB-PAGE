
---
title: 'Midway 2.13.3 发布，适用于构建 Serverless 服务的 Node.js 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5249'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 14:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5249'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <p style="margin-left:0; margin-right:0"><span>临近双十一，我们的发版会更加的慎重，周期变长，请谅解。</span></p> 
 <h2 style="margin-left:0; margin-right:0"><span>Features</span></h2> 
 <h3 style="margin-left:0; margin-right:0"><span>1、提供了一批新的组件</span></h3> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>1、tablestore 组件，for aliyun tablestore，并提供了完整的多实例方案和 ts 定义 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fmidwayjs%2Fmidway_v2%2Ftablestore" target="_blank"><span>使用文档</span></a></li> 
  <li><span>2、view 系列的组件，比如 view-ejs 和 view-nunjucks，</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fmidwayjs%2Fmidway_v2%2Frender" target="_blank"><span>使用文档</span></a></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0"><span>Bugfix</span></h2> 
 <h3 style="margin-left:0; margin-right:0"><span>1、provide uuid 改造后的循环注入问题</span></h3> 
 <p style="margin-left:0; margin-right:0"><span>感谢社区 @</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHuJingKang" target="_blank"><span>HuJingKang</span></a><span> 提供此 PR。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>在 v2.13.0 版本新增了providerUUId 之后，在组件中使用循环依赖会导致程序卡死，这一 PR 修复了该问题并提供了 case，后续可以避免再次出现。</span></p> 
 <h3 style="margin-left:0; margin-right:0"><span>2、修复一个隐藏的内存泄露问题</span></h3> 
 <p style="margin-left:0; margin-right:0"><span>在 Serverless 场景下是，运行时使用了一个 node 内置的 perf_hooks 的 performance 打点 API，该模块在记录后不会清理数据，导致在请求量过大时内存溢出。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>由于该泄露点非常小，在大量的压测后我们才定位发现该问题，现已修复。</span></p> 
 <h3 style="margin-left:0; margin-right:0"><span>3、修复函数式 configuration 的异步问题</span></h3> 
 <p style="margin-left:0; margin-right:0"><span>在之前提供的函数式 configuration 写法中遗漏了 async 函数的处理，导致 onReady 中的异步会返回 Promise，在某些情况下会卡住进行，在新版本中处理了该问题。</span></p> 
 <h3 style="margin-left:0; margin-right:0"><span>4、orm 组件中 geRepository 系列 API 的问题</span></h3> 
 <p style="margin-left:0; margin-right:0"><span>在之前版本中，我们提供了多个 connection 的写法，同时将获取连接池的注入变成了回调形式，但是漏改了 getRepository 系列 API，导致这些 API 不可用。新版本修复了该问题。</span></p> 
</div>
                                        </div>
                                      
</div>
            