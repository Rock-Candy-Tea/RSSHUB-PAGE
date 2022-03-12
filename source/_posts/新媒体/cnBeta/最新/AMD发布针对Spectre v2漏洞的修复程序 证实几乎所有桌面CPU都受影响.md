
---
title: 'AMD发布针对Spectre v2漏洞的修复程序 证实几乎所有桌面CPU都受影响'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0312/7f18d259984e792.png'
author: cnBeta
comments: false
date: Sat, 12 Mar 2022 07:30:20 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0312/7f18d259984e792.png'
---

<div>   
虽然AMD的CPU似乎不受影响于影响英特尔和ARM的CPU的Spectre-HB，但英特尔的IPAS
STORM安全团队声称，AMD用于修复Spectre
v2漏洞的补丁自2018年以来就已经失效。换句话说，英特尔声称，AMD对安全漏洞的缓解措施不仅没有效果，而且还存在问题。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0312/7f18d259984e792.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/7f18d259984e792.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>AMD近期发布了"CVE-2017-5715的缓解更新"，这基本上意味着该公司为Spectre Variant 2安全漏洞发布了新的修复方案。在英特尔的安全团队STORM发现AMD之前发布的缓解措施的问题后，这家CPU制造商提供了这个补丁。</p><p>AMD通过这个补丁建议使用另一种方法来缓解Spectre漏洞，并推测认为之前的缓解措施是无效的。从本质上讲，AMD已经为该公司以前修复的旧安全风险提供了一个新的补丁，但正如英特尔所证明的那样，并没有成功。</p><p>英特尔以及ARM CPU已经被发现仍然容易受到通过新的分支历史注入变体的基于Spectre v2的攻击。这令人担忧，因为英特尔已经使用了增强型间接分支限制性推测（eIBRS）和/或Retpoline缓解措施。大多数安全研究人员似乎认为这些修复和缓解措施足以解决Spectre v2带来的风险。</p><p>在试图开发替代缓解技术的同时，英特尔发现，AMD自2018年以来用于修补Spectre漏洞的缓解措施并不充分。具体来说，AMD一直依赖"LFENCE/JMP"缓解措施，但英特尔发现这些缓解措施不足以完全阻止使用Spectre v2漏洞的攻击。</p><p>Spectre漏洞有可能允许攻击者通过侧面通道攻击"不受阻碍和无法检测"地访问正在CPU中处理的信息。更令人担忧的是，该漏洞可以被远程利用。然而，AMD强调，它还没有观察到AMD产品在野外有任何活跃的漏洞，这些漏洞被标记为CVE-2017-5715的缺陷。</p><p><strong>了解更多：</strong></p><p><a href="https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1036" _src="https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1036" target="_blank">https://www.amd.com/en/corporate/product-security/bulletin/amd-sb-1036</a><br></p>   
</div>
            