
---
title: 'Mozilla Firefox 91支持自动打开下载内容 就像Google Chrome一样'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0802/a42744a560a6099.jpg'
author: cnBeta
comments: false
date: Mon, 02 Aug 2021 09:23:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0802/a42744a560a6099.jpg'
---

<div>   
在Chrome中，当下载正在进行时，如果你点击它就会在底部看到一个 "在X秒内打开"的信息，下载完成后内容就会自动打开。Mozilla正在Firefox 91中对下载实施同样的行为，作为其致力于改进浏览器下载面板工作的一部分。<br><br>
<p>目前Firefox浏览器的下载体验是，开始下载并点击"保存文件"，随后Firefox浏览器通过其工具栏上的下载图标显示下载进度信息。一旦下载结束，可以从下载面板或在下载包含的文件夹中打开该文件。而如果你使用Chrome浏览器，下载过程中点击下载功能的区域，那么该文件下载完成后就会自动打开，而不需要你等待和返回查看。可见，Chrome浏览器带动了Firefox浏览器的制作者复制这一功能。</p><p>现在，Firefox 91已经支持在下载完成后自动打开，该功能目前处于pref阶段，默认情况下是禁用的。</p><p><img src="https://static.cnbetacdn.com/article/2021/0802/a42744a560a6099.jpg" title alt="Firefox-download-Panel-showing-open-in-7s-for-download.jpg" referrerpolicy="no-referrer"></p><p>通常情况下，Firefox浏览器会将下载保存到临时文件夹，并从那里将其移动到下载文件夹中。现在，如果你在91版Firefox浏览器中激活新的下载面板改进，并指定Firefox浏览器将下载存储在下载文件夹中，它现在会默认自动打开某些文件类型的下载。否则，某些文件将打开下载目录。</p><p>要在Firefox 91中启用类似于Chrome的下载完成时打开行为，请按如下步骤操作：</p><p>1.访问about:config</p><p>2.在设定页面中创建一个名为browser.download.improvements_to_download_panel的布尔值参数，并将其值设为true。</p><p>3.当下载面板显示下载正在进行时，点击它，随后Firefox会显示 "在X秒内打开"的信息。</p>   
</div>
            