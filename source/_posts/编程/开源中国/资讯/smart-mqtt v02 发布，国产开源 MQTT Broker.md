
---
title: 'smart-mqtt v0.2 发布，国产开源 MQTT Broker'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ad661460c2369ec191334df31f97ef12b2c.png'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 10:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ad661460c2369ec191334df31f97ef12b2c.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">关于 smart-mqtt</strong></h1> 
 <p style="text-align:left"><span style="color:#333333">smart-mqtt 是用 java 语言开发的 MQTT Broker 服务，也是 smartboot 组织下首款真正意义上面向物联网的解决方案。旨在帮助企业以较低的成本快速搭建稳定、可靠的物联网服务，助力万物互联互通。</span></p> 
 <p><img height="481" src="https://oscimg.oschina.net/oscnet/up-ad661460c2369ec191334df31f97ef12b2c.png" width="750" referrerpolicy="no-referrer"></p> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">产品特色</strong></h1> 
 <ul style="list-style-type:disc"> 
  <li> <p style="text-align:left"><span style="color:#333333">国产血统：从底层通信（smart-socket）直至应用层 Broker 服务（smart-mqtt）皆为自研。</span></p> </li> 
  <li> <p style="text-align:left"><span style="color:#333333">开箱即用：零配置即可启动 MQTT Broker 服务。</span></p> </li> 
  <li> <p style="text-align:left"><span style="color:#333333">灵活扩展：通过插件机制，提供高度自由的定制化能力。</span></p> </li> 
  <li> <p style="text-align:left"><span style="color:#333333">高能低耗：运用设计和算法技巧充分发挥硬件能力。</span></p> </li> 
  <li> <p style="text-align:left"><span style="color:#333333">极致轻量：极少的外部依赖，发行包仅 3MB。</span></p> </li> 
 </ul> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">文档地址</strong></h1> 
 <p style="text-align:left"><span style="color:#333333">筹备中...</span></p> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">开源地址</strong></h1> 
 <p style="text-align:left"><span style="color:#333333">Gitee（主站）：</span><a href="https://gitee.com/smartboot/smart-mqtt"><u>https://gitee.com/smartboot/smart-mqtt</u></a></p> 
 <p style="text-align:left"><span style="color:#333333">GitHub（镜像同步）：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsmartboot%2Fsmart-mqtt" target="_blank"><u>https://github.com/smartboot/smart-mqtt</u></a></p> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">环境依赖</strong></h1> 
 <ul> 
  <li><span style="color:#1a1a1a">开发环境</span> 
   <ul> 
    <li><span style="color:#1a1a1a">JDK 1.8+</span></li> 
    <li><span style="color:#1a1a1a">Maven 3.x</span></li> 
    <li><span style="color:#1a1a1a">IDEA</span></li> 
   </ul> </li> 
  <li><span style="color:#1a1a1a">部署环境</span> 
   <ul> 
    <li><span style="color:#1a1a1a">操作系统：Linux/MacOS/Docker/K8S</span></li> 
    <li><span style="color:#1a1a1a">Java：JRE/JDK 1.8+</span></li> 
   </ul> </li> 
 </ul> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">本期更新</strong></h1> 
 <ol> 
  <li>优化客户端ping消息：发送了 PINGREQ 报文之后，如果在合理的时间内仍没有收到 PINGRESP 报文，则关闭到服务端的网络连接。</li> 
  <li>优化Connect消息监听：网络连接建立后，如果服务端在合理的时间内没有收到 CONNECT 报文，服务端应该关闭这个连接。</li> 
  <li>优化 Connect ACK 消息监听：如果客户端在合理的时间内没有收到服务端的 CONNACK 报文，客户端应该关闭网络连接。</li> 
  <li>优化报文标识符的生成策略，防止同一标识符在同时刻被复用。</li> 
  <li>内存持久化会话状态。</li> 
  <li>重构Qos1和Qos2的回调处理机制。</li> 
  <li>bugfix:修复unsuback报文标识符取值不正确问题</li> 
  <li>bugfix:修复 broker 推送消息至subscriber时继承了publisher消息质量的问题。</li> 
  <li>其他一些代码细节优化</li> 
 </ol> 
 <h1 style="text-align:left"><strong style="color:#1a1a1a">功能模块</strong></h1> 
 <p><img height="826" src="https://oscimg.oschina.net/oscnet/up-4c80aa0b4321f238a038e6f1ed7f5bb75dc.png" width="614" referrerpolicy="no-referrer">​​​​​​​</p> 
</div>
                                        </div>
                                      
</div>
            