
---
title: '高性能分布式文件系统 FastCFS V2.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8487'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 00:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8487'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FastCFS V2.3.0发布，主要改进如下：<br>     1. auth server以主备方式支持多节点，避免单点；<br>     2. leader/master选举/切换引入超时机制，选举时长可控；<br>     3. 网络通信相关改进：<br>        1）握手失败，server端主动断开连接；<br>        2）cluster内部通信server端超时控制；<br>        3）调整网络通信超时默认值（连接超时由10秒调整为2秒，收发数据超时由30秒调整为10秒）。</p> 
<p>另配置文件中的 section name统一用减号分隔，例如：[pool-generate]</p>
                                        </div>
                                      
</div>
            