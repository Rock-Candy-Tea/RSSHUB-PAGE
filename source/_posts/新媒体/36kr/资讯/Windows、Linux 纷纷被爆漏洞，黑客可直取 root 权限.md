
---
title: 'Windows、Linux 纷纷被爆漏洞，黑客可直取 root 权限'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210722/v2_5abc9c897cda4a76a575dc58335b3059_img_000'
author: 36kr
comments: false
date: Thu, 22 Jul 2021 07:28:08 GMT
thumbnail: 'https://img.36krcdn.com/20210722/v2_5abc9c897cda4a76a575dc58335b3059_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/7kYlDMHdmeldEskLxlDR_A">“CSDN”（ID:CSDNnews）</a>，作者：苏宓，36氪经授权发布。</p> 
<p>无论是开源还是闭源，没有绝对安全的操作系统。</p> 
<p>一夕间，多款操作系统被爆存在安全漏洞，其中包括开发者最为常用的 Windows 和 Linux 操作系统也未能幸免。有研究人员发现，通过漏洞，黑客或恶意软件可绕过 Windows 和 Linux 系统的安全限制，并获得管理员级别的权限，造成设备内部的敏感/隐私资源泄露。</p> 
<h2 label="一级标题" style>Windows 被“攻破” ？</h2> 
<p>事情要从 7 月 20 日一位名为 Jonas Lykkegaard 发布的一则 Twitter 说起，其在帖子中指出，“由于某种原因，在 Windows 11 上，用户现在可以读取 SAM 文件。因此，如果你启用了 shadowvolumes，就可以像这样读取 SAM 文件了。”</p> 
<p><img src="https://img.36krcdn.com/20210722/v2_5abc9c897cda4a76a575dc58335b3059_img_000" data-img-size-val="439,522" referrerpolicy="no-referrer"></p> 
<p>在 Windows 系统中，所谓 SAM 文件指的是账号密码数据库文件。当用户登陆系统时，系统会自动地和 Config 中的 SAM 自动校对，如果登录的用户名和密码与 SAM 文件中加密的数据一致，那么会成功登录，否则登陆失败。</p> 
<p>因此如果除了管理员之外的任何人有权限访问到 SAM 文件，相当于他们可以提取到加密的密码数据，这也意味着他人已经掌握了进入自家大门的一把钥匙，可以来去<a class="project-link" data-id="3969617" data-name="自如" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969617" target="_blank">自如</a>，甚至可以在易受攻击的计算机设备上创建一个全新的帐户。与此同时，非管理员用户也可以直接将自己的权限提升到 Windows 中的最高级别 System。然而，不仅是在全新的 Windows 11 预览版中，有网友发现，在 Windows 10 最新版本里面也发现了同样的问题。</p> 
<p>在这一漏洞披露之后，引发不少研究人员的关注，其中@Benjamin Delpy 还进行了一波演示验证证实了该漏洞的存在：</p> 
<p><img src="https://img.36krcdn.com/20210722/v2_d222b6efb1b44496b1df6915a2c1ceb8_img_000" data-img-size-val="441,551" referrerpolicy="no-referrer"></p> 
<p>在深入研究该漏洞出现的原因时，美国电脑紧急应变小组（US Computer Emergency Readiness Team）表示，从 Windows 10 build 1809 版本开始，非管理用户被授予访问 SAM、 SYSTEM 和 SECURITY 注册表配置单元文件的权限，而由于这一错误，本地用户的系统权限被提升。同时，该漏洞存在于 Volume Shadow 复制服务中，该服务运行操作系统或应用程序在不锁定文件系统的情况下让录制整个磁盘的“时间点快照”的 Windows 功能被打开。</p> 
<p>这一配置错误直接导致 Windows 在系统驱动器的卷影副本（VSS）可用的情况下，非管理员用户可直接读取 SAM 这些数据库，同时，更方便黑客：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>提取和利用账户的哈希密码；</p></li> 
 <li><p>发现原始的 Windows 安装密码；</p></li> 
 <li><p>获取 DPAP 计算机密码，可用于解密所有计算机私钥；</p></li> 
 <li><p>获得一个电脑机器账号，可以用来进行白银票据（silver ticket）攻击。</p></li> 
</ul> 
<p><img src="https://img.36krcdn.com/20210722/v2_e65f930113f740cc8dceb554c093b88a_img_000" data-img-size-val="680,524" referrerpolicy="no-referrer"></p> 
<p>简单来看，“经过本地身份验证的攻击者可能能够实现本地权限提升、伪装成其他用户或实现其他与安全相关的影响。” 这可用于借助恶意软件彻底感染系统、窥探其他用户等。</p> 
<p>也许很多用户会认为自己的计算机是安全的，但 US Computer Emergency Readiness Team 公告指出，“在某些配置中，VSS 卷影副本可能不能用，但是，只需拥有一个大于 128GB 的系统驱动器，然后执行 Windows 更新或安装 MSl 即可让 VSS 卷影副本自动创建。”</p> 
<p>当然如果你想检查一下自己的系统是否有可用的 VSS 卷影副本，可以使用一下命令：</p> 
<blockquote> 
 <p>vssadmin list shadows</p> 
