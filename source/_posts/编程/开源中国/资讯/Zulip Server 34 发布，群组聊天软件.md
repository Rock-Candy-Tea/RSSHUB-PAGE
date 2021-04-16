
---
title: 'Zulip Server 3.4 发布，群组聊天软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6165'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6165'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Zulip Server 3.4 发布了。Zulip 是一个强大的开源群组聊天软件，采用 Python 编写，使用 Django 框架，支持通过会话流的私人消息和群聊。Zulip 还支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</p> 
<p>具体更新内容包括：</p> 
<ul> 
 <li>CVE-2021-30487：防止管理员将主题移到不允许的 streams 中。</li> 
 <li>CVE-2021-30479：禁止访客用户访问<code>all_public_streams</code>API。</li> 
 <li>CVE-2021-30478：防止 API super users 伪造发给其他组织的消息。</li> 
 <li>CVE-2021-30477：阻止 outgoing webhook bots 将任意消息发送到任何 stream。</li> 
 <li>修复了 outgoing emails 中潜在的 HTML 注入错误。</li> 
 <li>修复了 Postfix 配置错误，当配置为使用本地 Postfix 发送 outgoing emails 时，该错误会阻止向任何包含 . 、+ 或以 mm 开头的邮件地址发送邮件。</li> 
 <li>修复了一个 backporting 错误，该错误导致 manage.py change_user_role 工具不能用于 admin、member 或 guest 角色。</li> 
 <li>添加对从现代版本的桌面应用程序发送的 logout events 的支持。</li> 
 <li>升级的次要 python 依赖项。</li> 
 <li>次要文档修复。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F3.4" target="_blank">https://github.com/zulip/zulip/releases/tag/3.4</a></p>
                                        </div>
                                      
</div>
            