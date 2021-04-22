
---
title: 'Android 实现小红书登陆页面背景图无限滚动效果 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9638'
author: 技术头条
comments: false
date: 2021-04-22 00:27:32
thumbnail: 'https://picsum.photos/400/300?random=9638'
---

<div>   
通过 uiautomatorviewer 分析页面布局，其应是通过自定义 FrameLayout 实现
通过清除 App 数据同时断开数据连接再启动该页面，确定背景加载的是本地图片
通过小红书 apk 获取资源文件，确定背景图片为单张图片
    
</div>
            