
---
title: 'Jenkins 2.296 发布，Java 编写的持续集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1984'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1984'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jenkins 是一款由 Java 编写的开源的持续集成工具。Jenkins 提供了软件开发的持续集成服务。它运行在 Servlet 容器中（例如 Apache Tomcat）。它支持软件配置管理（SCM）工具（包括 AccuRev SCM、CVS、Subversion、Git、Perforce、Clearcase 和 RTC），可以执行基于 Apache Ant 和 Apache Maven 的项目，以及任意的 Shell 脚本和 Windows 批处理命令。Jenkins 是在 MIT 许可证下发布的自由软件。</p> 
<p>Jenkins 2.296 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>修复任何浏览器中不需要的表单验证造成的表单提交回归问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.jenkins.io%2Fbrowse%2FJENKINS-65585" target="_blank">issue 65585</a>)</li> 
 <li>建议在 Java 11 上运行 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.jenkins.io%2Fbrowse%2FJENKINS-65577" target="_blank">issue 65577</a>)</li> 
 <li>将数字字段的错误信息中的 "数字" 改为 "整数" (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5538" target="_blank">pull 5538</a>)</li> 
 <li>显示隐含的插件依赖性或从核心拆分的插件的依赖性计数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5472" target="_blank">pull 5472</a>)</li> 
 <li>将 spring-security-bom 从 5.4.6 升级至 5.5.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5505" target="_blank">pull 5505</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Freleases%2Ftag%2F5.5.0" target="_blank">Spring project spring-security 5.5.0 release notes</a>)</li> 
 <li>Winstone 5.18：将 Jetty 从 9.4.40.v20210413 更新到 9.4.41.v20210516，以修复错误和增强功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5540" target="_blank">pull 5540</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fwinstone%2Freleases%2Ftag%2Fwinstone-5.18" target="_blank">Winstone 5.18 changelog</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feclipse%2Fjetty.project%2Freleases%2Ftag%2F9.4.41.v20210516" target="_blank">Jetty 9.4.41 changelog</a>)</li> 
 <li>一个特殊的、很少遇到的内部错误现在再次正确地显示了原因的细节 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5537" target="_blank">pull 5537</a>)</li> 
 <li>改进了登录页面中的复选框的对比度 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5536" target="_blank">pull 5536</a>)</li> 
 <li>Jenkins 在登录后将用户重定向到前一个页面，即使他们在未登录时能够查看该页面 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.jenkins.io%2Fbrowse%2FJENKINS-64991" target="_blank">issue 64991</a>)</li> 
 <li>开发者： <code>View</code> 现在是 <code>DescriptorByNameOwner</code>，允许其作为 <code>AncestorInPath</code> 使用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5533" target="_blank">pull 5533</a>)</li> 
 <li>开发者：依赖 <code>hudson.model.Queue$Item#id</code> 或 <code>hudson.model.AbstractProject#triggers</code> 字段的插件必须更新以调用相应的 getters (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5526" target="_blank">pull 5526</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jenkins.io%2Fvertx%2F" target="_blank">Vertx plugin</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jenkins.io%2Fslave-prerequisites%2F" target="_blank">Slave Prerequisites plugin</a>)</li> 
 <li>开发者：从 Jenkins 核心删除 JTidy 依赖。使用 JTidy 功能的插件必须更新，以明确声明对 JTidy 的依赖，而不是依赖 Jenkins 核心来提供这个库 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5521" target="_blank">pull 5521</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jenkins.io%2Fnis-notification-lamp%2F" target="_blank">NIS notification lamp plugin</a>)</li> 
 <li>移除部分阿拉伯语和葡萄牙语翻译 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5518" target="_blank">pull 5518</a>)</li> 
 <li>从 Remoting 4.8 升级到 Remoting 4.9，修正了错误并更新了依赖关系 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fjenkins%2Fpull%2F5539" target="_blank">pull 5539</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjenkinsci%2Fremoting%2Freleases%2Ftag%2Fremoting-4.9" target="_blank">Remoting 4.9 changelog</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jenkins.io%2Fchangelog%2F%2F%23v2.296" target="_blank">https://www.jenkins.io/changelog//#v2.296</a></p>
                                        </div>
                                      
</div>
            