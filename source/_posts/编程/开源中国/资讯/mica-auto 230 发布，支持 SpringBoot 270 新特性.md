
---
title: 'mica-auto 2.3.0 发布，支持 SpringBoot 2.7.0 新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5cd65810623da429a0aa7b29be1a7476055.png'
author: 开源中国
comments: false
date: Tue, 24 May 2022 09:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5cd65810623da429a0aa7b29be1a7476055.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><span>更新记录</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ 支持 Spring boot 2.7.0 新特性 @AutoConfiguration。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️ 升级 Spring boot 到 2.7.0</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>注意：mica-auto 并不强制依赖 Spring boot，仅仅是组合了 </span><span><code>spring-boot-configuration-processor</code></span><span>依赖，方便使用。mica-auto 2.3.0 理论上支持 Spring boot 所有版本。</span></p> 
<h2 style="text-align:start"><span>关于 Spring boot 2.7.0 @AutoConfiguration</span></h2> 
<h3 style="text-align:start"><span>1 @AutoConfiguration 注解</span></h3> 
<p><img height="868" src="https://oscimg.oschina.net/oscnet/up-5cd65810623da429a0aa7b29be1a7476055.png" width="1125" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Spring boot 2.7.0 新增 @AutoConfiguration 注解，它用来替换 @Configuration 注解，</span><span> </span><span> </span><span>我们可以看到它组合了 @Configuration（默认 proxyBeanMethods = false</span><span> </span><span> 配置类不进行代理，可节省资源另外对 GraalVM 更加友好）、@AutoConfigureAfter 和 @AutoConfigureBefore 方便使用。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>另外 Spring boot 2.7.0 开始推荐使用 </span><span><code>META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports</code></span><span> 替换 </span><span><code>spring.factories</code></span><span> 中的 </span><span><code>EnableAutoConfiguration</code></span><span> 配置。</span></p> 
<h3 style="text-align:start"><span>2 老的 spring.factories EnableAutoConfiguration 配置</span></h3> 
<p><img height="618" src="https://oscimg.oschina.net/oscnet/up-39b74611416380491fee3671f60ef742152.png" width="1125" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>3 新的 AutoConfiguration.imports 配置</span></h3> 
<p><img height="645" src="https://oscimg.oschina.net/oscnet/up-f3ab9a8cb7aae57f51aeb9458b34ea750b2.png" width="1125" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>使用 mica-auto 2.3.0 在 Spring boot 2.7.x 的配置类中如果使用 </span><span><code>@AutoConfiguration</code></span><span>注解就会自动生成到新的 AutoConfiguration.imports 配置中，如果任然使用的是老的 </span><span><code>@Configuration</code></span><span>则任然会生成到 </span><span><code>spring.factories</code></span><span>中。</span></p> 
<h2 style="text-align:start"><span>使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Spring boot starter 开发利器，自动生成 spring.factories、</span>AutoConfiguration.imports、spring-devtools.properties 配置。</p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>多模块项目中的子项目，包名不同时的自动配置（主项目不建议添加）。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>java spi 扩展自动生成配置。</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>建议关注如梦技术码云：</span><span><a href="https://gitee.com/596392912"><span>https://gitee.com/596392912</span></a></span><span> ，更多微服务核心组件值得拥有。</span></p>
                                        </div>
                                      
</div>
            