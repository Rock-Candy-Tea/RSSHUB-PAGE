
---
title: 'AppWeb v8.3.0 发布，嵌入式 Web 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6049'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6049'
---

<div>   
<div class="content">
                                                                    
                                                        <p>AppWeb 8.3.0 现已发布，此版本被划分为“建议升级，但不是必须的”。Appweb 是一个嵌入式 HTTP Web 服务器，主要的设计思路是安全。这是直接集成到客户的应用和设备，便于开发和部署基于 Web 的应用程序和设备。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容：</p> 
<ul> 
 <li>修复网络非常快而 CPU 较慢的系统的内存增长问题</li> 
 <li>将 HTTP_CURRENT flag 添加到 httpServiceNetQueues，只为预先存在的预定队列提供服务</li> 
 <li>更改 cookie 解析代码以更符合规范</li> 
 <li>修复代理处理程序传输大文件的问题</li> 
 <li>将 MbedTLS 更新到版本 2.28.0</li> 
 <li>修复 OpenSSL 加密引擎构建</li> 
 <li>修复 errorDoc 对 HTTP/1 的后续请求的传播</li> 
 <li>优化管道处理和队列服务</li> 
 <li>重构 tail filter 和 http/2 过滤器的重叠部分</li> 
 <li>为 Net callbacks 添加 HTTP_NET_IO 事件。</li> 
 <li>添加缺少的 HTTP 状态代码</li> 
 <li>长度检查超大上传文件边界字符串</li> 
 <li>修复未定义主机路由名称时缺少 host header 的问题</li> 
 <li>修复上传文件在上传文件中预置 CRLF 的罕见情况</li> 
 <li>修复 proxy death handling</li> 
 <li>确保 disconnectStreams 在 HTTP/1 中立即断开套接字连接</li> 
 <li>尽可能在 httpError 中将 HTTP_ABORT 转换为 HTTP_CLOSE。</li> 
 <li>修复网络断开时的代理处理</li> 
 <li>修复丢包时传入的分块传输处理</li> 
 <li>增加代理超时默认值</li> 
 <li>修复非常慢的网络上静态文件的过早请求超时问题</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fembedthis%2Fappweb%2Freleases%2Ftag%2Fv8.3.0" target="_blank">https://github.com/embedthis/appweb/releases/tag/v8.3.0</a></p>
                                        </div>
                                      
</div>
            