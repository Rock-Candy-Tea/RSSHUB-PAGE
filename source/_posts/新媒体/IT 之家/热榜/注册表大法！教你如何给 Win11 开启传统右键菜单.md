
---
title: '注册表大法！教你如何给 Win11 开启传统右键菜单'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_093736_962.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_7'
author: IT 之家
comments: false
date: Sun, 04 Jul 2021 02:26:22 GMT
thumbnail: 'https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_093736_962.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_7'
---

<div>   
<h2>前言</h2><p>Win11 的新右键菜单虽然简洁，但是用起来感觉并不如传统右键菜单顺手，可能需要时间来学习适应吧。因此发本帖帮助和我有同样需求的 IT 之家家友们，在 Win11 上无需点击 “show more options” 直接呼出传统右键菜单。</p><h2>效果如下</h2><p><img src="https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_093736_962.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_7" title="注册表大法！教你如何给 Win11 开启传统右键菜单" referrerpolicy="no-referrer"></p><h2>实现方法（末尾附注册表导入）</h2><p>1. Win+R 运行，输入 Regedit，打开注册表编辑器。</p><p>2. 定位到 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FeatureManagement\Overrides\4 右击创建新的项，命名为 586118283</p><p><img src="https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_094736_241.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_9" title="注册表大法！教你如何给 Win11 开启传统右键菜单" referrerpolicy="no-referrer"></p><p>3. 在创建的新项右侧窗格创建 5 个 DWORD 为：EnabledState、EnabledStateOptions、Variant、VariantPayload、VariantPayloadKind。这 5 个 DWORD 分别对应值见下图。</p><p><img src="https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_094749_903.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_9" title="注册表大法！教你如何给 Win11 开启传统右键菜单" referrerpolicy="no-referrer"></p><p>4. 完成，重启电脑即可直接在 Win11 中呼出传统右键菜单。</p><p><img src="https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_094809_507.png?x-bce-process=image/watermark,image_aW1nL3dhdGVybWFyay9xYy9xYzEwMC5wbmc=,g_7" title="注册表大法！教你如何给 Win11 开启传统右键菜单" referrerpolicy="no-referrer"></p><h2>附注册表导入</h2><p>蓝奏云：<a href="https://vier.lanzoui.com/iKsUNqzf08j" target="_blank">下载地址</a></p><p>密码：6q7b</p><p>百度云：<a href="https://pan.baidu.com/s/16KpJfunq7A7epi04RtFxvw" target="_blank">下载地址</a> </p><p>提取码：eumt</p><p><br></p><p><img src="https://img.ithome.com/mpimg/content/41922888/2021/7/20210704_100104_543.gif" title="注册表大法！教你如何给 Win11 开启传统右键菜单" referrerpolicy="no-referrer"></p>
          
</div>
            