
---
title: '微软 Office 被曝 0 day 漏洞，Windows 支持诊断工具来背锅'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/6/49ebf8c2-b1e0-432b-9325-b84e1eb228ac.png'
author: IT 之家
comments: false
date: Sat, 04 Jun 2022 12:58:58 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/6/49ebf8c2-b1e0-432b-9325-b84e1eb228ac.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1385139" rel="nofollow">Coje_He</a> 的线索投递！</div>
            <p data-vmark="d08a"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 4 日消息，有研究人员在微软 Office 中发现一个 0 day 安全漏洞 ——Follina，漏洞 CVE 编号为 CVE-2022-30190。</p><p data-vmark="03a4">微软已确认该漏洞存在于 Windows 上的微软微软支持诊断工具（Microsoft Support Diagnostic Tool）中，当 MSDT 使用 Word 等应用从 URL 协议调用时便会触发漏洞。</p><p data-vmark="fa50">值得注意的是，这种混淆的代码可以在不打开文档的情况下运行，比如通过 IE 的预览窗口。</p><p data-vmark="6b75">攻击者利用该漏洞可以以调用应用的权限运行任意代码，然后安装应用程序、查看、修改和删除数据，甚至创建新的账户等。</p><p data-vmark="360b">IT之家了解到，这一漏洞似乎不局限于 Windows 的版本，只要系统安装了 Microsoft 支持诊断工具就有可能会暴露出来。</p><p data-vmark="504d">微软表示，用户只需禁用 MSDT URL 协议即可避免此漏洞被利用，而且你仍然可以使用 Get Help 应用程序和系统设置中的其他或其他故障排除程序访问故障排除程序。此外，微软还提示用户将杀软 Microsoft Defender 更新至最新版本（1.367.719.0），以检测任何可能的漏洞利用。</p><p data-vmark="2e32">禁用 MSDT URL 协议的方法：</p><ul class=" list-paddingleft-2"><li><p data-vmark="df53">以管理员身份打开命令提示符 CMD。</p></li><li><p data-vmark="3902">备份注册表项，执行命令 reg export HKEY_CLASSES_ROOT\ms-msdt filename</p></li><li><p data-vmark="7c73">执行命令 reg delete HKEY_CLASSES_ROOT\ms-msdt /f</p></li></ul><p data-vmark="3007" style="text-align: start;">撤销：</p><ul class="ai-word-checked list-paddingleft-2"><li><p data-vmark="3e48">以管理员身份运行命令提示符。</p></li><li><p data-vmark="f5a6">要恢复注册表项，请执行命令“reg import <em>filename”</em></p></li></ul><p data-vmark="c647">安全研究人员 nao_sec 上个月意外发现一个位于 Belarus 的 IP 地址向 Virus Total 提交的恶意 Word 文档，该文件滥用了微软的 MSDT（ms-msdt）技术。他使用外部链接来加载 HTML，然后使用 ms-msdt 方案来执行 PowerShell 代码。</p><p data-vmark="9772">Kevin Beaumont 发现，这是一个微软 Word 使用 MSDT 执行的命令行字符串，即使在宏脚本被禁用的情况下也可以执行。目前已知受该漏洞影响的版本有 Office 2013、2016、Office Pro Plus 和 Office 2021 等。</p><p data-vmark="1fab">实际上，研究人员早在 4 月就将该漏洞报告给了微软，但微软称这并非是一个安全相关的问题，并且关闭了该漏洞报告，声称没有远程代码执行的安全影响，但直到 5 月 30 日微软才对该漏洞分配了 CVE 编号，虽然至今都没有发布关于该漏洞的修复补丁。</p><p style="text-align: center;" data-vmark="749f"><img src="https://img.ithome.com/newsuploadfiles/2022/6/49ebf8c2-b1e0-432b-9325-b84e1eb228ac.png" w="1440" h="1030" title="微软 Office 被曝 0 day 漏洞，Windows 支持诊断工具来背锅" width="1440" height="587" referrerpolicy="no-referrer"></p>
          
</div>
            