
---
title: '微软为PrintNightmare漏洞提供进一步的缓解措施 将其评级为 "高严重性"'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0704/c8789fbeb9b4e72.png'
author: cnBeta
comments: false
date: Sun, 04 Jul 2021 08:45:27 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0704/c8789fbeb9b4e72.png'
---

<div>   
<strong>几天前，我们了解到一个名为 "PrintNightmare"的新漏洞几乎影响到所有的Windows设备。</strong>它利用Windows Print
Spooler服务的未受保护的功能来触发远程代码执行（RCE）。美国网络安全和基础设施安全局（CISA）强调它是一个关键漏洞，微软正在积极调查修复。现在，微软公司就此事提供了更多信息。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0704/c8789fbeb9b4e72.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>PrintNightmare，在漏洞代号CVE-2021-34527下被追踪，现在已被授予通用漏洞评分系统（CVSS）基本评级为8.8。值得注意的是，CVSS v3.0规范文件将其定义为 "高严重性"漏洞，但它非常接近从9.0开始的"危急"评级。目前的时间紧迫性得分是8.2，时间分是根据一些因素来衡量一个漏洞的当前可利用性。</p><p>值得注意的是，一个类似的漏洞在6月的 "补丁星期二"更新中被修复，但它的CVSS基础分是7.8。</p><p>基础分被定为8.8分是因为微软已经确定该攻击载体是在网络层面，需要较低的攻击复杂性和权限，不涉及用户互动，并可能导致组织资源的保密性、完整性和可用性 "完全丧失"。同时，时间分是8.2分是因为功能上的漏洞代码在互联网上很容易获得，并且适用于所有版本的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>，存在关于它的详细报告，并且有一些官方的补救方法被建议。</p><p>我们已经知道，微软建议禁用Windows Print Spooler服务，或至少通过组策略禁用入站远程打印，随后还建议检查一些实体成员和包含权限的嵌套组成员。该公司建议，操作系统中远程权限成员的数量应尽可能地少，最好是在可能的情况下为零。尽管如此，该公司提醒说，从其中一些组中删除成员可能导致兼容性问题。</p><p><strong>这些受影响的群组如下：</strong></p><p>管理员</p><p>域控制器</p><p>只读域控制器</p><p>企业只读域控制器</p><p>证书管理员</p><p>模式管理员</p><p>企业管理员</p><p>组策略管理员</p><p>超级用户</p><p>系统操作人员</p><p>打印操作人员</p><p>备份操作人员</p><p>RAS服务器</p><p>兼容Windows 2000的访问</p><p>网络配置操作程序组对象</p><p>加密操作者组对象</p><p>本地账户和Administrators组的成员</p><p>微软强调将尽快提供修复方案，但与此同时，它建议企业利用Microsoft Defender 365等工具来监测潜在的恶意活动。虽然 "Print and Point"与这个漏洞没有直接关系，但微软仍然建议编辑一些注册表值以加强组织的本地安全基础设施，并表示客户端使用的打印服务器应明确列出。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1147467.htm" target="_blank">零日漏洞PrintNightmare曝光：可在Windows后台执行远程代码</a></p><p><a href="https://www.cnbeta.com/articles/tech/1148199.htm" target="_blank">0patch发布拯救Windows PrintNightmare漏洞的免费微补丁</a></p><p><a href="https://www.cnbeta.com/articles/tech/1148301.htm" target="_blank">微软警告攻击者正肆意利用Windows PrintNightmare漏洞</a></p></div>   
</div>
            