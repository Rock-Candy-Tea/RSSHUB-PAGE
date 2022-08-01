
---
title: '作弊条：SSH 的 ProxyJump 跳板服务 (blog.delphij.net)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6757'
author: 技术头条
comments: false
date: 2022-08-01 01:00:19
thumbnail: 'https://picsum.photos/400/300?random=6757'
---

<div>   
有些环境中，SSH 服务器可能无法从 Internet 直接访问（例如，SSH 服务器可能使用的是一个私有 IP地址，或是 Internet 服务提供商没有提供 IPv6 服务，而 SSH 服务器只提供 IPv6 服务）。
    考虑到 SSH 已经进行了相互认证（连接时客户端会验证服务器的公钥是否与已知公钥，例如 ~/.ssh/known_hosts，或是通过 DNSsec 发布的 SSHFP RR 匹配；服务器端则会验证用户是否能证明自己拥有与授权公钥对应的私钥），因此比较常见的解决方法便是使用 VPN、在防火墙上穿孔，或是使用代理服务器。
    由于 SSH 自身也提供了许多转发功能，因此如果中间的跳板服务器也提供 SSH 服务，便可以使用这些跳转服务器直接作为代理服务器来用。与前面那些传统方法相比，这样做的优点是避免了安装额外的软件，也不需要特别指定端口。
    
</div>
            