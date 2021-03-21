
---
title: 云函数通过tencentcloud-sdk-nodejs向腾讯云请求成功，却返回null？
categories: 
    - 编程
    - 微信开放平台 - 微信开放社区 - 小程序问答
author: 微信开放平台 - 微信开放社区 - 小程序问答
comments: false
date: Sun, 21 Mar 2021 13:45:10 GMT
thumbnail: http://mmbiz.qpic.cn/mmbiz_jpg/TgCrUBb8VXUsvqzn4xlEd7b87kXb7KNbrHRv8uFB9PZIz3uBAW7gibfmUNEbCavBrxB2ic7Zp8whV1l1eKBhibGCw/0?wx_fmt=jpeg
---

<div>   
<p>为什么云函数通过tencentcloud-sdk-nodejs向腾讯云人脸识别接口请求成功，却总是返回null？</p><p>以下云函数的代码完全根据腾讯云人脸识别接口给出的官方代码编写，return也写了，为什么在小程序控制台却总是返回null？</p><p><img src="http://mmbiz.qpic.cn/mmbiz_jpg/TgCrUBb8VXUsvqzn4xlEd7b87kXb7KNbrHRv8uFB9PZIz3uBAW7gibfmUNEbCavBrxB2ic7Zp8whV1l1eKBhibGCw/0?wx_fmt=jpeg" referrerpolicy="no-referrer"></p><p>小程序控制台返回数据总是null</p><p><img src="http://mmbiz.qpic.cn/mmbiz_png/TgCrUBb8VXUsvqzn4xlEd7b87kXb7KNbkbiaDVtg9cFK5kcVYuia1yL1iajhQcXyFJVE0Cl7odQhLrlNs0MNXuzZQ/0?wx_fmt=png" referrerpolicy="no-referrer"></p><p>查看云函数日志也是null,通过日志可以看到明明是请求成功的！</p><p><img src="http://mmbiz.qpic.cn/mmbiz_png/TgCrUBb8VXUsvqzn4xlEd7b87kXb7KNb7uIlicqtWSOgQZib20A6GY3wFQExdO3hEnfBictibgPCFLicGUafHafueFQ/0?wx_fmt=png" referrerpolicy="no-referrer"></p>  
</div>
            