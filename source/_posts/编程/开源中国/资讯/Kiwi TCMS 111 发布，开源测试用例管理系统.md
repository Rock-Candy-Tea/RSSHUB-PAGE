
---
title: 'Kiwi TCMS 11.1 发布，开源测试用例管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=335'
author: 开源中国
comments: false
date: Thu, 03 Feb 2022 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=335'
---

<div>   
<div class="content">
                                                                                            <p>Kiwi TCMS 是一个集测试计划、测试运行和测试用例于一身的管理系统，用 Python 和 Django 编写。它具有许多强大的功能，如 Bugzilla 和 JIRA 集成，快速测试计划和运行搜索，针对每个计划、运行和案例以及 XML-RPC API 的强大访问控制。</p> 
<p>Kiwi TCMS 11.1 发布了，该版本带来如下改动：</p> 
<p><strong>安全</strong></p> 
<ul> 
 <li>将 Django 从 3.2.10 更新到 4.0.2 ，以修复几个漏洞：CVE-2022-22818、CVE-2022-23833、CVE-2021-45115、CVE-2021-45116、CVE-2021-45452。</li> 
</ul> 
<h3 style="margin-left:0px">改进</h3> 
<ul> 
 <li>将 django-contrib-comments 从 2.1.0 更新到 2.2.0</li> 
 <li>将 django-uuslug 从 1.2.0 更新到 2.0.0</li> 
 <li>将 python-gitlab 从 3.1.0 更新到 3.1.1</li> 
 <li>将 node_modules/marked 从 4.0.10 更新到 4.0.12</li> 
</ul> 
<h3 style="margin-left:0px">设置</h3> 
<ul> 
 <li>不再使用 RECAPTCHA_PUBLIC_KEY、RECAPTCHA_PRIVATE_KEY 和 RECAPTCHA_USE_SSL </li> 
 <li>添加新设置 <code>USE_CAPTCHA</code>，默认为 True</li> 
 <li>字符串 “captcha” 被添加到 INSTALLED_APPS</li> 
</ul> 
<h3 style="margin-left:0px">Bug修复</h3> 
<ul> 
 <li>修复：不适当的 RPC 调用，导致版本和构建下拉小部件不显示任何值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkiwitcms%2FKiwi%2Fissues%2F2704" target="_blank"> #2704</a></li> 
</ul> 
<h3 style="margin-left:0px">重构和测试</h3> 
<ul> 
 <li>将 tzdata 添加到需求</li> 
 <li>用 django-simple-captcha 替换 django-recaptcha</li> 
 <li>调整 /init-db 视图，以可靠地检测应用数据库迁移何时完成，并且确保不会过早退出。</li> 
</ul> 
<h3 style="margin-left:0px">翻译</h3> 
<ul> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fsl%23" target="_blank">斯洛文尼亚语</a>翻译</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkiwitcms.org%2Fblog%2Fkiwi-tcms-team%2F2022%2F02%2F02%2Fkiwi-tcms-111%2F" target="_blank">https://kiwitcms.org/blog/kiwi-tcms-team/2022/02/02/kiwi-tcms-111/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            