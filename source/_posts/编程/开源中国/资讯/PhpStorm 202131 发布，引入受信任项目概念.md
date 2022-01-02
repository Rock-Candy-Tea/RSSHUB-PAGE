
---
title: 'PhpStorm 2021.3.1 发布，引入受信任项目概念'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1a2c8a70ac70b2b04f66b7f3f80585a2bd3.png'
author: 开源中国
comments: false
date: Sun, 02 Jan 2022 07:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1a2c8a70ac70b2b04f66b7f3f80585a2bd3.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#27282c">PhpStorm 2021.3.1 现已发布，这是 PhpStorm 2021.3 的第一个错误修复更新。</span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>除了错误修复和增强功能外，此版本还带来了一个重要的新功能：<strong>受信任项目（</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><strong><strong style="color:#27282c">trusted projects</strong><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>）。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<h4><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>受信任项目</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本引入了<strong>受信任项目</strong>的概念 ，旨在降低与处理来自未知和不受信任来源的项目相关的风险。当你打开一个项目时，PhpStorm 不会从中执行任何代码并检查它是否受信任或来自受信任的位置。如果项目当前不受信任，IDE 会要求你选择是以<strong>安全（</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><strong style="color:#27282c">safe</strong><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>）</strong>模式还是<strong>完全信任（</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><strong style="color:#27282c">full-trust</strong><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>）</strong>模式打开它 。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="241" src="https://oscimg.oschina.net/oscnet/up-1a2c8a70ac70b2b04f66b7f3f80585a2bd3.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果你在安全模式下打开项目，许多 IDE 功能（例如错误突出显示）将被禁用。但是，你仍然可以浏览项目的内容并在编辑器中打开其源文件。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="262" src="https://oscimg.oschina.net/oscnet/up-acc9283c92789f3bc2b3c6afe2330f0401e.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">IDE 还会就所有潜在的代码执行向你发出警告，包括运行 Composer 命令和刷新配置的测试框架和 PHP 命令行工具的版本。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c"><img alt height="161" src="https://oscimg.oschina.net/oscnet/up-e7f7e6b23330f427952ffa31b71755f67c8.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start">为了避免对每个项目都显示警告，PhpStorm允许你在"Preferences/Settings | Build, Execution, Deployment | Trusted Locations"下定义受信任的位置。指定为"Trusted Locations"的目录中的项目总是被认为是受信任的。为了确保只有在发生异常情况时才会出现不受信任的项目警告，建议将你通常创建项目的目录添加到受信任位置。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="139" src="https://oscimg.oschina.net/oscnet/up-ac96dd0c39ddeb456ddf07111f7b1256d4d.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start">如果你想禁用不受信任的项目警告，你可以把你机器的根目录添加到受信任的位置。但由于这有可能使你受到攻击，所以一般不建议这样做。</p> 
<p style="margin-left:0; margin-right:0; text-align:start">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2021%2F12%2Fphpstorm-2021-3-1-is-released%2F" target="_blank">查看官方博客</a></p>
                                        </div>
                                      
</div>
            