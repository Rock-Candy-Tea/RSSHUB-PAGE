
---
title: 'JetBrains 宣布：IntelliJ 平台彻底停用 Log4j 组件'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/83fa2e68-9976-4ca4-a756-cb6d238ac13b.png'
author: IT 之家
comments: false
date: Mon, 14 Feb 2022 07:57:11 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/83fa2e68-9976-4ca4-a756-cb6d238ac13b.png'
---

<div>   
<p data-vmark="741a"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 2 月 14 日消息，JetBrains 近日在官方博客宣布，<span class="accentTextColor">将从 IntelliJ 平台移除 Log4j 组件</span>，一部分原因是之前的<a href="https://www.ithome.com/0/591/592.htm" target="_blank">重大漏洞事件</a>。</p><p data-vmark="ad2f" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/83fa2e68-9976-4ca4-a756-cb6d238ac13b.png" w="1440" h="490" title="JetBrains 宣布：IntelliJ 平台彻底停用 Log4j 组件" width="1440" height="279" referrerpolicy="no-referrer"></p><p data-vmark="47c3">据介绍，基于 IntelliJ 平台的 IDE 不受此漏洞的影响，因为使用了 Log4j 1.2 的修补版本，并删除了所有与网络相关的代码。尽管如此，一些自动化安全工具仍然将安全版本的 Log4j 标记为不安全。</p><p data-vmark="b645">同时，IntelliJ 平台对日志框架的要求相当低，可以包含在作为 JDK 一部分的标准日志 API（java.util.logging）中。为了避免错误的安全警报并减少潜在的攻击面，JetBrains 决定完全停止使用 Log4j，<span class="accentTextColor">并切换到 java.util.logging 作为标准日志框架</span>。</p><p data-vmark="a129">IT之家了解到，<span class="accentTextColor">更改将在 2022.1 版本中发布</span>。由于大量第三方插件（直接或间接）使用 Log4j，JetBrains 将发布 Log4j API 的默认实现，将日志输出重定向到 java.util.logging，这一功能来自 SLF4J 项目。但是，默认实现并没有完全实现所有方法，因此为了保持插件的全部功能，开发者可能需要<a href="https://blog.jetbrains.com/platform/2022/02/removing-log4j-from-the-intellij-platform/" target="_blank">调整代码</a>以适应新环境。</p>
          
</div>
            