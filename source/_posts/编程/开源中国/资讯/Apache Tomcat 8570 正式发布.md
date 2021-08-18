
---
title: 'Apache Tomcat 8.5.70 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=208'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=208'
---

<div>   
<div class="content">
                                                                                            <p>Apache Tomcat 8.5.70 现已发布。Apache Tomcat 8 是 Java Servlet、JavaServer Pages、Java Unified Expression Language、Java WebSocket 和 Java Authentication Service Provider Interface for Containers 技术的一个开源实现软件。本次更新包括一些错误修复和新功能。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>发生未捕获的 NamingException 时始终关闭连接以避免连接锁定</li> 
 <li>更正了 65397 修复中的回归，如果符号链接目标的规范路径短于创建符号链接的目录的规范路径，则可能会触发 StringIndexOutOfBoundsException</li> 
 <li>重构 CorsFilter 以使其更易于扩展</li> 
 <li>为避免不必要的缓存重新验证，在设置添加 CacheControl: private 的 HTTP 标头时不会添加 HTTP Expires 标头</li> 
 <li>更正 HTTP/2 连接流控制管理中的错误，这意味着连接可能会停止等待已经到达的连接流控制窗口更新。发生这种情况时，该连接上任何试图写入的流都将超时</li> 
 <li>修复可能导致新请求延迟的竞争条件。新请求可以排队等待现有请求完成处理，而不是线程池创建新线程来处理新请求</li> 
 <li>更正了之前版本中引入的回归，以减少为流发送的小型 HTTP/2 窗口更新的数量。逻辑错误意味着没有刷新连接的小窗口更新，这意味着连接流窗口可能不会像理想的那样快速更新</li> 
 <li>改进了相关翻译，包括中文、法语、日语和韩语。</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253C782df79e-3b59-239e-2c10-8d4b80989cfb%40apache.org%253E" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            