
---
title: 'Mozi.Network 1.4.7 发布，初步实现 RTSP'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8775'
author: 开源中国
comments: false
date: Sat, 30 Jul 2022 16:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8775'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mozi.Network 是基于.Net 开发的<span>网络应用协议基础组件。包含 HTTP 服务器，IoT 服务端和客户端项目等网络通讯协议。</span></p> 
<p>经过一个多月的艰苦努力，终于初步实现了RTSP协议(<strong>RTP over RTSP</strong>)，目前相关功能还只能进行测试，不能用于实用。由于协议涉及的内容比较多，项目中还有一些逻辑需要清理，一些功能需要增强。下一个开发周期将会完善RTSP相关功能，使其具备实用性。</p> 
<p> </p> 
<p>RTSP是实时流传输协议，广泛应用于流媒体传输，视频监控等领域。</p> 
<p>计划实现如下功能：</p> 
<p>1，RTSP服务端TCP模式</p> 
<p>2，RTSP服务端UDP模式</p> 
<p>3，RTSP客户端</p> 
<p>4，RTP转FLV</p> 
<p>5，H264,AAC媒体文件相关功能</p> 
<p>同时新版本中有如下更新：</p> 
<p>解决简易注册接口ApiHandler触发不正确的问题<br> 改ApiHandler的返回值为object，使用来更灵活<br> 移动UUID到HttpEmbedded<br> 解决HttpClient响应获取不完整的问题<br> 优化HttpServer会话断开链接策略<br> 在SocketServer中增加几个方法<br> 解决Digest认证的BUG中的URI识别问题</p> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            