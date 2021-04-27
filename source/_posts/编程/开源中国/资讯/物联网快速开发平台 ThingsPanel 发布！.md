
---
title: '物联网快速开发平台 ThingsPanel 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9d41a1b329112cc733f1cea35e1b0caf606.png'
author: 开源中国
comments: false
date: Tue, 27 Apr 2021 13:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9d41a1b329112cc733f1cea35e1b0caf606.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:justify">如何快速、高质量交付物联网项目并获得更高的利润是全球所有物联网公司所关心的核心问题。</p> 
<p style="text-align:justify">针对这一问题，Amazon、Azure、Intel、aliyun等提出了快速的SAAS方案，但是给客户带来了长期的运行成本，也并不有利于物联网服务厂商获得更高的利润。于是方案就转向了Node-red、Grafana、Thingsboard等方案，但是由于Node-red美观度差、体验一般，Grafana功能单一，只能可视化等问题，于是Thingsboard变成了几乎唯一的选择。国内外的中小服务公司纷纷在Thingsboard上进行二次开发。Thingsboard的缺陷是复杂、美观度差、用户门槛高、交付之后客户不满意。因此Thingspanel应运而生。</p> 
<p style="text-align:justify">ThingsPanel物联网平台是一套面向快速实施的物联网方案开发与共享平台，平台以简单、快速、美观、通用为特点，技术研发人员通过ThingsPanel平台可以快速构建应用，并将业务打包分发给世界各地的用户以获取收入。对业务人员而言，ThingsPanel不用写代码，一整套方案开箱即用。业务交付时间是传统的物联网方案的30%以下。成本也大幅度降低，ThingsPanel整合一系列业务方案，可广泛应用于交通、医疗、消费、家居、消防、安防、工业、农业等各个领域。</p> 
<p style="text-align:justify"><img alt height="1140" src="https://oscimg.oschina.net/oscnet/up-9d41a1b329112cc733f1cea35e1b0caf606.png" width="1920" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:justify">ThingsPanel的优势</h1> 
<ul> 
 <li style="text-align:justify">更美观：Thingspanel借鉴了Grafana在美观度方面的优势，并远超越Thingsboard的界面和体验，使人看了就爱。</li> 
 <li style="text-align:justify">更简单：与ThingsBoard相比，Thingspanel开发门槛低，更简单。Thingspanel推行一种拿来就用的方案，尽可能的直接满足用户需求。</li> 
 <li style="text-align:justify">更快：与Thingsboard复杂的配置系统不同，Thingspanel对业务层进行抽象封装，使用户对复杂业务不可见，用业务的语言描述，更恰当的来说，Thingspanel是一个应用市场，下载安装，向导式部署即可完成安装。</li> 
 <li style="text-align:justify">成本更低：由于开源代码与集成度更高带来的双重优势，推广成本和实施成本大幅降低。开源虽然并不意味着免费，但是意味着极地的软件成本和推广成本，抽象与集成度高带来的就是系统更为简单。</li> 
</ul> 
<h1 style="text-align:justify">ThingsPanel针对的用户</h1> 
<ul> 
 <li style="text-align:justify">开发者：插件式结构适合快速开发构建物联网应用。</li> 
 <li style="text-align:justify">最终用户：获取预配置的物联网应用，不写代码，开箱即用。</li> 
</ul> 
<div> 
 <h1><span style="color:black">技术特点</span></h1> 
</div> 
<ul> 
 <li>PHP：Laravel</li> 
 <li>Swoole： <span style="color:#000000">PHP 协程框架，</span>单机十万节点，可通过集群扩展至百万节点。</li> 
 <li>Vue.js：前端构建，体验更佳</li> 
 <li>PostgreSQL：更高的负载能力，更低的拥有成本。</li> 
 <li>TimescaleDB ：时序数据库，PostgreSQL插件。</li> 
 <li>Nginx：高性能Web服务器。</li> 
 <li>RabbitMQ：企业级消息队列处理。</li> 
</ul> 
<h1>功能结构</h1> 
<p><img alt height="1065" src="https://oscimg.oschina.net/oscnet/up-48f1bc9eaa52558cec7a97cbddaff45ae2e.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h1>ThingsPanel产品图片</h1> 
<p>应用管理</p> 
<p><img alt height="979" src="https://oscimg.oschina.net/oscnet/up-4f7badb133b631eafcfa9cb8b87f171b9b1.png" width="1920" referrerpolicy="no-referrer"></p> 
<p>业务管理</p> 
<p><img alt height="1140" src="https://oscimg.oschina.net/oscnet/up-d0638cb91aca9f91ce5e7bcb133fdba965e.png" width="1920" referrerpolicy="no-referrer"></p> 
<p>可视化</p> 
<p><img alt height="1140" src="https://oscimg.oschina.net/oscnet/up-088d97b8d058702c19673480ea07b21903d.png" width="1920" referrerpolicy="no-referrer"></p> 
<p>气象站（实例）</p> 
<p><img alt height="717" src="https://oscimg.oschina.net/oscnet/up-c9ba0822f9f386cef0f580f6b88eb4f0566.png" width="1275" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>本项目经过一年多的开发，已经在多个项目上投入使用验证，如有问题请在本项目地址提交issues，我们将尽快更新，感谢各位的支持。</p> 
<ul> 
 <li>本项目发布地址： <a href="https://www.oschina.net/p/thingspanel">https://www.oschina.net/p/thingspanel</a></li> 
</ul> 
<div id="gtx-trans" style="position: absolute; left: 42px; top: 7780.73px;"> 
 <div class="gtx-trans-icon">
   
 </div> 
</div>
                                        </div>
                                      
</div>
            