
---
title: '微软封杀漏洞后，网友又挖出了 Win11 家庭版新的离线激活方法'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/390866dc-100e-491a-9431-afa9b8b08d19.png'
author: IT 之家
comments: false
date: Sun, 12 Sep 2021 15:01:08 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/390866dc-100e-491a-9431-afa9b8b08d19.png'
---

<div>   
<p data-vmark="e290"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 9 月 12 日消息 微软对 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 家庭版用户规定了特殊要求，要求用户必须在 OOBE 联网登录微软账户后方可进入桌面从而完成系统激活，而专业版和企业版都没有这一限制因此可直接创建本地账户。</p><p data-vmark="4d83">IT之家了解到，此前网友 Adam (warwagon) 发现，直接拔下网线并“Alt + F4”关闭提示窗即可绕过 OOBE 限制创建本地账户，但很可惜在经过泛滥传播后已经被微软封杀。</p><p data-vmark="bfd1">有趣的是，现在他又找出了一个新的漏洞，现在需要安装 Windows 11 家庭版的用户在首次配置开机向导时可通过以下步骤绕过联网要求实现离线激活：</p><ul class=" list-paddingleft-2"><li><p data-vmark="6aae">在 OOBE 提示联网的界面同时按下 Shift + F10 打开命令行</p></li><li><p data-vmark="a194" style="text-align: left;">在命令行窗口输入 taskmgr 并回车找到并结束 Network Connection Flow 进程，或者直接输入 taskkill /F/IM oobenetworkconnectionflow.exe 结束上述进程</p></li><li><p data-vmark="c6f9">现在你就会发现已经可以正常通过 OOBE 创建本地账户</p></li></ul><p data-vmark="2ac8"><img src="https://img.ithome.com/newsuploadfiles/2021/9/390866dc-100e-491a-9431-afa9b8b08d19.png" w="1077" h="821" title="微软封杀漏洞后，网友又挖出了 Win11 家庭版新的离线激活方法" width="1077" height="625" referrerpolicy="no-referrer"></p>
          
</div>
            