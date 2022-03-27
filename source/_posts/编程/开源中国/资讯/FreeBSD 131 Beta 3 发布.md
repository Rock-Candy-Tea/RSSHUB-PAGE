
---
title: 'FreeBSD 13.1 Beta 3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0327/070427_sKbG_4937141.png'
author: 开源中国
comments: false
date: Sun, 27 Mar 2022 07:04:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0327/070427_sKbG_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FreeBSD 13.1 发布周期的第三个 Beta 版本现已推出，自 Beta 2 以来的更改内容包括：</p> 
<p><img alt height="217" src="https://static.oschina.net/uploads/space/2022/0327/070427_sKbG_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>默认启用了 REPRODUCIBLE_BUILD 选项</li> 
 <li>对 USB 子系统的各种更新和修复</li> 
 <li>解决了 newfs(8) 中 sblock.fs_maxbsize 初始化的一个错误</li> 
 <li>对 lindebugfs 的更新和修复</li> 
 <li>删除了 libcxxrt 中不必要的兼容性修正</li> 
 <li>实现了对 compiler-rt 的编译时修改</li> 
 <li>OpenSSL 已经更新到了 1.1.1n 版本</li> 
 <li>解决了在 src.conf(5) 中定义 WITHOUT_BOOT 时的一个构建时修复问题</li> 
 <li>对 virtio_random(4) 进行了修正， 以避免出现死锁</li> 
 <li>对 if_epair(4) 进行了构建修复</li> 
 <li>闰秒文件已经更新到了 3676924800 版本</li> 
 <li>时区数据库已经更新到了 2022a 版本</li> 
 <li>修正了 vga(4) 和 vt(4) 有可能导致没有视频/控制台输出的问题</li> 
 <li>更新了 arm64 的特定代码， 使 get_pcpu() 成为一个函数</li> 
 <li>支持从 ZFS 文件系统中自动加载解密密钥</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freebsd.org%2Farchives%2Ffreebsd-snapshots%2F2022-March%2F000073.html" target="_blank">https://lists.freebsd.org/archives/freebsd-snapshots/2022-March/000073.html</a></p> 
<p>下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.freebsd.org%2Fftp%2Freleases%2FISO-IMAGES%2F13.1%2F" target="_blank">https://download.freebsd.org/ftp/releases/ISO-IMAGES/13.1/</a></p>
                                        </div>
                                      
</div>
            