
---
title: 'Spring Native 0.11.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7489'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7489'
---

<div>   
<div class="content">
                                                                                            <p>Spring Native 0.11.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F12%2F22%2Fspring-native-0-11-1-available-now" target="_blank">已发布</a>，此版本主要是修复 0.11.0 中发现的问题，以及改进兼容性和优化功能。</p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">从 WebMvcHints 中删除方法反射配置</span></li> 
 <li>优化<code>@EnableJpaRepositories</code>支持</li> 
 <li><span style="background-color:#ffffff; color:#24292f">无法处理 bean 定义时提供更多上下文</span></li> 
 <li>修复 <span style="background-color:#ffffff; color:#24292f">Netty native </span><span style="background-color:#ffffff; color:#24292f">构建失败的问题</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">……</span></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.1" target="_blank">详情查看 release note</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.0" target="_blank">Spring Native 0.11.0 </a>是两周前发布的一个主要版本，主要新特性：</p> 
<ul> 
 <li>使用 GraalVM 21.3, Spring Boot 2.6 和 Spring Cloud 2021.0 作为底层应用</li> 
 <li>由于 GraalVM 不再支持 Java 8，因此 Spring Native 也不再支持它。但可使用 Java 11 版本的 GraalVM 编译大多数 Java 8 应用程序</li> 
 <li><span style="background-color:#ffffff; color:#24292f">为函数类型提供 BeanFactoryNativeConfigurationProcessor 的实现</span></li> 
 <li>提供 SPI 以排除要写入的 bean 定义</li> 
 <li>避免为 java 和原始类型创建反射条目</li> 
 <li><span style="background-color:#ffffff; color:#24292f">将日志记录添加到 BeanDefinitionRegistrar</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 NativeConfiguration 中使用 NativeConfigurationRegistry</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">添加对非 Spring Boot 测试的支持</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">恢复 Spring 集成支持</span></li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            