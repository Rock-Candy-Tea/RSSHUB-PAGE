
---
title: '着力于应对未来量子计算机挑战的OpenSSH 9.0已经发布'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0408/bafabc77ff175ca.jpg'
author: cnBeta
comments: false
date: Fri, 08 Apr 2022 10:36:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0408/bafabc77ff175ca.jpg'
---

<div>   
OpenSSH 9.0作为广泛使用的、开源的SSH实现的最新版本今天已经上线。OpenSSH 9.0带来了新的功能和变化，如scp默认使用SFTP协议。OpenSSH 9.0是一个重要的版本，它带来了一些明显的变化。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0408/bafabc77ff175ca.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>首先，OpenSSH 9.0将scp从使用传统的SCP/RCP协议改为现在默认使用SFTP协议。这是OpenSSH一直在努力实现的一个变化，在之前的版本中为scp工具在内部使用SFTP奠定了基础。</p><p>另一个值得注意的变化是OpenSSH 9.0 SSH/SSHD默认使用混合的Streamlined NTRU Prime + x25519密钥交换方法，以抵御未来量子计算机的攻击。OpenSSH开发者现在做这个改变是为了提高安全性，以抵御"现在捕获，以后解密"的攻击，一旦有量子计算机有能力解密捕获的SSH密码文本。</p><p>OpenSSH 9.0的一个相当有用的变化是，sftp-server实现增加了对copy-data扩展的支持，以支持服务器端的文件/数据拷贝。sftp工具还增加了一个"cp"命令，允许SFTP客户端对服务器端的文件进行复制。</p><p>OpenSSH 9.0通过一些可移植性的改进、各种bug的修复和其他改进来完善。</p><p>关于OpenSSH 9.0的下载和更多细节请访问<a href="https://www.openssh.com/" target="_blank">OpenSSH.com</a>。</p>   
</div>
            