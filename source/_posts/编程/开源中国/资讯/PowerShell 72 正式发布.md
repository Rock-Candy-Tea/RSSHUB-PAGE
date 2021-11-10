
---
title: 'PowerShell 7.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1110/070804_wNCN_4937141.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 07:32:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1110/070804_wNCN_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>微软昨天正式发布 PowerShell 7.2。这个版本继续延续此前的策略，即偶数次要版本长期支持（LTS），奇数次要版本将拥有 1 年的支持周期。这就表示 7.2 版本将获得 3 年支持。</p> 
<p>这个版本建立在 .NET 6 基础之上，这意味着该版本包括许多性能改进、错误修复和新的 API。</p> 
<h3>支持 Microsoft Update</h3> 
<p>如上所述，PowerShell 已与 Microsoft Update 整合。MSI 安装程序将自动启用更新 PowerShell 7，以及启用 Microsoft Update。你也可以手动更改选项以实现手动更新 PowerShell 7。</p> 
<p>对于 Microsoft Update，将继续保留预览版和稳定版两个渠道（你可以同时使用这两个渠道）。</p> 
<h3>增强的 ANSI 支持</h3> 
<p>ANSI 转义序列是在控制台和支持的终端之间提供文本装饰支持（包括终端的其他功能）的一种行业标准方式。</p> 
<p>使用这些装饰是命令行工具和 Shell 突出显示或区分信息的一种常见方式。例如，7.2 中的一个新功能是在使用表格或列表视图时对元数据与数据使用不同的颜色。</p> 
<p><img alt height="653" src="https://static.oschina.net/uploads/space/2021/1110/070804_wNCN_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>在 7.2 中，增加了一个新的内置变量，叫做 <span data-darkreader-inline-bgcolor style="--darkreader-inline-bgcolor:rgba(96, 104, 108, 0.15); background-color:rgba(135, 131, 120, 0.15)">$PSStyle</span>，以便于为你的脚本或 cmdlets 添加装饰，以及控制 ANSI 转义序列的使用。你可以用它来添加着色、斜体、背景颜色等，由于它是一个变量，你可以使用 Tab-completion 来发现你可以做什么。</p> 
<p>任何定制都需要存储在你的 <code>$Profile</code> 中才能保留。</p> 
<h3>PSReadLine 的预测性提示</h3> 
<p>这是 PSReadLine 2.1 中的一个功能，它随 PowerShell 7.2 一同推出。该功能可以使交互式控制台更有效率，特别是重复性的任务，PSReadLine 2.1 可以使用你的历史记录来预测可能输入的内容。这个功能强制启用，用户可以自定义预测文本的颜色。</p> 
<h3>其他改进</h3> 
<p>许多错误修复和小的改进，更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases" target="_blank">https://github.com/PowerShell/PowerShell/releases</a></p>
                                        </div>
                                      
</div>
            