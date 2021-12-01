
---
title: 'Redkale 2.6.0 发布，Java 分布式微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5305'
author: 开源中国
comments: false
date: Wed, 01 Dec 2021 10:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5305'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redkale 2.6.0 发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redkale， 一个Java分布式微服务框架，1.6M的jar可以代替传统几十M的第三方。包含TCP/UDP、HTTP、RPC、依赖注入、序列化与反序列化、数据库操作、WebSocket等功能。  一方面模块高度整合，极大的简化业务开发代码，一方面暴露大量底层，方便二次框架开发。  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Java并不臃肿， 臃肿的是你自己的设计思维！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次版本更新内容：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f"> 1、【新增】FilterNode增加filter方法</span><br> <span style="background-color:#ffffff; color:#24292f">2、【新增】RestOnMessage.name的值支持*，表示参数中不带方法名</span><br> <span style="background-color:#ffffff; color:#24292f">3、【优化】【不兼容】WebSocketNodeService由包 org.redkale.service 迁移到 org.redkale.net.http</span><br> <span style="background-color:#ffffff; color:#24292f">4、【优化】EnMember、DeMember增加comment字段值</span><br> <span style="background-color:#ffffff; color:#24292f">5、【优化】优化HttpMessageClusterClient存在本地mqservice则优先调用HttpMessageLocalClient</span><br> <span style="background-color:#ffffff; color:#24292f">6、【优化】优化WebSocket.onOpen方法Future的回调处理</span><br> <span style="background-color:#ffffff; color:#24292f">7、【修复】修复DataResultSet字段byte[]与String转换的bug</span><br> <span style="background-color:#ffffff; color:#24292f">8、【修复】修复application.xml没有executor节点时不会自动创建的bug</span><br> <span style="background-color:#ffffff; color:#24292f">9、【修复】修复生成Attribute时ClassLoader无法加载动态Type的问题</span><br> <span style="background-color:#ffffff; color:#24292f">10、【修复】修复JsonDynEncoder没有判断JavaBean嵌套自身类型的bug</span><br> <span style="background-color:#ffffff; color:#24292f">11、【修复】修复HttpMessageResponse遗漏HttpResponse部分finish系列方法未重载的bug</span></p>
                                        </div>
                                      
</div>
            