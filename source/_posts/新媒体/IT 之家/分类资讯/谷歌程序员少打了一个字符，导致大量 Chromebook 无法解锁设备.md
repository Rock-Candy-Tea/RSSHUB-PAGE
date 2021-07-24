
---
title: '谷歌程序员少打了一个字符，导致大量 Chromebook 无法解锁设备'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/7/92812187-7e91-4b7c-b401-d36fef7124b2.png'
author: IT 之家
comments: false
date: Sat, 24 Jul 2021 07:20:12 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/7/92812187-7e91-4b7c-b401-d36fef7124b2.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 24 日消息 近日，谷歌为 Chromebook 推送了 Chrome OS 91 版本，版本号 <span class="accentTextColor">91.0.4772.165</span>。本次更新出现了重大 Bug，导致许多用户的 Chromebook <span class="accentTextColor">无法解锁设备</span>，官方已紧急撤销更新。</p><p>据用户反馈，在更新到该版本后，设备会卡在锁屏界面，无法进入桌面。即使用户输入了正确的密码，也无法使用，有的设备甚至会循环重启。</p><p>而开发者从<a href="https://chromium-review.googlesource.com/c/chromiumos/platform2/+/3039560/2/cryptohome/vault_keyset.cc#b471" target="_blank">谷歌官网源码</a>中发现，该问题是由一个极其低级的错误引发的。从下图可以看到，开发者在 if 判断语句中，两个条件之间的与连接符本来是“<span class="accentTextColor">&&</span>”，但开发者粗心只打了<span class="accentTextColor">一个“&”</span>，造成程序的运行错误，系统无法对用户登录信息进行解密。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/92812187-7e91-4b7c-b401-d36fef7124b2.png" w="1440" h="477" title="谷歌程序员少打了一个字符，导致大量 Chromebook 无法解锁设备" width="1440" height="272" referrerpolicy="no-referrer"></p><p>IT之家了解到，谷歌已紧急发布<span class="accentTextColor">修复补丁</span>解决了该问题，用户可放心更新了。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/a48ed491-2e9c-4878-ae4a-7ca18d5fbb92.png" w="1201" h="547" title="谷歌程序员少打了一个字符，导致大量 Chromebook 无法解锁设备" width="1201" height="373" referrerpolicy="no-referrer"></p>
          
</div>
            