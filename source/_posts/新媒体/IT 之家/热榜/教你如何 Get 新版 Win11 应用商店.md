
---
title: '教你如何 Get 新版 Win11 应用商店'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/8/f0e39c61-1891-42ba-8c00-b83672ffa03b.png'
author: IT 之家
comments: false
date: Sat, 21 Aug 2021 00:25:37 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/8/f0e39c61-1891-42ba-8c00-b83672ffa03b.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 8 月 21 日消息 目前许多用户已经成功更新了 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 预览版操作系统，目前的最新版本为 Build 22000.160。但是许多用户在升级完系统后，或者使用第三方制作的 ISO 安装系统之后，Microsoft Store 应用商店仍停留在 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Win10</a> 旧版。这种情况下，仅依靠系统更新或者应用商店内更新，是无法获取新版 Microsoft Store 的，需要进行手动更新操作。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/f0e39c61-1891-42ba-8c00-b83672ffa03b.png" w="1313" h="1075" title="教你如何 Get 新版 Win11 应用商店" width="1313" height="671" referrerpolicy="no-referrer"></p><p>以下为 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 获取新版应用商店的步骤：</p><h2>1、卸载旧版 Microsoft Store</h2><p>首先使用键盘快捷键“Win+X”打开菜单，然后启动“Windows 终端（管理员）”</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/42e29aaa-6aa2-4eb7-9849-7553433b497e.png" w="563" h="630" title="教你如何 Get 新版 Win11 应用商店" width="563" height="630" referrerpolicy="no-referrer"></p><p>输入以下命令，并按回车键执行。</p><pre class="brush:javascript;toolbar:false">get-appxpackage *store* | remove-Appxpackage</pre><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/f71f7524-9ca4-409f-a0b8-ba3265e0d30b.png" w="736" h="453" title="教你如何 Get 新版 Win11 应用商店" width="736" height="453" referrerpolicy="no-referrer"></p><h2>2、安装新版 Microsoft Store</h2><p>卸载旧版本之后，建议等待几分钟，然后再执行新版安装操作。PowerShell 窗口不要关闭，继续执行以下指令：</p><pre class="brush:javascript;toolbar:false ai-word-checked">add-appxpackage -register "C:\Program Files\WindowsApps\*Store*\AppxManifest.xml" -disabledevelopmentmode</pre><p>此时，会从服务器自动获取最新的应用商店。如果安装成功，则会在开始菜单看到全新的“Microsoft Store”图标，打开后即可正常运行。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/3de9e0ab-a0de-421c-a902-f8b551059238.png" w="631" h="384" title="教你如何 Get 新版 Win11 应用商店" width="631" height="384" referrerpolicy="no-referrer"></p><p>新版应用商店更新后，左上角显示有“预览”字样，证明这并不是最终发行版本。截至发稿，这一应用的版本号为 <span class="accentTextColor">22107.1401.4.0</span>。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/c1c73b46-6832-408a-8762-82e7ca34d5bd.png" w="975" h="869" title="教你如何 Get 新版 Win11 应用商店" width="975" height="731" referrerpolicy="no-referrer"></p><p>与之前相比，新版应用商店的标签移至左侧纵向排列，同时应用内的动画效果得到极大的丰富。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/8c8c0c18-9a2d-4621-9c74-650f2acf2fb6.png" w="1066" h="971" title="教你如何 Get 新版 Win11 应用商店" width="1066" height="747" referrerpolicy="no-referrer"></p><p>▲ Win11 版应用商店</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/4ef2a1a4-da30-4ef4-bfd3-0b0953d871e0.jpg@s_2,w_820,h_580" w="1419" h="1004" title="教你如何 Get 新版 Win11 应用商店" srcset="https://img.ithome.com/newsuploadfiles/2021/8/4ef2a1a4-da30-4ef4-bfd3-0b0953d871e0.jpg 2x" width="1419" height="580" referrerpolicy="no-referrer"></p><p>▲ Win10 版应用商店</p><p>新版 Microsoft Store 在使用时，如需检查更新，需要点击左下角的“库”按钮，而不需要单击账户图标然后再选择下载更新。在“库”页面中，用户可以分类查看已购买的 App，并自定义排序。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/8/7a8b8a7c-e9ee-4199-9280-db94ecd69384.png" w="1066" h="971" title="教你如何 Get 新版 Win11 应用商店" width="1066" height="747" referrerpolicy="no-referrer"></p>
          
</div>
            