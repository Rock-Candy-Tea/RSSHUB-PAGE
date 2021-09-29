
---
title: '开发者送新招：绕过TPM 2.0限制安装Windows 11系统'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210929/s_f626c1bf00074cad8220d87626deea64.jpg'
author: 快科技（原驱动之家）
comments: false
date: Wed, 29 Sep 2021 09:12:13 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210929/s_f626c1bf00074cad8220d87626deea64.jpg'
---

<div>   
<p>Windows 11 提高了系统的升级门槛，要求设备支持 TPM 2.0、Secure Boot，并使用支持的 CPU，微软并不会因为大家的反对而改变什么。</p>
<p>对于无法满足升级条件的用户来说，开发者AveYo最新推出的Universal MediaCreationTool（MCT）将是不错的解决方案。</p>
<p><strong>这位开发者创建的 MCT 是新的Windows 11安装脚本，能够帮你绕过 TPM 和系统要求检查。该工具本身并不是什么新应用，但本月增加了对 Windows 11 的支持和跳过TPM检查的功能。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210929/f626c1bf00074cad8220d87626deea64.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="开发者送新招：绕过TPM 2.0限制安装Windows 11系统" h="421" src="https://img1.mydrivers.com/img/20210929/s_f626c1bf00074cad8220d87626deea64.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>根据专门针对Windows 11的更新日志，该工具将通过winpeshl.ini文件在媒体启动和动态更新时跳过 TPM检查。当执行时，该脚本在注册表的“HKEY_LOCAL_MACHINE\SYSTEM\Setup\MoSetup”下创建“AllowUpgradesWithUnsupportedTPMOrCPU”值并将其设置为1或true。它还删除了“appraiserres.dll”文件。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210929/69f4d5a6cdfa4ca9a7a91a5420758a95.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="开发者送新招：绕过TPM 2.0限制安装Windows 11系统" h="347" src="https://img1.mydrivers.com/img/20210929/s_69f4d5a6cdfa4ca9a7a91a5420758a95.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>这位开发者还提醒，如果你想在你的日常驱动上运行它，你必须自己承担风险。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210929/b54f719905164dbda26d8e54b1e604b2.jpg" target="_blank"><img alt="开发者送新招：绕过TPM 2.0限制安装Windows 11系统" h="337" src="https://img1.mydrivers.com/img/20210929/s_b54f719905164dbda26d8e54b1e604b2.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     
<span>责任编辑：雪花</span>
</p>
        
</div>
            