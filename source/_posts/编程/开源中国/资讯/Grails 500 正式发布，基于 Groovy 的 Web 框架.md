
---
title: 'Grails 5.0.0 正式发布，基于 Groovy 的 Web 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9477'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 06:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9477'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Grails 的开发由 Grails 基金会领导，是一个用 Groovy 编程语言构建网络应用的框架。核心框架具有很强的可扩展性，而且有许多插件可供使用，可以轻松集成附加功能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Grails 5.0.0 值得关注的变化包括：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">重要变化</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>弃用基于 "dot" 的导航</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">基于 "dot" 的 Grails 配置导航已被弃用，并将在后续版本中移除。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">需要你更新插件，以使用配置 beans<span> </span><code>@ConfigurationProperties</code><span> </span>或<span> </span><code>@Value</code>，或通过使用<span> </span><code>grailsApplication.config.getProperty('a.b.c', String)</code><span> </span>而不是<span> </span><code>grailsApplication.config.a.b.c</code><span> </span>访问配置设置。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>默认的按类型自动装配</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在以前的版本中，Grails DataService 内部的 beans 是按名称自动装配的，但在 Grails 5 中，这被改为按类型自动装配。开发者可以使用 Spring 的<span> </span><code>@Qualifier</code><span> </span>注解来按名称自动装配。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Grails Gradle Plugin</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Grails Gradle Plugin 已从 grails-core 中移出，并可能遵循独立的版本管理，因此你应该在现有的应用程序中把<span> </span><code>grailsVersion</code><span> </span>Gradle 属性与<span> </span><code>grailsGradlePluginVersion</code><span> </span>脱钩。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>移除了 Grails Gradle Publish 插件</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Grails Gradle Publish 插件使用 Bintray API 来发布工件。然而在 JFrog 关闭 Bintray 后，这就停止了工作。我们已经从新的 Grails Plugin 应用中移除这个插件。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>依赖项更新</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Groovy 3.0.7</li> 
 <li>Micronaut 3</li> 
 <li>Micronaut for Spring 4</li> 
 <li>GORM 7.1.0</li> 
 <li>Spring Framework 5.3</li> 
 <li>Spring Boot 2.5</li> 
 <li>Gradle 7.2</li> 
 <li>Spock 2.0-groovy-3.0</li> 
 <li>Grails Testing Support 2.2.0</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrails%2Fgrails-core%2Freleases%2Ftag%2Fv5.0.0" target="_blank">https://github.com/grails/grails-core/releases/tag/v5.0.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            