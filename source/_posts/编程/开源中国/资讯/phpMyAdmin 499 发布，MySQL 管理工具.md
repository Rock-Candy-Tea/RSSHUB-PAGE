
---
title: 'phpMyAdmin 4.9.9 发布，MySQL 管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7655'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7655'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phpmyadmin.net%2Fnews%2F2022%2F1%2F23%2Fphpmyadmin-499-released%2F" target="_blank">phpMyAdmin 4.9.9 已发布</a>，这是针对 4.9.8 的紧急修复版本，修复了以下两个问题：</p> 
<ul> 
 <li>修复阻止与 PHP 5 一起使用的语法错误</li> 
 <li>设置 controluser 时显示有关新“hide_configuration_errors”指令的错误</li> 
</ul> 
<p><a href="https://www.oschina.net/news/179740/phpmyadmin-498-512-n-520-rc1-released">phpMyAdmin 4.9.8</a> 修复的安全漏洞包括：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#212529">PMASA-2022-1：</span>phpMyAdmin 在处理双因素认证的过程中被发现了一个漏洞，导致用户可能会在随后的认证会话中操纵他们的帐户以绕过双因素认证</li> 
 <li>某些情况下，潜在的敏感信息（如数据库名称）会暴露在 URL 中，现已支持加密此类信息</li> 
 <li> <p style="margin-left:0; margin-right:0">在尝试登录失败期间，错误消息会显示目标数据库服务器的主机名或 IP 地址。这会导致有关网络基础设施的一些信息被泄露。现已支持使用<span style="background-color:#ffffff; color:#212529"><span> </span></span><code>$cfg['Servers'][$i]['hide_connection_errors']</code><span style="background-color:#ffffff; color:#212529"><span> </span>指令来阻止</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">此外，phpMyAdmin 5.1.2 也已被发现两个已知问题，hide_connection_errors 和导航窗格问题。开发团队正在为这些问题准备修复程序，并将单独发布 5.1.3 版本。</p> 
<p>值得注意的是，phpMyAdmin 4.9 处于长期支持阶段，它只会获得重要的安全修复和关键错误修复。因此开发团队建议用户迁移到 5.1 版本。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phpmyadmin.net%2Fdownloads%2F" target="_blank">https://www.phpmyadmin.net/downloads/</a></p>
                                        </div>
                                      
</div>
            