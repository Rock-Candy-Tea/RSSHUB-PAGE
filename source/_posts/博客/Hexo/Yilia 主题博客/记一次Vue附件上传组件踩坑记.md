
---
title: '记一次Vue附件上传组件踩坑记'
categories: 
 - 博客
 - Hexo
 - Yilia 主题博客
headimg: 'https://picsum.photos/400/300?random=3528'
author: Hexo
comments: false
date: Thu, 30 Nov 2017 01:13:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=3528'
---

<div>   
上个礼拜刚刚结束一个Vue项目，这个项目分为移动端和桌面端，由于UI差异较大，分别建立了各自的Git仓库，公共代码部分通过Git Subtree共享。其中比较折腾的就是附件上传组件，这个组件有什么特点呢?

业务有大量附件要上传，包括图片和非图片，以及文件多选，图片类需要有预览
这个项目包括移动端和桌面端，希望能够复用非UI部分的代码
对于移动端，图片上传需要支持拍照上传，这对于iOS问题不大，可是安卓就坑了。
尤其移动端上的图片，一般都是手机拍照图片，像素可谓不小，需要进行压缩再上传，以加快上传速度、减少带宽占用

      
      
</div>
            