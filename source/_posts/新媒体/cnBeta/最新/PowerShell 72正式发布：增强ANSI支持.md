
---
title: 'PowerShell 7.2正式发布：增强ANSI支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1109/105c6d601fe70c3.jpg'
author: cnBeta
comments: false
date: Tue, 09 Nov 2021 01:53:08 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1109/105c6d601fe70c3.jpg'
---

<div>   
<strong>今天，<a href="https://devblogs.microsoft.com/powershell/general-availability-of-powershell-7-2/" target="_blank">PowerShell 7.2 正式发布</a>。该版本建立在 .NET 6 基础上，包括许多性能改进、错误修复和新的 API。</strong>该版本是偶数次要版本，将作为长期支持（LTS）发布，为期 3 年。而奇数版本只获得 1 年的支持。
微软现在将继续开发 PowerShell 7.3，将在 2022 年第 1 季度发布。<br>
 <p style="text-align: left;">PowerShell 7.2 更新内容</p><p style="text-align: left;"><strong>● 支持 Microsoft Update</strong></p><p style="text-align: left;">PowerShell 7.2 与 Microsoft Update 集成，每当<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>有一个服务版本，其中只包括关键的错误修复或安全更新，就会自动保持 7.2 的安装更新。</p><p style="text-align: left;">MSI 安装程序将自动启用更新 PowerShell 7 以及启用 Microsoft Update。如果你喜欢自己手动更新 PowerShell 7，你可以在安装时选择退出自动更新。</p><p style="text-align: left;">对于 Microsoft Update，微软继续有预览版和稳定版两个渠道（你可以同时使用这两个渠道）。因此，如果你安装了 7.2 的预览版并启用了 Microsoft Update，那么一旦有了 7.3预览版，你就会被更新到7.3预览版。</p><p style="text-align: left;">你需要单独安装 7.2 GA，以便为微软的稳定渠道启用 Microsoft Update，如果微软有一个服务版本，你将被更新到 7.2.1，并最终更新到 7.3 GA。</p><p style="text-align: left;"><strong>● 增强 ANSI 支持</strong></p><p style="text-align: left;">ANSI 转义序列是在控制台和支持的终端之间提供文本装饰支持（包括终端的其他功能）的一种行业标准方式。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1109/105c6d601fe70c3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1109/105c6d601fe70c3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">使用这些装饰是命令行工具和外壳突出显示或区分信息的一种常见方式。例如，7.2中的一个新功能是在使用表格或列表视图时对元数据与数据使用不同的颜色。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1109/dfab607fb4ae845.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1109/dfab607fb4ae845.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在7.2中，微软增加了一个新的内置变量，称为 $PSStyle，以便于向你的脚本或cmdlets添加装饰，以及控制ANSI转义序列的使用。你可以用它来添加着色、斜体、背景颜色等，由于它是一个变量，你可以使用Tab-completion来发现你可以做什么。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1109/cc4f0fc066cb253.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1109/cc4f0fc066cb253.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>● 使用 PSReadLine 的预测性直观提示</strong></p><p style="text-align: left;">这是 PSReadLine 2.1 中的一个功能，它与 PowerShell 7.2 一起出厂。为了使交互式控制台更有效率，特别是重复性的任务，微软增加了一个功能，使用你的历史记录来预测你可能要输入的内容。这项功能必须启用，你还可以自定义预测文本使用的颜色。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1109/cde28d56048fd38.webp" alt="ezgif.com-gif-maker(1).webp" referrerpolicy="no-referrer"></p><p style="text-align: left;"><strong>● 其他改进</strong></p><p style="text-align: left;">有许多错误的修复和小的改进，其中有一些来自社区！你可以在微软的博客上看到详细的内容。你可以在微软的更新日志中阅读细节，或者在微软的新文档中阅读摘要。</p>   
</div>
            