
---
title: 'OpenSSH 8.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2014'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2014'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenSSH 8.6 已发布，OpenSSH 是 100％ 完整的 SSH 协议 2.0 版本的实现，并且包括 sftp 客户端和服务器支持，它用于远程登录的主要连接工具。OpenSSH 对所有流量进行加密，避免窃听、连接劫持等攻击。此外，OpenSSH 还提供了一整套安全隧道功能、多种身份验证方法和复杂的配置选项。</p> 
<p>自 OpenSSH 8.5 以来的变更主要集中在 Bugfix，此外还引入了部分新功能。</p> 
<p><strong>Bugfix</strong></p> 
<ul> 
 <li>ssh_config(5), sshd_config(5)：在手册页中使用当前默认值同步 CASignatureAlgorithms 列表</li> 
 <li>ssh(1)：确保退出前调用 pkcs11_del_provider() </li> 
 <li>ssh(1), sshd(8)：修复 string->argv 的转换问题，多个反斜杠没有被正确引用，并且字符串中的引号空间被错误地分割</li> 
 <li>ssh(1)：当被信号杀死时返回非零退出状态</li> 
 <li>sftp-server(8)：增加 SSH2_FXP_READ 最大值以匹配最大数据包的大小，同时处理规范中没有明确禁止的零长度的读取</li> 
</ul> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>sftp-server(8)：增加了一个新的 limits@openssh.com 协议扩展，允许客户端发现多项服务器限制，包括最大数据包大小和最大读/写长度</li> 
 <li>sftp(1)：使用新的 limits@openssh.com 扩展 (当可用时) 以在客户端中选择更好的传输长度</li> 
 <li>sshd(8)：在 sshd_config 中增加 ModuliFile 关键字，以指定包含 DH-GEX 组的"moduli"文件的位置</li> 
 <li>unit tests：增加了 TEST_SSH_ELAPSED_TIMES 环境变量，以便能够打印出每个测试的耗时（以秒为单位）</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssh.com%2Ftxt%2Frelease-8.6" target="_blank">详情查看 release notes</a>。</p> 
<p>此外， 由于 SHA-1 哈希算法被发现构造前缀碰撞<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feprint.iacr.org%2F2020%2F014.pdf" target="_blank">攻击成本已降至低于 5 万美元</a>（实际为 4.5 万美元），因此开发团队决定禁用 ssh-rsa 公钥签名算法，但这并不意味着要停止使用 RSA 公钥，在 SSH 协议中，它仍然能配合不同算法用于签名。例如  ssh-rsa 可以用 rsa-sha2-256(RSA/SHA256)、rsa-sha2-512(RSA/SHA512) 和 ssh-rsa(RSA/SHA1) 进行签名，只有最后一个将被默认禁用。</p>
                                        </div>
                                      
</div>
            