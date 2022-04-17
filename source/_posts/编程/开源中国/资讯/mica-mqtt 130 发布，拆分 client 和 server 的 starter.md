
---
title: 'mica-mqtt 1.3.0 发布，拆分 client 和 server 的 starter'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=433'
author: 开源中国
comments: false
date: Sun, 17 Apr 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=433'
---

<div>   
<div class="content">
                                                                                            <h2><span>一、简介</span></h2> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 基于 </span><span><strong><span>t-io</span></strong><span> 实现的</span><span><strong><span>简单</span></strong><span>、</span><span><strong><span>低延迟</span></strong><span>、</span><span><strong><span>高性能</span></strong><span> 的 mqtt 物联网开源组件。</span></span></span></span></span></span></span></p> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></span></span></p> 
<h2><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a><span>。</span></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT client 客户端。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT server 服务端。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 遗嘱消息。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 保留消息。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持自定义消息（mq）处理转发实现集群。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 GraalVM 编译成本机可执行程序。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a><span>。</span></span></span></p> </li> 
</ul> 
<h2><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（云端 mqtt broker）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（边缘端消息通信）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>群组类 IM</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>消息推送</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>简单、易用的 mqtt client 客户端</span></span></p> </li> 
</ul> 
<h2><span>四、更新记录</span></h2> 
<h3><span>v1.3.0 - 2022-04-17</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt mqtt-server 简化，默认多设备可以直接互相订阅和处理消息。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt server、client 添加 tioConfigCustomize 方法，方便更大程度的自定义 TioConfig。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ 拆分 mica-mqtt-client-spring-boot-starter 和 mica-mqtt-server-spring-boot-starter gitee #I4OTC5</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-client-spring-boot-example 添加重连动态更新 clientId、username、password 示例。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt server 添加根据踢出指定 clientId 的 http api 接口。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt server IMqttConnectStatusListener api 调整，添加 username 字段。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt server IMqttMessageListener 不再强制要求实现。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ 使用 netty IntObjectHashMap 优化默认 session 存储。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ 添加 github action，用于提交后自动构建 SNAPSHOT 版本。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ 示例项目拆分到 example 目录，mica-mqtt client、server starter 拆分到 starter 目录。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>⬆️ 依赖升级.</span></span></p> </li> 
</ul> 
<h3><span>重点说明</span></h3> 
<p style="margin-left:.8em; margin-right:.8em"><span><span>此版本拆分出 mica-mqtt-client-spring-boot-starter 和 mica-mqtt-server-spring-boot-starter。</span></span></p> 
<p style="margin-left:.8em; margin-right:.8em"><span><span>mica-mqtt-client-spring-boot-starter 排除了非必要的依赖（包括 fastjson），如果有用到请自行添加依赖。</span></span></p> 
<h2><span>五、使用文档和示例</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/starter/mica-mqtt-client-spring-boot-starter">mica-mqtt-client-spring-boot-starter 使用文档</a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><a href="https://gitee.com/596392912/mica-mqtt/tree/master/starter/mica-mqtt-server-spring-boot-starter">mica-mqtt-server-spring-boot-starter 使用文档</a></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本记录</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            