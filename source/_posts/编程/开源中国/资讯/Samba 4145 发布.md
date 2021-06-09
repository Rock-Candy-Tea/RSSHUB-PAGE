
---
title: 'Samba 4.14.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8082'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 06:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8082'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Samba 是用于 Linux 和 Unix 的标准 Windows 互操作性程序套件。自 1992 年以来，Samba 为所有使用 SMB/CIFS 协议的客户提供了安全、稳定和快速的文件和打印服务。Samba 是将 Linux/Unix 服务器和桌面无缝集成到活动目录环境中的一个重要组件。</p> 
<p>Samba 4.14.5 发布，该版本更新内容如下：</p> 
<ul> 
 <li>s3: smbd: SMB1 SMBsplwr 在成功时不发送回复数据包；</li> 
 <li>s3: smbd: 确保 POSIX 默认 ACL 被映射到返回用于目录句柄的 Windows ACL；</li> 
 <li>s3: smbd: 修复当与 vfs_shadow_copy2() 一起使用时在 process_symlink_open() 中读取未初始化的内存；</li> 
 <li>docs：扩展审计日志的 "日志级别" 文档；</li> 
 <li>smbd：正确初始化关闭时间戳字段；</li> 
 <li>修复 gcc11 编译器问题；</li> 
 <li>docs-xml：更新 smbcacls 联机帮助页；</li> 
 <li>docs：更新 rpcclient 中可用命令的列表；</li> 
 <li>ctdb：修复了 run_proc_signal_handler() 中的崩溃；</li> 
 <li>s3:winbind: 对于 'security = ADS' 需要 realm/workgroup 设置；</li> 
 <li>lib:replace：不要使用 gcc 11 或更新版本构建 strndup 测试；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.samba.org%2Fsamba%2Fhistory%2Fsamba-4.14.5.html" target="_blank">https://www.samba.org/samba/history/samba-4.14.5.html</a></p>
                                        </div>
                                      
</div>
            