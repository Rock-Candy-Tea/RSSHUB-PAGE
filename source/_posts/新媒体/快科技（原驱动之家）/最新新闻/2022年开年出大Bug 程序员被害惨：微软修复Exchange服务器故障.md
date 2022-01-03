
---
title: '2022年开年出大Bug 程序员被害惨：微软修复Exchange服务器故障'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220103/s_56c8faccafde4359ad46c10df7005ca9.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 03 Jan 2022 07:40:45 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220103/s_56c8faccafde4359ad46c10df7005ca9.jpg'
---

<div>   
<p>随着日期从2021年12月31日跳转到2022年1月1日，不少使用微软Exchange的公司发现，自己写好的新年祝福等邮件，突然发不出去了，这也导致全球程序员被害惨。</p>
<p>Exchange Server是微软推出的一套电子邮件服务组件，可用于构建企业、高校或机构的邮件系统。简单来说，用它不止能构建“邮箱工作群”，还能协调内部工作流等。</p>
<p><strong>这些公司的邮箱服务器内滞留了大量邮件，有些甚至达到数十万封，面临服务器存储不下的问题。据一位Exchange管理员Joseph Roosen表示，这是一个由于“2022年”的到来而导致的bug。</strong></p>
<p>这个bug的根源，是微软Exchange上面的邮件过滤管理系统（FIP-FS），采用了一种名叫“yymmddHHMM”的有符号变量（Int32，也就是long）来存储日期。</p>
<p>现在微软方面表示，："我们已经创建了一个解决方案，以解决Exchange Server 2016和Exchange Server 2019上的消息卡在传输队列中的问题，因为Exchange Server内的恶意软件扫描引擎使用的签名文件中有一个潜在的日期问题。当问题发生时，你会在Exchange服务器上的应用程序事件日志中看到错误，特别是事件5300和1106（FIPFS）"。</p>
<p>为了代替使用脚本，客户也可以手动执行步骤来解决这个问题并恢复服务。要手动解决这个问题，你必须在你组织的每台Exchange服务器上执行以下步骤。</p>
<p>删除现有的引擎和元数据</p>
<p>1、停止微软过滤管理服务。 当提示您同时停止Microsoft Exchange传输服务时，请点击“是”。</p>
<p>2、使用任务管理器以确保 updateservice.exe 没有运行。</p>
<p>3、删除以下文件夹：%ProgramFiles%\Microsoft\Exchange Server\V15\FIP-FS\Data\Engines\AMD64\Microsoft。</p>
<p>4、移除以下文件夹中的所有文件：%ProgramFiles%\MicrosoftExchange Server\V15\FIP-FS\Data\Engines\metADATA。</p>
<p>更新到最新的引擎</p>
<p>1、启动Microsoft过滤管理服务和Microsoft Exchange传输服务。</p>
<p>2、打开Exchange管理壳，导航到Scripts文件夹（%ProgramFiles%\Microsoft\Exchange Server\V15\Scripts），并运行Update-MalwareFilteringServer.ps1 <server FQDN>。</p>
<p>验证引擎更新信息</p>
<p>1、在 Exchange Management Shell 中，运行 Add-PSSnapin Microsoft.Forefront.Filtering.Management.Powershell。</p>
<p>2、2.运行Get-EngineUpdateInformation，验证UpdateVersion信息为2112330001。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220103/56c8faccafde4359ad46c10df7005ca9.jpg" target="_blank"><img alt="2022年开年出大Bug 程序员被害惨：微软修复Exchange服务器故障" h="337" src="https://img1.mydrivers.com/img/20220103/s_56c8faccafde4359ad46c10df7005ca9.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     
<span>责任编辑：雪花</span>
</p>
        
</div>
            