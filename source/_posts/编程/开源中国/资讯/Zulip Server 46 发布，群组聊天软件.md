
---
title: 'Zulip Server 4.6 发布，群组聊天软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1618'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1618'
---

<div>   
<div class="content">
                                                                                            <p>Zulip Server 4.6 发布了。Zulip 是一个强大的开源群组聊天软件，采用 Python 编写，使用 Django 框架，支持通过会话流的私人消息和群聊。Zulip 还支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容包括：</p> 
<ul> 
 <li>已记录对 Debian 11 Bullseye 的官方支持，现在它已由 Debian 上游正式发布。</li> 
 <li>修复了在 Debian 10 Buster 上的安装。上游基础设施已经破坏了这个平台上的 Python <code>virtualenv</code>工具，在这个版本中解决了这个问题。</li> 
 <li>Zulip 版本现在从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.zulip.com%2Fserver%2F" target="_blank">https://download.zulip.com/server/</a> 分发，取代了旧<code>www.zulip.org</code>服务器发布。</li> 
 <li>添加了对 LDAP 同步的<code>is_realm_owner</code>和<code>is_moderator</code>标志的支持。</li> 
 <li><code>upgrade-zulip-from-git</code>现在使用<code>git fetch --prune</code>；这确保<code>upgrade-zulip-from-git master</code>返回错误而不是使用陈旧缓存版本的<code>master</code>分支，该分支本月已重命名为<code>main</code>。</li> 
 <li>添加了新的<code>reset_authentication_attempt_count</code>管理命令以允许系统管理员手动重置身份验证速率限制。</li> 
 <li>修正了一个错误，该错误导致<code>upgrade-postgresql</code>工具错误地删除<code>process-fts-updates</code>的<code>supervisord</code>配置。</li> 
 <li>修复了从 Zulip 2.1 及更早版本升级时罕见的迁移错误。</li> 
 <li>修复了一个微妙的错误，即左侧边栏会显示某些已重命名的的主题的新旧名称。</li> 
 <li>修复了对启用<code>http_only</code>设置的配置的传入电子邮件网关支持。</li> 
 <li>修复了 Zulip 的 outgoing webhook 与 Slack-compatible interface 与 Slack 的 documented interface 不同的问题。</li> 
 <li>安装和升级文档现在显示最新版本的版本号。</li> 
 <li>对 ReadTheDocs 文档进行了许多改进。</li> 
 <li>更新了 Transifex 的翻译数据。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F4.6" target="_blank">https://github.com/zulip/zulip/releases/tag/4.6</a></p>
                                        </div>
                                      
</div>
            