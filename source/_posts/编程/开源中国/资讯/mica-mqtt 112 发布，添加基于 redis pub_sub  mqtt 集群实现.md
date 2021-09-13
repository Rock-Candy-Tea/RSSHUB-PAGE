
---
title: 'mica-mqtt 1.1.2 发布，添加基于 redis pub_sub  mqtt 集群实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1f62e89ed8dfc8a086ccb1c252117a8cf69.jpg'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 10:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1f62e89ed8dfc8a086ccb1c252117a8cf69.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div class="lake-content" typography="traditional"> 
  <h2 id="6ddda5c2" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">一、简介</span></h2> 
  <p class="ne-p" id="u01dfeac3" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="uaed5b764" style="margin: 0; padding: 0; min-height: 24px"><strong><span class="ne-text">mica-mqtt</span></strong><span class="ne-text"> 基于 </span><strong><span class="ne-text">t-io</span></strong><span class="ne-text"> 实现的</span><strong><span class="ne-text">简单</span></strong><span class="ne-text">、</span><strong><span class="ne-text">低延迟</span></strong><span class="ne-text">、</span><strong><span class="ne-text">高性能</span></strong><span class="ne-text"> 的 mqtt 物联网开源组件。</span><strong><span class="ne-text">使用详见 mica-mqtt gitee 源码</span></strong><span class="ne-text"> </span><a class="ne-link" data-href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-example" href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-example" target="_blank"><span class="ne-text">mica-mqtt-example 模块</span></a><span class="ne-text">。</span></p> 
  <p class="ne-p" id="uae35c9cc" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="ub963a249" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">在多个朋友咨询 mica-mqtt 集群怎么实现之后，添加了一个 mica-mqtt-broker 模块演示了基于 redis pub/sub 实现集群实现。</span></p> 
  <p class="ne-p" id="u75a0d20c" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="362c1545" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">二、功能</span></h2> 
  <p class="ne-p" id="u4bbef53a" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="ucdf3079a"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></li> 
   <li id="ua7f6240e"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 websocket mqtt 子协议（支持 mqtt.js）。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u4c60cf5d"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 http rest api，</span><a class="ne-link" data-href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md" href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md" target="_blank"><span class="ne-text">http api 文档详见</span></a><span class="ne-text">。</span></li> 
   <li id="u7dbb055b"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 MQTT client 客户端。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u84a1f94c"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 MQTT server 服务端。</span></li> 
   <li id="uae5653af"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 MQTT 遗嘱消息。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u13451008"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 MQTT 保留消息。</span></li> 
   <li id="u86f3c605"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持自定义消息（mq）处理转发实现集群。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="ud595347c"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">MQTT 客户端 阿里云 mqtt 连接 demo。</span></li> 
   <li id="u46c84f20"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 GraalVM 编译成本机可执行程序。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u2448c012"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></li> 
   <li id="u6abc8b41"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></li> 
  </ul> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u596131bb"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">✅</span><span class="ne-text">基于 redis pub/sub 实现集群，详见 </span><a class="ne-link" data-href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker" href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker" target="_blank"><span class="ne-text">mica-mqtt-broker 模块</span></a><span class="ne-text">。</span></li> 
  </ul> 
  <p class="ne-p" id="ud8cd9e4e" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="5a121f0b" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">三、待办</span></h2> 
  <p class="ne-p" id="u0e9f6bd7" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <ul class="ne-tl" style="margin: 0; padding-left: 23px; padding: 0; list-style: none"> 
   <li id="u8131e852"><span class="ne-tli-symbol" style="margin: 3px 0.5ex; vertical-align: middle">🔲</span><span class="ne-text">优化处理 mqtt session，以及支持部分 mqtt v5.0 新特性。</span></li> 
  </ul> 
  <p class="ne-p" id="u75364020" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="4e6304af" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">四、更新记录</span></h2> 
  <p class="ne-p" id="u467bf5b6" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="ucb15c844"><span class="ne-text">✨ 添加 mica-mqtt-broker 模块，基于 redis pub/sub 实现 mqtt 集群。</span></li> 
   <li id="u26521312"><span class="ne-text">✨ mica-mqtt-broker 基于 redis 实现客户端状态存储。</span></li> 
  </ul> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="u2fd9db65"><span class="ne-text">✨ mica-mqtt-broker 基于 redis 实现遗嘱、保留消息存储。</span></li> 
   <li id="u546fb7f1"><span class="ne-text">✨ mqtt-server http api 调整订阅和取消订阅，方便集群处理。</span></li> 
  </ul> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="ue46fabd8"><span class="ne-text">✨ mica-mqtt-spring-boot-example 添加 mqtt 和 http api 认证示例。</span></li> 
   <li id="uf15e0893"><span class="ne-text">✨ 添加 mqtt 5 所有 ReasonCode。</span></li> 
  </ul> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="u9c359e0f"><span class="ne-text">✨ 优化解码 PacketNeededLength 计算。</span></li> 
   <li id="u94e7f0bd"><span class="ne-text">🐛 修复遗嘱消息，添加消息类型。</span></li> 
  </ul> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="u99433aa9"><span class="ne-text">🐛 修复 mqtt-server 保留消息匹配规则。</span></li> 
  </ul> 
  <p class="ne-p" id="u8103c2d0" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="986976fc" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">五、Spring boot 快速接入</span></h2> 
  <p class="ne-p" id="u0dbd18ef" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="004cbd2e" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">5.1 添加依赖</span></h3> 
  <p class="ne-p" id="u7a52a521" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <pre class="ne-codeblock" data-language="xml" id="d80713c0" style="border: 1px solid #e8e8e8; border-radius: 2px; background: #f9f9f9; padding: 16px; font-size: 13px; color: #595959"><dependency>
    <groupId>net.dreamlu</groupId>
    <artifactId>mica-mqtt-spring-boot-starter</artifactId>
    <version>1.1.2</version>
