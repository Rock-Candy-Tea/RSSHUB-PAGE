
---
title: '时隔8年：Linux背光接口问题终于迎来大修补'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220918/s_3339890f47764d2ab91ec07f959bf559.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 18 Sep 2022 15:06:48 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220918/s_3339890f47764d2ab91ec07f959bf559.png'
---

<div>   
<p>2014年，红帽的开发者Hans de Goede发现，Linux的背光接口存在问题，无法将背光sysfs设备映射到显示器，且存在一个显示器需要适配多个背光sysfs设备、控制亮度需要root权限等问题。</p>
<p>而在本周的Linux Plumbers大会上，<span style="color:#ff0000;"><strong>时隔8年，Hans de Goede为Linux带来了显示亮度与背光接口问题的修复。</strong></span></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220918/3339890f47764d2ab91ec07f959bf559.png" target="_blank"><img alt="时隔8年：Linux背光接口问题终于迎来大修补" h="335" src="https://img1.mydrivers.com/img/20220918/s_3339890f47764d2ab91ec07f959bf559.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>根据Hans的介绍，为了解决这一问题，<strong>他为DRM连接器对象加入了新的“display_brightness”和“display_brightness_max”属性。</strong></p>
<p>同时，Hans也一并解决了背光值为0的问题，<strong>当display_brightness_max==0时，将定义为不支持控制亮度。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220918/58d8cd24ef9b48e1a4e71ab0991d35aa.png" target="_blank"><img alt="时隔8年：Linux背光接口问题终于迎来大修补" h="332" src="https://img1.mydrivers.com/img/20220918/s_58d8cd24ef9b48e1a4e71ab0991d35aa.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>目前，Hans de Goede已经公布了他在LPC 2022上的<a class="f14_link" href="https://lpc.events/event/16/contributions/1390/attachments/990/1916/kernel-recipes-backlight-2022-16x9.pdf" target="_blank">幻灯片</a>，并放出了修补该问题的<a class="f14_link" href="https://lore.kernel.org/all/20220825143726.269890-1-hdegoede@redhat.com/" target="_blank">内核补丁</a>。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220918/d2f5a3c4d5514f428b2a90ae0718fa33.jpg" target="_blank"><img alt="时隔8年：Linux背光接口问题终于迎来大修补" h="401" src="https://img1.mydrivers.com/img/20220918/s_d2f5a3c4d5514f428b2a90ae0718fa33.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

            
 <div style="overflow: hidden;font-size:14px;padding-top:30px;border-bottom:1px solid #eee;">
           <p class="zhuanzai">【本文结束】如需转载请务必注明出处：快科技</p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span></p>
        </div>
     
        
</div>
            