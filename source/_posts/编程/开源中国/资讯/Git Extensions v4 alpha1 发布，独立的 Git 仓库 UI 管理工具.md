
---
title: 'Git Extensions v4 alpha1 发布，独立的 Git 仓库 UI 管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7359'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7359'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Git Extensions 是一个独立的 UI 工具，用于管理 git 存储库。它还与 Windows Explorer 和 Microsoft Visual Studio 集成。Git Extensions v4 alpha1 现已发布，更新内容如下：</span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Release Notes Highlights</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>该应用程序现在需要 .NET 6</li> 
 <li>大大改善了存储库加载时间以及其他性能调整（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9243" target="_blank">#9243</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9735" target="_blank">#9735</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9864" target="_blank">#9864</a> 等）</li> 
 <li>对<code>\\wsl$</code>shares 使用 native WSL Git 可执行文件以加快处理速度 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9702" target="_blank">#9702</a> )</li> 
 <li>使用 standard<code>FormBrowse</code>来浏览 file history 和 blame（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9445" target="_blank">#9445</a>）</li> 
 <li>BASE diff: 图标的独特变化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fpull%2F9720" target="_blank">#9720</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>以下功能和选项已被删除：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>PuTTY 二进制文件不再与 Git 扩展捆绑，需单独安装 PuTTY 并更改设置中的路径。</li> 
 <li>不支持 Theming - v3.x 依赖于 EasyHook 库来促进对 theming 所需的 Windows API 的 hooks。但是，.NET 6 不支持这些 hooks 所需的 remoting 和多个 AppDomain。迄今为止，还没有找到可行的替代方案。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fissues%2F9191" target="_blank">#9191</a></li> 
 <li>删除了 TFS 集成 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fcommit%2F8190d0c0570af95ffbf9e168072d1b169eb99618" target="_blank">8190d0c</a> )</li> 
 <li>删除了 JIRA 集成（参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Fissues%2F9659" target="_blank">#9659</a>）</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgitextensions%2Fgitextensions%2Freleases%2Ftag%2Fv4-alpha1" target="_blank">https://github.com/gitextensions/gitextensions/releases/tag/v4-alpha1</a></p>
                                        </div>
                                      
</div>
            