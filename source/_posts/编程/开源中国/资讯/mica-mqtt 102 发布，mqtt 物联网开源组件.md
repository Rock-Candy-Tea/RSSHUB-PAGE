
---
title: 'mica-mqtt 1.0.2 发布，mqtt 物联网开源组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7329'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 12:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7329'
---

<div>   
<div class="content">
                                                                                            <p>mica-mqtt 1.0.2 已经发布，mqtt 物联网开源组件。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>文档添加集群处理步骤说明，添加遗嘱消息、保留消息的使用场景。</li> 
 <li>✨ 去除演示中的 qos2 参数，性能损耗大避免误用。</li> 
 <li>✨ 遗嘱、保留消息内部消息转发抽象。</li> 
 <li>✨ mqtt server 连接时先判断 clientId 是否存在连接关系，有则先关闭已有连接。</li> 
 <li>✨ 添加 mica-mqtt-spring-boot-example 。感谢 wsq（ <a href="https://www.oschina.net/E_wsq">@冷月宫主 </a> ）pr。</li> 
 <li>✨ mica-mqtt-spring-boot-starter 支持客户端接入和服务端优化。感谢 wsq（ <a href="https://www.oschina.net/E_wsq">@冷月宫主 </a> ）pr。</li> 
 <li>✨ mica-mqtt-spring-boot-starter 服务端支持指标收集。可对接 Prometheus + Grafana 监控。</li> 
 <li>✨ mqtt server 接受连接时，先判断该 clientId 是否存在其它连接，有则解绑并关闭其他连接。</li> 
 <li>⬆️ 升级 mica-auto 到 2.1.3 修复 ide 多模块增量编译问题。</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/596392912/mica-mqtt/releases/1.0.2">https://gitee.com/596392912/mica-mqtt/releases/1.0.2</a></p>
                                        </div>
                                      
</div>
            