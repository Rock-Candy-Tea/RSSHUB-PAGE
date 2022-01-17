
---
title: 'Lemmy v0.15.1 发布，高性能自托管仿 Reddit 社区'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2608'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2608'
---

<div>   
<div class="content">
                                                                                            <p>Lemmy v0.15.1 现已发布。Lemmy 是一个 Rust 实现的类似于 Reddit、Lobste.rs、Raddle 与 Hacker News 等网站的项目，用户订阅感兴趣的论坛、发布链接和讨论，可以进行点赞/点踩，并对它们发表评论。基于 Fediverse 标准，所有服务器可以联合，这意味着在一台服务器上注册的用户可以订阅任何其它服务器上的论坛，并且可以与在其它地方注册的用户进行讨论。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">主要更新内容如下：</p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>所需的电子邮件验证</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>管理员可以打开此功能，新用户需要验证他们的电子邮件。当前用户不必这样做。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>注册申请</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>管理员现在可以选择让新用户填写申请以加入你的服务器。他们的顶部栏中有一个新面板，他们可以在其中批准或拒绝待处理的申请。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这与 require_email 字段一起使用。如果这也被打开了，那么只有在他们的电子邮件被验证后，才会显示申请。当他们被接受时，用户将收到一封电子邮件。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Closed / Private instances</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>实例设置现在包括一个私有实例选项，如果打开该选项，将只允许登录用户查看你的站点。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Temporary Bans</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在禁止用户访问你的网站或社区时，版主现在可以选择给禁令持续天数。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>允许被屏蔽用户的评论回复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>过去，如果用户屏蔽了你，你将无法回复他们的公开帖子和评论。现在已修复，他们不会看到你的内容，但其他人可以。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>详情可查看：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Freleases%2Ftag%2F0.15.1" target="_blank">https://github.com/LemmyNet/lemmy/releases/tag/0.15.1</a></p>
                                        </div>
                                      
</div>
            