
---
title: '什么是全站加速DCDN？与CDN有什么区别？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/13085430-b6762caed7e4ce35.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/13085430-b6762caed7e4ce35.png'
---

<div>   
<p>WebSocket协议可以为网站和应用提供真正的双向通信，具有控制开销、保持连接状态、更强实时性、更好的压缩效果等优点，是当下低延时应用最常采用的一种技术协议。</p>
<h1>WebSocket的优势与应用</h1>
<p>HTML5定义 的WebSocket协议是基于TCP的一种新的网络协议。它实现了浏览器与服务器全双工(full-duplex)通信，即允许服务器主动发送信息给客户端。因此，WebSocket使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在WebSocket API中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。</p>
<p><strong>WebSocket能更好的节省服务器资源和带宽，并且能够更实时地进行通讯，它的优势：</strong></p>
<p><strong>• 较少的控制开销。</strong>在连接创建后，服务器和客户端之间交换数据时，用于协议控制的数据包头部相对较小。<br>
<strong>• 更强的实时性。</strong>由于协议是全双工的，所以服务器可以随时主动给客户端下发数据。相对于HTTP请求需要等待客户端发起请求服务端才能响应，延迟明显更少；即使是和Comet等类似的长轮询比较，其也能在短时间内更多次地传递数据。<br>
<strong>• 保持连接状态。</strong>与HTTP不同的是，Websocket需要先创建连接，这就使得其成为一种有状态的协议，之后通信时可以省略部分状态信息。而HTTP请求可能需要在每个请求都携带状态信息（如身份认证等）。<br>
<strong>• 更好的二进制支持。</strong>Websocket定义了二进制帧，相对HTTP，可以更轻松地处理二进制内容。<br>
<strong>• 可以支持扩展。</strong>Websocket定义了扩展，用户可以扩展协议、实现部分自定义的子协议。<br>
<strong>• 更好的压缩效果。</strong>相对于HTTP压缩，Websocket在适当的扩展支持下，可以沿用之前内容的上下文，在传递类似的数据时，可以显著地提高压缩率。</p>
<h3>WebSocket主要用于解决以下几个问题：</h3>
<p>一、 在线聊天速度慢，断开连接较快，不能更好的保持业务通讯<br>
二、 网页通讯信息更安全，连接更稳定<br>
三、 提供更高效的网页通讯<br>
四、 网络抖动带来的连接时断时续问题<br>
五、 访问打不开网页，需要刷新页面<br>
六、 同时在线人数多，如何实时推送所有用户<br>
七、 服务端支持WebSocket协议<br>
八、 如何降低带宽，保证成本</p>
<p>总之，如果你的应用需要提供多个用户相互交流，或者展示服务器端经常变动的数据，就十分需要使用WebSocket技术。</p>
<h1>WebSocket应用场景</h1>
<p>阿里云CDN服务全球30多万家客户，涵盖视频、教育、政府、游戏、金融、社交、电商等各大行业场景，其中有几个典型的业务场景，可以利用平台技术优势，更好地解决实时通讯业务需求。DCDN已经支持WebSocket协议，可以应用在以下场景之中：</p>
<h3>场景一：弹幕</h3>
<p>弹幕的流程是终端用户A在自己的客户端广播了一条信息，这条信息需要在与其他N个用户端发送的弹幕信息一并展示在A这边。它需要马上显示到屏幕上，对实时性要求极高。在今年S8赛事总决赛中，虎牙直播就采用全站加速WebSocket协议，更从容地应对2000万在线超高并发流量下更实时、更猛烈的互动考验。</p>
<h3>场景二：在线教育</h3>
<p>在线教育跨越了时空的限制，学生与老师进行一对多/一对一的在线授课，老师在客户端内编写的笔记、大纲、白板信息等信息，需要实时推送至多个学生的客户端，同时在课堂上，通话、文字聊天、实时解题等交互的实时性要求非常高，需要通过WebSocket协议来完成。</p>
<h3>场景三：金融产品实时信息查询</h3>
<p>股票价格瞬息万变，如果显示数据不及时，很有可能会影响用户的收益。需要通过WebSocket协议流式更新数据变化，将价格实时推送至世界各地的客户端，方便交易员迅速做出交易判断。</p>
<h3>场景四：体育实况更新</h3>
<p>由于全世界体育爱好者数量众多，比赛实况成为他们最为关心的热点。如果你是提供体育新闻类服务，WebSocket能够助力你的用户降低延时，获得实时的更新。</p>
<h3>场景五：视频会议和互动直播</h3>
<p>尽管视频会议并不能代替和真人相见，但是应用场景众多。而互动直播和视频会议中的连麦的服务对低延时的要求非常高。试想主播或者你的主管说了一句话后，你要10秒后才能听到，那你们是根本无法进行正常交流的 。WebSocket可以帮助两端或多端接入会议/直播的用户实时传递信息。</p>
<h3>全站加速DCDN</h3>
<p>阿里云自主研发的全站加速产品 DCDN（Dynamic Route for Content Delivery Network），是融合了动态加速和静态加速技术的 CDN 产品。该产品旨在提升动静态资源混合站点的访问体验，支持静态资源边缘缓存，动态内容最优路由回源传输，同时满足整体站点的全网访问速度及稳定性需求。一站式解决了页面动静态资源混杂、跨运营商、网络不稳定、单线源站、突发流量、网络拥塞等诸多因素导致的响应慢、丢包、服务不稳定的问题，提升全站性能和用户体验。全站加速构建于阿里云 CDN 平台之上，适用于动静混合型、纯动态型站点或应用的内容分发加速服务。</p>
<p>您可以通过以下架构图，了解全站加速的工作原理。<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="960" data-height="484"><img data-original-src="//upload-images.jianshu.io/upload_images/13085430-b6762caed7e4ce35.png" data-original-width="960" data-original-height="484" data-original-format="image/png" data-original-filesize="41272" src="https://upload-images.jianshu.io/upload_images/13085430-b6762caed7e4ce35.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">全站加速 DCDN 工作原理</div>
</div><br>
<strong>智能区分动静态内容：</strong>域名接入阿里云全站加速后，通过域名访问的动静态内容将被智能识别并区分。<br>
<strong>动静态内容同时加速：</strong>静态内容使用阿里云 CDN 加速，缓存在 CDN 节点上，供用户就近访问。动态内容通过智能路由优化、协议优化等动态加速技术快速回源获取。<p></p>
<p><strong>全站加速 DCDN 特点</strong><br>
<strong>便捷接入：</strong>站点无需动静态内容拆分加速，一键接入解决网络拥塞，提高访问成功率；<br>
<strong>智能加速：</strong>加速方案更智能，多种分发策略，边缘缓存、最优路由、压缩传输，访问效率提升 60%；<br>
<strong>稳定极速：</strong>1500+ 全球节点，120T 带宽能力，六大洲覆盖，国内主流运营商支持；<br>
<strong>内容安全：</strong>全链路加密传输，集成多种访问控制方式，增强源站防护能力，为文件，视频的传输保驾护航。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1674" data-height="540"><img data-original-src="//upload-images.jianshu.io/upload_images/13085430-0f231c3d278c767c.png" data-original-width="1674" data-original-height="540" data-original-format="image/png" data-original-filesize="111816" src="https://upload-images.jianshu.io/upload_images/13085430-0f231c3d278c767c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">CDN 与全站加速 DCDN 对比</div>
</div>
  
</div>
            