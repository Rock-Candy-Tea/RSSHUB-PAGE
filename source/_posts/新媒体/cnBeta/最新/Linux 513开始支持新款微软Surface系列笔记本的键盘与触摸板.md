
---
title: 'Linux 5.13开始支持新款微软Surface系列笔记本的键盘与触摸板'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0330/1ce28647192f315.jpg'
author: cnBeta
comments: false
date: Tue, 30 Mar 2021 10:59:36 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0330/1ce28647192f315.jpg'
---

<div>   
改善Linux下微软Surface笔记本支持的探索还在继续。随着Linux 5.13的发布，不仅有Surface
DTX驱动，<strong>另一个新的Surface驱动
"surface-hid"将允许在较新的Surface设备上支持键盘和触摸板。</strong><br>
 <p>目前较新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a><a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a>设备，如Surface Laptop
3和Surface Book 3在运行主线内核时，这些硬件功能无法正常运行。</p><p><a href="https://static.cnbetacdn.com/article/2021/0330/1ce28647192f315.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0330/1ce28647192f315.jpg" title alt="et6oe973c1v41.jpg" referrerpolicy="no-referrer"></a></p><p>虽然一直有树外补丁/DKMS模块能够安装后使用，但作为畅销机型，Linux 5.13内核理应有支持与主线内核，现在surface-hid驱动已经进入HID的"-next "分支，这意味着在4月Linux 5.13合并窗口打开之前我们就可以看到它。</p><p>不过需要注意的是，这个Surface HID驱动不是微软的作品，而是Maximilian Luz的作品。Maximilian继续近乎单枪匹马地在Linux上改进微软Surface状态。这位独立开发者撰写了许多Linux的Surface驱动和其他改进，以便在Linux上更好地支持Surface。</p><p>由于连接到微软Surface系统聚合模块需要这个HID驱动来获得工作中的触摸板和键盘支持。Luz去年将微软"SAM"对Linux的支持预先安排妥当，它是这些设备使用的嵌入式控制器（EC，笔记本中的重要部件）。这样一来，随着这个HID for-next补丁超过600行新代码的加入，微软Surface Laptop 3/Surface Book 3及以后的键盘和触摸板终于可以在新款Linux内核上开箱即用了。</p><p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-next&id=b05ff1002a5c19f2fd511c6eada6f475ff701841" _src="https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-next&id=b05ff1002a5c19f2fd511c6eada6f475ff701841" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-next&id=b05ff1002a5c19f2fd511c6eada6f475ff701841</a><br></p>   
</div>
            