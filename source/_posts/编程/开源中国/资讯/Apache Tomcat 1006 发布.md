
---
title: 'Apache Tomcat 10.0.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6841'
author: 开源中国
comments: false
date: Sat, 15 May 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6841'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Tomcat 10.0.x 系列的目标平台是 Jakarta EE 9。官方表示，Tomcat 10 及更高版本的用户应注意，作为从 Java EE 迁移到 Eclipse Foundation 的的一部分，从 Java EE 迁移到 Jakarta EE 的结果是所有已实现 API 的主要软件包已从 javax. 改为 jakarta.，因此部分项目会需要更改代码，以使应用程序能够从 Tomcat 9 及更低版本迁移到 Tomcat 10 及更高版本。</p> 
<p>与 10.0.5 相比，值得注意的变化包括：</p> 
<ul> 
 <li>确保正确转义 JNDIRealm 中属性值和搜索过滤器；</li> 
 <li>HandlesTypes 应该包括在字段或方法上使用指定注解类型的类；</li> 
 <li>重构 WebSocket 端点、解码器和编码器实例的创建，使其对 IoC 更加友好。现在，实例可以通过 InstanceManager 创建；</li> 
</ul> 
<p>更多详情可以查看：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftomcat.apache.org%2Ftomcat-10.0-doc%2Fchangelog.html" target="_blank">http://tomcat.apache.org/tomcat-10.0-doc/changelog.html</a></p>
                                        </div>
                                      
</div>
            