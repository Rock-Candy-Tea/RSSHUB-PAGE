
---
title: 'mica-mqtt 1.3.2 发布，重构 topic 匹配添加 topic 校验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5011'
author: 开源中国
comments: false
date: Tue, 10 May 2022 08:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5011'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><span>mica-mqtt 1.3.2 发布，重构 topic 匹配规则</span></p> 
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
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></p> </li> 
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
<h3 style="text-align:start"><span>v1.3.2 - 2022-05-09</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt 订阅、发布时添加 topicFilter、topicName 校验。</span></p> </li> 
</ul> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt-broker 默认开启 http 和 basic auth。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 添加服务端共享订阅接口，方便开源之夏学生参与。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 添加 IMqttSessionListener。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server publish 保留消息存储。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 统一 http 响应模型、优化 http 请求判断。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 优化 MqttHttpRoutes，添加获取所有路由的方法。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 完善 Result 和 http api。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server http api 添加 endpoints 列表接口。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 添加同步连接 connectSync 方法。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 优化 bean 依赖，减少循环依赖可能性。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 重构 mqtt topic 匹配规则，提升性能减少内存占用，修复 gitee </span><span><a href="https://gitee.com/596392912/mica-mqtt/issues/I56BTC"><span>#I56BTC:topic 匹配问题</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️ spring boot、mica 版本升级</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、使用文档和示例</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/example/README.md"><span>mica-mqtt 快速开始</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-client-spring-boot-starter/README.md"><span>mica-mqtt-client-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-server-spring-boot-starter/README.md"><span>mica-mqtt-server-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><a href="https://gitee.com/596392912/mica-mqtt/issues/I45GO7"><span>mica-mqtt 使用中常见问题汇总</span></a></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            