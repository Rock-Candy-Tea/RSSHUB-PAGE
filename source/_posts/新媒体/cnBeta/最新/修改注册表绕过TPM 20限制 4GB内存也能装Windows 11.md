
---
title: '修改注册表绕过TPM 2.0限制 4GB内存也能装Windows 11'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0705/0c9fc1b68534465.png'
author: cnBeta
comments: false
date: Mon, 05 Jul 2021 07:30:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0705/0c9fc1b68534465.png'
---

<div>   
微软发布的Windows 11系统在硬件要求上提高了门槛，不仅需要4GB以上内存，还要TPM 2.0及安全启动两个功能，很多人卡在升级资格上都是因为TPM 2.0。不过即便没有这些功能及硬件，Windows 11修改注册表的话也能绕过这些限制。<br>
<p>Betanews网站上给出了这样的一套方法，其实国内之前也有人用过类似手段了，修改注册表可以绕过很多<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>官方的限制，只不过对普通人来说操作有点麻烦。</p><p>1、 按下Win+R打开运行框，输入regedit打开注册表界面。</p><p>2、 找到HKEY_LOCAL_MACHINE  SYSTEM  Setup，在该项目新建一个项——LabConfig。</p><p>3、 在LabConfig中，创建一个名为BypassTPMCheck的DWORD（32 位）值，数值设定为1。</p><p>4、 在LabConfig中，再创建一个名为BypassRAMCheck的DWORD（32 位）值，数值设定为1.</p><p>5、 接着创建一个名为BypassSecureBootCheck的DWORD（32 位）值，数值设定为1。</p><p>6、退出注册表编辑器。</p><p><img src="https://static.cnbetacdn.com/article/2021/0705/0c9fc1b68534465.png" referrerpolicy="no-referrer"></p><p>这三个注册表的意思都都很简单，<strong>就是绕过TPM、绕过内存检查、绕过安全启动，这样一来安装Win11就没有TPM 2.0、4GB内存及安全启动BIOS功能的限制了，可以让大部分机器正常安装Win11。</strong></p><p>考虑到注册表编辑有一定的危险性，硬件要求实在不满足的用户可以试试。</p><p><img src="https://static.cnbetacdn.com/article/2021/0705/525815a3f1e0eaf.png" referrerpolicy="no-referrer"></p>   
</div>
            