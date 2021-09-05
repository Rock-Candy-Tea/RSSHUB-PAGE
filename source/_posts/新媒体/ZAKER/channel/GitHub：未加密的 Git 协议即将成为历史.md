
---
title: 'GitHub：未加密的 Git 协议即将成为历史'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61340ab68e9f092d0d48fa10_1024.jpg'
author: ZAKER
comments: false
date: Sat, 04 Sep 2021 16:53:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61340ab68e9f092d0d48fa10_1024.jpg'
---

<div>   
<p>IT 之家 9 月 5 日消息 微软 GitHub 近日发布博客，表示 " 将提高 GitHub 上的 Git 协议安全性 "，即将删除未加密的 Git 协议。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202109/61340ab68e9f092d0d48fa10_1024.jpg" data-height="664" data-width="1056" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61340ab68e9f092d0d48fa10_1024.jpg" referrerpolicy="no-referrer"></div></div>GitHub 官方宣布，正在更改 SSH 支持的密钥并删除未加密的 Git 协议，具体来说：<p></p><p>取消对所有 DSA 密钥的支持</p><p>添加对新添加的 RSA 密钥的要求</p><p>删除一些旧的 SSH 算法（HMAC-SHA-1 和 CBC 密码）</p><p>为 SSH 添加 ECDSA 和 Ed25519 主机密钥</p><p>关闭未加密的 Git 协议</p><p>GitHub 表示，这一改变仅影响使用 SSH 或 git:// 进行连接的仓库，以 https:// 开头的连接协议完全不受影响。</p><p>GitHub 官方认为，公钥密码术依赖于安全算法和足够强大的密钥来保持安全。" 更少的位数 " 通常意味着 " 更容易暴力破解 "，而较旧的算法也已经出现了攻击方式。考虑到计算能力的变化、新的攻击等，在 2001 年被认为是安全的密钥，今天可能不再安全了。</p><p>IT 之家了解到，GitHub 在上个月还宣布取消对 HTTPS 密码的支持，总之就是要确保 GitHub 用户数据的安全。官方表示，将继续观察使用 SHA-1 算法的 RSA 密钥，一旦出现风险或者过时，将向社区通报弃用它。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            