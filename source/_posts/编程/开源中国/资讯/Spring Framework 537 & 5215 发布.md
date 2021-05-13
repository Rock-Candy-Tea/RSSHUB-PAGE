
---
title: 'Spring Framework 5.3.7 & 5.2.15 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5173'
author: 开源中国
comments: false
date: Thu, 13 May 2021 06:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5173'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Framework 5.3.7 和 5.2.15 现已发布，分别包含 45 项与 9 项修复和改进。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>5.3.7 
  <ul> 
   <li>spring-context-indexer 不支持 Java 记录</li> 
   <li>让 spring-expression 更容易被重新打包，以嵌入到第三方 JAR 中</li> 
   <li>忽略 CorsConfiguration 原始模式中的尾部斜杠</li> 
   <li>使用 RSocketRequester 处理底层 RSocketClient</li> 
   <li>添加 PreFlightRequestWebFilter</li> 
   <li>避免重用 PropertyComparator时的内存泄漏</li> 
   <li>在 MySQLMaxValueIncrementer 中支持 MySQL 安全更新模式</li> 
   <li>HttpStatus.resolve 每次调用分配一次 HttpStatus.values()</li> 
   <li>在 PatternMatchUtils 中使用 String.startsWith() 而不是 String.substring()</li> 
   <li>在 executorconfigurationsupport.IniTialize 中减小日志级别</li> 
  </ul> </li> 
 <li>5.2.15 
  <ul> 
   <li>确保多部分临时目录不冲突</li> 
   <li>在 Windows 上使用 NIO Path 属性运行 SpringBootTest 时，日志中会出现 InvalidPathException </li> 
   <li>Spring AOP 不应将 UndeclaredThrowableException 应用于 Kotlin 方法中的已检查异常</li> 
   <li>修复通过构造函数注入时的网络参数解析</li> 
   <li>修复 Router DSL 中的 Kotlin 过滤参数错误</li> 
   <li>修复 AbstractBrokerRegistration 的构造函数中的检查不正确的问题</li> 
   <li>修复 @ModelAttribute(binding=false) 不适合 WebFlux 的问题</li> 
   <li>从 WebClient 删除剩余的 Javadoc</li> 
   <li>升级到 Reactor Dysprosium-SR20</li> 
  </ul> </li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F04%2F13%2Fspring-framework-5-3-6-and-5-2-14-available-now" target="_blank">更新公告</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F05%2F11%2Fspring-framework-5-3-7-and-5-2-15-available-now" target="_blank">。</a></p>
                                        </div>
                                      
</div>
            