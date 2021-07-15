
---
title: 'Spring Framework 5.3.9 和 5.2.16 现已推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/20201115095235720.png#pic_center'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 06:56:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20201115095235720.png#pic_center'
---

<div>   
<div class="content">
                                                                    
                                                        <p>北京时间7月14日，Spring Framework推出 <code>5.3.9</code> 和 <code>5.2.16</code> 两个新版本。Spring Framework<code>5.3.9</code>包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.9" target="_blank">45 个修复和改进</a>。Spring Framework<code>5.2.16</code>包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.2.16.RELEASE" target="_blank">12 个选定的修复和改进</a>。</p> 
<p>随着越来越多的人使用Spring Boot 逐渐忽略了Spring Framework的关注，其实两者的关系密不可分，对Spring Boot 如果想要能研究得更深入，那么，就需要对Spring Framework有更足够的了解和应用。</p> 
<p><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20201115095235720.png#pic_center" referrerpolicy="no-referrer"></p> 
<h2>一、介绍Spring Framework</h2> 
<div style="text-align:start"> 
 <p><span style="color:#000000"><span style="background-color:#ffffff">Spring 使创建 Java 企业应用程序变得容易。它提供了在企业环境中使用 Java 语言所需的一切，支持 Groovy 和 Kotlin 作为 JVM 上的替代语言，并且可以根据应用程序的需要灵活地创建多种架构。从 Spring Framework 5.1 开始，Spring 需要 JDK 8+（Java SE 8+）并为 JDK 11 LTS 提供开箱即用的支持。建议将 Java SE 8 update 60 作为 Java 8 的最低补丁版本，但通常建议使用最新的补丁版本。</span></span></p> 
</div> 
<div style="text-align:start"> 
 <p><span style="color:#000000"><span style="background-color:#ffffff">Spring 支持广泛的应用场景。在大型企业中，应用程序往往存在很长时间，并且必须运行在升级周期不受开发人员控制的JDK和应用程序服务器上。其他可能作为嵌入服务器的单个 jar 运行，可能在云环境中。还有一些可能是不需要服务器的独立应用程序（例如批处理或集成工作负载）。</span></span></p> 
</div> 
<div style="text-align:start"> 
 <p><span style="color:#000000"><span style="background-color:#ffffff">Spring 是开源的。它拥有一个庞大而活跃的社区，可根据各种实际用例提供持续的反馈。这帮助 Spring 在很长一段时间内成功发展。</span></span></p> 
 <h2>二、Spring Framework 与Spring Boot的版本对应关系</h2> 
 <table cellspacing="0" style="width:962px"> 
  <thead> 
   <tr> 
    <th style="background-color:#eff3f5; vertical-align:middle">Spring boot 版本</th> 
    <th style="background-color:#eff3f5; vertical-align:middle">Spring Framework</th> 
    <th style="background-color:#eff3f5; vertical-align:middle">jdk 版本</th> 
    <th style="background-color:#eff3f5; vertical-align:middle">maven 版本</th> 
   </tr> 
  </thead> 
  <tbody> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.0.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.6.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.2.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.7.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.3.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.8.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.4.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.9.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.5.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.10.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.7.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.11.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.8.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.12.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">1.5.9.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">4.3.13.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">7</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.0.0.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.0.2.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.1.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.1.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.2+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.2.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.2.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.3+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.3.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.2.*.RELEASE</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8+</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.3+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.4.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.3.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8+</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.3+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.5.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.3.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8+</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.3+</td> 
   </tr> 
   <tr> 
    <td style="border-color:#dddddd; vertical-align:middle">2.6.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">5.3.*</td> 
    <td style="border-color:#dddddd; vertical-align:middle">8+</td> 
    <td style="border-color:#dddddd; vertical-align:middle">3.3+</td> 
   </tr> 
  </tbody> 
 </table> 
</div> 
<h2>三、主要更新内容</h2> 
<h3>5.3.9</h3> 
<h3>3.1 新的功能 </h3> 
<ul> 
 <li>配置 CommonsMultipartResolver 以支持特定的 HTTP 方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27161" target="_blank">#27161</a></li> 
 <li>允许 BeanDefinitionBuilder 使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27160" target="_blank">ResolvableType</a>设置实例供应商<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27160" target="_blank">#27160</a></li> 
 <li><code>@ResponseStatus</code>MessageSource 未解决 on handler 方法的原因<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27156" target="_blank">#27156</a></li> 
 <li>ResourceHandlerRegistry#getHandlerMapping 应该在外循环中初始化一次处理程序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27153" target="_blank">#27153</a></li> 
 <li>使用 BeanDefinitionBuilder 设置合成标志<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27141" target="_blank">#27141</a></li> 
 <li>BeanCreationException 错误消息应始终包括声明构造函数（或工厂方法）类<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27139" target="_blank">#27139</a></li> 
 <li>改进 Jetty 10 检查 JettyClientHttpResponse <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27136" target="_blank">#27136</a></li> 
 <li>Jetty10RequestUpgradeStrategy 使用旧的码头 9 类 HandshakeRFC6455 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27121" target="_blank">#27121</a></li> 
 <li>使用 Jetty 10 及其反应式客户端的 ClassNotFoundException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27112" target="_blank">#27112</a></li> 
 <li>尽可能使用 StringBuilder.append(char) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27098" target="_blank">#27098</a></li> 
 <li>考虑“wss”和“https”作为转发标头检查中的安全标志<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27097" target="_blank">#27097</a></li> 
 <li>SynchronossPartHttpMessageReader 应仅在需要时创建临时目录<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27092" target="_blank">#27092</a></li> 
 <li>在 BeanMethod 和 *Metadata 类型中实现 equals、hashCode 和 toString <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27076" target="_blank">#27076</a></li> 
 <li>删除 BeanUtils 中的日志依赖<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27070" target="_blank">#27070</a></li> 
 <li>从自动代理中排除密封接口（为了兼容 JDK 17）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27027" target="_blank">#27027</a></li> 
 <li>使用 TransactionOperator 运行事务时出现 Blockhound 错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F26955" target="_blank">#26955</a></li> 
 <li>配置 StandardServletMultipartResolver 以仅支持 multipart/form-data <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F26826" target="_blank">#26826</a></li> 
 <li>添加一种从 ThreadPoolTask​​Scheduler 设置 executeExistingDelayedTasksAfterShutdown 的方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F26719" target="_blank">#26719</a></li> 
 <li>在设置本地值之前在 ThreadPoolTask​​Executor 中应用动态更改<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F26700" target="_blank">#26700</a></li> 
