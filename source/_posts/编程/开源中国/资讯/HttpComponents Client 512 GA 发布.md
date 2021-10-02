
---
title: 'HttpComponents Client 5.1.2 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2513'
author: 开源中国
comments: false
date: Sat, 02 Oct 2021 08:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2513'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">HttpComponents Client 5.1.2 已正式 GA。需要注意的是，5.1.x 是与 Java 1.7 兼容的最后的发行版本，从 5.2 开始，HttpClient 将需要 Java 1.8 支持。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>URIBuilder 返回一个新的空列表而不是不可修改的集合</li> 
 <li>修复异步 SSL I/O 会话未能将流结束的事件传播到协议处理程序的问题。这可能导致在处理身份传输编码的HTTP/1.1响应信息时失败</li> 
 <li>错误修正：异步 HTTP/1.1 服务器端协议处理程序不能正确终止消息与身份转移编码响应的消息交换</li> 
 <li>修正了 I/O 会话池对主机名解析失败的不正确恢复</li> 
 <li>不再根据远程设置更改连接流控制窗口</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.apache.org%2Fhttpcomponents%2Fhttpcore%2FRELEASE_NOTES-5.1.x.txt" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            