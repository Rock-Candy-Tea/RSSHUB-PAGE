
---
title: 'OpenSSH 8.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2943'
author: 开源中国
comments: false
date: Sun, 22 Aug 2021 08:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2943'
---

<div>   
<div class="content">
                                                                                            <p>OpenSSH 8.7 已发布，OpenSSH 是 100％ 完整的 SSH 协议 2.0 版本的实现，并且包括 sftp 客户端和服务器支持，它用于远程登录的主要连接工具。OpenSSH 对所有流量进行加密，避免窃听、连接劫持等攻击。此外，OpenSSH 还提供了一整套安全隧道功能、多种身份验证方法和复杂的配置选项。</p> 
<p>主要新特性包括：</p> 
<ul> 
 <li>实验性支持使用 SFTP 作为文件传输协议，替代<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flwn.net%2FArticles%2F835962%2F" target="_blank">不再安全的 scp 协议</a></li> 
 <li>改变远程到远程的复制行为，默认通过本地主机传输</li> 
 <li>使用更严格的配置文件解析器</li> 
 <li>准备在下一个版本中默认停用 ssh-rsa 签名方案。鼓励用户现在迁移到更好、更安全的替代方案</li> 
 <li>错误修复和其他小的改进</li> 
</ul> 
<p>之所以默认停用 ssh-rsa 签名方案， 这是由于 SHA-1 哈希算法被发现构造前缀碰撞<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feprint.iacr.org%2F2020%2F014.pdf" target="_blank">攻击成本已降至低于 5 万美元</a>（实际为 4.5 万美元），因此开发团队决定停用 ssh-rsa 公钥签名算法，但这并不意味着要停止使用 RSA 公钥，在 SSH 协议中，它仍然能配合不同算法用于签名。例如  ssh-rsa 可以用 rsa-sha2-256(RSA/SHA256)、rsa-sha2-512(RSA/SHA512) 和 ssh-rsa(RSA/SHA1) 进行签名，只有最后一个将被默认禁用。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssh.com%2Ftxt%2Frelease-8.7" target="_blank">详情查看 release notes</a>。</p>
                                        </div>
                                      
</div>
            