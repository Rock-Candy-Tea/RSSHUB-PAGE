
---
title: 'Spring Framework 发布 5.3.11 和 5.2.18 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/20201115095235720.png#pic_center'
author: 开源中国
comments: false
date: Sat, 16 Oct 2021 04:31:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20201115095235720.png#pic_center'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、发布说明</h2> 
<p><span style="background-color:#ffffff; color:#333333">北京时间10月15日，Spring Framework推出<span> </span></span><code>5.3.11</code><span style="background-color:#ffffff; color:#333333"><span> </span>和<span> </span></span><code>5.2.18</code><span style="background-color:#ffffff; color:#333333"><span> </span>两个新版本。Spring Framework</span><code>5.3.11</code><span style="background-color:#ffffff; color:#333333">包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.11" target="_blank">32</a></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.11" target="_blank"> 个修复和改进</a><span style="background-color:#ffffff; color:#333333">。Spring Framework</span><code>5.2.18</code><span style="background-color:#ffffff; color:#333333">包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.2.18.RELEASE" target="_blank">10</a></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.2.18.RELEASE" target="_blank">个选定的修复和改进</a><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">随着越来越多的人使用Spring Boot 逐渐忽略了Spring Framework的关注，其实两者的关系密不可分，对Spring Boot 如果想要能研究得更深入，那么，就需要对Spring Framework有更足够的了解和应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20201115095235720.png#pic_center" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">二、介绍Spring Framework</h2> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><span style="background-color:#ffffff">Spring 使创建 Java 企业应用程序变得容易。它提供了在企业环境中使用 Java 语言所需的一切，支持 Groovy 和 Kotlin 作为 JVM 上的替代语言，并且可以根据应用程序的需要灵活地创建多种架构。从 Spring Framework 5.1 开始，Spring 需要 JDK 8+（Java SE 8+）并为 JDK 11 LTS 提供开箱即用的支持。建议将 Java SE 8 update 60 作为 Java 8 的最低补丁版本，但通常建议使用最新的补丁版本。</span></span></p> 
</div> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><span style="background-color:#ffffff">Spring 支持广泛的应用场景。在大型企业中，应用程序往往存在很长时间，并且必须运行在升级周期不受开发人员控制的JDK和应用程序服务器上。其他可能作为嵌入服务器的单个 jar 运行，可能在云环境中。还有一些可能是不需要服务器的独立应用程序（例如批处理或集成工作负载）。</span></span></p> 
</div> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><span style="background-color:#ffffff">Spring 是开源的。它拥有一个庞大而活跃的社区，可根据各种实际用例提供持续的反馈。这帮助 Spring 在很长一段时间内成功发展。</span></span></p> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">三、Spring Framework 与Spring Boot的版本对应关系</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:962px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th style="vertical-align:middle">Spring boot 版本</th> 
   <th style="vertical-align:middle">Spring Framework</th> 
   <th style="vertical-align:middle">jdk 版本</th> 
   <th style="vertical-align:middle">maven 版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.0.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.6.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.2.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.7.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.3.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.8.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.4.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.9.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.5.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.10.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.7.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.11.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.8.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.12.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">1.5.9.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">4.3.13.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.0.0.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.0.2.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.1.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.1.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.2+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.2.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.2.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.3+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.3.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.2.*.RELEASE</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8+</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.3+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.4.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.3.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8+</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.3+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.5.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.3.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8+</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.3+</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">2.6.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">5.3.*</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">8+</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:middle">3.3+</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">四、主要更新内容</h2> 
