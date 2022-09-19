
---
title: '强烈建议升级 _ mica-mqtt 2.0.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=493'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 18:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=493'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>一、简介</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 基于 </span><span><strong><span>t-io</span></strong></span><span> 实现的</span><span><strong><span>简单</span></strong></span><span>、</span><span><strong><span>低延迟</span></strong></span><span>、</span><span><strong><span>高性能</span></strong></span><span> 的 mqtt 物联网开源组件。</span><span><strong><span>mica-mqtt</span></strong></span><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
<h2 style="text-align:start"><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT client 客户端。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT server 服务端。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT 遗嘱消息。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT 保留消息。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持自定义消息（mq）处理转发实现集群。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 GraalVM 编译成本机可执行程序。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 jfinal 项目快速接入。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 Spring boot 项目快速接入。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a></span><span>。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（云端 mqtt broker）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（边缘端消息通信）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>群组类 IM</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>消息推送</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>简单、易用的 mqtt client 客户端</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>四、更新记录</span></h2> 
<h3 style="text-align:start"><span>v2.0.3 - 2022-09-18</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> 完善 ssl 方法，方便使用。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️</span><span> 依赖升级，避免依赖导致的 bug，感谢 </span><span><code>@JuneMare</code></span><span> 反馈。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v2.0.2 - 2022-09-13</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛</span><span> 彻底修复解码异常: </span><span><code>BufferUnderflowException</code></span><span>，感谢 </span><span><code>@JuneMare</code></span><span> 反馈。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v2.0.1 - 2022-09-12</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> 优化 MqttWebServer 配置。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt-example 添加华为云iot连接示例。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt-example 改为使用 tinylog。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛</span><span> 修复解码异常: </span><span><code>BufferUnderflowException</code></span><span>。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v2.0.0 - 2022-09-04</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica mqtt server 完善方法，方便使用。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> 切换到自维护的 java8 t-io，注意：升级了 t-io 部分类名变更。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、重点说明</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>自 1.3.8 最近几个版本都在</span><span><strong><span>修复 bug</span></strong></span><span>。其中包含了 mica-mqtt 和 t-io 的一些 bug，目前已经稳定，</span><span><strong><span>强烈建议升级</span></strong></span><span>。</span></p> 
<h2 style="text-align:start"><span>六、文档</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/link?target=https%3A%2F%2Fb23.tv%2FVJ8yc7v"><span>mqtt科普、mqttx、mica-mqtt的使用</span><span><strong><span>视频</span></strong></span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/example/README.md"><span>mica-mqtt 快速开始</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-client-spring-boot-starter/README.md"><span>mica-mqtt-client-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-server-spring-boot-starter/README.md"><span>mica-mqtt-server-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/jfinal-mica-mqtt-client/README.md"><span>jfinal-mica-mqtt-client 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/jfinal-mica-mqtt-server/README.md"><span>jfinal-mica-mqtt-server 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/issues/I45GO7"><span>mica-mqtt 使用常见问题汇总</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            