</dependency></pre> 
  <p class="ne-p" id="u73cc31ba" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="ab19321c" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">5.2 服务端配置示例</span></h3> 
  <p class="ne-p" id="u3e8097d7" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <pre class="ne-codeblock" data-language="yaml" id="2230059f" style="border: 1px solid #e8e8e8; border-radius: 2px; background: #f9f9f9; padding: 16px; font-size: 13px; color: #595959">mqtt:
  server:
    enabled: true               # 是否开启，默认：true
    ip: 127.0.0.1               # 服务端 ip 默认：127.0.0.1
    port: 5883                  # 端口，默认：1883
    name: Mica-Mqtt-Server      # 名称，默认：Mica-Mqtt-Server
    buffer-allocator: HEAP      # 堆内存和堆外内存，默认：堆内存
    heartbeat-timeout: 120000   # 心跳超时，单位毫秒，默认: 1000 * 120
    read-buffer-size: 8092      # 接收数据的 buffer size，默认：8092
    max-bytes-in-message: 8092  # 消息解析最大 bytes 长度，默认：8092
    debug: true                 # 如果开启 prometheus 指标收集建议关闭
    websocket-enable: true      # 开启 websocket 子协议，默认开启
    websocket-port: 8083        # websocket 端口，默认：8083</pre> 
  <p class="ne-p" id="u724a17e2" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="960e4706" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">5.3 服务端可实现接口（注册成 Spring Bean 即可）</span></h3> 
  <table class="ne-table" id="6b6bf7ce" style="table-layout: fixed; border-collapse: collapse; border: 1px solid #d9d9d9; width: 750px"> 
   <tbody> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ud8db239b" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">接口</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u409da3a7" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">是否必须</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u07813c71" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">说明</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u11bc3483" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IMqttServerAuthHandler</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ue8150995" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">是</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u998d30cc" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">用于客户端认证</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ud3484bcc" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IMqttMessageListener</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u422f5761" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">是</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ub0e8e224" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">消息监听</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u0371b550" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IMqttConnectStatusListener</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u9e0ec4c8" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">是</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u966f6baf" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">连接状态监听</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ud1331036" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IMqttSessionManager</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u9bcc09e9" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">否</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u2d04e16c" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">session 管理</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u0bd871a9" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IMqttMessageStore</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u54385cdb" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">集群是，单机否</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ud5d626d1" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">遗嘱和保留消息存储</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u976cb550" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">AbstractMqttMessageDispatcher</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="uf891c59e" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">集群是，单机否</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u2b3a4b6e" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">消息转发，（遗嘱、保留消息转发）</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="ud1546346" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">IpStatListener</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u55a54682" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">否</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="250"> <p class="ne-p" id="u4d047431" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">t-io ip 状态监听</span></p> </td> 
    </tr> 
   </tbody> 
  </table> 
  <p class="ne-p" id="u02e707d3" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="cdd05ad3" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">5.4 Prometheus + Grafana 监控对接</span></h3> 
  <p class="ne-p" id="ud7386e08" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="u58ef30b7" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">得益于 </span><strong><span class="ne-text">t-io</span></strong><span class="ne-text"> 良好的设计，监控指标直接对接的 </span><strong><span class="ne-text">t-iostat</span></strong><span class="ne-text">，目前支持下列指标，后期会不断完善。</span></p> 
  <table class="ne-table" id="d7d0695f" style="table-layout: fixed; border-collapse: collapse; border: 1px solid #d9d9d9; width: 750px"> 
   <tbody> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u98d88965" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">支持得指标</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u7f2dc9fd" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">说明</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ub7651cec" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_connections_accepted</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u457b508e" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">共接受过连接数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u0739a675" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_connections_closed</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ud450efaf" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">关闭过的连接数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ue1ef330c" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_connections_size</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ud37bea1c" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">当前连接数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u4d5a5e1a" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_handled_packets</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u59a5302d" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已处理消息数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ua130c447" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_handled_bytes</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u5e7de975" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已处理消息字节数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u7ea73e1a" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_received_packets</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u3224cc9e" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已接收消息数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u6b2f3dd6" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_received_bytes</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ue7524da5" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已处理消息字节数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u37dec75f" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_send_packets</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="u4e30a917" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已发送消息数</span></p> </td> 
    </tr> 
    <tr style="height: 33px"> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ubf5eb62d" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">mqtt_messages_send_bytes</span></p> </td> 
     <td style="border: 1px solid #d9d9d9" width="375"> <p class="ne-p" id="ubc1a40da" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">已发送消息字节数</span></p> </td> 
    </tr> 
   </tbody> 
  </table> 
  <p class="ne-p" id="u368226be" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="ub6a36f5c" style="margin: 0; padding: 0; min-height: 24px"><img alt src="https://oscimg.oschina.net/oscnet/up-1f62e89ed8dfc8a086ccb1c252117a8cf69.jpg" style="width: 752px; height: 766px;" referrerpolicy="no-referrer"></p> 
  <p class="ne-p" id="ud65c30c8" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="ua41026a6" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">关于 </span><strong><span class="ne-text">mica-mqtt-spring-boot-starter</span></strong><span class="ne-text"> 更多请查看文档：</span><a class="ne-link" data-href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter" href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter" target="_blank"><span class="ne-text">https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter</span></a></p> 
  <p class="ne-p" id="ufce3f042" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="c0fcf8af" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">六、普通 java 项目接入</span></h2> 
  <p class="ne-p" id="u778c2aa2" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="00a93394" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">6.1 maven 依赖</span></h3> 
  <p class="ne-p" id="u3cd2952a" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <pre class="ne-codeblock" data-language="xml" id="e0c13653" style="border: 1px solid #e8e8e8; border-radius: 2px; background: #f9f9f9; padding: 16px; font-size: 13px; color: #595959"> <dependency>
   <groupId>net.dreamlu</groupId>
   <artifactId>mica-mqtt-core</artifactId>
   <version>1.1.2</version>
 </dependency></pre> 
  <p class="ne-p" id="u3c13c77f" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="a8d8c13f" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">6.2 mica-mqtt 客户端</span></h3> 
  <p class="ne-p" id="ud4f096b9" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <pre class="ne-codeblock" data-language="java" id="6fa0d77a" style="border: 1px solid #e8e8e8; border-radius: 2px; background: #f9f9f9; padding: 16px; font-size: 13px; color: #595959"> // 初始化 mqtt 客户端
 MqttClient client = MqttClient.create()
     .ip("127.0.0.1")
     .port(1883)                     // 默认：1883
     .username("admin")
     .password("123456")
     .version(MqttVersion.MQTT_5)    // 默认：3_1_1
     .clientId("xxxxxx")             // 默认：MICA-MQTT- 前缀和 36进制的纳秒数
     .connect();                     // 连接
 
     // 消息订阅，同类方法 subxxx
     client.subQos0("/test/#", (topic, payload) -> &#123;
         logger.info(topic + '\t' + ByteBufferUtil.toString(payload));
     &#125;);
     // 取消订阅
     client.unSubscribe("/test/#");
 
     // 发送消息
     client.publish("/test/client", ByteBuffer.wrap("mica最牛皮".getBytes(StandardCharsets.UTF_8)));
 
     // 断开连接
     client.disconnect();
     // 重连
     client.reconnect();
     // 停止
     client.stop();</pre> 
  <p class="ne-p" id="ud2fe4ce7" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h3 id="49de213a" style="font-size: 20; line-height: 28px; margin: 7px 0"><span class="ne-text">6.3 mica-mqtt 服务端</span></h3> 
  <p class="ne-p" id="u67084eb2" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <pre class="ne-codeblock" data-language="java" id="01a3c4ad" style="border: 1px solid #e8e8e8; border-radius: 2px; background: #f9f9f9; padding: 16px; font-size: 13px; color: #595959"> // 注意：为了能接受更多链接（降低内存），请添加 jvm 参数 -Xss129k
 MqttServer mqttServer = MqttServer.create()
     // 默认：127.0.0.1
     .ip("127.0.0.1")
     // 默认：1883
     .port(1883)
     // 默认为： 8092（mqtt 默认最大消息大小），为了降低内存可以减小小此参数，如果消息过大 t-io 会尝试解析多次（建议根据实际业务情况而定）
     .readBufferSize(512)
     // 自定义认证
     .authHandler((clientId, userName, password) -> true)
     // 消息监听
     .messageListener((clientId, topic, mqttQoS, payload) -> &#123;
         logger.info("clientId:&#123;&#125; topic:&#123;&#125; mqttQoS:&#123;&#125; message:&#123;&#125;", clientId, topic, mqttQoS, ByteBufferUtil.toString(payload));
     &#125;)
     .debug() // 开启 t-io debug 信息日志
     .start();
 
 // 发送给某个客户端
 mqttServer.publish("clientId","/test/123", ByteBuffer.wrap("mica最牛皮".getBytes()));
 
 // 发送给所有在线监听这个 topic 的客户端
 mqttServer.publishAll("/test/123", ByteBuffer.wrap("mica最牛皮".getBytes()));
 
 // 停止服务
 mqttServer.stop();</pre> 
  <p class="ne-p" id="u6dfebbf3" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <h2 id="a1b4e980" style="font-size: 24px; line-height: 32px; margin: 7px 0"><span class="ne-text">七、集群演示</span></h2> 
  <p class="ne-p" id="ub674d674" style="margin: 0; padding: 0; min-height: 24px"> </p> 
  <p class="ne-p" id="u2147d098" style="margin: 0; padding: 0; min-height: 24px"><img alt src="https://oscimg.oschina.net/oscnet/up-1d4f9559daac5ea55de8a8859abd834422d.gif" style="width: 720px; height: 405px;" referrerpolicy="no-referrer"></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            