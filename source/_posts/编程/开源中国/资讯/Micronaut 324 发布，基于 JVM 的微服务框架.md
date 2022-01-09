
---
title: 'Micronaut 3.2.4 发布，基于 JVM 的微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9298'
author: 开源中国
comments: false
date: Sun, 09 Jan 2022 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9298'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">Micronaut 3.2.4 已发布，主要更新内容：</span></p> 
<ul> 
 <li>升级 micronaut-security 至 3.2.1<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6704" target="_blank">#6704</a>)</li> 
 <li>删除验证模块的冗余服务提供者定义 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6703" target="_blank">#6703</a>)</li> 
 <li>升级 clientBasics.adoc<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6695" target="_blank">#6695</a>)</li> 
 <li>使用 java.util.function.Supplier，而不是直接初始化 LOGGER<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6692" target="_blank">#6692</a>)</li> 
 <li>修复部分拼写错误<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6700" target="_blank">#6700</a>)</li> 
 <li>将默认验证上下文中先前验证的消息重置为 null<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fagugan" target="_blank">@agugan</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6607" target="_blank">#6607</a>)</li> 
 <li>嵌套 pojos 上的自定义验证器在从 2.x 到 3.x 的分支上缺少合并<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6686" target="_blank">#6686</a>)</li> 
 <li>升级 link<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6685" target="_blank">#6685</a>)</li> 
 <li>升级 micronaut-flyway 至 5.0.2<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6680" target="_blank">#6680</a>)</li> 
 <li>升级 micronaut-liquibase 至 5.0.1<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6679" target="_blank">#6679</a>)</li> 
 <li>升级 micronaut-data 至 3.2.2<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6675" target="_blank">#6675</a>)</li> 
 <li>[core] 升级 3.2.x 分支的通用文件<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6603" target="_blank">#6603</a>)</li> 
 <li>build: log4j2 从 2.16.0 升级到 2.17.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6671" target="_blank">#6671</a>)</li> 
</ul> 
<p>Bugfix</p> 
<ul> 
 <li>修复巨大请求的 ignoreBodyRead 问题<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6696" target="_blank">#6696</a>)</li> 
 <li><span>修复表单属性的两次发布问题 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6707" target="_blank">#6707</a>)</li> 
 <li>修复从 AnnotationMetadataHierarchy 解析绑定的错误<span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6669" target="_blank">#6669</a>)</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Freleases%2Ftag%2Fv3.2.4" target="_blank">详情查看 release note</a>。</p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="margin-left:0; margin-right:0">Micronaut 是 Grails 框架作者打造的开源项目，也是新一代基于 JVM 的全栈微服务框架，用于构建模块化的、易于测试的微服务应用。有关 Micronaut 的特性介绍<a href="https://www.oschina.net/news/96381/micronaut-open-sourced" target="_blank">点此查看</a>。</p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            