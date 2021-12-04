
---
title: 'Zulip Server 4.8 发布，群组聊天软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2356'
author: 开源中国
comments: false
date: Sat, 04 Dec 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2356'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Zulip Server 4.8 发布了。Zulip 是一个强大的开源群组聊天软件，采用 Python 编写，使用 Django 框架，支持通过会话流的私人消息和群聊。Zulip 还支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容包括：</p> 
<ul> 
 <li>CVE-2021-43791：Zulip 可能无法在确认密钥上强制执行过期日期，从而允许用户可能使用过期邀请、自行注册或领域创建链接。</li> 
 <li>默认情况下，开始安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstripe%2Fsmokescreen" target="_blank">Smokescreen</a> 以强化 Zulip 抵御 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fowasp.org%2Fwww-community%2Fattacks%2FServer_Side_Request_Forgery" target="_blank">SSRF</a> 攻击。Zulip 从 Zulip 4.0 开始提供 Smokescreen 作为选项。</li> 
 <li>用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcactus%2Fgo-camo" target="_blank">go-camo</a> 替换了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatmos%2Fcamo" target="_blank">camo</a> 图像代理，这是一个经过维护的重新实现，也可以防止 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fowasp.org%2Fwww-community%2Fattacks%2FServer_Side_Request_Forgery" target="_blank">SSRF</a> 攻击。当该服务器作为独立部署的一部分进行部署时，它现在仅监听 127.0.0.1。</li> 
 <li>开始对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzulip.com%2Fhelp%2Fallow-image-link-previews" target="_blank">URL preview</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzulip.com%2Fhelp%2Fallow-image-link-previews" target="_blank">s 中</a>显示的图像使用 camo。这提高了隐私并解决了以下问题：指向具有过期或其他无效 SSL 证书的第三方服务器的图像链接会触发 Zulip Desktop 用户的混乱弹出窗口。</li> 
 <li>修复了一个错误，该错误可能导致 Tornado 在重新启动负载过重的 Zulip 服务器时不正确地关闭（导致其客户端立即重新加载整页）。</li> 
 <li>更新了 Python 依赖项。</li> 
 <li>截断大型“remove”移动通知事件，以便将数百条私人消息或其他通知消息一次性标记为已读，不会超过 Apple 的 4 KB 通知大小限制。</li> 
 <li>Slack importer 改进： 
  <ul> 
   <li>确保为 Slack 机器人生成的虚假电子邮件地址是唯一的。</li> 
   <li>添加了对从目录导入 Slack 导出文件的支持，而不仅仅是 .zip 文件。</li> 
   <li>使用无效的 Slack 令牌提供更好的错误消息。</li> 
   <li>在 Windows 上添加了对 non-ASCII Unicode 文件夹名称的支持。</li> 
  </ul> </li> 
 <li>添加对 V3 Pagerduty webhook 的支持。</li> 
 <li>更新了 Apache SSO 的文档，现在Zulip使用C扩展（re2模块），需要额外的配置。</li> 
 <li>修复了 SAML 响应中的空名称会引发错误的错误。</li> 
 <li>确保<code>deliver_scheduled_emails</code>和<code>deliver_scheduled_messages</code>在同时运行于多个服务器时不会被重复发送。</li> 
 <li>扩展的 Certbot 故障排除文档。</li> 
 <li>修复了 soft deactivation catch-up code 中的一个错误，在这种情况下，一个 race condition 会在审计日志中为一个用户和一个数据流创建多个订阅停用条目。</li> 
 <li>更新翻译，包括添加僧伽罗语翻译。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F4.8" target="_blank">https://github.com/zulip/zulip/releases/tag/4.8</a></p>
                                        </div>
                                      
</div>
            