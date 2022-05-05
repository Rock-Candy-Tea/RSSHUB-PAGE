
---
title: 'smart-mqtt v0.3 发布，国产开源 MQTT Broker 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4f6b5b70f6389ab07f3c9a144d20c51e277.png'
author: 开源中国
comments: false
date: Thu, 05 May 2022 08:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4f6b5b70f6389ab07f3c9a144d20c51e277.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">关于 smart-mqtt</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>smart-mqtt 是用 java 语言开发的 MQTT Broker 服务，也是 smartboot 组织下首款真正意义上面向物联网的解决方案。旨在帮助企业以较低的成本快速搭建稳定、可靠的物联网服务，助力万物互联互通。</span></p> 
<p><img height="481" src="https://oscimg.oschina.net/oscnet/up-4f6b5b70f6389ab07f3c9a144d20c51e277.png" width="750" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">产品特色</span></h1> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>国产血统：从底层通信（smart-socket）直至应用层 Broker 服务（smart-mqtt）皆为自研。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>开箱即用：零配置即可启动 MQTT Broker 服务。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>灵活扩展：通过插件机制，提供高度自由的定制化能力。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>高能低耗：运用设计和算法技巧充分发挥硬件能力。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>极致轻量：极少的外部依赖，发行包仅 3MB。</span></p> </li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">文档地址</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>筹备中...</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">开源地址</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>Gitee（主站）：</span><u>https://gitee.com/smartboot/smart-mqtt</u></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>GitHub（镜像同步）：</span><u>https://github.com/smartboot/smart-mqtt</u></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">环境依赖</span></h1> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">开发环境</span></p> 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">JDK 1.8+</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">Maven 3.x</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">IDEA</span></p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">部署环境</span></p> 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">操作系统：Linux/MacOS/Docker/K8S</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span style="color:#1a1a1a">Java：JRE/JDK 1.8+</span></p> </li> 
  </ul> </li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">本期更新</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">【新特性】</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Retain 消息内存持久化，并在客户端 CONNECT 成功后推送匹配的消息。</li> 
 <li>新增飞行窗口（Inflight Window）功能，限制同时发送Qos1和Qos2的数量，保障通信质量。</li> 
 <li>新增 MQTT Broker 和 MQTT Client 的消息重发功能。</li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">【优化】</p> 
<ul> 
 <li>重构 MQTT 消息模型设计。</li> 
 <li>改进消息内存持久化的处理逻辑。</li> 
 <li>提升并发场景下的线程安全性。</li> 
 <li>改进客户端的 subscribe 和 publish 的接口设计。</li> 
 <li>客户端正常断开连接时发送 DISCONNECT 消息。</li> 
 <li>MQTT 消息对象序列化调整为 JSON 格式。</li> 
 <li>主动拦截已断开连接的消息发送行为。</li> 
 <li>以正整数作为合法的 packetId。</li> 
 <li>补充压测的单元测试。</li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">【Bugfix】</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>修复Broker端在某些异常场景下资源释放不彻底问题。</li> 
 <li>修复CONNECT消息的合法性校验错误问题：如果客户端提供的ClientId为零字节且清理会话标志为 0，服务端必须发送返回码为 0x02的CONNACK报文响应客户端的CONNECT报文。</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">功能模块</span></h1> 
<p><img height="924" src="https://oscimg.oschina.net/oscnet/up-1f0683274fe7aa7edb254673c0c7d086e49.png" width="578" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            