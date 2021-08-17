
---
title: 'OpenResty 1.19.9.1 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7028'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 06:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7028'
---

<div>   
<div class="content">
                                                                                            <p>OpenResty 1.19.9.1 已正式发布，此版本包含了过去几个月所有的优化、bug 修复和新特性。</p> 
<ul> 
 <li>底层基于较新的 nginx 主线版本 1.19.9</li> 
 <li>从上游 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenresty%2Fluajit2%23readme" target="_blank">LuaJIT</a> 仓库引入了许多错误修复程序</li> 
 <li>引入新的宏<code>LUAJIT_TEST_FIXED_ORDER</code>用于 lua 表的固定 (fixed-order) 顺序遍历</li> 
 <li>当 lua 请求内存失败时，会采取调用<code>abort()</code>的方式来处理，而不是进行关闭</li> 
 <li><code>get_ctx_table</code>支持使用来自调用者的 ctx 表，可降低创建新 ctx 表的成本</li> 
 <li>修复使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenresty%2Flua-tablepool" target="_blank">lua-tablepool</a> 清除 lua table 内容时，metatable 没有被清除的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenresty%2Flua-tablepool" target="_blank">问题</a></li> 
 <li>为了在使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenresty%2Flua-tablepool" target="_blank">lua-tablepool</a> 时获得更好性能，当内存池的大小大于 max_pool_size 时丢弃对象</li> 
 <li>针对 stream 子系统实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenresty%2Flua-resty-core%2Fblob%2Fmaster%2Flib%2Fngx%2Fprocess.md" target="_blank"><code>ngx.process</code></a>API</li> 
</ul> 
<p>此外，官方新增了 alpine 3.14 的 x86_64 和 arm64 的官方包仓库：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenresty.org%2Fcn%2Flinux-packages.html" target="_blank">https://openresty.org/cn/linux-packages.html</a></p> 
<p>完整的发布公告：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenresty.org%2Fcn%2Fann-1019009001.html" target="_blank">https://openresty.org/cn/ann-1019009001.html</a></p> 
<p>下载地址：<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenresty.org%2Fcn%2Fdownload.html" target="_blank">https://openresty.org/cn/download.html</a></p>
                                        </div>
                                      
</div>
            