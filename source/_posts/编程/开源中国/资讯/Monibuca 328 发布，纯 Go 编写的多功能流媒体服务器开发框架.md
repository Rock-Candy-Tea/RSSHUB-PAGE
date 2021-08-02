
---
title: 'Monibuca 3.2.8 发布，纯 Go 编写的多功能流媒体服务器开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7617'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 09:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7617'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">软件介绍</p> 
<p style="text-align:left">Monibuca（m7s） 是一个开源的流媒体服务器开发框架，适用于快速定制化开发流媒体服务器。</p> 
<ul> 
 <li style="text-align:left">采用纯Go编写，兼具性能和效率以及跨平台（包括嵌入式），二次开发不二选择，转发机制使用自研的环形链表+无锁读写，并全部开源</li> 
 <li style="text-align:left">独创的插件机制，极具扩展性和定制化能力，插件之间几乎没有任何耦合，可以自由组合，实现特定功能</li> 
 <li style="text-align:left">丰富的官方插件实现了不同协议之间的互通，包括rtmp、rtsp、hls、http-flv、gb28181、webrtc等</li> 
 <li style="text-align:left">官方提供编译好的二进制文件（Win、Mac、Linux）下载，一键部署，无需安装额外软件，无需docker</li> 
 <li style="text-align:left">默认UI嵌入可执行文件中，无需nginx也可直接访问管理后台，本地测试和线上使用均十分方便</li> 
</ul> 
<p style="text-align:left">3.2.8更新内容：</p> 
<ol> 
 <li style="text-align:left">引擎项目开源许可修改为MIT</li> 
 <li style="text-align:left">引擎转发逻辑升级，去除WaitGroup，进一步提高性能</li> 
 <li style="text-align:left">rtsp支持h265、pcma、pcmu</li> 
 <li style="text-align:left">rtsp支持拉流播放</li> 
 <li style="text-align:left">gb28181支持变相使用子码流（需要rtsp插件配合）</li> 
 <li style="text-align:left">rtp包解析支持B帧</li> 
</ol>
                                        </div>
                                      
</div>
            