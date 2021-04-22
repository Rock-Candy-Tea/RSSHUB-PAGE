
---
title: 'Swoole v4.6.6 发布，Bug 修复版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8366'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 18:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8366'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fswoole-src%2Freleases%2Ftag%2Fv4.6.6" target="_blank">v4.6.6</a> 版本主要是一个 Bug 修复版本，没有向下不兼容改动。</p> 
<h2 style="text-align:left">更新日志</h2> 
<p style="text-align:left">下面是完整的更新日志：</p> 
<h3 style="text-align:left">增强</h3> 
<ul> 
 <li>支持在 FreeBSD 下 Master 进程退出后向 Manager 发送 SIGTERM 信号 (#4150) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevnexen" target="_blank">@devnexen</a>)</li> 
 <li>支持将 Swoole 静态编译到 PHP 中 (#4153) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatyhtf" target="_blank">@matyhtf</a>)</li> 
 <li>支持 SNI 使用 HTTP 代理 (#4158) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatyhtf" target="_blank">@matyhtf</a>)</li> 
</ul> 
<h3 style="text-align:left">修复</h3> 
<ul> 
 <li>修复同步客户端异步连接的错误 (#4152) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatyhtf" target="_blank">@matyhtf</a>)</li> 
 <li>修复 Hook 原生 curl multi 导致的内存泄漏 (swoole/swoole-src<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F91bf243" target="_blank">@91bf243</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatyhtf" target="_blank">@matyhtf</a>)</li> 
</ul>
                                        </div>
                                      
</div>
            