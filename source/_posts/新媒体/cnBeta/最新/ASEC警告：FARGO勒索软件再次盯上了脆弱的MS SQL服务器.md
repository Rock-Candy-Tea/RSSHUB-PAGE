
---
title: 'ASEC警告：FARGO勒索软件再次盯上了脆弱的MS SQL服务器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0926/431218bc4461ca4.webp'
author: cnBeta
comments: false
date: Mon, 26 Sep 2022 10:54:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0926/431218bc4461ca4.webp'
---

<div>   
AhnLab 安全应急响应中心（ASEC）的安全分析团队，刚刚曝光了针对易受攻击的微软 SQL 服务器的新一轮网络犯罪活动。<strong>ASEC 指出，与 Globelmposter 一样，FARGO 也是一款臭名昭著的勒索软件。</strong>此前由于使用了 .mallox 这个文件扩展名，它也一度被叫做“Mallox”。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0926/431218bc4461ca4.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 1 - 进程树（来自：<a href="https://asec.ahnlab.com/en/39152/" target="_self">AhnLab</a>）</p><p>作为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>主导的关系型数据库管理系统，MS-SQL 也被许多软件应用程序和互联网服务用于数据存储和检索。但在 FARGO 勒索软件面前，大量企业正正经历重大威胁。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/8500a31e2245b6c.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 2 - 下载附加文件</p><p>ASEC 指出，感染发生在 MS-SQL 进程通过 cmd.exe 和 powershell.exe 下载 .NET 文件时 —— 此文件会获取并加载其它恶意软件，以生成并执行终止特定进程和服务的 BAT 批处理文件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/7f0ec2d4ed95449.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 3 - BAT 文件的创建与执行</p><p>ASEC 解释称，勒索软件首先是被注入到了一个普通的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 程序（AppLaunch.exe）中。它试图删除某个路径上的注册表项，并执行恢复停用命令和关闭某些进程。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/eed6b703836c1e3.webp" alt="4.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 4 - BAT 文件详情</p><p>尽管勒索软件会加密文件，但攻击者特地排除了某些路径和扩展名 —— 比如 Globeimposter 相关的文件扩展名（.FARGO 等）—— 以使系统在“部分可访问”的情况下运行。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/266e774078c9043.webp" alt="5.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 5 - 被删除的注册表项</p><p>之后攻击者会使用 .Fargo3 扩展名（例如 OriginalFileName.FileExtension.Fargo3）重命名加密文件，而恶意软件生成的勒索记录会在“RECOVERY FILES.txt”文本文件中显示。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/e87ba1e49ac8b0d.webp" alt="6.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 6 - 停用恢复和关闭流程</p><p>攻击者在消息中威胁称，若受害者擅自动用第三方软件，勒索软件就会永久删除相关系统文件。而且如果拒付赎金，它们也会将机密信息公之于众。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/9f5df5e510e9aae.webp" alt="7.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 7 - 勒索消息与受感染文件示例</p><p>ASEC 解释称，除了未被及时修补的漏洞，MS-SQL 和 MySQL 数据库服务器还很容易因为脆弱的账户凭据而被暴力 / 字典攻破。</p><p>对此，分析团队建议服务器管理员提升对密码复杂度和保管安全性上的重视力度、定期修改和打上新版补丁，以免数据库服务器遭受暴力和字典攻击。</p>   
</div>
            