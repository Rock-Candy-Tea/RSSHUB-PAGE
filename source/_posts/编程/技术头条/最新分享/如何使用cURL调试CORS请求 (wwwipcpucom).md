
---
title: '如何使用cURL调试CORS请求 (www.ipcpu.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4461'
author: 技术头条
comments: false
date: 2022-08-06 15:10:08
thumbnail: 'https://picsum.photos/400/300?random=4461'
---

<div>   
在实际的工作中，我们经常会遇到不通域名之间的js或者接口互相调用的情况，这就需要在被调用端设置CORSheader。CORS原理很简单，只需要向响应头header中注入Access-Control-Allow-Origin，这样浏览器检测到header中的Access-Control-Allow-Origin，就可以跨域操作了。
    
</div>
            