
---
title: 'Spring Boot Admin 2.6.3 发布，Spring Boot 应用程序的管理 UI'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9527'
author: 开源中国
comments: false
date: Sun, 27 Mar 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9527'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Boot Admin 是一个用于管理 Spring Boot 应用程序的管理界面，Spring Boot Admin 2.6.3 正式发布，该版本中的变化包括：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2Fa307b36afb516ab57e6ec46cb516a7994200feea" target="_blank">a307b36a</a> - 在 <code>customBlockingClientInBlockingEnvironment</code> 中切换到 <code>WebApplicationContextRunner</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F81eb97bca46797b72a0b02bb20a456e8693131f7" target="_blank">81eb97bc</a> - 允许在阻塞或 Reactive 的环境中覆盖注册客户端 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F2004" target="_blank">#2004</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F6920683cf655fe43c73fcf1906dca6a8a46342f9" target="_blank">6920683c</a> - chore(deps): 更新依赖 com.puppycrawl.tools:checkstyle 至 v9.3 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1978" target="_blank">#1978</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F7b19876ea7f60840188f60f6e21d26054906c3cd" target="_blank">7b19876e</a> - chore(deps): 将 spring boot 升级到 2.6.4，将 spring cloud 升级到 2021.0.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1998" target="_blank">#1998</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F17ab1aabd7aa08aa0490fb0b6a2c27a582e25fd0" target="_blank">17ab1aab</a> - 修复日志过滤 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1995" target="_blank">#1995</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F6292a4b3c329e85f5f5e562aead650789f96dad7" target="_blank">6292a4b3</a> - 修复格式化问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2Fdcdc83abddb84b7c0dde551311e990c292bf35d1" target="_blank">dcdc83ab</a> - fix(deps): 更新依赖 axios 到 v0.26.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1994" target="_blank">#1994</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F786b01e81bc56e827db862c2b5bba6a5034d291e" target="_blank">786b01e8</a> - <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fissues%2F1934" target="_blank">#1934</a> - 更新西班牙语翻译 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1976" target="_blank">#1976</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F01b09c55ab2b026b91075080651274dc74da03c7" target="_blank">01b09c55</a> - chore(ApplicationRegistry): 为 getStatus 添加缺失的测试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1970" target="_blank">#1970</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F50d702596eb3328dd9c75175425624588606dc72" target="_blank">50d70259</a> - chore(deps): 更新 storybook monorepo 至 v6.4.14 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1968" target="_blank">#1968</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2F6db8eba844d0ab0fe556e6e0822896b4b700334e" target="_blank">6db8eba8</a> - chore(CI): 更新到 windows-latest (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fpull%2F1969" target="_blank">#1969</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Fcommit%2Fc351087a483153c76a9ed06d2994ad2aa31e9561" target="_blank">c351087a</a> - 升级版本至 2.6.3-SNAPSHOT</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin%2Freleases%2Ftag%2F2.6.3" target="_blank">https://github.com/codecentric/spring-boot-admin/releases/tag/2.6.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            