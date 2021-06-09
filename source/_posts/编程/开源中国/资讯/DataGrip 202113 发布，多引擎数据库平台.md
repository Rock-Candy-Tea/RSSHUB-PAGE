
---
title: 'DataGrip 2021.1.3 发布，多引擎数据库平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eefed1e409c4052d31b4432eaa64b07a278.png'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 07:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eefed1e409c4052d31b4432eaa64b07a278.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>DataGrip 2021.1.3 现已发布，这是 DataGrip 2021.1 的第三个错误修复版本。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>处于安全方面的考虑，Java 放弃了对 TLSv1 和 TLSv1.1 协议的使用。这会在连接到只接受这些协议的旧服务器出现问题。作为修复，DataGrip 现在提供了明确打开这些协议的能力，不过用户需要记住，这样做会导致一些漏洞问题</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-eefed1e409c4052d31b4432eaa64b07a278.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>即使数据库支持 TLSv1.2 和 TLSv1.3 协议，连接到 MySQL 也可能出现问题。由于服务器端的错误，驱动程序禁用了对这些版本的 TLSv1.2 和 TLSv1.3 支持。用户可以尝试启用它们。但如果服务器返回一个 "bad handshake" 的错误，请禁用这些版本</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b0d2f271da6ba6086664abedd39634d0a91.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>代码完成现在可以在修改表中工作，即使案例不匹配</li> 
 <li>[SQL Server] 生成的 DDL 中不包含扩展属性</li> 
 <li>[Oracle] Introspection 与版本 9i 兼容</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fdatagrip%2F2021%2F06%2F08%2Fdatagrip-2012-1-3%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            