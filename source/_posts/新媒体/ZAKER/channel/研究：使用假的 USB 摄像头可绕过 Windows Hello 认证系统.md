
---
title: '研究：使用假的 USB 摄像头可绕过 Windows Hello 认证系统'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60f51d84b15ec00256277582_1024.jpg'
author: ZAKER
comments: false
date: Mon, 19 Jul 2021 00:46:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60f51d84b15ec00256277582_1024.jpg'
---

<div>   
<p>IT 之家 7 月 19 日消息 智能手机很早前就已经用上生物识别认证，如指纹和人脸，这些功能在笔记本电脑甚至台式机上也变得越来越普遍。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202107/60f51d84b15ec00256277582_1024.jpg" data-height="720" data-width="1280" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60f51d84b15ec00256277582_1024.jpg" referrerpolicy="no-referrer"></div></div>微软的 Windows Hello 系统试图为其桌面平台带来同样的便利和安全组合，而且在大多数情况下表现出色。然而，新的安全研究显示，Windows Hello 的人脸识别过程中有一个致命的漏洞，那就是可以通过使用定制的 USB 设备绕过认证。幸运的是，在现实生活中要想利用这一漏洞并没有那么简单。<p></p><p>CyberArk 的安全研究人员发现，要想愚弄 Windows Hello 系统非常简单，或者至少是其面部识别系统。Windows 要求个人电脑有一个带有 RGB 和红外传感器的摄像头，以便 Windows Hello 面部识别系统能够工作。然而，事实证明，只有红外传感器的数据才是绕过 Windows 安全系统的关键。</p><p>IT 之家了解到，研究人员使用恩智浦的评估板开发了一个 USB 设备，将自己显示为一个带有 RGB 和红外传感器的 USB 摄像头。但实际上，该设备只是发送预制的图像帧：一些真实主人的红外帧和一些海绵宝宝的 RGB 帧。经过几次测试，研究人员发现，他们真的只需要一个红外帧和一个普通的黑色 RGB 帧来欺骗 Windows Hello。</p><p>据 CyberArk 称，该漏洞的存在是因为 Windows Hello 允许外部设备作为生物识别认证的数据源。一方面，微软别无选择，因为并非所有的 Windows PC 都有内置的摄像头或指纹传感器。另一方面，研究证明，它也是本应是万无一失的安全系统中最薄弱的环节。</p><p>幸运的是，要想利用这个漏洞，攻击者需要获得目标脸部的红外图像，而这并不容易。此外，他们还需要对台式机或笔记本电脑进行物理接触。</p><p>微软这边也作出了回应，称这是 Windows Hello 安全功能的绕过漏洞（bypass vulnerability），并且在本月的 13 日已经发布了补丁来解决这一问题。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            