</blockquote> 
<p>与此同时，<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>也证实了这一漏洞的存在，该漏洞的 ID 为 CVE-2021-36934，微软对该安全漏洞的利用评估是“有可能被利用”，并表示（https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934）：</p> 
<p>由于对多个系统文件（包括安全帐户管理器 (SAM) 数据库）的访问控制列表 (ACL) 过于宽松，因此存在特权提升漏洞。成功利用此漏洞的攻击者可以使用 SYSTEM 权限运行任意代码。然后攻击者可以安装程序；查看、更改或删除数据；或创建具有完全用户权限的新帐户。</p> 
<p>微软称当前正在调查受影响的 Windows 版本并致力于修复，在正式的解决方案/补丁尚未发布之前，其也提出了两种临时的办法：</p> 
<p>一种是限制对 %windir%\system32\config 内容的访问。易受攻击的系统可以为 %windir%\system32\config 目录中的文件启用 ACL 继承，可以用管理员身份运行以下命令提示符：</p> 
<blockquote> 
 <p>icacls %windir%\system32\config\*.* /inheritance:e</p> 
</blockquote> 
<p>一旦针对这些文件更正了 ACL，就必须删除系统驱动器的任何 VSS 卷影副本，以保护系统免受攻击。这可以通过以下命令完成，假设你的系统驱动器是“c:”:</p> 
<blockquote> 
 <p>vssadmin delete shadows /for=c: /Quiet</p> 
</blockquote> 
<p>通过再次运行 vssadmin list shadows 确认 VSS 卷影副本已被删除。请注意，依赖现有卷影副本的任何功能（例如系统还原）都不会按预期运行。新创建的卷影副本将包含正确的 ACL，将按预期运行。</p> 
<p>另外一种是删除卷影复制服务 (VSS) 卷影副本。</p> 
<p>更多操作细节可参考：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934</p> 
<h2 label="一级标题" style>Linux 也未能幸免</h2> 
<p>无独有偶，除了 Windows 被爆有漏洞外，研究人员还在 Linux 内核文件系统中发现了一个 size_t-to-int 类型转换安全漏洞——CVE-2021-33909，任何非管理员用户都可以在易受攻击的设备上获得 root 级权限。</p> 
<p>发现该漏洞的安全公司 Qualys 团队研究人员将其称为 Sequoia，并表示“该漏洞存在于 Ubuntu 20.04、Ubuntu 20.10、Ubuntu 21.04、Debian 11 和 Fedora 34 Workstation 的默认安装中。其他 Linux 发行版可能容易受到攻击并且可能被利用。” </p> 
<p><img src="https://img.36krcdn.com/20210722/v2_0fc346f4facf4c929b4a2abc05e77d89_img_000" data-img-size-val="360,221" referrerpolicy="no-referrer"></p> 
<p>据悉，2014 年以后的所有 Linux 内核版本都存在这一漏洞，Qualys 指出要想完全修复此漏洞，必须要修补内核，此外，其也提供了一些缓解措施（https://blog.qualys.com/vulnerabilities-threat-research/2021/07/20/sequoia-a-local-privilege-escalation-vulnerability-in-linuxs-filesystem-layer-cve-2021-33909）：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>将 /proc/sys/kernel/unprivileged_userns_clone 设置为 0，以防止攻击者在用户命名空间中挂载长目录。但是，攻击者可能会通过 FUSE 挂载一个长目录，目前不排除有这种可行性，如果攻击者 FUSE-mount 一个长目录（超过 8MB），那么 systemd 会耗尽其堆栈，从而导致整个操作崩溃系统。</p></li> 
 <li><p>将 /proc/sys/kernel/unprivileged_bpf_disabled 设置为 1，以防止攻击者将 eBPF 程序加载到内核中。然而，攻击者可能会破坏其他 vmalloc() 化的对象（例如，线程堆栈）。</p></li> 
</ul> 
<p>对于普通用户而言，在等待官方的更新补丁之前，也切记不要下载或点击安装自己所不熟悉的软件，防止恶意软件造成信息泄露。与此同时，也需关注及检查设备是否有最新的更新，保证及时安装减少漏洞带来的影响。</p> 
<p>参考：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934</p></li> 
 <li><p>https://www.theregister.com/2021/07/21/windows_linux_privilege_escalation/</p></li> 
 <li><p>https://arstechnica.com/gadgets/2021/07/separate-eop-flaws-let-hackers-gain-full-control-of-windows-and-linux-systems/</p></li> 
</ul>  
</div>
            