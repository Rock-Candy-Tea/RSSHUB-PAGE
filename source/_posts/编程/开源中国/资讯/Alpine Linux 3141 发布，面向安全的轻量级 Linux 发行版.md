
---
title: 'Alpine Linux 3.14.1 发布，面向安全的轻量级 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-175c6f0b38773043c6862ff6db47e257249.png'
author: 开源中国
comments: false
date: Fri, 06 Aug 2021 06:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-175c6f0b38773043c6862ff6db47e257249.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Alpine Linux 3.14.1 现已发布。此版本包含对 apk-tools CVE-2021-36159 的修复。</p> 
<p>Alpine Linux 是一个面向安全的轻量级 Linux 发行版，该发行版以安全为理念，面向 x86 路由器、防火墙、虚拟专用网、IP 电话盒及服务器而设计。另外，不同于常见的 Linux 发行版，Alpine Linux 采用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmusl-libc.org%2F" target="_blank">musl libc</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbusybox.net%2F" target="_blank">busybox</a> 以减小系统的体积和运行时资源消耗。在保持瘦身的同时，Alpine Linux 还提供了自己的包管理工具 apk，可以在其网站上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages" target="_blank">查询软件包</a>，或直接通过 apk 命令进行查询和安装。</p> 
<p>由于 Alpine Linux 占用空间非常小，因此它在容器环境中非常受欢迎。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-175c6f0b38773043c6862ff6db47e257249.png" referrerpolicy="no-referrer"></p> 
<p><strong>部分更新细节</strong></p> 
<ul> 
 <li>main/luajit：在 mips64 上禁用一些测试</li> 
 <li>main/luajit：修复 mips64 案例的测试套件路径</li> 
 <li>community/opendmarc：为 CVE-2021-34555 添加缓解措施</li> 
 <li>main/libretls：降级 libtls SOVERSION 以允许与 community/libressl 共存</li> 
 <li>main/libretls：添加 so:libtls.so.20 以过渡</li> 
 <li>main/zstd：由于 160 个线程导致的问题，禁用 32 位 arm 上的测试</li> 
 <li>community/xwayland：在 xorg-server-xwayland 上添加缺失的替换</li> 
 <li>community/discover：禁用 KCM</li> 
 <li>community/vectorscan：添加调试符号包</li> 
 <li>community/bareos：从 webui 子包中移除 py3-selenium dep</li> 
 <li>main/rsyslog：在标准规则之前加载自定义配置</li> 
 <li>main/fail2ban：删除其他发行版的路径配置</li> 
 <li>main/fail2ban：跳过失败的 DNSUtilsNetworkTests.testFQDN</li> 
 <li>community/java-jffi：由于缺少 java，在 mips64 上禁用</li> 
 <li>......</li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falpinelinux.org%2Fposts%2FAlpine-3.14.1-released.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            