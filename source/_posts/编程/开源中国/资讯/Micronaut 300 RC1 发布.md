
---
title: 'Micronaut 3.0.0 RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4203'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4203'
---

<div>   
<div class="content">
                                                                                            <p>Micronaut 是 Grails 框架作者打造的开源项目，也是新一代基于 JVM 的全栈微服务框架，用于构建模块化的、易于测试的微服务应用。有关 Micronaut 的特性介绍<a href="https://www.oschina.net/news/96381/micronaut-open-sourced">点此查看</a>。</p> 
<p>Micronaut 3.0.0 RC1 发布，更新内容如下：</p> 
<h3>变化:</h3> 
<ul> 
 <li>将 New Relic Micrometer 注册表加入 BOM (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5960" target="_blank">#5960</a>)</li> 
 <li>将 micronaut-gcp 升级至 4.0.0-RC2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5959" target="_blank">#5959</a>)</li> 
 <li><code>AnnotationMetadataHierarchy</code> 改进 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5953" target="_blank">#5953</a>)</li> 
 <li>将 micronaut-views 升级至 3.0.0-M2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5958" target="_blank">#5958</a>)</li> 
 <li>改变总是将错误序列化为列表默认值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5935" target="_blank">#5935</a>)</li> 
 <li>为 GroovyClassElement 实现构造元素查询 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5957" target="_blank">#5957</a>)</li> 
 <li>在服务器上使用来自 ssl 处理程序的 ChannelPipelineCustomizer.HANDLER_SSL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5955" target="_blank">#5955</a>)</li> 
 <li>将 micronaut-liquibase 升级至 4.0.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5952" target="_blank">#5952</a>)</li> 
 <li>将 micronaut-flyway 升级至 4.1.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5950" target="_blank">#5950</a>)</li> 
 <li>修复 GraalVM 警告 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5949" target="_blank">#5949</a>)</li> 
 <li>修复 Open Rewrite 功能链接中的名称 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5943" target="_blank">#5943</a>)</li> 
 <li>将 mysql-connector-java 从 8.0.23 升级至 8.0.26(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5934" target="_blank">#5934</a>)</li> 
 <li>添加改进的 BeanBuilder API  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5917" target="_blank">#5917</a>)</li> 
 <li>在 BeanElements 被写入之前增加对其访问的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5906" target="_blank">#5906</a>)</li> 
 <li>允许从 ClassElement 访问 PackageElement (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5899" target="_blank">#5899</a>)</li> 
 <li>……</li> 
</ul> 
<h3>功能：</h3> 
<ul> 
 <li>支持从访问者那里向注解添加构造型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5926" target="_blank">#5926</a>)</li> 
</ul> 
<h3><strong>错误修复：</strong></h3> 
<ul> 
 <li>修复 remapper 和 transformers 之间不一致的行为 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5915" target="_blank">#5915</a>)</li> 
 <li>修复了同时具有 Value/Property 和 Inject 的 Java 字段注入 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5912" target="_blank">#5912</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Freleases%2Ftag%2Fv3.0.0-RC1" target="_blank">https://github.com/micronaut-projects/micronaut-core/releases/tag/v3.0.0-RC1</a></p>
                                        </div>
                                      
</div>
            