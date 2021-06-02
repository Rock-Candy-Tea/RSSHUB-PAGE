
---
title: '微软承认 Win10 新 Bug 可使部分 FLAC 格式音乐文件损坏，已发布紧急更新修复'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/6/3f8c2813-6516-4125-857e-0be06e2658ce.jpg'
author: IT 之家
comments: false
date: Tue, 01 Jun 2021 23:32:13 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/6/3f8c2813-6516-4125-857e-0be06e2658ce.jpg'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 2 日消息 根据微软发布的一份最新文档，Win10 文件管理器中存在一个 Bug，可<span class="accentTextColor">使部分 FLAC 格式音频文件损坏</span>。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/3f8c2813-6516-4125-857e-0be06e2658ce.jpg" alt="Windows 10 FLAC music files" w="696" h="365" title="微软承认 Win10 新 Bug 可使部分 FLAC 格式音乐文件损坏，已发布紧急更新修复" width="696" height="365" referrerpolicy="no-referrer"></p><p>微软称，在 Win10 2004 及以上版本中，如果<span class="accentTextColor">使用文件管理器修改 FLAC 音频文件的元数据</span>，比如标题、艺术家或者其他音频元数据，将使 FLAC 文件损坏，无法播放。</p><p>IT之家了解到，部分 FLAC 文件开头会包含<span class="accentTextColor"> ID3 帧头</span>，其中包含歌手、标题、专辑名称、年代、风格等信息。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/303c1865-0cbe-40c3-9752-3dab6475918c.png" w="543" h="771" title="微软承认 Win10 新 Bug 可使部分 FLAC 格式音乐文件损坏，已发布紧急更新修复" width="543" height="771" referrerpolicy="no-referrer"></p><p>而在 Win10 2004 及以上版本中，<span class="accentTextColor">文件资源管理器会忽略 ID3 帧头，因为它默认判定 FLAC 文件使用 4 字节 fLaC 开头</span>。因此当用户使用文件资源管理器修改 FLAC 文件的元数据时，就会把 ID3 帧头覆盖掉，从而破坏原有的 FLAC 文件结构，使音乐播放器无法正常识别。</p><p>微软已针对该 Bug 发布了紧急修复更新，<span class="accentTextColor">在 KB5003214 更新中，微软确认已修复该问题</span>，大家安装即可。</p>
          
</div>
            