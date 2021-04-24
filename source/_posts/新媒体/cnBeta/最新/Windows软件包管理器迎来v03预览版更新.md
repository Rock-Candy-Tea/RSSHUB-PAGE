
---
title: 'Windows软件包管理器迎来v0.3预览版更新'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0424/cf0dd76096d37ed.jpg'
author: cnBeta
comments: false
date: Sat, 24 Apr 2021 03:36:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0424/cf0dd76096d37ed.jpg'
---

<div>   
<strong>微软刚刚向喜欢尝鲜的朋友发布了 Windows 软件包管理器（winget）的 v0.3 预览版本，其中引入了诸多实用的附加功能。</strong>比如 winget 能够获取已安装软件的列表，以便用户能够在新 PC 上开展快速安装和配置。有趣的是，导入功能是默认启用的，但导出功能仍处于实验性阶段。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0424/cf0dd76096d37ed.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>想要启用 winget 的已安装软件列表导出功能，你需要执行 winget settings 命令，并将之添加到打开的 JSON 文件中：</p><blockquote><p>"experimentalFeatures": &#123;</p><p>"export": true</p><p>&#125;,</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/0424/4e9f03b65f5c468.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0424/4e9f03b65f5c468.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>启用之后，你可将当前程序列表导出到一个 JSON 文件中 —— 使用 <strong>winget export [filename].json</strong> 命令，且允许给它重命名（替换 [filename] 字段即可）。</p><p>在将文件复制到另一台计算机上后，可使用 <strong>winget import [filename] .json</strong> 命令将其导入，然后 winget 就会自动安装列表中提到的所有软件包。</p><p><img src="https://static.cnbetacdn.com/article/2021/0424/a38c17a0d7d816a.png" alt="2.png" referrerpolicy="no-referrer"></p><p>本次跟新的另一项变化，就是支持组策略管理，意味着 IT 管理员能够更轻松地对 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 软件包管理器的使用进行规划。</p><p>虽然大多数内容都涉及实验性功能，但仍有一些值得注意的地方。感兴趣的朋友，可从 <a href="https://github.com/microsoft/winget-cli/releases" target="_self">GitHub</a> 上获取可导入相关策略的 .admx 和 .adml 文件。</p><p><img src="https://static.cnbetacdn.com/article/2021/0424/6cf40cae7834aec.png" alt="3.png" referrerpolicy="no-referrer"></p><p><strong>其它功能介绍：</strong>（完整内容详见 <a href="https://github.com/microsoft/winget-cli/blob/master/doc/Settings.md" target="_self">GitHub</a> 主页）</p><blockquote><p>（1）winget list：可显示 PC 上已安装的所有软件包，包括 Microoft Store 和用户通过其它方式安装的完整应用程序。如不在 winget 存储库中，则会看到错误提示。</p><p>（2）winget update [package name]：此命令可快速更新已安装的软件包。</p><p>（3）winget uninstall [package name]：今年早些时候介绍过的卸载功能，无论最初是否通过 winget 执行的安装，现都可以将相应的应用程序卸载掉。</p></blockquote>   
</div>
            