<p>以下列举了5.3.11版本的更新内容，5.2.18请自行查看官网</p> 
<h3>4.1 新特性</h3> 
<ul> 
 <li>增强 DefaultResponseErrorHandler 以允许记录完整的错误响应正文<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27552" target="_blank">#27552</a></li> 
 <li>在 CookieAssertions 失败消息中包含正确的关键字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27550" target="_blank">#27550</a></li> 
 <li>在 ByteArrayResource.hashCode() 中使用 Arrays.hashCode() <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27544" target="_blank">#27544</a></li> 
 <li>通过系统属性允许默认的 CacheAwareContextLoaderDelegate 配置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27540" target="_blank">#</a> 27540</li> 
 <li>直接调用 bean 派生的 (Auto)Closeable.close() 方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27504" target="_blank">#27504</a></li> 
 <li>JDK 9+ 的 JNDI API 防御性参考（可选<code>java.naming</code>模块）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27483" target="_blank">#27483</a></li> 
 <li>当消费者任务被拒绝时 DefaultMessageListenerContainer 不会记录错误/警告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27451" target="_blank">#27451</a></li> 
 <li>在 externallyManaged RootBeanDefinition 属性上提供访问器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27449" target="_blank">#27449</a></li> 
 <li>允许在<code>CglibAopProxy</code>via <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27439" target="_blank">#27439 中</a>避免类验证<code>ProxyFactory</code></li> 
 <li>添加对非公共记录声明的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27437" target="_blank">#27437</a></li> 
 <li>为格式错误的 HTTP 响应发出 WebClientResponseException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27262" target="_blank">#27262</a></li> 
 <li>如果当前连接的自动提交设置为 false，则 DatabasePopulatorUtils.execute 应该提交<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27008" target="_blank">#27008</a></li> 
</ul> 
<h3>4.2 BUG修复</h3> 
<ul> 
 <li>CronTrigger 使用 new Date() 而不是上下文的时钟<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27546" target="_blank">#27546</a></li> 
 <li>在 AbstractFileResolvingResource.isReadable() 下载巨大的 jars 以检查组件长度时 con.getContentLengthLong() 的性能影响<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27541" target="_blank">#27541</a></li> 
 <li>ResourceUrlEncodingFilter 对 HttpServletResponse#encodeURL 的性能影响<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27538" target="_blank">#27538</a></li> 
 <li>UriTemplateRequestEntity 不会覆盖 hashCode() 和 equals() <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27531" target="_blank">#27531</a></li> 
 <li>DataBufferUtils.write 丢失上下文<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27517" target="_blank">#27517</a></li> 
 <li>避免在 <cache:annotation-driven /> 中重复注册 JCacheOperationSource bean <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27499" target="_blank">#27499</a></li> 
 <li>使用 Java 17 生成代理失败，并显示“无法调用“Object.getClass()”，因为“cause”为空” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27490" target="_blank">#27490</a></li> 
 <li>MediaType.sortBySpecificityAndQuality 抛出 java.lang.IllegalArgumentException：比较方法违反其一般约定<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27488" target="_blank">#27488</a></li> 
 <li>读取 SSE 响应时删除前导空格<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27473" target="_blank">#27473</a></li> 
 <li>RegEx 中的非转义<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27467" target="_blank">右</a>花括号导致 Android 上的初始化错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27467" target="_blank">#27467</a></li> 
 <li>ConcurrentReferenceHashMap 的 entrySet 违反了 Map 契约<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27454" target="_blank">#27454</a></li> 
 <li>避免在 StandardBeanExpressionResolver 中提前确定 ConversionService <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27446" target="_blank">#27446</a></li> 
 <li>Spring Framework >= 5.3.8 由于 InputStream 优化，ASM ClassReader 无法解析类文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27429" target="_blank">#27429</a></li> 
 <li>StringUtils.collectionToDelimitedString(?) 当集合包含 null 时失败并出现 NullPointerException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27419" target="_blank">#27419</a></li> 
 <li>Spring HATEOAS 在 WebFlux 中使用 Kotlin 协程和 ResponseEntity 导致 406 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27292" target="_blank">#27292</a></li> 
</ul> 
<h3>4.3 文档</h3> 
<ul> 
 <li>删除关于缺少缓存 API 的评论。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27501" target="_blank">#27501</a></li> 
</ul> 
<h3>4.4 依赖升级</h3> 
<ul> 
 <li>Upgrade to JUnit 5.8.1<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27450" target="_blank">#27450</a></li> 
 <li>Upgrade to Reactor 2020.0.12<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27527" target="_blank">#27527</a></li> 
 <li>Upgrade to SmallRye Mutiny 1.1.1<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27555" target="_blank">#27555</a></li> 
</ul> 
<p>详细请点击官网地址查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F10%2F14%2Fspring-framework-5-3-11-and-5-2-18-available-now" target="_blank">https://spring.io/blog/2021/10/14/spring-framework-5-3-11-and-5-2-18-available-now</a></p>
                                        </div>
                                      
</div>
            