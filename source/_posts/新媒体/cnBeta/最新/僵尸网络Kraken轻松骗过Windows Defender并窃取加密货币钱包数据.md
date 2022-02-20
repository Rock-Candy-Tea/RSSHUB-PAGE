
---
title: '僵尸网络Kraken轻松骗过Windows Defender并窃取加密货币钱包数据'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0220/50da23507e80a4b.jpeg'
author: cnBeta
comments: false
date: Sun, 20 Feb 2022 08:01:55 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0220/50da23507e80a4b.jpeg'
---

<div>   
微软最近对Windows Defender的排除权限进行了更新，没有管理员权限就无法查看排除的文件夹和文件。这是一个重要的变化，因为威胁者往往会利用这一信息在这种被排除的目录中提供恶意软件的载荷，以绕过防御者的扫描。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0220/50da23507e80a4b.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0220/50da23507e80a4b.jpeg" title alt="kraken-image-1-1024x394.jpeg" referrerpolicy="no-referrer"></a></p><p>然而，这可能无法阻止ZeroFox最近发现的一个名为Kraken的新僵尸网络。这是因为Kraken只是简单地将自己添加为一个排除项，而不是试图寻找排除的地方来传递有效载荷。这是一种绕过<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Defender扫描的相对简单和有效的方法。</p><p>ZeroFox已经解释了这是如何工作的。</p><p>在Kraken的安装阶段，它试图将自己移到%AppData%/Microsoft.Net中。</p><p>为了保持隐藏，Kraken运行以下两个命令：</p><blockquote><p>powershell -Command Add-MpPreference -ExclusionPath %APPDATA%\Microsoft</p><p>attrib +S +H %APPDATA%\Microsoft\%</p></blockquote><p>ZeroFox指出，Kraken主要是一个偷窃资产的恶意软件，类似于最近发现的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>Windows 11官网外观相同的欺诈网站。这家安全公司补充说，Kraken的能力现在包括窃取与用户的加密货币钱包有关的信息，让人联想到最近的假KMSPico Windows激活器恶意软件。</p><p><a href="https://static.cnbetacdn.com/article/2022/0220/3937cd08008ab8a.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0220/3937cd08008ab8a.jpeg" title alt="kraken2-1024x214.jpeg" referrerpolicy="no-referrer"></a></p><p>最近增加的功能是能够从以下位置窃取各种加密货币钱包：</p><blockquote><p>%AppData%\Zcash</p><p>%AppData%\Armory</p><p>%AppData%\bytecoin</p><p>%AppData%Electrum\wallets</p><p>%AppData%\Ethereum\keystore</p><p>%AppData%\Exodus\exodus.wallet</p><p>%AppData%\Guarda\Local Storage\leveldb</p><p>%AppData%\atomic\Local Storage\leveldb</p><p>%AppData%\com.liberty.jaxx\IndexedDB\file__0.indexeddb.leveldb</p></blockquote><p>你可以在官方博客文章中找到更多关于Kraken工作方式的细节：</p><p><a href="https://www.zerofox.com/blog/meet-kraken-a-new-golang-botnet-in-development/" _src="https://www.zerofox.com/blog/meet-kraken-a-new-golang-botnet-in-development/" target="_blank">https://www.zerofox.com/blog/meet-kraken-a-new-golang-botnet-in-development/</a><br></p>   
</div>
            