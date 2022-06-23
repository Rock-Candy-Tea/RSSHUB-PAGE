
---
title: 'Zulip Server 5.3 发布，开源团队协作工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6842'
author: 开源中国
comments: false
date: Thu, 23 Jun 2022 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6842'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">Zulip Server 5.3 现已发布。Zulip 是一个开源团队协作工具，一款专为实时和异步对话而设计的现代团队聊天应用程序，</span><span style="background-color:#ffffff">支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">具体更新内容如下：</span></span></p> 
<ul> 
 <li>CVE-2022-31017：修复了 protected-history streams 中的消息编辑事件暴露。Zulip 允许将一个流配置为具有受保护历史记录的私有流，这意味着新的订阅者应该只看到他们加入后发送的消息。然而，由于 Zulip Server 2.1.0 到 5.2 中的一个逻辑错误，当消息被编辑时，服务器会错误地向所有流的当前订阅者发送一个 API 事件，该事件包括消息的编辑内容和旧内容，无论他们是否可以看到原始消息。这个问题的影响已经被削弱，因为这个 API 事件被官方客户端忽略了，所以它只能被使用修改过的客户端或其浏览器的开发工具的用户观察到。</li> 
 <li>调整升级步骤以使使用 PostgreSQL 14 的服务器升级到 PostgreSQL 14.4，这修复了一个重要的潜在数据库损坏问题。</li> 
 <li>升级了异步请求处理以使用 Tornado 6。</li> 
 <li>修复了显示创建流失败的错误消息时的崩溃。</li> 
 <li>优化<code>upgrade-zulip</code>期间的步骤，以减少服务器停机时间。</li> 
 <li>为<code>upgrade-zulip</code>添加了一个新的<code>--skip-restart</code>flag，但不会将服务器重新启动到其中。</li> 
 <li>停止将整个远程 Git 存储库直接镜像到<code>/srv/zulip.git</code>。此镜像删除了本地分支并混淆了先前部署的状态。</li> 
 <li>修复了一个错误，该错误可能导致<code>delete_old_unclaimed_attachments</code>命令行工具删除仍被已删除（但尚未永久删除）消息引用的附件。</li> 
 <li>不再默认启用<code>USE_X_FORWARDED_HOST</code>，这通常是不需要的；代理文档现在阐明了何时需要。</li> 
 <li>修复了 nginx 配置以包含默认的系统级 nginx 模块。</li> 
 <li>仅在启用 HTTPS 的情况下尝试修复<code>certbot</code>SSL renewal 配置；这解决了 Zulip Server 5.2 中的一个回归问题；即，如果存在配置不当的证书，但证书已过期且未使用，升级将失败。</li> 
 <li>改进的代理和数据库备份文档。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F5.3" target="_blank">https://github.com/zulip/zulip/releases/tag/5.3</a></p>
                                        </div>
                                      
</div>
            