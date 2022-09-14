
---
title: 'Eoapi v1.7.0 发布：支持 Websocket 协议测试、插件管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eb70c6bfbd66440c67d4fe7e5ee2ee78349.png'
author: 开源中国
comments: false
date: Wed, 14 Sep 2022 09:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eb70c6bfbd66440c67d4fe7e5ee2ee78349.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div>
  距离上一次发布正式版本过了两周，这两周我们在攒一个大功能—— 
  <strong>支持 Websocket 协议测试！</strong>
 </div> 
 <div>
   
 </div> 
 <div>
  长期关注我们的共建者知道，这个功能预告了几万年，真不是我们拖延，是 API 协议实在太多了...
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="251" src="https://oscimg.oschina.net/oscnet/up-eb70c6bfbd66440c67d4fe7e5ee2ee78349.png" width="234" referrerpolicy="no-referrer">
 </div> 
 <div>
   
 </div> 
 <div>
  有些协议纵横互联网 20 年屹立不倒经久不衰，有些协议声音越来越微弱，还有新秀 gRPC、GraphQL 渐渐崭露头角。
 </div> 
 <div>
   
 </div> 
 <div>
  我们针对各种协议了调研，下图是调研的一部分。每种协议有不同的适用场景，分享给大家～
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="276" src="https://oscimg.oschina.net/oscnet/up-a6ccf41658be0b4e1c31dc794daff82049e.png" width="561" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:center">
   
 </div> 
 <div>
  在 Websocket 协议发布之前，浏览器只能单向通信，客户端可以联系服务端，但服务端不能主动联系客户端。
 </div> 
 <div>
   
 </div> 
 <div>
  在这种背景下，消息推送以及需要实时通信的聊天室等功能实现比较麻烦，机智的开发者们会一边骂骂咧咧一边哭着写轮询的代码，好生痛苦。
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="198" src="https://oscimg.oschina.net/oscnet/up-c76d93b8e8324b756dd902ca3010fcffd81.png" width="228" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:center">
   
 </div> 
 <div>
  Socket.IO 的诞世也是为了解决浏览器没有原生提供双向通信的方式，它为了支持长连接也是操碎了心，内置了好几种不同的降级方案。直到浏览器宣布原生支持 Websocket后，开发者乐开了花。
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img src="https://easy-open-link.feishu.cn/space/api/box/stream/download/asynccode/?code=NTU3YTk0YjVmZDA5ODJhYmFjNTliYTJlYjIzNzM2ZjVfN0s4RkNIQmxGVW03bVpQMm5Cc09OSGFIeHdGR25DU2dfVG9rZW46Ym94Y245MTdQdHQyTVQ4MDZyMHlCZkpxbXFTXzE2NjMxMTgyNTc6MTY2MzEyMTg1N19WNA" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:center">
   
 </div> 
 <div>
  Websocket 协议一直以来社区呼声都比较高，所以我们选择优先支持，
  <strong>大家可以升级到 v1.7.0 的 Eoapi 对它进行试用～</strong>
 </div> 
 <h1>Websocket 测试</h1> 
 <div>
  先上动图～
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt src="https://oscimg.oschina.net/oscnet/up-d78de38da6400dfb2c4724ab5d8498673e9.gif" referrerpolicy="no-referrer">
 </div> 
 <div>
   
 </div> 
 <div>
   
 </div> 
 <div>
  文字步骤：
 </div> 
 <ol start="1"> 
  <li> 
   <div>
    点击 Tab 加号选中 Websocket 协议
   </div> </li> 
 </ol> 
 <ol start="2"> 
  <li> 
   <div>
    输入地址后点击连接按钮就可以和服务端进行通信啦
   </div> </li> 
 </ol> 
 <ol start="3"> 
  <li> 
   <div>
    在 message 输入你想要发送的内容
   </div> </li> 
 </ol> 
 <ol start="4"> 
  <li> 
   <div>
    在返回 message 信息流中查看内容
   </div> </li> 
 </ol> 
 <div style="text-align:center">
  <img alt height="388" src="https://oscimg.oschina.net/oscnet/up-9a0f9dd6377c187cece2771ce19a64605f2.png" width="640" referrerpolicy="no-referrer">
 </div> 
 <div>
   
 </div> 
 <div>
   
 </div> 
 <div>
  测试结束后，还可以点击测试历史看到历史请求
 </div> 
 <div>
   
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="247" src="https://oscimg.oschina.net/oscnet/up-0ae408b6b8b3f059c1dfc1d52e752254657.png" width="640" referrerpolicy="no-referrer">
 </div> 
 <h1> </h1> 
 <h1>插件管理</h1> 
 <div>
  随着安装的插件越来越多，我们需要对插件进行管理，本次迭代优化了插件管理，增加了插件开发，插件配置等功能，话不多说，上图文：
 </div> 
 <div>
   
 </div> 
 <div>
  <strong>如果暂时不想这个插件生效？</strong>
 </div> 
 <div>
   
 </div> 
 <div>
  之前需要卸载，现在可以开关插件，控制粒度更精细，可以在保留插件配置的前提下不使用插件的功能。
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="203" src="https://oscimg.oschina.net/oscnet/up-17ed6fb84268c71b359b84423ef3abbbd0a.png" width="640" referrerpolicy="no-referrer">
 </div> 
 <div>
   
 </div> 
 <div>
  将插件配置放到每个插件的详情页，更好找更方便了～
 </div> 
 <div>
   
 </div> 
 <div style="text-align:center">
  <img alt height="370" src="https://oscimg.oschina.net/oscnet/up-53be9364a353f95e286c2f1e74879fb04ab.png" width="640" referrerpolicy="no-referrer">
 </div> 
 <h1> </h1> 
 <h1>预告</h1> 
 <div>
  后续计划支持功能：
 </div> 
 <ul> 
  <li> 
   <div>
    支持 HTTP API 测试用例
   </div> </li> 
 </ul> 
 <ul> 
  <li> 
   <div>
    插件支持 UI 控制
   </div> </li> 
 </ul> 
 <ul> 
  <li> 
   <div>
    更多协议支持
   </div> </li> 
 </ul> 
 <ul> 
  <li> 
   <div>
    ...
   </div> </li> 
 </ul> 
 <div> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">如果你对我们的项目有任何反馈或者建议，请在<span> </span><strong>Github<span> /Gitee </span></strong><span> </span>提个 issue</span></p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Gitee 地址：</strong>https://gitee.com/eolink_admin/eoapi</p> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Github 地址：</strong>https://github.com/eolinker/eoapi</p> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            