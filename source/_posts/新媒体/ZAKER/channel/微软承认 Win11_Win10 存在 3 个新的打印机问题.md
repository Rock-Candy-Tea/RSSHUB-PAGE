
---
title: '微软承认 Win11_Win10 存在 3 个新的打印机问题'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/6168d4c6b15ec07e154700e4_1024.jpg'
author: ZAKER
comments: false
date: Thu, 14 Oct 2021 20:32:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/6168d4c6b15ec07e154700e4_1024.jpg'
---

<div>   
<p>IT 之家 10 月 15 日消息，据 MSPoweruser 报道，最近在 Windows 的打印机堆栈中发现的重大漏洞以及随后的补救措施似乎对 Windows 11 造成了重大的兼容性问题，微软为其新发布的操作系统确认了 3 个新的打印机相关问题。值得注意的是这个问题也影响到 Windows 10，而且这个问题似乎只限于企业打印，因为企业打印使用的协议更复杂。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202110/6168d4c6b15ec07e154700e4_1024.jpg" data-height="508" data-width="803" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/6168d4c6b15ec07e154700e4_1024.jpg" referrerpolicy="no-referrer"></div></div><strong>下面是问题描述和解决方法</strong><p></p><p>通过某些网络连接尝试安装打印机时可能失败</p><p>首次尝试连接到网络打印机的设备可能无法下载和安装必要的打印机驱动程序。</p><p>IT 之家获悉，微软表示，这个问题已经通过打印服务器访问打印机的设备观察到，这些设备使用 HTTP 连接。当客户端连接到服务器来安装打印机时，会发生目录不匹配，导致安装程序文件生成不正确。因此，驱动程序可能无法下载。</p><p>解决方法：具有管理权限的 IT 管理员仍然可以通过其他方式在客户端安装打印机驱动程序，例如从已知的良好软件包位置复制打包的驱动程序。只有自动下载和安装过程会受到这个问题的影响。</p><p>自定义打印属性可能无法正确提供给打印服务器客户端</p><p>在该服务器上定义的打印属性可能无法正确提供给客户。注意这个问题是针对打印服务器的，不影响标准网络打印。这个问题不会导致打印操作失败，但是，在服务器上定义的自定义设置 —— 例如，双面打印设置 —— 将不会被自动应用，客户端将只用默认设置进行打印。</p><p>这个问题是由于包含打印机属性的数据文件构建不当造成的。收到该数据文件的客户端将无法使用该文件的内容，而是以默认的打印设置进行。使用默认打印设置和没有自定义设置提供给客户端的服务器不受影响。</p><p>解决办法：具有管理权限的 IT 管理员仍然可以通过其他方式在客户机上安装打印机驱动程序，例如从已知的良好软件包位置复制打包的驱动程序。此外，仍然可以手动修改客户端以采用所需的打印机设置。</p><p>通过互联网打印协议（IPP）安装打印机可能不成功</p><p>使用互联网打印协议（IPP）的打印机安装可能无法成功完成。</p><p>微软正在研究所有问题的解决方案，并计划在未来的更新中发布。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            