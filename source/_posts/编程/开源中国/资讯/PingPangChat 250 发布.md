
---
title: 'PingPangChat 2.5.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9100f66b1868579215e599e8bc9f4644882.png'
author: 开源中国
comments: false
date: Sun, 18 Apr 2021 14:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9100f66b1868579215e599e8bc9f4644882.png'
---

<div>   
<div class="content">
                                                                                            <p>1.再这之前的版本，直播采用的实现方式是通过<span style="background-color:#ffffff; color:#333333">node的peerjs服务器webrtc</span>实现的。</p> 
<p>2.在2.3和之前的版本视频聊天也是采用的peerjs实现的，</p> 
<p>  在2.4开始视频聊天采用了数据转发的方式。</p> 
<p>  在2.5这个版本直播也采用数据转发的方式实现。</p> 
<p>  这样做主要是对peerjs的不熟悉，只会搭建个环境。</p> 
<p>  对于采用数据转发的原因是因为对于后面数据信息可控可能节省点时间，还有时间不足只有周末才有时间调试。</p> 
<p> 为了实现直播数据转发页面在切换接收数据源有明显的卡顿现象，最后采用了在视频切换的时候添加了当前帧的图片作为封面，前端对我来说太难了。</p> 
<p>3.效果图</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-9100f66b1868579215e599e8bc9f4644882.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">4.<a href="https://gitee.com/0X00000000/PingPangChat">欢迎star和建议</a></span></strong></p>
                                        </div>
                                      
</div>
            