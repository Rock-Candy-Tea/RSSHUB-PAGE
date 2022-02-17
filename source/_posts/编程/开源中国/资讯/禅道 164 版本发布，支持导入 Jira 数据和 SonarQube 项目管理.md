
---
title: '禅道 16.4 版本发布，支持导入 Jira 数据和 SonarQube 项目管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://blog.easycorp.cn/file.php?f=easycorp/202202/f_3524f7cad3e46a63b223975daa7ae18d&t=png&o=&s=&v=1644894005'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 15:18:00 GMT
thumbnail: 'https://blog.easycorp.cn/file.php?f=easycorp/202202/f_3524f7cad3e46a63b223975daa7ae18d&t=png&o=&s=&v=1644894005'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">禅道项目管理软件集产品管理、项目管理、质量管理、文档管理、组织管理和事务管理于一体，是一款功能完备的项目管理软件，完美地覆盖了项目管理的核心流程。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">禅道官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2F" target="_blank">https://www.zentao.net</a></span></p> 
<p>大家好，禅道16.4发布了，本次发布主要实现了<span><strong>禅道导入</strong></span><strong>Jira数据</strong>，免费为广大Jira用户提供了新的平台和管理工具；同时还<strong>支持</strong><span style="background-color:#ffffff; color:#3c4353"><strong>创建</strong></span><span style="background-color:#ffffff; color:#3c4353"><strong>SonarQube项目</strong>、<strong>生成详细报告</strong>以及<strong>导入问题项到禅道Bug</strong>等功能</span>。</p> 
<p><strong>16.4版本给大家带来的功能改进主要包括：</strong></p> 
<ul> 
 <li>禅道支持导入Jira数据，<span>免费为广大Jira用户提供新的平台和管理工具</span>。</li> 
 <li>支持<span style="background-color:#ffffff; color:#3c4353">SonarQube项目的维护和管理，让代码检测和问题管理更加高效便捷。</span></li> 
 <li>优化GitLab相关细节，用户体验更加友好。</li> 
</ul> 
<p>欢迎大家下载升级。</p> 
<h3>一、修改记录</h3> 
<p><strong>完成的需求</strong></p> 
<p>30526 实现Jira数据导入到禅道功能<br> 30675 优化禅道中SonarQube的扫描结果详情页面<br> 30583 SonarQube免登录探针需求<br> 30576 在禅道中当对应的GitLab项目的代码库为空时，隐藏GitLab项目下关于分支与标签操作的按钮。<br> 30559 在禅道中设置GitLab项目或群组权限为公开时给予告警提示<br> 30558 实现GitLab群组URL可点击的功能<br> 30556 GitLab服务器列表中地址可点击<br> 30554 修改GitLab服务器列表“GitLab名称”为“GitLab服务器”<br> 30553 在禅道中实现创建GitLab服务器时对当前GitLab版本进行兼容性检查功能<br> 30552 在禅道中针对无权限用户将合并请求编辑按钮置灰<br> 30461 实现在禅道中将SonarQube问题转成禅道Bug的功能<br> 30455 实现SonarQube问题详情页面<br> 30453 实现SonarQube问题列表页面的搜索功能<br> 30451 实现SonarQube问题列表页面的返回功能<br> 30447 在SonarQube扫描报告概要页面添加问题详情列表的入口<br> 30443 实现在添加/编辑SonarQube服务器时验证填写用户是否为SonarQube管理员的功能<br> 30183 实现从禅道SonarQube项目列表查看SonarQube代码检查结果的入口<br> 29859 实现禅道中创建SonarQube项目功能<br> 29241 实现构建通知发送到喧喧功能<br> 29228 实现SonarQube项目问题列表页面</p> 
<p><strong>修复的Bug</strong></p> 
<p>18816 DevOps-代码中，GitLab类型的版本库代码内容未显示完全<br> 18382 代码页面版本列版本号显示不一致<br> 18380 历史记录中重复显示多条记录<br> 18104 VS Code COMMIT_EDITMSG文件中应只显示未选中的需求/Bug/任务<br> 18076 VS Code中查看项目/执行下的需求时应跳转到项目/执行下的需求详情页<br> 17869 VS code中查看需求、任务和Bug提示“请求后端出错”<br> 17851 <span>VS code</span>查看执行下的需求，提示先选择项目</p> 
<h3><span style="color:inherit">二、下载链接</span></h3> 
<table class="table table-kindeditor" style="width:100%"> 
 <tbody> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px">安装包下载</td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.zip" target="_blank">源码包</a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px">Windows 一键安装包</td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.win64.exe" target="_blank">64位</a>    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.win32.exe" target="_blank">32位</a>   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.old.exe" target="_blank">未加安全设置版</a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"> <p>Linux 一键安装包</p> <p>（适用于Ubuntu17+，centos7.x）</p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.zbox_64.tar.gz" target="_blank">64位</a>    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.zbox_32.tar.gz" target="_blank">32位</a></td> 
   <td colspan="1" rowspan="2" style="border-color:#dddddd; border-style:solid; border-width:1px"><span style="color:#e53333">注：Linux 一键安装包必须直接解压到 /opt 目录下。</span></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"> <p>低版本 Linux 一键安装包</p> <p>（适用于ubuntu16及以下版本、centos7.3及以下版本）</p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.zbox_old.64.tar.gz" target="_blank">64位</a>    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS.16.4.zbox_old.32.tar.gz" target="_blank">32位</a></p> </td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><span>DEB包下载：可以通过dpkg包管理器在Ubuntu和Debian系统下安装</span></td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2FZenTaoPMS_16.4_1_all.deb" target="_blank">官方下载源</a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><span>RPM包下载：可以通过rpm包管理器在Centos系统下安装</span></td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F16.4%2Fzentaopms-16.4-1.noarch.rpm" target="_blank">官方下载源</a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><span>最新版禅道客户端下载链接</span></td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F5.0.2%2Fzentaoclient.win64.zip" target="_blank">Windows64位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F5.0.2%2Fzentaoclient.linux64.zip" target="_blank">Linux64位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F5.0.2%2Fzentaoclient.mac64.zip" target="_blank">Mac</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F5.0.2%2Fzentaoclient.win32.zip" target="_blank">Windows32位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F5.0.2%2Fzentaoclient.linux32.zip" target="_blank">Linux32位</a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><span>最新版禅道客户端服务器下载链接</span></td> 
   <td colspan="2" rowspan="1" style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F5.0.2%2Fxxd.5.0.2.win64.zip" target="_blank">Windows64位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F5.0.2%2Fxxd.5.0.2.linux.x64.tar.gz" target="_blank">Linux64位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F5.0.2%2Fxxd.5.0.2.mac.tar.gz" target="_blank">Mac</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F5.0.2%2Fxxd.5.0.2.win32.zip" target="_blank">Windows32位</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F5.0.2%2Fxxd.5.0.2.linux.ia32.tar.gz" target="_blank">Linux32位</a></td> 
  </tr> 
 </tbody> 
