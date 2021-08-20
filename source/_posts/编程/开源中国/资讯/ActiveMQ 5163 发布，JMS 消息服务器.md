
---
title: 'ActiveMQ 5.16.3 发布，JMS 消息服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8936'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 06:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8936'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ActiveMQ 5.16.3 现已发布，此版本主要包括功能优化和 bug 修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>bug 修复 
  <ul> 
   <li>由于异常而死锁关闭连接</li> 
   <li>ActiveMQ WebConsole 不适用于带有 Jackson 2.10.x 的 Karaf</li> 
   <li>VirtualSelectorCacheBrokerPlugin 抛出误报异常</li> 
   <li>STOMP ProtocolConverter 错误应包括客户端 IP 信息</li> 
   <li>由 NIOSSSLTransport 中的 serviceRead() 同步引起的死锁</li> 
   <li> org.apache.activemq.transport.tcp.TcpTransport.run() 尝试从关闭的流中读取</li> 
   <li>改进和对齐 Karaf 功能中的版本以避免级联刷新</li> 
   <li>SubQueueSelectorCacheBrokerPlugin 抛出无法读取持久选择器缓存的错误</li> 
   <li>虚拟目的地消费者咨询消息无意中重播给所有现有的咨询消费者</li> 
   <li>使用 posix 处理汇编中的长文件路径</li> 
  </ul> </li> 
 <li>功能优化 
  <ul> 
   <li>在 Karaf 功能中扩展 Camel 版本范围以避免刷新</li> 
   <li>XmlMessageRenderer 存在 XStream 反序列化的风险</li> 
   <li>ActiveMQMessage.getStringProperty() 应该交换 equals 方法调用对象</li> 
  </ul> </li> 
 <li>依赖项升级 
  <ul> 
   <li>升级到 Jackson 2.12.3</li> 
   <li>升级到 Jetty 9.4.40.v20210413</li> 
   <li>升级到 xstream 1.4.17</li> 
   <li>升级到 xbean 4.20</li> 
   <li>升级到 Jetty 9.4.41.v20210516</li> 
   <li>升级到 commons-io 2.10.0</li> 
   <li>升级到 Jetty 9.4.42.v20210604</li> 
   <li>将 com.rometools/rome 更新到 1.16.0</li> 
   <li>将 Jackson 更新到 2.12.4</li> 
   <li>将 commons-io 更新到 2.11.0</li> 
   <li>将 Tomcat 更新到 9.0.48</li> 
   <li>将 Jetty 更新至 9.4.43.v20210629</li> 
   <li>将 slf4j 更新到 1.7.31</li> 
   <li>将 commons-pool2 更新到 2.10.0</li> 
   <li>删除对 smack(x) 的引用</li> 
   <li>升级到 Camel 2.25.4</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253CCAB8EV3QPM4FK_awdFWM-Vi%3DKsdDfFVr%2BKkr9QvHrcG6Tcx2EqQ%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            