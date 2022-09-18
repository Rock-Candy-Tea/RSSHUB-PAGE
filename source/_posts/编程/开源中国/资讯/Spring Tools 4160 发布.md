
---
title: 'Spring Tools 4.16.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=14'
author: 开源中国
comments: false
date: Sun, 18 Sep 2022 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=14'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Spring Tools 4.16.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F09%2F16%2Fspring-tools-4-16-0-released" target="_blank">发布</a>。Spring Tools 4 是由 Spring 团队打造的 Spring 开发工具，从零开始构建，融合了现代技术和开发者工具架构。它在单独的进程中运行，从构建之初就考虑到了性能问题，并且支持最新的 Spring 技术，为开发基于 Spring 的企业应用提供世界级支持。同时，全新版本的 Spring Tools 与 IDE 无关，可在各种编码环境中使用，支持 Eclipse、Visual Studio Code 与 Theia。</span></p> 
<p style="text-align:start"><strong><span><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Tools 4 for Eclipse 发行版的主要变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>更新到 Eclipse 2022-09 版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Feclipseide%2F2022-09%2F" target="_blank">新的和值得注意的</a>）</li> 
 <li>现在包括用于 ARM 上的 Linux 的新发行版（实验性）-<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fwiki%2FPrevious-Versions" target="_blank">下载地址在这里</a></li> 
 <li>m2e 2.0.5 版本包含在 Eclipse 的分发版本中</li> 
</ul> 
<p style="text-align:start"><strong><span><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>修复和改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>(Spring Boot)修复：自定义注释上的工作区符号 null ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F818" target="_blank">#818</a> )</li> 
 <li>(Spring Boot)修复：组织导入导致与语言服务器的通信问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F806" target="_blank">#806</a> )</li> 
 <li>(Spring Boot)增强：将字段注入重构为构造函数注入的快速修复操作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F522" target="_blank">#522</a> )</li> 
 <li>(Eclipse)增强：使启动支持适应新平台启用的 ansi console coloring 支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F823" target="_blank">#823</a> )</li> 
 <li>(Eclipse)修复：从错误日志中清理/删除更多条目 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F802" target="_blank">#802</a> )</li> 
 <li>(Eclipse)修复：在 Eclipse 中切换实时悬停以在启动后直接连接 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F832" target="_blank">#832</a> )</li> 
 <li>(Eclipse)修复：在启动启动配置中添加开关以启用/禁用自动实时悬停连接 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F843" target="_blank">#843</a> )</li> 
 <li>(Eclipse)修复：启动时实时悬停自动连接应检查执行器 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F842" target="_blank">#842</a> )</li> 
 <li>(Eclipse)增强：spring 工具套件 linux arm 分发（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F841" target="_blank">#841</a>）</li> 
 <li>(VSCode)修复：扩展永远不会激活，抛出错误“Header must provide a Content-Length property” ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F811" target="_blank">#811</a> )</li> 
 <li>(Concourse)修复：Concourse 扩展不知道 resource 的“check_every: never” ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F816" target="_blank">#816</a> )</li> 
 <li>(Concourse)修复：Concourse 扩展不知道 semver resource 的“depth”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F830" target="_blank">#830</a>）</li> 
 <li>(Concourse)修复：Concourse 扩展无法识别带有 docker-image resource 的“registry_mirror”的 URL ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F831" target="_blank">#831</a> )</li> 
 <li>(Concourse)修复：vscode-concourse：支持 .yml 和 .yaml 文件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F838" target="_blank">#838</a>）</li> 
 <li>(Concourse)修复：vscode-concourse：为管道和任务添加语言图标（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fsts4%2Fissues%2F839" target="_blank">#839</a>）</li> 
</ul> 
<p><span style="color:#333333">Spring Tools 4.16.1 计划于 2022 年 10 月下旬发布。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">下载地址：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Ftools%2F" target="_blank">https://spring.io/tools/</a></p> 
<div> 
 <div> 
  <div> 
   <p style="margin-left:0; margin-right:0"><span style="color:#000000">详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F09%2F16%2Fspring-tools-4-16-0-released" target="_blank">查看官方博客</a>。</span></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            