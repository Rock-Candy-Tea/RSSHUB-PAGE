
---
title: '微软Edge 94稳定版发布 迎来新的四周发布周期和"扩展稳定"通道'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0925/235d4557015c9ae.png'
author: cnBeta
comments: false
date: Sat, 25 Sep 2021 09:33:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0925/235d4557015c9ae.png'
---

<div>   
<strong>微软Edge 94现在可以在稳定频道中使用，这个版本标志着从6周到4周的发布周期的转换。</strong>微软在3月份解释说，这种更快的发布周期将为Edge用户带来更密集的新功能，但该公司还为企业用户提供了一个新的8周"扩展稳定"发布周期选项，每两周进行一次安全更新。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0925/235d4557015c9ae.png" title alt="Picture1.png" referrerpolicy="no-referrer"></p><p>要选择8周的"扩展稳定"发布周期选项，IT管理员将需要使用组策略或通过微软端点管理器中的Intune选择新的渠道选项。该公司解释说，微软Edge稳定版的8周"扩展稳定"发布周期选项将从微软Edge 94开始提供与偶数版一致的累积功能更新；奇数版的任何功能更新将被打包并作为后续偶数版的一部分提供。</p><p>微软Edge 94是一个相当小的版本，有安全改进和一个新的无障碍设置页面。你可以在下面找到改进清单：</p><ol style="list-style-type: decimal;" class=" list-paddingleft-2"><li><p>对打开MHTML文件的默认行为的改进。如果启用了IE模式，MHTML文件将继续以IE模式打开，除非MHTML文件是从Microsoft Edge保存的（使用Microsoft Edge中的"另存为"或"另存页面"选项）。如果该文件是从Microsoft Edge保存的，它现在将在Microsoft Edge中打开。这一变化将修复从Microsoft Edge保存的MHTML文件在IE模式下打开时出现的渲染问题。</p></li><li><p>将私密网络请求限制在安全范围内。从互联网上的页面访问本地（内网）网络上的资源，需要这些页面通过HTTPS交付。这一变化发生在Chromium项目中，而Microsoft Edge是基于该项目。欲了解更多信息，请浏览Chrome平台状态条目。有两种兼容性策略可用，以支持需要保留与非安全页面的兼容性的情况。InsecurePrivateNetworkRequestAllowed 和 InsecurePrivateNetworkRequestAllowedForUrls。</p></li><li><p>阻止混合内容的下载。安全页面将只下载托管在其他安全页面上的文件，如果从安全页面启动，托管在非安全（非HTTPS）页面上的下载将被阻止。这一变化发生在Chromium项目中，Microsoft Edge是基于该项目。欲了解更多信息，请浏览Google安全博客条目。</p></li><li><p>为企业内部账户启用隐式登录。通过启用OnlyOnPremisesImplicitSigninEnabled策略，只有企业内部账户将被启用隐式登录。Microsoft Edge不会尝试隐式登录到MSA或AAD账户。从企业内部账户升级到AAD账户也将被停止。</p></li><li><p>新的可访问性设置页面。Edge现在把与可访问性有关的设置集中在一个页面上。你可以在主设置列表下找到新的edge://settings/accessibility页面。在这里，你可以找到使网页变大的设置，在焦点区域周围显示高能见度的轮廓，以及其他可以帮助改善你的网页浏览体验的设置。未来的Microsoft Edge版本会继续在这里添加新的设置。</p></li><li><p>由于微软Edge的更新现在跟随Chromium的更新，GoogleChrome浏览器也从本周早些时候发布的Chrome 94开始转为4周的发布周期。就像微软一样，Google也开始为其<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>和macOS上的Chrome浏览器提供新的扩展渠道选项。</p></li></ol>   
</div>
            