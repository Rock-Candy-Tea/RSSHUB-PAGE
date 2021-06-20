
---
title: '苹果 iPhone 新 Bug 可禁用 WiFi，附解决方法'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png'
author: IT 之家
comments: false
date: Sat, 19 Jun 2021 23:54:27 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 20 日消息 安全人员 Carl Schou 近日发现了一个苹果 iPhone 的奇特 Bug，可使 <span class="accentTextColor">WiFi 功能</span><span class="accentTextColor">无法使用</span>。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png" w="660" h="732" title="苹果 iPhone 新 Bug 可禁用 WiFi，附解决方法" width="660" height="732" referrerpolicy="no-referrer"></p><p>根据 Carl Schou 的表述，该 Bug 的触发方式也十分简单，用户需要将 WiFi SSID 改为 <span class="accentTextColor">%p%s%s%s%s%n</span>，当苹果 iPhone 连接到该 WiFi 时，就会导致 WiFi 功能<span class="accentTextColor">无法开启</span>，同时 AirDrop、AirPlay 等功能也无法使用。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/7fddac7f-c51a-41f1-b5f0-88aa81a13fbe.png" w="732" h="233" title="苹果 iPhone 新 Bug 可禁用 WiFi，附解决方法" width="732" height="233" referrerpolicy="no-referrer"></p><p>从下图可以看到，WiFi 功能无法正常打开，打开开关之后就会立即关闭。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/f360e967-04d6-4c48-9d17-ab420db7bdc7.gif" w="316" h="681" title="苹果 iPhone 新 Bug 可禁用 WiFi，附解决方法" width="316" height="681" referrerpolicy="no-referrer"></p><p>不过，该 Bug 并不是永久的，用户只需要<span class="accentTextColor">在设置中重置网络</span>即可。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/05a4b1fd-f78b-4517-9a6d-7632b0546102.png" w="749" h="307" title="苹果 iPhone 新 Bug 可禁用 WiFi，附解决方法" width="749" height="307" referrerpolicy="no-referrer"></p><p>IT之家了解到，Carl Schou 并没有指出该 Bug 触发的原因，不过据外媒 9to5Mac，可能是由于 C 语言中 <span class="accentTextColor">%n</span> 用于在字符串中插入变量，而上述的 <span class="accentTextColor">%p%s%s%s%s%n</span> 是以 <span class="accentTextColor">%n</span> 结尾，因此导致了 iPhone 无法识别到具体变量，只能报错并关闭 WiFi。</p><p>家里有熊孩子的IT之家网友，你们学会了吗？</p>
          
</div>
            