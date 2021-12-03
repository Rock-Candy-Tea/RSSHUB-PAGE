
---
title: 'Fedora 36或支持RPM软件包的FS-VERITY完整性_真实性验证'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1203/6d6ebc06e5bdf1c.jpg'
author: cnBeta
comments: false
date: Fri, 03 Dec 2021 09:25:46 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1203/6d6ebc06e5bdf1c.jpg'
---

<div>   
Phoronix 报道称：<strong>Fedora 36 有望支持 Linux 内核的 fs-verity 代码，从而允许围绕 RPM 软件包的一些有趣的完整性（Integrity）和真实性（Authenticity）用例。</strong>具体说来是，该内核功能模块为只读文件提供了真实性保护，以便位于受支持文件系统上的内容，可被透明地验明它们的完整性和真实性。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1203/6d6ebc06e5bdf1c.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://fedoraproject.org/wiki/Changes/FsVerityRPM" target="_self">Fedora Wiki</a>）</p><p>FS-VERITY 还允许给特定文件构建 Merkle 树，将其与文件持久化，然后就可以根据 Merkle 树来验证文件。</p><p>这么做的好处是允许检测损坏的文件（无论是意外发生、还是遭遇了恶意性质的篡改），以及文件审计和其它类似的安全用例。</p><p>目前一支 Facebook（公司已更名为 Meta）工程师团队正在带头使用 fs-verity 来验证已安装的 RPM 文件，且相关更改对用户来说是透明的。</p><p>此外只有在安装 fs-verity 验证的 RPM 插件时，附加验证功能才会处于活动状态。从安全角度来看，这项变更是相当有趣的。</p><p>不过从 Merkle 树生成、签名开销等成本方面来考量，这项工作的后续走向，仍取决于 Fedora 工程指导委员会的评估。</p><p>如果一切顺利，我们有望于 2022 年春季（预计 4 月下旬）发布的 Fedora 36 版本中，正式迎来这项功能的支持。</p>   
</div>
            