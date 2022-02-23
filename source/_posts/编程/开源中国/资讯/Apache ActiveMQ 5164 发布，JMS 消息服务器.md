
---
title: 'Apache ActiveMQ 5.16.4 发布，JMS 消息服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2808'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2808'
---

<div>   
<div class="content">
                                                                                            <p>Apache 出品的开源消息总线 ActiveMQ 5.16.4 现已发布，此版本主要包括功能优化和 bug 修复：</p> 
<h2 style="margin-left:0px">修复漏洞</h2> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-5388" target="_blank">AMQ-5388</a> ] - 在 jetty.xml 中授予用户角色完全权限</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-7340" target="_blank">AMQ-7340</a> ] - 预估的消息性能下降</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8093" target="_blank">AMQ-8093</a> ] - IntrospectionSupport 的非法反射访问</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8252" target="_blank">AMQ-8252</a> ] - 在凭据无效的情况下不必要的堆栈跟踪</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8253" target="_blank">AMQ-8253</a> ] - 在无效 STOMP 版本的情况下不必要的堆栈跟踪</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8275" target="_blank">AMQ-8275</a> ] - Java 16 SSL 连接在日志中出现错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8383" target="_blank">AMQ-8383</a> ] - ActiveMQ 状态命令 - 5.16.2 版本</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8395" target="_blank">AMQ-8395</a> ] - 关于主题 SlowConsumerAdvisory 的 NPE</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8400" target="_blank">AMQ-8400</a> ] - Transaction.java 中的 ConcurrentModificationException</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8409" target="_blank">AMQ-8409</a> ] - 传入消息的标头属性中出现意外的 \\r 而不是 \r</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8425" target="_blank">AMQ-8425</a> ] - Linux 启动脚本不工作取决于 ps 命令版本</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8439" target="_blank">AMQ-8439</a> ] - 验证示例 camel.xml 在程序中集成失败</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8445" target="_blank">AMQ-8445</a> ] - 由于 SecurityException，activemq-stomp 中的几个测试失败</li> 
</ul> 
<h2 style="margin-left:0px">新功能</h2> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8372" target="_blank">AMQ-8372</a> ] - 通过 MBean 发送 TextMessage 时允许输入分隔符</li> 
</ul> 
<h2 style="margin-left:0px">改进</h2> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8053" target="_blank">AMQ-8053</a> ] - 当消息通过网络连接器时，不覆盖 JMSXUserId</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8397" target="_blank">AMQ-8397</a> ] - 将 SendDuplicateFromStoreToDLQ 标志添加到目标</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8412" target="_blank">AMQ-8412</a> ] - 发送最大消息大小时，向客户端返回格式正确的响应</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8413" target="_blank">AMQ-8413</a> ] - 支持远程代理的不同用户名和密码</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8443" target="_blank">AMQ-8443</a> ] - 修复 FailoverTransport 以尊重 ConnectionControl 重新连接</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8462" target="_blank">AMQ-8462</a> ] - 在连接关闭期间删除对 listConnectionStates 的双重调用</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8468" target="_blank">AMQ-8468</a> ] - CVE-2022-23437：Apache XercesJ xml 解析器中的无限循环</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8472" target="_blank">AMQ-8472</a> ] - 切换到 reload4j 进行日志记录</li> 
</ul> 
<h2 style="margin-left:0px">任务</h2> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-7351" target="_blank">AMQ-7351</a> ] - 更新到 Apache POM 24</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8362" target="_blank">AMQ-8362</a> ] - 将 Jenkinsfile 更新为 -fae 以进行测试</li> 
</ul> 
<h2 style="margin-left:0px">依赖升级</h2> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8358" target="_blank">AMQ-8358</a> ] - 将 xstream 升级到 1.4.18</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8359" target="_blank">AMQ-8359</a> ] - 将 slf4j 升级到 1.7.32</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8360" target="_blank">AMQ-8360</a> ] - 升级到 Apache Commons Pool 2.11.1</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8393" target="_blank">AMQ-8393</a> ] - 升级到 jackson 2.12.5</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8394" target="_blank">AMQ-8394</a> ] - 升级到 shiro 1.8.0</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8396" target="_blank">AMQ-8396</a> ] - 升级到 jaxb-basics 0.12.0</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8404" target="_blank">AMQ-8404</a> ] - 升级到 jackson 2.13.0</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8405" target="_blank">AMQ-8405</a> ] - 升级到 ASM 9.2</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8410" target="_blank">AMQ-8410</a> ] - 更新到 Guava 31.0.1</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8428" target="_blank">AMQ-8428</a> ] - 升级到 httpcore 4.4.15</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FAMQ-8467" target="_blank">AMQ-8467</a> ] - 升级到 xstream 1.4.19</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mail-archive.com%2Fannounce%40apache.org%2Fmsg07113.html" target="_blank">https://www.mail-archive.com/announce@apache.org/msg07113.html</a></p>
                                        </div>
                                      
</div>
            