
---
title: 'Apache Tomcat 9.0.46 & 8.5.66 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=956'
author: 开源中国
comments: false
date: Mon, 17 May 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=956'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Tomcat 9.0.46 和 8.5.66 现已发布，这两个版本均包含一些 Bug 修复和功能更新。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>9.0.46 & 8.5.66 
  <ul> 
   <li>确保正确转义 JNDIRealm 中属性值和搜索过滤器</li> 
   <li>HandlesTypes 应该包括在字段或方法上使用指定注解类型的类</li> 
   <li>重构 WebSocket 端点、解码器和编码器实例的创建，使其对 IoC 更加友好。现在，实例可以通过 InstanceManager 创建</li> 
   <li>使用 UnboundID LDAP SDK for Java 扩大 JNDIRealm 单元测试的覆盖面</li> 
   <li>在 RemoteIpValve 的 MBean 描述符文件中添加缺失的属性</li> 
   <li>当为一个具有无效请求行的 HTTP 请求生成错误信息时，确保所有可用的数据都包含在错误信息中</li> 
   <li>恢复了可选的HTTP功能，允许 LF 被视为请求行和 HTTP 头文件行的结束符，以及标准的 CRLF。此前，作为 CVE-2020-1935 修复的一个副作用，该行为已被移除</li> 
   <li>审查用于从 JSP 和标签中生成 Java 源代码的代码，并删除发现的不必要的代码</li> 
  </ul> </li> 
 <li>9.0.46 
  <ul> 
   <li>允许使用带有标志的监听器和默认的 HTTP/1.1 协议创建 APR 连接器。</li> 
   <li>在 Jakarta API JARs 的清单中手动创建 OSGi Require-Capability 部分，而不是通过 aQute.bnd.annotation.spi.ServiceConsumer 注解，因为这将引发 API JARs 下游消费者的 TCK 失败</li> 
   <li>更新 OWB 模块到 Apache OpenWebBeans 2.0.22</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容，请分别查看 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftomcat.apache.org%2Ftomcat-9.0-doc%2Fchangelog.html" target="_blank">9.0.46</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftomcat.apache.org%2Ftomcat-8.5-doc%2Fchangelog.html" target="_blank">8.5.66</a> 的更新公告。</p>
                                        </div>
                                      
</div>
            