
---
title: 'Kitex v0.1.3 发布，新功能更加稳定可靠'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5214'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 17:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5214'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Kitex 是一个 <span style="background-color:#ffffff; color:#333333">Golang 微服务 RPC 框架，具有</span><strong style="color:#333333">高性能</strong><span style="background-color:#ffffff; color:#333333">、</span><strong style="color:#333333">强可扩展</strong><span style="background-color:#ffffff; color:#333333">的特点，在字节内部已广泛使用。如今越来越多的微服务选择使用 Golang，如果对微服务性能有要求，又希望定制扩展融入自己的治理体系，Kitex 会是一个不错的选择。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">Kitex v0.1.3 版本已经发布，此版本更新内容包括：</span></p> 
<h2 style="text-align:left">功能优化</h2> 
<ul> 
 <li>JSON 泛化调用场景，向服务端传递 Base 信息，从而服务端可获取 Caller 等信息</li> 
</ul> 
<h2 style="text-align:left">Bugfix</h2> 
<ul> 
 <li>修复 streaming 的 metric 上报（server侧）丢失 method 信息的问题</li> 
 <li>修复 JSON 和 HTTP 泛化中 base64 和 binary 的不兼容改动</li> 
 <li>修复 gRPC 流控相关的问题，该问题会导致 client 侧出现持续超时</li> 
</ul> 
<h2 style="text-align:left">CI</h2> 
<ul> 
 <li>增加场景测试</li> 
</ul> 
<h2 style="text-align:left">Chore</h2> 
<ul> 
 <li>更新了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fblob%2Fdevelop%2FROADMAP.md" target="_blank">ROADMAP</a></li> 
</ul>
                                        </div>
                                      
</div>
            