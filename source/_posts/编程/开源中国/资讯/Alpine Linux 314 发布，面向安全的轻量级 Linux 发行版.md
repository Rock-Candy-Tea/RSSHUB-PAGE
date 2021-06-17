
---
title: 'Alpine Linux 3.14 发布，面向安全的轻量级 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2019/0514/192224_JlOT_2720166.png'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 23:49:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2019/0514/192224_JlOT_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falpinelinux.org%2Fposts%2FAlpine-3.14.0-released.html" target="_blank">Alpine Linux 3.14.0 已发布</a>，此版本是 3.14 系列的首个更新。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falpinelinux.org%2Fdownloads%2F" target="_blank">https://alpinelinux.org/downloads/</a></p> 
<p>Alpine Linux 是一个面向安全的轻量级 Linux 发行版，该发行版以安全为理念，面向 x86 路由器、防火墙、虚拟专用网、IP 电话盒及服务器而设计。另外，不同于常见的 Linux 发行版，Alpine Linux 采用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmusl-libc.org%2F" target="_blank">musl libc</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbusybox.net%2F" target="_blank">busybox</a> 以减小系统的体积和运行时资源消耗。在保持瘦身的同时，Alpine Linux 还提供了自己的包管理工具 apk，可以在其网站上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages" target="_blank">查询软件包</a>，或直接通过 apk 命令进行查询和安装。</p> 
<p>由于 Alpine Linux 占用空间非常小，因此它在容器环境中非常受欢迎。</p> 
<p><img src="https://static.oschina.net/uploads/space/2019/0514/192224_JlOT_2720166.png" referrerpolicy="no-referrer"></p> 
<p>Alpine Linux 3.14 更新内容：</p> 
<p><strong>新特性和值得关注的新软件包</strong></p> 
<ul> 
 <li>Lua 5.4.3</li> 
</ul> 
<p><strong>重要软件升级</strong></p> 
<ul> 
 <li>HAProxy 2.4.0</li> 
 <li>KDE 21.04.2</li> 
 <li>nginx 1.20.0 and njs 0.5.3</li> 
 <li>Node.js 14.17.0</li> 
 <li>Plasma 5.22.0</li> 
 <li>PostgreSQL 13.3</li> 
 <li>Python 3.9.5</li> 
 <li>R 4.1.0</li> 
 <li>QEMU 6.0.0</li> 
 <li>XEN 4.15.0</li> 
 <li>Zabbix 5.4.1</li> 
</ul> 
<p><strong>更新说明</strong></p> 
<ul> 
 <li>由于缺乏长期的上游支持，ClamAV 已迁移至社区</li> 
 <li>LuaJIT 包已经从无人维护的 MoonJIT 分支切换到 OpenResty 的维护分支</li> 
 <li>NGINX 包将 vhost 配置的默认目录从<code>/etc/nginx/conf.d</code>更改为<code>/etc/nginx/http.d</code></li> 
 <li>collectd 包已被拆分为插件的子包</li> 
 <li>Node.js npm 包已迁移到独立端口</li> 
 <li>在 nftables 中，echo-r​​equest 的速率限制已从默认规则集中删除</li> 
 <li>由于许多测试失败，fail2ban 暂时被禁用。作为替代方案，可以使用 sshguard</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falpinelinux.org%2Fposts%2FAlpine-3.14.0-released.html" target="_blank">详情查看发布公告</a>。</p> 
<ul> 
</ul>
                                        </div>
                                      
</div>
            