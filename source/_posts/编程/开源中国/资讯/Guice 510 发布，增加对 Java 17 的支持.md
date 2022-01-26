
---
title: 'Guice 5.1.0 发布，增加对 Java 17 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6587'
author: 开源中国
comments: false
date: Wed, 26 Jan 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6587'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Guice 5.1.0 发布了， Guice 是 Google 开发的轻量级依赖注入框架，目标是使开发和调试更容易，更快速。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Guice 核心</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加了对 Java 17 的支持，更新了 asm 版本并修复了不安全类定义<strong>。</strong></li> 
 <li>支持 TYPE_USE 类型的 @Nullable 注解。</li> 
 <li>改进了多重绑定，以避免不必要的链接绑定。</li> 
 <li>添加了用于访问 SPI  <code>InterceptorBindings</code><span> </span> 的 API。</li> 
 <li>删除了<span> </span><code>guice_include_stack_traces</code><span> </span>标志的 COMPLETE 选项。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>AssistedInject</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了 JDK17+ 私有查找行为。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Dagger Adapter</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>如有必要，在 DaggerAdapter 中实例化模块。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Servlet</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了 UriEncoder 中解释和剥离数字前缀的错误。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguice%2Fwiki%2FGuice510" target="_blank">https://github.com/google/guice/wiki/Guice510</a></p>
                                        </div>
                                      
</div>
            