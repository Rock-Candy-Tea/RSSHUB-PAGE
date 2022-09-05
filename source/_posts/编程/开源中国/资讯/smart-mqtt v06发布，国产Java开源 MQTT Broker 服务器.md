
---
title: 'smart-mqtt v0.6发布，国产Java开源 MQTT Broker 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-377369a4c9a9539db9d51442c9054892411.png'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 07:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-377369a4c9a9539db9d51442c9054892411.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:start"><img height="774" src="https://oscimg.oschina.net/oscnet/up-377369a4c9a9539db9d51442c9054892411.png" width="1080" referrerpolicy="no-referrer"></h1> 
<p style="margin-left:0px; margin-right:0px; text-align:justify">smart-mqtt 是用 java 语言开发的 MQTT Broker 服务，也是 smartboot 组织下首款真正意义上面向物联网的解决方案。旨在帮助企业以较低的成本快速搭建稳定、可靠的物联网服务，助力万物互联互通。</p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:start">一、更新内容 🎉</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.1 Features 🌈</h2> 
<ul> 
 <li>应社区用户要求，开源版 smart-mqtt适配 JDK 回退至1.8。</li> 
 <li>完善retain消息的规范实现，当服务端接收到保留标志为 1 且有效载荷为零字节的 PUBLISH 报文时，该主题下任何现存的保留消息必须被移除。</li> 
 <li>优化日志输出格式，增加时间信息。</li> 
 <li>smart-mqtt broker 线程数支持配置化。</li> 
 <li>更新客户端connect鉴权的接口设计。 (by<span> </span><a href="https://gitee.com/yamikaze">@yamikaze<span> </span></a>)</li> 
 <li>支持docker启动 smart-mqtt 服务</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.2 Bugfix 🛠</h2> 
<ul> 
 <li>修复mqtt协议版本不兼容时引发的空指针问题。</li> 
 <li>修复订阅topic后retain消息被无限推送的问题。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.3 文档 📘</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsmartboot%2Fsmart-mqtt%2Fdocker" target="_blank">Docker启动及交叉编译</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsmartboot%2Fsmart-mqtt%2Fspecification" target="_blank">社区行为规约</a></li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">二、文档地址</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span><span style="background-color:#ffffff; color:#40485b">语雀：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsmartboot%2Fsmart-mqtt%2F" target="_blank"><u>https://www.yuque.com/smartboot/smart-mqtt</u>/</a></span></span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1a1a1a">三、开源地址</span></h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>Gitee（主站）：</span><u><a href="https://gitee.com/smartboot/smart-mqtt">https://gitee.com/smartboot/smart-mqtt</a></u></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>GitHub（镜像同步）：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsmartboot%2Fsmart-mqt" target="_blank"><u>https://github.com/smartboot/smart-mqt</u></a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">详情见：<a href="https://gitee.com/smartboot/smart-mqtt/releases/tag/v0.6">https://gitee.com/smartboot/smart-mqtt/releases/tag/v0.6</a></p>
                                        </div>
                                      
</div>
            