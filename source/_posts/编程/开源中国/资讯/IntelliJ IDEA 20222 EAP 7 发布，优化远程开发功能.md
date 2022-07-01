
---
title: 'IntelliJ IDEA 2022.2 EAP 7 发布，优化远程开发功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4f868b89aaec18e898914cea3ffbebac815.gif'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 07:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4f868b89aaec18e898914cea3ffbebac815.gif'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.2 的第七个 EAP 版本已上线，此版本主要对远程开发功能进行了更新。</p> 
<p>远程开发在 2021.1.3 版本中作为 IntelliJ IDEA Ultimate 中的 beta 功能发布，远程开发功能将 IDE 拆分为本地和远程组件，IDE 本身作为后端服务安装在远程服务器上用于加载项目。同时瘦客户端（thin client）在本地运行并提供完整的工作 UI。这两个组件通过 SSH 连接，在远程服务器进行繁重任务的处理，进而提供流畅的本地体验。 关于远程开发的更多内容可查看 JetBrains 中国的<a href="https://my.oschina.net/u/5494143/blog/5332935">博客 </a>。</p> 
<h2>JetBrains 网关 </h2> 
<p>所有远程开发更新都可以通过捆绑的远程开发功能以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fremote-development%2Fgateway%2F" target="_blank">JetBrains Gateway</a> 访问，JetBrains Gateway 是一个独立的应用程序，可作为所有远程开发环境的单一入口点。 </p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>卸载后端 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过此构建可以卸载任何过时的 IDE 后端，只需按照以下步骤操作：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ol> 
 <li>在<em><strong>最近的项目</strong> </em>屏幕上，单击<em><strong>管理 IDE</strong> </em>按钮。</li> 
 <li>在这里可以找到当前安装的 IDE 的列表。</li> 
 <li>选择要删除的 IDE 并确认选择。</li> 
</ol> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-4f868b89aaec18e898914cea3ffbebac815.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>欢迎屏幕 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本更新了欢迎屏幕。在这里可以选择你心仪的后端编排方法：可以手动配置服务器或选择具有现成开发环境的提供商，例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fspace%2F2022%2F01%2F12%2Fa-deep-dive-into-space-dev-environments%2F" target="_blank">Space</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fblog%2F2022%2F04%2F28%2Fjetbrains_partners_with_gitpod%2F" target="_blank">Gitpod</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-d934212e29e3744ff3d922f63adf6b78e84.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他质量改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FGTW-1123" target="_blank">最近的项目 - GTW-1123</a> 始终显示主机状态。</li> 
 <li>支持 CSH 和 TCSH 作为远程主机的登录 shell – <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FGTW-747" target="_blank">GTW-747</a>。</li> 
 <li>如果禁用 SFTP 或 SFTP 路径非标准 - <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FGTW-870%2FDeploy-fails-if-no-SFTP-on-backend-or-non-standard-path" target="_blank">GTW-870</a> ，部署不会失败。</li> 
</ul> 
<h2>JetBrains 客户端 </h2> 
<h3>VCS 注释</h3> 
<p>此版本在 JetBrains Client 的装订线菜单中添加了 VCS 注释，这个改进允许开发人员在远程开发时直接在瘦客户端上跟踪项目更改，可以找出谁对代码进行了更改，查看提交之间的差异，并浏览项目历史记录。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-848ccc7daeb0f18ec07ca177ecf986d23e0.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Gradle</h3> 
<p>此版本修复 Gradle 工具窗口中的一个问题，现在可以在选择任务树的根节点时查看构建日志 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FCWM-4416" target="_blank">CWM-4416</a> )。最重要的是，点击停止按钮将正确停止构建 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FCWM-3734" target="_blank">CWM-3734</a> )。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-7bad69da61fee4bddbc17add31d1ac0fb17.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>GitHub</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>此版本添加了一些修复，可以在远程开发时无缝登录 GitHub 帐户。在 JetBrains Client 中打开<em>Settings ，然后选择 </em><em>Version Control</em> | <em>GitHub</em> | <em>添加帐户 </em>即可加入 GitHub 帐户。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-78d7faa7d2e464d1da2b3b59c070c301da4.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>终端 - Terminal</h2> 
<p>大部分终端升级都围绕改进瘦客户端和 IDE 后端之间的连接，目标是使远程开发体验与本地开发一样流畅。</p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>端口转发 - </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Port forwarding </h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>端口转发功能可用于终端上运行的进程。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-6e1e3597ab27fb0cffa6562aa67a742de1d.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start">此外，<span style="background-color:#ffffff; color:#27282c">关闭远程会话时，PowerShell、Bash 和 Zsh 等终端进程将终止。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="margin-left:0; margin-right:0; text-align:start">有关此版本中包含的完整更改列表，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F06%2Fintellij-idea-2022-2-eap-7%2F" target="_blank">发布博客</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-221%2FIntelliJ-IDEA-20222-EAP-7-22232444-build-Release-Notes" target="_blank">发行说明</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            