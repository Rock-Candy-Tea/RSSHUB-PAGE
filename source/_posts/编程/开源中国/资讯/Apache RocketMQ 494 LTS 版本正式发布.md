
---
title: 'Apache RocketMQ 4.9.4 LTS 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6d97dda2d63c0382689d95bad63877541f2.png'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 10:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6d97dda2d63c0382689d95bad63877541f2.png'
---

<div>   
<div class="content">
                                                                                            <p><span>经过社区全体开发者的努力，Apache RocketMQ 在近期正式发布了4.9.3版本和LTS 4.9.4 版本，共有 120 名贡献者参与其中，新增来自字节跳动、理想汽车、小米、华为云四名committer。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#676464"><em>下载地址：<span style="color:#337ab7">https://rocketmq.apache.org/release_notes/release-notes-4.9.3/</span></em></span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#676464"><em>下载地址：<span style="color:#337ab7">https://rocketmq.apache.org/release_notes/release-notes-4.9.4/</span></em></span></p> 
<p style="margin-left:0; margin-right:0">首先RocketMQ LTS 版本指的是Apache RocketMQ社区长期提供支持的版本。在社区后续版本中的BUG修复也会及时的从trunk反向移植到这个版本，从而实现后续5.x和4.9.x双版本交替发布，预计每个 LTS 版本将会支持 18 个月。</p> 
<p style="margin-left:0; margin-right:0">4.9.3 是RocketMQ的一个重要版本，该版本除了引入社区非常关注的RIP-28轻量级消息队列LMQ等新特性之外，稳定性和性能也做了大量优化。</p> 
<p style="margin-left:0; margin-right:0">4.9.4 作为Apache RocketMQ 的一个 LTS 版本，在4.9.3版本的基础上，该版本中收录PR超过150条，再次对性能和稳定性进行了全面提升。</p> 
<p style="margin-left:0; margin-right:0"><strong>RIP-28 轻量级消息队列Light message queue (LMQ)支持  @</strong><strong>田六合</strong><span style="color:#000000"><strong>(</strong></span><span style="color:#000000"><strong>tianliuliu</strong></span><span style="color:#000000"><strong>)</strong></span></p> 
<p style="margin-left:0; margin-right:0">在一些非常容易见到的消息传递场景需要支持大量的主题，比如MQTT、AMQP协议，它们的MQTT多级主题或AMQP轻量级队列可以由用户在发送和订阅消息的时候随意设置，我们暂且称它们为轻量级消息队列（LMQ）。由于LMQ的数量非常多，而原来RocketMQ主题资源密集，很难支持百万级别甚至更多的LMQ。我们需要为IOT设备和 AMQP 协议用户提供一个可靠和实时的消息服务的新解决方案，同时解决有关可靠性、延迟和可用性的问题。因此在 Apache RocketMQ 项目中，我们将构建一个新特性，用 LMQ 来支持 MQTT 和 AMQP 等功能。</p> 
<p style="margin-left:0; margin-right:0">如图，这里我们简单给出了轻量级消息队列LMQ的基本实现原理，可以看到一个普通消息是如何自动分发到多个Consumer的多列中的，想了解更多可以参考</p> 
<p style="margin-left:0; margin-right:0; text-align:left">RIP-28(<em><span style="color:#337ab7">https://github.com/apache/rocketmq/wiki/RIP-28-Light-message-queue-(LMQ)</span></em>)</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6d97dda2d63c0382689d95bad63877541f2.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>ISSUE-3585 RocketMQ性能优化 @</strong><strong>黄理(areyouok)</strong></p> 
<p style="margin-left:0; margin-right:0">在4.9.3版本中,我们针对上一个版本的性能做了大量优化工作，例如对RocketMQ协议消息头的编解码优化；在序列化的时候引入零拷贝；在写消费队列和写备机commitlog的时候使用mmap buffer替换原来的FileChannel等。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fefd7225b6ddd51101159987f9930b74775.png" referrerpolicy="no-referrer"></p> 
<p><strong>版本全量PR列表：</strong></p> 
<p style="margin-left:0; margin-right:0">目前Github支持每个版本都进行PR的统计，为方便大家了解，这里分别给出了两个版本的PR列表，大家可以参考每个版本的变化。</p> 
<p style="margin-left:0; margin-right:0">参考<span style="color:#337ab7"><em>https://github.com/apache/rocketmq/releases</em></span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#000000">4.9.3</span></strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-12b6d078bc8f7c4a556dca3589a382c76a6.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>4.9.4 LTS</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-de23a69dfcdf5edeceddfd970fa2557d4d0.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            