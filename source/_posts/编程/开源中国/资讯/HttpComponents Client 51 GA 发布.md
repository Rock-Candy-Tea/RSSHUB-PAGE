
---
title: 'HttpComponents Client 5.1 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7339'
author: 开源中国
comments: false
date: Thu, 13 May 2021 08:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7339'
---

<div>   
<div class="content">
                                                                    
                                                        <p>HttpComponents Client 5.1 已正式 GA。需要注意的是，5.1 是与 Java 1.7 兼容的最后的发行版本，从 5.2 开始，HttpClient 将需要 Java 1.8 支持。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>修复缓存后端生成的响应对象缺少原始内容编码的问题</li> 
 <li>修正了异步请求重试执行拦截器对未检查异常的处理方式</li> 
 <li>异步客户端将支持延迟的请求重新执行命令</li> 
 <li>修复执行器的访问线程安全问题</li> 
 <li>当没有 dNSName 时，与 CN 匹配</li> 
 <li>修复了 HC Fluent 的抢占式身份验证问题</li> 
 <li>清理 H2 连接验证代码</li> 
 <li>使 IOReactor 异常回调可配置</li> 
 <li>如果重试间隔超过了响应超时，HttpClient 将不重试请求</li> 
 <li>如果实体为空，在 Response 的处置过程中修复 NPE</li> 
 <li>阻止连接管理器在不活动超过 2s 后默认验证连接的行为</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202105.mbox%2F%253C4ebfdc31ffdb4fbb619a039d21ca62d3df059e4d.camel%40apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            