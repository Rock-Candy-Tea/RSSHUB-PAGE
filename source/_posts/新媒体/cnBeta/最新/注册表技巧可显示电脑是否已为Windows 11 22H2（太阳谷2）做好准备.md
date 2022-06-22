
---
title: '注册表技巧可显示电脑是否已为Windows 11 22H2（太阳谷2）做好准备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0622/a5332dbf788e189.jpg'
author: cnBeta
comments: false
date: Wed, 22 Jun 2022 11:32:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0622/a5332dbf788e189.jpg'
---

<div>   
上个月，微软证实了人们的猜测，Windows 11 Build 22621确实是Windows 11
22H2功能更新的RTM候选，将在今年晚些时候发布。据微软称，Windows 11
22H2的系统要求没有变化，尽管未来有一点可能是让固态硬盘成为强制性硬件需求，公司正在推动OEM厂商为Windows
11系统采用更快的存储选项。<br>
 <p>虽然<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>没有更新官方工具来检查<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11的兼容性，就像之前的PC健康检查应用程序一样，但用户仍然可以借助一个技巧，即挖掘Windows注册表，以了解系统是否准备好接受Windows 11 22H2（太阳谷2）。</p><p>这些信息可以在HKEY_LOCAL_MACHINE\Software中找到，其中"TargetVesionUpgradeExperienceIndicators"子树揭示了关于电脑是否准备好了22H2，或者是否有什么东西阻碍了它的兼容性和升级到太阳谷2（SV2）的能力。</p><p>该子键的完整地址是：</p><p>HKLM\SOFTWARE\MicrosoftWindows NT\CurrentVersion\AppCompatFlags\TargetVersionUpgradeExperienceIndicators\NI22H2</p><p><a href="https://static.cnbetacdn.com/article/2022/0622/a5332dbf788e189.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0622/a5332dbf788e189.jpg" title alt="1655886898_win_11_22h2_compatiblity_check_registry_(source-_panu_saukko_twitter).jpg" referrerpolicy="no-referrer"></a></p><p>在这个文件夹中，"UpEx"和"UpExU"的值应该被设置为"Green"，如果一个系统已经准备好使用Windows 11 22H2的话。同时，"RedReason"的值应该是"None"。相反，对于一个不兼容的系统，这些值应该是"Red"而不是"Green"，而且RedReason应该列出使其不兼容的原因，如缺少TPM 2.0或安全启动。</p><p>下面是Twitter用户Panu Saukko发布的一个不兼容系统的例子，该系统有一个不支持的CPU，也不支持TPM。该截图是在一个Windows 10版本20H2系统上拍摄的，这就是为什么Windows版本21H1、21H2、CO21H2和NI22H2的升级体验指标会出现。</p><p>关于兼容或不兼容规格的更多细节可在正上方的"CompatMarkers/NI22H2"文件夹中找到。</p>   
</div>
            