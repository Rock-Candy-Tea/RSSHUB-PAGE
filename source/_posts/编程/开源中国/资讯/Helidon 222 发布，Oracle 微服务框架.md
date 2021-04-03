
---
title: 'Helidon 2.2.2 发布，Oracle 微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4784'
author: 开源中国
comments: false
date: Sat, 03 Apr 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4784'
---

<div>   
<div class="content">
                                                                                            <p>Helidon 2.2.2 现已发布，这是一个 bug 修复版本。除了修复各种错误之外，它还包含了一个安全修复；详情可见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fissues%2F2903" target="_blank">2903</a>。Helidon 是 Oracle 开源的一个用于编写微服务的 Java 框架，这些微服务运行在由 Netty 提供支持的快速 Web 内核上。该项目的特性包括轻量、快速、支持 Microprofile、函数式编程模型与可观察性、弹性。</p> 
<p>官方建议所有 Helidon 2 用户升级至此版本。新版本具体更新内容如下：</p> 
<p><strong>兼容性</strong></p> 
<ul> 
 <li>2.2.2 与 2.2.0 兼容。</li> 
</ul> 
<p><strong>CHANGES</strong></p> 
<ul> 
 <li>WebClient：keep-alive 的小改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2882" target="_blank">2882</a></li> 
 <li>WebClient：Keep alive 默认值更改为true <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2775" target="_blank">2775</a></li> 
 <li>Security：当 CDI 注入实例时，获取 actual class <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2897" target="_blank">2897</a></li> 
 <li>MicroProfile Server：删除 standard output。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2780" target="_blank">2780</a></li> 
 <li>Metrics：避免 NaN 值在指标输出中引起问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2812" target="_blank">2812</a></li> 
 <li>Logging：修正了 Slf4j MDC context propagation 以及 null MDC 映射的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2861" target="_blank">2861</a></li> 
 <li>JAX-RS：使用 Jersey 的一个 PropertiesDelegate 的实现 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2756" target="_blank">2756</a></li> 
 <li>Fault Tolerance：新的 RequestScopeHelper 类可跨线程跟踪请求范围  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2856" target="_blank">2856</a></li> 
 <li>Dependencies：将 Netty 升级到 4.1.59.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Fpull%2F2793" target="_blank">2793</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foracle%2Fhelidon%2Freleases%2Ftag%2F2.2.2" target="_blank">https://github.com/oracle/helidon/releases/tag/2.2.2</a></p>
                                        </div>
                                      
</div>
            