
---
title: 'Notification Manager 2.0.0 发布：新增飞书通知、通知路由、通知静默'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=965'
author: 开源中国
comments: false
date: Wed, 11 May 2022 15:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=965'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fnotification-manager" target="_blank">Notification Manager</a><span> </span>是 KubeSphere 可观测团队开源的一款 Kubernetes 平台上的<strong>多租户通知管理系统</strong>，其从 Kubernetes 接收告警、事件、审计，根据用户设置的模板生成通知消息并推送给用户。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在过去的几个月里，社区一直在努力工作，为 Notification Manager 2.0.0 版本的发布做准备。今天，我们非常高兴地宣布 Notification Manager 2.0.0 已经正式发布了！感谢社区各位小伙伴对新功能、增强功能和错误修复的各种帮助！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Notification Manager 2.0.0 为您带来了许多值得关注的功能，包括新增<strong>飞书通知</strong>、<strong>通知路由</strong>、<strong>通知静默</strong>、<strong>自定义模板增强</strong>等。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">通知</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增了对飞书的支持，支持通过机器人向群组发送通知，支持同时向多个用户和部门发送通知。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">路由</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增路由功能，用户可以通过设置路由规则，将指定的通知发送给指定的用户。在 1.x 版本中，Notification Manager 会根据通知中的 namespace 标签自动选择需要接收通知的用户。这种做法可以减化用户的配置工作，但是也使得用户无法控制通知的流向。路由功能弥补了这一缺憾，路由功能<strong>赋予了用户自主控制通知流向的能力</strong>，用户可以通过路由对通知进行更细粒度的管理。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">静默</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增静默功能，可以通过配置静默规则，在特定的时间段屏蔽特定的通知。用户可以设置全局静默规则和租户静默规则，全局静默规则会对所有租户生效，租户静默规则只会对租户所属的通知渠道生效。静默规则有两方面的作用，一是在特定的时间段屏蔽通知，二是可以作为过滤器使用，对通知进行过滤，结合静默规则和通知过滤，用户可以实现更复杂的通知管理功能。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">模板</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持动态更新模板，用户更新模板文件后<strong>不需要重启 Notification Manager</strong><span> </span>了。 支持为 Receiver 设置模板，用户可以自由定义通知格式，不用担心对其他用户造成影响。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此外，您还可以通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fnotification-manager%2Freleases%2Ftag%2Fv2.0.0" target="_blank">发布说明</a>来了解 Notification Manager 2.0.0 的更多相关信息。</p> 
<p> </p>
                                        </div>
                                      
</div>
            