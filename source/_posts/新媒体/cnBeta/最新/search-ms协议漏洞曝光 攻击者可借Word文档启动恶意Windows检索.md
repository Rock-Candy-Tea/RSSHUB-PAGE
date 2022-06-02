
---
title: 'search-ms协议漏洞曝光 攻击者可借Word文档启动恶意Windows检索'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0602/c4afc4a82b453c8.png'
author: cnBeta
comments: false
date: Thu, 02 Jun 2022 10:55:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0602/c4afc4a82b453c8.png'
---

<div>   
<strong>在微软公布了 MSDT 支持诊断工具的高危漏洞之后，又有研究人员曝光了另一个可连接到远程托管的恶意软件的零日漏洞。</strong>问题在于被称作“search-ms”的统一资源标识符（URI），相关应用或链接能够借此来启用客户端设备上的搜索功能，而现代的 Windows 操作系统（比如 11 / 10 / 7）又允许 Windows Search 浏览本地和远程主机上的文件。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0602/c4afc4a82b453c8.png" alt="1-1.png" referrerpolicy="no-referrer"></p><p>正常情况下，用户可设置一个带有远程主机和显示名称的 URI、并在搜索窗口的标题栏上展现出来，而 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 可以使用各种方法来调用个性化搜索窗口（比如通过 Web 浏览器、或 Win+R 运行）。</p><p>然而 BleepingComputer 指出，别有用心的人或利用协议处理程序来创建虚假的 Windows 更新目录、再诱骗用户点击伪装成合法更新的恶意软件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0602/7683e6416297b73.gif" alt="1-2.gif" referrerpolicy="no-referrer"></p><p>庆幸的是，search-ms 协议漏洞仍需目标用户执行部分手动操作、且现代浏览器（比如 Microsoft Edge）都会弹出额外的安全警告。即便如此，攻击者仍可利用其它“组合拳”来达成目的。</p><p>比如结合 Microsoft <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> OLEObject 中的一个新缺陷，便可绕过受保护的视图并启动 URI 协议处理程序、而无需用户交互介入。</p><p>为做概念验证，@hackerfantastic 尝试制作了一个可自动打开 Windows 搜索窗口、并连接到远程 SMB 的 Word 文档。</p><p>此外由于 search-ms 允许对搜索窗口进行重命名，黑客甚至可以通过“个性化”的搜索来误导用户上钩。</p><p><img src="https://static.cnbetacdn.com/article/2022/0602/91e78f892703581.png" alt="2-1.png" referrerpolicy="no-referrer"></p><p>在另一个概念验证中，他甚至通过一个 RTF 文档实现了同样的目的、且这次甚至无需启动 Word 即可得逞。</p><p>当文件资源管理器在预览窗格上创建预览时，search-ms 漏洞就会让它自动启动一个新的搜索窗口。</p><p><strong>为堵住这个漏洞，广大现代 Windows 操作系统用户（如 11 / 10 / 7）可尝试以下缓解措施：</strong></p><blockquote><p>● 使用 WinKey+R 组合键，召唤‘运行’窗口。</p><p>● 按下 Ctrl + Shift + Enter 组合键，以管理员身份运行 CMD 命令提示符。</p><p>● 输入 reg export HKEY_CLASSES_ROOT\search-ms search-ms.reg 并执行，以创建密钥备份。</p><p>● 键入 reg delete HKEY_CLASSES_ROOT\search-ms /f 并确认执行，以从 Windows 注册表中删除密钥。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0602/5b99760bceaa40c.gif" alt="2-2.gif" referrerpolicy="no-referrer"></p><p>目前<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>正在努力修补协议处理程序和相关 Windows 功能中的漏洞，即便如此，安全专家仍警告黑客可能随时找到其它可利用的组合缺陷。</p><p>有鉴于此，我们只能寄希望于微软会专注于封堵“在无用户交互介入下，便可利用 Office 应用程序调动 URI 处理程序”的功能漏洞。</p><p>事实上，去年的 PrintNightmare 漏洞利用已是前车之鉴。然而当时微软仅仅修复了一个组件，结果后来又让研究人员曝光了其它漏洞。</p>   
</div>
            