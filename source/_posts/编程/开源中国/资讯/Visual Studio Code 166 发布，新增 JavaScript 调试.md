
---
title: 'Visual Studio Code 1.66 发布，新增 JavaScript 调试'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8b686f3506c1dc60e61cf9f9d2c5c7c26b8.gif'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 07:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8b686f3506c1dc60e61cf9f9d2c5c7c26b8.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Visual Studio Code 1.66<span> </span></span>现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_66" target="_blank">已发布</a><span style="background-color:#ffffff; color:#333333">，该版本更新内容很多，下面摘录部分新特性作介绍：</span></p> 
<h2><strong style="color:#444444"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_66%23_local-history" target="_blank">本地历史记录</a></strong></h2> 
<p>可以在<strong style="color:#444444">时间轴</strong>视图中使用文件的本地历史记录，<span style="background-color:#ffffff; color:#444444">独立于源代码控制跟踪本地文件更改</span>。根据配置的设置，每次保存编辑器时，都会在列表中添加一个新条目：</p> 
<p><img alt height="416" src="https://oscimg.oschina.net/oscnet/up-8b686f3506c1dc60e61cf9f9d2c5c7c26b8.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#444444">每个本地历史的条目都包含创建条目时文件的全部内容，</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从条目中可以：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>将更改与本地文件或以前的条目进行比较。</li> 
 <li>还原内容。</li> 
 <li>删除或重命名条目。</li> 
</ul> 
<h3 style="text-align:start">设置编辑器</h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>语言过滤器</strong></p> 
<ul> 
 <li style="text-align:start">现在可以在设置编辑器搜索框中键入 @lang:languageId ，来查看和编辑对应语言配置的所有设置。</li> 
 <li style="text-align:start">查看特定于语言的设置也称为语言覆盖，这些覆盖将一直保持配置，直到通过单击齿轮图标并重置设置来明确重置。</li> 
 <li style="text-align:start">下图演示了将语言过滤器设置为 @lang:css ，以显示所有可能的 CSS 语言覆盖设置。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-69c97a18cbf0127ba428a7df2a8a5100371.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong style="color:#444444">工作区和文件夹设置保存</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#444444">设置编辑器中的工作区和文件夹设置现在会保留，直到用户手动重置。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>以前，用户必须打开工作区设置 JSON 文件才能设置此值，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>在设置编辑器工作区</strong>选项卡中设置编辑器选项卡大小下方，它会自动添加到工作区的<code>settings.json</code>文件中。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt src="https://oscimg.oschina.net/oscnet/up-fd99c0d8d989c279cb13120cc714d51a4de.gif" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start">终端</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>显示所有找到的匹配项</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#444444">在终端中搜索时，搜索词的所有实例都将突出显示。可以通过以 terminal.findMatch 为前缀的颜色自定义命令来微调突出显示的高亮颜色。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#444444"><img alt height="613" src="https://oscimg.oschina.net/oscnet/up-12ef3f2cb3b9144d55bb117a7bc03f303ac.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h3 style="text-align:start">滚动条注释</h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>终端的滚动条中加入注释，以指示每个重要的节点。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>例如，查找的结果在滚动条中有相应的注释：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="448" src="https://oscimg.oschina.net/oscnet/up-dab85c1916ea18dc827213df1121782cb0b.png" width="350" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start">调试</h2> 
<h3 style="text-align:start">JavaScript 调试</h3> 
<p>JavaScript 调试器现在支持收集和可视化堆配置文件，堆配置文件允许查看随时间分配的内存位置和数量。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="410" src="https://oscimg.oschina.net/oscnet/up-403d463296351ec9b882d0d73d5dc3cd3ff.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>语言</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>CSS 格式化程序</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>内置的 CSS 扩展附带一个格式化程序，格式化程序适用于 CSS、LESS 和 SCSS。由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbeautify-web%2Fjs-beautify" target="_blank">JS Beautify 库</a>实现，并带有以下设置：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><code>css.format.enable</code>- 启用/禁用默认 CSS 格式化程序。</li> 
 <li><code>css.format.newlineBetweenRules</code>- 用空行分隔规则集。</li> 
 <li><code>css.format.newlineBetweenSelectors</code>- 用新行分隔选择器。</li> 
 <li><code>css.format.spaceAroundSelectorSeparator</code>- 确保选择器分隔符“>”、“+”、“~”周围有空格字符（例如，<code>a > b</code>）。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code>less</code> 和 <code>scss</code> 也存在相同的设置。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="text-align:start">HTML 中的 JavaScript 语义突出显示</h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>该版本将 HTML 文件中 JavaScript 源代码的语义突出显示，与普通<code>.js</code>文件中看到的内容对齐。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>此举不仅使代码颜色更加一致，还添加了一些以前缺少的重要语义信息，例如突出显示只读类型。</p> 
<h2 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用于 Web 的 VS Code</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3>支持拖放文件</h3> 
<p>可以将本地文件和文件夹拖放到在 vscode.dev 或 insiders.vscode.dev 上打开的浏览器窗口中，以访问具体内容。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d82605c5683c79dfb4006c0eb892254c93c.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>VS Code 中的 R 语言</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>一个新的 R 语言主题描述了 VS Code 中带有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DIkuyadeu.r" target="_blank">R 扩展的</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.r-project.org%2F" target="_blank">R 编程语言</a>支持。R 扩展包括丰富的语言功能，例如代码完成和 linting，以及集成的 R 终端和专用的工作区、数据和绘图查看器。</p> 
<p><img alt height="214" src="https://oscimg.oschina.net/oscnet/up-a4fbaba3a50888b053fde18d65b51b7357d.png" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>该版本还包含更多更新内容，由于篇幅原因不一一介绍，可在微软<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_66" target="_blank">博客原文</a>中查看。</p> 
<p> </p>
                                        </div>
                                      
</div>
            