</table> 
<h4><span style="color:inherit"><span style="color:inherit"><span style="color:#e53333">Docker镜像:</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Feasysoft%2Fzentao%2Ftags" target="_blank">点击这里</a></span></span></h4> 
<h3><span style="color:inherit">三、帮助手册</span></h3> 
<h4>安装升级</h4> 
<p>安装文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.zentao.net%2Fbook%2Fzentaopmshelp%2F40.html" target="_blank">https://www.zentao.net/book/zentaopmshelp/40.html</a></p> 
<p>升级文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.zentao.net%2Fbook%2Fzentaoprohelp%2F41.html" target="_blank">https://www.zentao.net/book/zentaoprohelp/41.html</a></p> 
<h4>导入集成</h4> 
<p>导入Jira数据文档：<a href="https://www.oschina.net/book/extra/656.html" target="_blank">https://www.zentao.net/book/extra/656.html</a></p> 
<p>集成SonarQube文档：<a href="https://www.oschina.net/book/extra/653.html" target="_blank">https://www.zentao.net/book/extra/653.html</a></p> 
<h3><span style="color:inherit">四、功能截图</span></h3> 
<p>后台-导入Jira<strong><span style="color:#e53333">（需要超级管理员权限，并且PHP版本大于等于5.6）</span></strong></p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202202/f_3524f7cad3e46a63b223975daa7ae18d&t=png&o=&s=&v=1644894005" referrerpolicy="no-referrer"></p> 
<p>从数据库导入</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202202/f_27e17b1398346d87256c5e15aa1e1336&t=png&o=&s=&v=1644894005" referrerpolicy="no-referrer"></p> 
<p>创建SonarQube项目</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202202/f_ac28881bfffbae66907632caf190f730&t=png&o=&s=&v=1644894005" referrerpolicy="no-referrer"></p> 
<p>SonarQube报告页面</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202202/f_01427c4b328a46656bb22ff12cef7c29&t=png&o=&s=&v=1644894005" referrerpolicy="no-referrer"></p> 
<p>SonarQube问题列表页面</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202202/f_957a5f0e5527bddd081f057eec71e72f&t=png&o=&s=&v=1644894005" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            