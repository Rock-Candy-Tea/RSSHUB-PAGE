
---
title: 'smqtt 1.1.0 正式发布：高性能、开箱即用的 MQTT 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202110/14093857_WLY7.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 08:41:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202110/14093857_WLY7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">SMQTT 基于 Netty 开发，底层采用 Reactor 3 反应堆模型，支持单机、集群和容器化部署，具备低延迟、高吞吐量，支持百万 TCP 连接，同时支持多种协议交互、规则引擎、Grafana监控、系统事件，是一款非常优秀的消息中间件！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">smqtt 目前拥有的功能如下：</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="架构图" src="https://static.oschina.net/uploads/img/202110/14093857_WLY7.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新日志</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增grafana监控，支持influxdb，prometheusd数据源。</li> 
 <li>修复已知集群bug</li> 
</ul> 
<h2>Grafana监控部分截图</h2> 
<blockquote> 
 <p>文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwiki.smqtt.cc%2Fdocs%2Fsmqtt%2Fmonitor%2F1.monitor.html" target="_blank">http://wiki.smqtt.cc/docs/smqtt/monitor/1.monitor.html</a></p> 
</blockquote> 
<ul> 
 <li><strong><code>smqtt-application</code><span> </span>，应用程序监控</strong></li> 
</ul> 
<p style="color:#242424; text-align:start">​<span> </span><img alt="image-20211206171254864" src="https://gitee.com/eeasy/picbed/raw/master/img/2021/image-20211206171254864.png" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<p style="color:#242424; text-align:start"><img alt="image-20211206171332074" src="https://gitee.com/eeasy/picbed/raw/master/img/2021/image-20211206171332074.png" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><code>smqtt-jvm</code>，应用JVM监控</strong></li> 
</ul> 
<p style="color:#242424; text-align:start"><img alt="image-20211206171401373" src="https://gitee.com/eeasy/picbed/raw/master/img/2021/image-20211206171401373.png" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><code>smqtt-netty</code><span> </span>，reactor-netty监控</strong></li> 
</ul> 
<p style="color:#242424; text-align:start"><img alt="image-20211206171458469" src="https://gitee.com/eeasy/picbed/raw/master/img/2021/image-20211206171458469.png" style="margin-top:0px" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            