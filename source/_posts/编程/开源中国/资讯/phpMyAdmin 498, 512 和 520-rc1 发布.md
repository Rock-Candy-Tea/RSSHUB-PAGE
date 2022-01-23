
---
title: 'phpMyAdmin 4.9.8, 5.1.2 和 5.2.0-rc1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=332'
author: 开源中国
comments: false
date: Sun, 23 Jan 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=332'
---

<div>   
<div class="content">
                                                                                            <p>phpMyAdmin 近日<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phpmyadmin.net%2Fnews%2F2022%2F1%2F22%2Fphpmyadmin-498-512-and-520-rc1-are-released%2F" target="_blank">发布</a>了三个新版本：</p> 
<ul> 
 <li>4.9.8：修复部分安全漏洞</li> 
 <li>5.1.2：修复部分安全漏洞，同时还修复了大量错误，以及更好地兼容 PHP 8.0 和 8.1</li> 
 <li>5.2.0-rc1：引入大量新特性的测试版本</li> 
</ul> 
<p><strong>修复安全漏洞</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#212529">PMASA-2022-1：</span>phpMyAdmin 在处理双因素认证的过程中被发现了一个漏洞，导致用户可能会在随后的认证会话中操纵他们的帐户以绕过双因素认证（4.9 和 5.1 系列受影响）</li> 
 <li><span style="background-color:#ffffff; color:#212529">PMASA-2022-2：</span>此漏洞会导致攻击者提交恶意信息，在图形化设置页面中进行 XSS 或 HTML 注入攻击（仅 5.1 系列受影响，不影响 4.9）</li> 
 <li>某些情况下，潜在的敏感信息（如数据库名称）会暴露在 URL 中，现已支持加密此类信息（4.9 和 5.1 系列受影响）</li> 
 <li> <p>在尝试登录失败期间，错误消息会显示目标数据库服务器的主机名或 IP 地址。这会导致有关网络基础设施的一些信息被泄露。现已支持使用<span style="background-color:#ffffff; color:#212529"><span> </span></span><code>$cfg['Servers'][$i]['hide_connection_errors']</code><span style="background-color:#ffffff; color:#212529"><span> </span>指令来阻止（</span>4.9 和 5.1 系列受影响<span style="background-color:#ffffff; color:#212529">）</span></p> </li> 
</ul> 
<p><strong><span style="background-color:#ffffff; color:#212529">新变化 </span>(5.2.0-rc1)</strong></p> 
<ul> 
 <li>删除对 Microsoft Internet Explorer 的支持</li> 
 <li>要求 PHP 7.2 或更高版本</li> 
 <li>要求安装 openssl PHP 扩展</li> 
 <li>改进对 system CA bundle 和 cacert.pem 的处理，亦可根据需要回滚到 Mozilla CA</li> 
 <li>使用 "primary/replica" 替代 "master/slave"</li> 
 <li>将 "NOT LIKE %...%" 运算符添加到 Table search</li> 
 <li>支持 Mroonga 引擎</li> 
 <li>支持锁定帐户</li> 
 <li>对 SQL 解析器库的修复和改进</li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpmyadmin.net%2Fdownloads%2F" target="_blank">https://phpmyadmin.net/downloads/</a></p>
                                        </div>
                                      
</div>
            