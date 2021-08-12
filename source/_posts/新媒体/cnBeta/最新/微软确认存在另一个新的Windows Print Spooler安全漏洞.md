
---
title: '微软确认存在另一个新的Windows Print Spooler安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0812/2223a064ea59d52.png'
author: cnBeta
comments: false
date: Thu, 12 Aug 2021 07:28:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0812/2223a064ea59d52.png'
---

<div>   
<strong>与微软Windows打印机的相关问题的噩梦挥之不去，今天早些时候，该公司确认了Windows Print Spooler服务的一个新的安全漏洞。这个新的漏洞被编号为CVE-2021-36958。</strong>微软表示，当Windows Print Spooler服务不适当地执行特权文件操作时，存在一个远程代码执行的漏洞，成功利用该漏洞的攻击者可以用系统权限运行任意代码。<br>
 <p>然后，攻击者可以安装程序；查看、更改或删除数据；或创建具有完全用户权限的新账户。</p><p>那些一直密切关注此事的人可能会注意到，这个新问题与正在发生的PrintNightmare漏洞有关，该公司几天前曾为此发布了一个补丁。微软声称，该补丁应该在很大程度上有助于缓解这个问题，因为它现在需要管理员权限来实现打印驱动的安装和更新操作。然而，在已经安装了打印机驱动程序的系统上，可能是威胁者的非管理员用户仍然可以利用该漏洞。</p><p>值得注意的是，该漏洞被标记为远程代码执行（RCE），但CERT的Will Dormann表示，这显然是本地权限升级漏洞（LPE）。事实上，在该漏洞的文档中，微软自己将攻击媒介描述为本地。</p><p><img src="https://static.cnbetacdn.com/article/2021/0812/2223a064ea59d52.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>微软对此正在进行修复工作，并再一次建议用户在非必要的情况下禁用<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Print Spooler服务作为临时的变通办法。然而，安全研究员Benjamin Delpy说他有一个比完全禁用打印服务更好的方法。建议用户通过使用Windows组策略中的Windows"Package Point and Print - Approved Servers"选项，将打印功能只限制在批准的服务器上。</p><p>微软还提供了更多利用组策略解决打印安全问题的细节汇总：</p><p><a href="https://docs.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer" _src="https://docs.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer" target="_blank">https://docs.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer</a><br></p>   
</div>
            