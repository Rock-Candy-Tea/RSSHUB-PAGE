
---
title: '大佬们！萌新提问，为什么这个多线程里面我不添加sleep（），第一个线程就一直不释放锁，永远都是第一个线程在执行for循环，但是我用了sleep（），其他线程就可...'
categories: 
 - 编程
 - 掘金
 - 沸点
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc556b21b9a143399740b1e413c2b859~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:25:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc556b21b9a143399740b1e413c2b859~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
大佬们！萌新提问，为什么这个多线程里面我不添加sleep（），第一个线程就一直不释放锁，永远都是第一个线程在执行for循环，但是我用了sleep（），其他线程就可以抢到cup时间片和锁去执行，因为我的样本量已经放大到10w了，按理说不应该一直是线程一在执行啊？<br>
            
          <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc556b21b9a143399740b1e413c2b859~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"><br>
        <br>
          
</div>
            