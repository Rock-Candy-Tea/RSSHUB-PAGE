
---
title: 'GitHub：未加密的 Git 协议即将成为历史'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/f5e52abc-4911-4f60-aa42-e73f92c49f81.png'
author: IT 之家
comments: false
date: Sun, 05 Sep 2021 00:00:47 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/f5e52abc-4911-4f60-aa42-e73f92c49f81.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 9 月 5 日消息 微软 GitHub 近日发布<a href="https://github.blog/2021-09-01-improving-git-protocol-security-github/" target="_blank">博客</a>，表示“将提高 GitHub 上的 Git 协议安全性”，即将删除未加密的 Git 协议。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/9/f5e52abc-4911-4f60-aa42-e73f92c49f81.png" w="1056" h="664" title="GitHub：未加密的 Git 协议即将成为历史" width="1056" height="516" referrerpolicy="no-referrer"></p><p>GitHub 官方宣布，<span class="accentTextColor">正在更改 SSH 支持的密钥并删除未加密的 Git 协议</span>，具体来说：</p><ul class=" list-paddingleft-2"><li><p>取消对所有 DSA 密钥的支持</p></li><li><p>添加对新添加的 RSA 密钥的要求</p></li><li><p>删除一些旧的 SSH 算法（HMAC-SHA-1 和 CBC 密码）</p></li><li><p>为 SSH 添加 ECDSA 和 Ed25519 主机密钥</p></li><li><p>关闭未加密的 Git 协议</p></li></ul><p>GitHub 表示，这一改变<span class="accentTextColor">仅影响使用 SSH 或 git:// 进行连接的仓库</span>，以 https:// 开头的连接协议完全不受影响。</p><p>GitHub 官方认为，公钥密码术依赖于安全算法和足够强大的密钥来保持安全。“更少的位数”通常意味着“更容易暴力破解”，而较旧的算法也已经出现了攻击方式。考虑到计算能力的变化、新的攻击等，在 2001 年被认为是安全的密钥，今天可能不再安全了。</p><p>IT之家了解到，GitHub 在上个月还宣布取消对 HTTPS 密码的支持，总之就是要确保 GitHub 用户数据的安全。官方表示，将继续观察使用 SHA-1 算法的 RSA 密钥，一旦出现风险或者过时，将向社区通报弃用它。</p>
          
</div>
            