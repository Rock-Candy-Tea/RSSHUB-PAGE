
---
title: 'Ubuntu 22.10正优化OpenSSH服务器内存使用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0828/c02c68f541cbb3e.webp'
author: cnBeta
comments: false
date: Sun, 28 Aug 2022 00:07:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0828/c02c68f541cbb3e.webp'
---

<div>   
<strong>为减少 Ubuntu Linux 的系统内存占用，尤其是针对服务器和容器/云用例，Ubuntu 22.10 的 OpenSSH 服务器已切换到使用基于套接字的激活（socket-based activation）</strong>。Ubuntu 22.10 的 OpenSSH 守护程序未来只有在接收到即将到来的连接请求之后启动，而不是在任何连接请求都会运行 SSHD。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0828/c02c68f541cbb3e.webp" alt="5w6frg65.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">通过在有传入连接请求之前不运行 OpenSSH 守护程序，可以节省了大约 3MB 的系统内存，对于轻量级 VM/LXD 容器，对于空闲的全新 Ubuntu 22.10 容器来说，这可能是大约 5% 的内存使用量。</p><p style="text-align: left;">SSH 服务器切换到“基于套接字的激活”，是为了在 Ubuntu Server 前端进一步对 Ubuntu Linux 进行简化，特别是对于虚拟机和容器场景。 Canonical 的长期 Ubuntu 工程师 Steve Langasek 指出：</p><blockquote style="text-align: left;"><p style="text-align: left;">在 Canonical，我们非常关心让 Ubuntu 在您的硬件和云中尽可能高效，这就是为什么这项更改已作为减少镜像的默认内存占用的更大努力的一部分。发布时默认的 Ubuntu 22.04 LXD 映像使用了 65MiB 的 RAM，在这次 OpenSSH 更改之后，动力学现在使用 58MiB；更多改进正在进行中，旨在将更安全的更改向后移植到我们的 Ubuntu 22.04 映像，以提高最大数量用户的内存使用率。</p></blockquote>   
</div>
            