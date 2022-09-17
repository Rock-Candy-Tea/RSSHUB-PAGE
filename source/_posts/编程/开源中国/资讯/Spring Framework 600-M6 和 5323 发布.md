
---
title: 'Spring Framework 6.0.0-M6 和 5.3.23 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5921'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5921'
---

<div>   
<div class="content">
                                                                                            <p>Spring Framework 6.0.0-M6 和 5.3.23 已发布。</p> 
<p>Spring Framework<code>5.3.23</code>包含 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.23" target="_blank">32 项修复和改进</a>，建议所有在生产环境使用的用户都进行升级。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.23" target="_blank"><strong>5.3.23 主要变化</strong></a></p> 
<ul> 
 <li>引入 AnnotationUtils.isSynthesizedAnnotation(Annotation) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29054" target="_blank">#29054</a></li> 
 <li>在 AbstractGenericWebContextLoader 中引入 createContext() 工厂方法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28983" target="_blank">#28983</a></li> 
 <li>在 CollectionFactory.createCollection() 中支持 TreeSet collection 类型而不使用反射 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F28949" target="_blank">#28949</a></li> 
 <li>当 RequestEntity.getUrl() 抛出 UnsupportedOperationException 异常时进行记录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28930" target="_blank">#28930</a></li> 
 <li>弃用 NestedIOException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28929" target="_blank">#28929</a></li> 
 <li>将 WebSocketConnectionManager 中的 isConnected() 设置为公开 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F28785" target="_blank">#28785</a></li> 
 <li>将 STOMP RECEIPT 帧中的 header 公开给已注册的回调 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F28715" target="_blank">#28715</a></li> 
 <li>使 WebClientException 可序列化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28321" target="_blank">#28321</a></li> 
 <li>将依赖项<span style="color:#24292f"> Reactor 升级到 2020.0.23 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29129" target="_blank">#29129</a></li> 
 <li>……</li> 
</ul> 
<p>Spring Framework<code>6.0.0-M6</code>包含 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv6.0.0-M6" target="_blank">123 </a>项特定于 6.0 分支的附加修复和改进。这个里程碑囊口了目前大部分 AOT 工作，团队称已经为发布 RC 做好准备。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv6.0.0-M6" target="_blank"><strong>6.0.0-M6 主要变化</strong></a></p> 
<ul> 
 <li>添加 HandshakeWebSocketService runtime 提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29146" target="_blank">#29146</a></li> 
 <li>在 ReflectionHintsPredicates 中添加 className 变体用于检查字段和方法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29143" target="_blank">#29143</a></li> 
 <li>在原生镜像中2将<code>hibernate.bytecode.provider</code>设置为<code>none</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29140" target="_blank">#29140</a></li> 
 <li>为 org.hibernate.SessionFactory 和 org.hibernate.Session 添加代理提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29138" target="_blank">#29138</a></li> 
 <li>修复 DefaultPersistenceUnitManager.determineDefaultPersistenceUnitRootUrl 无法解析原生镜像中的根 url 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29137" target="_blank">#29137</a></li> 
 <li>使 FieldHint 适应最新的 GraalVM 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F29130" target="_blank">#29130</a></li> 
 <li>弃用 StreamUtils.emptyInput() <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29125" target="_blank">#29125</a></li> 
 <li>当无法生成值的代码时，改进异常消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29118" target="_blank">#29118</a></li> 
 <li>弃用对 theme 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F29114" target="_blank">#29114</a></li> 
 <li>为<code>HtmlCharacterEntityReferences.properties</code>添加资源提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29112" target="_blank">#29112</a></li> 
 <li>在 TestContext 框架中引入 AotTestAttributes 机制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29100" target="_blank">#29100</a></li> 
 <li>支持从 ClassPathResource#getPath 返回不带斜杠的绝对路径 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29099" target="_blank">#29099</a></li> 
 <li>为通过 PersistenceManagedTypes 公开的类型注册运行时提示  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29096" target="_blank">#29096</a></li> 
 <li>删除不推荐使用的 SynthesizedAnnotation 接口 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F29092" target="_blank">#29092</a></li> 
 <li>添加对提供 JNI 运行时提示的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F29085" target="_blank">#29085</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F09%2F15%2Fspring-framework-6-0-0-m6-and-5-3-23-available-now" target="_blank">发布公告</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            