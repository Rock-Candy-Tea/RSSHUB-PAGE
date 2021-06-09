
---
title: '今日分享：Vue3的createApp做了什么
核心要点—这些事儿不是vue3独有的，vue2也在做，只是外在表现不同，事情就是，根据模版创建DOM，把data里的数据塞进去，把D...'
categories: 
 - 编程
 - 掘金
 - 沸点
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e40d3ed3c7c4ebdb072caaa5934774f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 16:19:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e40d3ed3c7c4ebdb072caaa5934774f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
今日分享：Vue3的createApp做了什么<br>核心要点—这些事儿不是vue3独有的，vue2也在做，只是外在表现不同，事情就是，根据模版创建DOM，把data里的数据塞进去，把DOM渲染到页面上。<br>如图是简版的实现。<br>
            
          <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e40d3ed3c7c4ebdb072caaa5934774f~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"><br>
        
          <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45f529adb0da41e9aa1f12abd6a4e2a7~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"><br>
        <br>
          
</div>
            