</ul> 
<h3>3.2 <span style="color:#24292e"><span style="background-color:#ffffff">Bug修复</span></span></h3> 
<ul> 
 <li>JettyHttpHandlerAdapter 不知道 Server[Request|Response]Wrapper <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27146" target="_blank">#27146</a></li> 
 <li>&#123;*path&#125; 模式 (CaptureTheRestPathElement) 在<code>@PathVariable</code>路径<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27132" target="_blank">#27132 中</a>包含未记录的前导斜杠</li> 
 <li>在 jetty 10 中调用 JettyWebSocketSession.getRemoteAddress 时出现 NoSuchMethodError <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27120" target="_blank">#27120</a></li> 
 <li>CronExpression在 spring-context-5.3.8 上<em>仍然</em>被破坏<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27117" target="_blank">#27117</a></li> 
 <li>SimpleMethodMetadataReadingVisitor.Source.toString() 省略了方法参数的分隔符<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27095" target="_blank">#27095</a></li> 
 <li>DefaultPathSegment 允许改变共享的空参数映射<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27064" target="_blank">#27064</a></li> 
 <li>使用 proxyTargetClass=true 的 AOP 自动代理和介绍建议不适用于 JDK 代理目标<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27044" target="_blank">#27044</a></li> 
 <li>ServletRequestDataBinder 假定标准 servlet 多部分处理<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F26999" target="_blank">#26999</a></li> 
 <li>DataClassRowMapper 不应覆盖 Kotlin 初始化属性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F26569" target="_blank">#26569</a></li> 
</ul> 
<h3>3.3 文档</h3> 
<ul> 
 <li>将 Javadoc 添加<code>@since</code>到<code>BeanDefinitionBuilder.setSynthetic()</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27155" target="_blank">#27155</a></li> 
 <li>修复指向 Javadoc API 的链接<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27151" target="_blank">#27151</a></li> 
 <li>添加了 HandlerInterceptor 的描述<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27122" target="_blank">#27122</a></li> 
 <li>修复 core-beans.adoc 中的错字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27113" target="_blank">#27113</a></li> 
 <li>修复 BeanDefinitionDsl.kt 中的错字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27105" target="_blank">#27105</a></li> 
 <li>改进 ContentCachingRequestWrapper 的 getContentAsByteArray 方法的文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27068" target="_blank">#27068</a></li> 
 <li>修复了参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27067" target="_blank">#27067 中</a>内容协商默认设置的解释</li> 
 <li><code>@Valid*</code>在参考手册中记录任何注释都会触发验证<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27050" target="_blank">#27050</a></li> 
 <li>改进 RequestPartMethodArgumentResolver Javadoc <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27043" target="_blank">#27043</a></li> 
 <li>改进 RequestResponseBodyMethodProcessor Javadoc <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27042" target="_blank">#27042</a></li> 
 <li>澄清 ResourceBundleMessageSource 中的 baseName 不支持多个位置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27038" target="_blank">#27038</a></li> 
 <li>链接替代文档格式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F27015" target="_blank">#27015</a></li> 
</ul> 
<h3>3.4 <span style="color:#24292e"><span style="background-color:#ffffff">依赖升级</span></span></h3> 
<ul> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">适配 HtmlUnit 2.51 #27147</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 ASM 9.2 (for early Java 18 support) #27069</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Kotlin 1.5.21 #27110</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Kotlin Coroutines 1.5.1 #27157</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Mockk 1.11.0 #27109</span></span></li> 
 <li><span style="color:#24292e"><span style="background-color:#ffffff">升级至 Reactor 2020.0.9 #27158</span></span></li> 
</ul> 
<h2><span style="color:#24292e"><span style="background-color:#ffffff">四、 应用案例</span></span></h2> 
<p><a href="https://gitee.com/matevip/matecloud">MateCloud</a>是基于Spring Cloud和Spring Boot的低代码快速开发平台，底层基于Spring Framework.</p>
                                        </div>
                                      
</div>
            