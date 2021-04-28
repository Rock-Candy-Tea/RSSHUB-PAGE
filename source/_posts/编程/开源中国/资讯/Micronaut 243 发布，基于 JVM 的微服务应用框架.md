
---
title: 'Micronaut 2.4.3 发布，基于 JVM 的微服务应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3723'
author: 开源中国
comments: false
date: Wed, 28 Apr 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3723'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Micronaut 是 Grails 框架作者打造的开源项目，也是新一代基于 JVM 的全栈微服务框架，用于构建模块化的、易于测试的微服务应用。有关 Micronaut 的特性介绍<a href="https://www.oschina.net/news/96381/micronaut-open-sourced">点此查看</a>。</p> 
<p>近日，Micronaut 2.4.3 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>改进 Init/Bean context 的性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5306" target="_blank">#5306</a>)；</li> 
 <li>将 micronaut-grpc 升级至 2.4.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5314" target="_blank">#5314</a>)；</li> 
 <li>将 micronaut-liquibase 升级至 3.3.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5312" target="_blank">#5312</a>)；</li> 
 <li>将 micronaut-kafka 升级至 3.3.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5308" target="_blank">#5308</a>)；</li> 
 <li>性能/内存优化 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5297" target="_blank">#5297</a>)；</li> 
 <li>将 micronaut-openapi 升级至 2.4.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5302" target="_blank">#5302</a>)；</li> 
 <li>构建：将 micronaut-problem-json 添加到 bom (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5300" target="_blank">#5300</a>)；</li> 
 <li>允许改变 Netty 的资源泄漏检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5298" target="_blank">#5298</a>)；</li> 
 <li>将 micronaut-data 升级至 2.4.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5296" target="_blank">#5296</a>)；</li> 
 <li>Micronaut Data 2.4 发布说明 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5287" target="_blank">#5287</a>)；</li> 
 <li>将 micronaut-security 升级至 2.4.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5294" target="_blank">#5294</a>)；</li> 
 <li>延迟读取流式请求的正文，直到执行过滤器之后 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5261" target="_blank">#5261</a>)；</li> 
 <li>将 GraalVM 升级至 21.1.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5292" target="_blank">#5292</a>)；</li> 
 <li>注释处理应该让具有更高优先级的访问者先处理可能的元素 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5283" target="_blank">#5283</a>)；</li> 
 <li>将 micronaut-micrometer 升级至 3.4.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5284" target="_blank">#5284</a>)；</li> 
 <li>修复 Groovy 的 InterceptorBinding 映射，添加测试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5282" target="_blank">#5282</a>)；</li> 
 <li>将 micronaut-oracle-cloud 升级至 1.3.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5280" target="_blank">#5280</a>)；</li> 
 <li>将 Netty 升级至 4.1.63 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5104" target="_blank">#5104</a>)；</li> 
 <li>在 WhatsNew 中把 HTTP 添加到 HTTPS 文档 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5276" target="_blank">#5276</a>)；</li> 
 <li>移除拦截器中 Type 注解的使用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5274" target="_blank">#5274</a>)；</li> 
 <li>将 actions/cache 从 2.1.4 升级至 2.1.5 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5267" target="_blank">#5267</a>)；</li> 
 <li>确保为重定向设置正确的 host header (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5256" target="_blank">#5256</a>)；</li> 
 <li>将 micronaut-maven-plugin 升级至 1.1.8 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5272" target="_blank">#5272</a>)；</li> 
 <li>添加 HTTP 到 HTTPS 重定向处理程序 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5258" target="_blank">#5258</a>)；</li> 
 <li>将 micronaut-flyway 升级至 3.6.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5262" target="_blank">#5262</a>)；</li> 
 <li>修复问题 5255 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5260" target="_blank">#5260</a>)；</li> 
 <li>禁用 Java 8 增量上的路由验证 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5248" target="_blank">#5248</a>)；</li> 
 <li>支持自定义验证器消息 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5202" target="_blank">#5202</a>)；</li> 
 <li>更新 types.adoc (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5220" target="_blank">#5220</a>)；</li> 
 <li>更新 websocketClient.adoc (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5245" target="_blank">#5245</a>)；</li> 
 <li>同时处理无请求状态错误的可忽略的异常 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5229" target="_blank">#5229</a>)；</li> 
 <li>将 micronaut-elasticsearch 升级到 2.3.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5232" target="_blank">#5232</a>)；</li> 
 <li>将 micronaut-servlet 升级至 2.1.3 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5228" target="_blank">#5228</a>)；</li> 
 <li>修复内部配置介绍建议中的前缀 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5214" target="_blank">#5214</a>)；</li> 
 <li>将 actions/setup-java 从 v1 升级到 v2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5235" target="_blank">#5235</a>)；</li> 
 <li>添加 NOTICE 文件，说明 UPL 下 GraalVM 的使用情况 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5231" target="_blank">#5231</a>)；</li> 
 <li>输入流支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5204" target="_blank">#5204</a>)；</li> 
 <li>将 micronaut-azure 升级至 2.2.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5225" target="_blank">#5225</a>)；</li> 
 <li>修复 kotlin 增量编译的警告 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5217" target="_blank">#5217</a>)；</li> 
 <li>build：将 Micronaut Kotlin 升级至 2.3.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5216" target="_blank">#5216</a>)；</li> 
 <li>feat(document): 更新 clientFallback.adoc (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5207" target="_blank">#5207</a>)；</li> 
 <li>将 micronaut-aws 升级至 2.6.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5205" target="_blank">#5205</a>)；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Freleases%2Ftag%2Fv2.4.3" target="_blank">https://github.com/micronaut-projects/micronaut-core/releases/tag/v2.4.3</a></p>
                                        </div>
                                      
</div>
            