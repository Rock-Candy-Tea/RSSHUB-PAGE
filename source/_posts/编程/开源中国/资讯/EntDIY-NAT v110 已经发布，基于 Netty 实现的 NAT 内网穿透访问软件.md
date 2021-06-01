
---
title: 'EntDIY-NAT v1.1.0 已经发布，基于 Netty 实现的 NAT 内网穿透访问软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5353'
author: 开源中国
comments: false
date: Mon, 31 May 2021 20:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5353'
---

<div>   
<div class="content">
                                                                    
                                                        <p>EntDIY-NAT v1.1.0 已经发布，这是一个基于 Netty 实现的 NAT 内网穿透访问软件。</p> 
<p>此版本更新内容包括：</p> 
<p>类似这种基于Netty的网络编程，最麻烦就是各种网络异常导致的程序问题排查，很难跟踪重现。尤其对于Server端Remote端口监听，如何合理的处理异常情况能维持正常的监听响应，同时又能在Client异常情况下及时释放Remote端口占用。</p> 
<p>几经反复调整和一段时间的试用，先发布一个版本：优先照顾Remote端口能在网络异常中断后能维持正常的监听响应处理。后续再持续优化Client断开情况下自动释放Server端Remote占用问题。</p> 
<p>详情查看：<a href="https://gitee.com/xautlx/entdiy-nat/releases/v1.1.0">https://gitee.com/xautlx/entdiy-nat/releases/v1.1.0</a></p>
                                        </div>
                                      
</div>
            