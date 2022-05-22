
---
title: 'App开放接口api安全：Token签名sign的设计与实现 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9357'
author: 技术头条
comments: false
date: 2022-05-22 06:11:49
thumbnail: 'https://picsum.photos/400/300?random=9357'
---

<div>   
在app开放接口api的设计中，避免不了的就是安全性问题，因为大多数接口涉及到用户的个人信息以及一些敏感的数据，所以对这些 接口需要进行身份的认证，那么这就需要用户提供一些信息，比如用户名密码等，但是为了安全起见让用户暴露的明文密码次数越少越好，我们一般在web项目 中，大多数采用保存的session中，然后在存一份到cookie中，来保持用户的回话有效性。
    
</div>
            