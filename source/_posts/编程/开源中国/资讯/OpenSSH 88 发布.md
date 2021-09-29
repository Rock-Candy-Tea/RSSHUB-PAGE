
---
title: 'OpenSSH 8.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=489'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=489'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">OpenSSH 是一个 100% 完整的 SSH 2.0 协议的实现，包括 sftp 客户端和服务器的支持。OpenSSH 8.8 的更新内容包括：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>ssh(1)：允许 ssh_config(5) CanonicalizePermittedCNAMEs 指令接受 "none" 参数，以指定默认的行为。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修正</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>scp(1): 当使用 SFTP 协议时，在发生传输错误后继续传输文件时，更好地匹配原始 scp/rcp 行为</li> 
 <li>ssh(1): 修正了多路复用中的一些内存泄漏问题</li> 
 <li>ssh-keygen(1): 避免在使用 -Y find-principals 命令时崩溃</li> 
 <li>一系列文档和手册的改进</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">可移植性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>ssh-agent(1): 在 FreeBSD 上，使用 procctl 禁用 ptrace(2)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fseclists.org%2Foss-sec%2F2021%2Fq3%2F187" target="_blank">https://seclists.org/oss-sec/2021/q3/18</a></p>
                                        </div>
                                      
</div>
            