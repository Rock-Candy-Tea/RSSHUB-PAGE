
---
title: 'OpenSSH 9.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1512'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1512'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenSSH 是使用 SSH 协议进行远程登录的首要连接工具。它对所有通信进行加密，以消除窃听、连接劫持和其他攻击。此外，OpenSSH 还提供了一套大型的安全隧道功能、几种认证方法和复杂的配置选项。</p> 
<p>OpenSSH 是由 OpenBSD 项目的一些开发者开发的，并在 BSD-style 的许可下提供。</p> 
<p>自 OpenSSH 8.9 以来的变化包括：</p> 
<h3>不兼容的变化</h3> 
<ul> 
 <li>这个版本将 scp 从使用传统的 scp/rcp 协议改为默认使用 SFTP 协议；传统的 scp/rcp 会通过远程 shell 对远程文件名进行通配符扩展（例如 "scp host:* ..."）。这会产生一个副作用，就是需要在文件名中对 shell 元字符进行双引号处理，否则它们可能被解释为远程的 shell 命令。而这就产生了一个潜在的不兼容的地方：scp(1) 在使用 SFTP 协议时，不再需要这种引号。而试图使用它可能会导致传输失败。</li> 
 <li>在不兼容的情况下，scp(1)客户端可以被使用 <code>-O</code> 标志来使用的传统 scp/rcp。</li> 
</ul> 
<h3>新功能</h3> 
<ul> 
 <li>ssh, sshd: 默认使用混合的 Streamlined NTRU Prime + x25519 密钥交换方法</li> 
 <li>sftp-server: 支持 "copy-data" 扩展以允许服务器端复制文件/数据</li> 
 <li>sftp: 增加了一个 "cp" 命令， 允许 sftp 客户端执行服务器端的文件拷贝</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>sshd: 在服务器监听/接受循环中打包 pollfd 数组，可能导致服务器在 MaxStartups > RLIMIT_NOFILE 时挂起/自旋</li> 
 <li>scp: 修复了参数 processing.bz3404 中的内存泄漏</li> 
 <li>sshd: 不要尝试在 sshd re-exec 路径中解析 ListenAddress 指令</li> 
 <li>sshd: 客户端使用未经批准或不支持的签名算法而拒绝公钥认证请求时，在日志信息中包括算法的名称，以使调试更加容易</li> 
 <li>……</li> 
</ul> 
<h3>其他</h3> 
<ul> 
 <li>sshd: 重构了特定平台的锁定账户检查</li> 
 <li>ssh, sshd: 修正可能出现的整数下溢</li> 
 <li>sshd: 提供 killpg 的实现</li> 
 <li>检查丢失的 ftruncate 原型</li> 
 <li>sshd: 在交叉编译时默认不使用沙盒</li> 
 <li>sshd: 在 seccomp 沙箱中允许 ppoll_time64，应该可以修复沙盒在某些 32 位 Linux 平台上的违规行为</li> 
 <li>改进对配置脚本中 -fzero-call-used-regs=all 支持的检测</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssh.com%2Freleasenotes.html%239.0" target="_blank">https://www.openssh.com/releasenotes.html#9.0</a></p>
                                        </div>
                                      
</div>
            