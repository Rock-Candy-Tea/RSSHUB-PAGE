
---
title: 'Zulip Server 5.2 发布，开源团队协作工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3446'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3446'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">Zulip Server 5.2 现已发布。Zulip 是一个</span><span style="background-color:#ffffff">开源团队协作工具，一款专为实时和异步对话而设计的现代团队聊天应用程序，</span><span style="background-color:#ffffff">支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">具体更新内容如下：</span></span></p> 
<ul> 
 <li>修复了打开 compose box 时在 5.0 中引入的 UI 中的性能回归问题。</li> 
 <li>修复了一个错误，如果 Zulip 在 Docker 或低内存环境中运行，可能会间歇性导致 URL 预览失败。</li> 
 <li>修复了一个问题，即使未配置 S3 WAL 备份/复制，也会导致 PostgreSQL 10 和 PostgreSQL 11 尝试将每个 WAL 日志写入 S3。</li> 
 <li>修复了阻止 SCIM 集成停用用户的问题。</li> 
 <li>修复了一个错误，当通过“near”链接查看主题中的新消息时，会错误地出现"You unsubscribed"的通知。</li> 
 <li>修复了明确设置为空时，<code>EMAIL_HOST_PASSWORD</code>被取消设置的警告。</li> 
 <li>修复了在 Markdown 渲染期间发生超时时不完整的回溯。</li> 
 <li>修复了在比较 settings.py 的可能的原始版本时，没有考虑 Zulip Server 的一些旧版本。</li> 
 <li>停止使用<code>database_password</code>，如果它被设置但<code>database_user</code>没有被设置。</li> 
 <li>如果当前未使用 LetsEncrypt 证书配置，则停止尝试修复它们。</li> 
 <li>对<code>check-database-compatibility</code>工具的输出进行排序和美化。</li> 
 <li>将大<code>zerver/lib/actions.py</code>文件拆分为<code>zerver/actions/</code>下的许多文件。此非功能性更改已向后移植，以确保向后移植其他更改仍然很容易。</li> 
 <li>更新了文档以反映当前的移动应用程序仅保证与 Zulip Server 3.0 及更高版本兼容；它们也可能适用于早期版本，但体验会降低。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F5.2" target="_blank">https://github.com/zulip/zulip/releases/tag/5.2</a></p>
                                        </div>
                                      
</div>
            