
---
title: 'Spring Boot 2.4.9 & 2.5.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=541'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=541'
---

<div>   
<div class="content">
                                                                                            <p>Spring Boot 2.4.9 和 2.5.3 现已发布，分别包括 35 个和 58 个错误修复、文档改进以及依赖项升级。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>2.4.9 
  <ul> 
   <li>将 Gson 设置为首选映射器会破坏返回 JSON 字符串的控制器方法</li> 
   <li>使用 spring.config.import=configtree:xxxx 时从 /actuator/configprops 端点抛出异常</li> 
   <li>当集群状态为失败时，Redis 健康指标报告 Redis 已启动</li> 
   <li>如果不存在，带有模式的可选文件搜索位置会引发异常 </li> 
   <li>启用延迟初始化后，Spring Session JDBC 不起作用</li> 
   <li>使用 Spring Batch 和 JDBC 时应用程序无法启动，并且启用了延迟初始化</li> 
   <li>DurationStyle.SIMPLE.print 不能与 ChronoUnit.MICROS 一起正常工作</li> 
   <li>使用 Devtools 实时重新加载不再连接</li> 
   <li>YamlPropertySourceLoader 可能不会使用正确的 ClassLoader 来检查 SnakeYAML 是否存在</li> 
   <li>工作目录中名为“config”的文件导致 IllegalStateException</li> 
   <li>记录自动配置的 Jetty 指标</li> 
   <li>改进 @DefaultValue 的 javadoc</li> 
  </ul> </li> 
 <li>2.5.3 
  <ul> 
   <li>尝试从未知数据源类型派生数据源时，DataSourceBuilder 抛出 UnsupportedDataSourcePropertyException</li> 
   <li>DatabaseInitializerDetector 和 DependsOnDatabaseInitializationDetector 实现可能会使用错误的 ClassLoader 进行实例化</li> 
   <li>Prometheus 的 Pushgateway 的依赖管理不完整</li> 
   <li>图层配置 XSD 不可用</li> 
   <li>AbstractDataSourceInitializers 未被检测为数据库初始值设定项</li> 
   <li>使用 Devtools 实时重新加载时不再连接</li> 
   <li>DurationStyle.SIMPLE.print 不能与 ChronoUnit.MICROS 一起正常工作</li> 
   <li>从 2.5.1 开始，当一个 SpringLiquibase bean 被配置为依赖另一个时会创建一个循环引用</li> 
   <li>配置属性元数据具有错误的 spring.netty.leak-detection 默认值</li> 
   <li>“无法确定数据库的类型，因为 ConnectionFactory 不支持选项”错误消息没有提供足够的详细信息</li> 
   <li>@SpyBean 在用于监视 Spring Data Repository 时不起作用</li> 
  </ul> </li> 
</ul> 
<p>详情请查看更新公告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F22%2Fspring-boot-2-4-9-is-now-available%3F__cf_chl_captcha_tk__%3Dpmd_e5e2fd9a4bc1b7688fbae9ee6df90f5de83bab23-1626992209-0-gqNtZGzNAvijcnBszQ1i" target="_blank">2.4.9</a> 与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F22%2Fspring-boot-2-5-3-is-now-available" target="_blank">2.5.3</a>。</p>
                                        </div>
                                      
</div>
            