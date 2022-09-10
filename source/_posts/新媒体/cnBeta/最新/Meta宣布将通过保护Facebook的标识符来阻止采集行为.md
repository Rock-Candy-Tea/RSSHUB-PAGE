
---
title: 'Meta宣布将通过保护Facebook的标识符来阻止采集行为'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0910/c1c53a73fa31a46.webp'
author: cnBeta
comments: false
date: Sat, 10 Sep 2022 07:02:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0910/c1c53a73fa31a46.webp'
---

<div>   
作为正在进行的解决数据滥用系列的一部分，Meta最近分享了关于我们的外部数据滥用（EDM）团队如何保护人们免受克隆网站的影响的最新情况。今天，官方在博客详细介绍了在Facebook上阻止采集Facebook标识符（FBIDs）的方法。<br>
 <p>大多数公司在其网站的URL中使用独特的标识符。识别符是一种唯一引用人或内容的方式，如帖子、图片和视频。在Facebook内部，这些标识符被称为FBID，用它们来为人们加载内容。</p><p>采集是指从网站或应用程序中自动收集数据，这可以是在授权下进行的，也可以是未经授权的。未经授权的采集通常涉及猜测标识符，或使用购买的标识符来采集人们的数据。在某些情况下，采集者收集标识符，并碰撞交叉筛选电话号码或其他可公开获得的数据，以创建可重复使用的数据集，这些数据有时会被出售牟利。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0910/c1c53a73fa31a46.webp" title alt="01_URL.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图为一个Facebook帖子的例子，其URL中含有PFBID</p><p>有鉴于此，Meta创建了假名化的Facebook标识符（PFBIDs），它结合了时间戳和FBIDs，生成了一个独特的时间旋转标识符。随着逐步取消访问原始标识符的能力，这有助于阻止未经授权的数据刮擦，使攻击者更难猜测、连接和重复访问数据。</p><p>这些标识符的设计并不是为了防止浏览器工具从URL中删除跟踪组件，这个过程是为了更好地保护人们的隐私不受某些类型的枚举和延时攻击的影响，同时保留了长效链接的能力。</p><p>用户可以在Facebook的"隐私事务"页面上阅读关于隐私举措的其他更新和见解：</p><p><a href="https://about.fb.com/news/tag/privacy-matters/" _src="https://about.fb.com/news/tag/privacy-matters/" target="_blank">https://about.fb.com/news/tag/privacy-matters/</a><br></p>   
</div>
            