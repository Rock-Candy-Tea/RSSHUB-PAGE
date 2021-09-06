
---
title: 'mica-mqtt 1.1.1 发布，mqtt 物联网开源组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5432'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 08:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5432'
---

<div>   
<div class="content">
                                                                                            <p>mica-mqtt 1.1.1 已经发布，mqtt 物联网开源组件。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>mqtt-server 优化连接关闭日志。</li> 
 <li>mqtt-server 优化订阅，相同 topicFilter 订阅对 qos 判断。</li> 
 <li>mqtt-server 监听器添加 try catch，避免因业务问题导致连接断开。</li> 
 <li>mqtt-server 优化 topicFilters 校验。</li> 
 <li>mqtt-client 优化订阅 reasonCodes 判断。</li> 
 <li>mqtt-client 监听器添加 try catch，避免因业务问题导致连接断开。</li> 
 <li>mqtt-client 添加 session 有效期。</li> 
 <li>代码优化，减少 codacy 上的问题。</li> 
 <li>mqtt-server 修复心跳时间问题。</li> 
 <li>修复 mqtt-server 多个订阅同时匹配时消息重复的问题。</li> 
 <li>mqtt-client 优化连接处理的逻辑，mqtt 连接之后再订阅。</li> 
 <li>修复 MqttProperties 潜在的一个空指针。</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/596392912/mica-mqtt/releases/1.1.1">https://gitee.com/596392912/mica-mqtt/releases/1.1.1</a></p>
                                        </div>
                                      
</div>
            