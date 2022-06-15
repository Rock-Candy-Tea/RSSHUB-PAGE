
---
title: 'Golang 实现的远程桌面 Vnc 代理组件 Vprix-VncProxy发布 v1.0.0 稳定版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7315'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 10:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7315'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <h3 style="margin-left:0; margin-right:0">软件简介</h3> 
</div> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <p style="margin-left:0; margin-right:0">VprixVncProxy 是 Golang 实现的 Vnc 远程桌面代理组件，完全解析 rfb 协议，支持远程桌面代理，rbs 文件录屏，rbs 文件回放，截图，录制视频。</p> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>全协议支持的 VncProxy。 
    <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
     <li>支持 Tcp 代理</li> 
     <li>支持 WebSocket 代理</li> 
    </ul> </li> 
   <li>支持远程桌面操作保存为<span> </span><strong>rbs</strong><span> </span>文件。</li> 
   <li>支持使用<span> </span><strong>rbs</strong><span> </span>文件作为重播服务，通过 vnc 客户端连接 player 服务，回放远程桌面的操作。</li> 
   <li> <p style="margin-left:0; margin-right:0">支持实时录制视频。</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持通过<span> </span><strong>rbs</strong><span> </span>文件录制视频</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持屏幕截图</p> </li> 
  </ul> 
  <h2 style="margin-left:0; margin-right:0">应用场景</h2> 
  <ul> 
   <li>远程桌面中间人角色，可以进行审计。</li> 
   <li>需要对远程桌面更多权限控制的场景。</li> 
   <li>内网隔离场景</li> 
  </ul> 
  <h2 style="margin-left:0; margin-right:0">组件说明</h2> 
  <h4 style="margin-left:0; margin-right:0">Proxy</h4> 
  <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
   <li>启动 `server` 接受 `vnc viewer` 的链接.</li> 
   <li> 启动 `client` 连接到指定的 `vnc server`.</li> 
   <li> 为 `vnc viewer` 和 `vnc server` 之间建立起消息转发通道。</li> 
   <li> 因为 `rfb` 协议被完全解析，可以针对通信的消息进行转发处理，产生了后续的功能。</li> 
  </ol> 
  <h4 style="margin-left:0; margin-right:0">Recorder</h4> 
  <p style="margin-left:0; margin-right:0">1. 启动 `client` 连接到指定的 `vnc server`.<br> 2. 发送帧缓冲区更新消息 `FramebufferUpdateRequest` 到 `vnc server`。<br> 3. 处理 `vnc server` 回复的界面更新消息 `FramebufferUpdate`。<br> 4. 把这一过程以 `rbs` 文件格式记录下来。</p> 
  <h4 style="margin-left:0; margin-right:0">Player</h4> 
  <p style="margin-left:0; margin-right:0">1. 启动 `server` 接受 `vnc viewer` 的链接.<br> 2. 读取 `rbs` 文件，并按格式生成 `FramebufferUpdate` 消息发送给 `vnc viewer`。<br> 3. `vnc viewer` 的界面就会回放动作。</p> 
  <h4 style="margin-left:0; margin-right:0">Screenshot</h4> 
  <p style="margin-left:0; margin-right:0">1. 支持 `Proxy`,`Recorder` 和 `rbs` 文件作为输入源。<br> 2. 把当前的界面视图转换为图片文件。</p> 
  <h4 style="margin-left:0; margin-right:0">Video</h4> 
  <p style="margin-left:0; margin-right:0">1. 支持 `Proxy`,`Recorder` 和 `rbs` 文件作为输入源。<br> 2. 把 `FramebufferUpdate` 消息转换为视频文件。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            