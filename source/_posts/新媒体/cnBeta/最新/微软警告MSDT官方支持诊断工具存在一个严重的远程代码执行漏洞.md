
---
title: '微软警告MSDT官方支持诊断工具存在一个严重的远程代码执行漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0531/cd7cbb16508ac65.png'
author: cnBeta
comments: false
date: Tue, 31 May 2022 07:50:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0531/cd7cbb16508ac65.png'
---

<div>   
<strong>如果你曾就 Windows 或 Windows Server 系统中的某些问题，而直接与微软客户支持取得过联系，那或许不会对官方推荐使用的 MSDT 支持诊断工具感到陌生。</strong>参照微软技术支持的建议，你可通过 WinKey + R 组合键唤出运行窗口、并输入 msdt 来直接调用该工具。此时系统会要求用户输入支持代表提及的密钥以运行一些诊断，然后将结果直接提交给微软以供进一步分析。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0531/cd7cbb16508ac65.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：MS <a href="https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/" target="_self">Security Response Center</a>）</p><p>尴尬的是，周一的时候，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>披露了 MSDT 中存在某个远程代码执行（RCE）漏洞的公告（<a href="https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-30190" target="_self">CVE-2022-30190</a>）。</p><p>更糟糕的是，该安全漏洞几乎波及所有受支持的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 和 Windows Server 版本 —— 包括 Windows 7 / 8.1 / 10 / 11，以及 Windows Server 2008 / 2012 / 2016 / 2019 / 2022 。</p><p>尽管微软尚未给出详细说明（或许尚未完成修复），但该公司解释称 —— 当 Microsoft Word 等应用程序通过 URL 协议调用 MSDT 时，该 RCE 漏洞就有被攻击者利用的风险。</p><p>在得逞后，攻击者将能够运行任意代码、通过调用应用程序的权限来查看、删除或更改您的文件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0531/187ff4036712735.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;"><a href="https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-30190" target="_self">CVE-2022-30190</a> 被视作一个高危漏洞</p><p><strong>作为应对，目前微软给出的缓解措施是通过命令提示符（CMD）禁用 MSDT：</strong></p><blockquote><p>● 以管理员身份运行 CMD 命令提示符；</p><p>● 正式操作前，请记得先备份注册表（执行 reg export HKEY_CLASSES_ROOT\ms-msdt filename 命令）；</p><p>● 然后确认执行“reg delete HKEY_CLASSES_ROOT\ms-msdt /f”命令。</p></blockquote><p>若后续仍有调用 MSDT 诊断支持工具的需要，亦可在必要时（推荐等待微软推出正式补丁修复后）执行如下命令来解封：</p><blockquote><p>● 以管理员身份运行 CMD 命令提示符；</p><p>● 执行以下命令，以恢复先前备份的注册表文件（reg import [文件名]）。</p></blockquote><p>与此同时，我们强烈建议广大 Windows 用户开启 Microsoft Defender 或其它靠谱的第三方防护软件，并允许向云端自动提交嫌疑样本。</p><p>至于 Microsoft Defender for Endpoint 的企业管理员，也请通过适当的配置策略，来减少源于 <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 应用程序的攻击面。</p>   
</div>
            