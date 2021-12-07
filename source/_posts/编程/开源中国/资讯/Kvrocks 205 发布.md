
---
title: 'Kvrocks 2.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8461'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 11:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8461'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>GitHub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKvrocksLabs%2Fkvrocks%2Freleases%2Ftag%2Fv2.0.5" target="_blank">https://github.com/KvrocksLabs/kvrocks/releases/tag/v2.0.5</a></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Kvrocks  发布 v2.0.5 版本，开始支持 blob db 来减少大 key-value 场景的读写放大问题，同时也支持使用一些 RocksDB 的特性来优化读性能。另外，新版本也加入类似 CAS/CAD 相关命令来帮助用户更好的实现原子更新的功能，具体更新如下:</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span>新特性</span></strong></p> 
<hr> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:justify"><span>支持 zrevrangebylex 命令</span></li> 
 <li> <p style="margin-left:0; margin-right:0"><span>开始支持 blob db，在大 key-value 场景可以减少写放大问题。同时也使用一些 rocksdb 新特性来优化性能</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 CAS(Compare And Swap) 以及 CAD(Compare And Delete) 命令</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持使用 row cache 来优化读性能(需要手动开启)</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span>优化点</span></strong></p> 
<hr> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:justify"><span>增加 rocksdb ops 统计指标到 info 命令输出</span></li> 
 <li> <p style="margin-left:0; margin-right:0"><span>增加 maxclients 到 info 命令输出</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>增加 rocksdb write stall/stop 统计指标到 info 命令输出</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>根据 maxclients  和 rocksdb max open file 自动调整进程 max open file</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>调整 kvrocks2redis  迁移工具兼容带 slot id 的编码格式</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>同时，我们也基于 oliver006/redis_exporter 之上实现了 Kvrocks  的 metric exporter 工具，方便用户监控 Kvrocks。具体见:  </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUxNTg5NzM1Nw%3D%3D%26mid%3D2247483711%26idx%3D1%26sn%3D178fd68b054c0a7f8eb751e285baa009%26chksm%3Df9aee05dced9694b75712f04af38800532d36abee876164b9644192aefa34be45f1108d67d53%26scene%3D21%23wechat_redirect" target="_blank"><span>Kvrocks 发布 Exporter 工具</span></a></p>
                                        </div>
                                      
</div>
            