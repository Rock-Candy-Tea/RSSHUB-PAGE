
---
title: '你的电脑能不能升级Windows 11 22H2？一招检测'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0628/a4f7a7045fbacd1.webp'
author: cnBeta
comments: false
date: Tue, 28 Jun 2022 00:11:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0628/a4f7a7045fbacd1.webp'
---

<div>   
Windows 11 22H2将于2022年秋季开始推出，预计将提供大量改进以及一些新功能。<strong>虽然Windows 11 22H2不会真正改变硬件要求，但微软已经悄悄启用了一个注册表，可以让你检查与即将到来的更新的兼容性。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0628/a4f7a7045fbacd1.webp" alt="4gaxpdln.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">如果它不兼容，会给你列出原因，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>还提供支持文档的链接，以获取有关兼容性问题的更多信息。</p><p style="text-align: left;"><strong>步骤如下：</strong></p><p style="text-align: left;">1、在PC上打开<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>注册表编辑器。</p><p style="text-align: left;">2、在注册表编辑器中，点击地址栏并删除地址。</p><p style="text-align: left;">3、转到Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\TargetVersionUpgradeExperienceIndicators</p><p style="text-align: left;">4、要检查与22H2的兼容性，请打开NI22H2 NI 代表“Nickel”，而22H2代表更新版本。</p><p style="text-align: left;">5、如果双击该值，你会注意到“ RedReason ”。如果值为NONE，则表示您的设备已准备好进行功能更新。</p><p style="text-align: left;">6、如果你看到的是其他值，那么将无法升级。该值取决于兼容性问题。</p><p style="text-align: left;">例如，如果您的设备不符合硬件要求，您将在“RedReason”中看到“TPM UEFISecureBoot”</p><p style="text-align: left;">同样，您还可以了解更新是否会被某个应用程序阻止。</p><p style="text-align: left;">此外，有一个名为“SystemDriveTooFull”的字符串告诉您升级可用的存储空间。如果数值为1，则你的设备没有足够的存储空间用于22H2或更高版本。</p>   
</div>
            