
---
title: '微软修复 Win11 Wi-Fi 热点问题'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/6/bd739e0b-7aa4-45e2-8ca9-dd45cf0eba71.png'
author: IT 之家
comments: false
date: Sat, 25 Jun 2022 14:48:12 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/6/bd739e0b-7aa4-45e2-8ca9-dd45cf0eba71.png'
---

<div>   
<p data-vmark="de29"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 25 日消息，上周，微软官方公告了一个新的已知问题。据微软称，该公司 6 月 14 日发布的 Windows 最新累积更新会导致 Wi-Fi 热点出现问题，主要出现在 OS 内部版本 22000.739（KB5014697）上，用户叫苦不迭。</p><p data-vmark="88f4">微软表示：“安装此更新后，Windows 设备可能无法使用 Wi-Fi 热点功能。尝试使用热点功能时，主机设备可能会在客户端设备连接后失去与 Internet 的连接”。</p><p data-vmark="b154">无需多说，大家都能明白这是一次重大失误，对于 Windows 来说十分影响体验。但幸运的是，微软现在已经准备好完整的修复程序。</p><p style="text-align: center;" data-vmark="8202"><img src="https://img.ithome.com/newsuploadfiles/2022/6/bd739e0b-7aa4-45e2-8ca9-dd45cf0eba71.png" w="783" h="724" title="微软修复 Win11 Wi-Fi 热点问题" width="783" height="724" referrerpolicy="no-referrer"></p><p data-vmark="c2d7">现在，微软已经通过累积更新 KB5014668 解决了这个问题。当然，KB5014668 更新目前仅在 Windows 11 上作为可选更新，你必须手动前往 Windows 更新并检查更新以下载和安装。</p><p data-vmark="5c94">但是，不止有 Win11 用户受其影响，目前主流的所有 Windows 版本（包括 Windows 7 SP1、Windows 8.1、Windows 10 和几个 Windows Server 版本）都存在这一问题，希望微软可以早日提供解决方案，但恐怕最早也得等到 7 月下一个星期二。</p><p data-vmark="c54b">IT之家曾报道，微软昨日面向所有受支持的 Windows 10 和 Windows 11 版本发布了新的可选更新（C-Updates）。Win11 用户可下载 KB5014668 补丁，安装后可使系统版本号提升到  Build 22000.778，但当时微软还没有确认这一修复内容。</p><p data-vmark="21aa">值得一提的是，KB5014668 也同样存在 Bug。例如安装此更新后，某些 .NET Framework 3.5 应用可能会出现问题或可能无法打开。受影响的应用在 .NET Framework 3.5 中使用某些可选组件，例如 Windows Communication Foundation (WCF) 和 Windows 工作流 (WWF) 组件，目前还没有好的解决办法，你可以通过命令提示符 以编程方式执行此操作 (以管理员身份运行) 并运行以下命令：</p><p data-vmark="0ae9"><code class="ocpCode"></code></p><pre><code class="ocpCode">dism /online /enable-feature /featurename:netfx3 /all<br></code></pre><p><code class="ocpCode"></code></p><pre><code class="ocpCode">dism /online /enable-feature /featurename:WCF-HTTP-Activation</code></pre><code class="ocpCode ai-word-checked"><pre>dism /online /enable-feature /featurename:WCF-NonHTTP-Activation</pre></code><p></p><p data-vmark="9be5">拓展阅读：</p><p data-vmark="16c7">《<a href="https://www.ithome.com/0/624/929.htm" target="_blank">微软承认 Win11/10/8.1/7 等存在 Wi-Fi 热点问题，连接无线后即自动断网</a>》</p><p data-vmark="7162">《<a href="https://www.ithome.com/0/626/060.htm" target="_blank">微软 Win11 Build 22000.778 (KB5014668) 发布：新增搜索亮点，带来大量修复内容</a>》</p>
          
</div>
            