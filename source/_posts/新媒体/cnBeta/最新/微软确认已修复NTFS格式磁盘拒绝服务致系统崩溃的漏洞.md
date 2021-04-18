
---
title: '微软确认已修复NTFS格式磁盘拒绝服务致系统崩溃的漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0228/096959acbe92bbe.jpg'
author: cnBeta
comments: false
date: Sun, 18 Apr 2021 11:10:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0228/096959acbe92bbe.jpg'
---

<div>   
在1月中旬，我们报道了Windows 10中的一个漏洞，它可以被用来破坏NTFS格式化驱动器的内容。只需要一个特别制作的文件夹名称，就可以导致卷被标记为dirty状态，然后系统需要使用Chkdsk实用程序进行修复。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0228/096959acbe92bbe.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0228/096959acbe92bbe.jpg" referrerpolicy="no-referrer"></a></p><p>但Chkdsk并不总是能做到这一点，反而让受害者无法启动系统。几个月前，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>开始在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Insiders社区测试修复补丁，现在补丁正在提供给所有用户，微软标记其为解决了被追踪为CVE-2021-28312（Windows NTFS拒绝服务漏洞）的问题。</p><p>这些修复措施被列为本月周二发布的补丁的一部分，一同到来的KB5001330和KB5001337更新主要负责卸载Windows 10中的微软Edge的传统版本。但这些Windows 10的更新，一如既往地是一把双刃剑。</p><p>不幸的是，虽然这些更新解决了不可否认的破坏性NTFS问题，但它们也给人们带来了其他问题，包括性能下降和访问共享文件夹时出现问题。在安装了Windows 10的相关更新后，试图访问有问题的路径时，会出现与Insiders构建版21322测试期间相同的消息，即" 该目录名称无效"。</p><p><strong>有关该漏洞的更多细节，可在微软安全响应中心找到：</strong></p><p><a href="https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-28312" _src="https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-28312" target="_blank">https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-28312</a><br></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1078659.htm" target="_blank">[图]微软承认Windows 10存在严重NTFS漏洞 承诺尽快修复</a></p><p><a href="https://www.cnbeta.com/articles/tech/1095699.htm" target="_blank">[图]微软正测试补丁 修复NTFS磁盘损坏问题</a></p></div>   
</div>
            