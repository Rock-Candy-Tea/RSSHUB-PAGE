
---
title: 'Redmine 5.0.0 发布，项目管理与缺陷跟踪管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4271'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 23:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4271'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redmine 是一个网页界面的项目管理与缺陷跟踪管理系统的自由及开放源代码软件工具。它集成了项目管理所需的各项功能：日历、燃尽图和甘特图以协助可视化表现项目与时间限制，问题跟踪和版本控制。此外，Redmine也可以同时处理多个项目。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redmine 5.0.0  版本包含 143 项更新，新增多项新特性和多个漏洞修复。</p> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[账户/认证]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F30998" target="_blank">#30998</a>：添加 rake 任务，以在一定天数后清理注册用户</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F31920" target="_blank">#31920</a>：仅对某些用户组需要 2FA 验证</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F33345" target="_blank">#33345</a>：在 LDAP 连接错误消息中包含身份验证方法名称</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35001" target="_blank">#35001</a>：当为用户启用双因素身份验证时，使用用户名和密码禁用 API 身份验证</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35439" target="_blank">#35439</a>：仅对具有管理权限的用户要求 2FA 的选项</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36825" target="_blank">#36825</a>：将电子邮件地址长度限制从 60 增加到 254</li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[行政]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35421" target="_blank">#35421</a>：在 configuration.yml 中检测到 YAML 语法错误时未处理的异常</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F32116" target="_blank">#32116</a>：将配置的主题添加到 Redmine::Info</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35562" target="_blank">#35562</a>：当有挂起的迁移时，在 admin/info 中显示警告</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35934" target="_blank">#35934</a>：在管理的用户列表中显示 2FA 状态，并带有过滤选项</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36391" target="_blank">#36391</a>：将“时间跨度格式”的默认值从“十进制”更改为“分钟”</li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[附件]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35539" target="_blank">#35539</a>：Attachment.disk_filename 中的竞争条件（可能的文件名冲突）</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F32898" target="_blank">#32898</a>：Windows 上的 PDF 缩略图支持</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35462" target="_blank">#35462</a>：下载日记中的所有附件</li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[代码清理/重构]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F31132" target="_blank">#31132</a>：删除未使用的列 trackers.is_in_chlog</li> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36149" target="_blank">#36149</a>：列表扩展器图标的 CSS 类中的错字</li> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36361" target="_blank">#36361</a>：IssueRelationsControllerTest#test_bulk_create_should_show_errors 随机失败</li> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36394" target="_blank">#36394</a>：避免在 MailHandlerController 之外传递 ActionController::Parameters</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F34337" target="_blank">#34337</a>：删除 jQuery 迁移</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35259" target="_blank">#35259</a>：将测试覆盖率报告输出到控制台</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35671" target="_blank">#35671</a>：将问题显示视图的子任务部分移动到单独的部分</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F15118" target="_blank">#15118</a>：弃用并将 rss_* 方法重命名为 atom_* 方法</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F31035" target="_blank">#31035</a>：删除 ActionMailer::LogSubscriber#deliver 的重新定义，由于删除了 Setting.bcc_recipients，因此不再需要重新定义</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F32922" target="_blank">#32922</a>：重新加载分离的附件</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F33079" target="_blank">#33079</a>：从 Redmine::Helpers::TimeReport 中删除未使用的参数</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F33337" target="_blank">#33337</a>：清理工作流控制器</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F34976" target="_blank">#34976</a>：将缺少的夹具添加到 TimeEntryCustomFieldTest</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35024" target="_blank">#35024</a>：由于“/”路径分隔符，Windows 中的系统测试失败</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35026" target="_blank">#35026</a>：删除 rake 任务 check_parsing_by_psych</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35031" target="_blank">#35031</a>：删除应该在 Redmine 5 中删除的已弃用代码</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35075" target="_blank">#35075</a>：在基本布局和帐户侧边栏中使用命名路由</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35076" target="_blank">#35076</a>：菜单管理器 - 从命名空间控制器呈现时生成正确的 URL</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35208" target="_blank">#35208</a>：使用 `Time.use_zone` 而不是 `Time.zone=`</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35230" target="_blank">#35230</a>：修复 ApplicationHelper.html_title 注释中的错字</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35396" target="_blank">#35396</a>：使用 base_scope 获取问题查询结果</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35466" target="_blank">#35466</a>：将 test/fixtures/configuration/*.yml.example 重命名为 test/fixtures/files/configuration/*.yml</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35610" target="_blank">#35610</a>：从项目设置中删除 Wiki 选项卡后的清理 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F26579" target="_blank">#26579</a> )</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35727" target="_blank">#35727</a>：将缺少的固定装置添加到 Redmine::ProjectJumpBoxTest</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35773" target="_blank">#35773</a>：将版本索引视图（路线图）上的侧边栏内容移动到单独的部分</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35952" target="_blank">#35952</a>：在测试套件中明确指定文本格式</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35975" target="_blank">#</a> 35975：将缺少的夹具添加到 UserTest</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36005" target="_blank">#36005</a>：采用 2FA 电子邮件到新的 Mailer 界面</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36241" target="_blank">#36241</a>：MenuManagerTest 随机失败</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36347" target="_blank">#36347</a>：将缺少的夹具添加到 IssuesHelperTest</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36358" target="_blank">#36358</a>：使用 File.exist？，而不是弃用的 File.exists？</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36379" target="_blank">#36379</a>：将源文件中的版权年份更新为 2022</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36716" target="_blank">#36716</a>：IssueControllerTest 随机失败</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36730" target="_blank">#36730</a>：将 Member.find_or_new 替换为 ActiveRecord 的 find_or_initialize_by</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36770" target="_blank">#36770</a>：修复在迁移中使用正确的异常类 ActiveRecord::IrreversibleMigration</li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[自定义字段]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>缺陷<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F32977" target="_blank">#32977</a>：从“用户”格式自定义字段中删除对已删除用户的引用</li> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F14275" target="_blank">#14275</a>：向自定义字段添加提示</li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0; text-align:start"><span><span><span style="color:#606060"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[数据库]</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F35073" target="_blank">#35073</a>：在 LIKE 语句中转义值以防止注入占位符（_ 或 %）</li> 
 <li>补丁<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fissues%2F36416" target="_blank">#36416</a>：在项目删除时清理更多依赖对象</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#606060">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redmine.org%2Fprojects%2Fredmine%2Fwiki%2FChangelog_5_0" target="_blank">https://www.redmine.org/projects/redmine/wiki/Changelog_5_0</a></p>
                                        </div>
                                      
</div>
            