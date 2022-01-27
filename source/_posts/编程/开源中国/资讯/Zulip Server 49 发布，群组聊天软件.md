
---
title: 'Zulip Server 4.9 发布，群组聊天软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5302'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5302'
---

<div>   
<div class="content">
                                                                                            <p>Zulip Server 4.9 发布了。Zulip 是一个强大的开源群组聊天软件，采用 Python 编写，使用 Django 框架，支持通过会话流的私人消息和群聊。Zulip 还支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容包括：</p> 
<ul> 
 <li>CVE-2021-43799：涉及 RabbitMQ 的远程执行代码。</li> 
 <li>关闭对 RabbitMQ 25672 端口的访问；初始安装尝试关闭此端口，但未能重新启动 RabbitMQ 进行配置。</li> 
 <li>删除了<code>zulip.conf</code>中的<code>rabbitmq.nodename</code>配置；所有RabbitMQ 实例都将被重新配置为具有<code>zulip@localhost</code>的节点名称。你可以从<code>zulip.conf</code>配置文件中删除此设置（如果存在）。</li> 
 <li>在 Docker 镜像中添加了对 Camo 镜像代理的缺失支持。这解决了一个长期存在的问题，即图像预览（如果启用）在基于 Docker 的安装中显示为损坏的图像。</li> 
 <li>修复了当用户最初无权发送此类消息时，允许用户编辑消息以添加通配符提及的错误。</li> 
 <li>修复了工具中的一个错误，纠正了因更新托管 PostgreSQL 的操作系统而导致的数据库损坏，该错误以前在验证中省略了一些索引。</li> 
 <li>开始将来自 Camo 图像代理的请求通过一个非 Smokescreen 代理进行路由。如果配置了非 Smokescreen 代理的话；因为 Camo 包括拒绝访问私有子网的逻辑，通过 Smokescreen 路由其请求通常是不必要的。</li> 
 <li>修复了更改 Camo secret 需要运行<code>zulip-puppet-apply</code>的错误。</li> 
 <li>修复了<code>scripts/setup/compare-settings-to-template</code>，使其能够从任何目录运行。</li> 
 <li>切换 Let's Encrypt 更新以使用它自己的计时器，而不是自定义 cron 作业。这修复了<code>nginx</code>在获得更新的证书后偶尔不会重新加载的错误。</li> 
 <li>更新了文档和工具，注意使用安装<code>upgrade-zulip-from-git</code>需要 3 GB 的 RAM，或 2 GB 和至少 1GB 的 swap。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F4.9" target="_blank">https://github.com/zulip/zulip/releases/tag/4.9</a></p>
                                        </div>
                                      
</div>
            