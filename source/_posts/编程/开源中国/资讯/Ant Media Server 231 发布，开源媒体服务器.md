
---
title: 'Ant Media Server 2.3.1 发布，开源媒体服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7138'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7138'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Media Server 旨在为直播视频流技术基础架构提供超低延迟（WebRTC）和低延迟（HLS，CMAF 在 v2.2 + 中可用）。它可以用于将任何类型的实时或点播视频流传输到任何设备，包括手机、PC 或 IPTV 盒子。</p> 
<p>Ant Media Server 2.3.1 正式发布，本次更新内容如下：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F6072c28834360068e86fdfb33cb4de908bfb38f1" target="_blank">6072c288</a> 修复发送统计信息中的应用程序投放问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F7684ab4688555873ac4edd2fffb8ebc16ef15125" target="_blank">7684ab46</a> 为 macOS 添加本机库；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F1f905b527b28fc19ef7b9d7c2fd3da36097bbe6f" target="_blank">1f905b52</a> 通过修复 rtp 时间戳比例来构建本机库；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F7a2f2fa53c1657f2c3198df26d5023fccca83ade" target="_blank">7a2f2fa5</a> 创建用于访问工作者队列大小的公共方法；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F2d0cf8932b04c429c34e87ac263af970a80c2404" target="_blank">2d0cf893</a> 使结果处理程序为空；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Fc84659d5bf58d97818600d220d35e271c3df6435" target="_blank">c84659d5</a> 默认 CPU 限制更改为 75%；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F8daf2ab4264b7be8043eedfe48c1ffa494c1d5c3" target="_blank">8daf2ab4</a> 使用 http11nio2 协议而不是 apr；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Fbf31ae865128dbd3a0b2f00da7e3913c3d7694c1" target="_blank">bf31ae86</a> 检查 CMAF 超时和错误值；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F92e93b075119c408bda64a26ecef3110121d0877" target="_blank">92e93b07</a> 修复集群中的应用删除；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F0cfa3016e388687c7aa38040c702f8499137df83" target="_blank">0cfa3016</a> 恢复为 librtmp style live = 1；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Fecf3e757cf14a42a883e06fbd5eb897fdf1e7c65" target="_blank">ecf3e757</a> 通过群集通知程序更新应用程序设置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F916afc84a4bfbbbc348bd6f694c913d4d4869c2d" target="_blank">916afc84</a> 在 ChunkTransferServlet 中更改日志级别；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Ff3544afbf6847a543c95f9ec730abe413d1c188c" target="_blank">f3544afb</a> 使用 librtmp 方式修复实时播放；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F76a4b101b1f0f67dc4b56abdfa5a8107ea557b7f" target="_blank">76a4b101</a> 将最大工作时间延长至10秒；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F38d668a214e390e7c138627062ae30d58c122154" target="_blank">38d668a2</a> 增加 tomcat 中的线程数；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Fbae7aff34997987eaea0082f5fd623e73519fcfb" target="_blank">bae7aff3</a> 使用 sudo 运行 create app 脚本；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F75fc3af7a989902d54743bbc2aaac21cca2e6c97" target="_blank">75fc3af7</a> 改善 rtmp 摄取分析持续时间测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2Fc13de97a24ad290807b27e8a6ebb9e763113cf15" target="_blank">c13de97a</a> 修复测试的安装位置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F10dddb8a1be99d8e0ab9751cff35d7baeae0ff08" target="_blank">10dddb8a</a> 修复参数问题和写入测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F1e3584e2863d2429f14996cf257bd613e7efc1e9" target="_blank">1e3584e2</a> 删除冗余测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Fcommit%2F59cdec7650ca04e381c2a77540f9ca8a44c9f09b" target="_blank">59cdec76</a> 调整测试代码并添加新的测试代码；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-media%2FAnt-Media-Server%2Freleases%2Ftag%2Fams-v2.3.1" target="_blank">https://github.com/ant-media/Ant-Media-Server/releases/tag/ams-v2.3.1</a></p>
                                        </div>
                                      
</div>
            