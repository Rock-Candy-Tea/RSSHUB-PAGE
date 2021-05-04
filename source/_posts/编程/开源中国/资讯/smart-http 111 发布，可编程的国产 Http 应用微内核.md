
---
title: 'smart-http 1.1.1 发布，可编程的国产 Http 应用微内核'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1355'
author: 开源中国
comments: false
date: Tue, 04 May 2021 08:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1355'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">smart-http 是一款可编程的 Http 应用微内核，用户可根据自身需求进行 </span><span style="color:#ffffff"><span style="background-color:#e67e22"> </span><strong><span style="background-color:#e67e22">Server </span> </strong></span><span style="background-color:#ffffff; color:#333333">或 </span><span style="color:#ffffff"><span style="background-color:#e67e22"> </span><strong><span style="background-color:#e67e22">Client </span> </strong></span><span style="background-color:#ffffff; color:#333333">的应用开发。</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">你可以基于它开发 HTTP 代理服务器、网关、静态服务器、http  client 工具、性能压测工具等。smart-http 依旧延续着作者一贯秉持的极简、易用、高性能风格，只提供高性能的运行能力和易用的接口设计。把更多的可能性交给开发者，由那些富有创造力的 Java 开发者打造更优秀的 Http 作品。</span></p> 
<p style="text-align:left"><strong>更新内容</strong></p> 
<ol> 
 <li>重构附件模型 <span style="color:#000000">Attachment。</span></li> 
 <li>服务端 
  <ol> 
   <li>优化：移除 Header Value 缓存。</li> 
   <li>优化：移除 URI Query 缓存。</li> 
   <li>优化：调整 Http Method 的缓存区域。</li> 
   <li>优化：调整 Http Protocol 的缓存区域。</li> 
   <li>优化：支持 body 长度为 0 的 Post 提交方式。</li> 
   <li>优化：重构 Http 响应的 Header 输出逻辑。</li> 
   <li>优化：移除 Host 的强制校验，允许客户端 Http 请求不包含 Host。</li> 
   <li>优化：重构 HttpBootstrap 接口设计。</li> 
   <li>新特性：新增服务端的 Basic 认证组件。</li> 
   <li>新特性：WebSocketRequest 支持存放附件对象。</li> 
   <li>bugfix：修复半包情况下解析 URI 失败的问题。</li> 
  </ol> </li> 
 <li>客户端 
  <ol> 
   <li>新特性：支持为 Request 设置 Header。</li> 
   <li>新特性： Post 支持 application/x-www-form-urlencoded 表单提交。</li> 
   <li>优化：客户端断链时释放所有响应监听。</li> 
   <li>优化：移除 Header Value 缓存。</li> 
  </ol> </li> 
</ol> 
<p><strong>最后</strong></p> 
<p>基于 smart-http 实现的首个国产开源 servlet3.1 容器：<a href="https://gitee.com/smartboot/smart-servlet">smart-servlet</a> 将在近期发布新版本，敬请关注。</p>
                                        </div>
                                      
</div>
            