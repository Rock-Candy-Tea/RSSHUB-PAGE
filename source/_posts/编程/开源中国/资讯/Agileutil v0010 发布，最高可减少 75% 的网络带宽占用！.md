
---
title: 'Agileutil v0.0.10 发布，最高可减少 75% 的网络带宽占用！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7877'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 20:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7877'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次发布的版本是v0.0.10。 由于RPC服务端、客户端在数据传输前进行了序列化，程序内的对象或数据结构被序列化为二进制，对二进制数据压缩可减少网络带宽占用，减少网络IO。因此一直想支持数据压缩的功能。如何选取一种更适合的压缩方式呢？于是在几种压缩方式中进行了对比测试。通过测试，选取了数据压缩性价比最高的lz4压缩方式，淘汰gzip, zib。</p> 
<p>v0.0.10版本中，RPC客户端、服务端在收发数据过程中会自动进行压缩、解压缩（添加了一个标志位用于标记本次TCP/UDP/HTTP传输的数据中，是否进行了压缩，对应的一端，做解压缩处理）。默认大于4k的数据传输时，会自动开启压缩（如果传输数据较少，实际压缩后的二进制大小有可能会比原数据更大，这是不符合预期的。因此不是所有的数据都会压缩），经过测试，最高可减少1/4的网络流量，10kB数据压缩至2.5KB左右，并且在压缩后数据大小不相上下的情况下，lz4的压缩性能是gzip, zlib的10倍左右！</p> 
<p style="text-align:left">详情</p> 
<ul> 
 <li style="text-align: left;"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flycclsltt%2Fagileutil" target="_blank">Github</a></li> 
 <li><a href="https://gitee.com/lycclsltt/agileutil">Gitee</a>   </li> 
</ul>
                                        </div>
                                      
</div>
            