
---
title: 'Agileutil v0.0.12 发布，优化 TCP 传输，减少网络 IO 耗时！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7233'
author: 开源中国
comments: false
date: Sat, 03 Apr 2021 21:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7233'
---

<div>   
<div class="content">
                                                                                            <p>本次发布的版本是v0.0.12，针对TCP传输进行了优化，减少了网络IO等待时间。</p> 
<p>由于每次RPC请求的数据中会携带请求体长度字段，压缩标记字段，数据字段等二进制数据，在之前实现的send逻辑中，会针对不同的字段分批调用socket.sendall()。 经过测试，将数据组合后一次性调用socket.sendall()，单向请求会减少4倍的耗时，recv的等待时间明显变短。</p> 
<p>详情: <a href="https://gitee.com/lycclsltt/agileutil">https://gitee.com/lycclsltt/agileutil</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            