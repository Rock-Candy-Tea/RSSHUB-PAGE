
---
title: 'OpenSSH 8.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5397'
author: 开源中国
comments: false
date: Sun, 27 Feb 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5397'
---

<div>   
<div class="content">
                                                                                            <p>OpenSSH 是一个 100% 完整的 SSH 2.0 协议的实现，包括 sftp 客户端和服务器的支持。OpenSSH 8.9 的更新内容包括：</p> 
<h3>新功能</h3> 
<ul> 
 <li>ssh(1), sshd(8), ssh-add(1), ssh-agent(1): 增加了一个用于限制转发和使用添加到 ssh-agent(1) 的密钥的系统</li> 
 <li>ssh-keygen(1): 当从 FIDO token 下载常驻密钥时，传回创建密钥时使用的用户 ID，并将其附加到密钥被写入的文件名中</li> 
 <li>ssh-keygen(1), ssh(1), ssh-agent(1): 更好地处理 FIDO 密钥，以在设备本身上提供用户验证（UV）</li> 
 <li>ssh-keygen(1): 增加了 "ssh-keygen -Y match-principals" 的操作</li> 
 <li>ssh-add(1), ssh-agent(1): 允许将 pin-required FIDO 密钥添加到 ssh-agent(1)</li> 
 <li>ssh-keygen(1): 允许在 sshsig 签名时选择哈希值</li> 
 <li>ssh(1), sshd(8): 直接读取网络数据到数据包输入的缓冲区，而不是通过一个小的堆栈缓冲区间接地读取网络数据</li> 
 <li>ssh(1), sshd(8): 直接读取数据到通道输入缓冲区</li> 
 <li>ssh(1): 扩展了 PubkeyAuthentication 的配置指令，以便接受 yes|no|unbound|host-bound</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>sshd(8): 记录了 CASignatureAlgorithms、ExposeAuthInfo 和 PubkeyAuthOptions 可以在一个 Match 块中使用</li> 
 <li>sshd(8): 修复构建路径到具有很长用户主目录名称的 .rhosts/.shosts 文件时，可能产生的字符串截断</li> 
 <li>ssh(1): 当 SessionType=none 时，不要把 TTY 放到 raw 模式</li> 
 <li>scp(1): 修正了 SFTP 模式下处理 ~-前缀路径时的一些错误</li> 
 <li>ssh(1): 允许 ssh(1) 当只有 RSA/SHA2 签名算法时选择 RSA 密钥</li> 
 <li>ssh-keysign(1): 使 ssh-keysign 使用请求的签名算法，而不是默认的签名算法</li> 
 <li>ssh(1): 在客户端有更严格的 UpdateHostkey 签名验证逻辑</li> 
 <li>ssh-keygen(1): 使得 sshsig 验证时间参数的解析成为可选项</li> 
 <li>sshd(8): 修正 rhosts/shosts 路径结构中的截断</li> 
 <li>ssh(1), sshd(8): 更正 IPTOS_DSCP_LE 的值</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fseclists.org%2Foss-sec%2F2022%2Fq1%2F156" target="_blank">https://seclists.org/oss-sec/2022/q1/156</a></p>
                                        </div>
                                      
</div>
            