
---
title: 'Kiwi TCMS 11.2 发布，开源测试用例管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1965'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1965'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Kiwi TCMS 是一个集测试计划、测试运行和测试用例于一身的管理系统，用 Python 和 Django 编写。它具有许多强大的功能，如 Bugzilla 和 JIRA 集成，快速测试计划和运行搜索，针对每个计划、运行和案例以及 XML-RPC API 的强大访问控制。</p> 
<p style="margin-left:0px">Kiwi TCMS 11.2 发布了，这是一个包含多项改进、新 API 方法、内部重构和新翻译的小版本，也是这是第一个发布 aarch64容器镜像的版本。该版本带来如下改动：</p> 
<h2 style="margin-left:0px">自 Kiwi TCMS 11.1 以来的变化</h2> 
<h3 style="margin-left:0px">改进</h3> 
<ul> 
 <li>将 django 从 4.0.2 更新到 4.0.3</li> 
 <li>将 django-grappelli 从 3.0.2 更新到 3.0.3</li> 
 <li>将 django-simple-captcha 从 0.5.14 更新到 0.5.17</li> 
 <li>将 python-bugzilla 从 3.1.0 更新到 3.2.0</li> 
 <li>将 python-gitlab 从 3.1.1 更新到 3.2.0</li> 
 <li>将 node_modules/prismjs 从 1.26.0 更新到 1.27.0</li> 
 <li>添加新命令以执行一系列升级任务，建议将 manage.py migrate 替换为 manage.py upgrade</li> 
</ul> 
<h3 style="margin-left:0px">API</h3> 
<ul> 
 <li>新的 API 方法Category.create()。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkiwitcms%2FKiwi%2Fissues%2F2705" target="_blank">问题 #2705</a></li> 
 <li>新的 API 方法Classification.create()。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkiwitcms%2FKiwi%2Fissues%2F2705" target="_blank">问题 #2705</a></li> 
</ul> 
<h3 style="margin-left:0px">重构和测试</h3> 
<ul> 
 <li>添加 docker 构建和推送自动化</li> 
 <li>修复 Bandit 排除规则</li> 
 <li>在 aarch64 上测试和构建</li> 
 <li>从 pre-commit.ci 应用自动修复</li> 
 <li>从 Deepsource 应用自动修复</li> 
 <li>更新几个 GitHub Actions 的版本</li> 
 <li>为 Dependabot 使用适当的 package.json 路径</li> 
 <li>删除菜单中的旧遥测链接，以避免混淆</li> 
</ul> 
<h3 style="margin-left:0px">翻译</h3> 
<ul> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fbg%23" target="_blank">保加利亚语翻译</a></li> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fja%23" target="_blank">日文翻译</a></li> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fzh-TW%23" target="_blank">繁体中文翻译</a></li> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fsl%23" target="_blank">斯洛文尼亚语翻译</a></li> 
 <li>更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrowdin.com%2Fproject%2Fkiwitcms%2Fes-ES%23" target="_blank">西班牙语翻译</a></li> 
</ul> 
<h2 style="margin-left:0px">Kiwi TCMS Enterprise v11.2-mt</h2> 
<ul> 
 <li>基于猕猴桃TCMS v11.2</li> 
 <li>将 django-ses 从 2.4.0 更新到 2.6.0</li> 
 <li>将 python3-saml 从 1.13.0 更新到 1.14.0</li> 
 <li>还原“使用 Django==3.2.12 中的 django.contrib.staticfiles.storage”，而是使用最新 Django 版本的实现。关闭 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkiwitcms%2Fenterprise%2Fissues%2F140" target="_blank">问题 #140</a></li> 
 <li>开始<strong>在 aarch64 上构建</strong> kiwitcms/enterprise</li> 
 <li>添加变更日志检查和 docker 发布自动化</li> 
 <li>在登录页面上添加对 PSA 登录 URL 的测试。参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkiwitcms%2Fenterprise%2Fissues%2F83" target="_blank">问题 #83</a></li> 
 <li>添加 SAML 和 Azure AD 徽标图像</li> 
 <li>更新 GitHub 操作</li> 
 <li>使用 Keycloak 16.1.1 进行硬代码测试以解决与 Keycloak v17 容器的显着差异</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkiwitcms.org%2Fblog%2Fkiwi-tcms-team%2F2022%2F03%2F09%2Fkiwi-tcms-112%2F" target="_blank">https://kiwitcms.org/blog/kiwi-tcms-team/2022/03/09/kiwi-tcms-112/</a></p>
                                        </div>
                                      
</div>
            