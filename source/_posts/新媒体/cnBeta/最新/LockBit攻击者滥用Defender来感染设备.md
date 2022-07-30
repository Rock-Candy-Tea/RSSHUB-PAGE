
---
title: 'LockBit攻击者滥用Defender来感染设备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0730/c4f4c7fd088be6d.jpg'
author: cnBeta
comments: false
date: Sat, 30 Jul 2022 02:29:33 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0730/c4f4c7fd088be6d.jpg'
---

<div>   
<a href="https://www.sentinelone.com/labs/lockbit-ransomware-side-loads-cobalt-strike-beacon-with-legitimate-vmware-utility/" target="_blank"><strong>网络安全公司 SentinelOne 今天发布新闻稿</strong></a><strong>，表示微软内置的反恶意软件解决方案已经被滥用，在受害者设备上加载 <a href="https://trial.cobaltstrike.com/help-staged-exe" target="_blank">Cobalt Strike</a> 信标。</strong>LockBit Ransomware as a Service (RaaS) 运营商及其附属公司在 Microsoft Defender 中使用专门的命令行工具“mpcmdrun.exe”，实现感染受害者个人电脑。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0730/c4f4c7fd088be6d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0730/c4f4c7fd088be6d.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在博文中，SentinelOne 表示："在近期的调查中，我们发现威胁者滥用 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Defender 命令行工具 MpCmdRun.exe 来破译和加载 Cobalt Strike"。</p><p style="text-align: left;">这种攻击方式和此前曝光的 VMWare CLI 案件非常相似。攻击者利用 Log4j 漏洞下载 MpCmdRun，执行从 Command-and-Control (C2) 服务器下载恶意 DLL 文件和经过加密的 Cobalt Strike payload 文件，从而感染受害者的系统。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0730/4d59a84e6f22668.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0730/4d59a84e6f22668.jpg" alt="azkurxjp.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">滥用的 MpCmd.exe 可以侧载经过改装的 mpclient.dll，该 dll 文件从 c0000015.log 文件中加载和解密 Cobalt Strike Beacond。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0730/f66f6c677d577de.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0730/f66f6c677d577de.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            