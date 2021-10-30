
---
title: '旧版WinRAR中发现远程代码执行漏洞 请立即更新'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1030/20cfb6dae0dde70.webp'
author: cnBeta
comments: false
date: Fri, 29 Oct 2021 23:50:31 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1030/20cfb6dae0dde70.webp'
---

<div>   
<strong>上周，一名研究人员在WinRAR文件压缩软件的旧版试用版中发现了一个漏洞。它允许远程代码执行，允许攻击者拦截和改变发送给WinRAR用户的请求。</strong>网络安全研究员Igor
Sak-Sakovskiy在10月20日发表了一篇文章，详细介绍了WinRAR的漏洞，并指定了常见漏洞和暴露的ID
CVE-2021-35052。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1030/20cfb6dae0dde70.webp" title alt="2021-10-29-image-3-p.webp" referrerpolicy="no-referrer"></p><p>该漏洞影响到WinRAR试用版本5.70，但不包括最新的版本（6.02版），开发人员在7月更新了该版本，这意味着解决方案已经提供，只是需要用户尽快实施手动升级。</p><p>研究人员在偶然发现5.70版中的一个JavaScript错误时发现了这个漏洞。进一步调查，他们发现有可能拦截WinRAR与互联网的连接，并中途改变其对终端用户的回应。</p><p>然而，除了运行docx、pdf、py或rar文件时，该漏洞仍然会触发<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>安全警告。为了工作，用户必须在对话框中点击"是"或"运行"。因此，当运行WinRAR时出现这些窗口时，用户应该小心。攻击者要完成恶意行为，还需要能够进入与目标相同的网络域。</p><p>Sakovskiy还指出，早期版本的WinRAR有可能通过2019年更知名的漏洞CVE-2018-20250进行远程代码执行，因此尽快升级到新版更是当务之急。</p><p>如果你不确定正在运行哪个版本的WinRAR，打开程序后，点击窗口顶部的"帮助"，然后点击"关于WinRAR"。当然，转换到7-Zip也是一个不错的办法。</p>   
</div>
            