
---
title: 'HttpComponents Core 5.1.2 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9745'
author: 开源中国
comments: false
date: Wed, 06 Oct 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9745'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">HttpComponents Core 5.1.2 GA<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202109.mbox%2F%253C5f8cb992355b3540d4aec38403845cc1a9479d98.camel%40apache.org%253E" target="_blank">已发布</a>，这是一个维护版本，修复了 5.1.1 发布后出现的错误，包括在处理身份传输编码的 HTTP/1.1 响应信息方面的错误。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>HTTPCLIENT-2174: URIBuilder 返回新的空列表而不是不可修改的 Collections#emptyList</li> 
 <li>HTTPCORE-684: 修复异步 SSL I/O 会话未能将流结束的事件传播到协议处理程序的错误。该错误可能导致在处理身份传输编码的 HTTP/1.1 响应信息时出现失败的情况</li> 
 <li>Bug fix: 修复异步 HTTP/1.1 服务器端协议处理程序未能正确终止身份转移编码响应的消息交换</li> 
 <li>HTTPCORE-683: 修复 I/O 会话池对主机名解析失败的不正确恢复问题</li> 
 <li>不会根据远程设置更改连接流控制窗口</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.apache.org%2Fhttpcomponents%2Fhttpcore%2FRELEASE_NOTES-5.1.x.txt" target="_blank">详情查看 release note</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">请注意，HttpCore 5.1 应该是最后一个与 Java 1.7 兼容的系列。从 5.2 开始，HttpCore 需求使用 Java 1.8+。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">HttpCore 是 HTTP/1.1 和 HTTP/2 传输组件，使用者可通过它以最小的空间构建自定义的客户端和服务器端 HTTP 服务。</span></p>
                                        </div>
                                      
</div>
            